# vayyar-assignment

A task in a job interview for Vayyar - the code counts the number of submarines in a matrix, that each submarine should be square and surrounded by water (i.e., there can be no submarine next to the submarine)

Three functions perform this:
1. Performs this in a simple way - goes through all the cells and checks if there is a new submarine in the cell.
2. slightly more efficient because when it find submarine so does not look at the nearby cell either - because in any case, he will not join the count, if there is a submarine there - then there is no reason because it is part of the same submarine. And if not - then it will certainly not join the count.
3. More efficient especially in cases of wide submarines spreading over several rows - in each crossing of a row it keeps the starting point of each submarine and its end point, and then in the next crossing - the function can skip the places in the row above which there was a submarine.

The program also has tests that check that the code is correct.

# installation and use
download the code:
```cmd
git clone https://github.com/egoldshm/vayyar-assignment
cd vayyar-assignment
```

run the tests:
```cmd
python Test_Submarine.py
```

Output should be:
```python
........
----------------------------------------------------------------------
Ran 12 tests in 0.003s

OK
```
