from time import sleep

import requests

import json

from bs4 import BeautifulSoup

from random import choice

import SteamMarket


id = '76561198391598489'

desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']




def random_headers():
    return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


def get_game_appid(id):
    try:
        game_appids = []
        res = requests.get('https://steamcommunity.com/profiles/%s/inventory/' % (id), headers=random_headers(), timeout=2,)
        print('Get games status - ', res.status_code)
        res_soup = BeautifulSoup(res.text, 'html.parser')
        games_list = res_soup.find('select', class_ = "responsive_tab_select").find_all('option')
        for i in range(len(games_list)):
            game_appids.append(games_list[i].get('data-appid'))
            game_appids.sort()
    except:
        print('Get games list error, status - ', res.status_code)
    return game_appids





def get_context_id(appid):
    if appid == '753':
        return '6'
    elif appid == '322330':
        return '1'
    else:
        return '2'





def get_items_info(id, appid):
    try:
        items_info = {}
        res = requests.get('https://steamcommunity.com/inventory/%s/%s/%s?l=russian&count=1' % (id,     appid, get_context_id(appid)), headers=random_headers(), timeout=2,)
        print('Get first item info status - ', res.status_code)
        response_dict = json.loads(res.text)
        total_inventory_count = response_dict['total_inventory_count']

        for i in range(total_inventory_count):
            items_info.update({response_dict['descriptions'][0]['name'] : {
            'market_hash_name' : response_dict['descriptions'][0]['market_hash_name'],
            'classid' : response_dict['descriptions'][0]['classid'],
            'appid' : response_dict['descriptions'][0]['appid'],
            'instanceid' : response_dict['descriptions'][0]['instanceid'],
            'img_url' : 'https://community.cloudflare.steamstatic.com/economy/image/%s' %(response_dict['descriptions'][0]['icon_url']),
            'tradable' : response_dict['descriptions'][0]['tradable'],
            'marketable' : response_dict['descriptions'][0]['marketable'],}})
            last_acces_id = response_dict['assets'][0]['assetid']
            res = requests.get('https://steamcommunity.com/inventory/%s/%s/%s?l=russian&count=1&start_assetid=%s' % (id, appid, get_context_id(appid), last_acces_id), headers=random_headers(), timeout=2,)
            response_dict = json.loads(res.text) 
            sleep(1)
            print('Get item info status - ', res.status_code)
    except:
        print('Get item info error status - ', res.status_code, appid)
    return items_info




def price_of_inventory(id):
    sum = 0
    appids = get_game_appid(id)
    for i in range(len(appids)):
        items_info = get_items_info(id, appids[i])
        for key in items_info.keys():
            if items_info[key]['marketable'] == 1:
                try:
                    elem_price = SteamMarket.get_current_price(appids[i], items_info[key]['market_hash_name'], 2)
                    sum = sum + elem_price
                    print('succes - ', appids[i], items_info[key]['market_hash_name'])
                except:
                    print('Get price error - ')
    return sum

print(price_of_inventory(id))




















