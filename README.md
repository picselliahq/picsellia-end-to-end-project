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

Activate the virtual environment you created by executing this command (as an example my venv is called myvenv): 

```shell
source myvenv/bin/activate 
```

## Setup the environment variables 

Create a .env file in the root directory of this project and add to it your API Token. 
You can retrieve it in your profile page in Picsellia. 

```
API_TOKEN="YOUR_API_TOKEN"
ORGANIZATION_ID="YOUR_ORGANIZATION_ID"
```

