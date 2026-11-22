class GenerationConfig():
    created_count = 0
    MAX_TEMPERATURE = 2.0
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
    

    @temperature.setter
    def temperature(self, value: float) -> None:
        if type(value) not in [float, int]:
            raise TypeError("Value must be a number")
        if value < 0 or value > GenerationConfig.MAX_TEMPERATURE:
            raise ValueError(f"Temperature must be between 0 and {GenerationConfig.MAX_TEMPERATURE} inclusive")
        self._temperature = value

    @max_tokens.setter
    def max_tokens(self, tokens: int) -> None:
        if type(tokens) != int:
            raise TypeError("Tokens must be int")
        if tokens <= 0:
            raise ValueError("Max Tokens must be a positive int")
        self._max_tokens = tokens

    def __repr__(self) -> str:
        return f'{type(self).__name__}(temperature={self.temperature}, max_tokens={self.max_tokens})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GenerationConfig):
            return NotImplemented
        return self.temperature == other.temperature and self.max_tokens == other.max_tokens

    
    
        