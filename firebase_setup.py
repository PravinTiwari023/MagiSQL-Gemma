import pyrebase

# Pyrebase config setup
config = {
    "apiKey": "AIzaSyDXdVcsrfr--lnPV-PkiaDrd8CU2X9MwAI",
    "authDomain": "magisql-gemma-b1a7c.firebaseapp.com",
    "databaseURL": "https://magisql-gemma-b1a7c-default-rtdb.firebaseio.com",
    "projectId": "magisql-gemma-b1a7c",
    "storageBucket": "magisql-gemma-b1a7c.appspot.com",
    "messagingSenderId": "190184286002",
    "appId": "1:190184286002:web:4f885d3f961f9cce54592b",
}

# Initialize Pyrebase app
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()