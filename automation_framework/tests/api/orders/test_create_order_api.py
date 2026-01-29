import pytest
from framework.api.api_client import post,get

@pytest.mark.api
@pytest.mark.workflow_order_create
@pytest.mark.component_orders
def test_create_order_api():
    r=post("/orders",{"item":"Phone","quantity":1})
    assert r.status_code==200
    orders=get("/orders").json()
    assert "Phone" in [o["item"] for o in orders]
