import torch
from torch import nn
from torchvision.utils import save_image

media_dir = './media/gans_images/'
LATENT_SIZE = 100
MEAN = (0.520236, 0.425154, 0.380275)
DEV  = (0.250834, 0.225002, 0.222173)

D = nn.Sequential(
    nn.Conv2d(3,60,4,2,1),#60 64
    nn.BatchNorm2d(60),
    nn.LeakyReLU(0.2),

    nn.Conv2d(60,125,4,2,1),#125 32
    nn.BatchNorm2d(125),
    nn.LeakyReLU(0.2),

    nn.Conv2d(125,250,4,2,1),#250 16
    nn.BatchNorm2d(250),
    nn.LeakyReLU(0.2),

    nn.Conv2d(250,500,4,2,1),#500 8
    nn.BatchNorm2d(500),
    nn.LeakyReLU(0.2),

    nn.Conv2d(500,800,3,2,1),#800 4
    nn.BatchNorm2d(800),
    nn.LeakyReLU(0.2),

    nn.AdaptiveAvgPool2d(1),#800 1 1
    nn.Flatten(),#800

    nn.Linear(800,20),
    nn.LeakyReLU(0.2),
    nn.Linear(20,1),

    nn.Sigmoid()
)

G = nn.Sequential(
    nn.ConvTranspose2d(LATENT_SIZE,800,4,1,0),#800 4 
    nn.BatchNorm2d(800),
    nn.ReLU(),
    nn.ConvTranspose2d(800,400,4,2,1),#400 8
    nn.BatchNorm2d(400),
    nn.ReLU(),
    nn.ConvTranspose2d(400,200,4,2,1),#200 16
    nn.BatchNorm2d(200),
    nn.ReLU(),
    nn.ConvTranspose2d(200,100,4,2,1),#100 32
    nn.BatchNorm2d(100),
    nn.ReLU(),
    nn.ConvTranspose2d(100,50,4,2,1),#50 64
    nn.BatchNorm2d(50),
    nn.ReLU(),
    nn.ConvTranspose2d(50,3,4,2,1),#3 128
    nn.Tanh()
)



def generate(grid1=7, grid2=3):
    D.load_state_dict(torch.load("./models/Human_CNN6.pth",map_location="cpu"))
    G.load_state_dict(torch.load("./models/G_Human.pth",map_location="cpu"))

    rand = torch.randn((grid1**2,LATENT_SIZE,1,1))

    images = G(rand)

    for i in range(grid1**2):
        images[i][0]=images[i][0]*DEV[0]+ MEAN[0]
        images[i][1]=images[i][1]*DEV[1]+ MEAN[1]
        images[i][2]=images[i][2]*DEV[2]+ MEAN[2] 

    preds = D(images)

    better_images = torch.zeros(grid2**2,3,128,128)
    
    for i in range(grid2**2):
        max_pred = preds.max()
        max_pred_index = torch.where(preds==max_pred)[0].item()

        best_image = images[max_pred_index]
        better_images[i]=best_image

        preds[max_pred_index] = torch.zeros(1)

    name = "human.png"

    save_image(better_images,media_dir + name, nrow=grid2)
    
    return name