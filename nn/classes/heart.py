import torch
import numpy as np


class LogisticRegression(torch.nn.Module):
    def __init__(self):
        super(LogisticRegression, self).__init__()
        self.linear = torch.nn.Linear(13,1)

    def forward(self, targets_train ):
        out = self.linear(targets_train)
        targets_preds = torch.sigmoid(out)
        return targets_preds


def predict_heart_attack(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    inputs = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]

    #------------------------standards------------------
    mean = [54.366336633663366, 0.6831683168316832, 0.966996699669967, 131.62376237623764, 246.26402640264027, 
            0.1485148514851485, 0.528052805280528, 149.64686468646866, 0.32673267326732675, 1.0396039603960396,
            1.3993399339933994, 0.7293729372937293, 2.3135313531353137]
    std =  [9.067101638577872, 0.46524119304834577, 1.0303480250839463, 17.509178065734393, 51.74515101045713,
            0.3556096038825341, 0.5249911240963214, 22.86733258188924, 0.46901858543869346, 1.1591574732421364,
            0.6152084301256651, 1.0209175011165652, 0.6112653149988239]
    #-----------------------------------------------------

    for i in range(len(mean)):
        inputs[i] = (inputs[i] - mean[i])/ std[i]

    inputs = torch.from_numpy(np.array(inputs).astype(np.float32))

    pre_model = LogisticRegression()

    # loading weights

    pre_model.load_state_dict(torch.load("./models/heart_attack_data.pth"))
    
    preds = pre_model(inputs).item()*100

    return [("Bad Heart",round(preds,2))]
