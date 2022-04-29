from epythonsetuptools.loader import getmode, cfp

def calc():
    epy_calc = getmode(cfp(__file__), "calc", "changefast")
    epy_calc.print_result(23)
