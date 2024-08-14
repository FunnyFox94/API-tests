import pytest

import practicum.sprint_7.src.api_client as api
import practicum.sprint_7.utils.test_literals as json
import practicum.sprint_7.utils.generators as generate


class TestGetListOfOrders:

    def test_get_order_positive_check(self):
        response_get_orders = api.get_order()
        assert response_get_orders.status_code == 200
