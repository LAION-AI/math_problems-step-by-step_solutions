from sympy.functions.elementary.integers import ceiling
import basicmathsfunctions
import inspect
import itertools
import random
import argparse
import pandas as pd

# Get all global functions from the mathfunctions module
global_functions = [
    name
    for name, obj in inspect.getmembers(basicmathsfunctions)
    if inspect.isfunction(obj) and inspect.getmodule(obj) == basicmathsfunctions
]

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
    results_corrected=[]
    for e in results:
      e = e[:num_samples_per_function]
      results_corrected.append(e)
      #print(len(e))
    return results_corrected

def add_values_in_dictionary(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("num_samples_total", type=int, help="Total number of samples")
parser.add_argument("outputpath", help="Output path for the Parquet file")
args = parser.parse_args()
 
# Create a dictionary of function names and assign the desired number of samples to each function
functions = {}
num_samples_per_function = ceiling(args.num_samples_total / len(global_functions))
for function_name in global_functions:
    functions[function_name] = num_samples_per_function

# Get the list of results
result_list = execute_functions(functions, args.num_samples_total)

# Concatenate the lists in result_list
concatenated_list = list(itertools.chain(*result_list))
print(concatenated_list)


# Shuffle the concatenated list
shuffled_list = random.sample(concatenated_list, len(concatenated_list))

# Create a DataFrame from the shuffled list
df = pd.DataFrame({"problem+solution": shuffled_list, "index": range(len(shuffled_list))})


# Save the DataFrame as a Parquet file
df.to_parquet(args.outputpath,  row_group_size=1000)
print(df)
# Calculate and print the sum of results
result_sum = add_values_in_dictionary(functions)
print("Sum of all ordered math problems in the dict:", result_sum)
