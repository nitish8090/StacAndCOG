import pystac
import os
import rasterio

from datetime import datetime, timezone
from shapely.geometry import Polygon, mapping


def create_a_catalog(output_folder: str):
    catalog = pystac.Catalog(
        id='tutorial-catalog',
        description='This catalog is a basic demonstration catalog utilizing a scene from SpaceNet 5.')
    catalog.normalize_hrefs(output_folder)
    catalog.save(catalog_type=pystac.CatalogType.SELF_CONTAINED)



def get_bbox_and_footprint(raster):
    with rasterio.open(raster) as r:
        bounds = r.bounds
        bbox = [bounds.left, bounds.bottom, bounds.right, bounds.top]
        footprint = Polygon([
            [bounds.left, bounds.bottom],
            [bounds.left, bounds.top],
            [bounds.right, bounds.top],
            [bounds.right, bounds.bottom]
        ])

        return (bbox, mapping(footprint))


def add_item_to_catalog(catalog_path, input_image):

    catalog = pystac.Catalog.from_file(catalog_path)

    bbox, footprint = get_bbox_and_footprint(input_image)
    print("bbox: ", bbox, "\n")
    print("footprint: ", footprint)

    datetime_utc = datetime.now(tz=timezone.utc)
    item = pystac.Item(id='local-image',
                       geometry=footprint,
                       bbox=bbox,
                       datetime=datetime_utc,
                       properties={})

    catalog.add_item(item)

    item.add_asset(
        key='image',
        asset=pystac.Asset(
            href=input_image,
            media_type=pystac.MediaType.GEOTIFF
        )
    )

    catalog.save(catalog_type=pystac.CatalogType.SELF_CONTAINED)


if __name__ == '__main__':
    create_a_catalog(output_folder=os.path.join('', "stac"))

    add_item_to_catalog(
        catalog_path=r'E:\CodeRize\IngestorScripts\stac\catalog.json',
        input_image=r"C:\Users\nitis\Downloads\SN5_roads_train_AOI_7_Moscow_MS_chip996_cog.tif"
    )
