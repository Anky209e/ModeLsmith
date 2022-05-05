import torch
from torchvision.transforms import ToTensor

import numpy as np
from PIL import Image
import os

class CNN7(torch.nn.Module):
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

def predict(path_to_image):
    size = 64

    img = Image.open(path_to_image)
    img_cls = ["Infected", "uninfected"]

    if img.size != (size,size):
        img = img.resize((size,size))
    
    transform = ToTensor()
    img_tensor = transform(img)
    img_tensor = img_tensor[:3]
    
    img_tensor = torch.reshape(img_tensor, (1,3,size,size))

    model_pred = CNN7()
    model_pred.load_state_dict(torch.load("./models/Maleria_CNN7_acc96.pth",map_location=torch.device("cpu")))

    pred = model_pred(img_tensor).detach()
    pred = np.array(pred[0])
    for i in range(len(img_cls)):
        pred[i] = round(pred[i]*100, 2)

    result = list(zip(img_cls, pred))
    result.sort(key=lambda x:x[1], reverse=True)
    
    os.remove(path_to_image)
    
    return result
