import xarray
import rasterio
import numpy as np
from metrics import two_class

def Agreement_on_aligned_rasters(candidate_map, benchmark_map):
    
    """
    Computes agreement raster between categorical candidate and benchmark maps.

    - Reads input rasters in chucks (blocks/windows).
    - Computes agreement map (two-class, multi-class, continuous).
    - Computes agreement primary metrics (tp/fp/tn/fn, multi-class, diff).
        - aggregates them into a storage variable
    - Returns agreement map and primary metrics.

    """

    



return(agreement_map)
