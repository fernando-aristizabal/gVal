
import dask
import dask.dataframe as dd
import xarray

@dask.delayed()
def crosstab_rasters(
    candidate_map: xarray.DataArray,
    benchmark_map: xarray.DataArray
    ) -> tuple[dask.dataframe.DataFrame,dask.array.Array]:
    
    """
    Creates contingency and agreement tables as dds from candidate and benchmark sliceable arrays.

    Only to be used on spatially aligned candidates and benchmarks.
    """

    # convert to dask dataframes with only the data via a dataset
    # only use indices from benchmark
    candidate_map_dd = candidate_map.to_dataset(name='candidate').to_dask_dataframe().loc[:,'candidate']
    benchmark_map_dd = benchmark_map.to_dataset(name='benchmark').to_dask_dataframe().loc[:,:]

    # concat dds
    comparison_dd = dd.concat([candidate_map_dd, benchmark_map_dd],axis=1)

    # create categorical datatypes
    comparison_dd = comparison_dd.categorize(columns=['benchmark','candidate'])

    # nans index
    comparison_dd_no_nans = comparison_dd.dropna()
    breakpoint()

    # create contingency table with ascending categories
    contingency_table = comparison_dd.value_counts(ascending=True)

    # create agreement table, extract count column, and convert to dask Array
    agreement_table = contingency_table.reset_values(name='count').loc[:,'count'].to_dask_array()

    # convert agreement table back to dask array
    agreement_array = None

    return(agreement_table, contingency_table)


def compare_continuous_rasters():
    pass
