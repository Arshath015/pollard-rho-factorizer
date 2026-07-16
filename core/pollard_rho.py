class PollardRho:
    @staticmethod
    def factor(n: int) -> list:
        '''Factors the given number using Pollard's rho algorithm.'''
        if n % 2 == 0:
            return [2, n // 2]
        x = 2
        y = 2
        c = 1
        g = 1
        while g == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            g = PollardRho.gcd(abs(x - y), n)
        if g == n:
            return None
        return [g, n // g]
    @staticmethod
    def gcd(a: int, b: int) -> int:
        '''Computes the greatest common divisor of two numbers.'''
        while b:
            a, b = b, a % b
        return a