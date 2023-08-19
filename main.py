from pyasset import builder

@builder()
class A:
    def __init__(self) -> None:
        self.name = str()

    def __str__(self) -> str:
        return f"{self.name}"
    

if __name__ == '__main__':
    a = A.builder().name("hello").build()
    print(a)