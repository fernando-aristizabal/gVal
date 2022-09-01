import xarray
import rasterio
import numpy as np
from gval.utils.loading_datasets import load_single_rasterio_file

def Agreement_on_aligned_rasters(candidate_map, benchmark_map, comparison_type='two-class', positive_condition=2):
    """
    Computes agreement raster between categorical candidate and benchmark maps.
    
    - Reads input rasters in chucks (blocks/windows).
    - Applies function to chunk and returns appropriate values (primary metrics, diff, etc).
    - Aggregate function to combine window scale outputs.
    - Returns agreement map and metrics.

    Parameters
    ----------
    candidate_map : str
       Candidate map
    benchmark_map : str
       Benchmark map
    comparison_type : str 
       Variable type. Accepts two-class, multi-class, continuous.
    candidate_positive_condition : int or a series of ints
        Value or values representing positive condition in candidate map. Only necessary when comparison_type is set to two-class.
    benchmark_positive_condition : int or a series of ints
        Value or values representing positive condition in candidate map. Only necessary when comparison_type is set to two-class.
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
