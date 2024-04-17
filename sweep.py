# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invlaid) 
def validate( block_data ):
  bomb_count = 0
  # Check whether the centre block is a bomb, a number, or an invalid input
  # Skip bombs, send an error on invalid input, verify numbers
  for i in range (3):
    for j in range (3):
      if block_data [i][j] == -1:
        bomb_count = bomb_count + 1
  if block_data [1][1] == -1:
    return "This block is a bomb."
  if block_data [1][1] == bomb_count:
    if block_data [1][1] == 1:
      return 'Valid. There is '+ str(bomb_count)+' bomb around this block.'
    if block_data [1][1] != 1:
      return 'Valid. There are '+ str(bomb_count)+' bombs around this block.'
  if block_data [1][1] != bomb_count:
    return 'Invalid. There are '+ str(bomb_count)+' bombs around this block.'


grid = [
  [-1,1,0],
  [-1,2,0],
  [0,0,0]
]
print (validate(grid))
