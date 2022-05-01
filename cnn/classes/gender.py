import torch
from torchvision.transforms import ToTensor

import numpy as np
from PIL import Image
from os import remove

class ResNet10(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
        self.res15t75 = torch.nn.Conv2d(15,75,1,2,0)
        self.res75t150 = torch.nn.Conv2d(75,150,1,2,0)
        self.res150t300 = torch.nn.Conv2d(150,300,1,2,0)
        
        self.conv15 = torch.nn.Conv2d(3,15,3,1,1)
        
        self.conv75a =  torch.nn.Conv2d(15,75,3,2,1)
        self.conv75b =  torch.nn.Conv2d(75,75,3,1,1)
        self.conv75c =  torch.nn.Conv2d(75,75,3,1,1)
        
        self.conv150a = torch.nn.Conv2d(75,150,3,2,1)
        self.conv150b = torch.nn.Conv2d(150,150,3,1,1)
        self.conv150c = torch.nn.Conv2d(150,150,3,1,1)
        
        self.conv300a = torch.nn.Conv2d(150,300,3,2,1)
        self.conv300b = torch.nn.Conv2d(300,300,3,1,1)
        self.conv300c = torch.nn.Conv2d(300,300,3,1,1)
        
        self.aapool = torch.nn.AvgPool2d(2,2)
        
        self.flat = torch.nn.Flatten()
        
        self.linear1 = torch.nn.Linear(1800,300)
        self.linear2 = torch.nn.Linear(300,2)
    
    def forward(self,data):
        
        out = torch.relu(self.conv15(data))
        
        x = self.res15t75(out)
        out = torch.relu(self.conv75a(out))
        out = torch.relu(self.conv75b(out) + x)
        out = torch.relu(self.conv75c(out))
        
        x = self.res75t150(out)
        out = torch.relu(self.conv150a(out))
        out = torch.relu(self.conv150b(out) + x)
        out = torch.relu(self.conv150c(out))
        
        x = self.res150t300(out)
        out = torch.relu(self.conv300a(out))
        out = torch.relu(self.conv300b(out) + x)
        out = torch.relu(self.conv300c(out))       
        
        out = self.aapool(out)
        out = self.aapool(out)
        
        out = self.flat(out)
        
        out = self.linear1(out)
        out = torch.relu(out)
        out = self.linear2(out)

        out = torch.softmax(out, -1)
        
        return out      


def predict_gender(path):
    img = Image.open(path)
    
    if img.size != (64,96):
        img = img.resize((64,96))

    pred_model = ResNet10()
    pred_model.load_state_dict(torch.load("./models/Gender_RN10_acc97.pth", map_location=torch.device("cpu")))
    
    img_cls = ['Female', 'Male']

    transform = ToTensor()
    img_tensor = transform(img)
    img_tensor = img_tensor[:3]
    
    img_tensor = torch.reshape(img_tensor, (1,3,96,64))
    
    pred = pred_model(img_tensor).detach()
    pred = np.array(pred[0])
    for i in range(len(img_cls)):
        pred[i] = round(pred[i]*100, 2)

    result = list(zip(img_cls, pred))
    result.sort(key=lambda x:x[1], reverse=True)

    remove(path)
    
    return result

