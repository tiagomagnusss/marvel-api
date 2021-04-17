import configparser
from jinja2 import Environment, FileSystemLoader, select_autoescape
from services.marvel_manager import MarvelManager
env = Environment(
	loader=FileSystemLoader("templates/"),
	autoescape=select_autoescape(["html"])
)

# read configs
config = configparser.ConfigParser()
config.read("config.ini")

keys = config["KEYS"]
api_spec = config["API_SPEC"]
character = config["CHARACTER"]

# gets the story data
try:
	manager = MarvelManager(dict(keys), dict(api_spec))
except:
	exit(1)

story = manager.getStory( character.get("STORY_ID") )

# fetch each character
try:
	results = story["data"]["results"][0]
	storyData = {
		"title": results.get("title", "No title"),
		"description": results.get("description", "No description"),
		"attributionText": story.get("attributionText")
	}
except KeyError as e:
	print("Couldn't find the story data")
	exit(1)

characters = []
for char in results["characters"]["items"]:
	charData = manager.getCharacter(char["name"])
	thumb = charData["data"]["results"][0]["thumbnail"]

	try:
		thumbnail = thumb["path"] + "." + thumb["extension"]
	except:
		thumbnail = ""

	charDict = {
		"name": char.get("name", "No name"),
		"thumbnail": thumbnail
	}
	characters.append(charDict)

# generates the output
template = env.get_template("marvel_template.html")
output = template.render(characters=characters, story=storyData)

# encodes the page
with open("output.html", "wb+") as f:
	f.write(output.encode("utf-8"))

print("Succesfully generated. Exiting...")
