import pytest

import practicum.sprint_7.src.api_client as api
import practicum.sprint_7.utils.test_literals as json


class TestCreateOrder:

    @pytest.mark.parametrize(
        'order_info', [
            json.ORDER_INFO_COLOR_BLACK,
            json.ORDER_INFO_COLOR_GREY,
            json.ORDER_INFO_COLOR_GREY_AND_BLACK,
            json.ORDER_INFO_WITHOUT_COLOR
        ]
    )
    def test_create_order_positive_check(self, order_info):
        response = api.create_order(order_info)
        assert 'track' in response.json()
