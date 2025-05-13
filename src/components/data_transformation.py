import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import os
from src.utils import save_object
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function creates preprocessing pipelines for numerical and categorical features.
        '''
        try:
            numerical_columns = ['writing_score', 'reading_score']
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            # Numerical pipeline
            numerical_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
            ])

            # Categorical pipeline
            categorical_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehotencoder", OneHotEncoder()),
            ])

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            # Combine pipelines
            preprocessor = ColumnTransformer(transformers=[
                ("numerical_pipeline", numerical_pipeline, numerical_columns),
                ("categorical_pipeline", categorical_pipeline, categorical_columns),
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            # Read train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data successfully")
            logging.info("Obtaining preprocessing object")

            preprocessor_obj = self.get_data_transformer_object()
            target_column_name = "math_score"
            numerical_columns = ['writing_score', 'reading_score']

            input_features_train = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train = train_df[target_column_name]

            input_features_test = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test = test_df[target_column_name]

            logging.info("Applying preprocessing object on training and testing data")

            input_features_train_array = preprocessor_obj.fit_transform(input_features_train)
            input_features_test_array = preprocessor_obj.transform(input_features_test)

            # Combine features and targets
            train_arr = np.c_[input_features_train_array, np.array(target_feature_train)]
            test_arr = np.c_[input_features_test_array, np.array(target_feature_test)]

            logging.info("Saving preprocessor object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)
