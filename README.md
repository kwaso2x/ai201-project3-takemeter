TAKEMETER — LeBron vs Jordan Comment Classifier
AI201 • CodePath • Project 3
Created by Kwasi Osei

Overview
Takemeter is a text‑classification project that analyzes online comments from the LeBron vs. Jordan GOAT debate and predicts whether a comment is:

pro_lebron

pro_jordan

neutral

The model is a fine‑tuned DistilBERT transformer trained on a custom dataset of basketball debate comments collected from Reddit, YouTube, and other public sources.

This project demonstrates:

Dataset creation

Text preprocessing

Fine‑tuning a transformer model

Evaluation and confusion matrix

Building a simple Python app (app.py) to run predictions

Repository Structure
Code
app.py
requirements.txt
confusion_matrix.png
evaluation_results.json
dataset.csv
Kwasi_Osei_ai201_project3_takemeter_starter_clean.ipynb
README.md
(Model hosted externally on Google Drive)
Model Download (Required to Run app.py)
Because the fine‑tuned DistilBERT model is too large for GitHub, it is hosted on Google Drive.

Download the model here:
https://drive.google.com/file/d/1tARbfRlHqATVJvElnDT7cD4l6Kg9aeQq/view?usp=sharing

After downloading:

Extract the ZIP

You will get a folder named takemeter-model

Place that folder in the root of your project, next to app.py

Your folder should look like:

Code
takemeter-model/
app.py
requirements.txt
...
How the Model Works
The model uses:

DistilBERT base uncased

Fine‑tuned for 3‑class sequence classification

Labels: pro_lebron, pro_jordan, neutral

Tokenized using HuggingFace AutoTokenizer

Optimized with AdamW

Trained on a labeled dataset of basketball debate comments

Evaluation Results
Evaluation metrics are stored in:

evaluation_results.json

confusion_matrix.png

These include:

Accuracy

Precision

Recall

F1‑scores

Class performance breakdown

How to Run the App
1. Install dependencies
Code
pip install -r requirements.txt
2. Make sure the model folder is in place
Code
takemeter-model/
app.py
3. Run the app
Code
python app.py
4. Enter a comment
Example:

Code
LeBron is the greatest all-around player ever
Output:

Code
Prediction: pro_lebron
requirements.txt
Code
transformers
torch
scikit-learn
pandas
numpy
matplotlib
Dataset
The dataset (dataset.csv) contains:

Raw comment text

Cleaned text

Label (pro_lebron, pro_jordan, neutral)

Collected from:

Reddit threads

YouTube debates

Basketball forums

Demo Video
(Add your YouTube link after recording)

Code

Credits
CodePath AI201 Team

HuggingFace Transformers

PyTorch

Reddit & YouTube communities for public comment data
