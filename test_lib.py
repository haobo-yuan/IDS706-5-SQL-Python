import lib

def test_my_load():
    # Load data
    lib.my_load(nrows=3)
    # Check if data was loaded
    results = lib.my_read(name='AAPL')
    assert len(results) > 0
    print("test_my_load passed.")

def test_my_create():
    # Insert a new record
    lib.my_create(record=('2021-10-01', 100, 110, 90, 105, 1000000, 'Test Stock'))
    # Check if the record was inserted
    results = lib.my_read(name='Test Stock')
    assert len(results) == 1
    print("test_my_create passed.")

def test_my_read():
    # Read the record
    results = lib.my_read(name='Test Stock')
    assert len(results) == 1
    print("test_my_read passed.")

def test_my_update():
    # Update the record
    lib.my_update(name='Test Stock', new_close=200)
    # Check if the record was updated
    results = lib.my_read(name='Test Stock')
    assert results[0][4] == 200  # 'Close' is at index 4
    print("test_my_update passed.")

def test_my_delete():
    # Delete the record
    lib.my_delete(name='Test Stock')
    # Check if the record was deleted
    results = lib.my_read(name='Test Stock')
    assert len(results) == 0
    print("test_my_delete passed.")

if __name__ == "__main__":
    test_my_load()
    test_my_create()
    test_my_read()
    test_my_update()
    test_my_delete()
    print("All tests passed.")
