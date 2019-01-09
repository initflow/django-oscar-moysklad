from datetime import datetime

from models import UserSync
from synchroniser.util.loader import RequestList
from synchroniser.upload.static_upload_values import StaticUploadValues


class CounterPartyUpload:
    default_url = "https://online.moysklad.ru/api/remap/1.1/entity/counterparty/"

    def upload(self, user):
        attributes = [StaticUploadValues.counter_party_gender, StaticUploadValues.counter_party_city]
        data = {'name': user.first_name + ' ' + user.last_name, 'email': user.email, 'phone': '',
                'actualAddress': '', 'attributes': attributes}
        result = RequestList.upload(CounterPartyUpload.default_url, json_data=data)

        updated_date = datetime.strptime(result.get('updated'), '%Y-%m-%d %H:%M:%S') if result.get(
            'updated') is not None else None

        user_sync = UserSync(sync_id=result.get('id'), user=user, updated=updated_date,
                             archived=result.get('archived'), email=result.get('email'))
        result = user_sync.save()
        k = 10
