# Video alternative: ...

from lib.helpers import check_that_these_are_equal

# Remember `if`s? Here's a reminder:

my_name = "Kay"
if my_name == "Kay":
    print("Hello, Kay!")
else:
    print("Hello!")

# The `if` is part of a category of programming tools known
# as 'control flow'. These are tools that control the flow
# of execution in a program. The `if` controls which lines
# get executed.

# There's another kind of control flow: the loop. It comes
# in two varieties: `for` and `while` loops.

# A while loop is perhaps the most simple:

i = 0
while i < 10:
    print(f"The number is now {i}")
    i = i + 1

# @TASK: run this program and see what it does.

# The `while` loop is like an `if`, in that it takes an
# expression that evaluates to True or False, and then
# executes its block of code if the condition is True.

# However, the `while` loop is different in that it
# repeats for as long as the condition is True.

# @TASK: Here's an exercise where you can put it into
# practice:

print("")
print("Function: add_cats_repeatedly")

def add_cats_repeatedly(word_list, count):
    # ...
    return word_list

check_that_these_are_equal(
    add_cats_repeatedly([], 3), ['cats', 'cats', 'cats'])
check_that_these_are_equal(
    add_cats_repeatedly(['dogs'], 2), ['dogs', 'cats', 'cats'])

# When you're done, move on to 033_for_loops.py
