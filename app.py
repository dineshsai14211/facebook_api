import requests
import json

Access_token = ''


def facebook_post():  # POST request
    headers = {
        'Content-Type': 'application/json',
    }
    data = {"message": "Github link of profile management repository",
            "link": "https://github.com/dineshsai14211/Profile_Management_flask-",
            "published": True,
            }

    response = requests.post(f"https://graph.facebook.com/367234763145366/feed?access_token={Access_token}",
                             headers=headers, data=json.dumps(data))
    print(response)
    print(f"Response is {response.json()}")


facebook_post()


def post_photo():  # POST request
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'message': '#Photooftheday',
        'url': 'https://hips.hearstapps.com/hmg-prod/images/alpe-di-siusi-sunrise-with-sassolungo-or-langkofel-royalty-free-image-1623254127.jpg',
    }

    response = requests.post(f'https://graph.facebook.com/v20.0/367234763145366/photos?access_token={Access_token}',
                             headers=headers, json=data)
    print(f"Response is {response.json()}")


post_photo()


def get_posts():  # GET Request
    response = requests.get(f'https://graph.facebook.com/v20.0/367234763145366/feed?access_token={Access_token}')
    print(f"Response is {response.json()}")


get_posts()


def delete_post():  # DELETE Request
    response = requests.delete(
        f'https://graph.facebook.com/v20.0/367234763145366_122094606962466172?access_token={Access_token}')
    print(f"Response is {response.json()}")


delete_post()
