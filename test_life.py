import life

def test_life_grid():
    expected_value = [['-', '-', '-'],['*', '*', '*'],['-', '-', '-']]
    assert life.grid([[False, False, False],
                     [True, False, True],
                      [False, False, False]]) == expected_value
