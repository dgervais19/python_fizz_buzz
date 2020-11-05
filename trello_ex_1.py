# create a parent class that has functions needed for list to 100 being outputted

class FizzBuzz:
    def __init__(self, Fizz, Buzz):
        self.Fizz = Fizz
        self.Buzz = Buzz
        self.FizzBuzz = Fizz * Buzz

    # create function that takes an empty list, and appends 1-100 with fizz and buzz accordingly (Check README)
    def fizz_buzz(self):
        num_list = []
        for num in range(1,101):
            if num % self.FizzBuzz == 0:
                num_list.append("FizzBuzz")
            elif num % self.Fizz == 0:
                num_list.append("Fizz")
            elif num % self.Buzz == 0:
                num_list.append("Buzz")
            else:
                num_list.append(num)
        return num_list

three_five = FizzBuzz(3, 5)
print(three_five.fizz_buzz())

