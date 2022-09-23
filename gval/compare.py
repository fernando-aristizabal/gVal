
import dask
import dask.dataframe as dd

@dask.delayed()
def compare_rasters(
    candidate_map: dask.array.Array,
    benchmark_map: dask.array.Array
    ) -> Tuple[dask.dataframe.DataFrame,dask.array.Array]:
    
    """
    Creates contingency and agreement tables as dds from candidate and benchmark sliceable arrays.

    Only to be used on spatially aligned candidates and benchmarks.
    """

    # mask dds
    candidate_map = dd.from_dask_array(candidate_map)
    benchmark_map = dd.from_dask_array(benchmark_map)

    # concat dds
    comparison_dd = dd.concat( candidate_map,
                               benchmark_map,
                               axis=1)

    # create categorical datatypes
    comparison_dd.categorize()

    # create contingency table with ascending categories
    contingency_table = comparison_dd.value_counts(ascending=True)

    # create agreement table, extract count column, and convert to dask Array
    agreement_table = contingency_table.reset_values(name='count').loc[:,'count'].to_dask_array()

    # convert agreement table back to dask array
    agreement_array = 

    return(agreement_table, contingency_table)


@dask.delayed()
def compare_vectors():
    pass
