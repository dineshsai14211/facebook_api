from apps.constants import *
import apps.constants as const
import logging as log


def is_valid_response(response):
    if response.status_code == 200:
        log.debug(f"{const.PAGE_ID} - {response.json()}")
        return True
    else:
        raise False
