from functools import partial


class BuilderPattern:
    def __init__(self, cls, build_method_name, setter_prefix, type_check):
        temp_class = cls()
        self.__dict__.update(
            {str(setter_prefix) + key: partial(self.__set_variable, key) for key in temp_class.__dict__})
        if type_check:
            self.__type = {key: type(key) for key in temp_class.__dict__}
        del temp_class
        setattr(self, build_method_name, self.__build)
        self.type_check = type_check
        self.__parameters = {}
        self.__main_class = cls

    def __set_variable(self, key, value):
        if self.type_check: assert not isinstance(value, self.__type[key]), TypeError
        self.__parameters.update({key: value})
        return self

    def __build(self):
        main = self.__main_class()
        main.__dict__.update(self.__parameters)
        return main

    def __str__(self):
        return f"{self.__main_class.__name__} builder"

    def __repr__(self):
        return f"{self.__main_class.__name__} builder, {self.__parameters}"


def builder(build_method_name="build", setter_prefix="", type_check=False):
    def decorator(cls):
        setattr(cls, 'builder', partial(BuilderPattern, cls, build_method_name, setter_prefix, type_check))
        return cls

    return decorator
