## Evernote + Python Sample Application

### Prerequisites

1. Python (you probably already have this; if not, head over to [python.org](http://python.org)
2. Git if you're cloning the SDK from Github
3. PIP if you're using the Python pacakge manager
4. An account on [Evernote's Sandbox](https://sandbox.evernote.com) (our development server)
5. A developer token for your Sandbox account — [get it here](https://sandbox.evernote.com/api/DeveloperToken.action)

### Before running the app

Install the Evernote SDK for Python in one of two ways:

##### Using PIP (recommended)

`pip install evernote` — This may require admin privileges (sudo, etc.)

##### Cloning from Github

`git clone git@github.com:evernote/evernote-sdk-python.git`

`cd evernote-sdk-python && sudo python setup.py install`

Both of these methods will install the SDK such that it's globally available for import; you don't need to copy the SDK into your project (though, you can)

### Running the app

`python main.py`

You'll be prompted for your developer token when you run the app. If you'd rather not be prompted, populate the `auth_token` variable within the app source code (on or around line 20 of `main.py`)
