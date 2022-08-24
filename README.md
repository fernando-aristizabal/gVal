# gVal: Geospatial Evaluator
gVal (pronounced "g-val") is a high-level Python package to evaluate geospatial datasets by computing agreement maps and metrics between candidate and benchmark maps.

# Requirements
- Easy to use, well documented, high-level functionality.
- Accepts rasters and vector files.
- Accepts continous and categorical variables.
- Supports a wide array of continous and categorical metrics.
- Reads files in chunks to avoid lower memory requirements.
- Conducts operations in parallel using Dask.
- Candidate map and benchmark maps should have a series of metadata values (discrete, categorical, continous) associated with them (source model, assumptions, parameter values, sensors, etc).
    - Agreement maps and metrics should be able to inherit these metadata 

# To-Do
- Decide on vocabulary
    - metrics 
    - agreement
    - difference
    - evaluation
    - benchmark map
    - Candidate map? Need better name?
- write up architecture
    - Classes
        - metrics dictionary
            - method to include/remove metrics from dictionary
        - candidate map?
        - benchmark map?
- Decide on metrics
    - How to handle multiple names for the same metric (TPR/POD)
        - Use name dictionary?
- consider meta-data problem: STAC?
- Docstring style
- PEP formats
- Documentation website
- Test functionality
- output formats
    - metrics: json, xml, dictionary, dataframe, etc?
    - maps: rasterio object, numpy array, GDAL rasters/vectors, xarray?
- Dependency management/Packaging
    - Docker, PyPi, pip, etc
- User interface
    - public functions as API
    - command line utilities
- Alignment dimensions
    - space (extents and resolutions)
    - time (extents and resolutions)
    - modeling parameters (ie flow rates)
    - target variable (ie extents, depths, speeds, LULC, etc)

- How to deal with flow magnitudes?
    - avoiding comparison between maps of different flow magnitudes
- Computing statistical significance, confidence intervals, etc of a sampling of metrics.

