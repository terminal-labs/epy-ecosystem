from Cython.Build import cythonize

def prep():
    r = cythonize(["changefast/calc.pyx"])
    additons = [
        {"key":"ext_modules", "value": r},
    ]

    return additons
