import xarray
import rasterio
import numpy as np
from gval.utils.loading_datasets import load_single_rasterio_file

def Agreement_on_aligned_rasters( candidate_map, benchmark_map,
                                  comparison_type='two-class',
                                  # support discretizing functions: equal, greater,less, greaterequal, lessequal,isclose
                                  # accepts thresholds as single or series of values for each
                                  # returns a private function with __equal(value_to_threshold)
                                  candidate_positive_conditions=2,
                                  candidate_negative_conditions=2,
                                  benchamrk_positive_conditions=2,
                                  benchmark_negative_conditions=2,
                                  multi_class_comparison='one-v-all' # 'one-v-one'
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
    candidate_positive_conditions : int or a series of ints
        Value or values representing positive condition in candidate map. Only necessary when comparison_type is set to two-class or multi-class.
    candidate_negative_conditions : int or a series of ints
        Value or values representing negative condition in candidate map. Only necessary when comparison_type is set to two-class or multi-class.
    benchmark_positive_condition : int or a series of ints
        Value or values representing positive condition in benchmark map. Only necessary when comparison_type is set to two-class or multi-class.
    benchmark_negative_condition : int or a series of ints
        Value or values representing negative condition in benchmark map. Only necessary when comparison_type is set to two-class or multi-class.
    
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
