from ex7_lru_cache import LRUCache
import pytest


def test_walkthrough():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    cache.put("c", 3)
    assert cache.get("b") is None
    assert cache.get("a") == 1
    assert cache.get("c") == 3

def test_get_missing_key():
    cache = LRUCache(2)
    assert cache.get("x") is None
    cache.put("a", 10)
    assert cache.get("z") is None

def test_put_updates_existing_key():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("a", 99)
    assert cache.get("a") == 99
    assert len(cache) == 1

def test_put_update_refreshes_recency():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("a", 10)
    cache.put("c", 3)
    assert cache.get("b") is None
    assert cache.get("a") == 10
    assert cache.get("c") == 3

def test_get_refreshes_recency():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.get("a")
    cache.put("c", 3)
    assert cache.get("a") == 1
    assert cache.get("b") is None

def test_capacity_one():
    cache = LRUCache(1)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") is None
    assert cache.get("b") == 2
    assert len(cache) == 1

def test_len():
    cache = LRUCache(3)
    assert len(cache) == 0
    cache.put("a", 1)
    assert len(cache) == 1
    cache.put("b", 2)
    assert len(cache) == 2
    cache.put("c", 10)
    assert len(cache) == 3
    cache.put("d", 11)
    assert len(cache) == 3

def test_invalid_capacity():
    with pytest.raises(ValueError):
        LRUCache(0)
    with pytest.raises(ValueError):
        LRUCache(-1)