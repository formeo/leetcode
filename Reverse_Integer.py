class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0       
        reversed_string = str(x)[::-1]

        if reversed_string[-1] == "-":
            reversed_string = "-" + reversed_string[:-1]

        while reversed_string[0] == "0":
            reversed_string = reversed_string[1:]

        if float(reversed_string) >= 2147483648:
            return 0
        elif float(reversed_string) < -2147483648:
            return 0
        else:
            return int(reversed_string)
