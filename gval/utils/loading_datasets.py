import rasterio


def load_single_rasterio_data(source):
    
    if isinstance(source,rasterio.DatasetReader):
