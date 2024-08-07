# local Imports
from apps.constants import OPTION, PAGE_ID
from apps.app import *


def start_program():
    """
    This function is used to start the application
    :return: json
    """
    while True:
        options = int(input(OPTION))
        if options == 1:
            print(facebook_post(PAGE_ID))
        elif options == 2:
            print(facebook_post_with_photo(PAGE_ID))
        elif options == 3:
            print(get_posts_info(PAGE_ID))
        elif options == 4:
            print(delete_post(PAGE_ID))
        elif options == 5:
            break
        else:
            print("Entered wrong option...choose from these:-")


start_program()
