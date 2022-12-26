from picsellia import Client

import config
from processing.data.data_manager import import_annotations

if __name__ == "__main__":
    # Connect to Picsellia 
    client = Client(
    api_token=config.API_TOKEN,
    ORGANIZATION_NAME=config.ORGANIZATION_NAME
    )

    import_annotations()