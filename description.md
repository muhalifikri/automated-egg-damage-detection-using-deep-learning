# Project Title
Automated Egg Damage Detection Using Deep Learning

## Repository Outline
1. P2G7_muhalifikri_porto(eng).ipynb - A notebook containing a simple analysis (EDA) and the process of building an ML model.
2. P2G7_muhalifikri_inference.ipynb - A notebook containing model experiments using data outside the dataset.
3. url.txt - A text file containing URLs for the dataset, model deployment, and the ML model
4. Folder Deployment - A folder containing the files used for model deployment

## Problem Background
Egg collection in poultry farms requires timely monitoring to maintain product quality and farm cleanliness. However, Mr. Gofar experienced difficulties in consistently monitoring and collecting eggs at the right time. As a result, some eggs were left in the coop for too long, increasing the risk of damage such as cracks or breakage, which also negatively affected the cleanliness and overall condition of the farm environment.

To address this issue, an automated solution was proposed to assist the egg collection process. This project focuses on developing a Machine Learning-based Computer Vision model capable of classifying eggs into two categories: damaged eggs and non-damaged eggs. The system is expected to support faster and more accurate identification of egg conditions before the collection process.

## Project Output
The objective of this project is to develop a Computer Vision Machine Learning model that can automatically classify egg conditions into two categories: damaged and non-damaged eggs. The model is designed to assist in improving efficiency, maintaining egg quality, and supporting a more effective egg monitoring and collection process.

## Data
The dataset used in this project was obtained from Kaggle and consists of images of damaged and non-damaged chicken eggs. The dataset contains approximately 794 images distributed across both categories.

## Method
The method used in this project is a Deep Learning-based Computer Vision approach using the Convolutional Neural Network (CNN) algorithm. CNN was chosen because it is effective for image classification tasks and capable of extracting important visual features such as shapes, textures, and crack patterns from egg images.

The model was developed to classify chicken eggs into two categories: damaged and non-damaged eggs. Several techniques such as Data Augmentation, Dropout, and Early Stopping were applied to improve model performance and reduce overfitting.

The dataset was divided into:

Training Set : 714 data
Test Set : 80 data

Model performance was evaluated using:

Accuracy
Loss
Classification Report

The final model was deployed using Hugging Face Spaces for real-time prediction and demonstration purposes.

## Stacks
Programming Language : Python, Pandas, Numpy, Scikit-Learn, Tensorflow
Tools : VSCode, HuggingFace, Google Drive, Notepad


## Reference

MODEL ML
Name : model_comvis_gc7.keras
Link : https://drive.google.com/drive/folders/156lKJbwJlYYYfq9JhU1vq_Ajc5xDg8JE?usp=sharing

MODEL DEPLOY
Link : https://huggingface.co/spaces/muhalifikri/model_egg_gc7

DATASET
Link : https://www.kaggle.com/datasets/abdullahkhanuet22/eggs-images-classification-damaged-or-not


**Additional reference:**

