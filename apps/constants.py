ACCESS_TOKEN = os.getenv("access_token")

PAGE_ID = "403714366157679"

HEADERS = {'Content-Type': 'application/json'}

OPTION = "Enter which operation need to perform \n1)Make a post \n2)Make a post with photo \n3)Getting post information \n4)Delete a post \n5)Exit = "

# GitHub Link
REPO_LINK = "https://github.com/dineshsai14211/Profile_Management_flask-"

# Endpoint construction URL's
GRAPH_API = "https://graph.facebook.com/"
POST_URI = "/feed?access_token="
POST_PHOTO_URL = "/photos?access_token="

# Image URL
PHOTO_URL = "https://hips.hearstapps.com/hmg-prod/images/alpe-di-siusi-sunrise-with-sassolungo-or-langkofel-royalty-free-image-1623254127.jpg"

# Body Messages
PAYLOAD = {"message": None, "link": None, "published": None}

PAYLOAD_WITH_PHOTO = {"message": None, "url": None}

# Normal Message
MESSAGE = "#Photooftheday"
GIT_MSG = "Github link of profile management repository"

# https://graph.facebook.com/v20.0/{const.PAGE_ID}/feed?access_token={const.ACCESS_TOKEN}
