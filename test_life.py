import life

def test_life_grid_2_true():
    expected_value = [['-', '-', '-'],['*', '-', '*'],['-', '-', '-']]
    assert life.grid_view(3,3,[3,5]) == expected_value

def test_life_grid_3rows_4cols():
    expected_value = [['-', '*', '-','*'],[ '-', '*','-', '-'],[ '-','-', '-', '-']]
    assert life.grid_view(3,4,[1,3,5]) == expected_value

