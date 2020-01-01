import life

def test_life_grid_2_true():
    expected_value = [[False, False, False],[True, False, True],[False, False, False]]
    assert life.grid_view(3,3,[3,5]) == expected_value

def test_life_grid_3rows_4cols():
    expected_value = [[False, True, False,True],[ False, True,False, False],[ False,False, False, False]]
    assert life.grid_view(3,4,[1,3,5]) == expected_value

def test_life_grid_3rows_4cols_repeat_input():
    expected_value = [[False, True, False,True],[ False, True,False, False],[ False,False, False, False]]
    assert life.grid_view(3,4,[1,3,5,1]) == expected_value


def test_neighbours_0():
    expected_value = 0
    assert life.neighbours( [[ True, False,True],[ False,False, False],[ False,False, True, False]]) == expected_value
