from flask import Flask, render_template as rt, request as fr, redirect, url_for as uf
from urllib import request as urlrequest, response as urlresponse, parse as urlparse
import requests as r
import tweepy
import json
import os
import base64
from dotenv import load_dotenv

load_dotenv("/Users/faisalalbasu/GitHub/literate-octo-barnacle/.env")

oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id = os.environ.get("client_id"),
    redirect_uri = os.environ.get("redirect_uri"),
    scope = ["bookmark.read", "tweet.read", "users.read", "offline.access"],
    client_secret = os.environ.get("client_secret")
)

endpoint = "https://api.twitter.com/2/users/:id/bookmarks"

authorization_url = (oauth2_user_handler.get_authorization_url())
print("Please visit this URL to authorize: " + authorization_url)

authorization_response = (oauth2_user_handler.redirect_uri)
token_url = "https://api.twitter.com/2/oauth2/token"

access_token = oauth2_user_handler.fetch_token(
    # token_url,
    authorization_response = authorization_response,
)['access_token']

client = tweepy.Client(access_token)

user = r.request(
    "GET",
    "https://api.twitter.com/2/users/me"
).json()

user_id = user['data']['id']




# user = requests.request(
#     "GET",
#     user_endpoint = "https://api.twitter.com/2/users/me",
#     headers={'Authorization': 'Bearer {}'.format(access)}
# ).json()

# # user_endpoint = "https://api.twitter.com/2/users/me"
# user_id = user['data']['id']
# bookmarks_endpoint = "https://api.twitter.com/2/users/{}/bookmarks".format(user_id)

# headers = {
#     'Authorization': 'Bearer {}'.format(access),
#     'User-Agent': 'BookmarksSampleCode',
# }

# response = requests.request("GET", bookmarks_endpoint, headers=headers)

# if response.status_code != 200:
#     raise Exception(
#         "Request Error: {} {}".format(response.status_code, response.text)
#     )
# print("Response: {}".format(response.status_code))
# json_response = response.json()
# print(json.dumps(json_response, indent=4, sort_keys=True))