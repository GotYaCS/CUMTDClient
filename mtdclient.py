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

    def get_stops(self,isJson):
        api_method = 'getstops?key='
        base_url = api_endpoint + api_method + self.key
        params = ''
        page_json_data = requests.get(base_url+params).json()
        
        if isJson:
            return page_json_data
        
        stop_entries = []

        for stop_loc in page_json_data["stops"]:
            for stop in stop_loc["stop_points"]:
                stop_entry = namedtuple('stop_entry','stop_id stop_name')
                stop_entry.stop_id = stop["stop_id"]
                stop_entry.stop_name = stop["stop_name"]
                stop_entries.append(stop_entry)
        return stop_entries

    def get_departures_by_stop(self,stop_id,isJson):        
        api_method = 'getdeparturesbystop?key='
        base_url = api_endpoint + api_method + self.key
        params = '&stop_id='+ stop_id

        page_json_data = requests.get(base_url+params).json()
        
        if isJson:
            return page_json_data

        departure_entries = []

        for departure in page_json_data["departures"]:
            depart_entry = namedtuple('depart_entry','stop_id bus expected expected_mins')
            depart_entry.stop_id = departure["stop_id"]
            depart_entry.bus = departure["headsign"]
            depart_entry.expected = departure["expected"]
            depart_entry.expected_mins = departure["expected_mins"]
            departure_entries.append(depart_entry)
        return departure_entries


    



