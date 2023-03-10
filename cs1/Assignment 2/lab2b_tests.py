# lab2b_tests.py
# Updated for Fall 2013

from lab2b import *

def test_make_random_code():
    for i in range(100):
        code = make_random_code()
        assert len(code) == 4
        for char in code:
            assert char in 'RGBYOW'

def make_random_codes(n):
    codes = []
    for _ in range(n):
        # We assume that make_random_code() works.
        codes.append(make_random_code())
    return codes

def test_count_exact_matches():
    # Check basic invariants.
    codes1 = make_random_codes(1000)
    codes2 = make_random_codes(1000)
    for (c1, c2) in zip(codes1, codes2):
        assert 0 <= count_exact_matches(c1, c2) <= 4

    # Check specific answers.
    assert count_exact_matches('RGBY', 'RGBY') == 4
    assert count_exact_matches('RGBY', 'GBYR') == 0
    assert count_exact_matches('RGBY', 'RGOO') == 2
    assert count_exact_matches('RGBY', 'RWBW') == 2
    assert count_exact_matches('RGBY', 'WOWO') == 0 
 

def test_count_letter_matches():
    # Check basic invariants.
    codes1 = make_random_codes(1000)
    codes2 = make_random_codes(1000)
    for (c1, c2) in zip(codes1, codes2):
        assert 0 <= count_letter_matches(c1, c2) <= 4

    # Check specific answers.
    assert count_exact_matches('RGBY', 'RGBY') == 4
    assert count_letter_matches('RGBY', 'RGBY') == 4
    assert count_letter_matches('RGBY', 'GBYR') == 4
    assert count_letter_matches('RGBY', 'OROG') == 2
    assert count_letter_matches('RGBY', 'BWBR') == 2
    assert count_letter_matches('RGBY', 'WOWO') == 0 

def test_compare_codes():
    # Check basic invariants.
    codes1 = make_random_codes(1000)
    codes2 = make_random_codes(1000)
    for (c1, c2) in zip(codes1, codes2):
        comp = compare_codes(c1, c2)
        assert len(comp) == 4
        for char in comp:
            assert char in 'bw-'

    # Check specific answers.
    assert compare_codes('RGBY', 'RGBY') == 'bbbb'
    assert compare_codes('RGBY', 'GBYR') == 'wwww'
    assert compare_codes('RGBY', 'OROG') == 'ww--'
    assert compare_codes('RGBY', 'BWBR') == 'bw--'
    assert compare_codes('RGBY', 'WOWO') == '----'

if __name__ == '__main__':
    try:
        test_make_random_code()
        print("Test test_make_random_code succeeded.")
    except Exception as e:
        print("Test test_make_random_code failed.\n\t%s" % e)
    try:
        test_count_exact_matches()
        print("Test test_count_exact_matches succeeded.")
    except Exception as e:
        print("Test test_count_exact_matches failed.\n\t%s" % e)
    try:
        test_count_letter_matches()
        print("Test test_count_letter_matches succeeded.")
    except Exception as e:
        print("Test test_count_letter_matches failed.\n\t%s" % e)
    try:
        test_compare_codes()
        print("Test test_compare_codes succeeded.")
    except Exception as e:
        print("Test test_compare_codes failed.\n\t%s" % e)
