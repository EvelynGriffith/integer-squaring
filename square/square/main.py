"""Perform integer squaring with different approaches."""

# import the Callable class for type annotations from the typing module
from typing import Callable

# import the List class for type annotations from the typing module
from typing import List

from enum import Enum

# import the path class from the pathlib website
from pathlib import Path

# import typer module
import typer

from rich.console import Console

# create a Typer object to support the command-line interface
cli = typer.Typer()


class IntegerSquareApproach(str, Enum):
    """Define the name for the approach to squaring a number."""

    for_loop = "for"
    while_loop = "while"


def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # determine if the file is not None and if it is a file
    if file is not None:
        # the file is valid
        if file.is_file():
            return True
    # the file was either none or not valid
    return False


def compute_square_while(value: int) -> int:
    """Compute the square of a number through iteration with a while loop."""
    # initialize the number of iterations and the answer
    num_iterations = 0
    answer = 0
    # repeatedly increase the answer until getting to the value
    while num_iterations < abs(value):
        answer = answer + abs(value)
        num_iterations = num_iterations + 1
    # return the computed integer square
    return answer


def compute_square_for(value: int) -> int:
    """Compute the square of a number through iteration with a for loop."""
    # initialize the answer to zero
    answer = 0
    # repeatedly add to the answer the absolute value of the variable called value
    for _ in range(abs(value)):
        answer = answer + abs(value)
    # return the computed integer square
    return answer


def compute_square_iterative(
    contents: str, square_function: Callable[[int], int]
) -> List[int]:
    """Compute the square of all of the integer values inside of the contents."""
    # create an empty list for the squared values
    squared_values = []
    # iterate through all of the items in the contents
    for x in contents.split("\n"):
        # --> convert the line into a number
        if x != "":
            squared_values.append(square_function(int(x)))
    # -->  perform the number squaring computation with square_function
    # --> add the squared_number to the square_list
    # return the list of the squared numbers
    return squared_values


@cli.command()
def square(
    approach: IntegerSquareApproach = IntegerSquareApproach.for_loop,
    dir: Path = typer.Option(None),
    file: Path = typer.Option(None),
) -> None:
    """Iterate square all integers in a file."""
    # create a console for rich text output
    console = Console()
    # add extra space after the command to run the program
    console.print()
    # create the full name of the file
    file_fully_qualified = dir / file
    # display a message to explain the file that will be input
    console.print(f":smiley: Squaring numbers in a file called {file_fully_qualified}!")
    console.print()
    # the file is value and so the program should search through it for the word
    if confirm_valid_file(file_fully_qualified):
        # read in the contents of the file
        contents_text = file_fully_qualified.read_text()
        square_list = []
        # the for loop approach should be invoked
        if approach.value == IntegerSquareApproach.for_loop:
            # create the square function to be compute_square_for
            square_function = compute_square_for
            # call the compute_square_iterative function with:
            # --> the contents_text variable with the numerical values as text
            # --> the square function that is set to be compute_square_for
            square_list = compute_square_iterative(contents_text, square_function)
        # the while loop approach should be invoked
        elif approach.value == IntegerSquareApproach.while_loop:
            # create the square function to be compute_square_while
            # call the compute_square_iterative function with:
            # --> the contents_text variable with the numerical values as text
            # --> the square function that is set to be compute_square_while
            square_function = compute_square_while
            square_list = compute_square_iterative(contents_text, square_function)
        # display the list of squared values
        console.print(square_list)
    # the file was no valid and thus you cannot perform the number squaring
    else:
        console.print(
            f":person_shrugging: {file_fully_qualified} was not a valid file! Sorry, cannot square the numbers!"
        )
        console.print()
