# Multiclass Noisy Text Classification with Curriculum Learning

## Description

This project addresses the challenge of multiclass noisy text classification, specifically focusing on predicting relevant hashtags for tweets. It tackles the inherent noise and imbalance present in social media text data by employing curriculum learning, a training strategy inspired by human learning processes.

## Dataset

The project utilizes a dataset of tweets, each labeled with one or more hashtags. The dataset is divided into training, validation, and test sets. Due to the nature of social media data, the dataset exhibits noise in the form of informal language, abbreviations, and misspellings, as well as class imbalance with certain hashtags appearing more frequently than others.

## Methodology

1.  **Data Preprocessing:**
    *   The tweet data is preprocessed to reduce noise and prepare it for feature extraction. This includes converting text to lowercase, removing URLs, and eliminating non-alphanumeric characters.

2.  **Feature Extraction:**
    *   The preprocessed text data is converted into numerical features using the `CountVectorizer`. This creates a vocabulary of unique words and represents each tweet as a vector of word counts.

3.  **Model Training:**
    *   A `VWClassifier` model is trained using curriculum learning. This approach involves gradually increasing the difficulty of the training data presented to the model, starting with easier examples and progressively introducing more challenging ones. This strategy helps the model learn more effectively and generalize better to unseen data.

4.  **Model Evaluation:**
    *   The trained model is evaluated on the validation data using balanced accuracy as the primary metric. This metric accounts for class imbalance and provides a more accurate assessment of the model's performance.
    *   Additional evaluation measures include a confusion matrix and a distribution plot of the predicted hashtag classes.

5.  **Test Data Prediction:**
    *   The trained model is used to predict hashtag labels for the test data.
    *   The predictions are saved to a text file for further analysis or application.

## Results

The model achieved a balanced accuracy of 0.7550 on the validation set. The confusion matrix and predicted hashtag class distribution provide further insights into the model's performance across different classes.

## Usage

To run this project, follow these steps:

1.  **Data Preparation:** Ensure your train, validation, and test datasets are in the specified format (ID, Label, Text) and stored in the correct file paths.
2.  **Run the Code:** Execute the provided code in a Python environment (e.g., Jupyter Notebook, Google Colab) in the given order.
3.  **Check Output:** After running the code, check the generated output files. The test predictions will be saved in the specified file path.
4.  **Adjustments:** If needed, adjust the code (e.g., file paths, preprocessing steps) to suit your requirements.

## Conclusion

This project demonstrates the effectiveness of curriculum learning in improving the performance of multiclass noisy text classification. The model successfully learned to predict relevant hashtags for tweets, despite the challenges of noise and class imbalance. This approach can be applied to various text classification tasks involving noisy and imbalanced data.

## Future Work

*   Explore different curriculum learning strategies and hyperparameter settings to further optimize model performance.
*   Investigate alternative feature extraction techniques, such as TF-IDF or word embeddings, to potentially improve classification accuracy.
*   Apply the model to other noisy text classification tasks, such as sentiment analysis or topic classification.
