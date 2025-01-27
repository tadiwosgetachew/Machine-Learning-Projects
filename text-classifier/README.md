# SMS Text Classifier - Neural Network

This project is a machine learning model that classifies SMS messages as either "ham" (normal, non-spam message) or "spam". The goal of this project is to use a neural network to build a classifier that can accurately predict whether a message is "ham" or "spam".

## Project Description

In this challenge, we created a function called `predict_message` that takes an SMS message as input and returns a list containing:
1. A probability score (between 0 and 1) indicating the likelihood that the message is "ham" (0) or "spam" (1).
2. A label, either "ham" or "spam", indicating the classification.

### Dataset

We used the **SMS Spam Collection Dataset** provided by freeCodeCamp. The dataset consists of messages labeled as either "ham" or "spam".

- **Ham**: Normal, non-spam messages sent by friends or individuals.
- **Spam**: Messages that are advertisements or automated messages from companies.

The dataset can be downloaded from the following links:

- **Train Data**: [Download train-data.tsv](https://cdn.freecodecamp.org/project-data/sms/train-data.tsv)
- **Test Data**: [Download valid-data.tsv](https://cdn.freecodecamp.org/project-data/sms/valid-data.tsv)

### Libraries Used
- **numpy**: For numerical operations
- **pandas**: For data manipulation and preprocessing.
- **scikit-learn**: For feature extraction, model building, and evaluation.
- **tensorflow**: For building and training the neural network model.
- **string**: For string manipulation tasks such as removing punctuation.
- **re**: For regular expressions and text preprocessing tasks.


## Model Evaluation

The model was evaluated using the test dataset (valid-data.tsv), and its performance was measured using accuracy, which was found to be 98.5%, showcasing its effectiveness in classifying SMS messages as either "ham" or "spam". 

## Getting Started

1. Clone this repository to your local machine.
2. Install the necessary libraries by running:
```bash
   pip install -r requirements.txt
```

## Acknowledgments

This project uses the **SMS Spam Collection dataset** from **freeCodeCamp**, as well as libraries such as **Keras**, **Scikit-learn**, and **TensorFlow**.

## Contributing

Contributions are welcome! Feel free to fork the repository or open an issue for improvements or suggestions. Potential improvements could include fine-tuning the model, using different feature extraction techniques, or integrating additional evaluation metrics. 

## Conclusion

This project demonstrates how to apply machine learning, specifically a neural network, to classify SMS messages as spam or not-spam. It provides a function that enables real-time prediction of message classification.


