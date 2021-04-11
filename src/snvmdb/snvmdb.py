import json
import os
from typing import Any, List, Dict, NoReturn

from .errors import (
    DatabaseNotFoundError,
    NotListError,
    NotHashError,
    NotSecondActionError
)


class SnvmDB:
    """
    Simple and easy-to-use database. Yes, JSON database. I want to make it, and I made.
    """
    def __init__(self, filename: str, auto_sync: bool = False):
        self.auto_sync = auto_sync
        if not filename == 'memory':
            location = os.path.expanduser(filename)
            self.location = location
            if os.path.exists(location):
                self.__load()
            else:
                raise DatabaseNotFoundError('Can\'t find database file.')
        else:
            self.db = {}

    def __load(self):
        """
        Internal method to load database
        """
        try: 
            with open(self.location, 'r') as db:
                self.db = json.load(db)
        except json.decoder.JSONDecodeError:
            if os.stat(self.location).st_size == 0:
                self.db = {}
            else:
                return

    def __autosync(self):
        """
        Internal method to sync changes automatically
        """
        if self.auto_sync:
            self.sync()

    def sync(self):
        """
        Manual changes syncing.
        Returns True if synced.
        """
        with open(self.location, 'w') as db:
            json.dump(self.db, db)
        return True

    def add(self, key: str, value: Any) -> Any:
        """
        Add string-any pair to database.
        Returns this value.
        """
        self.db[str(key)] = value
        self.__autosync()
        return self.db[str(key)]

    def get(self, key: str) -> Any:
        """
        Get value from database by its key, and return it.
        """
        return self.db[str(key)]

    def remove(self, key: str) -> bool:
        """
        Delete key from database.
        Returns True if deleted.
        """
        del self.db[key]
        return True
        self.__autosync()

    def get_keys(self) -> List:
        """
        Get all keys in database, return it.
        """
        return list(self.db.keys())
    
    def get_all(self) -> Dict[str, Any]:
        """
        Returns dictionary of all keys in database.
        """
        return self.db

    def has(self, key: str) -> bool:
        """
        Checks if key exists in database.
        """
        return key in self.db

    def append_list(self, name: str, value: str) -> bool:
        """
        Append value to list created with `Database.add('value', [])`
        Returns True on success.
        Raises NotListError if trying to add to not list value.
        """
        if isinstance(self.db[name], list):
            self.db[name].append(value)
            self.__autosync()
            return True
        else:
            raise NotListError('Can\'t use list function on other values')

    def get_list(self, name: str) -> List[Any]:
        """
        Get list values, returns it.
        Raises NotListError if trying to get values of not list.
        """
        if isinstance(self.db[name], list):
            return self.db[name]
        else:
            raise NotListError('Can\'t use list function on other values')

    def get_list_value(self, name: str, pos: int) -> Any:
        """
        Get list value by its position, return it.
        Raises NotListError if trying to get value of not list.
        """
        if isinstance(self.db[name], list):
            return self.db[name][pos]
        else:
            raise NotListError('Can\'t use list function on other values')

    def remove_list_value(self, name: str, pos: int = None, value: str = None) -> bool:
        """
        Remove value from list by position or value name.
        Return True on success.
        Raises Exception if trying to use `pos` and `value` at one time.
        Raises NotListError if trying to remove value from not list.
        """
        if isinstance(self.db[name], list):
            if value and pos:
                raise Exception('Don\'t use `pos` and `value` at one time!')
            if value:
                self.db[name].remove(value)
                self.__autosync()
                return True
            if pos:
                del self.db[name][pos]
                self.__autosync()
                return True
        else:
            raise NotListError('Can\'t use list function on other values')

    def append_hash(self, name: str, key: str, value: Any) -> bool:
        """
        Append key-value pair to hash-table(which is basically a dict).
        Returns True.
        Raises NotHashError if trying append to not hash.
        """
        if isinstance(self.db[name], dict):
            self.db[name][str(key)] = value
            self.__autosync()
            return True
        else:
            raise NotHashError('Can\'t use hash function on other values')

    def get_hash_values(self, name: str) -> List:
        """
        Get values from hash, return it.
        Raises NotHashError if trying to get from not hash.
        """
        if isinstance(self.db[name], dict):
            return list(self.db[name].values())
        else:
            raise NotHashError('Can\'t use hash function on other values')

    def get_hash_keys(self, name: str) -> List:
        """
        Get keys from hash, return it.
        Raises NotHashError if trying to get from not hash.
        """
        if isinstance(self.db[name], dict):
            return list(self.db[name].keys())
        else:
            raise NotHashError('Can\'t use hash function on other values')

    def get_hash(self, name: str) -> Dict[str, Any]:
        """
        Get all hash contents, return it.
        Raises NotHasheError if trying to get not hash.
        """
        if isinstance(self.db[name], dict):
            return self.db[name]
        else:
            raise NotHashError('Can\'t use hash function on other values')

    def remove_hash_value(self, name: str, key: str) -> bool:
        """
        Remove value from hash.
        Returns True.
        Raises NotHashError if trying to remove from not hash.
        """
        if isinstance(self.db[name], dict):
            del self.db[name][key]
            return True
        else:
            raise NotHashError('Can\'t use hash function on other values')

    def get_hash_value(self, name: str, key: str) -> Any:
        """
        Get value from hash by its key, return it.
        Raises NotHashError if trying to get from not hash.
        """
        if isinstance(self.db[name], dict):
            return self.db[name][key]
        else:
            raise NotHashError('Can\'t use hash function on other values')

    def destroy(self) -> NoReturn:
        """
        Destory database.
        This action is irrevisible!.
        To proceed with it, you need to call .completely_destroy() after it!
        """
        self.before_destroy = True
        return 'Continue'

    def completely_destroy(self) -> NoReturn:
        if not self.before_destroy:
            raise NotSecondActionError('You need to call this after .destroy()!')
        
        self.db = {}
        self.__autosync()
        return True
