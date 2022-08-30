import rasterio
import rioxarray
import xarray as xr


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
        output = source
    
    # local file path or S3 url
    if isinstance(source,str):
        # TO-DO: support authentication
        output = rasterio.open(source)
    
    # if neither rasterio dataset, filepath, or url
    else:
        raise ValueError("Source should be Rasterio DatasetReader or either a file path or a URL to a raster file.")

    return(output)


def load_single_raster_with_xarray(filename, *args, **kwargs):
    """
    Utility function loads a single raster as xarray from file path or URL checking if not already a raster.
    
    Parameters
    ----------
    filename : str, rasterio.io.DatasetReader, or Rasterio.vrt.WarpedVRT
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
    if isinstance(source,xr.dataset):
        output = source
    if isinstance(source,xr.DataArray):
        output = source
    if isinstance(filename,list):
        if all( [isinstance(e,xr.Dataset) for e in filename] )
        output = source
    
    # local file path or S3 url
    if isinstance(filename,str):
        # TO-DO: support authentication
        output = rioxarray.open_rasterio(source)
    
    # if neither rasterio dataset, filepath, or url
    else:
        raise ValueError("Source should be a filepath to a raster or xarray Dataset, DataArray or list of Datasets.")

    return(output)
