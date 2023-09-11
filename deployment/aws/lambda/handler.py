"""AWS Lambda handler."""

import logging
import os

from mangum import Mangum

from titiler.application.main import app

logging.getLogger("mangum.lifespan").setLevel(logging.ERROR)
logging.getLogger("mangum.http").setLevel(logging.ERROR)

REQUEST_HOST_HEADER_OVERRIDE_ENV_VAR = "REQUEST_HOST_HEADER_OVERRIDE"

def handler(event, context):
    if REQUEST_HOST_HEADER_OVERRIDE_ENV_VAR in os.environ and os.environ[REQUEST_HOST_HEADER_OVERRIDE_ENV_VAR] != "":
        event["headers"]["host"] = os.environ[REQUEST_HOST_HEADER_OVERRIDE_ENV_VAR]

    asgi_handler = Mangum(app, lifespan="auto")
    return asgi_handler(event, context)
