__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "12.07.2023"
__email__ = "m@hler.eu"
__status__ = "Production"


class RandomNumberGenerator:
    """
    Initializes a RandomNumberGenerator object.

    The RandomNumberGenerator uses the parameters IA, IM, IQ, IR, NTAB, AM, and RNMX
    to generate random numbers based on a seed value.
    """

    def __init__(self):
        self.mIdum = 0
        self.mIy = 0

        self.NTAB = 32
        self.mIv = [0] * self.NTAB  # Initialize mIv with zeros

        self.IA = 16807
        self.IM = 2147483647
        self.IQ = 127773
        self.IR = 2836
        self.NDIV = 1 + (self.IM - 1) // self.NTAB
        self.AM = 1.0 / self.IM
        self.RNMX = 1.0 - 1.2e-7

    def set_seed(self, seed):
        """
        Sets the seed value for the random number generator.

        :param seed: The seed value to initialize the random number generator.
        :type seed: int
        """

        self.mIdum = seed

        if seed >= 0:
            self.mIdum = -seed

        self.mIy = 0

    def random_number(self):
        """
        Generates a random integer using the current seed value.

        :return: A random integer value.
        :rtype: int
        """

        if self.mIdum <= 0 or self.mIy == 0:
            if -self.mIdum < 1:
                self.mIdum = 1
            else:
                self.mIdum = -self.mIdum

            for j in range(self.NTAB + 7, -1, -1):
                k = self.mIdum // self.IQ
                self.mIdum = self.IA * (self.mIdum - k * self.IQ) - self.IR * k

                if self.mIdum < 0:
                    self.mIdum += self.IM

                if j < self.NTAB:
                    self.mIv[j] = self.mIdum

            self.mIy = self.mIv[0]

        k = self.mIdum // self.IQ
        self.mIdum = self.IA * (self.mIdum - k * self.IQ) - self.IR * k

        if self.mIdum < 0:
            self.mIdum += self.IM

        j = self.mIy // self.NDIV
        self.mIy = self.mIv[j]
        self.mIv[j] = self.mIdum

        return self.mIy

    def random_float(self, low, high):
        """
        Generates a random float between the given low and high values.

        :param low: The lower bound of the random float.
        :type low: float
        :param high: The upper bound of the random float.
        :type high: float
        :return: A random float value between low and high (inclusive).
        :rtype: float
        """

        float_val = self.AM * self.random_number()

        if float_val > self.RNMX:
            float_val = self.RNMX

        return (float_val * (high - low)) + low


if __name__ == '__main__':
    exit(1)
