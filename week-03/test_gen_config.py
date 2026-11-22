from gen_config import GenerationConfig
import pytest

def test_gen_config_temperature():
    gencon = GenerationConfig()
    gencon.temperature = 1.5
    assert gencon.temperature == 1.5

def test_gen_config_temperature_zero():
    gencon = GenerationConfig()
    gencon.temperature = 0
    assert gencon.temperature == 0

def test_gen_config_temperature_two():
    gencon = GenerationConfig()
    gencon.temperature = 2
    assert gencon.temperature == 2

def test_gen_config_temperature_out_of_range():
    gencon = GenerationConfig()
    with pytest.raises(ValueError):
        gencon.temperature = 5

def test_gen_config_temperature_out_of_range_init():
    with pytest.raises(ValueError):
        GenerationConfig(temperature=5)

def test_gen_config_temperature_string():
    gencon = GenerationConfig()
    with pytest.raises(TypeError):
        gencon.temperature = "five"

def test_gen_config_temperature_bool():
    gencon = GenerationConfig()
    with pytest.raises(TypeError):
        gencon.temperature = True

def test_gen_config_max_tokens_negative():
    gencon = GenerationConfig()
    with pytest.raises(ValueError):
        gencon.max_tokens = -2

def test_gen_config_max_tokens_zero():
    gencon = GenerationConfig()
    with pytest.raises(ValueError):
        gencon.max_tokens = 0

def test_gen_config_max_tokens_float():
    gencon = GenerationConfig()
    with pytest.raises(TypeError):
        gencon.max_tokens = 2.5

def test_gen_config_max_tokens_bool():
    gencon = GenerationConfig()
    with pytest.raises(TypeError):
        gencon.max_tokens = True

def test_gen_config_max_tokens_string():
    gencon = GenerationConfig()
    with pytest.raises(TypeError):
        gencon.max_tokens = "two"

def test_gen_config_temp_set():
    gencon = GenerationConfig(temperature=1.5)
    with pytest.raises(ValueError):
        gencon.temperature = 5
    assert gencon.temperature == 1.5

def test_gen_config_max_tokens_set():
    gencon = GenerationConfig(max_tokens=512)
    with pytest.raises(ValueError):
        gencon.max_tokens = -5
    assert gencon.max_tokens == 512

def test_gen_config_max_temp():
    gencon = GenerationConfig()
    assert gencon.MAX_TEMPERATURE == 2.0

def test_gen_config_created_count():
    count = GenerationConfig.created_count
    gencon = GenerationConfig()
    gencon2 = GenerationConfig()
    assert GenerationConfig.created_count == count + 2

def test_gen_config_repr():
    gencon = GenerationConfig(temperature=0.7, max_tokens=256)
    assert repr(gencon) == 'GenerationConfig(temperature=0.7, max_tokens=256)'


def test_gen_config_eq():
    gencon = GenerationConfig(temperature=0.7, max_tokens=256)
    gencon2 = GenerationConfig(temperature=0.7, max_tokens=256)
    assert gencon == gencon2
    assert gencon != "Hello tests!"
    assert gencon != True
    assert GenerationConfig(temperature=0.7) != GenerationConfig(temperature=1.9)
    assert GenerationConfig(temperature=0, max_tokens=512) != GenerationConfig(temperature=0, max_tokens=513)
    

def test_gen_config_defaults():
    gencon = GenerationConfig()
    assert gencon.temperature == 1.0
    assert gencon.max_tokens == 256