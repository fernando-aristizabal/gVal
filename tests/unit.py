"""
Test functionality 
"""

# __all__ = ['a', 'b', 'c']
__version__ = '0.0.0.0'
__author__ = 'Fernando Aristizabal'

import pytest
import os
import sys

# temporary
sys.path.append(os.path.abspath('..'))

from gval.utils.loading_datasets import load_raster_as_xarray
from gval.prep_comparison.spatial_alignment import *


test_data_dir = os.path.join('/home','fernandoa','data','gval')

pytestmark = pytest.mark.parametrize( "candidate_map,benchmark_map,expect", 
                                       [(os.path.join(test_data_dir,'candidate_map_0.tif'),
                                         os.path.join(test_data_dir,'benchmark_map_0.tif'),
                                         True )])

@pytest.fixture(scope='module', params=['candidate_map_0.tif'])
def candidate_map(request):
    """ returns candidate maps """
    filepath = os.path.join(test_data_dir,request.param)
    return load_raster_as_xarray(filepath)

@pytest.fixture(scope='module', params=['benhcmark_map_0.tif'])
def benchmark_map(request):
    """ returns benchmark maps """
    filepath = os.path.join(test_data_dir,request.param)
    return load_raster_as_xarray(filepath)

@pytest.mark.parametrize("expect",[True])
def load_raster_as_xarray(candidate_map, benchmark_map, expect):
    

@pytest.mark.parametrize("expect",[True])
def test_matching_crs(candidate_map, benchmark_map, expect):

    candidate_map_xr = load_raster_as_xarray(candidate_map)
    benchmark_map_xr = load_raster_as_xarray(candidate_map)
    
    matching = matching_crs(candidate_map_xr,benchmark_map_xr)

    assert matching == expect, f'matching_crs result ({matching}) does not agree with expected ({expect})'



@pytest.mark.parametrize("expect",[True])
def test_transform_bounds(candidate_map, benchmark_map, target_map, dst_crs, expect):
    """
    """

    transform_bounds(candidate_map,benchmark_map,target_map, dst_crs, expect)


#def test_compare_categorical_rasters(candidate_map, benchmark_map):
    #"""
    #"""
    
    #candidate_map_xr = load_raster_as_xarray(candidate_map)
    #benchmark_map_xr = load_raster_as_xarray(benchmark_map)
    #pass
