"""
This module helps user to navigate through json object
obtained via Twitter API.
GitHub Repository: https://github.com/Andrusyshyn-Orest/learning_API.git
"""


from pprint import pprint

import requests


def get_json(bearer_token: str, endpoint: str,
             screen_name: str, count: str) -> dict:
    """
    Return .json object using Twitter API using bearer token.

    >>> get_json('d', '1.1/friends/list.json', '@kaka', '2')
    {'errors': [{'code': 89, 'message': 'Invalid or expired token.'}]}
    """

    base_url = 'https://api.twitter.com/'

    if endpoint == "":
        endpoint = '1.1/friends/list.json'
    if screen_name == '':
        screen_name = '@BarackObama'
    if count == "":
        count = '2'

    search_url = f"{base_url}{endpoint}"

    search_headers = {
        'Authorization': f'Bearer {bearer_token}'
    }

    search_params = {
        'screen_name': screen_name,
        'count' : int(count)
    }

    response = requests.get(search_url,
                            headers=search_headers,
                            params=search_params)

    json_response = response.json()

    return json_response


def show_keys(objectt: dict) -> list:
    """
    Returns list of keys on objectt.

    >>> show_keys(get_json('d', '1.1/friends/list.json', '@kaka', '2'))
    ['errors']
    """

    return list(objectt.keys())


def main():
    """
    Runs a program.
    """

    bearer_token = input('Enter your bearer token: ')
    endpoint = input('Enter endpoint (press Enter for default value "1.1/friends/list.json"): ')
    screen_name = input('Enter screenname (press Enter for default value "@BarackObama"): ')
    count = input('Enter count (press Enter for default value "2"): ')

    json_data = get_json(bearer_token, endpoint, screen_name, count)
    objectt = json_data

    while True:
        if isinstance(objectt, dict):
            answer = input('Do you want to see the whole object? [y/n]: ')
            if answer.lower() == 'y':
                pprint(objectt)
            elif answer.lower() != 'n':
                print('Error (you should enter "y" or "n"')
                return
            answer = input('Do you want to check available fields? [y/n]: ')
            if answer.lower() == 'y':
                print(show_keys(objectt))
                parametr = input("Enter the name of the field or press Enter to finish: ")
                if parametr == '':
                    return
                objectt = objectt[parametr]
            elif answer.lower() != 'n':
                print('Error (you should enter "y" or "n"')
                return
            else:
                return

        elif isinstance(objectt, list):
            answer = input('Do you want to see whole array? [y/n]: ')
            if answer.lower() == 'y':
                pprint(objectt)
            elif answer.lower() != 'n':
                print('Error (you should enter "y" or "n"')
                return
            answer = input('Do you want to choose an object [y/n]: ')
            if answer.lower() == 'y':
                index = input('Enter index or press Enter to finish: ')
                if index == '':
                    return
                objectt = objectt[int(index)]
            elif answer.lower() != 'n':
                print('Error (you should enter "y" or "n"')
                return
            else:
                return

        else:
            print(objectt)
            return

if __name__ == "__main__":
    #import doctest
    #print(doctest.testmod())
    main()
