import requests 
import json

# Calling DATA API pipeline to get all the data 
def get_all():
    url = "https://eu-central-1.aws.data.mongodb-api.com/app/data-qpocg/endpoint/data/v1/action/find"
    payload = json.dumps({
        "collection": "urlcollection",
        "database": "short_urls",
        "dataSource": "Cluster0",
        "filter" : {}
    
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'hLL3bx3Ni1QlPwxH8caj0oaWHYYRVleEBKMDqmIhw74Wj1Fhh2bSs1RgypZ0xy8G', 
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response


result = get_all().json()
