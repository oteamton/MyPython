import argparse
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.autograd import Variable
import numpy as np
import os
import time
from model import YOLOv3
from dataset import CustomDataset

def parse_args():
    parser = argparse.ArgumentParser(description='Train YOLOv3 on custom dataset')
    parser.add_argument('--epochs', type=int, default=100, help='number of training epochs')
    parser.add_argument('--batch_size', type=int, default=32, help='training batch size')
    parser.add_argument('--lr', type=float, default=0.001, help='learning rate')
    parser.add_argument('--data_dir', type=str, default='data', help='directory containing the dataset')
    parser.add_argument('--weights_dir', type=str, default='weights', help='directory to save model weights')
    parser.add_argument('--num_classes', type=int, default=80, help='number of object classes')
    parser.add_argument('--img_size', type=int, default=416, help='input image size')
    args = parser.parse_args()
    return args

def train(args):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = YOLOv3(args.num_classes, args.img_size)
    model = model.to(device)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=args.lr)
    dataset = CustomDataset(args.data_dir, args.img_size)
    data_loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=True, num_workers=4)
    for epoch in range(args.epochs):
        running_loss = 0.0
        for i, (images, targets) in enumerate(data_loader):
            images = images.to(device)
            targets = targets.to(device)
            outputs = model(images)
            loss = criterion(outputs, targets)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, args.epochs, running_loss/len(data_loader)))
    if not os.path.exists(args.weights_dir):
        os.makedirs(args.weights_dir)
    torch.save(model.state_dict(), os.path.join(args.weights_dir, 'yolov3.pth'))

if __name__ == '__main__':
    args = parse_args()
    train(args)
