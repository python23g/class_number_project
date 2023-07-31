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
        return self.value // 2 == 0

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value // 2 == 1

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        return len(self.get_divisors()) == 2

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        divisors = []
        for i in range(1 , self.value +1):
            if self.value % i == 0:
                divisors.append(i)
        return divisors

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        p = str(self.value)
        return len(p)

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        s = str(self.value)
        l = []
        for i in s:
            l.append(int(i))
        return sum(l)

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        s = str(self.value)
        l = ''
        for i in s:
            l = i + l
        l = int(l)
        return l

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        s = str(self.value)
        l = ''
        for i in s:
            l = i + l
        l = int(l)
        return l == self.value

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        l = []
        for i in str(self.value):
            l.append(int(i))

        return l

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        l = []
        for i in str(self.value):
            l.append(int(i))

        max = l[0]

        for i in l:
            if max < int(i):
                max = i
        return max

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        l = []
        for i in str(self.value):
            l.append(int(i))
        min = l[0]

        for i in l:
            if min > i:
                min = i
        return min


    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        s  = str(self.value)
        ave = 0
        for i in s:
            ave += int(i)
        return ave/len(s)

       
    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        s = str(self.value)
        l = []
        for i in s:
            l.append(int(i))
        return l

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(353)
print(number.get_range())