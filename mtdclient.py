import json
import requests
import datetime
from urllib.request import urlopen
from Helpers.web import join_url_path
from collections import namedtuple

api_endpoint = "https://developer.cumtd.com/api/v2.2/json/?key="

class MTDClient:
	def __init__(self, key: str):
		self.key = key
		api_endpoint = join_url_path(api_endpoint,self.key)

	def get_stops(self):
		pass

	def get_departures_by_stop(self, stop_id: str)
		pass

	



