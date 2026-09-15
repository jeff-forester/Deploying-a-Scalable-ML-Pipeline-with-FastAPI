# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model is a Random Forest classifier created with scikit-learn. It predicts whether an individual's income is greater than $50K or less than or equal to $50K based on census data. A random state of 42 was used for reproducibility.

## Intended Use

The model is intended as an educational example of building, evaluating, and deploying a machine learning classification model. It can be used to demonstrate data processing, model training, API deployment, and model performance evaluation. It should not be used to make employment, lending, or other high-stakes decisions about individuals.

## Training Data

The model was trained using the Census Income dataset. The data includes demographic and employment-related attributes such as age, workclass, education, marital status, occupation, relationship, race, sex, hours worked per week, and native country. The salary column was used as the target variable.

The dataset was split into training and test sets using an 80/20 split. The split used a random state of 42 and was stratified by the salary column. Categorical features were encoded during preprocessing before model training.

## Evaluation Data

The evaluation data consists of the 20% test portion of the Census Income dataset that was held out during training. The same preprocessing steps and encoder created from the training data were applied to the test data before predictions were generated.

## Metrics

The model was evaluated using precision, recall, and F1 score.

The model achieved a precision of 0.7353, a recall of 0.6378, and an F1 score of 0.6831 on the test data.

Performance was also evaluated across categorical data slices to identify differences in model performance among different groups.

## Ethical Considerations

The dataset contains demographic information such as race and sex. These attributes may reflect historical or societal biases in the original data. As a result, the model could produce different levels of performance for different demographic groups. The model should not be used as the sole basis for decisions that could significantly affect an individual.

## Caveats and Recommendations

The model was trained on a limited historical census dataset and may not represent current populations or economic conditions. Its performance may not generalize to data from different time periods or populations.

Before using the model in another setting, the data distribution and categorical slice performance should be reviewed. Additional data, fairness testing, and model monitoring would be recommended before considering the model for a real-world application.