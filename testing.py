from numpy import *

board = array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])
m = matrix(board)



mboard = matrix('1 1 1; 0 1 0; 1 1 0')

print(mboard)

print("Sum axis 1")
print(mboard.sum(axis=1))

print("Sum axis 2")
print(mboard.sum(axis=0))


print("Mboard")
print(mboard)


# Check rows
for row in mboard:
    row_sum = sum(row)
    if row_sum == 3 or row_sum == -3:
        print("Row sum:", row_sum)
        break

# Check columns
for col in mboard.T:
    col_sum = sum(col)
    if col_sum == 3 or col_sum == -3:
        print("Column sum:", col_sum)
        break

# Check diagonals
diag_sum_1 = trace(mboard)
diag_sum_2 = trace(fliplr(mboard))
if diag_sum_1 == 3 or diag_sum_1 == -3:
    print("Diagonal 1 sum:", diag_sum_1)
if diag_sum_2 == 3 or diag_sum_2 == -3:
    print("Diagonal 2 sum:", diag_sum_2)