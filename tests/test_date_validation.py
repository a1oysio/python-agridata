import os
import sys
from datetime import datetime
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agridata.queries.cereals import CerealPricesQuery


def test_datetime_converted():
    q = CerealPricesQuery(beginDate=datetime(2020, 1, 2), endDate="03/01/2020")
    params = q.dict()
    assert params["beginDate"] == "02/01/2020"
    assert params["endDate"] == "03/01/2020"


def test_invalid_format_raises():
    with pytest.raises(ValueError):
        CerealPricesQuery(beginDate="2020-01-02")
