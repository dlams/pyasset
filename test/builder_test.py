import unittest
from builder import builder


@builder()
class MyClass:
    def __init__(self):
        self.integer = 32
        self.string = "Undefined"

    def __str__(self):
        return str(self.integer) + ", " + self.string


@builder(
    build_method_name="run",
    setter_prefix="set_"
)
class SecondMyClass:
    def __init__(self):
        self.ready = bool(False)
        self.initial_speed = float()

    def __str__(self):
        return "speed : " + str(self.initial_speed) if self.ready else "not ready."


@builder(type_check=True)
class ThirdMyClass:
    def __init__(self):
        self.integer = int()
        self.float = float()
        self.string = str()
        self.boolean = bool()


class BuilderTestModel(unittest.TestCase):
    def test_runs(self):
        print("✨ Not use builder(). ✨")
        print(MyClass())
        print()

        print("✨ Use default builder ✨")
        obj = MyClass.builder().integer(64)
        obj.string("define.")
        print(obj.build())
        print()

        vehicle1 = SecondMyClass.builder()
        vehicle1.set_ready(True)
        vehicle1.set_initial_speed(0.5)

        vehicle2 = SecondMyClass.builder().set_initial_speed(2023).run()

        print("""✨ Check builder's initial options. ✨
    - build_method_name = "run",
    - setter_prefix = "set_"
                """)
        print("   Vehicle 1 :", vehicle1.run())
        print("   Vehicle 2 :", vehicle2)
        print()

    def test_z_make_error(self):
        print("❌ Make Type Error <- type check ❌")
        obj = ThirdMyClass.builder()
        obj.integer(1)
        print("   - type_check option prevent other type")
        print("   - here. expect float, but input is str")
        obj.float("MAKE ERROR")


if __name__ == '__main__':
    unittest.main()
