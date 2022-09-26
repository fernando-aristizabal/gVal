"""
Functions to load datasets
"""

# __all__ = ['a', 'b', 'c']
__version__ = '0.0.0.0'
__author__ = 'Fernando Aristizabal'

import os

import rioxarray as rxr
import xarray as xr
import rasterio

# To-Do: allow for s3 reads
#import boto3


def load_raster_as_xarray(
    source: Union[str, os.PathLike, rasterio.io.DatasetReader,
             Rasterio.vrt.WarpedVRT, xarray.DataArray],
    *args,
    **kwargs
    ) -> xarray.DataArray:
    """
    Loads a single raster as xarray DataArray from file path or URL.

    Currently working on extending support for S3.

    Parameters
    ----------
    source : str, os.PathLike, rasterio.io.DatasetReader, Rasterio.vrt.WarpedVRT, xarray.DataArray
        Path to file or opened Rasterio Dataset.
    *args : args, optional
        Optional positional arguments to pass to rioxarray.open_rasterio.
    *kwargs : kwargs, optional
        Optional keyword arguments to pass to rioxarray.open_rasterio.

    Returns
    -------
    xarray.DataArray
        xarray dataarray.
    """
    
    #if isinstance(source,(xr.Dataset,xr.DataArray)):
    
    # existing xr DataArray
    if isinstance(source,xr.DataArray):
        return source
    
    # local file path or S3 url
    elif isinstance(source,(str,os.PathLike)):
        # TO-DO: support authentication
        return rxr.open_rasterio(source, *args, **kwargs)
    
    # removed DataSet support for now
    # List[xarray.DataArray]
    #elif isinstance(source,list):
    #    if all( [isinstance(e,xr.Dataset) for e in source] ):
    #        return source
    
    # if neither rasterio dataset, filepath, or url
    else:
        raise ValueError("Source should be a filepath to a raster or xarray Dataset, DataArray or list of Datasets.")

