"""
Test goes here

"""

from mylib.query import query


def test_query():
    assert query("SELECT COUNT(*) FROM JeopardyDB") == [("36557",)]

    pass


def test_extract():
    pass


def test_transform_load():
    pass
