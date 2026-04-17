import requests
import json
import sys

def main():
    api_url = "https://api.discogs.com"
    request_token_url = "https://api.discogs.com/oauth/request_token"
    auth_url = "https://discogs.com/oauth/authorize"
    access_token = "https://api.discogs.com/oauth/access_token"
    print("Requesting Discogs Authorization")
    
    search = requests.get(f"{api_url}/database/search?q={query}&{?type,title,release_title,credit,artist,anv,label,genre,style,country,year,format,catno,barcode,track,submitter,contributor}"
    {}
    )

def authentication():

def authorize_token():


def request_token():

main()
