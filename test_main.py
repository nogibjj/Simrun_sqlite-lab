"""
Test goes here

"""

from mylib.query import query


def test_query():
    assert query("SELECT "Facility ID" FROM PatientDB where "HCAHPS Answer Description" = "Nurse communication - star rating" ") == [('Facility ID',), ('340001',)]
    
    pass
def test_extract():
    pass
def test_transform_load():
    pass
