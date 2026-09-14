import numpy as np
import pytest
from sklearn.ensemble import RandomForestClassifier

from ml.model import compute_model_metrics, inference, train_model


def test_train_model():
    """Test that train_model returns a RandomForestClassifier."""
    X_train = np.array(
        [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1],
        ]
    )
    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


def test_inference():
    """Test that inference returns one prediction for each input row."""
    X_train = np.array(
        [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1],
        ]
    )
    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)
    preds = inference(model, X_train)

    assert isinstance(preds, np.ndarray)
    assert len(preds) == len(X_train)
    assert set(preds).issubset({0, 1})


def test_compute_model_metrics():
    """Test precision, recall, and F1 against known expected values."""
    y = np.array([1, 1, 0, 0])
    preds = np.array([1, 0, 0, 0])

    precision, recall, f1 = compute_model_metrics(y, preds)

    assert precision == pytest.approx(1.0)
    assert recall == pytest.approx(0.5)
    assert f1 == pytest.approx(2 / 3)
