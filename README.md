# Automated Egg Damage Detection Using Deep Learning 🥚🔍

A Computer Vision and Deep Learning solution designed to automatically inspect and classify chicken egg conditions into damaged and non-damaged categories, optimizing poultry farm logistics and quality control.

---

## 📌 Problem Background

Timely and consistent egg collection in poultry farms is essential for maintaining product quality and facility hygiene. On Mr. Gofar's farm, manual monitoring and inconsistent collection times led to eggs being left in the coops for too long. This significantly increased the rate of damage—such as cracks and breakages—and negatively impacted the overall cleanliness of the farm environment.

To resolve these operational challenges, this project introduces an automated computer vision solution. By developing a Deep Learning-based model, the system accelerates the screening process, ensuring faster, highly accurate identification of egg conditions before collection, minimizing waste, and safeguarding farm hygiene.

## 📈 Project Output

The core deliverable of this project is a production-ready **Computer Vision Machine Learning Model** capable of robustly classifying chicken eggs into two distinct categories: **Damaged** and **Non-Damaged**. 

* **Live Web App Demonstration:** [Access on Hugging Face Spaces](https://huggingface.co/spaces/muhalifikri/model_egg_gc7)

## 📂 Repository Outline

* `P2G7_muhalifikri_porto(eng).ipynb`: Core development notebook encompassing Exploratory Data Analysis (EDA), data preprocessing, model architecture design, training, and evaluation.
* `P2G7_muhalifikri_inference.ipynb`: Dedicated inference script simulating real-world production by testing the trained model against external, unseen data.
* `url.txt`: Centralized reference text file containing direct links to the dataset, serialised weights, and deployment environments.
* `Folder Deployment/`: Manifest directory holding the configuration files, application logic, and dependencies required to serve the model on the web wrapper.

## 📊 Dataset Overview

* **Source:** [Kaggle - Eggs Images Classification Dataset](https://www.kaggle.com/datasets/abdullahkhanuet22/eggs-images-classification-damaged-or-not)
* **Dataset Size:** ~794 high-resolution images across both target classes.
* **Data Split:** * **Training Set:** 714 images (used for feature extraction and pattern recognition)
    * **Test Set:** 80 images (held-out data reserved for rigorous evaluation)

## 🧠 Methodology

This project utilizes a **Convolutional Neural Network (CNN)** architecture, natively built for image processing to extract complex visual cues such as geometry, textures, structural cracks, and fracture patterns. 

Key modeling techniques implemented to boost generalization and mitigate overfitting include:
* **Data Augmentation:** Artificially expanding dataset diversity (e.g., rotations, scaling, flips) to make the model invariant to camera angles and lighting variations.
* **Regularization:** Utilizing `Dropout` layers to prevent co-adaptation of features.
* **Early Stopping:** Monitoring validation loss during training to automatically cease training at peak validation performance.

### Evaluation Metrics
Model validation is extensively assessed using:
* **Categorical Accuracy & Loss Curves**
* **Classification Report:** Precision, Recall, and F1-Score to evaluate the risk of False Negatives (missing a damaged egg).

## 🛠️ Tech Stack

* **Language & Core Libraries:** Python, NumPy, Pandas
* **Machine Learning & Deep Learning:** TensorFlow, Keras, Scikit-Learn
* **Development Tools & Cloud Infrastructure:** VS Code, Google Drive, Hugging Face Spaces (Gradio/Streamlit)

---

## 🔗 References & Project Artifacts

* **Production Model Weights (`.keras`):** [Google Drive Folder](https://drive.google.com/drive/folders/156lKJbwJlYYYfq9JhU1vq_Ajc5xDg8JE?usp=sharing)
* **Interactive Web Application:** [Hugging Face Spaces Deployment](https://huggingface.co/spaces/muhalifikri/model_egg_gc7)
* **Original Dataset Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/abdullahkhanuet22/eggs-images-classification-damaged-or-not)
