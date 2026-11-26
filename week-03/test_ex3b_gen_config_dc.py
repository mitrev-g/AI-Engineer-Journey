from ex3_gen_config import GenerationConfig
from ex3b_gen_config_dc import GenerationConfigDC
from dataclasses import FrozenInstanceError, replace
import pytest


# --- Part A ---
GEN_CON=[GenerationConfig, GenerationConfigDC]

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_defaults(cls):
    assert cls().temperature == 1.0
    assert cls().max_tokens == 256

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_temperature_zero(cls):
    gencon=cls(0)
    assert gencon.temperature == 0

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_temperature_two(cls):
    gencon=cls(2)
    assert gencon.temperature == 2
        

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_temperature_out_of_range_init(cls):
    with pytest.raises(ValueError):
        cls(5)

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_temperature_string(cls):
    with pytest.raises(TypeError):
        cls("five")

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_temperature_bool(cls):
    with pytest.raises(TypeError):
        cls(True)

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_max_tokens_negative(cls):
    with pytest.raises(ValueError):
        cls(0, -2)

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_max_tokens_zero(cls):
    with pytest.raises(ValueError):
        cls(1, 0)

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_max_tokens_float(cls):
    with pytest.raises(TypeError):
        cls(1, 2.5)

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_max_tokens_bool(cls):
    with pytest.raises(TypeError):
        cls(1, True)

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_max_tokens_string(cls):
    with pytest.raises(TypeError):
        cls(1, "three")

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_max_temp(cls):
    gencon = cls()
    assert gencon.MAX_TEMPERATURE == 2.0

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_created_count(cls):
    count = cls.created_count
    gencon = cls()
    gencon2 = cls()
    assert cls.created_count == count + 2

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_repr(cls):
    gencon = cls(temperature=0.7, max_tokens=256)
    assert repr(gencon) == f'{cls.__name__}(temperature=0.7, max_tokens=256)'

@pytest.mark.parametrize('cls', GEN_CON)
def test_gen_configs_eq(cls):
    gencon = cls(temperature=0.7, max_tokens=256)
    gencon2 = cls(temperature=0.7, max_tokens=256)
    assert gencon == gencon2
    assert gencon != "Hello tests!"
    assert gencon != True
    assert cls(temperature=0.7) != cls(temperature=1.9)
    assert cls(temperature=0, max_tokens=512) != cls(temperature=0, max_tokens=513)
    

# --- Part B ---
def test_gen_configs_dc_frozen():
    gencon = GenerationConfigDC()
    with pytest.raises(FrozenInstanceError):
        gencon.temperature = 0.5

def test_gen_configs_dc_replace():
    gencon = GenerationConfigDC()
    gencon2 = replace(gencon, temperature=0.5)
    assert gencon.temperature == 1
    assert gencon2.temperature == 0.5

def test_gen_configs_dc_replace_invalid_temp():
    gencon = GenerationConfigDC()
    with pytest.raises(ValueError):
        gencon2 = replace(gencon, temperature=5)