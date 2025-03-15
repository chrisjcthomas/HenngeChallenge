# HenngeChallenge
This challenge is intended for backend position or global internship (full-stack) applicants.

# Mission 1: Write a program which fulfills the requirements below

## Description
This project involves writing a program to calculate the sum of squares of given integers, excluding any negatives. The program handles multiple test cases as specified in the input.

## Requirements
- The first line of the input is an integer \( n \) ( \( 1 < n \leq 100 \) ), indicating the number of test cases.
- Each test case consists of an integer \( X \) ( \( 0 < X \leq 100 \) ), followed by \( X \) space-separated integers \( Yn \) ( \( -100 < Yn \leq 100 \) ).
- For each test case, the program calculates the sum of squares of the integers, excluding negatives, and prints the result.

## Rules
- The solution must be written in either Go or Python.
- No global variables should be declared.
- Specific constraints apply based on the chosen language:
  - **Go**: No use of `for` or `goto` statements.
  - **Python**: No use of `for` loops, `while` loops, or comprehensions.

## Sample Input
*2
*4
3 -1 1 14
5
9 6 -53 32 16

## Sample Output.
206
1397
