from picsellia import Client

import config
from processing.data.data_manager import upload_data_to_datalake_with_tags


if __name__ == "__main__":
    # Connect to Picsellia 
    client = Client(
    api_token=config.API_TOKEN,
    organization_id=config.ORGANIZATION_ID
    )

    # Upload train data to the Datalake 
    upload_data_to_datalake_with_tags(
        client=client,
        folder_path=config.TRAIN_DATA_DIR,
        tags=[config.CARTONS_TAG, config.TRAIN_TAG]
    )

    # Upload test data to the Datalake 
    upload_data_to_datalake_with_tags(
        client=client,
        folder_path=config.TEST_DATA_DIR,
        tags=[config.CARTONS_TAG, config.TEST_TAG]
    )

    # Upload validation data to the Datalake 
    upload_data_to_datalake_with_tags(
        client=client,
        folder_path=config.VALID_DATA_DIR,
        tags=[config.CARTONS_TAG, config.VALID_TAG]
    )

