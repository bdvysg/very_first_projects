import json 

import requests 

from os import mkdir

mkdir('C:/Users/Admin/Desktop/jolymemes')

headers = {
    'Cookie': 'mid=YIWOnAAEAAE2oS9dJ2O8BM8z4B4Z; ig_did=476A6867-BA3F-4EE5-890F-605685CFF528; ig_nrcb=1; shbid="7454\0545828255762\0541658150112:01f778ae85ec279804c5e7487891d73937e22b353a8e3ebaf295a33f74d45d1caa92953f"; shbts="1626614112\0545828255762\0541658150112:01f73c39161f5275c822d8cdc0341ab4aa2c4c22908b301c7e9a28f3b0031d2fe8cbea4f"; csrftoken=m89R5X4jILtazQhJhFMbVomqzVAsDoO2; ds_user_id=5828255762; sessionid=5828255762%3AuuxLys1y1GwTQ7%3A11; rur="RVA\0545828255762\0541658152542:01f7ef939e9547d1927b2d32bb8a3009582d62a5e5187da03321121de001df0d7cd84ede',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
}

res = requests.get('https://www.instagram.com/graphql/query/?query_hash=ea4baf885b60cbf664b34ee760397549&variables={"id":"5971865344","first":50,"after":"QVFCV21lNnVDMmtqQi1tQ1ZDckF6SFMtWlpBUF9iUkRqbXJsNHA4UDI1MnFPTnh0cUhQc1c4a1NJMnN6VXMwekZfVnE2b3RBakNqeFdxRmdJOGdSMnFpUA=="}', headers=headers)

jsonRes = json.loads(res.text)

isNextPage = jsonRes["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["has_next_page"]

endCursor = jsonRes["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]

while isNextPage == jsonRes["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["has_next_page"]: 

    for i in range(50):
        img_res = requests.get(jsonRes["data"]["user"]["edge_owner_to_timeline_media"]["edges"][i]["node"]["display_url"])
        with open('C:/Users/Admin/Desktop/jolymemes/%s' % (jsonRes["data"]["user"]["edge_owner_to_timeline_media"]["edges"][i]["node"]["shortcode"]) + '.jpg', 'wb') as image:
            image.write(img_res.content)
        print('Загружено - ', jsonRes["data"]["user"]["edge_owner_to_timeline_media"]["edges"][i]["node"]["shortcode"] + '.jpg')

    
    res = requests.get('https://www.instagram.com/graphql/query/?query_hash=ea4baf885b60cbf664b34ee760397549&variables={"id":"5971865344","first":50,"after":"%s"}' % (endCursor), headers=headers)
    jsonRes = json.loads(res.text)
    isNextPage = jsonRes["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["has_next_page"]
    endCursor = jsonRes["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]




