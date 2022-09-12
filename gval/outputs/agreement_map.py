import xarray as xr
import rioxarray as rxr

class Agreement_map(rxr.Dataset):

    def __init__(self, data, comparison_type, encoding):

        super().__init__(data.copy())
        
        # set metadata

