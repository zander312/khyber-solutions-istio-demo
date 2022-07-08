import os
import time
import socket
from faker import Faker
from flask import Flask
from random import randrange

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
        "product-data": {
            "id": fake.ean(length=8),
            "product": fake.catch_phrase(),
            "quantity": randrange(100, 1000)
        }
    }


# ROUTES
@app.route('/')
def index():
    return payload()
