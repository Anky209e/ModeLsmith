import torch
import numpy as np

class IrisModel(torch.nn.Module):
        def __init__(self,input_dim, output_dim):
            super().__init__()
            self.linear = torch.nn.Linear(input_dim, output_dim) 
        
        def forward(self, inputs):
            relud = torch.relu(self.linear(inputs))
            targets_pred = torch.softmax(relud,dim=-1) 
            return targets_pred

def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    inputs = [sepal_length, sepal_width, petal_length, petal_width]
    mean = [5.843333333333334, 3.0540000000000003, 3.758666666666666, 1.1986666666666668]
    std = [0.8253012917851409, 0.4321465800705435, 1.7585291834055212, 0.7606126185881716]
    
    for i in range(4):
        inputs[i] = (inputs[i] - mean[i])/ std[i]
    inputs = torch.from_numpy(np.array(inputs).astype(np.float32))

    logistic_model = IrisModel(4,3)
    logistic_model.load_state_dict(torch.load("./models/Iris.pth"))

    pred = logistic_model(inputs)
    
    pred = pred.detach().numpy().reshape(-1)
    ans = np.where(pred == max(pred))
    
    if ans[0][0]==0:
        final_ans = "Iris-setosa"
    elif ans[0][0]==1:
        final_ans = "Iris-versicolor"
    else:
        final_ans = "Iris-virginica"
    
    return final_ans, round(float(pred.max())*100, 2), pred
