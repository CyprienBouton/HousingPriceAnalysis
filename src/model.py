from stqdm import stqdm
import pickle
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score

def cross_validate(model, n_splits, random_state=None):
    """Computes the mean of the R2 scores among the different folders.
    :param model: Machine learning model to assess.
    :type model: ml model
    :param n_splits: Number of splits used for the cross validation.
    :type n_splits: int
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
        model.fit(X[idx_train], y[idx_train])
        predictions = model.predict(X[idx_test])
        scores.append(r2_score(y[idx_test], predictions))
    return sum(scores)/len(scores)