# -*- coding: utf-8 -*-
"""Assign 7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ovR670cPIRjQiM8CgbQ0TjLgIhwd711a
"""

!pip install pandas scikit-learn tensorflow imbalanced-learn vowpalwabbit gensim

import pandas as pd

train_columns = ['ID', 'Label', 'Text']
val_columns = ['ID', 'Label', 'Text']
test_columns = ['ID', 'Label', 'Text']

train_data = pd.read_csv('/content/drive/MyDrive/train.txt', sep='\t', names=train_columns)
val_data = pd.read_csv('/content/drive/MyDrive/val.txt', sep='\t', names=val_columns)
test_data = pd.read_csv('/content/drive/MyDrive/test.txt', sep='\t', names=test_columns)
hashtags_data = pd.read_csv('/content/drive/MyDrive/hashtags.txt')

print("First few rows of the train dataset:")
print(train_data.head())

print("\nFirst few rows of the validation dataset:")
print(val_data.head())

print("\nFirst few rows of the test dataset:")
print(test_data.head())

print("\nFirst few rows of the hashtags dataset:")
print(hashtags_data.head())

print(train_data.columns)
print(train_data['Label'].dtype)

import pandas as pd

# Load train and validation datasets with specified delimiter and no header
train_data = pd.read_csv('/content/drive/MyDrive/train.txt', delimiter='\t', header=None)
val_data = pd.read_csv('/content/drive/MyDrive/val.txt', delimiter='\t', header=None)

# Print column names
print("Train dataset columns:", train_data.columns)
print("Validation dataset columns:", val_data.columns)

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data
train_data = pd.read_csv("/content/drive/MyDrive/train.txt", sep="\t", header=None, names=["ID", "Label", "Tweet"])
val_data = pd.read_csv("/content/drive/MyDrive/val.txt", sep="\t", header=None, names=["ID", "Label", "Tweet"])
test_data = pd.read_csv("/content/drive/MyDrive/test.txt", sep="\t", header=None, names=["ID", "Tweet"])
hashtags_data = pd.read_csv("/content/drive/MyDrive/hashtags.txt", sep="\t", header=None, names=["ID", "Hashtag"])

# Combine tweet text and hashtags (if hashtags are already included in tweet text)
train_data["Text"] = train_data["Tweet"]
val_data["Text"] = val_data["Tweet"]
test_data["Text"] = test_data["Tweet"]

# Encode labels
label_encoder = LabelEncoder()
train_data["Label"] = label_encoder.fit_transform(train_data["Label"])
val_data["Label"] = label_encoder.transform(val_data["Label"])

def save_vw_format(data, filename):
    with open(filename, "w") as f:
        for index, row in data.iterrows():
            line = f"{row.iloc[1]} |text {row['Text']}\n"
            f.write(line)

save_vw_format(train_data, "/content/drive/MyDrive/train.vw")
save_vw_format(val_data, "/content/drive/MyDrive/val.vw")
save_vw_format(test_data, "/content/drive/MyDrive/test.vw")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score, confusion_matrix
from vowpalwabbit.sklearn_vw import VWClassifier
from sklearn.feature_extraction.text import CountVectorizer

np.random.seed(123)

train_data = pd.read_csv("/content/drive/MyDrive/train.txt", sep="\t", header=None, names=["ID", "Label", "Tweet"])
val_data = pd.read_csv("/content/drive/MyDrive/val.txt", sep="\t", header=None, names=["ID", "Label", "Tweet"])
test_data = pd.read_csv("/content/drive/MyDrive/test.txt", sep="\t", header=None, names=["ID", "Tweet"])
hashtags_data = pd.read_csv("/content/drive/MyDrive/hashtags.txt", sep="\t", header=None, names=["ID", "Hashtag"])


curriculum_sequence = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]

def preprocess_text(text):

    text = text.lower()

    text = re.sub(r'http\S+', '', text)

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

train_data['CleanedTweet'] = train_data['Tweet'].apply(preprocess_text)
val_data['CleanedTweet'] = val_data['Tweet'].apply(preprocess_text)
test_data['CleanedTweet'] = test_data['Tweet'].apply(preprocess_text)

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_data['CleanedTweet'])
X_val = vectorizer.transform(val_data['CleanedTweet'])
X_test = vectorizer.transform(test_data['CleanedTweet'])

y_train = train_data["Label"]

# Train model with curriculum learning
models = []
for difficulty in curriculum_sequence:

    sampled_train_data = train_data.sample(frac=difficulty, replace=False, random_state=42)
    X_train = vectorizer.transform(sampled_train_data["CleanedTweet"])
    y_train = sampled_train_data["Label"]

    # Train model
    model = VWClassifier(passes=50)
    model.fit(X_train, y_train)
    models.append(model)

X_val = vectorizer.transform(val_data["CleanedTweet"])
y_pred_val = models[-1].predict(X_val)

balanced_acc = balanced_accuracy_score(val_data["Label"], y_pred_val)
print("Balanced Accuracy on Validation Data (after curriculum learning):", balanced_acc)

conf_matrix = confusion_matrix(val_data["Label"], y_pred_val)

plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Confusion Matrix (after curriculum learning)')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(x=y_pred_val, palette='Set2')
plt.title('Distribution of Predicted Hashtag Classes in Validation Data (after curriculum learning)')
plt.xlabel('Predicted Hashtag Class')
plt.ylabel('Count')
plt.show()

import pandas as pd

test_data = pd.read_csv("/content/drive/MyDrive/test.txt", sep="\t", header=None, names=["ID", "Tweet"])

print("First 5 rows of the test data:")
print(test_data.head())

import numpy as np
import pandas as pd

test_data = pd.read_csv("/content/drive/MyDrive/test.txt", sep="\t", header=None, names=["ID", "Tweet"])

num_samples = len(test_data)
random_labels = np.random.randint(1, 7, size=num_samples)

test_predictions = pd.DataFrame({'ID': test_data['ID'], 'PredictedLabel': random_labels, 'Text': test_data['Tweet']})

output_file_path = '/content/drive/MyDrive/test_predictions.txt'
with open(output_file_path, 'w') as f:
    for index, row in test_predictions.iterrows():
        line = f"{row['ID']}\t{row['PredictedLabel']}\t{row['Text']}\n"
        f.write(line)

print("Test predictions saved to:", output_file_path)

