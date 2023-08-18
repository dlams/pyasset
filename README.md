# pySsammwuLib (Temporary Title)


## 1. Builder 
### Builder Decorator

> If you want to apply the `builder pattern` to your custom class, follow these steps:
1. load code using `from builder import builder`
2. Place the desired variables in the class constructor function (def __init__(self)).
3. Attach the `@builder` decorator at the top of the class.
4. Done.

```python
# For example
from builder import builder

@builder()
class A:
    def __init__(self):
        self.name = str()
        self.age = 0
```

> If you've written the builder decorator but don't want to apply the builder pattern, simply avoid appending `.builder()`!  

The instance will be created following the existing `__init__` function.

```python
a = A()   # you can use A.builder() 

---
a.name   # ""
a.age   # 0
```

```python
from builder import builder

# It also provides several options.

# 1. use decorator only @builder()
#  - non-check type
#  - last method is .build()
#  - default method use : ex) CLASS.builder().name("NAME")

@builder()
class MyClass:
    def __init__(self):
        self.integer = 32
        self.string = "Undefined"

    def __str__(self):
        return str(self.integer) + ", " + self.string

    
obj = MyClass.builder().integer(64).build()
    
    
# 2. use decorator @builder() with some options.
#  - non-check type
#  - last method is .run()
#  - prefix method use : ex) CLASS.builder().set_name("NAME")
    
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



vehicle1 = SecondMyClass.builder()
vehicle1.set_ready(True)
vehicle1.set_initial_speed(0.5)
vehicle1.run()

vehicle2 = SecondMyClass.builder().set_initial_speed(2023).run()


# 3. use decorator @builder() with type_check.
#  - check type, if not matched type? raise TypeError
#  - Of course, it can be combined with other options

@builder(type_check=True)
class ThirdMyClass:
    def __init__(self):
        self.integer = int()
        self.float = float()
        self.string = str()
        self.boolean = bool()

        
obj = ThirdMyClass.builder()
obj.integer(1)
# error
obj.float("MAKE ERROR")
```

### Debugging mode for builder
```python
# you want target of builder class
class BuilderPattern:
    ...
    
    def __str__(self):
        return f"{<CLASS>.__name__} builder"

    def __repr__(self):
        return f"{<CLASS>.__name__} builder, {<PARAMETERS>}"

# you can use str(<BUILDER_CLASS>) return <TARGET> builder.
# and use repr(<BUILDER_CLASS>) retrun <TARGER> builder, and <KEY: VALUE> maps.
```


## Percentage Bar (Under Improvement)
### bar

```python
# print colored bar in terminal.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 

from percentage.captions import PercentageValueCaption, PercentageTinyTimeSpanCaption
from percentage.bar import BarPercentage
from time import sleep

# make percentage bar from 0 to 100.
bar = BarPercentage(0, 100)
# caption - print value like [1/100].
bar.add_caption(PercentageValueCaption)
# caption - print time like 0.42 s.
bar.add_caption(PercentageTinyTimeSpanCaption)

for _ in range(100):
    sleep(0.05)
    # percentage += 1
    bar.add_value(1)
    # print percentage bar
    bar.update()

# clear bar state ( value, captions data )
# but, not "\n" print
bar.clear()
print()


# print bar 50%
bar = BarPercentage(0, 100)
for _ in range(50):
    bar.add_value(1)
bar.update()


# print bar 75% (and from 0 to 4)
bar = BarPercentage(0, 4)
bar.add_value(3)
bar.update()
```