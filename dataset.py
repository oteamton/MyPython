import os
import torch
import numpy as np
import cv2

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.img_files = os.listdir(root_dir)

    def __len__(self):
        return len(self.img_files)

    def __getitem__(self, idx):
        img_path = os.path.join(self.root_dir, self.img_files[idx])
        image = cv2.imread(img_path)
        target = np.zeros((1, 5))
        target[0, 0] = idx
        target[0, 1:] = np.array([0.5, 0.5, 0.5, 0.5])
        if self.transform:
            image = self.transform(image)
        return image, target
