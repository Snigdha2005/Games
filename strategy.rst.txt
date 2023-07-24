Strategy
--------

+ Take the row wise clues.
+ Based upon the sum of the clues given for that row, change the color of a block to black which  must certainly be black
+ Repeat the above two steps for column too
+ Check if all the rows and columns satisfy the conditions given
+ If not, add black blocks wherever necessary

Let B = BLACK BLOCK,  W = WHITE BLOCK

+---------------+-----------------+---------------+
| SUM OF CLUES  |  COMBINATIONS   |  ROW/ COLUMN  |
+===============+=================+===============+
| 5             |  5              | B B B B B     |
+---------------+-----------------+---------------+ 
| 4             |  4              | W B B B W     |
|               +-----------------+---------------+
|               |  3 1            | B B B W B     |
|               +-----------------+---------------+
|               |  1 3            | B W B B B     |
|               +-----------------+---------------+
|               |  2 2            | B B W B B     |
+---------------+-----------------+---------------+
| 3             |  3              | W W B W W     |
|               +-----------------+---------------+
|               |  2 1            | W B W W W     |
|               +-----------------+---------------+
|               |  1 2            | W W W B W     |
+---------------+-----------------+---------------+
