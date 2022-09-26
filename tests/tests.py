
import pytest
import os

from gval.utils import load_raster_with_xarray

test_data_dir = os.path.join(os.path.expanduser("~"),'data','foss_fim','test_cases'
benchmark_data_dir = os.path.join(test_data_dir,

@pytest.mark.parametrize( "candidate_map,benchmark_map", 
                          [("3+5", 8)]
                        )
def test_compare_categorical_rasters(candidate_map, benchmark_map):
    """
    """
    
    candidate_map_xr = load_raster_with_xarray(candidate_map)
    benchmark_map_xr = load_raster_with_xarray(benchmark_map)
