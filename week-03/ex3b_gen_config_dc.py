from dataclasses import dataclass
from typing import ClassVar
@dataclass(frozen=True)
class GenerationConfigDC:
    created_count: ClassVar[int] = 0
    MAX_TEMPERATURE: ClassVar[float] = 2.0
    temperature: float = 1.0
    max_tokens: int = 256

    # Time Complexity: O(1) - Always the same amount of checks.
    # Space Complexity: O(1) - No extra memory is created. The counter already exists
    def __post_init__(self) -> None:
        if type(self.temperature) not in [float, int]:
            raise TypeError("Value must be a number")
        if self.temperature < 0 or self.temperature > self.MAX_TEMPERATURE:
            raise ValueError(f"Temperature must be between 0 and {self.MAX_TEMPERATURE} inclusive")
        if type(self.max_tokens) != int:
            raise TypeError("Tokens must be int")
        if self.max_tokens <= 0:
            raise ValueError("Max Tokens must be a positive int")
        GenerationConfigDC.created_count += 1    