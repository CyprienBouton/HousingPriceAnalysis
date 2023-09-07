from stqdm import stqdm
import pickle

from sklearn.model_selection import KFold
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler


def train_model(class_model, dataset, labels, model_params={}):
    """ Train a model to predict that predicts the transaction cost.

    :param class_model: Class used to generate a model.
    :type class_model: Class to generate a ml_model
    :param dataset: train dataset.
    :type dataset: np.array
    :param labels: Transaction cost of the flats.
    :type labels: pd.Series
    :param model_params: Parameters used to generate the model.
    :type model_params: dict
    :return models_dict: Dictionary containing the trained models.
    :rtype models_dict: dict
    """
    # Scale data
    scaler = StandardScaler()
    dataset = scaler.fit_transform(dataset)
    # Initiate model
    model = class_model(**model_params)
    # Training
    model.fit(dataset, labels)
    
    models_dict = {
        "scaler": scaler,
        "model": model,
    }
    return models_dict


def predict_model(dataset, models_dict):
    """ Predict train occupancy rate.

    :param dataset: train dataset.
    :type dataset: pd.DataFrame
    :param models_dict: Trained models.
    :type models_dict: dict or ml model
    :return transaction_costs: Predicted transaction costs.
    :rtype transaction_costs: np.array
    """
    # Scale data
    dataset = models_dict['scaler'].transform(dataset)
    # Predict
    transaction_costs = models_dict['model'].predict(dataset)
    return transaction_costs


def cross_validate(class_model, n_splits, model_params={}, random_state=None):
    """Computes the mean of the R2 scores among the different folders.
    
    :param model: Machine learning model to assess.
    :type model: ml model
    :param n_splits: Number of splits used for the cross validation.
    :type n_splits: int
    :param model_params: Parameters used to generate the model.
    :type model_params: dict
    :param random_state: Controls the randomness of the splits.
    :type random_state: int or None
    :return cross_validation_score: mean r2 score among the splits.
    :rtype cross_validation_score: float
    """
    # Load the datasets
    X = pickle.load(open("dset/X.pkl", "rb"))
    y = pickle.load(open("dset/y.pkl", "rb"))
    # K-Folds cross-validator provides indices to split data in train/test sets
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    scores = []
    # Compute the R2 score for each split
    for idx_train, idx_test in stqdm(kf.split(X), total=n_splits):
        models_dict = train_model(
            class_model, 
            X[idx_train], 
            y[idx_train], 
            model_params)
        predictions = predict_model(X[idx_test], models_dict)
        scores.append(r2_score(y[idx_test], predictions))
    return sum(scores)/len(scores)