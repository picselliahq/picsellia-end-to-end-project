from picsellia import Client

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
        type=config.DATASET_TYPE,
        framework=config.FRAMEWORK,
        description=config.MODEL_DESCRIPTION
    )

    # Model parameters 
    parameters = {
        "steps": config.STEPS,
        "lr_type": config.LR_TYPE,
        "batch_size": config.BATCH_SIZE,
        "decay_steps": config.DECAY_STEPS,
        "decay_factor": config.DECAY_FACTOR,
        "learning_rate": config.LEARNING_RATE,
        "annotation_type": config.ANNOTATION_TYPE 
    }

    # It's important that the labels keys starts at "1".
    labels = { 
        "1": config.LABELS[0],
        "2": config.LABELS[1]
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

