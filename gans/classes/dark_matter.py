
import torch
from torch import nn

from torchvision.utils import save_image

import os

stats = (0.5, 0.5, 0.5), (0.5, 0.5, 0.5)
sample_dir = './media/gans_images'
os.makedirs(sample_dir, exist_ok=True)

generator = torch.nn.Sequential(
    # in: latent_size x 1 x 1

    nn.ConvTranspose2d(128 , 512, kernel_size=4, stride=1, padding=0, bias=False),
    nn.BatchNorm2d(512),
    nn.ReLU(True),
    # out: 512 x 4 x 4

    nn.ConvTranspose2d(512, 256, kernel_size=4, stride=2, padding=1, bias=False),
    nn.BatchNorm2d(256),
    nn.ReLU(True),
    # out: 256 x 8 x 8

    nn.ConvTranspose2d(256, 128, kernel_size=4, stride=2, padding=1, bias=False),
    nn.BatchNorm2d(128),
    nn.ReLU(True),
    # out: 128 x 16 x 16

    nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1, bias=False),
    nn.BatchNorm2d(64),
    nn.ReLU(True),
    # out: 64 x 32 x 32

    nn.ConvTranspose2d(64, 3, kernel_size=4, stride=2, padding=1, bias=False),
    nn.Tanh()
    # out: 3 x 64 x 64
)



def denorm(img_tensors):
    return img_tensors * stats[1][0] + stats[0][0]


def save_samples(index=4):
    fixed_latent = torch.randn(index**2, 128, 1, 1)
    generator.load_state_dict(torch.load("./models/G_matter.pth", map_location="cpu"))
    fake_images = generator(fixed_latent)
    fake_fname = 'dark_matter.png'
    
    save_image(denorm(fake_images), os.path.join(sample_dir, fake_fname),nrow=index)
    
    return fake_fname

