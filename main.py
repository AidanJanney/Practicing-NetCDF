from imports import *

## Accessing Practice Data from NASA GISTemp Global Temperature Anomaly Dataset
gisdata = pooch.retrieve('https://data.giss.nasa.gov/pub/gistemp/gistemp1200_GHCNv4_ERSSTv5.nc.gz',
    known_hash = None,
    processor=pooch.Decompress(),)

# Converting to an xarray object, gissdata is currently a netCDF
ds = xr.open_dataset(gisdata)
print(ds)

