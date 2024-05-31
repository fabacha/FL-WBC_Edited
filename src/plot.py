import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import numpy as np
import pandas as pd
import seaborn as sns
import numpy as np
from torch.utils.data import Subset, DataLoader
import os
from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset, ConcatDataset, DataLoader


from functools import partial
from matplotlib import pyplot as plt


# Assuming traindata is the CIFAR-10 dataset
idx_to_class = {v: k for k, v in datasets.CIFAR10('./data', download=True, train=True).class_to_idx.items()}

def get_class_distribution(dataset):
    count_dict = {k: 0 for k in idx_to_class.values()} # Initialize dictionary

    for _, label in dataset:
        for l in label.tolist():  # Convert label tensor to list
            l = idx_to_class[l]
            count_dict[l] += 1

    return count_dict

def plot_class_distribution(data):
    plt.figure(figsize=(20, 10))
    for i, loader in enumerate(data, 1):
        plt.subplot(2, 5, i)
        class_dist = get_class_distribution(loader)
        sns.barplot(x=list(class_dist.keys()), y=list(class_dist.values())).set_title(f'Client {i} Class Distribution')
        plt.xlabel('Class')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


