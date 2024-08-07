# local import
import apps.constants as C
from logs.logging_logic import *


def is_valid_response(response):
    if response.status_code == 200:
        log.debug(f"{C.PAGE_ID} - {response.json()}")
        return True
    else:
        return False


def success_response(response, page_id):
    log.debug(f"{page_id} - Facebook post successful")
    return {"status": "Success", "message": response.json()}


def failure_response(response, page_id):
    log.error(f"{page_id} - Facebook post failed")
    return {"status": "Failed", "message": response.json()}
