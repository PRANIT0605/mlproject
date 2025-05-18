import os
import sys
from dataclasses import dataclass
from catboost import CatBoostClassifier
from sklearn.ensemble import(
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from src.utils import evaluate_models
@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.modle_trainer_config = ModelTrainerConfig()
        
    
    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],#All columns except the last one
                train_array[:, -1],# Last column
                test_array[:, :-1],
                test_array[:, -1],
            )
            models = {
                "RandomForestClassifier": RandomForestClassifier(),
                "DecisionTreeClassifier": DecisionTreeClassifier(),
                "KNeighborsClassifier": KNeighborsClassifier(),
                "GradientBoostingClassifier": GradientBoostingClassifier(),
                "AdaBoost Classifier": AdaBoostClassifier(),
                "XGBClassifier": XGBRegressor(),
                "CatBoosting Classifier": CatBoostClassifier(verbose=False),
                "Linear Regression:": LinearRegression()
            }
            model_report: dict = evaluate_models(x_train = x_train, y_train = y_train,x_test = x_test, y_test = y_test,
                                                models = models)
            # Getting the best model score from dict
            best_model_score = max(sorted(model_report.values()))
            #Getting best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            
            if best_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info(f"Best model found: {best_model_name} with score: {best_model_score}")
            
            save_object(
                file_path = self.modle_trainer_config.trained_model_file_path,
                obj = best_model
            )
            
            predicted = best_model.predict(x_test)
            r2_square = r2_score(y_test, predicted)
            return r2_square
        
        except Exception as e:
            raise CustomException(e, sys) from e
        