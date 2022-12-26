from picsellia import Client
from picsellia.exceptions import ResourceNotFoundError

import config


if __name__ == "__main__":
    # Connect to Picsellia. 
    client = Client(
    api_token=config.API_TOKEN,
    ORGANIZATION_NAME=config.ORGANIZATION_NAME
    )

    # Get your project. 
    my_project = client.get_project(project_name=config.PROJECT_NAME)

    # Get a base model from the model registry under your organization. 
    base_model = client.get_model(name=config.MODEL_NAME)

    # Get a base model version. 
    base_model_version = base_model.get_version(version=config.MODEL_VERSION)

    # Create or get an experiment.
    try:
        my_experiment = my_project.get_experiment(name=config.EXPERIMENT_NAME)
    except ResourceNotFoundError: 
        my_experiment = my_project.create_experiment(
            name=config.EXPERIMENT_NAME,
            description=config.EXPERIMENT_DESCRIPTION,
            base_experiment=None,
            base_model_version=base_model_version
        )

    # Get a dataset to use in your experiment.
    my_dataset = client.get_dataset(name=config.EXPERIMENT_DATASET_NAME)

    # Get a dataset version to use in your experiment. 
    my_dataset_version = my_dataset.get_version(version=config.EXPERIMENT_DATASET_VERSION)

    # Retrieve or create a dataset version and attach it to your experiment. 
    my_experiment.attach_dataset(
        name=config.EXPERIMENT_DATASET_VERSION,
        dataset_version=my_dataset_version
    )


    



