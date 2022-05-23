# vayyar-assignment

A task in a job interview for Vayyar - the code counts the number of submarines in a matrix, that each submarine should be square and surrounded by water (i.e., there can be no submarine next to the submarine)

Two functions perform this, one slightly more efficient because when it find submarine so does not look at the nearby cell either - because in any case, he will not join the count, if there is a submarine there - then there is no reason because it is part of the same submarine. And if not - then it will certainly not join the count.

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
Ran 8 tests in 0.001s

OK
```
