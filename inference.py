import json
from pathlib import Path

import requests
from loguru import logger
from picsellia import Client

import config


if __name__ == "__main__":
    # Connect to Picsellia. 
    client = Client(
    api_token=config.API_TOKEN,
    organization_name=config.ORGANIZATION_NAME
    )

    # Get deployment by name.
    my_deployment = client.get_deployment(name=config.DEPLOYMENT_NAME)

    # Get your deployment ID.
    deployment_id = str(my_deployment.id)

    # Get your API token from your profile. 
    api_token = str(config.API_TOKEN)

    # Authentication url 
    auth_url = "https://serving.picsellia.com/api/login"

    headers = {
        "Authorization": "Token " + api_token,
    }

    jwt_generation_data = {
        "deployment_id": deployment_id,
        "api_token": api_token
    }

    jwt_request = requests.post(
        auth_url,
        headers=headers,
        data=json.dumps(jwt_generation_data)
    )

    # Retrieving the JWT. 
    jwt = jwt_request.json()["jwt"]

    # Serving API endpoint 
    url = "https://serving.picsellia.com/api/deployment/{}/predict".format(my_deployment.id)

    header = {
        "Authorization": "Bearer " + jwt,
    }

    # Metadata that helps extrat data from datalake.
    data = {
        "source": "camera1",   
        "tag": "Cartons"     
    }
    
    images_folder = config.INFERENCE_DATA_DIR

    images_path = Path(images_folder).glob('*.jpg')

    for image_path in images_path:
        with open(image_path, "rb") as file:
            r = requests.post(
                url=url,
                files={'media': file},
                headers=header,
                data=data
            )
        
    logger.info(r.text)

    prediction = r.json()
    

