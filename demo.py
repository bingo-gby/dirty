import torch
print(torch.cuda.is_available())

from torch.backends import cudnn
print(cudnn.is_available())

print(torch.__version__)