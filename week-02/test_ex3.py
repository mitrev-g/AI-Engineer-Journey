from ex3_hash_maps import HashMap


# ---------- put / get ----------

def test_put_then_get():
    m = HashMap()
    m.put("dog", 9)
    assert m.get("dog") == 9

def test_get_missing_key():
    m = HashMap()
    assert m.get("cat") is None

def test_get_on_empty_map():
    assert HashMap().get("anything") is None

def test_put_updates_existing_key():
    m = HashMap()
    m.put("dog", 9)
    m.put("dog", 10)
    assert m.get("dog") == 10

def test_many_keys():
    m = HashMap()
    for i in range(100):
        m.put(f"key{i}", i)
    for i in range(100):
        assert m.get(f"key{i}") == i

def test_different_key_types():
    m = HashMap()
    m.put(1, "int")
    m.put("1", "str")
    m.put((1, 2), "tuple")
    assert m.get(1) == "int"
    assert m.get("1") == "str"          # 1 and "1" are different keys
    assert m.get((1, 2)) == "tuple"

def test_value_can_be_none():
    m = HashMap()
    m.put("x", None)
    assert m.get("x") is None
    assert "x" in m                     # stored, even though the value is None


# ---------- __len__ ----------

def test_len_empty():
    assert len(HashMap()) == 0

def test_len_counts_new_keys():
    m = HashMap()
    m.put("a", 1)
    m.put("b", 2)
    assert len(m) == 2

def test_len_unchanged_on_update():
    m = HashMap()
    m.put("a", 1)
    m.put("a", 2)
    assert len(m) == 1


# ---------- collisions ----------
# Small integers hash to themselves, so with 8 buckets,
# 1, 9 and 17 all land in bucket 1.

def test_colliding_keys_kept_separate():
    m = HashMap(capacity=8)
    m.put(1, "one")
    m.put(9, "nine")
    m.put(17, "seventeen")
    assert m.get(1) == "one"
    assert m.get(9) == "nine"
    assert m.get(17) == "seventeen"
    assert len(m) == 3

def test_update_inside_crowded_bucket():
    m = HashMap(capacity=8)
    m.put(1, "a")
    m.put(9, "b")
    m.put(9, "B")
    assert m.get(9) == "B"
    assert m.get(1) == "a"
    assert len(m) == 2


# ---------- remove ----------

def test_remove_existing():
    m = HashMap()
    m.put("a", 1)
    assert m.remove("a") is True
    assert m.get("a") is None
    assert len(m) == 0

def test_remove_missing():
    m = HashMap()
    m.put("a", 1)
    assert m.remove("zzz") is False
    assert len(m) == 1

def test_remove_on_empty():
    assert HashMap().remove("a") is False

def test_remove_one_of_colliding_keys():
    m = HashMap(capacity=8)
    m.put(1, "one")
    m.put(9, "nine")
    m.put(17, "seventeen")
    assert m.remove(9) is True
    assert m.get(1) == "one"            # neighbours in the bucket survive
    assert m.get(17) == "seventeen"
    assert m.get(9) is None
    assert len(m) == 2

def test_put_after_remove():
    m = HashMap()
    m.put("a", 1)
    m.remove("a")
    m.put("a", 2)
    assert m.get("a") == 2
    assert len(m) == 1


# ---------- __contains__ ----------

def test_contains():
    m = HashMap()
    m.put("a", 1)
    assert "a" in m
    assert "b" not in m

def test_contains_after_remove():
    m = HashMap()
    m.put("a", 1)
    m.remove("a")
    assert "a" not in m


# ---------- resizing (write this part last) ----------

def test_resize_grows_buckets():
    m = HashMap(capacity=8)
    for i in range(7):                  # 7 / 8 = 0.875 > 0.75
        m.put(i, i)
    assert len(m.buckets) > 8

def test_resize_keeps_all_data():
    m = HashMap(capacity=8)
    for i in range(1000):
        m.put(i, i * 10)
    assert len(m) == 1000
    for i in range(1000):
        assert m.get(i) == i * 10

def test_resize_keeps_buckets_short():
    m = HashMap(capacity=8)
    for i in range(1000):
        m.put(f"key{i}", i)
    longest = max(len(b) for b in m.buckets)
    assert longest < 10                 # resizing should prevent long chains

def test_get_missing_key_in_occupied_bucket():
    m = HashMap(capacity=8)
    m.put(1, "one")
    assert m.get(9) is None             # 9 shares bucket 1 with key 1

def test_remove_missing_key_in_occupied_bucket():
    m = HashMap(capacity=8)
    m.put(1, "one")
    assert m.remove(9) is False
    assert m.get(1) == "one"            # key 1 must survive