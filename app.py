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

    response = requests.post(f"https://graph.facebook.com/v20.0/me/feed?access_token={Access_token}",
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

    response = requests.post('https://graph.facebook.com/v20.0/61564010091393/photos', headers=headers, json=data)
    print(f"Response is {response.json()}")


def get_posts():  # GET Request
    response = requests.get('https://graph.facebook.com/v20.0/61564010091393/feed')
    print(f"Response is {response.json()}")


def delete_post():
    response = requests.delete('https://graph.facebook.com/v20.0/page_post_id')
    print(f"Response is {response.json()}")
