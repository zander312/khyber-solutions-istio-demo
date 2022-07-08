import os
import time
import socket
from faker import Faker
from flask import Flask

# INIT
fake = Faker()
app = Flask(__name__)


# FUNCTIONS
def payload():
    return {
        "host-data": {
            "app": os.environ.get('APP'),
            "hostname": socket.gethostname(),
            "version": os.uname()[3],
            "epoch": time.time()
        },
        "account-data": fake.simple_profile()
    }


# ROUTES
@app.route('/')
def index():
    return payload()
