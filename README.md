![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg)

# MMulticlass vs Multi-label Classification
Multiclass classification is a machine learning task where the goal is to assign instances to one of multiple predefined classes or categories, where each instance belongs to exactly one class. Whereas multilabel classification is a machine learning task where each instance can be associated with multiple labels simultaneously, allowing for the assignment of multiple binary labels to the instance.
## Multiclass Classification
While binary classification involves distinguishing between only two classes, multiclass classification expands this scope to involve distinguishing between multiple classes. In essence, the goal is to train a model that can effectively sort instances into various predefined categories, providing a nuanced solution for scenarios where items can belong to more than two exclusive groups. This approach is commonly employed in tasks such as handwriting recognition, email categorization, and image classification involving more than two distinct categories.
### Model Training Techniques
Training a multiclass classification model involves a use of **softmax** activation function in the output layer of the neural network. Softmax converts the raw model outputs into probabilities, assigning higher probabilities to the correct classes. Additionally, **categorical cross-entropy loss** is often used as the objective function during training. This loss function measures the dissimilarity between the predicted probabilities and the actual class labels, guiding the model to minimize errors and improve accuracy.
### Evaluation Metrics
To assess the performance of a multiclass classification model, evaluation metrics like `accuracy`, `precision`, `recall` (sensitivity) and `F1 score`.

## Multi-label Classification
Multi-label classification is a machine learning paradigm where instances can be associated with multiple labels simultaneously. Unlike traditional classification tasks, where an instance is assigned a single exclusive label, multi-label classification recognizes the possibility for instances to exhibit characteristics that span across various categories. The goal is to develop models capable of accurately predicting and assigning a set of relevant labels to each instance, reflecting the complex relationships and diversity inherent in real-world datasets. This approach acknowledges the overlapping nature of labels, providing a more realistic representation of the multifaceted attributes present in the data.
### Scenarios
Multi-label classification is highly applicable in diverse scenarios where instances can possess multiple attributes or labels. Examples include:
`Document Tagging`: Assigning multiple tags or topics to a document, such as labeling an article as both "technology" and "business."
`Image Classification with Multiple Labels`: Identifying and labeling multiple objects or features within an image, like recognizing both "cat" and "outdoor" in a photograph.
Model Training Techniques:
### Training models for multi-label classification
`Sigmoid Activation`: In the output layer of the neural network, sigmoid activation is often used. Unlike `softmax` in multiclass scenarios, sigmoid independently activates each output node, producing a value between 0 and 1, representing the likelihood of the corresponding label being present.
`Binary Cross-Entropy Loss`: This loss function is employed during training to measure the dissimilarity between the predicted probabilities and the actual presence or absence of each label. It guides the model to minimize errors in its multi-label predictions.
### Evaluation Metrics
Assessing the performance of a multi-label classification model requires specific metrics tailored to handle the complexity of multiple labels per instance:
`Hamming Loss`: This metric calculates the fraction of labels that are incorrectly predicted. It provides a comprehensive measure of overall model performance in terms of label accuracy.
`Precision at k`: Precision at k evaluates the precision of the top-k predicted labels, recognizing that not all labels need to be considered. It accounts for scenarios where only the most relevant labels are of interest.
`Recall at k`: Similar to precision at k, recall at k assesses the recall of the top-k predicted labels. It focuses on capturing the relevant labels among the top predictions.






## Dataset and it's Features

Can you predict if customer is going to cancel the reservation ?
A significant number of hotel reservations are called-off due to cancellations or no-shows. The typical reasons for cancellations include change of plans, scheduling conflicts, etc. This is often made easier by the option to do so free of charge or preferably at a low cost which is beneficial to hotel guests, but it is a less desirable and possibly revenue-diminishing factor for hotels to deal with. A Kaggle Hotel Reservations Dataset is used for the project. It has 36275 entries, 19 columns. One of them (booking_status) is the target column, 12 features columns with data type of integer or float and 3 features columns with data type of object. One column - Booking_ID - was dropped.

[uv docs link](https://docs.astral.sh/uv/guides/projects/)
[Multiclass Classification vs Multi-label Classification](https://www.geeksforgeeks.org/machine-learning/multiclass-classification-vs-multi-label-classification/)
