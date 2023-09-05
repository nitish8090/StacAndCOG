from osgeo import gdal


def convert_to_cog(input_path: str, output_path: str):
    
    ds = gdal.Open(input_path)
    gdal.Translate(output_path, ds, options=['of=COG'])


# convert_to_cog(
#     input_path=r"C:\Users\nitis\Downloads\SN5_roads_train_AOI_7_Moscow_MS_chip996.tif",
#     output_path=r"C:\Users\nitis\Downloads\SN5_roads_train_AOI_7_Moscow_MS_chip996_cog.tif"
# )


