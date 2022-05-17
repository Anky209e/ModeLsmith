
import torch
from torch import nn

from torchvision.utils import save_image

import os

stats = (0.5, 0.5, 0.5), (0.5, 0.5, 0.5)
sample_dir = './media/gans_images'
os.makedirs(sample_dir, exist_ok=True)

generator = nn.Sequential(
    #  seed_size x 1 x 1
    nn.ConvTranspose2d(128, 512, kernel_size=4, padding=0, stride=1, bias=False),
    nn.BatchNorm2d(512),
    nn.ReLU(True),
    # 512 x 4 x 4
    
    nn.ConvTranspose2d(512, 256, kernel_size=4, padding=1, stride=2, bias=False),
    nn.BatchNorm2d(256),
    nn.ReLU(True),
    # 256 x 8 x 8
    
    nn.ConvTranspose2d(256, 128, kernel_size=4, padding=1, stride=2, bias=False),
    nn.BatchNorm2d(128),
    nn.ReLU(True),
    #  128 x 16 x 16
    
    nn.ConvTranspose2d(128, 64, kernel_size=4, padding=1, stride=2, bias=False),
    nn.BatchNorm2d(64),
    nn.ReLU(True),
    #  64 x 32 x 32
    
    nn.ConvTranspose2d(64, 32, kernel_size=4, padding=1, stride=2, bias=False),
    nn.BatchNorm2d(32),
    nn.ReLU(True),
    #  32 x 64 x 64
    
    nn.ConvTranspose2d(32, 16, kernel_size=4, padding=1, stride=2, bias=False),
    nn.BatchNorm2d(16),
    nn.ReLU(True),
    #  16 x 128 x 128
    
    nn.ConvTranspose2d(16, 3, kernel_size=4, padding=1, stride=2, bias=False),
    nn.Tanh()
    #  3 x 256 x 256
)



def denorm(img_tensors):
    return img_tensors * stats[1][0] + stats[0][0]


def save_samples(index=4):
    fixed_latent = torch.randn(index**2, 128, 1, 1)
    generator.load_state_dict(torch.load("./models/G_flower_imit.pth", map_location="cpu"))
    fake_images = generator(fixed_latent)
    fake_fname = 'flower_imit.png'
    
    save_image(denorm(fake_images), os.path.join(sample_dir, fake_fname),nrow=index)
    
    return fake_fname

