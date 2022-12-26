from picsellia import Client
from picsellia.types.enums import InferenceType
from picsellia.sdk.model import Framework

import config


if __name__ == "__main__":
    # Connect to Picsellia. 
    client = Client(
    api_token=config.API_TOKEN,
    ORGANIZATION_NAME=config.ORGANIZATION_NAME
    )

    # Create a new model. 
    my_custom_model = client.create_model(
        name=config.MODEL_NAME,
        type=InferenceType.OBJECT_DETECTION,
        framework=Framework.TENSORFLOW,
        description=config.MODEL_DESCRIPTION
    )

    # Model parameters 
    parameters = {
        "steps": 1000,
        "lr_type": "exponential_decay",
        "batch_size": 4,
        "decay_steps": 500,
        "decay_factor": "0.9",
        "learning_rate": 0.001,
        "annotation_type": "rectangle" 
    }

    # It's important that the labels keys starts at "1".
    labels = { 
        "1": "Energy_Tiffin",
        "2": "Energy_Regular"
    }

    # Create a model version  
    model_version = my_custom_model.create_version(
        base_parameters=parameters,
        labels=labels
    )

    # Register model on Picsellia and store its artifacts 
    model_version.store(
        name=str(config.ARTIFACTS_NAME),
        path=str(config.ARTIFACTS_DIR)
    )

