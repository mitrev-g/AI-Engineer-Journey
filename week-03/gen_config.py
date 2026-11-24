class GenerationConfig():
    created_count = 0
    MAX_TEMPERATURE = 2.0

    # Time Complexity: O(1) - Calls the setters so O(1) + O(1) which is O(1)
    # Space Complexity: O(1) - 3 variables in total.
    def __init__(self, temperature: float=1.0, max_tokens: int=256) -> None:
        self.temperature = temperature
        self.max_tokens = max_tokens
        GenerationConfig.created_count += 1

    @property
    def temperature(self) -> float:
        return self._temperature

    @property
    def max_tokens(self) -> int:
        return self._max_tokens
    

    # Time Complexity: O(1) - a fixed number of checks (type, range) and one assignment, with no loops.
    # Space Complexity: O(1) - There is always just 1 variable, no matter how many times you change it.
    @temperature.setter
    def temperature(self, value: float) -> None:
        if type(value) not in [float, int]:
            raise TypeError("Value must be a number")
        if value < 0 or value > GenerationConfig.MAX_TEMPERATURE:
            raise ValueError(f"Temperature must be between 0 and {GenerationConfig.MAX_TEMPERATURE} inclusive")
        self._temperature = value

    # Time Complexity: O(1) - fixed number of checks (type, range) and one assignment, with no loops.
    # Space Complexity: O(1) - There is always just 1 variable, no matter how many times you change it.
    @max_tokens.setter
    def max_tokens(self, tokens: int) -> None:
        if type(tokens) != int:
            raise TypeError("Tokens must be int")
        if tokens <= 0:
            raise ValueError("Max Tokens must be a positive int")
        self._max_tokens = tokens

    # Time Complexity: O(1) - it just returns a string, doing O(1) of work reading all 3 variables and formatting them in a string.
    # Space Complexity: O(1) - stores just 1 string with fixed length.
    def __repr__(self) -> str:
        return f'{type(self).__name__}(temperature={self.temperature}, max_tokens={self.max_tokens})'

    # Time Complexity: O(1) - makes 2 comparisons and 1 check which will always need the same amount of time 
    # Space Complexity: O(1) - doesn't store anything.
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GenerationConfig):
            return NotImplemented
        return self.temperature == other.temperature and self.max_tokens == other.max_tokens

    
    
        