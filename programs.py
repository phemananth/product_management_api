class SamplePrograms:
    @staticmethod
    def reverse_integer():
        num = int(input("Please give a number to reverse: "))
        print("Before reverse your number is: %d" % num)
        rev = int(str(num)[::-1])
        print("After reverse the number:", rev)

    @staticmethod
    def reverse_string():
        word = str(input("Please give a string to reverse: "))
        print("Before reverse your string is: ", word)
        rev = str(word)[::-1]
        print("After reverse the string:", rev)

    @staticmethod
    def armstrong_number():
        num = int(input("Please Enter a Number to check amstrong: "))
        digits = [int(digit) for digit in str(num)]
        count = len(digits)
        armstrong_sum = sum([digit ** count for digit in digits])
        if num == armstrong_sum:
            print(f"Given {num} is an Armstrong number")
        else:
            print(f"Given {num} is not an Armstrong number")

    @staticmethod
    def prime_number():
        n = int(input("Please give a number to check primenumber: "))
        temp = 0
        for i in range(2, n // 2):
            if n % i == 0:
                temp = 1
                break
        if temp == 1:
            print("Given number is not prime")
        else:
            print("Given number is prime")

    @staticmethod
    def fibonacci_iteration():
        n = int(input("Please give a number for the Fibonacci series: "))
        first, second = 0, 1
        print("Fibonacci series is:")
        for i in range(0, n):
            if i <= 1:
                result = i
            else:
                result = first + second
                first, second = second, result
            print(result)

    @staticmethod
    def fibonacci_recursion():
        n = int(input("Please give a number for the Fibonacci series: "))
        def fibonacci(num):
            if num == 0:
                return 0
            elif num == 1:
                return 1
            else:
                return fibonacci(num - 1) + fibonacci(num - 2)

        print("Fibonacci series is:")
        for i in range(0, n):
            print(fibonacci(i))

    @staticmethod
    def palindrome_iteration():
        n = int(input("Please give a number to check palindrome: "))
        reverse, temp = 0, n
        while temp != 0:
            reverse = reverse * 10 + temp % 10
            temp = temp // 10
        if reverse == n:
            print("Number is palindrome")
        else:
            print("Number is not palindrome")

    @staticmethod
    def palindrome_recursion():
        n = int(input("Please give a number to cbeck palindrome: "))
        def reverse(num):
            if num < 10:
                return num
            else:
                return int(str(num % 10) + str(reverse(num // 10)))

        def is_palindrome(num):
            return 1 if num == reverse(num) else 0

        if is_palindrome(n) == 1:
            print("Given number is a palindrome")
        else:
            print("Given number is not a palindrome")

    @staticmethod
    def greatest_among_n_numbers():
        n = int(input("Enter the number of elements need to find greatest: "))
        numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(n)]
        max_number = max(numbers)
        max_indices = [i + 1 for i, num in enumerate(numbers) if num == max_number]
        print(f"The greatest number(s) is/are {', '.join(map(str, max_indices))} with the value {max_number}")

    @staticmethod
    def is_binary():
        num = int(input("Please give a number to check binary: "))
        while num > 0:
            j = num % 10
            if j != 0 and j != 1:
                print("Number is not binary")
                break
            num = num // 10
            if num == 0:
                print("Number is binary")

    @staticmethod
    def swap_two_numbers_without_third_variable():
        x = int(input("Please give first number x: "))
        y = int(input("Please give second number y: "))
        x, y = y, x
        print("After swapping:")
        print("Value of x is:", x)
        print("Value of y is:", y)

    @staticmethod
    def swap_two_numbers_using_third_variable():
        a = int(input("Please give first number a: "))
        b = int(input("Please give second number b: "))
        a, b = b, a
        print("After swapping:")
        print("Value of a is:", a)
        print("Value of b is:", b)

    @staticmethod
    def factorizing():
        def prime_factors(n):
            i = 2
            factors = []
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    factors.append(i)
            if n > 1:
                factors.append(n)
            return factors

        num = int(input("Please enter a number: "))
        print("Prime factors of", num, "are:", prime_factors(num))

    @staticmethod
    def add_two_numbers_without_arithmetic_operator():
        def add_numbers(x, y):
            while y != 0:
                temp = x & y
                x = x ^ y
                y = temp << 1
            return x

        num1, num2 = 10, 15
        sum_result = add_numbers(num1, num2)
        print(f"Sum of {num1} and {num2} is: {sum_result}")

    @staticmethod
    def find_average_number():
        n = int(input("Enter the number of elements: "))
        numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(n)]
        average = sum(numbers) / n
        print(f"The average of the numbers is: {average}")


# Example of using the class and its methods
sample_programs = SamplePrograms()
sample_programs.reverse_integer()
sample_programs.reverse_string()
sample_programs.armstrong_number()
sample_programs.prime_number()
sample_programs.fibonacci_iteration()
sample_programs.fibonacci_recursion()
sample_programs.palindrome_iteration()
sample_programs.palindrome_recursion()
sample_programs.greatest_among_n_numbers()
sample_programs.is_binary()
sample_programs.swap_two_numbers_without_third_variable()
sample_programs.swap_two_numbers_using_third_variable()
sample_programs.factorizing()
sample_programs.add_two_numbers_without_arithmetic_operator()
sample_programs.find_average_number()
