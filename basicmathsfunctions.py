import random, math

def generate_addition_problems(n_samples):
    problems_and_solutions = []
    for _ in range(n_samples):
        a = random.randint(-10000, 10000)
        b = random.randint(-10000, 10000)
        result = a + b
        problem = f"{a} + {b} = ?"
        solution = f"{a} + {b} = {result}"
        problems_and_solutions.append(problem + "\n" + solution)
    return problems_and_solutions


def generate_addition_problems2(number_of_samples):
    results_addition = []
    for i in range(number_of_samples):
        for j in range(number_of_samples):
            a = i - 100
            b = j - 100

            result = a + b
            part1 = str(a) + " + " + str(b) + " = "
            part2 = str(result)
            results_addition.append(part1 + "\n" + part2)

    return results_addition

def generate_subtraction_problems(n_samples):
    problems_and_solutions = []
    for _ in range(n_samples):
        a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        result = a - b
        problem = f"{a} - {b} = ?"
        solution = f"{a} - {b} = {result}"
        problems_and_solutions.append(problem + "\n" + solution)
    return problems_and_solutions

def generate_subtraction_problems2(number_of_samples):
    results_subtraction = []
    for i in range(number_of_samples):
        for j in range(number_of_samples):
            a = i - 100
            b = j - 100

            result = a - b
            part1 = str(a) + " - " + str(b) + " = "
            part2 = str(result)
            results_subtraction.append(part1 + "\n" + part2)

    return results_subtraction


def generate_power_problems(number_of_samples):
    results_power = []
    for i in range(number_of_samples):
        for j in range(number_of_samples):
            a = i - 30
            b = j - 30

            result = a ** b
            part1 = str(a) + " ^ " + str(b) + " = "
            part2 = str(result)
            results_power.append(part1 + "\n" + part2)

    return results_power

def generate_multiplication_problems(number_of_samples):
    results_multiplication = []
    for i in range(number_of_samples):
        for j in range(number_of_samples):
            a = i - 1000
            b = j - 1000

            result = a * b
            part1 = str(a) + " * " + str(b) + " = "
            part2 = str(result)
            results_multiplication.append(part1 + "\n" + part2)

    return results_multiplication


def generate_division_problems(number_of_samples):
    results_division = []
    for i in range(number_of_samples):
        for j in range(number_of_samples):
            a = i - 1000
            b = j - 1000

            if b == 0:  # avoiding division by zero
                part1 = str(a) + " / " + str(b) + " = "
                part2 = "Not defined - Division by zero is not defined"
                results_division.append(part1 + "\n" + part2)
                continue

            result = round(a / b, 2)  # rounding to 2 decimal places
            part1 = str(a) + " / " + str(b) + " = "
            part2 = str(result)
            results_division.append(part1 + "\n" + part2)

    return results_division


def generate_addition_with_3_numbers_problems(number_of_samples):
    results_addition_3_nums = []
    for _ in range(number_of_samples):
        a = random.randint(-100000000, 100000000)
        b = random.randint(-100000000, 100000000)
        c = random.randint(-100000000, 100000000)

        result = a + b + c
        part1 = str(a) + " + " + str(b) + " + " + str(c) + " = "
        part2 = str(result)
        results_addition_3_nums.append(part1 + "\n" + part2)

    return results_addition_3_nums


def generate_addition_subtraction_with_3_numbers_problems(number_of_samples):
    results_addition_subtraction_3_nums = []
    for _ in range(number_of_samples):
        a = random.randint(-100000000, 100000000)
        b = random.randint(-100000000, 100000000)
        c = random.randint(-100000000, 100000000)

        result = a + b - c
        part1 = str(a) + " + " + str(b) + " - " + str(c) + " = "
        part2 = str(result)
        results_addition_subtraction_3_nums.append(part1 + "\n" + part2)

    return results_addition_subtraction_3_nums


def generate_addition_subtraction_with_3_numbers_problems(number_of_samples):
    results_addition_subtraction = []
    for _ in range(number_of_samples):
        a = random.randint(-100000000, 100000000)
        b = random.randint(-100000000, 100000000)
        c = random.randint(-100000000, 100000000)

        result = a + b - c
        part1 = str(a) + " + " + str(b) + " - " + str(c) + " = "
        part2 = str(result)
        results_addition_subtraction.append(part1 + "\n" + part2)

    return results_addition_subtraction

def generate_subtraction_subtraction_with_3_numbers_problems(number_of_samples):
    results_subtraction_subtraction = []
    for _ in range(number_of_samples):
        a = random.randint(-100000000, 100000000)
        b = random.randint(-100000000, 100000000)
        c = random.randint(-100000000, 100000000)

        result = a - b - c
        part1 = str(a) + " - " + str(b) + " - " + str(c) + " = "
        part2 = str(result)
        results_subtraction_subtraction.append(part1 + "\n" + part2)

    return results_subtraction_subtraction

def generate_multiplication_division_with_3_numbers_problems(number_of_samples):
    results_multiplication_division = []
    for _ in range(number_of_samples):
        a = random.randint(-100000000, 100000000)
        b = random.randint(-100000000, 100000000)
        c = 0
        while c == 0:
            c = random.randint(9, 100)

        result = a * b / c
        part1 = str(a) + " * " + str(b) + " / " + str(c) + " = "
        part2 = str(result)
        results_multiplication_division.append(part1 + "\n" + part2)

    return results_multiplication_division


def generate_addition_division_with_3_numbers_problems(number_of_samples):
    results_addition_division_3_nums = []
    for _ in range(number_of_samples):
        a = random.randint(-100000000,100000000)
        b = random.randint(-100000000,100000000)
        c = 0
        while c == 0:
            c = random.randint(-14,29)

        result = a + b / c
        part1 = str(a) + " + " + str(b) + " / " + str(c) + " = "
        part2 = str(result)
        results_addition_division_3_nums.append(part1 + "\n" + part2)

    return results_addition_division_3_nums


def generate_addition_multiplication_with_3_numbers_problems(number_of_samples):
    results_addition_multiplication_3_nums = []
    for _ in range(number_of_samples):
        a = random.randint(-100000000,100000000)
        b = random.randint(-100000000,100000000)
        c = random.randint(-10000,10000)

        result = a + b * c
        part1 = str(a) + " + " + str(b) + " * " + str(c) + " = "
        part2 = str(result)
        results_addition_multiplication_3_nums.append(part1 + "\n" + part2)

    return results_addition_multiplication_3_nums


def generate_addition_with_5_numbers_problems(number_of_samples):
    results_addition_5_nums = []
    for _ in range(number_of_samples):
        a = random.randint(-100000000,100000000)
        b = random.randint(-100000000,100000000)
        c = random.randint(-100000000,100000000)
        d = random.randint(-100000000,100000000)
        e = random.randint(-100000000,100000000)

        result = a + b + c + d + e
        part1 = str(a) + " + " + str(b) + " + " + str(c) + " + " + str(d) + " + " + str(e) + " = "
        part2 = str(result)
        results_addition_5_nums.append(part1 + "\n" + part2)

    return results_addition_5_nums


def generate_exponential_with_2_numbers_problems(number_of_samples):
    results_exponential_2_nums = []
    for _ in range(number_of_samples):
        a = random.randint(-100000,100000) / 100
        b = random.randint(0,100) / 20
        result = a ** b
        part1 = str(a) + " ** " + str(b) + " = "

        part2 = str(result)
        results_exponential_2_nums.append(part1 + "\n" + part2)

    return results_exponential_2_nums


import random
import operator

# Mapping of operations
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def generate_random_math_problems(number_of_samples, min_numbers=3, max_numbers=6):
    results = []
    for _ in range(number_of_samples):
        # Randomly choose the number of operands in this problem
        num_operands = random.randint(min_numbers, max_numbers)

        operands = []
        operators = []
        for _ in range(num_operands):
            operands.append(random.randint(-1000, 1000))  # reduce the range to make computations faster
            operators.append(random.choice(list(ops.keys())))

        # Insert a division operation, if chosen
        if random.choice([True, False]):
            # Add a division operation
            pos = random.randint(0, num_operands-2)  # position to insert the operation
            operators[pos] = '/'
            operands[pos+1] = random.randint(1, 100)  # make sure we don't divide by zero

        # Calculate result
        result = operands[0]
        for i in range(1, num_operands):
            result = ops[operators[i-1]](result, operands[i])

        # Build the problem string
        problem = ""
        for i in range(num_operands):
            problem += str(operands[i])
            if i != num_operands - 1:
                problem += " " + operators[i] + " "
            else:
                problem += " = "

        # Append problem and solution to results
        results.append(problem + "\n" + str(result))

    return results




import random


def addition_step_by_step1(number_of_samples):

    def generate_addition_problem():
      num1 = random.randint(1, 9999999999)
      num2 = random.randint(1, 9999999999)
      return num1, num2, num1 + num2

    templates = [
        "Alright, let's solve this problem step by step. We have {} and {} and we're adding them together.",
        "No problem, let's work through this together. We're starting with {} and {} and adding them all up.",
        "Sure thing! We've got {} and {} and we're gonna add them together.",
        "OK, let's do this. We've got {} and {} and we're adding them all together.",
        "Let's get this math done. We have {} and {} and we're going to add them all together.",
        "Okay, we are given {} and {}. Let's add them up step by step.",
        "We have numbers {} and {}. Let's start adding them together.",
        "Let's break this down. We're going to add {} and {} together.",
        "Ready to do some math? We're starting with {} and {} and adding them up.",
        "Let's solve this addition problem. We have {} and {}, and we need to add them together.",
        "Not to worry, we've got {} and {}. Let's get to adding them!",
        "We are presented with {} and {}. Let's work out the sum.",
        "Okay, we are tasked with adding {} and {}. Let's begin!",
        "Here we go! We're going to add {} and {} together.",
        "We've got two numbers: {} and {}. Let's find their sum."
    ]

    
    problems = []
    for _ in range(number_of_samples):
        num1, num2, result = generate_addition_problem()
        explanation = random.choice(templates).format(num1, num2)
        explanation += "\n\n"

        num1, num2 = str(num1), str(num2)
        max_len = max(len(num1), len(num2))
        carry = 0
        for i in range(max_len):
            cur_digit_sum = carry
            cur_digit1 = int(num1[-i-1]) if i < len(num1) else 0
            cur_digit2 = int(num2[-i-1]) if i < len(num2) else 0
            cur_digit_sum += cur_digit1 + cur_digit2

            explanation += f"Step {i+1}: We'll start by adding the digits {cur_digit1} & {cur_digit2} in column {i+1} and get {cur_digit_sum}.\n"
            if cur_digit_sum > 9:
                explanation += f"We'll write down the last digit {cur_digit_sum%10} and carry the {cur_digit_sum//10} to the next column.\n\n"
                carry = cur_digit_sum//10
            else:
                explanation += "\n"
                carry = 0

        explanation += f"So, {num1} + {num2} = {result}.\n\n"
        problems.append(explanation)
    return problems



def addition_step_by_step2(number_of_samples):

    def generate_addition_problem():
      num1 = random.randint(1, 9999)
      num2 = random.randint(1, 9999)
      return num1, num2, num1 + num2

    templates = [
        "Alright, let's solve this problem step by step. We have {} and {} and we're adding them together.",
        "No problem, let's work through this together. We're starting with {} and {} and adding them all up.",
        "Sure thing! We've got {} and {} and we're gonna add them together.",
        "OK, let's do this. We've got {} and {} and we're adding them all together.",
        "Let's get this math done. We have {} and {} and we're going to add them all together.",
        "Okay, we are given {} and {}. Let's add them up step by step.",
        "We have numbers {} and {}. Let's start adding them together.",
        "Let's break this down. We're going to add {} and {} together.",
        "Ready to do some math? We're starting with {} and {} and adding them up.",
        "Let's solve this addition problem. We have {} and {}, and we need to add them together.",
        "Not to worry, we've got {} and {}. Let's get to adding them!",
        "We are presented with {} and {}. Let's work out the sum.",
        "Okay, we are tasked with adding {} and {}. Let's begin!",
        "Here we go! We're going to add {} and {} together.",
        "We've got two numbers: {} and {}. Let's find their sum."
    ]

    
    problems = []
    for _ in range(number_of_samples):
        num1, num2, result = generate_addition_problem()
        explanation = random.choice(templates).format(num1, num2)
        explanation += "\n\n"

        num1, num2 = str(num1), str(num2)
        max_len = max(len(num1), len(num2))
        carry = 0
        for i in range(max_len):
            cur_digit_sum = carry
            cur_digit1 = int(num1[-i-1]) if i < len(num1) else 0
            cur_digit2 = int(num2[-i-1]) if i < len(num2) else 0
            cur_digit_sum += cur_digit1 + cur_digit2

            explanation += f"Step {i+1}: We'll start by adding the digits {cur_digit1} & {cur_digit2} in column {i+1} and get {cur_digit_sum}.\n"
            if cur_digit_sum > 9:
                explanation += f"We'll write down the last digit {cur_digit_sum%10} and carry the {cur_digit_sum//10} to the next column.\n\n"
                carry = cur_digit_sum//10
            else:
                explanation += "\n"
                carry = 0

        explanation += f"So, {num1} + {num2} = {result}.\n\n"
        problems.append(explanation)
    return problems


import random

def substraction_step_by_step1(number_of_samples):

    templates = [
        "Alright, let's solve this problem step by step. We have {} and {}, and we're subtracting the second number from the first.",
        "No problem, let's work through this together. We're starting with {} and are subtracting {} from it.",
        "Sure thing! We've got {} and {}, and we're going to subtract the second number from the first.",
        "OK, let's do this. We've got {} and {}, and we're subtracting the second number from the first.",
        "Let's get this math done. We have {} and {}, and we're going to subtract the second number from the first.",
        "Alright, ready to do some subtraction? We're taking {} and subtracting {} from it.",
        "We can solve this together! We're beginning with {} and removing {} from it.",
        "Got it! So, we have {} and {}, and we'll subtract the latter from the former.",
        "Okay, let's tackle this math problem. We're starting with {} and subtracting {}.",
        "Let's dive into this subtraction. We'll start with {} and subtract {} from it."
    ]


    problems = []
    for _ in range(number_of_samples):
        num1 = random.randint(0, 1000000000)
        num2 = random.randint(0, 1000000000)
        if num2 > num1:
          num1, num2 = num2, num1
        result = num1 - num2

        explanation = random.choice(templates).format(num1, num2)
        explanation += "\n\n"

        nums = [str(num1), str(num2)]
        max_len = max([len(num) for num in nums])
        borrow = 0
        try:
          for i in range(max_len):
              cur_digit_diff = int(nums[0][-i-1]) - borrow
              cur_digit = int(nums[1][-i-1]) if i < len(nums[1]) else 0
              cur_digit_diff -= cur_digit

              explanation += f"Step {i+1}: We'll start by subtracting the digit {cur_digit} and the borrow {borrow} from {cur_digit_diff + borrow+cur_digit} in column {i+1} and get {cur_digit_diff}.\n"
              if i ==0:
                if cur_digit_diff < 0:
                    explanation += f"We add {cur_digit_diff} to 10 and get {(cur_digit_diff + 10)%10} as the first digit of the result.\n\n"
                    borrow = 1
                else:
                    explanation += f"{cur_digit_diff} is the first digit of our result.\n\n"
                    borrow = 0
              else:

                if cur_digit_diff < 0:
                    explanation += f"We add {cur_digit_diff} to 10 and get {(cur_digit_diff + 10)%10} as the next digit of the result.\n\n"
                    borrow = 1
                else:
                    explanation += f"{cur_digit_diff} is the next digit of our result.\n\n"
                    borrow = 0
        except:
          continue
        explanation += f"So, {num1} - {num2} = {result}."
        problems.append(explanation)

    return problems

def substraction_step_by_step2(number_of_samples):

    templates = [
        "Alright, let's solve this problem step by step. We have {} and {}, and we're subtracting the second number from the first.",
        "No problem, let's work through this together. We're starting with {} and are subtracting {} from it.",
        "Sure thing! We've got {} and {}, and we're going to subtract the second number from the first.",
        "OK, let's do this. We've got {} and {}, and we're subtracting the second number from the first.",
        "Let's get this math done. We have {} and {}, and we're going to subtract the second number from the first.",
        "Alright, ready to do some subtraction? We're taking {} and subtracting {} from it.",
        "We can solve this together! We're beginning with {} and removing {} from it.",
        "Got it! So, we have {} and {}, and we'll subtract the latter from the former.",
        "Okay, let's tackle this math problem. We're starting with {} and subtracting {}.",
        "Let's dive into this subtraction. We'll start with {} and subtract {} from it."
    ]


    problems = []
    for _ in range(number_of_samples):
        num1 = random.randint(0, 1000000)
        num2 = random.randint(0, 100000)
        if num2 > num1:
          num1, num2 = num2, num1
        result = num1 - num2

        explanation = random.choice(templates).format(num1, num2)
        explanation += "\n\n"

        nums = [str(num1), str(num2)]
        max_len = max([len(num) for num in nums])
        borrow = 0
        try:
          for i in range(max_len):
              cur_digit_diff = int(nums[0][-i-1]) - borrow
              cur_digit = int(nums[1][-i-1]) if i < len(nums[1]) else 0
              cur_digit_diff -= cur_digit

              explanation += f"Step {i+1}: We'll start by subtracting the digit {cur_digit} and the borrow {borrow} from {cur_digit_diff + borrow+cur_digit} in column {i+1} and get {cur_digit_diff}.\n"
              if i ==0:
                if cur_digit_diff < 0:
                    explanation += f"We add {cur_digit_diff} to 10 and get {(cur_digit_diff + 10)%10} as the first digit of the result.\n\n"
                    borrow = 1
                else:
                    explanation += f"{cur_digit_diff} is the first digit of our result.\n\n"
                    borrow = 0
              else:

                if cur_digit_diff < 0:
                    explanation += f"We add {cur_digit_diff} to 10 and get {(cur_digit_diff + 10)%10} as the next digit of the result.\n\n"
                    borrow = 1
                else:
                    explanation += f"{cur_digit_diff} is the next digit of our result.\n\n"
                    borrow = 0
        except:
          continue
        explanation += f"So, {num1} - {num2} = {result}."
        problems.append(explanation)
    return problems
import random

import random

import random

def multiplication_step_by_step(number_of_samples):
    problems = []
    for _ in range(number_of_samples):
        x = random.randint(0, 1000)
        y = random.randint(0, 500)
        result = 0
        templates = [
            f"Alright, let's solve this math problem step by step. First, we have the number {x}. Next, we see the multiplication sign, which means we need to multiply something. And what are we multiplying it by? We multiply it by {y}. So, we're going to take the number {x} and add it to itself {y} times.",
            f"OK, let's work through this together. We're starting with {x} and we're going to multiply it by {y}, which means we add {x} to itself {y} times.",
            f"Sure thing! We've got {x} and we're gonna multiply it by {y}. That's the same as adding {x} to itself {y} times.",
            f"Let's get this math done. We have {x} and we're going to multiply it by {y}. This is the same as taking {x} and adding it to itself {y} times.",
            f"OK, let's crack this. We're given {x} and our task is to multiply it by {y}. Essentially, we'll be adding {x} to itself {y} times.",
            f"Without delay, let's solve this. We've got {x} and we will be multiplying it by {y}, that is, adding {x} to itself {y} times.",
            f"Sure thing, let's get straight to it. We start with {x} and we're going to multiply it by {y}, which means adding {x} to itself {y} times.",
            f"Let's roll up our sleeves and solve this. We have {x} and we're going to multiply it by {y}, essentially adding {x} to itself {y} times."
        ]
        explanation = random.choice(templates)
        explanation += "\n"
        for i in range(1, y+1):
            result += x
            explanation += f"Step {i}: {result-x} + {x} = {result}\n"
        explanation += f"\nSo, {x}*{y} = {result}"
        problems.append(explanation)
    return problems



def multiplication_step_by_step_short1(number_of_samples):
    templates = [
        "Let's calculate {num1} x {num2}",
        "We're going to solve {num1} multiplied by {num2}",
        "Alright, let's work through {num1} times {num2} step by step",
        "No problem, we've got {num1} and {num2} to multiply",
        "Sure thing! Let's multiply {num1} and {num2} together"
    ]

    alternative_texts = [
        "that equals",
        "which equals",
        "that is equal",
        "what gives us",
        "that results in",
        "yielding",
        "giving us",
        "producing",
        "resulting in"
    ]

    problems = []
    for _ in range(number_of_samples):
        num1 = random.randint(0, 10000)
        num2 = random.randint(0, 10000)
        
        num1_str = str(num1)
        num2_str = str(num2)

        template = random.choice(templates)
        explanation = template.format(num1=num1, num2=num2) + "\n"

        explanation += f"{num1} × {num2} = {num2} × ({num1_str})\n"

        partial_sums = []
        for i, digit in enumerate(num1_str[::-1]):
            partial_product = int(digit) * num2 * (10 ** i)
            partial_sums.append(partial_product)
            alternative_text = random.choice(alternative_texts)
            explanation += f"+ {num2} × {digit}{'0' * i} {alternative_text} {partial_product}\n"

        result = sum(partial_sums)
        explanation += f"\n= {result}\n"

        problems.append(explanation)

    return problems



def multiplication_step_by_step_short2(number_of_samples):
    templates = [
        "Let's calculate {num1} x {num2}",
        "We're going to solve {num1} multiplied by {num2}",
        "Alright, let's work through {num1} times {num2} step by step",
        "No problem, we've got {num1} and {num2} to multiply",
        "Sure thing! Let's multiply {num1} and {num2} together"
    ]

    alternative_texts = [
        "that equals",
        "which equals",
        "that is equal",
        "what gives us",
        "that results in",
        "yielding",
        "giving us",
        "producing",
        "resulting in"
    ]

    problems = []
    for _ in range(number_of_samples):
        num1 = random.randint(0, 100000000)
        num2 = random.randint(0, 100000000)
        
        num1_str = str(num1)
        num2_str = str(num2)

        template = random.choice(templates)
        explanation = template.format(num1=num1, num2=num2) + "\n"

        explanation += f"{num1} × {num2} = {num2} × ({num1_str})\n"

        partial_sums = []
        for i, digit in enumerate(num1_str[::-1]):
            partial_product = int(digit) * num2 * (10 ** i)
            partial_sums.append(partial_product)
            alternative_text = random.choice(alternative_texts)
            explanation += f"+ {num2} × {digit}{'0' * i} {alternative_text} {partial_product}\n"

        result = sum(partial_sums)
        explanation += f"\n= {result}\n"

        problems.append(explanation)

    return problems



import random

def division_step_by_step1(number_of_samples):
    templates = [
        "Let's divide {dividend} by {divisor}.",
        "We're going to perform division on {dividend} with {divisor} as the divisor.",
        "Alright, let's work through the division of {dividend} by {divisor} step by step.",
        "No problem, we've got {dividend} and {divisor} for the division.",
        "Sure thing! Let's divide {dividend} by {divisor} together."
    ]
    def long_division(dividend, divisor):
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder
    #explanation += template.format(dividend=dividend, divisor=divisor) + "\n"
    explanations = []
    def step_by_step_solution(dividend, divisor):
        quotient, remainder = long_division(dividend, divisor)
        result = str(quotient) + " R" + str(remainder)

        solution = f"{dividend} ÷ {divisor} = {result}\n"
        #solution += f"We want to divide {dividend} by {divisor}.\n"
        template =random.choice(templates)
        solution += template.format(dividend=dividend, divisor=divisor) + "\n"
        temp_dividend = str(dividend)
        temp_result = ""
        current_remainder = 0
        result=""
        for i, digit in enumerate(temp_dividend):
            current_remainder = current_remainder * 10 + int(digit)

            current_quotient, current_remainder = long_division(current_remainder, divisor)

            temp_result += str(current_quotient)
            if i ==0:
              prev_remainder = temp_dividend[i:i + 1]
            solution += f"\nStep {i + 1}:\n"
            solution += f"{divisor} goes into {prev_remainder} {current_quotient} times with a remainder of {current_remainder}.\n"
            solution += f"Write down {current_quotient} as next digit of of the result. \n"
            result+=str(current_quotient)
            result=str(int(result))
            solution += f"Result so far: {result}\n" 
            solution += f"Subtract {current_quotient * divisor} from {current_remainder + current_quotient * divisor} to get {current_remainder}.\n"
            if str(temp_dividend[i + 1:i + 2])=="":
              break
            prev_remainder= int(str(current_remainder) +str(temp_dividend[i + 1:i + 2]))
            solution += f"Bring next digit ({temp_dividend[i + 1:i + 2]}) of the dividend behind the {current_remainder} and repeat the process: {prev_remainder} / {divisor}\n"

        solution += f"\nThe final result is {result} with a remainder of {current_remainder}."
        return solution

    for i in range(number_of_samples):

      dividend = random.randint(10, 99999)
      divisor = random.randint(1, 9)

      solution = step_by_step_solution(dividend, divisor)


      explanations.append(solution)

    return explanations


def division_step_by_step2(number_of_samples):

  def long_division(dividend, divisor):
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder
  def step_by_step_solution(dividend, divisor):
      quotient, remainder = long_division(dividend, divisor)
      result = str(quotient) + " R" + str(remainder)
      templates = {
          "introduction": [
              "{dividend} ÷ {divisor} \n",
              "We're dividing {dividend} by {divisor} \n",
              "{dividend} divided by {divisor} \n",
              "We look at the division of {dividend} by {divisor} \n",
              "We divide {dividend} by {divisor}\n",
              "Let's divide {dividend} by {divisor}\n"
          ],
          "divide_statement": [
              "We want to divide {dividend} by {divisor}.\n",
              "Our goal is to divide {dividend} by {divisor}.\n",
              "We're looking to find how many times {divisor} goes into {dividend}.\n",
              "Let's see how many times {divisor} fits into {dividend}.\n",
              "The aim is to understand the frequency of {divisor} in {dividend}.\n",
              "We want to figure out the number of times {dividend} can be divided by {divisor}.\n"
          ],
          "step": [
              "\nStep {step_number}:\n",
              "\nMoving on to step {step_number}:\n",
              "\nLet's proceed to step {step_number}:\n",
              "\nGoing ahead to step {step_number}:\n",
              "\nAdvancing to step {step_number}:\n",
              "\nOn to step {step_number}:\n"
          ],
          "division_process": [
              "{divisor} goes into {prev_remainder} {current_quotient} times with a remainder of {current_remainder}.\n",
              "When dividing {prev_remainder} by {divisor}, we get {current_quotient} with a remainder of {current_remainder}.\n",
              "The number {divisor} fits into {prev_remainder} {current_quotient} times, leaving a remainder of {current_remainder}.\n",
              "{divisor} can be fit into {prev_remainder} {current_quotient} times, resulting in a remainder of {current_remainder}.\n",
              "{prev_remainder} divided by {divisor} is {current_quotient} with a remainder of {current_remainder}.\n",
              "If we divide {prev_remainder} by {divisor}, we get {current_quotient} and a remainder of {current_remainder}.\n"
          ],
          "write_quotient": [
              "Write down {current_quotient} as next digit of the result. \n",
              "Record the quotient {current_quotient} as the next digit in the result. \n",
              "The number {current_quotient} becomes the next digit in our result. \n",
              "Put {current_quotient} as the next digit of the answer. \n",
              "Use {current_quotient} as the next digit of our solution. \n",
              "The next digit of our result is {current_quotient}. \n"
          ],
          "subtraction": [
              "Subtract {product} from {sum} to get {remainder}.\n",
              "If we take {product} away from {sum}, we end up with {remainder}.\n",
              "Deduct {product} from {sum} and we're left with {remainder}.\n",
              "Subtracting {product} from {sum} leaves us with {remainder}.\n",
              "If we subtract {product} from {sum}, we get {remainder}.\n",
              "The remainder is {remainder} after subtracting {product} from {sum}.\n"
          ],
          "next_digit": [
              "Bring next digit ({next_digit}) of the dividend behind the {current_remainder} and repeat the process: {prev_remainder} / {divisor}\n",
              "Take the next digit ({next_digit}) from the dividend and append it to {current_remainder}, then repeat: {prev_remainder} / {divisor}\n",
              "Fetch the next digit ({next_digit}) from the dividend, attach it to {current_remainder} and continue: {prev_remainder} / {divisor}\n",
              "Grab the next digit ({next_digit}) from the dividend, add it to {current_remainder}, then carry on: {prev_remainder} / {divisor}\n",
              "Include the next digit ({next_digit}) from the dividend after {current_remainder}, then repeat: {prev_remainder} / {divisor}\n",
              "Append the next digit ({next_digit}) from the dividend to {current_remainder} and continue with: {prev_remainder} / {divisor}\n"
          ],
          "final_result": [
              "\nThe final result is {result} with a remainder of {remainder}.",
              "\nOur division results in {result} with a remaining {remainder}.",
              "\nThe final outcome is {result}, with a leftover of {remainder}.",
              "\nIn conclusion, the division gives {result} with a balance of {remainder}.",
              "\nAfter the division, we end up with {result} and a remainder of {remainder}.",
              "\nThe quotient of the division is {result}, and the remainder is {remainder}."
          ]
      }
      
      solution = random.choice(templates['introduction']).format(dividend=dividend, divisor=divisor)
      solution += random.choice(templates['divide_statement']).format(dividend=dividend, divisor=divisor)

      temp_dividend = str(dividend)
      temp_result = ""
      current_remainder = 0
      result = ""
      first_decimal=True
      i = 0
      while len(result.split('.')[1] if '.' in result else result) < 8:
          current_remainder = current_remainder * 10 + int(temp_dividend[i]) if i < len(temp_dividend) else current_remainder * 10
          current_quotient, current_remainder = long_division(current_remainder, divisor)
          temp_result += str(current_quotient)
          
          if i == 0:
              prev_remainder = temp_dividend[i:i + 1]
              
          solution += random.choice(templates['step']).format(step_number=i+1)
          solution += random.choice(templates['division_process']).format(divisor=divisor, prev_remainder=prev_remainder, current_quotient=current_quotient, current_remainder=current_remainder)
          
          result += str(current_quotient)
          if i >= len(temp_dividend) - 1 and '.' not in result:
              result += '.'

          solution += random.choice(templates['write_quotient']).format(current_quotient=current_quotient)
          solution += f"Result so far: {float(result)}\n"
          solution += random.choice(templates['subtraction']).format(product=current_quotient*divisor, sum=current_remainder+current_quotient*divisor, remainder=current_remainder)
          
          if str(temp_dividend[i + 1:i + 2]) == "":
              prev_remainder = int(str(current_remainder) + '0')
              if first_decimal ==True:
                decimaldigits=1
                first_decimal= False
              else:
                decimaldigits+=1
              solution += f"Since there are no more digits in the dividend, we add a zero to the remainder making it {prev_remainder}, and continue the process.\n"
          else:
              prev_remainder = int(str(current_remainder) + str(temp_dividend[i + 1:i + 2]))
              solution += random.choice(templates['next_digit']).format(next_digit=temp_dividend[i + 1:i + 2], current_remainder=current_remainder, prev_remainder=prev_remainder, divisor=divisor)
          if result.find(".")>=0 and result[-1]==result[-2:-1]:
            result = round (float(result),i-1)
            break
          i += 1
      #current_remainder= current_remainder / float(10^8)

      solution += random.choice(templates['final_result']).format(result=float(result), remainder=current_remainder/10**decimaldigits)
      
      return solution




  explanations=[]
  for i in range(number_of_samples):

    dividend = random.randint(10, 999999)
    divisor = random.randint(1, 99)


    solution = step_by_step_solution(dividend, divisor)


    explanations.append(solution)

  return explanations




def division_step_by_step3(number_of_samples):
  def long_division(dividend, divisor):
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder

  def step_by_step_solution(dividend, divisor):
      quotient, remainder = long_division(dividend, divisor)
      result = str(quotient) + " R" + str(remainder)
      templates = {
          "introduction": [
              "{dividend} ÷ {divisor} \n",
              "We're dividing {dividend} by {divisor} \n",
              "{dividend} divided by {divisor} \n",
              "We look at the division of {dividend} by {divisor} \n",
              "We divide {dividend} by {divisor}\n",
              "Let's divide {dividend} by {divisor}\n"
          ],
          "divide_statement": [
              "We want to divide {dividend} by {divisor}.\n",
              "Our goal is to divide {dividend} by {divisor}.\n",
              "We're looking to find how many times {divisor} goes into {dividend}.\n",
              "Let's see how many times {divisor} fits into {dividend}.\n",
              "The aim is to understand the frequency of {divisor} in {dividend}.\n",
              "We want to figure out the number of times {dividend} can be divided by {divisor}.\n"
          ],
          "step": [
              "\nStep {step_number}:\n",
              "\nMoving on to step {step_number}:\n",
              "\nLet's proceed to step {step_number}:\n",
              "\nGoing ahead to step {step_number}:\n",
              "\nAdvancing to step {step_number}:\n",
              "\nOn to step {step_number}:\n"
          ],
          "division_process": [
              "{divisor} goes into {prev_remainder} {current_quotient} times with a remainder of {current_remainder}.\n",
              "When dividing {prev_remainder} by {divisor}, we get {current_quotient} with a remainder of {current_remainder}.\n",
              "The number {divisor} fits into {prev_remainder} {current_quotient} times, leaving a remainder of {current_remainder}.\n",
              "{divisor} can be fit into {prev_remainder} {current_quotient} times, resulting in a remainder of {current_remainder}.\n",
              "{prev_remainder} divided by {divisor} is {current_quotient} with a remainder of {current_remainder}.\n",
              "If we divide {prev_remainder} by {divisor}, we get {current_quotient} and a remainder of {current_remainder}.\n"
          ],
          "write_quotient": [
              "Write down {current_quotient} as next digit of the result. \n",
              "Record the quotient {current_quotient} as the next digit in the result. \n",
              "The number {current_quotient} becomes the next digit in our result. \n",
              "Put {current_quotient} as the next digit of the answer. \n",
              "Use {current_quotient} as the next digit of our solution. \n",
              "The next digit of our result is {current_quotient}. \n"
          ],
          "subtraction": [
              "Subtract {product} from {sum} to get {remainder}.\n",
              "If we take {product} away from {sum}, we end up with {remainder}.\n",
              "Deduct {product} from {sum} and we're left with {remainder}.\n",
              "Subtracting {product} from {sum} leaves us with {remainder}.\n",
              "If we subtract {product} from {sum}, we get {remainder}.\n",
              "The remainder is {remainder} after subtracting {product} from {sum}.\n"
          ],
          "next_digit": [
              "Bring next digit ({next_digit}) of the dividend behind the {current_remainder} and repeat the process: {prev_remainder} / {divisor}\n",
              "Take the next digit ({next_digit}) from the dividend and append it to {current_remainder}, then repeat: {prev_remainder} / {divisor}\n",
              "Fetch the next digit ({next_digit}) from the dividend, attach it to {current_remainder} and continue: {prev_remainder} / {divisor}\n",
              "Grab the next digit ({next_digit}) from the dividend, add it to {current_remainder}, then carry on: {prev_remainder} / {divisor}\n",
              "Include the next digit ({next_digit}) from the dividend after {current_remainder}, then repeat: {prev_remainder} / {divisor}\n",
              "Append the next digit ({next_digit}) from the dividend to {current_remainder} and continue with: {prev_remainder} / {divisor}\n"
          ],
          "final_result": [
              "\nThe final result is {result} with a remainder of {remainder}.",
              "\nOur division results in {result} with a remaining {remainder}.",
              "\nThe final outcome is {result}, with a leftover of {remainder}.",
              "\nIn conclusion, the division gives {result} with a balance of {remainder}.",
              "\nAfter the division, we end up with {result} and a remainder of {remainder}.",
              "\nThe quotient of the division is {result}, and the remainder is {remainder}."
          ]
      }
      
      solution = random.choice(templates['introduction']).format(dividend=dividend, divisor=divisor)
      solution += random.choice(templates['divide_statement']).format(dividend=dividend, divisor=divisor)

      temp_dividend = str(dividend)
      temp_result = ""
      current_remainder = 0
      result = ""
      first_decimal=True
      i = 0
      while len(result.split('.')[1] if '.' in result else result) < 8:
          current_remainder = current_remainder * 10 + int(temp_dividend[i]) if i < len(temp_dividend) else current_remainder * 10
          current_quotient, current_remainder = long_division(current_remainder, divisor)
          temp_result += str(current_quotient)
          
          if i == 0:
              prev_remainder = temp_dividend[i:i + 1]
              
          solution += random.choice(templates['step']).format(step_number=i+1)
          solution += random.choice(templates['division_process']).format(divisor=divisor, prev_remainder=prev_remainder, current_quotient=current_quotient, current_remainder=current_remainder)
          
          result += str(current_quotient)
          if i >= len(temp_dividend) - 1 and '.' not in result:
              result += '.'

          solution += random.choice(templates['write_quotient']).format(current_quotient=current_quotient)
          solution += f"Result so far: {float(result)}\n"
          solution += random.choice(templates['subtraction']).format(product=current_quotient*divisor, sum=current_remainder+current_quotient*divisor, remainder=current_remainder)
          
          if str(temp_dividend[i + 1:i + 2]) == "":
              prev_remainder = int(str(current_remainder) + '0')
              if first_decimal ==True:
                decimaldigits=1
                first_decimal= False
              else:
                decimaldigits+=1
              solution += f"Since there are no more digits in the dividend, we add a zero to the remainder making it {prev_remainder}, and continue the process.\n"
          else:
              prev_remainder = int(str(current_remainder) + str(temp_dividend[i + 1:i + 2]))
              solution += random.choice(templates['next_digit']).format(next_digit=temp_dividend[i + 1:i + 2], current_remainder=current_remainder, prev_remainder=prev_remainder, divisor=divisor)
          if result.find(".")>=0 and result[-1]==result[-2:-1]:
            result = round (float(result),i-1)
            break
          i += 1
      #current_remainder= current_remainder / float(10^8)

      solution += random.choice(templates['final_result']).format(result=float(result), remainder=current_remainder/10**decimaldigits)
      
      return solution




  explanations=[]
  for i in range(number_of_samples):

    dividend = random.randint(10, 99999999)
    divisor = random.randint(1, 999)


    solution = step_by_step_solution(dividend, divisor)


    explanations.append(solution)

  return explanations






# Generate 1 problem
#problems = generate_division_problems (1)

# Print the problem
#print(problems[0])



