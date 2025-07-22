from authz import id

def test_authz_false():
    assert id("fake_id") == False