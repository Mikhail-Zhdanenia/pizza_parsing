import requests
import json


def print_hi(url):


    param_request = {"location" : 'warsaw', "term" : 'pizza'}
    headers_our = {
        'Authorization': 'Bearer B6sOjKGis75zALWPa7d2dNiNzIefNbLGGoF75oANINOL80AUhB1DjzmaNzbpzF-b55X-nG2RUgSylwcr_UYZdAQNvimDsFqkkhmvzk6P8Qj0yXOQXmMWgTD_G7ksWnYx',
        'Content-Type': 'application/json'
    }

    response = requests.get(url=url, params=param_request, headers=headers_our)
    #data = response.json()
    data = json.loads(response.text)
    return data


def get_recursively(search_dict, field):

    fields_found = []

    for key, value in search_dict.items():

        if key == field:
            fields_found.append(value)

        elif isinstance(value, dict):
            results = get_recursively(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = get_recursively(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result)
    return fields_found

if __name__ == '__main__':
    #print_hi('https://api.yelp.com/v3/businesses/search')
    key = 'name'
    counter = 0
    value = get_recursively(print_hi('https://api.yelp.com/v3/businesses/search'), key)
    if value:
        for pizzeria in value:
            print(f'{key}: {pizzeria}.')
        print(f'\nWe have {len(value)} pizzerias around.')
    else:
        print('No match, no pizza)')

