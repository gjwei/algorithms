# coding: utf-8
# Author: gjwei
import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self, in_features, units):
        super(Model, self).__init__()
        self.layer = nn.Linear(in_features, units)
        self.softmax = nn.LogSoftmax(dim=-1)
        self.loss_function = nn.NLLLoss(size_average=True)

        self.reset_parameters()

    def reset_parameters(self):
        nn.init.xavier_uniform_(self.layer.weight)

    def forward(self, input):
        output = self.softmax(self.layer(input))
        return output

    def calcuate_loss(self, labels, logits):
        return self.loss_function(logits, labels)


if __name__ == '__main__':
    x = torch.rand((32, 100))
    label = torch.randint(low=0, high=9, size=(32, )).long()

    model = Model(100, 10)

    logits = model(x)
    print(label.size())
    print(logits.size())
    print(model.calcuate_loss(label, logits))

    x = x * 2
    print(model.calcuate_loss(label, model(x)))