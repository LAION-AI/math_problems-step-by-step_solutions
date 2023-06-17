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
        b = random.randint(0,200) / 20

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




def generate_hypothenuse_with_pythagoras(number_of_samples):
    # define templates for each step
    template_intro = ["We are given a right-angled triangle with side 'a' measuring {side1} units and side 'b' measuring {side2} units. We're looking to find the length of the hypotenuse (h).",
                      "We have a right triangle where the lengths of sides 'a' and 'b' are {side1} units and {side2} units respectively. We are tasked with finding the length of the hypotenuse (h).",
                      "In a right-angled triangle with sides 'a' and 'b' of lengths {side1} units and {side2} units respectively, we are searching for the length of the hypotenuse (h).",
                      "Given a right triangle with side lengths of 'a' = {side1} units and 'b' = {side2} units, we're aiming to find the length of the hypotenuse, 'h'.",
                      "In a scenario where we have a right triangle, side 'a' is {side1} units long and side 'b' is {side2} units long. Our objective is to compute the length of the hypotenuse (h).",
                      "Imagine a right triangle with sides 'a' and 'b' that measure {side1} units and {side2} units respectively. Our mission is to determine the length of the hypotenuse, denoted as 'h'.",
                      "Let's consider a right-angled triangle, where the length of side 'a' is {side1} units and side 'b' is {side2} units. We're looking to ascertain the length of the hypotenuse, 'h'.",
                      "We're dealing with a right triangle here. Side 'a' is {side1} units, side 'b' is {side2} units. Our goal? To find out how long the hypotenuse (h) is.",
                      "Think of a right-angled triangle. Side 'a' has a length of {side1} units, and side 'b' is {side2} units long. We're tasked with determining the length of the hypotenuse (h).",
                      "Picture this: a right triangle. Side 'a' measures {side1} units, side 'b' measures {side2} units. Our task is to figure out the length of the hypotenuse, 'h'.",
                      "Let's work with a right-angled triangle where side 'a' equals {side1} units and side 'b' equals {side2} units. Our task is to identify the length of the hypotenuse, 'h'.",
                      "We have a right triangle at our hands, with side 'a' being {side1} units long and side 'b' being {side2} units long. We're aiming to uncover the length of the hypotenuse, denoted as 'h'."]
    
    template_step1 = ["Step 1: According to the Pythagorean theorem, the square of the hypotenuse is equal to the sum of the squares of the other two sides.",
                      "The first step is to remember the Pythagorean theorem, which states that in any right triangle, the square of the length of the hypotenuse is the sum of the squares of the lengths of the other two sides.",
                      "We begin with the Pythagorean theorem, which says the hypotenuse's square is the sum of the squares of the other two sides.",
                      "Firstly, we apply the Pythagorean theorem. It states that the square of the hypotenuse is equivalent to the sum of the squares of the other two sides.",
                      "Starting off with the Pythagorean theorem, the square of the hypotenuse equals the sum of the squares of the other two sides.",
                      "The initial step is guided by the Pythagorean theorem. This theorem posits that the hypotenuse's square equals the sum of the squares of the other two sides.",
                      "Our journey starts with the Pythagorean theorem, declaring that the square of the hypotenuse amounts to the sum of the squares of the other two sides.",
                      "First and foremost, we acknowledge the Pythagorean theorem, asserting that the square of the hypotenuse is the total of the squares of the other two sides.",
                      "We kick off with the Pythagorean theorem, which claims the square of the hypotenuse is the aggregate of the squares of the other two sides.",
                      "Step one involves the Pythagorean theorem. This theorem suggests that the square of the hypotenuse equals the accumulation of the squares of the other two sides.",
                      "Let's start with the Pythagorean theorem, according to which the square of the hypotenuse equals the summation of the squares of the other two sides.",
                      "We start by applying the Pythagorean theorem. It says the square of the hypotenuse is the combination of the squares of the other two sides."]
    
    template_step2 = ["Step 2: Applying the theorem, we get {side1}^2 + {side2}^2 = h^2.",
                      "Next, we apply the theorem to our specific situation, yielding {side1}^2 + {side2}^2 = h^2.",
                      "We then apply this theorem to our case, which gives us {side1}^2 + {side2}^2 = h^2.",
                      "The theorem applied to our case gives us {side1}^2 + {side2}^2 = h^2.",
                      "When we apply this theorem, we get {side1}^2 + {side2}^2 = h^2.",
                      "Upon application of the theorem, the equation is {side1}^2 + {side2}^2 = h^2.",
                      "By implementing the theorem, we obtain {side1}^2 + {side2}^2 = h^2.",
                      "In applying the theorem, we derive {side1}^2 + {side2}^2 = h^2.",
                      "Through the theorem's application, it follows that {side1}^2 + {side2}^2 = h^2.",
                      "Upon using the theorem, we are left with {side1}^2 + {side2}^2 = h^2.",
                      "By leveraging the theorem, we get {side1}^2 + {side2}^2 = h^2.",
                      "Through utilizing the theorem, we attain {side1}^2 + {side2}^2 = h^2."]
    
    template_step3 = ["Step 3: Simplifying the equation, we have {side1}^2 + {side2}^2 = h^2.",
                      "In the third step, we simplify the equation, which gives us {side1}^2 + {side2}^2 = h^2.",
                      "Then, we simplify the equation, resulting in {side1}^2 + {side2}^2 = h^2.",
                      "We proceed to simplify the equation to {side1}^2 + {side2}^2 = h^2.",
                      "Simplifying the equation leaves us with {side1}^2 + {side2}^2 = h^2.",
                      "On simplifying the equation, we have {side1}^2 + {side2}^2 = h^2.",
                      "We then simplify the equation, and we get {side1}^2 + {side2}^2 = h^2.",
                      "We simplify the equation next, yielding {side1}^2 + {side2}^2 = h^2.",
                      "When we simplify the equation, it becomes {side1}^2 + {side2}^2 = h^2.",
                      "Upon simplification of the equation, we get {side1}^2 + {side2}^2 = h^2.",
                      "Simplification of the equation results in {side1}^2 + {side2}^2 = h^2.",
                      "By simplifying the equation, we obtain {side1}^2 + {side2}^2 = h^2."]
    
    template_step4 = ["Step 4: Taking the square root of both sides, we find that h = sqrt({side1}^2 + {side2}^2).",
                      "In the fourth step, we take the square root of both sides, which leads us to h = sqrt({side1}^2 + {side2}^2).",
                      "Next, we take the square root of both sides of the equation, giving us h = sqrt({side1}^2 + {side2}^2).",
                      "We now take the square root of both sides of the equation to get h = sqrt({side1}^2 + {side2}^2).",
                      "We take the square root on both sides of the equation, resulting in h = sqrt({side1}^2 + {side2}^2).",
                      "By taking the square root on both sides, we get h = sqrt({side1}^2 + {side2}^2).",
                      "When we take the square root of both sides, we find that h = sqrt({side1}^2 + {side2}^2).",
                      "Upon taking the square root of both sides, it results in h = sqrt({side1}^2 + {side2}^2).",
                      "Taking the square root of both sides of the equation, we obtain h = sqrt({side1}^2 + {side2}^2).",
                      "After taking the square root on both sides, we conclude that h = sqrt({side1}^2 + {side2}^2).",
                      "By taking the square root on both sides, it is found that h = sqrt({side1}^2 + {side2}^2).",
                      "We determine h by taking the square root of both sides, which yields h = sqrt({side1}^2 + {side2}^2)."]
    
    template_conclusion = ["So, the length of the hypotenuse (h) is approximately {hypotenuse} units.",
                           "Therefore, the length of the hypotenuse, 'h', is roughly {hypotenuse} units.",
                           "Hence, the length of the hypotenuse (h) is about {hypotenuse} units.",
                           "As a result, the hypotenuse 'h' measures approximately {hypotenuse} units.",
                           "So, 'h', the hypotenuse, has a length of approximately {hypotenuse} units.",
                           "In conclusion, the hypotenuse 'h' is roughly {hypotenuse} units long.",
                           "Thus, the length of the hypotenuse (h) is approximately {hypotenuse} units.",
                           "Accordingly, the length of the hypotenuse, noted as 'h', is around {hypotenuse} units.",
                           "This means that the length of the hypotenuse 'h' is nearly {hypotenuse} units.",
                           "Consequently, the hypotenuse 'h' measures about {hypotenuse} units.",
                           "This leads us to conclude that the hypotenuse (h) is approximately {hypotenuse} units long.",
                           "Subsequently, the length of the hypotenuse, known as 'h', is nearly {hypotenuse} units."]

    results = []
    for _ in range(number_of_samples):
        side1 = random.randint(1, 100)
        side2 = random.randint(1, 100)
        hypotenuse = math.sqrt(side1**2 + side2**2)
        
        # randomly select a template for each step
        explanation_intro = random.choice(template_intro).format(side1=side1, side2=side2)
        explanation_step1 = random.choice(template_step1)
        explanation_step2 = random.choice(template_step2).format(side1=side1, side2=side2)
        explanation_step3 = random.choice(template_step3).format(side1=side1, side2=side2)
        explanation_step4 = random.choice(template_step4).format(side1=side1, side2=side2)
        explanation_conclusion = random.choice(template_conclusion).format(hypotenuse=round(hypotenuse, 2))
        
        # combine all steps to form the final explanation
        explanation = explanation_intro + '\n' + explanation_step1 + '\n' + explanation_step2 + '\n' + explanation_step3 + '\n' + explanation_step4 + '\n' + explanation_conclusion
        results.append(explanation)
    return results








import math
import random
import random
import math

def generate_missing_side_with_pythagoras(number_of_samples):
    # define templates for each step
    template_intro = ["We are given a right-angled triangle with hypotenuse 'h' measuring {hypotenuse} units and one side 'a' measuring {side1} units. We're looking to find the length of the other side.",
                      "Consider a right triangle where the lengths of the hypotenuse 'h' is {hypotenuse} units and one side 'a' is {side1} units. We are tasked with finding the length of the missing side.",
                      "Imagine a right-angled triangle. The hypotenuse 'h' measures {hypotenuse} units, one side 'a' measures {side1} units. Our task is to figure out the length of the other side.",
                      "Let's work with a right-angled triangle where the hypotenuse 'h' equals {hypotenuse} units and one side 'a' equals {side1} units. Our task is to identify the length of the other side.",
                      "Picturing a right triangle, we know the length of the hypotenuse 'h' to be {hypotenuse} units and one of the sides 'a' to be {side1} units. Our aim is to find the length of the remaining side.",
                      "We are dealing with a right-angled triangle, with a hypotenuse 'h' of {hypotenuse} units and one side 'a' of {side1} units. We need to find out how long the other side is.",
                      "Envision a right triangle with hypotenuse 'h' at {hypotenuse} units and a side 'a' at {side1} units. We are searching for the length of the second side."]

    template_step1 = ["Step 1: According to the Pythagorean theorem, the square of the hypotenuse is equal to the sum of the squares of the other two sides. In this case, we can rearrange the formula to find the missing side.",
                      "The first step is to remember the Pythagorean theorem, which states that in any right triangle, the square of the length of the hypotenuse is the sum of the squares of the lengths of the other two sides. We'll modify the formula to calculate our missing side.",
                      "We start by applying the Pythagorean theorem. In our situation, we will adjust the theorem to calculate the missing side length.",
                      "Step one involves the Pythagorean theorem. Given our scenario, we'll be tweaking the theorem to compute the length of the missing side.",
                      "The initial step calls upon the Pythagorean theorem. The square of the hypotenuse is equal to the sum of the squares of the other two sides. We'll alter this theorem to find the length of the missing side.",
                      "We first turn to the Pythagorean theorem, where the hypotenuse's square equals the sum of the squares of the other two sides. We will adapt this theorem for our needs.",
                      "Firstly, we make use of the Pythagorean theorem. This theorem states that the square of the hypotenuse is the sum of the squares of the other two sides. We will rearrange this to find the missing side."]

    template_step2 = ["Step 2: Applying the rearranged theorem, we get {hypotenuse}^2 - {side1}^2 = missing side^2.",
                      "Next, we apply the adjusted theorem to our specific situation, yielding {hypotenuse}^2 - {side1}^2 = missing side^2.",
                      "We then apply this modified theorem to our case, which gives us {hypotenuse}^2 - {side1}^2 = missing side^2.",
                      "When we apply this revised theorem, we get {hypotenuse}^2 - {side1}^2 = missing side^2.",
                      "The next step involves using the modified theorem, which gives us {hypotenuse}^2 - {side1}^2 = missing side^2.",
                      "Following this, we apply our adjusted formula. This provides us with {hypotenuse}^2 - {side1}^2 = missing side^2.",
                      "Moving on, we utilize the rearranged formula, which results in {hypotenuse}^2 - {side1}^2 = missing side^2."]

    template_step3 = ["Step 3: Taking the square root of both sides, we find that the missing side = sqrt({hypotenuse}^2 - {side1}^2).",
                      "In the third step, we take the square root of both sides, which leads us to missing side = sqrt({hypotenuse}h^2 - {side1}^2).",
                      "Next, we take the square root of both sides of the equation, giving us missing side = sqrt({hypotenuse}^2 - {side1}^2).",
                      "We now take the square root of both sides of the equation to get missing side = sqrt({hypotenuse}^2 - {side1}^2).",
                      "Lastly, we will take the square root of both sides of our equation. This gives us missing side = sqrt({hypotenuse}^2 - {side1}^2).",
                      "The final step is to take the square root of both sides, leading us to missing side = sqrt({hypotenuse}^2 - {side1}^2).",
                      "The concluding step requires us to take the square root of both sides, resulting in missing side = sqrt({hypotenuse}^2 - {side1}^2)."]

    template_conclusion = ["So, the length of the missing side is approximately {missing_side} units.",
                          "Therefore, the length of the missing side is roughly {missing_side} units.",
                          "Hence, the length of the missing side is about {missing_side} units.",
                          "As a result, the missing side measures approximately {missing_side} units.",
                          "Thus, the missing side is approximately {missing_side} units long.",
                          "This implies that the missing side's length is approximately {missing_side} units.",
                          "Consequently, the length of the missing side is roughly {missing_side} units.",
                          "In conclusion, the missing side is about {missing_side} units long."]

    samples = []
    for _ in range(number_of_samples):
        hypotenuse = round(random.uniform(1, 100), 2)
        side1 = round(random.uniform(0.5, hypotenuse), 3)
        missing_side = round(math.sqrt(hypotenuse**2 - side1**2), 3)
        problems = []
        problem = '\n'.join([
            random.choice(template_intro).format(hypotenuse=hypotenuse, side1=side1),
            random.choice(template_step1),
            random.choice(template_step2).format(hypotenuse=hypotenuse, side1=side1),
            random.choice(template_step3).format(hypotenuse=hypotenuse, side1=side1),
            random.choice(template_conclusion).format(missing_side=missing_side)
        ])
        problems.append(problem)


    
    return problems




#print(generate_missing_side_with_pythagoras(1)[0])



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


def long_division(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder
import random

def division_step_by_step1(number_of_samples):
    templates = [
        "Let's divide {dividend} by {divisor}.",
        "We're going to perform division on {dividend} with {divisor} as the divisor.",
        "Alright, let's work through the division of {dividend} by {divisor} step by step.",
        "No problem, we've got {dividend} and {divisor} for the division.",
        "Sure thing! Let's divide {dividend} by {divisor} together."
    ]
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




def generate_fraction_problems(num_problems):


    def generate_fraction_problem():
        numer1 = random.randint(1, 100)
        denom1 = random.randint(1, 100)
        numer2 = random.randint(1, 100)
        denom2 = random.randint(1, 100)
        
        operator = random.choice(['+', '-', '*', '/'])
        
        fraction1 = f"{numer1}/{denom1}"
        fraction2 = f"{numer2}/{denom2}"
        
        problem = f"{fraction1} {operator} {fraction2}"
        solution = evaluate_fraction_problem(numer1, denom1, numer2, denom2, operator)
        
        return problem, solution

    def evaluate_fraction_problem(numer1, denom1, numer2, denom2, operator):
        fraction1 = numer1 / denom1
        fraction2 = numer2 / denom2
        
        if operator == '+':
            result = fraction1 + fraction2
        elif operator == '-':
            result = fraction1 - fraction2
        elif operator == '*':
            result = fraction1 * fraction2
        elif operator == '/':
            result = fraction1 / fraction2
        
        return result
        
    problems = []
    
    for _ in range(num_problems):
        problem, solution = generate_fraction_problem()
        problems.append(problem +" = "+ str( solution))
    
    return problems



from fractions import Fraction


def generate_fraction_problems2(num_problems):
  def generate_fraction_problem(min_value=1, max_value=99):



    def solve_fraction_problem(numerator1, denominator1, numerator2, denominator2):


        # Calculate the solution
        total_numerator = numerator1 * denominator2 + numerator2 * denominator1
        total_denominator = denominator1 * denominator2

        # Simplify the fraction
        fraction = Fraction(total_numerator, total_denominator)
        simplified_numerator = fraction.numerator
        simplified_denominator = fraction.denominator

        # Generate the step-by-step solution
        solution = f"({numerator1} * {denominator2} + {numerator2} * {denominator1})/{denominator1 * denominator2} = "
        solution += f"{total_numerator}/{total_denominator} = "
        solution += f"{simplified_numerator}/{simplified_denominator}"
        if simplified_numerator > simplified_denominator:
            whole_number = simplified_numerator // simplified_denominator
            remainder = simplified_numerator % simplified_denominator
            if remainder == 0:
                solution += f" = {whole_number}"
            else:
                solution += f" = {whole_number} {remainder}/{simplified_denominator}"
        
        return solution

    numerator1 = random.randint(min_value, max_value)
    denominator1 = random.randint(min_value, max_value)
    numerator2 = random.randint(min_value, max_value)
    denominator2 = random.randint(min_value, max_value)

    problem = f"{numerator1}/{denominator1} + {numerator2}/{denominator2}"
    solution = solve_fraction_problem(numerator1, denominator1, numerator2, denominator2)

    return problem+ " = "+ solution
  problems = []
  
  for _ in range(num_problems):
      solution = generate_fraction_problem()
      problems.append(str( solution))
  
  return problems

def generate_fraction_problems3(num_problems):
    from fractions import Fraction
    from random import randint, choice

    OPERATORS = ['+', '-', '*', '/']
    MIN_NUMERATOR = -10
    MAX_NUMERATOR = 10
    MIN_DENOMINATOR = 1
    MAX_DENOMINATOR = 10


    def generate_fraction():
        numerator = randint(MIN_NUMERATOR, MAX_NUMERATOR)
        denominator = randint(MIN_DENOMINATOR, MAX_DENOMINATOR)
        return Fraction(numerator, denominator)


    def generate_fraction_problem(num_terms):
        problem = str(generate_fraction())
        for _ in range(num_terms - 1):
            operator = choice(OPERATORS)
            term = generate_fraction()
            problem += f" {operator} {term}"
        return problem


    def evaluate_fraction_expression(expression):
        terms = expression.split()
        result = Fraction(terms[0])
        intermediate_steps = [str(result)]
        for i in range(1, len(terms), 2):
            operator = terms[i]
            term = Fraction(terms[i + 1])
            if operator == '+':
                result += term
            elif operator == '-':
                result -= term
            elif operator == '*':
                result *= term
            elif operator == '/':
                result /= term
            intermediate_steps.append(f"{operator} {term} = {result}")
        return result, intermediate_steps


    def explain_solution(problem, intermediate_steps, solution):
        explanation = f"Problem: {problem}\n"
        explanation += "Solution:\n"
        i = 1
        for step in intermediate_steps:
            explanation += f"Step {i}: {step}\n"
            i+=1
        explanation += f"\nFinal Solution: {problem} = {solution}"
        return explanation


    def generate_fraction_problems(num_problems, num_terms):
        problems_and_solutions = []
        for _ in range(num_problems):
          try:
            problem = generate_fraction_problem(num_terms)
            solution, intermediate_steps = evaluate_fraction_expression(problem)
            explanation = explain_solution(problem, intermediate_steps, solution)
            problems_and_solutions.append( explanation+ "\n")
          except:
            pass
        return problems_and_solutions

    return generate_fraction_problems(num_problems, randint(3,10))


def generate_fraction_problems4(num_problems):
  import random
  from fractions import Fraction

  def generate_fraction_problem(min_value=1, max_value=9):
      num_fractions = random.randint(2, 20)
      operators = ["+", "-"]
      fractions = []
      for _ in range(num_fractions):
          numerator = random.randint(min_value, max_value)
          denominator = random.randint(min_value, max_value)
          operator = random.choice(operators)
          fractions.append((numerator, denominator, operator))

      problem = f"{fractions[0][0]}/{fractions[0][1]}"
      for fraction in fractions[1:]:
          problem += f" {fraction[2]} {fraction[0]}/{fraction[1]}"

      solution = solve_fraction_problem(fractions)

      return problem + "\n"+solution


  def solve_fraction_problem(fractions):
      total_fraction = Fraction(fractions[0][0], fractions[0][1])
      solution = f"Start with the first fraction {fractions[0][0]}/{fractions[0][1]}.\n"

      for fraction in fractions[1:]:
          numerator, denominator, operator = fraction
          if operator == "+":
              solution += f"\nNext, we add {numerator}/{denominator} to the current total.\n"
              total_fraction += Fraction(numerator, denominator)
          else:
              solution += f"\nNext, we subtract {numerator}/{denominator} from the current total.\n"
              total_fraction -= Fraction(numerator, denominator)
          
          simplified_numerator = total_fraction.numerator
          simplified_denominator = total_fraction.denominator
          solution += f"The intermediate result is: {simplified_numerator}/{simplified_denominator}\n"

      simplified_numerator = total_fraction.numerator
      simplified_denominator = total_fraction.denominator

      solution += f"\nThe final result in fraction form is {simplified_numerator}/{simplified_denominator}. "
      if simplified_numerator > simplified_denominator:
          whole_number = simplified_numerator // simplified_denominator
          remainder = simplified_numerator % simplified_denominator
          if remainder == 0:
              solution += f"This simplifies to the whole number {whole_number}."
          else:
              solution += f"This simplifies to the mixed number {whole_number} {remainder}/{simplified_denominator}."
      
      return solution
  problems = []
  
  for _ in range(num_problems):
      solution = generate_fraction_problem()
      problems.append(str( solution))
  return problems


def sales_commission(n_samples):
    problems = []
    for _ in range(n_samples):
        sales = random.randint(1001, 100000)
        salery = random.randint(1001, 10000)
        gross_pay = salery + (0.02 * (sales - 4000))
        problem = f"Eva work as a sales clerk. She is paid a salary of {salery} a week plus 2% commission on sales over 4000. Find her gross pay for a week in which her sales are {sales}."
        solution = f"Step-by-step solution:\n\nTo calculate Eva's gross pay, we need to add her salary to the commission she earned on sales over 4000.\n\nHer salary is {salery} per week.\n\nHer sales for this week are {sales}.\n\nCommission = 2% of (sales - 4000).\n\nCommission = 0.02 * ({sales} - 4000) = {0.02 * (sales - 4000)}.\n\nTherefore, Eva's gross pay for the week is {gross_pay}.\n\n"
        problems.append(problem + "\n" + solution)
    
    return problems



names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Avery", "Sofia", "Camila", "Aria", "Scarlett"]

template1 = "{} work as a sales clerk. {} is paid a salary of {} a week plus {}% commission on sales over {}. Find {}'s gross pay for a week in which {}'s sales are {}."
template2 = "{} earns a salary of {} a week plus {}% commission on sales greater than {}. If {}'s sales for a week are {}, what is their gross pay?"

def sales_clerk_salary(n_samples):
    problems = []
    for i in range(n_samples):
        name = random.choice(names)
        salary = random.randint(2000, 4000)
        commission = random.randint(1, 5)
        threshold = random.randint(3000, 5000)
        sales = random.randint(threshold + 1, 10000)
        if random.choice([True, False]):
            problem = template1.format(name, name, salary, commission, threshold, name, name, sales)
            solution = "Step-by-Step Solution:\n\n"
            solution += "1) Determine threshold sales:\n"
            solution += "   Threshold sales = {}\n".format(threshold)
            solution += "2) Determine commissionable sales:\n"
            solution += "   Commissionable sales = {} - {} = {}\n".format(sales, threshold, sales - threshold)
            commissionable_sales = sales - threshold
            solution += "3) Determine commission amount:\n"
            solution += "   Commission amount = {}% of {} = {}\n".format(commission, commissionable_sales, commissionable_sales * commission / 100)
            commission_amount = commissionable_sales * commission / 100
            solution += "4) Determine gross pay:\n"
            solution += "   Gross pay = {} + {} = {}\n".format(salary, commission_amount, salary + commission_amount)
            gross_pay = salary + commission_amount
            solution += "5) The gross pay is ${}".format(gross_pay)
        else:
            problem = template2.format(name, salary, commission, threshold, name, sales)
            solution = "Step-by-Step Solution:\n\n"
            solution += "1) Determine commissionable sales:\n"
            solution += "   Commissionable sales = {} - {} = {}\n".format(sales, threshold, sales - threshold)
            commissionable_sales = sales - threshold
            solution += "2) Determine commission amount:\n"
            solution += "   Commission amount = {}% of {} = {}\n".format(commission, commissionable_sales, commissionable_sales * commission / 100)
            commission_amount = commissionable_sales * commission / 100
            solution += "3) Determine gross pay:\n"
            solution += "   Gross pay = {} + {} = {}\n".format(salary, commission_amount, salary + commission_amount)
            gross_pay = salary + commission_amount
            solution += "4) The gross pay is ${}".format(gross_pay)
        problems.append(problem + "\n\n" + solution)
    return problems



def sales_commission2(n_samples):
    problems = []
    for i in range(n_samples):
        name = random.choice(names)
        salary = random.randint(2500, 5000)
        sales_amt = random.randint(5000, 10000)
        commission_rate = random.uniform(0.01, 0.1)

        problem = "{} works as a sales clerk. She is paid a salary of ${} a week plus {}% commission on sales over $4000. Find her gross pay for a week in which her sales are ${}.".format(name, salary, commission_rate*100, sales_amt)
        solution = "Step-by-Step Solution:\n"
        solution += "1. Calculate the commission for sales over $4000.\n"
        if sales_amt > 4000:
            commission = (sales_amt - 4000) * commission_rate
        else:
            commission = 0
        solution += "Commission = (${:,} - $4,000) x {} = ${:,.2f}\n".format(sales_amt, commission_rate, commission)
        solution += "2. Calculate gross pay by adding salary and commission.\n"
        gross_pay = salary + commission
        solution += "Gross Pay = ${:,} + ${:,.2f} = ${:,.2f}".format(salary, commission, gross_pay)

        problems.append(problem + "\n" + solution)

    return problems
import math
def age_problem(n_samples):
    names = ['Asaf', 'Alexander', 'David', 'Sarah', 'Sophie', 'George']
    problems = []
    for i in range(n_samples):
        name1 = random.choice(names)
        names.remove(name1)
        name2 = random.choice(names)
        names.append(name1)
        age_sum = random.randint(100, 150)
        asaf_age = random.randint(25, 45)
        age2 = age_sum -asaf_age
        age_diff = int(math.sqrt((asaf_age -age2)**2))
        asaf_pencils = age_diff*2
        alex_pencils = asaf_pencils + 60
        total_pencils = asaf_pencils + alex_pencils
        problem = f"The age difference between {name1} and {name2}'s age is half the total number of pencils {name1} has. The sum of their ages is {age_sum}, and {name1} is {asaf_age} years old. If {name2} has 60 more pencils than {name1}, calculate the total number of pencils they have together."
        sol1 = f"If the sum of their ages is {age_sum}, and {name1} is {asaf_age} years old, {name2} is {age_sum-asaf_age} years old."
        sol2 = f"The age difference between {name1} and {name2}'s age is {age_sum-asaf_age}-{asaf_age} = {age_diff}."
        sol3 = f"Since the age difference between {name1} and {name2}'s age is half the total number of pencils {name1} has, {name1} has 2*{age_diff} = {asaf_pencils} pencils."
        sol4 = f"If {name2} has 60 more pencils than {name1}, {name2} has {asaf_pencils}+60= {alex_pencils} pencils."
        sol5 = f"Together, they have {asaf_pencils} + {alex_pencils} = {total_pencils} pencils."
        solution = sol1 + "\n" + sol2 + "\n" + sol3 + "\n" + sol4 + "\n" + sol5
        problems.append(problem + "\nSolution: " + solution)
    return problems


def cookie_problem(n_samples):

    names = ["Emma", "Sophia", "Ava", "Mia", "Charlotte", "Amelia", "Olivia", "Harper", "Evelyn", "Abigail"]

    problems = []

    for i in range(n_samples):
        num_adults = random.randint(1, 5)
        num_children = random.randint(2, 8)
        total_cookies = random.randint(10, 2000)

        adult_cookies = round(total_cookies * 1/3, 2)

        remaining_cookies = total_cookies - adult_cookies

        cookies_per_child = round(remaining_cookies / num_children)

        name = random.choice(names)

        problem_str = f"In {name}'s family, there are {num_adults} adults and {num_children} children. In a cookie jar, there are a total of {total_cookies} cookies. If the adults eat 1/3 of the cookies and then gives the rest to the children to divide equally, how many cookies does each child get?"

        solution_str = f"The adults ate 1/3*{total_cookies} = {adult_cookies} cookies.\n"
        solution_str += f"The remaining number of cookies is {total_cookies}-{adult_cookies} = {remaining_cookies} cookies.\n"
        solution_str += f"If the children divided the cookies equally, each child got {remaining_cookies}/{num_children} = {cookies_per_child} cookies."

        problems.append(f"{problem_str} \nSolution: \n{solution_str}")

    return problems
def department_store(n_samples):
    names = ["Sofia", "Emma", "Jackson", "Olivia", "Aiden", "Mia", "Ethan", "Isabella"]
    problems = []
    for i in range(n_samples):
        name = random.choice(names)
        shirt_price = random.randint(1, 100)
        shoe_price = shirt_price + random.randint(2, 600)
        bag_price = (shirt_price * 2 + shoe_price) / 2
        total_price = shirt_price * 2 + shoe_price + bag_price
        problem = f"{name} went to the department store to buy a pair of shoes and 2 shirts. A shirt costs ${shirt_price} while a pair of shoes is ${shoe_price}. If she decides to buy a bag which costs half the total price of the 2 shirts and a pair of shoes, how much will she pay for all those items?"
        steps = [f"Two shirts costs ${shirt_price*2}.",
                 f"The cost of a pair of shoes is ${shoe_price}.",
                 f"The total cost of two shirts and a pair of shoes is ${shirt_price*2 + shoe_price}.",
                 f"The cost of a bag is ${bag_price}.",
                 f"So, {name} paid a total of ${total_price}."]
        solution = "\n".join(steps)
        problems.append(problem + "\nSolution: " + solution)
    return problems
def generate_math_problems(n_samples):
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    problems = []

    for _ in range(n_samples):
        # Randomly select names, quantities, and prices
        name1 = random.choice(names)
        name2 = random.choice(names)
        notebooks1 = round(random.randint(1, 1000), 1)
        notebooks2 = round(random.randint(1, 1000), 1)
        erasers1 = round(random.uniform(1, 5000), 1)
        erasers2 = round(random.uniform(1, 5000), 1)
        total1 = round(random.uniform(100, 5000), 1)
        total2 = round(random.uniform(100, 5000), 1)

        # Create problem description
        problem = f"{name1} bought {notebooks1} notebooks and {erasers1} erasers for ${total1}.\n"
        problem += f"{name2} bought {notebooks2} notebooks and {erasers2} erasers for ${total2}.\n\n"
        problem += "We're trying to figure out how much each notebook and each eraser costs."

        # Create step-by-step solution
        solution = f"Let's solve the problem step by step:\n\n"
        solution += f"Step 1: Set up the equations:\n"
        solution += f"   {notebooks1}n + {erasers1}e = {total1}\n"
        solution += f"   {notebooks2}n + {erasers2}e = {total2}\n\n"
        solution += f"Step 2: Solve the equations simultaneously to find the values of 'n' and 'e'.\n"
        solution += f"   Multiply the first equation by {notebooks2} and the second equation by {notebooks1}:\n"
        solution += f"   {notebooks2 * notebooks1}n + {notebooks2 * erasers1}e = {notebooks2 * total1}\n"
        solution += f"   {notebooks1 * notebooks2}n + {notebooks1 * erasers2}e = {notebooks1 * total2}\n"
        solution += f"   Subtract the second equation from the first equation:\n"
        solution += f"   {notebooks2 * notebooks1 - notebooks1 * notebooks2}n + {notebooks2 * erasers1 - notebooks1 * erasers2}e = {notebooks2 * total1 - notebooks1 * total2}\n"
        solution += f"   Simplify the equation:\n"
        solution += f"   0n + {notebooks2 * erasers1 - notebooks1 * erasers2}e = {notebooks2 * total1 - notebooks1 * total2}\n"
        solution += f"   Solve for 'e':\n"
        solution += f"   e = {(notebooks2 * total1 - notebooks1 * total2) / (notebooks2 * erasers1 - notebooks1 * erasers2)}\n"
        solution += f"   Substitute 'e' into the first equation to find 'n':\n"
        solution += f"   {notebooks1}n + {erasers1} * {(notebooks2 * total1 - notebooks1 * total2) / (notebooks2 * erasers1 - notebooks1 * erasers2)} = {total1}\n"
        solution += f"   Simplify the equation:\n"
        solution += f"   {notebooks1}n + {(erasers1 * (notebooks2 * total1 - notebooks1 * total2)) / (notebooks2 * erasers1 - notebooks1 * erasers2)} = {total1}\n"
        solution += f"   Solve for 'n':\n"
        solution += f"   n = {total1 - (erasers1 * (notebooks2 * total1 - notebooks1 * total2)) / (notebooks2 * erasers1 - notebooks1 * erasers2) }\n\n"
        solution += f"The cost of each notebook and each eraser:\n"
        solution += f"   Cost of each notebook = {total1 - (erasers1 * (notebooks2 * total1 - notebooks1 * total2)) / (notebooks2 * erasers1 - notebooks1 * erasers2) }\n"
        solution += f"   Cost of each eraser = {(notebooks2 * total1 - notebooks1 * total2) / (notebooks2 * erasers1 - notebooks1 * erasers2)} \n"


        problems.append(problem + "\n" + solution)

    return problems


def generate_linear_equations_problems(n_samples):
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Igor', 'Jill']
    problems = []
    for _ in range(n_samples):
        while True: # Loop until we get a valid system of equations
            a1, b1, c1 = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 5000)
            a2, b2, c2 = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 5000)

            try:
                # Try to calculate solutions
                x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
                y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)
                break # Exit loop if no ZeroDivisionError
            except ZeroDivisionError:
                pass # Generate new coefficients if ZeroDivisionError occurs

        name = random.choice(names)

        # System of equations
        equation = f'{a1}x + {b1}y = {c1}\n{a2}x + {b2}y = {c2}'

        # Solution
        x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
        y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)

        problem_templates = [
            f"{name} has two equations that they need to solve:\n{equation}\n",
            f"The following system of linear equations is given to {name}:\n{equation}\n",
            f"{name} is attempting to solve this system of equations:\n{equation}\n"
        ]

        solution_template = f"Step 1: The goal is to make the coefficients of y in both equations the same. " \
            f"This is done by multiplying the entire first equation by {b2} and the entire second equation by {b1}, leading to:\n\n" \
            f"{a1*b2}x + {b1*b2}y = {c1*b2}\n" \
            f"and\n" \
            f"{a2*b1}x + {b2*b1}y = {c2*b1}\n\n" \
            f"Step 2: Now, subtract the second equation from the first. This involves subtracting each corresponding term on both sides. After performing the subtraction, we get:\n\n" \
            f"({a1*b2}-{a2*b1})x + ({b1*b2}-{b2*b1})y = ({c1*b2}-{c2*b1})\n\n" \
            f"Which simplifies to:\n\n" \
            f"x = {x}\n\n" \
            f"Step 3: We now know the value of x, so we substitute x = {x} into the first equation. The first equation becomes:\n\n" \
            f"{a1}*{x} + {b1}y = {c1}\n\n" \
            f"Step 4: Simplify the equation by performing the multiplication {a1}*{x}, which results in:\n\n" \
            f"{a1*x} + {b1}y = {c1}\n\n" \
            f"Then, isolate y by subtracting {a1*x} from both sides. This gives us:\n\n" \
            f"y = {y}\n\n" \
            f"Step 5: Thus, the solution to the system of equations is\n\nx = {x}\nand\ny = {y}."

        problem = random.choice(problem_templates) + "Can you find the values of x and y?\n\n" + solution_template
        problems.append(problem)

    return problems



def generate_fraction_problems5(n_samples):
    from fractions import Fraction

    def generate_fraction_problem(min_value=1, max_value=90000):
        num_fractions = random.randint(2, 5)
        operators = ["+", "-"]
        fractions = []
        for _ in range(num_fractions):
            numerator = random.randint(min_value, max_value)
            denominator = random.randint(min_value, max_value)
            operator = random.choice(operators)
            fractions.append((numerator, denominator, operator))

        problem = f"{fractions[0][0]}/{fractions[0][1]}"
        for fraction in fractions[1:]:
            problem += f" {fraction[2]} {fraction[0]}/{fraction[1]}"

        solution = solve_fraction_problem(fractions)

        return problem, solution


    def solve_fraction_problem(fractions):
        total_fraction = Fraction(fractions[0][0], fractions[0][1])
        solution = f"Step 1: Start with {fractions[0][0]}/{fractions[0][1]}"

        for i, fraction in enumerate(fractions[1:], start=2):
            numerator, denominator, operator = fraction
            if operator == "+":
                total_fraction += Fraction(numerator, denominator)
                solution += f"\nStep {i}: Add {numerator}/{denominator} to the current total. The new total is {total_fraction}."
            else:
                total_fraction -= Fraction(numerator, denominator)
                solution += f"\nStep {i}: Subtract {numerator}/{denominator} from the current total. The new total is {total_fraction}."

        simplified_numerator = total_fraction.numerator
        simplified_denominator = total_fraction.denominator

        solution += f"\n\nFinal Calculation: The simplified total is {simplified_numerator}/{simplified_denominator}"
        if simplified_numerator > simplified_denominator:
            whole_number = simplified_numerator // simplified_denominator
            remainder = simplified_numerator % simplified_denominator
            if remainder == 0:
                solution += f"\nSince the numerator is larger than the denominator, we can simplify this to a whole number: {whole_number}"
            else:
                solution += f"\nSince the numerator is larger than the denominator, we can simplify this to a mixed number: {whole_number} {remainder}/{simplified_denominator}"
        
        return solution

    results = []
    for _ in range(n_samples):

        problem, solution = generate_fraction_problem()
        results.append("Problem: "+problem +"\nSolution: "+ solution)


    return results

def generate_linear_equations_problems2(n_samples):
    import random
    import sympy

    def generate_equation():
        a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        c = random.randint(-1000, 1000)
        d = random.randint(-1000, 1000)
        return a, b, c, d

    def solve_equation(a, b, c, d):
        x = sympy.symbols('x')
        equation = sympy.Eq(a*x + b, c*x + d)
        text = ""
        text += f'Start with the equation: {a}*x + {b} = {c}*x + {d}\n'
        
        if a != c:
            # Combine x terms on one side
            new_a = a - c
            equation = sympy.Eq(new_a*x + b, d)
            text +=f'Step 1: Subtract {c}*x from both sides: ({new_a})*x + {b} = {d}\n'
            
        if b != d:
            # Combine constant terms on one side
            new_d = d - b
            equation = sympy.Eq(new_a*x, new_d)
            text +=f'Step 2: Subtract {b} from both sides: ({new_a})*x = {new_d}\n'
            
        # Simplify x coefficient
        if new_a != 1:
            solution = new_d / new_a
            text += f'Step 3: Divide both sides by {new_a}: x = {solution}\n'
        else:
            solution = new_d
            text += f'Step 3: x is already isolated: x = {solution}\n'
        text += f'\nFinal Equation: x = {solution}\n'
        return text 
    problems=[]
    for _ in range(n_samples):
      a, b, c, d = generate_equation()
      text = solve_equation(a, b, c, d)
      problems.append(text)
    return problems
      





def generate_linear_equations_problems3(n_samples):
    #write a python program that generates a linear equation like this one, 199*x + -9 = -336*x + 981  , then simplyfies it step by step to the form x*m+b = y where m is the slope and b is the y-intersection. The program should then calculate step by step the calculation of m for given values of x, y and b and explain every step.

    import random
    import sympy

    def generate_equation():
        a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        c = random.randint(-1000, 1000)
        d = random.randint(-1000, 1000)
        return a, b, c, d

    def simplify_equation(a, b, c, d):
        x = sympy.symbols('x')
        equation = sympy.Eq(a*x + b, c*x + d)
        text = ""
        text += f'Start with the equation: {a}*x + {b} = {c}*x + {d}\n'

        # Combine x terms on one side
        new_a = a - c
        equation = sympy.Eq(new_a*x, d - b)
        text +=f'Step 1: Subtract {c}*x from both sides and subtract {b} from both sides: {new_a}*x = {d} - {b}\n'
        # Simplify to y = mx + b form
        m = new_a
        new_b = d - b
        equation = sympy.Eq(y, m*x + new_b)
        text +=f'Step 2: Simplify to y = mx + b form: y = {m}*x + {new_b}\n'

        return equation, m, new_b ,text

    def solve_for_slope(x_val, y_val, b_val):
        # y = mx + b --> m = (y - b) / x
        print(f'\nGiven x = {x_val}, y = {y_val}, and b = {b_val}, we solve for m.')
        print('Step 1: Subtract b from both sides: y - b = mx')
        print('Step 2: Divide both sides by x: m = (y - b) / x')
        m_val = (y_val - b_val) / x_val
        print(f'The slope m is: {m_val}')

        return m_val
    problems=[]
    for _ in range(n_samples):
      a, b, c, d = generate_equation()
      y = sympy.symbols('y')
      equation, m, new_b, text = simplify_equation(a, b, c, d)


      

      text+=f'\nFinal Equation: y = {m}*x + {new_b}'

      problems.append(text)
    return problems


def generate_linear_functions(n_samples):
  def generate_value_table():
    def generate_linear_function():
        # Generate random values for y-intercept and slope
        y_intercept = random.uniform(-10, 10)
        slope = random.uniform(-5, 5)
        return y_intercept, slope

    def calculate_y(x, y_intercept, slope):
        # Calculate the y-value for a given x-value
        # Step-by-step explanation:
        text = []
        text.append(f"Calculating y for x = {round(x,4)}")
        text.append(f"y = y_intercept + slope * x")
        text.append(f"y = {round(y_intercept,4)} + {round(slope,4)} * {x}")
        intermediate_step = slope * x
        text.append(f"Intermediate Step: {round(slope,4)} * {x} = {round(intermediate_step,4)}")
        y = y_intercept + intermediate_step
        text.append(f"Final Step: {round(y_intercept,4)} + {round(intermediate_step,4)} = {round(y,4)}")
        text.append("--------------------------------------------------")
        return y, text

    x_start = random.randint(-1000, 1000)
    x_end = x_start + random.randint(0, 1000)
    step_size = random.randint(1, 100)

    y_intercept, slope = generate_linear_function()
    texts = []
    texts.append("Linear function:")
    texts.append("Y-intercept: " + str(round(y_intercept, 4)))
    texts.append("x_start: " + str(x_start))
    texts.append("x_end: " + str(x_end))
    texts.append("step_size: " + str(step_size))
    texts.append("Value table:")
    texts.append("x\t|\ty")
    texts.append("----------------------")
    x = x_start
    while x <= x_end:
        y, explanation = calculate_y(x, y_intercept, slope)
        texts.extend(explanation)
        texts.append(f"{round(x, 4)}\t|\t{round(y, 4)}")
        x += step_size

    return texts



  problems=[]
  for _ in range(n_samples):
 
    output_texts = generate_value_table()
    output_texts = '\n'.join(output_texts)

    problems.append(output_texts)
  return problems





# Generate 1 problem
#problems = generate_linear_functions(1)

# Print the problem
#print(problems[0])





