from sympy.functions.elementary.integers import ceiling
import mathfunctions
import inspect

# Get all global functions from the mathfunctions module
global_functions = [
    name
    for name, obj in inspect.getmembers(mathfunctions)
    if inspect.isfunction(obj) and inspect.getmodule(obj) == mathfunctions
]

num_samples_total = 10

def execute_functions(function_dict, n):
    import mathfunctions
    
    results = []
    
    for function_name in function_dict:
        function = getattr(mathfunctions, function_name, None)
        
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

# Create a dictionary of function names and corresponding values
functions = {}
for function_name in global_functions:
    functions[function_name] = ceiling(num_samples_total / len(global_functions))

# Get the list of results
result_list = execute_functions(functions, num_samples_total)

# Print the list of results
print("List of results:")
for result in result_list:
    print(result)

# Calculate and print the sum of results
result_sum = add_values_in_dictionary(functions)
print("Sum of all ordered math problems in the dict:", result_sum)
