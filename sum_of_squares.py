import sys
from functools import reduce

def calculate_sum_of_squares(numbers_str):
    """Calculate sum of squares of non-negative integers from a space-separated string"""
    numbers = list(map(int, numbers_str.split()))
    # Filter out negatives and square each number
    positive_squares = map(lambda x: x**2, filter(lambda x: x >= 0, numbers))
    # Sum the squares
    return reduce(lambda acc, x: acc + x, positive_squares, 0)

def read_and_process_all():
    """Read all input and process test cases"""
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    
    lines_iter = iter(lines)
    
    # Read number of test cases
    try:
        n = int(next(lines_iter).strip())
    except StopIteration:
        return []  # Return an empty list if no input is available
    
    # Process each test case
    results = []
    
    def process_remaining_cases(count, results_list):
        """Recursively process remaining test cases"""
        if count <= 0:
            return results_list
        
        try:
            x = int(next(lines_iter).strip())  # Read x, but it's not used in the calculation
            numbers_str = next(lines_iter).strip()  # Read the numbers string
            result = calculate_sum_of_squares(numbers_str)
            return process_remaining_cases(count - 1, results_list + [result])
        except StopIteration:
            return results_list  # Return whatever results were accumulated

    return process_remaining_cases(n, results)  # Ensure it starts with an empty list

def main():
    """Main function to read input and print results"""
    results = read_and_process_all()
    if results:
        print("\n".join(map(str, results)))
    else:
        print("No results to display.")

if __name__ == "__main__":
    main()
