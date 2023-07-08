import requests

API_KEY = "e2a9e7bbcfc0df66296ae3a8116161b239dfb"
BASE_URL = 'https://cutt.ly/api/api.php'

def shorten_link(full_link, link_name):
    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    print('')

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print('Title:', title)
        print('Link:', short_link)
    except KeyError:
        status = data['url']['status']
        print('Error Status:', status)

        link = input('Enter a link: >> ')
        name = input('Give your link a name: >> ')

        shorten_link(link, name)


# Example usage
link = input('Enter a link: >> ')
name = input('Give your link a name: >> ')
shorten_link(link, name)
