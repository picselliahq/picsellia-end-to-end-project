from loguru import logger
from picsellia import Client
from picsellia.exceptions import ResourceNotFoundError

import config
from processing.data.data_manager import retrieve_data_with_tags


if __name__ == "__main__":
    # Connect to Picsellia. 
    client = Client(
    api_token=config.API_TOKEN,
    ORGANIZATION_NAME=config.ORGANIZATION_NAME
    )

    # Create a dataset. 
    try:
        dataset = client.get_dataset(name=config.DATASET_NAME)
    except ResourceNotFoundError:
        dataset = client.create_dataset(
        name=config.DATASET_NAME,
        description=config.DATASET_DESCRIPTION
        )


    # Create a dataset version.
    try:
        dataset_version = dataset.get_version(version=config.DATASET_VERSION)
    except ResourceNotFoundError:
        dataset_version = dataset.create_version(
        version=config.DATASET_VERSION,
        description=config.DATASET_DESCRIPTION
        )


    # Add data to the dataset from the Datalake: 
    # Get Datalake.
    datalake = client.get_datalake()

    # Fetch data from the Datalake to be used in your dataset.
    data = retrieve_data_with_tags(datalake, tags = config.TAGS, limit=config.NB_OF_DATA)
    logger.info(f"The data your are retrieving have these tags: {config.TAGS}")
    
    # Adding data to dataset is a time intensive task. 
    # Therefore it is recommended to run it asynchronously. 
    job = dataset_version.add_data(data)
    job.wait_for_done()

    # Set dataset type
    # The supported types are "CLASSIFICATION", "LINE", "MULTI",
    # "POINT", "SEGMENTATION" or "OBJECT_DETECTION" or "NOT_CONFIGURED".
    dataset_version.set_type(type=config.DATASET_TYPE)

    # Add labels to your dataset 
    labels = [dataset_version.get_or_create_label(name=label) for label in config.LABELS]
