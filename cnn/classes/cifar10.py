import torch
import numpy as np
from PIL import Image


class ResNet12(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.norm15 = torch.nn.BatchNorm2d(15)
        self.norm30 = torch.nn.BatchNorm2d(30)
        self.norm60 = torch.nn.BatchNorm2d(60)
        self.norm120 = torch.nn.BatchNorm2d(120)
        self.norm200 = torch.nn.BatchNorm2d(200)
        self.norm360 = torch.nn.BatchNorm2d(360)
        
        self.conv1 = torch.nn.Conv2d(3,15,kernel_size=3,stride=1,padding=1)
        
        self.conv2 = torch.nn.Conv2d(15,30,kernel_size=3,stride=1,padding=1)
        
        self.conv3 = torch.nn.Conv2d(30,60,kernel_size=3,stride=2,padding=1)
        
        self.res1 = torch.nn.Conv2d(60,120,kernel_size=1,stride=1,padding=0)
        self.conv4 = torch.nn.Conv2d(60,120,kernel_size=3,stride=1,padding=1)
        
        self.res2 = torch.nn.Conv2d(120,200,kernel_size=1,stride=2,padding=0)
        self.conv5 = torch.nn.Conv2d(120,200,kernel_size=3,stride=2,padding=1)
        self.res3 = torch.nn.Conv2d(200,200,kernel_size=1,stride=1,padding=0)
        self.conv6 = torch.nn.Conv2d(200,200,kernel_size=3,stride=1,padding=1)
        self.conv7 = torch.nn.Conv2d(200,200,kernel_size=3,stride=1,padding=1)
        self.conv7b = torch.nn.Conv2d(200,200,kernel_size=3,stride=1,padding=1)
        
        self.res4 = torch.nn.Conv2d(200,360,kernel_size=1,stride=2,padding=0)
        self.conv8 = torch.nn.Conv2d(200,360,kernel_size=3,stride=2,padding=1)
        self.res5 = torch.nn.Conv2d(360,360,kernel_size=1,stride=1,padding=0)
        self.conv9 = torch.nn.Conv2d(360,360,kernel_size=3,stride=1,padding=1)
        self.conv10 = torch.nn.Conv2d(360,360,kernel_size=3,stride=1,padding=1)
        self.conv10b = torch.nn.Conv2d(360,360,kernel_size=3,stride=1,padding=1)
        
        
        self.pool = torch.nn.MaxPool2d(2,2)
        self.avgpool = torch.nn.AvgPool2d(2,2)
        self.flat = torch.nn.Flatten()
        
        self.linear = torch.nn.Linear(360,10)
    

    def forward(self, data):
        # data 3 32 32

        out = torch.relu(self.norm15(self.conv1(data)))#15 32 32
        out = torch.relu(self.norm30(self.conv2(out)))#30 32 32
        
        out = torch.relu(self.norm60(self.conv3(out)))#60 16 16
        x = self.res1(out)#120 16 16
        out = torch.relu(self.norm120(self.conv4(out) + x))#120 16 16
        
        x = self.res2(out)#200 8 8
        out = torch.relu(self.norm200(self.conv5(out) + x))#200 8 8
        out = torch.relu(self.conv6(out))#200 8 8
        out = torch.relu(self.conv7(out) + x)#200 8 8
        out = torch.relu(self.conv7b(out))#200 8 8
        
        x = self.res4(out)#360 4 4
        out = torch.relu(self.norm360(self.conv8(out) + x))#360 4 4
        out = torch.relu(self.conv9(out))#360 4 4
        out = torch.relu(self.conv10(out)+x)#360 4 4 
        out = torch.relu(self.conv10b(out))#360 4 4 
        
        
        out = self.avgpool(out)#360 2 2
        out = self.avgpool(out)#360 1 1
        
        out = self.flat(out)#360
        out = self.linear(out)#10
        
        out = torch.softmax(out,dim=-1)
        
        return out

def predict(path,model):
    img = Image.open(path)
    
    if img.size != (32,32):
        img = img.resize((32,32))
    
    transform = ToTensor()
    img_tensor =torch.reshape(transform(img) , (1,3,64,64))

    model_pred = ResNet12()

    img_arr = img_arr/255
    img_tsr = torch.Tensor([img_arr])
    img_tsr = img_tsr.permute(0,3,1,2)
    
    for i in range(3):
        img_tsr[0][i] = (img_tsr[0][i]-mean[i])/dev[i] 
    
    pred = model(img_tsr).detach()
    pred = np.array(pred[0])
    pred_index = np.where(pred==max(pred))[0][0]
    
    print("Prediction: ",img_cls[pred_index])