from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
	loader=FileSystemLoader("templates/"),
	autoescape=select_autoescape(["html"])
)

# generates the output
template = env.get_template("marvel_template.html")

characters = {}
storyData = {}
output = template.render(characters=characters, story=storyData)

# encodes the page
with open("output.html", "wb+") as f:
	f.write(output.encode("utf-8"))