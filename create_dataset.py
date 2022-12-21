from picsellia import Client
import config 


from processing.data.data_manager import (
    create_dataset_version,
    create_dataset,
    add_data_to_dataset,
    add_labels
) 


if __name__ == "__main__":
    # Connect to Picsellia 
    client = Client(
    api_token=config.API_TOKEN,
    organization_id=config.ORGANIZATION_ID
    )


    # Create a dataset 
    dataset = create_dataset(
        client=client,
        name=config.DATASET_NAME,
        description=config.DATASET_DESCRIPTION
    )

    # Create a dataset version
    dataset_version = create_dataset_version(
        dataset=dataset,
        version=config.DATASET_VERSION,
        description=config.DATASET_VERSION_DESCRIPTION
    )

    # Add data to the dataset from the Datalake
    add_data_to_dataset(
        client=client,
        dataset_version=dataset_version,
        nb_of_data=None,
        dataset_type=config.DATASET_TYPE,
        tags=config.TAGS
    ) 

    # Add labels to a dataset 
    add_labels(
        dataset_version=dataset_version,
        labels=config.LABELS
    )


