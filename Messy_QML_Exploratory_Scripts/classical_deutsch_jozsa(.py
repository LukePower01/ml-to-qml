def classical_deutsch_jozsa(f):
    n = len(bin(max(int(f(0)), int(f(1)))) - 2)  # Explicitly convert to integers

    # Check if the function is constant or balanced
    constant_value = int(f(0))
    for i in range(1, 2**n):
        if int(f(i)) != constant_value:
            return "Balanced"
    
    return "Constant"

# Example usage:
# Define a function that is either constant or balanced
def example_function(x):
    return int(1)  # You can change this value to make the function constant or balanced

result = classical_deutsch_jozsa(example_function)
print(f"The function is {result}.")
