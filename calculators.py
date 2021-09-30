import sys
import math
import random
from bigO import BigO
from sympy import Limit, S, Symbol, sympify, sqrt, log, factorial

import global_var


def exps_comp_cal(exps, hash):
    n = Symbol('n')
    try:
        exps = [sympify(exp) for exp in exps.strip().split('\n')]
    except:
        return False
    report = ''
    results = {}

    for a in exps:
        results[str(a)] = 0
        for b in exps:
            if a == b:
                continue
            result = str(Limit(a/b, n, S.Infinity).doit())
            if result == '0':
                results[str(a)] += 1
            report += '%s / %s = %s<br>' % (str(a), str(b), result)
        report += '<br>'

    report += ' < '.join(x[0] for x in sorted(results.items(),
                         key=(lambda x: x[1]), reverse=True))
    global_var.exps_results[hash] = report


def func_time_comp_cal(code):
    def f(A):
        n = len(A)
        exec(code)

    try:
        return BigO().test_all(f)
    except:
        print(sys.exc_info()[0])
        return False
