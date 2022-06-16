from http import client
import requests
import tweepy
import json
import os
import sys
import base64
from dotenv import load_dotenv

load_dotenv("/Users/faisalalbasu/GitHub/literate-octo-barnacle/.env")

oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id = os.environ.get("client_id"),
    redirect_uri = os.environ.get("redirect_uri"),
    scope = ["bookmark.read", "tweet.read", "users.read", "offline.access"],
    client_secret = os.environ.get("client_secret")
)

authorization_url = (oauth2_user_handler.get_authorization_url())
print("Please visit this URL to authorize: " + authorization_url)

authorization_response = input("Paste the full URL you were redirected to: ")
token_url = oauth2_user_handler.get_access_token_url(authorization_response)

access_token = oauth2_user_handler.fetch_token(
    authorization_response = authorization_response,
    token_url = token_url,
    client_id = oauth2_user_handler.client_id,
)

client = tweepy.Client()
