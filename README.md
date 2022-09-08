# gVal: Geospatial Evaluation Engine
gVal (pronounced "g-val") is a high-level Python engine to evaluate geospatial datasets by comparing candidate and benchmark maps to produce agreement maps and metrics.

## Architecture
- Inputs maps
    - Candidates and Benchmarks
        - Including collections and catalogs
    - Variable name
        - ie inundation, land cover, land use, backscatter, etc
    - Statistical Data Type
        - Categorical (multi-class)
        - Binary (two- class)
            - encodings for positive and negative condition values
        - Continous
    - Raster attribute table: associates names to data values
    - Data format
        - GDAL compatible vector 
        - GDAL compatible raster
    - Additional metadata
        - modeling parameters
        - time
    - Decide on storage types and in-memory data structures
        - Deserialization methods
        - Especialy for metadata (STAC, geoparquet, geojson, etc)
- Comparison Prep
    - The following prep operations should be done during the comparison to avoid excessive I/O operations.
        - Exceptions include:
            - Checking for spatial extents
            - Data format check and conversion
    - Check for alignment between candidate and benchmark.
        - spatial
            - CRS
            - extents (reject if no alignment is found)
            - resolution
        - temporal
        - metadata
    - Homogenize
        - spatial
            - Reproject
            - Match extents
            - Resample resolutions
        - temporal
            - select temporal mis-alignment criteria
        - metadata
            - select rules for disagreement
    - Statistical Data Type Conversions
        - Pass operator functions both registered and user defined
        - Conversion Types
            - Categorical to binary
            - Continuous to categorical
            - Continuous to binary
    - Data Format Check and Conversion
        - Check for vector and raster data formats
        - Convert to one consistent data format for comparison
    - Metadata prep
- Comparison
    - Comparisons should avoid opening up the entire files to avoid excessive memory use.
    - Comparisons should minimize I/O operations.
    - Comparison type
        - Binary
        - Categorical
            - one vs one
            - one vs all
        - Continuous
    - Metrics to use:
        - registered list per comparison type
            - handle multiple names for same metric
        - user provided
        - user ignored
    - Data format of comparison
        - vector or raster
- Outputs
    - Decide on storage types and methods to serialize
    - agreement maps
        - raster, vector, both
    - metric values
        - contingency tables
        - metric values
        - dataframes

## Road Map

### Checkpoint 1: Minimum Viable Product
- [ ] Easy to use, well documented, high-level functionality.
- [ ] Accepts GDAL compatible single-band raster formats.
- [ ] Accepts two-class (binary) categorical variables with set encodings.
- [ ] Handles a registry of encodings based on keyword descriptors (e.g. inundation map, landcover data, etc).
- [ ] Accepts local and remote files on S3s.
- [ ] Supports a wide array of two-class categorical metrics.
- [ ] Reads files in chunks to avoid lower memory requirements.
- [ ] Conducts operations in parallel.
- [ ] Uses a consistent set of vocabulary in variables, comments, and documentation
    - [ ] metrics, agreement, difference, evaluation, benchmark map, Candidate map? Need better name?
- [ ] Clear, concise, and foundational Object Oriented Architecture
     - [ ] Organize functions, classes, modules, parameters, etc in a logical directory structure
- [ ] Use consistent Docstring styling
- [ ] Use PEP formats and standards
- [ ] Make a documentation website
    - [ ] installation, objects, usage examples
- [ ] Include test functionality
    - [ ] unit tests
    - [ ] integration tests
    - [ ] include simple test datasets
    - [ ] include results for tests on readme/website
- [ ] Dependency management & packaging
    - [ ] Docker, PyPi, pip, etc
- [ ] Use a logger
- [ ] Have a clear user interface
    - [ ] public functions as API
    - [ ] command line tools
- [ ] Have a clear, code versioning and tagging system.

### Checkpoint 2: Extending Functionality
- Extending to include continuous data inputs and metrics.
- Support discretization of continuous maps to categorical conversion
- Create a survey of metrics.
    - Organize in hierarchy.
    - Include in tables with descriptions, math formulas, and references.

### Checkpoint 3: Scaling to Catalogs of Maps
- Evaluations should be scaled to accept a series of candidates and benchmarks.
    - These maps should be accepted as lists of objects, file paths, or catalogs.
    - Catalogs should be a data structure designed for this purpose to include experiment relevant parameters associated with each map.
- Candidate and benchmark maps need to be cataloged with associated metadata values
    - space, time, parameters, etc
- Agreement maps and metrics should be able to inherit these metadata 
    - Consider meta-data problem: STAC, raster tags, database, table?
- When comparing catalogs, need to address the alignment problem
    - Have functions to test for candidate and benchmark map alignment across the following dimensions:
        - space (extents and resolutions)
        - time (extents and resolutions)
        - modeling parameters (ie flow rates)
        - target variable (ie extents, depths, speeds, LULC, etc)
- Computing statistical significance, confidence intervals, etc of a sampling of metrics.

### Checkpoint 4: Extending Functionality
- Accepts vectors files (points, lines, and polygons) for candidate or benchmark maps.
    - Handling raster/raster, vector/raster, raster/vector, or vector/vector comparison?
- Allows for metrics to be sorted by geometries with associated parameter combinations for analysis purposes.
- Multi-band raster support?
- Multi-class categorical extension
- Analyze contingency tables with statistics:
    - [StatsModels](https://www.statsmodels.org/stable/contingency_tables.html)
    - [SciPy](https://docs.scipy.org/doc/scipy-0.18.0/reference/stats.html#contingency-table-functions)

## Contributing

Please see the [Contributing](CONTRIBUTING.rst) file for instructions on how to contribute to this work.

## References

Please see the [References](REFERENCES.bib) file for citations to all the references used in this work.
