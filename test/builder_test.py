import unittest
from builder import Builder, RigidBuilder


class A:
    def __init__(self):
        self.a = int()
        self.b = float()
        self.c = str()

    def __str__(self):
        return ", ".join(map(str, [self.a, self.b, self.c]))


class Car:
    def __init__(self):
        self.name = "Undefined"
        self.speed = 0

    def __str__(self):
        return f"name : {self.name}, speed : {self.speed}"


class BuilderTestModel(unittest.TestCase):

    def test_builder_normal(self):
        model = Builder(A).build()
        self.assertEqual(model.a, int())
        self.assertEqual(model.b, float())
        self.assertEqual(model.c, str())

    def test_builder(self):
        value_a = 5
        model = Builder(A).a(value_a).build()
        self.assertEqual(model.a, value_a)

    def test_rigid_builder(self):
        name = "First Car"
        model = RigidBuilder(Car).name(name)
        self.assertEqual(model.build().name, name)

    def test_make_error(self):
        # make error
        error_value = "speed is 5"
        model = RigidBuilder(Car).speed(error_value)


if __name__ == '__main__':
    unittest.main()
