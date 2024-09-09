"""
This module contains the functionalities of making a post with photo or without on facebook
and getting posts information, deleting the post through facebook API's with access token.
"""

# Third party library imports
import requests

# Standard Imports
import copy
import os 

# Local Imports
from utilis.utility import *


# POST request
def facebook_post(page_id):
    """
    Function used to create a Facebook post
    :return: Json
    """
    log.info(f'{page_id} - has started facebook_post function...')
    try:
        payload = copy.copy(C.PAYLOAD)
        payload["message"] = C.GIT_MSG
        payload["link"] = C.REPO_LINK
        payload["published"] = True

        URL = C.GRAPH_API + page_id + C.POST_URI + C.ACCESS_TOKEN
        log.debug(f'{page_id} - Endpoint URL is {URL}')

        response = requests.post(url=URL,
                                 headers=C.HEADERS, json=payload)

        if is_valid_response(response):
            return success_response(response, page_id)

        return failure_response(response, page_id)

    except Exception as err:
        log.error(f'{page_id} - Error is {err}')

    finally:
        log.info(f'{page_id} - ended the facebook_post function...')


# POST request
def facebook_post_with_photo(page_id):
    """
    These function used to make a facebook post with photo
    :param page_id: str
    :return: json
    """
    log.info(f'{page_id} - has started post_photo function...')
    try:
        payload = copy.copy(C.PAYLOAD_WITH_PHOTO)
        payload["message"] = C.MESSAGE
        payload["url"] = C.PHOTO_URL

        URL = C.GRAPH_API + page_id + C.POST_PHOTO_URL + C.ACCESS_TOKEN
        log.debug(f'{page_id} - Endpoint URL is {URL}')

        response = requests.post(url=URL,
                                 headers=C.HEADERS, json=payload)

        if is_valid_response(response):
            return success_response(response, page_id)

        return failure_response(response, page_id)
    except Exception as err:
        log.error(f'{page_id} - Error is - {err}')

    finally:
        log.info(f'{page_id} - ended post_photo function...')


# GET Request
def get_posts_info(page_id):
    """
    This function is used to get the posts information of that particular page
    :return: json
    """
    log.info(f'{page_id} - has started the get_posts function...')
    try:
        URL = C.GRAPH_API + page_id + C.POST_URI + C.ACCESS_TOKEN
        log.debug(f'{page_id} - Endpoint URL is {URL}')

        response = requests.get(url=URL)

        if is_valid_response(response):
            return success_response(response, page_id)
        return failure_response(response, page_id)

    except Exception as err:
        log.error(f'{page_id} - Error is - {err}')
    finally:
        log.info(f'{page_id} - ended get_posts function...')


# DELETE Request
def delete_post(page_id):
    """
    This function is used to delete the post on that particular page using page_post_id.
    :return: json
    """
    log.info(f'{page_id} - has started delete_post functon...')
    try:
        page_post_id = input('Enter the "page_post_id" to delete post = ')

        URL = C.GRAPH_API + page_post_id + "?access_token=" + C.ACCESS_TOKEN
        log.debug(f'{page_id} - Endpoint URL is {URL}')

        response = requests.delete(url=URL)

        if is_valid_response(response):
            return success_response(response, page_id)
        return failure_response(response, page_id)

    except Exception as err:
        log.error(f'{page_id} - {err}')
    finally:
        log.info(f'{page_id} - ended delete_post function...')
