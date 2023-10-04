# Module titiler.core.dependencies

Common dependency.

## Variables

```python3
RescaleType
```

## Functions

    
### BufferParams

```python3
def BufferParams(
    buffer: typing_extensions.Annotated[Union[float, NoneType], Query(PydanticUndefined)] = None
) -> Union[float, NoneType]
```

Tile buffer Parameter.

    
### ColorFormulaParams

```python3
def ColorFormulaParams(
    color_formula: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
) -> Union[str, NoneType]
```

ColorFormula Parameter.

    
### ColorMapParams

```python3
def ColorMapParams(
    colormap_name: typing_extensions.Annotated[Union[titiler.core.dependencies.ColorMapName, NoneType], Query(PydanticUndefined)] = None,
    colormap: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
) -> Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]], NoneType]
```

Colormap Dependency.

    
### CoordCRSParams

```python3
def CoordCRSParams(
    crs: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
) -> Union[rasterio.crs.CRS, NoneType]
```

Coordinate Reference System Coordinates Param.

    
### DatasetPathParams

```python3
def DatasetPathParams(
    url: typing_extensions.Annotated[str, Query(PydanticUndefined)]
) -> str
```

Create dataset path from args

    
### DstCRSParams

```python3
def DstCRSParams(
    crs: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
) -> Union[rasterio.crs.CRS, NoneType]
```

Coordinate Reference System Coordinates Param.

    
### RescalingParams

```python3
def RescalingParams(
    rescale: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None
) -> Union[List[Tuple[float, ...]], NoneType]
```

Min/Max data Rescaling

## Classes

### AssetsBidxExprParams

```python3
class AssetsBidxExprParams(
    assets: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None,
    expression: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None,
    asset_indexes: typing_extensions.Annotated[Union[Sequence[str], NoneType], Query(PydanticUndefined)] = None,
    asset_as_band: typing_extensions.Annotated[Union[bool, NoneType], Query(PydanticUndefined)] = None
)
```

Assets, Expression and Asset's band Indexes parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.AssetsParams
* titiler.core.dependencies.DefaultDependency

#### Descendants

* titiler.core.dependencies.AssetsBidxExprParamsOptional

#### Class variables

```python3
asset_as_band
```

```python3
asset_indexes
```

```python3
assets
```

```python3
expression
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### AssetsBidxExprParamsOptional

```python3
class AssetsBidxExprParamsOptional(
    assets: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None,
    expression: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None,
    asset_indexes: typing_extensions.Annotated[Union[Sequence[str], NoneType], Query(PydanticUndefined)] = None,
    asset_as_band: typing_extensions.Annotated[Union[bool, NoneType], Query(PydanticUndefined)] = None
)
```

Assets, Expression and Asset's band Indexes parameters but with no requirement.

#### Ancestors (in MRO)

* titiler.core.dependencies.AssetsBidxExprParams
* titiler.core.dependencies.AssetsParams
* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
asset_as_band
```

```python3
asset_indexes
```

```python3
assets
```

```python3
expression
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### AssetsBidxParams

```python3
class AssetsBidxParams(
    assets: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None,
    asset_indexes: typing_extensions.Annotated[Union[Sequence[str], NoneType], Query(PydanticUndefined)] = None,
    asset_expression: typing_extensions.Annotated[Union[Sequence[str], NoneType], Query(PydanticUndefined)] = None
)
```

Assets, Asset's band Indexes and Asset's band Expression parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.AssetsParams
* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
asset_expression
```

```python3
asset_indexes
```

```python3
assets
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### AssetsParams

```python3
class AssetsParams(
    assets: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None
)
```

Assets parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Descendants

* titiler.core.dependencies.AssetsBidxExprParams
* titiler.core.dependencies.AssetsBidxParams

#### Class variables

```python3
assets
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### BandsExprParams

```python3
class BandsExprParams(
    bands: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None,
    expression: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

Band names and Expression parameters (Band or Expression required).

#### Ancestors (in MRO)

* titiler.core.dependencies.ExpressionParams
* titiler.core.dependencies.BandsParams
* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
bands
```

```python3
expression
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### BandsExprParamsOptional

```python3
class BandsExprParamsOptional(
    bands: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None,
    expression: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

Optional Band names and Expression parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.ExpressionParams
* titiler.core.dependencies.BandsParams
* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
bands
```

```python3
expression
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### BandsParams

```python3
class BandsParams(
    bands: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None
)
```

Band names parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Descendants

* titiler.core.dependencies.BandsExprParamsOptional
* titiler.core.dependencies.BandsExprParams

#### Class variables

```python3
bands
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### BidxExprParams

```python3
class BidxExprParams(
    indexes: typing_extensions.Annotated[Union[List[int], NoneType], Query(PydanticUndefined)] = None,
    expression: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

Band Indexes and Expression parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.ExpressionParams
* titiler.core.dependencies.BidxParams
* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
expression
```

```python3
indexes
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### BidxParams

```python3
class BidxParams(
    indexes: typing_extensions.Annotated[Union[List[int], NoneType], Query(PydanticUndefined)] = None
)
```

Band Indexes parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Descendants

* titiler.core.dependencies.BidxExprParams

#### Class variables

```python3
indexes
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### ColorMapName

```python3
class ColorMapName(
    /,
    *args,
    **kwargs
)
```

An enumeration.

#### Ancestors (in MRO)

* enum.Enum

#### Class variables

```python3
accent
```

```python3
accent_r
```

```python3
afmhot
```

```python3
afmhot_r
```

```python3
algae
```

```python3
algae_r
```

```python3
amp
```

```python3
amp_r
```

```python3
autumn
```

```python3
autumn_r
```

```python3
balance
```

```python3
balance_r
```

```python3
binary
```

```python3
binary_r
```

```python3
blues
```

```python3
blues_r
```

```python3
bone
```

```python3
bone_r
```

```python3
brbg
```

```python3
brbg_r
```

```python3
brg
```

```python3
brg_r
```

```python3
bugn
```

```python3
bugn_r
```

```python3
bupu
```

```python3
bupu_r
```

```python3
bwr
```

```python3
bwr_r
```

```python3
cfastie
```

```python3
cividis
```

```python3
cividis_r
```

```python3
cmrmap
```

```python3
cmrmap_r
```

```python3
cool
```

```python3
cool_r
```

```python3
coolwarm
```

```python3
coolwarm_r
```

```python3
copper
```

```python3
copper_r
```

```python3
cubehelix
```

```python3
cubehelix_r
```

```python3
curl
```

```python3
curl_r
```

```python3
dark2
```

```python3
dark2_r
```

```python3
deep
```

```python3
deep_r
```

```python3
delta
```

```python3
delta_r
```

```python3
dense
```

```python3
dense_r
```

```python3
diff
```

```python3
diff_r
```

```python3
flag
```

```python3
flag_r
```

```python3
gist_earth
```

```python3
gist_earth_r
```

```python3
gist_gray
```

```python3
gist_gray_r
```

```python3
gist_heat
```

```python3
gist_heat_r
```

```python3
gist_ncar
```

```python3
gist_ncar_r
```

```python3
gist_rainbow
```

```python3
gist_rainbow_r
```

```python3
gist_stern
```

```python3
gist_stern_r
```

```python3
gist_yarg
```

```python3
gist_yarg_r
```

```python3
gnbu
```

```python3
gnbu_r
```

```python3
gnuplot
```

```python3
gnuplot2
```

```python3
gnuplot2_r
```

```python3
gnuplot_r
```

```python3
gray
```

```python3
gray_r
```

```python3
greens
```

```python3
greens_r
```

```python3
greys
```

```python3
greys_r
```

```python3
haline
```

```python3
haline_r
```

```python3
hot
```

```python3
hot_r
```

```python3
hsv
```

```python3
hsv_r
```

```python3
ice
```

```python3
ice_r
```

```python3
inferno
```

```python3
inferno_r
```

```python3
jet
```

```python3
jet_r
```

```python3
magma
```

```python3
magma_r
```

```python3
matter
```

```python3
matter_r
```

```python3
name
```

```python3
nipy_spectral
```

```python3
nipy_spectral_r
```

```python3
ocean
```

```python3
ocean_r
```

```python3
oranges
```

```python3
oranges_r
```

```python3
orrd
```

```python3
orrd_r
```

```python3
oxy
```

```python3
oxy_r
```

```python3
paired
```

```python3
paired_r
```

```python3
pastel1
```

```python3
pastel1_r
```

```python3
pastel2
```

```python3
pastel2_r
```

```python3
phase
```

```python3
phase_r
```

```python3
pink
```

```python3
pink_r
```

```python3
piyg
```

```python3
piyg_r
```

```python3
plasma
```

```python3
plasma_r
```

```python3
prgn
```

```python3
prgn_r
```

```python3
prism
```

```python3
prism_r
```

```python3
pubu
```

```python3
pubu_r
```

```python3
pubugn
```

```python3
pubugn_r
```

```python3
puor
```

```python3
puor_r
```

```python3
purd
```

```python3
purd_r
```

```python3
purples
```

```python3
purples_r
```

```python3
rain
```

```python3
rain_r
```

```python3
rainbow
```

```python3
rainbow_r
```

```python3
rdbu
```

```python3
rdbu_r
```

```python3
rdgy
```

```python3
rdgy_r
```

```python3
rdpu
```

```python3
rdpu_r
```

```python3
rdylbu
```

```python3
rdylbu_r
```

```python3
rdylgn
```

```python3
rdylgn_r
```

```python3
reds
```

```python3
reds_r
```

```python3
rplumbo
```

```python3
schwarzwald
```

```python3
seismic
```

```python3
seismic_r
```

```python3
set1
```

```python3
set1_r
```

```python3
set2
```

```python3
set2_r
```

```python3
set3
```

```python3
set3_r
```

```python3
solar
```

```python3
solar_r
```

```python3
spectral
```

```python3
spectral_r
```

```python3
speed
```

```python3
speed_r
```

```python3
spring
```

```python3
spring_r
```

```python3
summer
```

```python3
summer_r
```

```python3
tab10
```

```python3
tab10_r
```

```python3
tab20
```

```python3
tab20_r
```

```python3
tab20b
```

```python3
tab20b_r
```

```python3
tab20c
```

```python3
tab20c_r
```

```python3
tarn
```

```python3
tarn_r
```

```python3
tempo
```

```python3
tempo_r
```

```python3
terrain
```

```python3
terrain_r
```

```python3
thermal
```

```python3
thermal_r
```

```python3
topo
```

```python3
topo_r
```

```python3
turbid
```

```python3
turbid_r
```

```python3
turbo
```

```python3
turbo_r
```

```python3
twilight
```

```python3
twilight_r
```

```python3
twilight_shifted
```

```python3
twilight_shifted_r
```

```python3
value
```

```python3
viridis
```

```python3
viridis_r
```

```python3
winter
```

```python3
winter_r
```

```python3
wistia
```

```python3
wistia_r
```

```python3
ylgn
```

```python3
ylgn_r
```

```python3
ylgnbu
```

```python3
ylgnbu_r
```

```python3
ylorbr
```

```python3
ylorbr_r
```

```python3
ylorrd
```

```python3
ylorrd_r
```

### DatasetParams

```python3
class DatasetParams(
    nodata: typing_extensions.Annotated[Union[str, int, float, NoneType], Query(PydanticUndefined)] = None,
    unscale: typing_extensions.Annotated[Union[bool, NoneType], Query(PydanticUndefined)] = False,
    resampling_method: typing_extensions.Annotated[Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'gauss', 'rms'], Query(PydanticUndefined)] = 'nearest'
)
```

Low level WarpedVRT Optional parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
nodata
```

```python3
resampling_method
```

```python3
unscale
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### DefaultDependency

```python3
class DefaultDependency(
    
)
```

Dataclass with dict unpacking

#### Descendants

* titiler.core.dependencies.BidxParams
* titiler.core.dependencies.ExpressionParams
* titiler.core.dependencies.AssetsParams
* titiler.core.dependencies.BandsParams
* titiler.core.dependencies.ImageParams
* titiler.core.dependencies.DatasetParams
* titiler.core.dependencies.ImageRenderingParams
* titiler.core.dependencies.StatisticsParams
* titiler.core.dependencies.HistogramParams

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### ExpressionParams

```python3
class ExpressionParams(
    expression: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

Expression parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Descendants

* titiler.core.dependencies.BidxExprParams
* titiler.core.dependencies.BandsExprParamsOptional
* titiler.core.dependencies.BandsExprParams

#### Class variables

```python3
expression
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### HistogramParams

```python3
class HistogramParams(
    bins: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None,
    range: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

Numpy Histogram options.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
bins
```

```python3
range
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### ImageParams

```python3
class ImageParams(
    max_size: typing_extensions.Annotated[int, 'Maximum image size to read onto.'] = 1024,
    height: typing_extensions.Annotated[Union[int, NoneType], 'Force output image height.'] = None,
    width: typing_extensions.Annotated[Union[int, NoneType], 'Force output image width.'] = None
)
```

Common Preview/Crop parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
height
```

```python3
max_size
```

```python3
width
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### ImageRenderingParams

```python3
class ImageRenderingParams(
    add_mask: typing_extensions.Annotated[bool, Query(PydanticUndefined)] = True
)
```

Image Rendering options.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
add_mask
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### StatisticsParams

```python3
class StatisticsParams(
    categorical: typing_extensions.Annotated[bool, Query(PydanticUndefined)] = False,
    categories: typing_extensions.Annotated[Union[List[Union[float, int]], NoneType], Query(PydanticUndefined)] = None,
    percentiles: typing_extensions.Annotated[Union[List[int], NoneType], Query(PydanticUndefined)] = None
)
```

Statistics options.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
categorical
```

```python3
categories
```

```python3
percentiles
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.