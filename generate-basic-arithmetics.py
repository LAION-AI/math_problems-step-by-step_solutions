from sympy.functions.elementary.integers import ceiling
import basicmathsfunctions
import inspect
import itertools
import random


# Get all global functions from the mathfunctions module
global_functions = [
    name
    for name, obj in inspect.getmembers(basicmathsfunctions)
    if inspect.isfunction(obj) and inspect.getmodule(obj) == basicmathsfunctions
]
 
num_samples_total = 100

def execute_functions(function_dict, n):
    import basicmathsfunctions
    
    results = []
    
    for function_name in function_dict:
        function = getattr(basicmathsfunctions, function_name, None)
        
        if function and callable(function):
            try:
                result = function(function_dict[function_name])
                results.append(result)
            except Exception as e:
                print("Error:", function_name, "-", str(e))
        else:
            print("Invalid function:", function_name)
    
    return results

def add_values_in_dictionary(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total

# Create a dictionary of function names and assign the desired number of samples to each function
functions = {}
num_samples_per_function = ceiling(num_samples_total / len(global_functions))
for function_name in global_functions:
    #print(num_samples_per_function)
    functions[function_name] = num_samples_per_function

# Get the list of results
result_list = execute_functions(functions, num_samples_total)

concatenated_list = list(itertools.chain(*result_list))

# Shuffle the concatenated list
random.shuffle(concatenated_list)

# Print the shuffled list
print("Shuffled list:")
for item in concatenated_list:
    print(item)


# Calculate and print the sum of results
result_sum = add_values_in_dictionary(functions)
print("Sum of all ordered math problems in the dict:", result_sum)