from sympy.functions.elementary.integers import ceiling
import basic_arithmetic_functions
import inspect

# Get all global functions from the mathfunctions module
global_functions = [
    name
    for name, obj in inspect.getmembers(mathfunctions)
    if inspect.isfunction(obj) and inspect.getmodule(obj) == mathfunctions
]


num_samples_total=10

def execute_functions(function_dict, n):
    import basic_arithmetic_functions
    
    for function_name in function_dict:
        function = getattr(basic_arithmetic_functions, function_name, None)
        
        if function and callable(function):
            try:
                result = function(function_dict[function_name])
                print(function_name, ": ", result)
            except Exception as e:
                print("Error:", function_name, "-", str(e))
        else:
            print("Invalid function:", function_name)

            
def add_values_in_dictionary(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total

# Beispielaufruf
functions = {}

# Print the list of function names
for function_name in global_functions:
    functions [function_name]= ceiling(num_samples_total /len(global_functions))
print(global_functions)
result = add_values_in_dictionary(functions)
print("Sum of all ordered math problems in the dict:", result)

execute_functions(functions, num_samples_total)
