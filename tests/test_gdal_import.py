import pytest
import os


def test_import():
    from osgeo import ogr
    from osgeo import gdal

    print(os.environ['GDALVERSION'], gdal.__version__)
    assert os.environ['GDALVERSION'] == gdal.__version__

