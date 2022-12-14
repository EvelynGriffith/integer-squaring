# Integer Squaring

## Evelyn Griffith

## Program Output

### What is the output from running the following commands?

- `poetry run square --approach while --dir input --file numbers.txt`

```

😃 Squaring numbers in a file called input\numbers.txt!

[
    5184,
    841,
    3721,
    1764,
    1936,
    3136,
    36,
    1764,
    7225,
    4624,
    256,
    2401,
    3025,
    2704,
    1764,
    1764,
    7396,
    3600,
    4900,
    2916,
    256,
    729,
    2025,
    2809,
    576,
    576,
    2916,
    9216,
    841,
    1296,
    4624,
    576,
    1849,
    7569,
    1444,
    3025,
    1369,
    3025,
    2601,
    4,
    7569,
    5929,
    4761,
    1089,
    196,
    169,
    900,
    8281,
    1681,
    2209
]
```


- `poetry run square --approach for --dir input --file numbers.txt`

```😃 Squaring numbers in a file called input\numbers.txt!

[
    5184,
    841,
    3721,
    1764,
    1936,
    3136,
    36,
    1764,
    7225,
    4624,
    256,
    2401,
    3025,
    2704,
    1764,
    1764,
    7396,
    3600,
    4900,
    2916,
    256,
    729,
    2025,
    2809,
    576,
    576,
    2916,
    9216,
    841,
    1296,
    4624,
    576,
    1849,
    7569,
    1444,
    3025,
    1369,
    3025,
    2601,
    4,
    7569,
    5929,
    4761,
    1089,
    196,
    169,
    900,
    8281,
    1681,
    2209
]
```

### Use an Itemized List to Provide the First Three Squared Integers in the Output Lists

<ul>
    <li>5184</li>
    <li>841</li>
    <li>3721</li>
</ul>

## Source Code and Configuration Files

### Describe in detail how the completed source code works

#### A function that confirms that a file containing data is valid

```
def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # determine if the file is not None and if it is a file
    if file is not None:
        # the file is valid
        if file.is_file():
            return True
    # the file was either none or not valid
    return False
```

Essentially what this is saying is that the function called "confirm_valid_file" is going to determine if the file has numbers in it, that the file exists, and it will also say if the file is a valid path, meaning a valid directory. It will do this using an if statement. By saying "if the file is not none" it is saying that if the file has things in it it will return the word "True", but if the file either doesnt exist or has nothing in it it will return "False".

#### A function that squares an integer using a `for` loop

```
def compute_square_for(value: int) -> int:
    """Compute the square of a number through iteration with a for loop."""
    # initialize the answer to zero
    answer = 0
    # repeatedly add to the answer the absolute value of the variable called value
    for _ in range(abs(value)):
        answer = answer + abs(value)
    # return the computed integer square
    return answer
```

This is a function called compute_for_square that uses a for loop to iterate through the list of integers within the numbers.txt file. First it will take the string of numbers and turn them into individual integers. Then it will square them by first taking the absolute value of that number, it does so by using the "for _ in range(abs(value))", and then using the answer variable in "answer = 0" it will add the absolute value of the integer to the answer variable giving the output of a squared integer.

#### A function that uses a `while` loop to square an integer value

```
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
```

This is saying that first the string will be converted into integers so that each number becomes a singular integer. Then is will iterate through the file called numbers.txt. Notice though, that this has a new variable called num_iterations = 0 this is set there because the while loop functions on the condition that if there are still more numbers to go through then continue through the file. So every time it iterates through the loop it will at 1 to the num_iterations variable. That is done through this line of code "num_iterations = num_iterations + 1". Then there is also the answer variable which will in the beginning also be set to zero. This is similar to the for loop in a sense that when the loop collects the integer it will add the absolute value of the integer to answer which equals 0. Then it will return answer which is the squared value of the integer.

#### An enumeration class that defines the options for squaring an integer

```
class IntegerSquareApproach(str, Enum):
    """Define the name for the approach to squaring a number."""

    for_loop = "for"
    while_loop = "while"
```

This is basically telling the computer to go into a class called enum and import Enum from that class. then it is telling you that it will give two options for squaring an integer either a for loop or a while loop. This means that it defines the for loop as "for" and the while loop as "while" so that when you call upon it it will create those specific loops.

#### An example of a higher-order function that accepts a function as input

```
def compute_square_iterative(
    contents: str, square_function: Callable[[int], int]
) -> List[int]:
    """Compute the square of all of the integer values inside of the contents."""
    squared_values = []
    for x in contents.split("\n"):
        if x != '':
            squared_values.append(square_function(int(x)))
    return squared_values
```

This function is a bit more complicated. It is called compute_square_iterative and this function is going to call on antoher function in order to square the values and print them as a list. In the first line of code, it is defining the function and telling it to take the string of integers in the numbers.txt file and turn them into a list of integers. The list will then be called squared_values. From there the function will iterate into a for loop that says for the integer, in this case x, in contents we will split them and create a single integer. Then if x has a value (does not equal nothing) we will append (or bring back) the squared value from the square_function callable list and print that squared value.

### What is the purpose of the `pyproject.toml` file?

This file is going to set parameters for what the program needs in order to run correctly. It will also connect the user to the poetry package and give them information on what the package settings are. Not only that, but it also sets the package linting tools in order and allows the running of those files so that the program can be properly checked. It will also create a virtual environment for that code to live in and allow for the dependencies that it installs to set further parameters that can improve the virtual environment for the code and allow for further development of said code.

### What is the purpose of the `poetry.lock` file?

This is something like the .toml file but it categorizes dependencies and prevents you from automatically getting the latest versions of your dependencies. It also allows people to all have the same versions of things so that if there is collaboration on the project no one is going to have different versions. It will also prevent updates so that you cant have problems working on a specific project due to a unwanted update. It also creates co-dependencies and allows all of the different dependencies to work together.

### What are three different ways in which you can run the `square` program?

The first way is to cd into the square directory and run this code `poetry run square --approach for --dir input --file numbers.txt` which will iterate you through a for loop.

The second way is to cd into the square directory and run this code `poetry run square --approach while --dir input --file numbers.txt` which will iterate through a while loop but ultimately show the same answer.

The final way is to cd into the square directory and run this code :
`poetry install`
`poetry shell`
`square --approach while --dir input --file numbers.txt`

### What was the greatest challenge that you faced when completing this assignment?

I think that the biggest challenge I faced when trying to work through this lab was working on the third function which calls on another function. When working on that I struggled to figure out how to split the string into singular integers and then call on them as well to square that integer. I also really struggled with how to make the function call the absolute value of the function because that was actually centered around the original function that it's calling on rather than the function itself.

### Based on your experiences with this project, what is one way in which you want to improve?

I really want to improve my knowledge of source code and the commands I can use to make things much more efficient. I also want to better understand the why behind things so that I can follow logical courses of action in order to solve problems. 
