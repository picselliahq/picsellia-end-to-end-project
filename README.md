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
that you can retrieve it in your profile page on Picsellia (https://app.picsellia.com/ORGANIZATION_NAME/profile#token) and your **ORGANIZATION_NAME** that you can retrieve from the organization settings (https://app.picsellia.com/ORGANIZATION_NAME/settings#informations)

```
API_TOKEN="YOUR_API_TOKEN"
ORGANIZATION_NAME="YOUR_ORGANIZATION_NAME"
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
````python 
# Project & data Directories
ROOT_DIR = Path.cwd().resolve()
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
TRAIN_DATA_DIR = RAW_DATA_DIR / "train"
TEST_DATA_DIR = RAW_DATA_DIR / "test"
VALID_DATA_DIR = RAW_DATA_DIR / "valid"

# Data tags in the Datalake 
TRAIN_TAG = "train"
TEST_TAG = "test"
VALID_TAG = "valid"
LABEL_TAG_X = "label-x"
LABEL_TAG_Y = "label-y"
````

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

Once your dataset is fully annotated, you can leverage the **Analytics tab** to have an overview on the different metrics e.g data distribution, dataset balance, etc, as shown below: 

![annotation](/docs/dataset_analytics.png)

# 📈 Model training & monitoring

After completing the data management workflow, you should be all set to create your project and start launching training experiments. 

## 1. Create a project 

To grant that you have an overview on the different experiments, you start by creating a project by navigating to the **Projects tab**, as shown below: 

![create_project](/docs/create_project.png)

Click on **New project** and fill in the needed information and add from your team who you want to collaborate with to work on this project, as shown below: 

![project](/docs/project.png)

## 2. Attach a dataset to your project 
Once you have created your project, the first thing you need to do it to attach a dataset to it by choosing a dataset version to run your experiments on. You can do that by navigating to your project interface as shown below: 

![attach_dataset](/docs/attach_dataset.png)

## 3. Create experiments

### a. Using a model from Picsellia's model hub 

An experiment is a great way to keep track on the traceability of your training. For instance, through the experiment you can have an overview on which model you used for the training, which dataset and dataset version you trained on, as well as the hyperparameters of your model, etc.  

- To create an experiment, navigate to your project interface and add a new experiment as shown below: 

![create_experiment](/docs/create_experiment.png)

- Give your experiment a name (as a recommendation, indicate the model you used in your experiment name), choose a base architecture either from your organization or from the public models hub and choose a dataset version. You can also edit the hyperparameters of your chosen model. 

After filling the form, you should have such result as shown below: 

![experiment](/docs/efficientdet-d3-experiment.png)

- Once you have setup your experiment with the model and attached a dataset to it, you are all set to launch the training on Picsellia. To do that, navigate to the Launch tab under your experiment tab and you have two options: 
  - Train on Picsellia using a `remote server` (recommended).
  - Train on your own infrastructure by copying the command to run the the `training Docker image` already packaged by Picsellia for a straight forward use. 

![launch training](/docs/efficientdet-d3-launch-training.png)

### b. Using your custom trained model
Supposing that you have trained your own model and you want to benefit from the capabilities of Picsellia to track your model metrics and launch different experiments with different dataset versions based on your trained model, you can follow these steps: 
 
- Add the configuration related to registering your model on Picsellia in the [config.py](config.py) file: 

````python
# Model 
MODEL_NAME = "custom-model-x"
MODEL_DESCRIPTION = "A custom model-x description"

# Trained models & weights directories
MODELS_DIR = ROOT_DIR / "models" 
ARTIFACTS_DIR = MODELS_DIR / "custom-model-x"
ARTIFACTS_NAME = "custom-trained-model-artifacts"

# Custom model parameters
PARAM_1 = "param-1"
PARAM_2 = "param-2"

# Custom model framework 
FRAMEWORK = Framework.TENSORFLOW

# Labels 
LABELS = ["label_1", "label_2"]

# Inference type 
DATASET_TYPE = InferenceType.OBJECT_DETECTION
````
- Register your **custom model** on Picsellia by running the following command: 
````shell
python register_model.py
````
 
 After running this command, you should have registered your model artifacts to Picsellia and once you navigate to the `Models Registry tab`, you should have something like this:

![registered model](/docs/model.png)

 By clicking on your model, you should have an overview on the metadata and parameters of your custom model available on Picsellia and ready to be used in the experiments and for further deployment.  

![registered model](/docs/registered-model.png)

- Create an experiment and make the necessary changes in the [config.py](config.py) file: 

 ````python
# Project 
PROJECT_NAME = "your-project-name"

# Model 
MODEL_NAME = "custom-model-x"
MODEL_VERSION = 0

# Experiment 
EXPERIMENT_NAME = "experiment-model-x"
EXPERIMENT_DESCRIPTION = "experiment1 using model x"
EXPERIMENT_DATASET_VERSION = "train"
EXPERIMENT_DATASET_NAME = "experiment-dataset-name"
````

- Run the following command to create an experiment using your custom model that you just registered: 
````shell
python create_experiment.py
````

## 4. Monitor your experiments 

Picsellia gives you the advantage of tracking your model training metrics to be able to evaluate accurately its performance and robustness. 

### a. View training logs 
Once you launch your training, all you have to do is to navigate to the **logs tab** under your experiment. There you have an overview on the different metrics pre-configured by Picsellia and that you can customize to log your own metrics. 

The figure below shows the logs of the model you trained on Picsellia to perform an object detection task: 

![training logs](/docs/training-logs-gif.gif)

### b. Compare experiments 
Picesllia gives you the flexibility to easily launch multiple experiments with different models and most importantly, it gives you the capability to compare your experiments with minimal effort. 

All you have to do is to click on experiments on your project interface, 
then, select the models that you want to compare as shown below: 

![compare experiment](/docs/compare-experiment.png)

When you click on compare, this is what you should get: 

![compare experiments results](/docs/compare-experiments-gif.gif)

# 🚀 Deployment to production

After comparing your experiments and having a close look into the performance and metrics of the different models, you are able to choose a winning experiment to export as model and deploy to production. 

To export your chosen experiment, you simply click on the button **Export as model** in the experiment logs interface as shown in the figure below: 

![export as model](/docs/export-model.png)

Once you export your model, you can find it under the `Model Regitry` tab. Thanks to Picsellia, you are able to have a visibility on the origin of your model e.g which dataset you used to train that model, model parameters, label map, etc... 

![export as model](/docs/exported-model.png)
 
The next step is to **deploy** your model to production. 

With Picsellia 🥑, it is as easy as a button click! 

By clicking on the button `Deploy` on the model interface, 
you should select one of the deployment options: 
- Deploy on Picsellia serving (recommended)
- Connect your serving with Picsellia's APIs  
- Monitoring only 

![export as model](/docs/deployment-options.png)

Enter a confidence threshold to filter predictions below and avoid noise.

Once the deployment is executed, you should be forwarded to the deployment interface of your model as shown below: 

![export as model](/docs/deployment.png)

As long as you did not any inference requests yet, the deployment dashboard should be still empty. 

# 🏹 Inference with the deployed model

## 1. Make inference requests 
Once your have deployed your model to production 🚀, your are now able to make inference requests and benefit from the monitoring dashboard to track the performance of your model, avoid data drift, etc. 
To do that, follow these steps: 

- First add the needed configuration for the inference in the [config.py](config.py) file: 

 ````python
# Deployment
DEPLOYMENT_NAME = "energetic-cave"
TEST_DATA_DIR = RAW_DATA_DIR / "test"
`````
- Run this command in your terminal to make predictions: 

````shell
python inference.py
````
## 2. Review predictions  
After making your prediction requests, you can leverage Picsellia deployments dashboard to monitor your deployed models. From the dashboard you have an overview on a variety of metrics e.g inference latency, heatmap, outlier score, KS drift, etc. 

To be able to compute these prediction metrics, the predictions made has to be first reviewed. Navigate to to the **Predictions** tab under the deployment interface. By hovering on the images, click on the button **review**, you will be then forwarded to an annotation-like interface, as shown below: 

![review prediction](/docs/review-prediction.png)

When reviewing the predictions you can adjust the bounding boxes, correct a prediction if it is wrong or save the results if you are satisfied with the prediction. Make sure to click on the button **Save** to save your changes. 

![reviewed prediction](/docs/reviewed-prediction.png)

 The **Accepted** tag on the images help you recognize the images that were reviewed from the once that were not reviewed. 


# 🔁 Continuous training and deployment

## 1. Feedback Loop 

Once you are done with the predictions review, you can leverage the prediction dataset to enable the **`Feedback Loop`**.

You can select a dataset version, all predictions coming from your deployment will be then sent to your dataset version once they are reviewed. 

The setup is done in the **Settings tab** under the deployments interface, as shown below: 

![feedback loop](/docs/feedback-loop.png)

The next step is to submit the reviewed prediction images to the **Feedback Loop**. To do that, navigate to the **Predictions tab** and select all or a subset of the images and click on **Submit to Feedback-Loop** button. 

![submit feedback loop](/docs/submit-feedback-loop.png)








