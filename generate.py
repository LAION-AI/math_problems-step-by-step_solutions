from mathfunctions import *

num_samples_total=10

def execute_functions(function_dict, n):
    for function_name in function_dict:
        function = globals().get(function_name)
        if function and callable(function):
            n= function_dict[function_name]
            result = function(n)
            print(function_name,":                                  ", result)
def add_values_in_dictionary(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total

# Beispielaufruf
functions = { "generate_addition_problems":int(0.1 * num_samples_total), "generate_addition_problems2":int(0.1 * num_samples_total), "generate_subtraction_problems":int(0.1 * num_samples_total), "generate_subtraction_problems2":int(0.1 * num_samples_total), "generate_power_problems":int(0.1 * num_samples_total), "generate_division_problems":int(0.1 * num_samples_total), "generate_addition_with_3_numbers_problems":int(0.1 * num_samples_total), "generate_addition_subtraction_with_3_numbers_problems":int(0.1 * num_samples_total), "generate_addition_subtraction_with_3_numbers_problems":int(0.1 * num_samples_total), "generate_subtraction_subtraction_with_3_numbers_problems":int(0.1 * num_samples_total), "generate_multiplication_division_with_3_numbers_problems":int(0.1 * num_samples_total), "generate_addition_division_with_3_numbers_problems":int(0.1 * num_samples_total), "generate_addition_multiplication_with_3_numbers_problems":int(0.1 * num_samples_total), "generate_addition_with_5_numbers_problems":int(0.1 * num_samples_total), "generate_exponential_with_2_numbers_problems":int(0.1 * num_samples_total), "generate_random_math_problems":int(0.1 * num_samples_total), "generate_hypothenuse_with_pythagoras":int(0.1 * num_samples_total), "generate_missing_side_with_pythagoras":int(0.1 * num_samples_total), "addition_step_by_step2":int(0.1 * num_samples_total), "addition_step_by_step1":int(0.1 * num_samples_total), "substraction_step_by_step1":int(0.1 * num_samples_total), "substraction_step_by_step2":int(0.1 * num_samples_total), "multiplication_step_by_step":int(0.1 * num_samples_total), "multiplication_step_by_step_short1":int(0.1 * num_samples_total), "multiplication_step_by_step_short2":int(0.1 * num_samples_total), "division_step_by_step1":int(0.1 * num_samples_total), "division_step_by_step2":int(0.1 * num_samples_total), "division_step_by_step3":int(0.1 * num_samples_total), "generate_fraction_problems":int(0.1 * num_samples_total), "generate_fraction_problems2":int(0.1 * num_samples_total), "generate_fraction_problems3":int(0.1 * num_samples_total), "generate_fraction_problems4":int(0.1 * num_samples_total) }
result = add_values_in_dictionary(functions)
print("Sum of all ordered math problems in the dict:", result)

execute_functions(functions, num_samples_total)
