import xarray
import rasterio
import numpy as np
from gval.utils.loading_datasets import load_single_rasterio_file

def Agreement_on_aligned_rasters(candidate_map, benchmark_map, comparison_type='two-class'):
    """
    Computes agreement raster between categorical candidate and benchmark maps.
    
    - Reads input rasters in chucks (blocks/windows).
    - Computes agreement map (two-class, multi-class, continuous).
    - Computes agreement primary metrics (tp/fp/tn/fn, multi-class, diff).
        - aggregates them into a storage variable
    - Returns agreement map and primary metrics.

    Parameters
    ----------
    candidate_map : str
       Candidate map
    
    benchmark_map : str
       Benchmark map
    
    comparison_type : str 
       Variable type. Accepts two-class, multi-class, continuous.

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
