import requests
from logs import logging_logic
import constants as const
import logging as log
from utilis.utility import *


# POST request
def facebook_post():
    log.info(f'{const.PAGE_ID} - has started facebook_post function...')
    try:
        data = {"message": "Github link of profile management repository",
                "link": "https://github.com/dineshsai14211/Profile_Management_flask-",
                "published": True,
                }
        response = requests.post(f"https://graph.facebook.com/{const.PAGE_ID}/feed?access_token={const.ACCESS_TOKEN}",
                                 headers=const.HEADERS, json=data)

        if not is_valid_response(response):
            raise Exception(response)
        return f"Response is {response.json()}"

    except Exception as err:
        log.error(f'{const.PAGE_ID} - {err}')
    finally:
        log.info(f'{const.PAGE_ID} - ended the facebook_post function...')


# POST request
def post_photo():
    log.info(f'{const.PAGE_ID} - has started post_photo function...')
    try:
        data = {
            'message': '#Photooftheday',
            'url': 'https://hips.hearstapps.com/hmg-prod/images/alpe-di-siusi-sunrise-with-sassolungo-or-langkofel-royalty-free-image-1623254127.jpg',
        }

        response = requests.post(
            f'https://graph.facebook.com/v20.0/{const.PAGE_ID}/photos?access_token={const.ACCESS_TOKEN}',
            headers=const.HEADERS, json=data)

        if not is_valid_response(response):
            raise Exception(response)
        return f"Response is {response.json()}"

    except Exception as err:
        log.error(f'{const.PAGE_ID} - {err}')
    finally:
        log.info(f'{const.PAGE_ID} - ended post_photo function...')


# GET Request
def get_posts():
    log.info(f'{const.PAGE_ID} - has started the get_posts function...')
    try:
        response = requests.get(
            f'https://graph.facebook.com/v20.0/{const.PAGE_ID}/feed?access_token={const.ACCESS_TOKEN}')

        if not is_valid_response(response):
            raise Exception(response)
        return f"Response is {response.json()}"

    except Exception as err:
        log.error(f'{const.PAGE_ID} - {err}')
    finally:
        log.info(f'{const.PAGE_ID} - ended get_posts function...')


# DELETE Request
def delete_post():
    log.info(f'{const.PAGE_ID} - has started delete_post functon...')
    try:
        page_post_id = input('Enter the "page_post_id" to delete post = ')
        response = requests.delete(
            f'https://graph.facebook.com/v20.0/{page_post_id}?access_token={const.ACCESS_TOKEN}')

        if not is_valid_response(response):
            raise Exception(response)
        return f"Response is {response.json()}"

    except Exception as err:
        log.error(f'{const.PAGE_ID} - {err}')
    finally:
        log.info(f'{const.PAGE_ID} - ended delete_post function...')


def start_program():
    while True:
        options = int(input(const.OPTION))
        if options == 1:
            print(facebook_post())
        elif options == 2:
            print(post_photo())
        elif options == 3:
            print(get_posts())
        elif options == 4:
            print(delete_post())
        elif options == 5:
            break
        else:
            print("Entered wrong option...choose frm these")
            options = int(input(const.OPTION))

start_program()