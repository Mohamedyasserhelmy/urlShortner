import requests 
import json


def update_url(slug, data_to_update):
    url = "https://eu-central-1.aws.data.mongodb-api.com/app/data-qpocg/endpoint/data/v1/action/updateOne"
    payload = json.dumps({
        "collection": "urlcollection",
        "database": "short_urls",
        "dataSource": "Cluster0",
        "filter": { "slug": slug },
        "update": {
         "$set":  data_to_update 
     }
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'hLL3bx3Ni1QlPwxH8caj0oaWHYYRVleEBKMDqmIhw74Wj1Fhh2bSs1RgypZ0xy8G', 
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response