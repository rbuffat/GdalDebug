import pytest


def test_import():
    from osgeo import ogr
    from osgeo import gdal

    print(gdal.__version__) 
    assert True
