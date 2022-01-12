from code_challenges.hash_table.hashtable import Hashtable

def test_import():
    assert Hashtable

def test_hash():
    hash = Hashtable()
    assert hash.hash('cat') == 760

def test_hash2():
    hash = Hashtable(1200)
    assert hash.hash('cat') == 552

def test_add():
    hash = Hashtable()
    hash.add('cat', 2)
    assert hash.buckets[760] == [('cat', 2)]

def test_add_collision():
    hash = Hashtable()
    hash.add('cat', 2)
    hash.add('cta', 3)
    assert hash.buckets[760] == [('cat', 2), ('cta', 3)]

def test_get():
    hash = Hashtable()
    hash.add('cat', 2)
    hash.add('cta', 3)
    assert hash.get('cat') == 2
    assert hash.get('cta') == 3

def test_get_collision():
    hash = Hashtable()
    hash.add('cat', 2)
    assert hash.get('cat') == 2

def test_get_null():
    hash = Hashtable()
    hash.add('cat', 2)
    assert hash.get('rat') is None

def test_contains_true():
    hash = Hashtable()
    hash.add('cat', 2)
    assert hash.contains('cat') == True

def test_contains_false():
    hash = Hashtable()
    hash.add('cat', 2)
    assert hash.contains('rat') == False
