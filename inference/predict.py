from data.dataset import FLAGS

def predict(model, scaler, sample):
    pred = model.predict(scaler.transform([sample]))[0]
    return [FLAGS[i] for i, v in enumerate(pred) if v == 1]