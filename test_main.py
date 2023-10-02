"""
Test goes here

"""

from mylib.query import query


def test_query():
    """Test the query function"""

    assert query(the_query) == [("36557",)]

    pass


def test_extract():
    pass


def test_transform_load():
    pass


if __name__ == "__main__":
    the_query = "SELECT COUNT(*) FROM JeopardyDB"
    test_query(the_query)
