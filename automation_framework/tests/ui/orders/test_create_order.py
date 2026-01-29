import pytest
from pages.orders_page import OrdersPage

@pytest.mark.ui
@pytest.mark.workflow_order_create
@pytest.mark.component_orders
def test_create_order_ui(page):
    orders=OrdersPage(page)
    orders.open()
    orders.enter_item("Laptop")
    orders.click_create()
    assert orders.first_order_text()=="Laptop"
