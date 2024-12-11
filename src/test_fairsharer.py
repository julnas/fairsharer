import pytest
def test_fair_sharer():
  #check if the code breaks if the list is empty
  assert fair_sharer([], 1)
  #check what happens if the highest number is at the front
  assert fair_sharer([100, 70, 60, 80], 2)
  #check what happens if the highest number is at the back
  assert fair_sharer([70, 60, 80, 100], 2)
