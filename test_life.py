import life

def test_life_grid():
    expected_value = [['-', '-', '-'],['*', '*', '*'],['-', '-', '-']]
    assert life.grid_view([[False, False, False],
                     [True, False, True],
                      [False, False, False]]) == expected_value
