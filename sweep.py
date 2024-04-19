# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invlaid) 
try:
  def validate( block_data ):
    bomb_count = 0
    result = ""
    while (1):
    # Check whether the centre block is a bomb, a number, or an invalid input
    # Skip bombs, send an error on invalid input, verify numbers
      if block_data [1][1] == -1:
          result = "This block is a bomb."
          break
      for i in range (3):
        for j in range (3):
          if block_data [i][j] == -1:
            bomb_count = bomb_count + 1
      if block_data [1][1] == bomb_count:
        if bomb_count == 1:
          result = 'Valid. There is ' + str(bomb_count) + ' bomb around this block. The number in this block is ' + str(block_data[1][1]) + '. The number in the block is equal to the number of surrounding bombs.'
          break
        if bomb_count != 1:
          result = 'Valid. There are '+ str(bomb_count)+' bombs around this block. The number in this block is ' + str(block_data[1][1]) + '. The number in the block is equal to the number of surrounding bombs.'
          break
      if block_data [1][1] != bomb_count:
        if bomb_count == 1:
          result = 'Invalid. There is '+ str(bomb_count)+' bomb around this block. The number in this block is ' + str(block_data[1][1]) + '. The number in the block is not equal to the number of surrounding bombs.'
          break
        if bomb_count != 1:
          result = 'Invalid. There are '+ str(bomb_count)+' bombs around this block. The number in this block is ' + str(block_data[1][1]) + '. The number in the block is not equal to the number of surrounding bombs.'
          break
    return result

  grid = [
    [0,1,-1],
    [1,2,1],
    [-1,1,0]
  ]
    
  print (validate(grid))

except:
  print ("Error!")
  print ("The value in this block, or in any surrounding blocks is not a number. Please fill the grid with only numbers.")
