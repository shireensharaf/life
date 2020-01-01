import life


def test_life_grid_input():
    expected_value = [[False, True, False,True],[ False, True,False, False],[ False,False, False, False],[False, False, False,False]]
    assert life.grid_view([1,3,5]) == expected_value

def test_life_grid_repeat_input():
    expected_value = [[False, True, False,True],[ False, True,False, False],[ False,False, False, False],[False, False, False,False]]
    assert life.grid_view([1,3,5,1]) == expected_value


def test_position_of_true(): 
    assert life.position_true( [[ True, False,True, False],
                                [ False,False, False, False],
                                [ False, True, False, False],
                                [False, False, False,False]]) == [[0,0],[0,2],[2,1]]


def test_no_neighbour():
    assert life.neighbours( [[ True, False,True, False],
                                [ False,False, False, False],
                                [ False, True, False, False],
                                [False, False, False,False]], [[0,0],[0,2],[2,1]]) == 0
