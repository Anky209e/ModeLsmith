import torch
from torchvision.transforms import ToTensor

import numpy as np
from PIL import Image
import os

# Eye and Sign model
class CNN8(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.network = torch.nn.Sequential(
            # 3 128
            torch.nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            # 32 64
            torch.nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            torch.nn.MaxPool2d(2, 2),
            # 64 32
            torch.nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            # 128 16
            torch.nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1),
            torch.nn.MaxPool2d(2, 2),
            # 128 8
            torch.nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            # 256 4
            torch.nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1),
            torch.nn.MaxPool2d(2, 2),
            # 256 2
            torch.nn.Flatten(),
            # 256*2*2
            torch.nn.Linear(256 * 2 * 2, 128),
            torch.nn.ReLU(),
            # 128
            torch.nn.Linear(128, 26)
            # 26
        )
    def forward(self, inputs):
        out = self.network(inputs)
        return torch.softmax(out, dim=-1)

def predict(path_to_image):
    size = 128

    img = Image.open(path_to_image)
    img_cls = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    if img.size != (size,size):
        img = img.resize((size,size))
    
    transform = ToTensor()
    img_tensor = transform(img)
    img_tensor = img_tensor[:3]
    
    img_tensor = torch.reshape(img_tensor, (1,3,size,size))

    model_pred = CNN8()
    model_pred.load_state_dict(torch.load("./models/Sign_CNN8_acc97.pth",map_location=torch.device("cpu")))

    pred = model_pred(img_tensor).detach()
    pred = np.array(pred[0])
    for i in range(len(img_cls)):
        pred[i] = round(pred[i]*100, 2)

    result = list(zip(img_cls, pred))
    result.sort(key=lambda x:x[1], reverse=True)
    
    os.remove(path_to_image)
    
    return result


