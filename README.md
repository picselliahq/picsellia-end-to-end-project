# Picsellia 🥑 end-to-end project
This repository showcases the implementation of an end-to-end Computer Vision project using Picsellia 🥑 with a use case on object detection. 

The following are the steps which are covered within this project: 
- 💾 Data management
- 📈 Model training & monitoring 
- 🚀 Deployment to production
- 🏹 Inference with the deployed model 
- 🔁 Continuous training and deployment


## Setup a virtual environment 

In order to isolate the dependencies used in this project, setting up a Python virtual environment to run this projects recommended. 

Run the following commands in your project folder: 

```shell
cd project_folder
python -m venv <venv_directory> 
```

Activate the virtual environment you created by executing this command (as an example, my venv is called myvenv): 

```shell
source myvenv/bin/activate 
```

## Setup the environment variables 

Create a `.env` file in the root directory of this project and add to it your **API_TOKEN** 
that you can retrieve it in your profile page on Picsellia and your **ORGANIZATION_ID** that you can retrieve from the url in the browser in this format: https://app.picsellia.com/ORGANIZATION_ID/dashboard

```
API_TOKEN="YOUR_API_TOKEN"
ORGANIZATION_ID="YOUR_ORGANIZATION_ID"
```

# 💾 Data management 

In Computer Vision projects, data management is the most time consuming step. 

With Picsellia 🥑, this is no longer the case! 

## 1. Upload your data to the Datalake 

By storing all your data in the Datalake, you can take advantage from the following features:
- Visualize all your data and have an overview on its metadata.
- Search easily by using tags and Picsellia's querying language.
- Filter and modify your data easily via the UI.
- Import your data from a third party data storage service. 

![datalake](/docs/datalake.png)

You can upload your data to the Datalake in two ways: 
- Via Picsellia platform UI by navigating to the Datalake tab and following the steps after clicking the button **upload data**. 
- Via Picsellia's Python SDK by running the following command in your terminal: 
````
python upload_data.py
````

If you choose to upload your data via the sdk, take into account to update the `config.py` file. In the [config.py](config.py) file you can precise the path to your data (e.g train, test, val) in your local machine, and the tags you want to use to identify your uploaded data. 

## 2. Create a dataset with data from the Datalake

You will now create a dataset with the data that you need from your Datalake. 
Since you have added tags when uploading your data to the Datalake, now you can leverage the capabilities of retrieving data with the tags, to create respective dataset versions e.g **train** version, **test** version and **valid** version. 

To do that, you can follow either of the following ways: 
- Through Picsellia's platform UI using the **query language** to select data with the tags that you precise and then by clicking on **Create dataset** as shown below:

![create dataset](/docs/create_dataset.png)

- Via Picsellia's Python SDK by doing the necessary configuration in the [config.py](config.py) file. The most important configurations to note are the **TAGS**, **DATASET_VERSION**, **DATASET_TYPE**, **LABELS**: 
````python
# Dataset 
DATASET_NAME = "your-dataset-name"
DATASET_DESCRIPTION = "you dataset description"
NB_OF_DATA = <number of data to retrieve> 
TAGS = ["tag1", "tag2"]

# Dataset version
DATASET_VERSION = "train"
DATASET_VERSION_DESCRIPTION = "training version"
DATASET_TYPE = InferenceType.OBJECT_DETECTION
LABELS = ["label1","label2"]
````
- Then, running the following command in your terminal as many times as you need to create your different dataset versions after changing the configuration in each time you run it:
````shell
python create_dataset.py
````

One thing to note about the **DATASET_TYPE** is that Picsellia supports the following types: `"CLASSIFICATION"`, `"LINE"`, `"MULTI"`, `"POINT"`, `"SEGMENTATION"`, `"OBJECT_DETECTION"` or `"NOT_CONFIGURED"`. So make sure to choose the appropriate type to the task you want to perform with your dataset. To do that, you can edit the [config.py](config.py) file. As an example as shown below the `InferenceType` is OBJECT_DETECTION: 

````python
DATASET_TYPE = InferenceType.OBJECT_DETECTION
````

After doing the described steps to create three dataset versions: **train**, **test** and **valid**, this is the result you should get by navigating to the **Datasets** tab on Picsellia:

![datasets](/docs/datasets.png)

## 3. Annotation 

Once you have created your dataset and the different dataset versions you need, at that point, you do not have the annotations yet.  

So two cases could be possible here: 
-  **If you have the annotations:** 
Supposing that you have the annotation files available on your local machine respective to the dataset versions you have created. You could simply upload them via Picsellia's platform UI as shown below, by navigating to the dataset version and clicking on the button **Annotations** then **Import annotations** 

![annotation](/docs/import_annotations.png)

 - **If you do not have the annotations:**
  Picsellia has its annotation tool. You could easily use it to annotate your data from scratch. By navigating to the dataset version, once you hover on an image, you can click on **Annotate** and you will by landing on the annotation tool. But first, make sure to set the labels before you do the annotations by navigating to the **settings** tab in the dataset version you are in and add the labels as shown below: 

![annotation](/docs/labels.png)

Then you will be able to annotate as shown below: 

![annotation](/docs/annotation_tool.png)

Once your dataset is fully annotated, you can leverage the **Analytics tab** to have an overview on the different metrics e.g data distribution, dataset balance, etc. as shown below: 

![annotation](/docs/dataset_analytics.png)

# 📈 Model training & monitoring

After completing the data management workflow, you should be all set to create your project and start launching training experiments. 

## 1. Create a project 

To grant that you have an overview on the different experiments, you start by creating a project by navigating to the **Projects tab** as shown below: 

![create_project](/docs/create_project.png)

Click on **New project** and fill in the needed information and add from your team who you want to collaborate with to work on this project, as shown below: 

![project](/docs/project.png)

## 2. Attach a dataset to your project 
Once you have created your project, the first thing you need to do it to attach a dataset to it by choosing a dataset version to run your experiments on. You can do that by navigating to your project interface as shown below: 

![attach_dataset](/docs/attach_dataset.png)

## 3. Create experiments

An experiment is a great way to keep track on the traceability of your training. For instance, through the experiment you can have an overview on which model you used for the training, which dataset and dataset version you trained on, as well as the hyperparameters of your model, etc.  

to create an experiment, navigate to your project interface and add a new experiment as shown below: 

![create_experiment](/docs/create_experiment.png)

Give your experiment a name (as a recommendation, indicate the model you used in your experiment name), choose a base architecture either from your organization or from the public models hub and choose a dataset version. You can also edit the hyperparameters of your chosen model. 

After filling the form, you should have such result as shown below: 

![experiment](/docs/experiment.png)








 







