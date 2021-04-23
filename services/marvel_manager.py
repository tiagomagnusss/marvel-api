import requests
import hashlib
import time

class MarvelManager:
	""" Manager to fetch data from the Marvel API """
	def __init__(self, keys: dict, spec: dict):
		try:
			self.host = spec["host"]
			self.version = spec["version"]
			self.public_key = keys["public_key"]
			self.private_key = keys["private_key"]
		except KeyError as e:
			print("Can't run without all the configurations.")
			print(f"{e} missing")
			raise(e)

	def __request__(self, endpoint: str, params: dict={}) -> dict:
		"""
		Make a request to the Marvle API using the given configuration

		Args:
			endpoint (str): The endpoint to hit
			params (dict, optional): Optional dict of query parameters

		Raises:
			Exception: Raised if status code is not OK

		Returns:
			dict: API response
		"""
		# hashes according to the API specification
		# see: https://developer.marvel.com/documentation/authorization
		ts = int(time.time())
		encoded = hashlib.md5( (str(ts) + self.private_key + self.public_key).encode() ).hexdigest()
		authparams = {
			"ts": ts,
			"apikey": self.public_key,
			"hash": encoded
		}
		response = requests.get( self.host + self.version + endpoint, params=authparams | params)

		if ( response.status_code != 200 ):
			raise Exception(f"Failed to fetch data. REASON: {response.reason}; TEXT: {response.text}")

		return response.json()

	def get_story(self, id: int) -> dict:
		"""
		Get a story with an specific ID

		Args:
			 id (int): Story identifier

		Returns:
			 dict: JSON
		"""
		return self.__request__(f"stories/{id}")

	def get_character(self, name: str) -> dict:
		"""
		Get a character given its name

		Args:
			 name (str): Character's name

		Returns:
			 dict: JSON
		"""
		return self.__request__(f"characters", {"name": name})