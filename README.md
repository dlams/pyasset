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