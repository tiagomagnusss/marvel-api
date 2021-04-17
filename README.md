# marvel-api
This project uses the [Marvel API](https://developer.marvel.com/) to generate an HTML page containing a story's title, description and its characters (represented by their thumbnail and their name).

## Configuration
Inside the config.ini file you can specify which story ID to gather from the API. Also, you must specify both your **PUBLIC KEY** and **PRIVATE KEY**, otherwise the generator won't be able to access the API. To generate your API keys, follow the instructions at [the docs](https://developer.marvel.com/account).

## Dependencies
To correctly run this code you need the following dependencies installed:
* Python>=3.9.4;
* [Tailwind CSS](https://tailwindcss.com/) (automatically imported inside the HTML)

The following dependencies are Python packages and can be installed by running
```
python -m pip install -r requirements.txt
```

Python packages:
  * Jinja2>=2.11.3;
  * requests>=2.25.1

## Running
After all the configurations are done, you can generate your favorite story's HTML by simply running the **generate.py** script:
```
python generate.py
```

The output will be placed on the root folder and will be named "output.html".



