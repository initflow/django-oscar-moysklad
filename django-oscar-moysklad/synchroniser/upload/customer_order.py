from random import random

from models import UserSync
from synchroniser.util.loader import RequestList
from synchroniser.upload.static_upload_values import StaticUploadValues


class CustomerOrderUpload:
    default_url = "https://online.moysklad.ru/api/remap/1.1/entity/customerorder/"

    def upload(self, order, store):
        # order = Order()
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
                'positions': []}  # order variants

        result = RequestList.upload(CustomerOrderUpload.default_url, json_data=data)

        # updated_date = datetime.strptime(result.get('updated'), '%Y-%m-%d %H:%M:%S') if result.get(
        #     'updated') is not None else None
        #
        # user_sync = UserSync(sync_id=result.get('id'), user=user, updated=updated_date,
        #                      archived=result.get('archived'), email=result.get('email'))
        # result = user_sync.save()
        # k = 10