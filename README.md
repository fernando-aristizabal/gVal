# gVal: Geospatial Evaluations
gVal is a high-level Python package to evaluate geospatial datasets by computing agreement maps and metrics between a proposed dataset and a benchmark dataset.

# Requirements
- Easy to use, well documented, high-level functionality.
- Accepts rasters and vector files.
- Accepts continous and categorical variables.
- Supports a wide array of continous and categorical metrics.
- Reads files in chunks to avoid lower memory requirements.
- Conducts operations in parallel using Dask.

# To-Do:
- Decide on language
    - metrics vs statistics
    - agreement
    - evaluation
    - 
- write up architecture
    - what classes to have?
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


