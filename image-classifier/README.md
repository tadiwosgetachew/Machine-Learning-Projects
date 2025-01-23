# Cats vs Dogs Image Classifier (CNN)

This project is an image classification model that classifies images into two categories: cats and dogs. The model is built using Convolutional Neural Networks (CNN) and achieves over 70% accuracy. 

## Project Structure

- `cats_dogs_image_classifier.ipynb`: Jupyter notebook containing the entire model training process.
- `cat_dog_image_classifier_model.keras`: The trained model.
- `requirements.txt`: List of required libraries/frameworks to run the notebook.

## Dataset

The model uses a dataset provided by FreeCodeCamp. The dataset consists of:

- 2000 images for training (1000 images of cats and 1000 images of dogs)
- 1000 images for validation (500 images of cats and 500 images of dogs)
- 50 images for testing (25 images of cats and 25 images of dogs)

You can download the dataset by running the following command in your notebook:

```bash
!wget https://cdn.freecodecamp.org/project-data/cats-and-dogs/cats_and_dogs.zip
```

## Installation 

To run this project, clone the repository and install the required dependencies:

- git clone https://github.com/tadiwosgetachew/machine_learning_projects/image-classifier.git
- pip install -r requirements.txt

## Usage 

- download the dataset: !wget https://cdn.freecodecamp.org/project-data/cats-and-dogs/cats_and_dogs.zip
- !unzip cats_and_dogs.zip
- Upload the dataset to Colab (or modify the paths in the notebook if running locally).
- Open the notebook cats_dogs_image_classifier.ipynb and run the cells to train and test the model.
- The model will be trained for a few epochs, and you will see the accuracy after training.

## Model Performance

The model achieves an accuracy of 70%+ on the validation set. Performance may vary based on training parameters, dataset size, and model architecture changes.

## Future Improvements

Here are some ideas to improve the model's performance:

- **Advanced Data Augmentation**: Implement more sophisticated augmentation techniques to create a more diverse training set and improve the model's ability to generalize.

- **Transfer Learning**: Use pre-trained models such as VGG16 or ResNet for transfer learning, which may improve performance with a smaller dataset.

- **Model Tuning**: Experiment with hyperparameter tuning, such as adjusting the learning rate, batch size, or adding more layers to the model.

- **Fine-tuning CNN Layers**: Explore fine-tuning individual layers of the CNN after pre-training the model with a larger dataset to improve accuracy.

- **Ensemble Methods**: Combine multiple models (e.g., CNN with SVM or Random Forest) for a more robust classifier.

## Requirements

This project requires the following Python packages:

- **tensorflow**: version 2.x
- **numpy**
- **matplotlib**

## Contributing

Feel free to fork the repository, make improvements, or open issues to discuss potential enhancements!

