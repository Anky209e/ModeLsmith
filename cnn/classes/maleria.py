import torch
import numpy as np
from PIL import Image
import os
from torchvision.transforms import ToTensor


class MaleriaModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.network = torch.nn.Sequential(
            # 3 64 64
            torch.nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            # 32 32 32
            torch.nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            # 64 16 16
            torch.nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            # 128 8 8
            torch.nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            # 128 4 4
            torch.nn.Flatten(),
            # 128*4*4
            torch.nn.Linear(128 * 4 * 4, 128),
            torch.nn.ReLU(),
            # 128
            torch.nn.Linear(128, 16),
            torch.nn.ReLU(),
            torch.nn.Linear(16, 2),
            # 2
        )

    def forward(self, inputs):

        out = self.network(inputs)
        return torch.softmax(out, dim=-1)

def predict_maleria(path_to_image):

    img = Image.open(path_to_image)

    if img.size != (64,64):
        img = img.resize((64,64))
    
    transform = ToTensor()
    img_tensor = transform(img)
    img_tensor = torch.reshape(img_tensor, (1,3,64,64))

    model_pred = MaleriaModel()
    model_pred.load_state_dict(torch.load("./models/Maleria_CNN7_acc96.pth",map_location=torch.device("cpu")))
    pred = model_pred(img_tensor)

    if pred[0][0].item()>=pred[0][1].item():
        result = "Infected"
        chance = round(pred[0][0].item()*100,2)
    else:
        result = "Uninfected"
        chance = round(pred[0][1].item()*100,2)
    
    os.remove(path_to_image)
    
    return result,chance
