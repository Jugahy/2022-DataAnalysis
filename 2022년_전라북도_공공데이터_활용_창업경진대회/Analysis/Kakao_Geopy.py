import requests, json


def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    headers = {"Authorization": "KakaoAK b0fb3729d2fb8c9d30c1d622f364130d"}
    api_json = json.loads(str(requests.get(url, headers=headers).text))
    address = api_json['documents'][0]['address']
    crd = {"lat": str(address['y']), "lng": str(address['x'])}
    address_name = address['address_name']

    return crd


crd = get_location("전라북도 전주시 완산구 내원당길 70-15")
print(crd)
