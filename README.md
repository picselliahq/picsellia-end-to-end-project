# Picsellia 🥑 end-to-end project
This repository showcases the implementation of an end-to-end Computer Vision project using Picsellia 🥑 with a use case on object detection. 

The following are the steps which are covered within this project: 
- 💾 Data management
- 📈 Model training & monitoring 
- 🚀 Deployment to production
- 🏹 Inference with the deployed model 
- 🔁 Continuous training and deployment


## Setup a virtual environment 

In order to isolate the dependencies used in this project, we recommend setting up a Python virtual environment to run this project. 

Run the following command in your project folder: 

```shell
cd project_folder
python -m venv <venv_directory> 
```

Activate the virtual environment you created by executing this command (as an example, my venv is called myvenv): 

```shell
source myvenv/bin/activate 
```

## Setup the environment variables 

Create a `.env` file in the root directory of this project and add to it your API Token. 
You can retrieve it in your profile page on Picsellia. 

```
API_TOKEN="YOUR_API_TOKEN"
ORGANIZATION_ID="YOUR_ORGANIZATION_ID"
```

## 💾 Data management 

In Computer Vision projects, data management is the most time consuming step. 

With Picsellia 🥑, this is no longer the case! 

### 1. Upload your data to the Datalake 

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



