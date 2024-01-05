class ParentTest:
    def __init__(self) -> None:
        print("Parent")


class ChildTest(ParentTest):
    name = "Name"; last = "test"

    # Object Constructor
    def __init__(self) -> None:
        super()
        print("Child")
        pass
    
    # Object Destructor
    def __del__(self) -> None:
        pass
    
    # Method Overloading
    def sum(self, a: int, b: int) -> int:
        return a + b
    
    # Method Overloading
    def sum(self, a: str, b: str) -> int:
        return a + b
    
    # Method Overloading
    def sum(self, a: int, b: str) -> int:
        return str(a) + b

a = ChildTest()