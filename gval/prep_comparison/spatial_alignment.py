
import rioxarray as rxr
import shapely

def Spatial_alignment( candidate_map, benchmark_map,
                       match_map='benchmark', dst_crs=None, resolution=None, 
                       shape=None, transform=None, resampling=Resampling.nearest,
                       nodata=None, **kwargs):
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
    resolution: float or tuple(float, float), optional
        Size of a destination pixel in destination projection units
        (e.g. degrees or metres).
    shape: tuple(int, int), optional
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
    rasters_intersect(candidate_map, benchmark_map, match_map, desired_crs)

    # reproject maps to align
    align_rasters(candidate_map, benchmark_map, match_map, desired_crs)



def align_rasters(candidate_map, benchmark_map, match_map=None, desired_crs=None):

    # reproject rasters
    if match_map == 'benchmark':
        candidate_map = candidate_map.rio.reproject_match(benchmark_map)
    elif match_map == 'candidate':
        benchmark_map = benchmark_map.rio.reproject_match(candidate_map)
    elif match_map == None:
        pass
    else:
        raise ValueError("match_map argument only accepts None type, 'candidate', or 'benchmark'.")
    
    # override values if any are passed
    candidate_map = candidate_map.rio.reproject( dst_crs, resolution, 
                                                 shape, transform, resampling,
                                                 nodata, **kwargs )
    benchmark_map = benchmark_map.rio.reproject( dst_crs, resolution, 
                                                 shape, transform, resampling,
                                                 nodata, **kwargs )

    return(candidate_map, benchmark_map)


def rasters_intersect(candidate_map, benchmark_map, match_map=None, dst_crs=None):
    
    # transform bounds of candidate map to that of CRS of benchmark
    if (match_map == 'benchmark') & (dst_crs != None):
        candidate_bounds = candidate_map.rio.transform_bounds(benchmark_map.rio.crs)
        benchmark_bounds = benchmark_map.rio.bounds()
    elif (match_map == 'candidate') & (dst_crs != None):
        benchmark_bounds = benchmark_map.rio.transform_bounds(candidate_map.rio.crs)
        candidate_bounds = candidate_map.rio.bounds()
    elif (match_map == None) & (dst_crs != None):
        candidate_bounds = candidate_map.rio.transform_bounds(dst_crs)
        benchmark_bounds = benchmark_map.rio.transform_bounds(dst_crs)
    else:
        raise ValueError("match_map argument only accepts None type, 'candidate', or 'benchmark'.")

    # convert bounds to shapely boxes
    candidate_bounds_geom = box(*candidate_bounds)
    benchmark_bounds_geom = box(*benchmark_bounds)

    # check for intersection
    intersect_bool = candidate_bounds_geom.intersects(benchmark_bounds_geom)

    return(intersect_bool)


