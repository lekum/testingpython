class Calculate:
    def add(self, x, y):
        """
        Takes two integers and adds them together to produce the result
         
        >>> c.add(1, 1)
        2

        >>> c.add(25, 125)
        150
        >>> c.add(1.0, 1.0)
        Traceback (most recent call last):
        ....
        TypeError: Invalid type: <class 'float'> and <class 'float'>
        """

        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x),
                                                             type(y),
                                                           )
                           )


if __name__ == '__main__': #pragma: no cover
    import doctest
    doctest.testmod(extraglobs={'c': Calculate()})
