
import numpy as np
import rasterio as rs
import rioxarray as rxr
import xarray as xr

def Spatial_alignment( candidate_map, benchmark_map,
                       match_map, dst_crs=None, resolution=None, 
                       shape=None, transform=None, resampling=Resampling.nearest,
                       nodata=None, **kwargs):
    """
    Reproject :class:`xarray.Dataset` objects

    .. note:: Only 2D/3D arrays with dimensions 'x'/'y' are currently supported.
        Others are appended as is.
        Requires either a grid mapping variable with 'spatial_ref' or
        a 'crs' attribute to be set containing a valid CRS.
        If using a WKT (e.g. from spatiareference.org), make sure it is an OGC WKT.

    .. versionadded:: 0.0.27 shape
    .. versionadded:: 0.0.28 transform
    .. versionadded:: 0.5.0 nodata, kwargs

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

    # check extents


def check_raster_spatial_extents(candidate_map, benchmark_map):
    pass
