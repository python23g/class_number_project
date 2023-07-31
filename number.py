class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value % 2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value % 2 == 0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        if self.value < 2:
            return False
        for i in range(2, self.value):
            if self.value % i == 0:
                return False
        
        return True

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        ans = []
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                ans.append(i)
        return ans
                

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(self.get_digits())

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        return sum(self.get_digits())

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(self.value)[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        c = str(self.value)[::-1]
        return c==str(self.value)

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        value = self.value  # 45315 -> 5, 1, 3, 5, 4
        digits = []

        while value != 0:
            d = value % 10  # Get the last digit
            value //= 10  # Remove the last digit

            digits.append(d)  # Add the last digit to the list

        return digits

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max(self.get_digits())
        

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min(self.get_digits())

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        return self.get_sum() / self.get_length()

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        digits = [int(digit) for digit in str(self.value)]  # Extract digits
        sorted_digits = sorted(digits)  # Sort the digits
        length = len(sorted_digits)
    
    # Find the median
        if length % 2 == 0:  # If the length is even
            mid = length // 2  # Find the middle index
            median = (sorted_digits[mid - 1] + sorted_digits[mid]) / 2
        else:  # If the length is odd
            mid = length // 2  # Find the middle index
            median = sorted_digits[mid]
    
        return median

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        return [self.get_min(), self.get_max()]

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        # Convert number to a list of digits
        digits = [int(digit) for digit in str(self.value)]
    
    # Initialize an empty dictionary for frequencies
        frequency_dict = {}
    
    # Count the frequency of each digit using a loop
        for digit in digits:
            if digit in frequency_dict:
                frequency_dict[digit] += 1
            else:
                frequency_dict[digit] = 1
    
        return frequency_dict

# Create a new instance of Number
number = Number(363363)
print(number.get_digits())
# print(number.get_number())
# print(number.is_odd())
# print(number.is_even())
# print(number.is_prime())
# print(number.get_divisors())
# #print(number.get_digits())
# print(number.get_length())
# print(number.get_sum())
# print(number.get_reverse())
# print(number.is_palindrome())
# print(number.get_digits())
# print(number.get_max())
# print(number.get_min())
# print(number.get_average())
# print(number.get_median())
# print(number.get_range())
# print(number.get_frequency())

