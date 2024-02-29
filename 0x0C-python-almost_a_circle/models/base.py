#!/usr/bin/python3
"""Define class"""
import json


class Base:
    """Class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """stringfy data"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """String representaion"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """deserialize json string"""
        my_list = []
        if json_string is None or json_string == "":
            return my_list
        else:
            my_list = json.loads(json_string)
            return my_list

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiation of dict attr"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                my_inst_list = Base.from_json_string(f.read())
            return [cls.create(**d) for d in my_inst_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list of instances into csv format"""
        file_name = str(cls.__name__) + ".csv"
        with open(file_name, "w") as f:
                if list_objs is None:
                    f.write([])
                else:
                    list_objc = [c.to_dictionary() for c in list_objs]
                    f.write(Base.to_json_string(list_objc))
    
    @classmethod
    def load_from_file_csv(cls):
        """return list of instances"""
        filename = str(cls.__name__) + ".csv"
        try:
            with open(filename, "r") as f:
                my_csv_inst = Base.from_json_string(f.read())
            return [cls.create(**d) for d in my_csv_inst]
        except IOError:
            return []
        
