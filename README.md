# gVal: Geospatial Evaluator
gVal (pronounced "g-val") is a high-level Python package to evaluate geospatial datasets by computing agreement maps and metrics between candidate and benchmark maps.

# Road Map

## Checkpoint 1: Minimum Viable Product
- Easy to use, well documented, high-level functionality.
- Accepts GDAL compatible single-band raster formats.
- Accepts categorical variables with set encodings.
- Supports a wide array of continous and categorical metrics.
- Reads files in chunks to avoid lower memory requirements.
- Conducts operations in parallel.
- Uses a consistent set of vocabulary in variables, comments, and documentation
    - metrics, agreement, difference, evaluation, benchmark map, Candidate map? Need better name?
- Clear, concise, foundational Object Oriented Architecture
    - Classes
        - Metrics
            - How to handle multiple names for the same metric (TPR/POD)
                - metrics dictionary
                    - method to include/remove metrics from dictionary
        - candidate map?
        - benchmark map?
        - evaluation map/metrics
            - make python object stantards for evaluation map and metrics
                - maps: xarray object, rasterio object, arrays, etc
                - metrics: dictionary, pandas dataframe, dask dataframe, etc?
            - include methods to serialize and deserialize
                - map formats: gdal compatible rasters
                - metric formats: json, plain-text tabular with separator (tsv, csv, etc), pandas dataframe pickle, hdf, etc
     - Organize functions, classes, modules, parameters, etc in a logical directory structure
- Use consistent Docstring styling
- Use PEP formats and standards
- Make a documentation website
- Include test functionality
    - unit tests
    - integration tests
    - include simple test datasets
    - include results for tests on readme/website
- Dependency management & packaging
    - Docker, PyPi, pip, etc
- Have a clear user interface
    - public functions as API
    - command line tools
- Have a clear, code versioning and tagging system.

## Checkpoint 2: Scaling to Catalogs of Maps
- Candidate and benchmark maps need to be cataloged with associated metadata values
    - space, time, parameters, etc
- When comparing catalogs, need to address the alignment problem
    - Have functions to test for candidate and benchmark map alignment across the following dimensions:
        - space (extents and resolutions)
        - time (extents and resolutions)
        - modeling parameters (ie flow rates)
        - target variable (ie extents, depths, speeds, LULC, etc)
- Agreement maps and metrics should be able to inherit these metadata 
- Consider meta-data problem: STAC, raster metadata, database, table?
- Computing statistical significance, confidence intervals, etc of a sampling of metrics.

## Checkpoint 3: Extending Functionality
- Accepts vectors files for candidate or benchmark maps.
- Allows for metrics to be sorted by geometries with associated parameter combinations for analysis purposes.
- Multi-band raster support?
