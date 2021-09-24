from sympy import Limit, S, Symbol, sympify, sqrt, log, factorial


def exps_comp_cal(exps):
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
    return report
