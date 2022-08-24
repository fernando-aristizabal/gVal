import rasterio


def load_single_rasterio_file(source):
    """
    Loads a single raster
    """
    # rasterio dataset
    if isinstance(source,rasterio.io.DatasetReader):
        output = source
    # local file path or S3 url
    if isinstance(source,str):
        # TO-DO: support authentication
        output = rasterio.open(source)
    else:
        raise ValueError("Source should be Rasterio DatasetReader or either a file path or a URL to a raster file.")

    return(output)
