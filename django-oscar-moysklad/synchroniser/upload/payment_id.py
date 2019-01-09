from random import random

from models import UserSync
from synchroniser.util.loader import RequestList
from synchroniser.upload.static_upload_values import StaticUploadValues


class PaymentInUpload:
    default_url = "https://online.moysklad.ru/api/remap/1.1/entity/paymentin/"

    def upload(self, order, customer_order_response):
        random_id = random.randrange(0, 100000)
        user_sync_id = UserSync.objects.filter(user=order.user).first().sync_id

        operations = {
            'meta': customer_order_response.get('meta'),
            'linkedSum': order.shipping_incl_tax
        }
        data = {
            'name': 'IM_' + order.id + '_' + random_id + '_server',
            'agent': StaticUploadValues.get_counter_party_container(user_sync_id),
            'organization': StaticUploadValues.organization_meta_container,
            'sum': order.shipping_incl_tax,
            'operations': [operations]
        }

        result = RequestList.upload(PaymentInUpload.default_url, json_data=data)
