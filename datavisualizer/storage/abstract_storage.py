"""Abstract Storage Class"""

import json
from abc import ABCMeta, abstractmethod
from datavisualizer.logger.log import LOGGER

class AbstractStorage:
    """Abstract class for Storages

    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self._init_from_env()
        self.connect()

    @abstractmethod
    def _init_from_env(self):
        """This function allows to read env variables
        """

    @abstractmethod
    def connect(self):
        """This function allows to read env variables
        """

    @abstractmethod
    def read(self, query):
        """The function receives a message from a topic and processes it
           Return status code so the calling method knows what to do next
           The method should be public.
        """
