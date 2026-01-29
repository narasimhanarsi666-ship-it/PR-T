import pytest
from pages.orders_page import OrdersPage

@pytest.mark.ui
@pytest.mark.workflow_order_view
@pytest.mark.component_orders
def test_view_orders(page):
    orders=OrdersPage(page)
    orders.open()
    assert orders.first_order_text() is not None
