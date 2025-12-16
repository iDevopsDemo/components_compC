"""Simple Storage Factory"""
from datavisualizer.storage.dummy import DummyStorage
from datavisualizer.storage.mysql import MySQLStorage

class StorageFactory:
    """ PersistenceFactory """

    @staticmethod
    def get_storage(storage_name):
        if storage_name == 'dummy':
            return DummyStorage()
        elif storage_name == 'mysql':
            return MySQLStorage()
        return None
