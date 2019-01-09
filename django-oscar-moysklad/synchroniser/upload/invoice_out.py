from random import random

from models import UserSync
from synchroniser.util.loader import RequestList
from synchroniser.upload.static_upload_values import StaticUploadValues


class InvoiceOutUpload:
    default_url = "https://online.moysklad.ru/api/remap/1.1/entity/invoiceout/"

    def upload(self, order, customer_order_response):
        description = 'Доставка по адресу: ' + order.shipping_address.title + ';\n Тел.: ' \
                      + order.shipping_address.phone_number + ';'
        random_id = random.randrange(0, 100000)
        user_sync_id = UserSync.objects.filter(user=order.user).first().sync_id

        data = {'name': 'IM_' + order.id + '_' + random_id + '_server',
                'agent': StaticUploadValues.get_counter_party_container(user_sync_id),
                'organization': StaticUploadValues.organization_meta_container,
                'store': StaticUploadValues.get_store_container(store.sync_id),
                'attributes': [],  # discount
                'description': description,
                'customerOrder': customer_order_response.get('meta'),
                'positions': []}  # order variants

        result = RequestList.upload(InvoiceOutUpload.default_url, json_data=data)