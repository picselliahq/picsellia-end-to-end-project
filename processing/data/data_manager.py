from pathlib import Path
from typing import List, Union

from loguru import logger
from picsellia import Client
from picsellia.sdk.data import Data, MultiData


def upload_data_to_datalake_with_tags(
    client: Client,
    folder_path: Path, 
    tags: Union[str, List[str]]
    ) -> Union[Data, MultiData]:
    """
    Upload your data to the Datalake by specifiying the folder 
    path in which your images are stored.
    """

    # Get default datalake to your organization
    datalake = client.get_datalake()
    # Path to the images that will be uploaded to the Datalake
    images = [str(path) for path in folder_path.glob("*.jpg")]
    logger.info(folder_path)
    logger.info(images)
    # Upload data to Datalake 
    data = datalake.upload_data(filepaths=images)

    # Create a data tag in your datalake 
    tags = [datalake.get_or_create_data_tag(tag) for tag in tags]
    # Attach tag to data
    data.add_tags(tags=tags)

    return data




