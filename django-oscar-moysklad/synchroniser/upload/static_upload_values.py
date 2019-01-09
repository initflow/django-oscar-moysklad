class StaticUploadValues:
    counter_party_gender = {
        "meta": {
            "href": "https://online.moysklad.ru/api/remap/1.1/entity/counterparty/metadata/attributes/30c654a6-8ac6-11e4-90a2-8ecb0018ab05",
            "type": "attributemetadata",
            "mediaType": "application/json"
        },
        "id": "30c654a6-8ac6-11e4-90a2-8ecb0018ab05",
        "name": "Пол",
        "type": "customentity",
        "value": {
            "meta": {
                "href": "https://online.moysklad.ru/api/remap/1.1/entity/customentity/4b2c7099-6e40-11e3-d503-7054d21a8d1e/3ec5ed0e-0b1c-11e7-7a69-9711000420d3",
                "metadataHref": "https://online.moysklad.ru/api/remap/1.1/entity/companysettings/metadata/customEntities/4b2c7099-6e40-11e3-d503-7054d21a8d1e",
                "type": "customentity",
                "mediaType": "application/json",
                "uuidHref": "https://online.moysklad.ru/app/#custom_4b2c7099-6e40-11e3-d503-7054d21a8d1e/edit?id=3ec5ed0e-0b1c-11e7-7a69-9711000420d3"
            },
            "name": "???????"
        }
    }

    counter_party_city = {
        "meta": {
            "href": "https://online.moysklad.ru/api/remap/1.1/entity/counterparty/metadata/attributes/30c65676-8ac6-11e4-90a2-8ecb0018ab06",
            "type": "attributemetadata",
            "mediaType": "application/json"
        },
        "id": "30c65676-8ac6-11e4-90a2-8ecb0018ab06",
        "name": "Город",
        "type": "customentity",
        "value": {
            "meta": {
                "href": "https://online.moysklad.ru/api/remap/1.1/entity/customentity/2c734312-8ac6-11e4-90a2-8ecb0018aab1/3ec27c94-0b1c-11e7-7a69-9711000420d2",
                "metadataHref": "https://online.moysklad.ru/api/remap/1.1/entity/companysettings/metadata/customEntities/2c734312-8ac6-11e4-90a2-8ecb0018aab1",
                "type": "customentity",
                "mediaType": "application/json",
                "uuidHref": "https://online.moysklad.ru/app/#custom_2c734312-8ac6-11e4-90a2-8ecb0018aab1/edit?id=3ec27c94-0b1c-11e7-7a69-9711000420d2"
            },
            "name": "?????"
        }
    }

    organization_meta_container = {
        "meta": {
            "href": "https://online.moysklad.ru/api/remap/1.1/entity/organization/d00d670f-f282-11e6-7a34-5acf000302da",
            "metadataHref": "https://online.moysklad.ru/api/remap/1.1/entity/organization/metadata",
            "type": "organization",
            "mediaType": "application/json",
            "uuidHref": "https://online.moysklad.ru/app/#mycompany/edit?id=d00d670f-f282-11e6-7a34-5acf000302da"
        }
    }

    @staticmethod
    def get_store_container(sync_id):
        return {
            "meta": {
                "href": "https://online.moysklad.ru/api/remap/1.1/entity/organization/" + sync_id,
                "metadataHref": "https://online.moysklad.ru/api/remap/1.1/entity/organization/metadata",
                "type": "organization",
                "mediaType": "application/json"
            }
        }

    @staticmethod
    def get_counter_party_container(sync_id):
        return {
            "meta": {
                "href": "https://online.moysklad.ru/api/remap/1.1/entity/counterparty/" + sync_id,
                "metadataHref": "https://online.moysklad.ru/api/remap/1.1/entity/counterparty/metadata",
                "type": "counterparty",
                "mediaType": "application/json"
            }
        }
