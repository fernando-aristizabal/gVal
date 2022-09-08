import rasterio
import rioxarray
import xarray as xr
import boto3


def load_single_rasterio_file(source):
    """
    Utility function loads a single raster from file path or URL checking if not already a raster.
    
    Parameters
    ----------

    Returns
    -------

    """
    
    # rasterio dataset
    if isinstance(source,rasterio.io.DatasetReader):
        return source
    
    # local file path or S3 url
    if isinstance(source,(str,os.PathLike)):
        # TO-DO: support authentication
        return rasterio.open(source)
    
    # if neither rasterio dataset, filepath, or url
    else:
        raise ValueError("Source should be Rasterio DatasetReader or either a file path or a URL to a raster file.")


def load_single_raster_with_xarray(source, *args, **kwargs):
    """
    Utility function loads a single raster as xarray from file path or URL checking if not already a raster.
    
    Parameters
    ----------
    source : str, os.PathLike, rasterio.io.DatasetReader, Rasterio.vrt.WarpedVRT, xarray.Dataset, xarray.DataArray, or list of xarray.DataArray
        Path to file or opened Rasterio Dataset.
    *args : args, optional
        Optional positional arguments to pass to rioxarray.open_rasterio.
    *kwargs : kwargs, optional
        Optional keyword arguments to pass to rioxarray.open_rasterio.

    Returns
    -------
    xarray.Dataset
        xarray dataset.
    xarray.DataArray
        xarray dataarray.
    List[xarray.Dataset]
        list of xarray datasets.

    """
    
    # rasterio dataset
    if isinstance(source,(xr.dataset,xr.DataArray)):
        return source
    
    # local file path or S3 url
    elif isinstance(source,(str,os.PathLike)):
        # TO-DO: support authentication
        return rioxarray.open_rasterio(source)
    
    # List[xarray.DataArray]
    elif isinstance(source,list):
        if all( [isinstance(e,xr.Dataset) for e in source )
        return source
    
    # if neither rasterio dataset, filepath, or url
    else:
        raise ValueError("Source should be a filepath to a raster or xarray Dataset, DataArray or list of Datasets.")

