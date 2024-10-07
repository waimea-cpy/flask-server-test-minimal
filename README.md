# Flask Server Test - Minimal

Experimenting with using Flask as a back-end

Trying out [Flask](https://flask.palletsprojects.com) as a simple web back-end. Using [Railway.app](https://railway.app/) for deployment. This is a minimal setup.

## My Requirements

In order to replace the tech. stack I've used for years, I'll need...

- A simple way to serve up basic HTML pages
- A simple routing system
- A simple templating system for pages

Ideally I'll be able to work with the students in VS Code (or possibly PyCharm)

## Setting up a Virtual Environment for Python

Create the virtual environment...

Windows:
```PowerShell
python -m venv venv
.\venv\Scripts\activate
pip install -r .\requirements.txt
```

Linux:
```Bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Launching the Server

Since the project is configured as a module called **app** (with main code in `__init__.py`), then running the server is as simple as:

```Bash
flask run
```

Or to get full debug info...

```Bash
flask run --debug
```

## Deploying to Railway

Deploying to Railway from this repo with no additional tweaking should 'just work'.

All that is required is to specify tha host address to run on (`0.0.0.0`), and to generate a public URL. In the Railway project settings:

#### Build
- Check *Builder* is **DockerFile** (should be auto-detected)

#### Deploy
- Set a *Custom Start Command*:
  ```Bash
  flask run --host=0.0.0.0
  ```

#### Networking
- Select *Generate a Domain* and make sure port is set to **5000** (should be auto-set)




