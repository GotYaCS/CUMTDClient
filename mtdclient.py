import json
import requests
import datetime
import urllib.parse as urlp
from urllib.request import urlopen
from collections import namedtuple

api_endpoint = "https://developer.cumtd.com/api/v2.2/json/"

class MTDClient:
    def __init__(self, key):
        self.key = key  

    def get_stops(self):
        api_method = 'getstops?key='
        base_url = api_endpoint + api_method + self.key
        params = ''
        page_json_data = requests.get(base_url+params).json()
        return page_json_data

    def get_departures_by_stop(self, stop_id):        
        api_method = 'getdeparturesbystop?key='
        base_url = api_endpoint + api_method + self.key
        params = '&stop_id='+ stop_id

        page_json_data = requests.get(base_url+params).json()
        return page_json_data
    



