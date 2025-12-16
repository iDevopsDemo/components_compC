""" DummyStorage """
from datavisualizer.logger.log import LOGGER
from datavisualizer.storage.abstract_storage import AbstractStorage

class DummyStorage(AbstractStorage):

    """ DummyStorage """

    def _init_from_env(self):
        """ Get env variables """
        return

    def connect(self):
        return True

    def read(self, query):
        items = [dict(topic='Topic1', message='Message1'),
                dict(topic='Topic2', message='Message2'),
                dict(topic='Topic3', message='Message3')]
        return items
