# -*- coding: utf-8 -*-
# @Time    : 2025-02-23 19:39
# @Author  : sun bo
# @File    : LDP_protocol.py
# @Software: PyCharm


from abc import ABC, abstractmethod

class LDPProtocol(ABC):
    """
    the abstract base class, OUE, OLH, kRR can be derived from this
    """
    def __init__(self, epsilon):
        self.epsilon = epsilon
        self.domain = None
        self.p = None
        self.q = None

    @abstractmethod
    def load_data(self, file_path):
        pass

    @abstractmethod
    def encode(self, raw_item):
        pass

    @abstractmethod
    def perturb(self, encoded_value):
        pass

    @abstractmethod
    def aggregate(self, perturbed_values):
        pass