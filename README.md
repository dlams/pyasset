# pySsammwuLib (임시 이름)



## 1. Builder
### Builder

```python
from builder import Builder

class A:
    def __init__(self):
        self.a = int()
        self.b = float()
        self.c = str()

model1 = Builder(A).build()
model2 = Builder(A).a(5).build()
model3 = Builder(A).a("hello").b("world")
result = model3.build()
```

### RigidBuilder
```python
from builder import RigidBuilder

class A:
    def __init__(self):
        self.a = int()
        self.b = float()
        self.c = str()

model1 = RigidBuilder(A).build()
model2 = RigidBuilder(A).a(5).build()
# Make error - Type Error
    # Why? a is int, b is float.
    # rigid builder checking variable type.
model3 = RigidBuilder(A).a("hello").b("world")
```

## Percentage Bar
### bar
```python
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