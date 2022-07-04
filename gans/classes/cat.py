from torch import nn
import torch
from torchvision.utils import save_image

media_dir = './media/gans_images/'
LATENT_SIZE = 100
MEAN = (0.4819, 0.4325, 0.3845)
DEV = (0.2602, 0.2519, 0.2537)

G = nn.Sequential(
    nn.ConvTranspose2d(LATENT_SIZE,600,4,1,0),#600 4 
    nn.BatchNorm2d(600),
    nn.ReLU(),

    nn.ConvTranspose2d(600,300,4,2,1),#300 8
    nn.BatchNorm2d(300),
    nn.ReLU(),
    
    nn.ConvTranspose2d(300,150,4,2,1),#150 16
    nn.BatchNorm2d(150),
    nn.ReLU(),
    
    nn.ConvTranspose2d(150,50,4,2,1),#60 32
    nn.BatchNorm2d(50),
    nn.ReLU(),
    
    nn.ConvTranspose2d(50,3,4,2,1),#3 64
    nn.Tanh()
)

def generate(matrix=4):
    G.load_state_dict(torch.load("./models/G_cat.pth", map_location="cpu"))
    
    images = G(torch.randn(matrix**2, LATENT_SIZE ,1,1))

    for i in range(len(images)):
        images[i][0]=images[i][0]*DEV[0]+MEAN[0]
        images[i][1]=images[i][1]*DEV[1]+MEAN[1]
        images[i][2]=images[i][2]*DEV[2]+MEAN[2]

    name = "cat.png"
    save_image(images,media_dir+name,nrow=matrix)

    return name