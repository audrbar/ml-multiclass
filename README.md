![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg)

# Multiclass vs Multi-label Classification
Multiclass classification is a machine learning task where the goal is to assign instances to one of multiple predefined classes or categories, where each instance belongs to exactly one class. Whereas multilabel classification is a machine learning task where each instance can be associated with multiple labels simultaneously, allowing for the assignment of multiple binary labels to the instance.
### Multiclass Classification
While binary classification involves distinguishing between only two classes, multiclass classification expands this scope to involve distinguishing between multiple classes. In essence, the goal is to train a model that can effectively sort instances into various predefined categories, providing a nuanced solution for scenarios where items can belong to more than two exclusive groups. This approach is commonly employed in tasks such as handwriting recognition, email categorization, and image classification involving more than two distinct categories.
#### Model Training Techniques
Training a multiclass classification model involves a use of **softmax** activation function in the output layer of the neural network. Softmax converts the raw model outputs into probabilities, assigning higher probabilities to the correct classes. Additionally, **categorical cross-entropy loss** is often used as the objective function during training. This loss function measures the dissimilarity between the predicted probabilities and the actual class labels, guiding the model to minimize errors and improve accuracy.
#### Evaluation Metrics
To assess the performance of a multiclass classification model, evaluation metrics like `accuracy`, `precision`, `recall` (sensitivity) and `F1 score`.

### Multi-label Classification
Multi-label classification is a machine learning paradigm where instances can be associated with multiple labels simultaneously. Unlike traditional classification tasks, where an instance is assigned a single exclusive label, multi-label classification recognizes the possibility for instances to exhibit characteristics that span across various categories. The goal is to develop models capable of accurately predicting and assigning a set of relevant labels to each instance, reflecting the complex relationships and diversity inherent in real-world datasets. This approach acknowledges the overlapping nature of labels, providing a more realistic representation of the multifaceted attributes present in the data.
#### Scenarios
Multi-label classification is highly applicable in diverse scenarios where instances can possess multiple attributes or labels. Examples include:
`Document Tagging`: Assigning multiple tags or topics to a document, such as labeling an article as both "technology" and "business."
`Image Classification with Multiple Labels`: Identifying and labeling multiple objects or features within an image, like recognizing both "cat" and "outdoor" in a photograph.
Model Training Techniques:
#### Training models for multi-label classification
In the output layer of the neural network `Sigmoid Activation` function is often used. Unlike `softmax` in multiclass scenarios, sigmoid independently activates each output node, producing a value between 0 and 1, representing the likelihood of the corresponding label being present. `Binary Cross-Entropy Loss` function is employed during training to measure the dissimilarity between the predicted probabilities and the actual presence or absence of each label. It guides the model to minimize errors in its multi-label predictions.
#### Evaluation Metrics
Assessing the performance of a multi-label classification model requires specific metrics tailored to handle the complexity of multiple labels per instance: \
`Hamming Loss`: This metric calculates the fraction of labels that are incorrectly predicted. It provides a comprehensive measure of overall model performance in terms of label accuracy. \
`Precision at k`: Precision at k evaluates the precision of the top-k predicted labels, recognizing that not all labels need to be considered. It accounts for scenarios where only the most relevant labels are of interest. \
`Recall at k`: Similar to precision at k, recall at k assesses the recall of the top-k predicted labels. It focuses on capturing the relevant labels among the top predictions.
### Choosing Between Multi-Class and Multi-Label Classification
When embarking on a classification task, one of the foundational decisions is whether to opt for multi-class or multi-label classification, and this choice significantly influences the model's performance and relevance to real-world scenarios.
- Assess whether the instances in your dataset belong to mutually exclusive classes (Multi-Class) or if they can have multiple labels simultaneously (Multi-Label). Understanding the nature of labels is fundamental in choosing the appropriate classification approach.
- Examine the relationships between labels. If the labels are independent or weakly correlated, multi-class classification may be suitable. For strong correlations or overlapping characteristics, multi-label classification is more appropriate.
- Gauge the complexity of your classification problem. Multi-class classification is generally simpler as it deals with exclusive categorization. If the problem is inherently complex and instances can have diverse characteristics, opt for multi-label classification.
- Consider domain-specific requirements and constraints. Some domains naturally lend themselves to one approach over the other based on the inherent characteristics of the data and the specific objectives of the task.
In conclusion, the choice between multi-class and multi-label classification should be made considering the intricacies of the problem, the nature of the data, and the specific requirements of the application. Each approach has its merits, and selecting the most suitable classification method is pivotal for achieving optimal model performance in diverse real-world scenarios.

## Dataset and it's Features

Can you predict if customer is going to cancel the reservation ?
A significant number of hotel reservations are called-off due to cancellations or no-shows. The typical reasons for cancellations include change of plans, scheduling conflicts, etc. This is often made easier by the option to do so free of charge or preferably at a low cost which is beneficial to hotel guests, but it is a less desirable and possibly revenue-diminishing factor for hotels to deal with. A Kaggle Hotel Reservations Dataset is used for the project. It has 36275 entries, 19 columns. One of them (booking_status) is the target column, 12 features columns with data type of integer or float and 3 features columns with data type of object. One column - Booking_ID - was dropped.

## Resources
[uv docs link](https://docs.astral.sh/uv/guides/projects/) \
[Multiclass Classification vs Multi-label Classification](https://www.geeksforgeeks.org/machine-learning/multiclass-classification-vs-multi-label-classification/)
[A Comprehensive Guide to Multiclass Classification in Machine Learning](https://medium.com/@murpanironit/a-comprehensive-guide-to-multiclass-classification-in-machine-learning-c4f893e8161d) \
[Classification in Machine Learning: An Introduction](https://www.datacamp.com/blog/classification-machine-learning)
