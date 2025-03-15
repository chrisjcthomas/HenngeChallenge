<h1 align="center">HenngeChallenge</h1>
<p align="center">This challenge is intended for backend position or global internship (full-stack) applicants.</p>

# Mission 1: Write a program which fulfills the requirements below

## Description
This project involves writing a program to calculate the sum of squares of given integers, excluding any negatives. The program handles multiple test cases as specified in the input.

## Requirements
- We want you to calculate the sum of squares of given integers, excluding any negatives.
- The first line of the input will be an integer `N` (`1 <= N <= 100`), indicating the number of test cases to follow.
- Each of the test cases will consist of a line with an integer `X` (`0 < X <= 100`), followed by another line consisting of `X` number of space-separated integers `Yn` (`-100 <= Yn <= 100`).
- For each test case, calculate the sum of squares of the integers, excluding any negatives, and print the calculated sum in the output.
- **Note**: There should be no output until all the input has been received.
- **Note 2**: Do not put blank lines between test cases solutions.
- **Note 3**: Take input from standard input, and output to standard output.

## Rules
- The solution must be written in either Go or Python.
- No global variables should be declared.
- Specific constraints apply based on the chosen language:
  
  - **Go**: Your source code must be a single file
  - No use of `for` or `goto` statements.
  - Your solution will be tested against Go 1.24 (as of March 2025) or higher
    ```
    package main

    func main() {
       ...
    }
    ```
    
  - **Python**: Your source code must be a single file, containing at least a main function
  - No use of `for` loops, `while` loops, or comprehensions.
  - Your solution will be tested against Python 3.13 (as of January 2025) or higher
    ```
    def main():
        ...
  

    if __name__ == "__main__":
        main()
    ```
## Sample Input
```
2
4
3 -1 1 14
5
9 6 -53 32 16
```
## Sample Output
```
206
1397
```
<br>
<br>

# Mission 2: Publish your source code as a secret gist

## Description
Publish your source code as a secret gist. You will need a GitHub account to create a secret gist, if you are not familiar with secret gists, follow the instructions here.

Please make sure not to publish it as a public gist.

We will take a look at your source code later, after you achieve Mission 3.

Your program will be auto-tested, so please be strict about the input/output specification. For failed solution, we will still assess it case-by-case but it will cause points reduction to your overall score.

**Note**: Make sure to upload only a single file as your solution and no additional files should exist in your provided gist.
<br>
<br>

# Mission 3: Send us the URL of your work

## Description
First, construct a JSON string like below:
