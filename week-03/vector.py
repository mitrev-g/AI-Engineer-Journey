class Vector():
    def __init__(self, nums: list[float]) -> None:
        if len(nums) == 0:
            raise ValueError("Can not initialize an empty vector.")
        vec = nums.copy()
        self.body = vec

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.body})'

    def __len__(self) -> int:
        return len(self.body)

    def __str__(self) -> str:
        return str(tuple(self.body))

    # Time Complexity - O(n), where n is number of components 
    # - Worst case scenario is all elements of the vector are matching. We have to go through each individual element. 
    # Space Complexity - O(1) - We don't store anything
    def __eq__(self, vec: Vector) -> bool:
        if not isinstance(vec, Vector):
            return NotImplemented
        return self.body == vec.body

    # Time Complexity - O(n), where n is the length of the vector.
    # - We go through the loop n times each doing O(1) of work.
    # Space Complexity - O(n), res - holding a list with the same length as the input vectors
    def __add__(self, vec: object) -> Vector:
        if not isinstance(vec, Vector):
            return NotImplemented
        if len(self.body) != len(vec.body):
            raise ValueError("Both vectors must be of same length.")
        res=[]
        for a, b in zip(self.body, vec.body):
            res.append(a + b)
        return Vector(res)

    # Time Complexity - O(n), where n is the length of the vector
    # - We run the loop n times, doing O(1) of work
    # Space Complexity - O(n) - list with the same length as input vectors
    def dot(self, vec: Vector) -> float:
        if not isinstance(vec, Vector):
            raise TypeError("vec must be of type Vector")
        if len(self.body) != len(vec.body):
            raise ValueError("Both vectors must have equal length")
        res = []
        for a, b in zip(self.body, vec.body):
            res.append(a * b)
        return sum(res)
    