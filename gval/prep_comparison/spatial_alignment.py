# spatial_alignment.py
"""
Functions to check for and ensure spatial alignment of two xarray DataArrays

# To-Do
- make functions that check indices
"""

# __all__ = ['a', 'b', 'c']
__version__ = '0.0.0.0'
__author__ = 'Fernando Aristizabal'

from typing import (
    Any,
    Dict,
    Hashable,
    Iterable,
    List,
    Literal,
    Mapping,
    Optional,
    Tuple,
    Union,
)

import xarray 
import rioxarray as rxr
import dask
from rasterio.enums import Resampling

def matching_crs(
    candidate_map: xarray.DataArray,
    benchmark_map: xarray.DataArray,
    ) -> bool:
    """ Checks candidate and benchmark maps for matching crs's """

    match = candidate_map.rio.crs == benchmark_map.rio.crs

    return(match)

def matching_indices(
    candidate_map: xarray.DataArray,
    benchmark_map: xarray.DataArray
    ) -> bool:
    """ Checks for matching indices in candidate and benchmark maps """
    
    # floating point error?
    match = candidate_map.rio.indices == benchmark_map.rio.indices

    return(match)

def transform_bounds(
    candidate_map: xarray.DataArray,
    benchmark_map: xarray.DataArray,
    target_map: Optional[Union[xarray.DataArray,str]] = None,
    dst_crs: Optional[str] = None
    ) -> Tuple[Tuple[float, float, float, float],Tuple[float, float, float, float]]:
    """ Transforms bounds of xarray datasets to target map or desired crs """


    # already matching crs's
    if matching_crs(candidate_map, benchmark_map): 
        return(candidate_map.rio.bounds(), benchmark_map.rio.bounds())
    
    # match candidate to benchmark
    elif isinstance(target_map,xarray.DataArray) & (dst_crs != None):
        return( 
          candidate_map.rio.transform_bounds(target_map.rio.crs),
          benchmark_map.rio.transform_bounds(target_map.rio.crs)
          )
    
    # match candidate to benchmark
    elif (target_map == 'benchmark') & (dst_crs != None):
        return( 
          candidate_map.rio.transform_bounds(benchmark_map.rio.crs),
          benchmark_map.rio.bounds()
          )
    
    # match benchmark to candidate
    elif (target_map == 'candidate') & (dst_crs != None):
        return(
          candidate_map.rio.bounds(),
          benchmark_map.rio.transform_bounds(candidate_map.rio.crs)
          )
    
    # dst_crs is set
    elif (target_map == None) & (dst_crs != None):
        return(
          candidate_map.rio.transform_bounds(dst_crs),
          benchmark_map.rio.transform_bounds(dst_crs)
          )
    
    # both arguments are None types
    elif (target_map == None) & (dst_crs == None):
        raise ValueError("The arguments target_map and dst_crs cannot both be None types.")
    
    # wrong argument value passed to target_map
    else:
        raise ValueError("target_map argument only accepts None type, 'candidate', or 'benchmark'.")
    
def rasters_intersect(
    candidate_map_bounds: Tuple[float, float, float, float],
    benchmark_map_boundss: Tuple[float, float, float, float]
    ) -> bool:

    """ Checks if two rasters intersect spatially at all given their bounds"""

    # convert bounds to shapely boxes
    c_min_x, c_min_y, c_max_x, c_max_y = candidate_map_bounds
    b_min_x, b_min_y, b_max_x, b_max_y = benchmark_map_bounds

    # check for intersection
    if (
         (b_min_x <= c_min_x <= b_max_x) |
         (b_min_x <= c_max_x <= b_max_x) |
         (b_min_y <= c_min_y <= b_max_y) |
         (b_min_y <= c_max_y <= b_max_y) 
       ):
        return True
    else:
        return False

def align_rasters(
    candidate_map: xarray.DataArray,
    benchmark_map: xarray.DataArray,
    target_map: Optional[Union[xarray.DataArray,str]] = None,
    **kwargs
    ) -> Tuple[xarray.DataArray,xarray.DataArray]:

    """
    Reprojects raster to match target map and/or override values.

    """

    # match candidate to benchmark
    if target_map == 'benchmark':
        candidate_map = candidate_map.rio.reproject_match(benchmark_map,**kwargs)
    
    # match benchmark to candidate
    elif target_map == 'candidate':
        benchmark_map = benchmark_map.rio.reproject_match(candidate_map,**kwargs)
    
    # align benchmark and candidate to target
    elif isinstance(target_map,xarray.DataArray):
        candidate_map = candidate_map.rio.reproject_match(target_map,**kwargs)
        benchmark_map = benchmark_map.rio.reproject_match(target_map,**kwargs)
    
    # no target passed but with override values
    elif (target_map == None) & (kwargs):
        candidate_map = candidate_map.rio.reproject(**kwargs)
        benchmark_map = benchmark_map.rio.reproject(**kwargs)
    
    else:
        raise ValueError("target_map argument only accepts xarray.DataArray, 'candidate', 'benchmark', or None type.")

    return(candidate_map, benchmark_map)

def Spatial_alignment( 
    candidate_map: xarray.DataArray,
    benchmark_map: xarray.DataArray,
    target_map: Optional[Union[xarray.DataArray,str]] = 'benchmark',
    **kwargs
    ) -> Union[xarray.DataArray,xarray.DataArray]:
    """
    Reproject :class:`xarray.Dataset` objects

    .. note:: Only 2D/3D arrays with dimensions 'x'/'y' are currently supported.
        Others are appended as is.
        Requires either a grid mapping variable with 'spatial_ref' or
        a 'crs' attribute to be set containing a valid CRS.
        If using a WKT (e.g. from spatiareference.org), make sure it is an OGC WKT.

    .. versionadded:: X.X.X.X feature

    Parameters
    ----------
    dst_crs: str
        OGC WKT string or Proj.4 string.
    resolution: float or Tuple(float, float), optional
        Size of a destination pixel in destination projection units
        (e.g. degrees or metres).
    shape: Tuple(int, int), optional
        Shape of the destination in pixels (dst_height, dst_width). Cannot be used
        together with resolution.
    transform: Affine, optional
        The destination transform.
    resampling: rasterio.enums.Resampling, optional
        See :func:`rasterio.warp.reproject` for more details.
    nodata: float, optional
        The nodata value used to initialize the destination;
        it will remain in all areas not covered by the reprojected source.
        Defaults to the nodata value of the source image if none provided
        and exists or attempts to find an appropriate value by dtype.
    **kwargs: dict
        Additional keyword arguments to pass into :func:`rasterio.warp.reproject`.
        To override:
        - src_transform: `rio.write_transform`
        - src_crs: `rio.write_crs`
        - src_nodata: `rio.write_nodata`

    Returns
    --------
    :class:`xarray.Dataset`:
        The reprojected Dataset.
    """
    # check if rasters intersect at all
    rasters_intersect(candidate_map, benchmark_map, target_map, desired_crs)

    # reproject maps to align
    align_rasters(candidate_map, benchmark_map, target_map, desired_crs)


