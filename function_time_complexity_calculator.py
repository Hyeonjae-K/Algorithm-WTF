import sys
import math
import random
from bigO import BigO


def func_time_comp_cal(code):
    def f(A):
        n = len(A)
        exec(code)

    try:
        return BigO().test_all(f)
    except:
        print(sys.exc_info()[0])
        return False
