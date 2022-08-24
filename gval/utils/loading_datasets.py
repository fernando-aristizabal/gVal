import rasterio


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
