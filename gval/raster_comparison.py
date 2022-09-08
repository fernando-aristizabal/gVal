import xarray
import rasterio
import numpy as np
from gval.utils.loading_datasets import load_single_raster_with_xarray
from operator import eq, ne, gt, lt, le, ge

def Raster_comparison( candidate_map, benchmark_map,
                                  comparison_type='two-class',
                                  multi_class_comparison='one-v-all', # 'one-v-one'
                                  metrics='two-class',
                                 ):
    """
    Computes agreement raster between categorical candidate and benchmark maps.
    
    - Reads input rasters in chucks (blocks/windows).
    - Applies function to chunk and returns appropriate values (primary metrics, diff, etc).
    - Aggregate function to combine window scale outputs.
    - Returns agreement map and metrics.

    Parameters
    ----------
    candidate_map : str, os.PathLike, rasterio.io.DatasetReader, rasterio.io.WarpedVRT, xarray.Dataset, xarray.DataArray
       Candidate map
    benchmark_map : str, os.PathLike, rasterio.io.DatasetReader, rasterio.io.WarpedVRT, xarray.Dataset, xarray.DataArray
       Benchmark map
    comparison_type : str 
       Variable type. Accepts two-class, multi-class, continuous. When two-class is elected, multiple positive conditions are grouped together as a single positive condition for evaluation.
    
    Returns
    -------

    Raises
    ------

    Notes
    -----
    
    References
    ----------

    Examples
    --------
    """

    load_ 




return(agreement_map)
