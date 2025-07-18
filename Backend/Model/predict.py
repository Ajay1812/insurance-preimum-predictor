import pickle
import pandas as pd

# import ml model
with open("Model/model.pkl", "rb") as f:
    model = pickle.load(f)

# MLflow 
MODEL_VERSION = "1.0.0"

class_labels = model.classes_.tolist()

def predict_output(user_input: dict) -> dict:
    df = pd.DataFrame([user_input])
    predicted_class = model.predict(df)[0] 
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)
    
    class_probs = dict(zip(class_labels, map(lambda p: round(p,4), probabilities)))
    
    return {
        "predicted_category": predicted_class,
        "confidence_score": round(confidence, 4),
        "class_probabilities": class_probs
    }