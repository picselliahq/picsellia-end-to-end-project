from pathlib import Path
from typing import List, Union

from loguru import logger
from picsellia import Client
from picsellia.exceptions import NoDataError
from picsellia.sdk.data import Data, MultiData
from picsellia.sdk.datalake import Datalake
from picsellia.sdk.dataset import DatasetVersion
from picsellia.types.enums import ImportAnnotationMode


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


def retrieve_data_with_tags(
    datalake: Datalake,
    tags: Union[str, List[str]],
    limit: int | None
    ) -> Union[Data, MultiData]:
    """ Retrieve data from the Datalake by tags. """

    if not tags:
        raise RuntimeError(f"{tags} should not be empty")

    k = 1
    intersect_data = {data.id: data for data in datalake.list_data(limit ,tags=tags[0])}
    while k < len(tags) and len(intersect_data) > 0:
        retrieved_data = [data.id for data in datalake.list_data(limit, tags=tags[k]).items]
        k += 1
        
        for id_data in list(intersect_data.keys()):
            if id_data not in retrieved_data:
                del intersect_data[id_data]

    intersect_data = list(intersect_data.values())
    if not intersect_data:
        raise NoDataError()
    elif len(intersect_data) == 1:
        return intersect_data[0]
    else:
        return MultiData(intersect_data[0].connexion, intersect_data[0].datalake_id, intersect_data)


def import_annotations(
    client: Client,
    dataset_version: DatasetVersion,
    annotation_file_path: str,
    annotation_file_type: str,
    mode: ImportAnnotationMode
    ):
    """
    Import annotation(s) file(s) to your dataset.
    The supported annotation file formats are COCO and Pascal Voc.
    """

