import json

class FileStorage():
    """
    A class FileStorage that serializes instances to a JSON file 
    and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            json.dump({str(k): v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        - Check if the JSON file (__file_path) exists
        - Otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
