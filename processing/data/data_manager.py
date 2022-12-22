from pathlib import Path
from typing import List, Union

from loguru import logger
from picsellia import Client
from picsellia.exceptions import NoDataError, ResourceNotFoundError
from picsellia.sdk.data import Data, MultiData
from picsellia.sdk.datalake import Datalake
from picsellia.sdk.dataset import Dataset, DatasetVersion
from picsellia.sdk.label import Label
from picsellia.types.enums import InferenceType


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


def create_dataset(
    client: Client,
    name: str,
    description: str
    ) -> Dataset:
    """ Create dataset with data from the Datalake."""

    try:
        dataset = client.get_dataset(name)
    except ResourceNotFoundError:
        dataset = client.create_dataset(name, description)
    return dataset


def create_dataset_version(
    dataset: Dataset,
    version: str,
    description: str
    ) -> DatasetVersion:
    """ Create a dataset version."""
    try:
        dataset_version = dataset.get_version(version)
    except ResourceNotFoundError: 
        dataset_version = dataset.create_version(version=version, description=description)
    return dataset_version


def retrieve_data_with_tags(
    datalake: Datalake,
    tags: Union[str, List[str]]
    ) -> Union[Data, MultiData]:
    """ Retrieve data from the Datalake by tags """

    if not tags:
        raise RuntimeError(f"{tags} should not be empty")

    k = 1
    intersect_data = {data.id: data for data in datalake.list_data(tags=tags[0])}
    while k < len(tags) and len(intersect_data) > 0:
        retrieved_data = [data.id for data in datalake.list_data(tags=tags[k]).items]
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


def add_data_to_dataset(
    client: Client,
    dataset_version: DatasetVersion,
    nb_of_data: int | None,
    tags: Union[str, List[str]],
    dataset_type: InferenceType 
    ):
    """ 
    Add data from the Datalake to a dataset version.
    You can choose a limited number of data by using tags 
    to be added to your dataset.
    """

    # Get Datalake
    datalake = client.get_datalake()
    logger.info(f"The data your are retrieving have these {tags}")
    # Fetch data from the Datalake to be used in your dataset
    data = retrieve_data_with_tags(datalake, tags)
    # Adding data to dataset is a time intensive task. 
    # Therefore it is recommended to run it asynchronously. 
    job = dataset_version.add_data(data)
    job.wait_for_done()

    # Set dataset type
    # The supported types are "CLASSIFICATION", "LINE", "MULTI",
    # "POINT", "SEGMENTATION" or "OBJECT_DETECTION" or "NOT_CONFIGURED".
    dataset_version.set_type(type=dataset_type)


def add_labels(
    dataset_version: DatasetVersion,
    labels: Union[str, List[str]]
    )-> Union[Label, List[Label]]:
    """ Add labels to a dataset."""

    labels = [dataset_version.get_or_create_label(name=label) for label in labels]
    return labels


