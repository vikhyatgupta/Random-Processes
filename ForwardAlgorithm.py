val1 = 0
val2 = 0

def calculate_alpha(seq, outcome, pi_s, s_s):
    a = outcome.get(seq[0])
    alpha_s = []
    s = []
    for i in range(0, len(a)):
        s.append(pi_s[i] * a[i])
    alpha_s.append(s)

    for i in range(1, len(seq)):
        p = []
        x = outcome.get(seq[i])
        y = alpha_s[i - 1]
        for j in range(0, len(a)):
            sum_for_alpha = 0
            alpha = 1
            for k in range(0, len(a)):
                sum_for_alpha = sum_for_alpha + y[k] * s_s[j][k]
            alpha = sum_for_alpha * x[j]
            p.append(alpha)
        alpha_s.append(p)

    for i in range(len(alpha_s)):
        print('alpha ' + str(i) + ' ' + str(alpha_s[i]))
    last = alpha_s[-1:]
    final = 0
    for i in range(len(last)):
        sum_of_last = sum(last[i])
        final += sum_of_last
    return final

def Model1():
    seq = '1634163435146254263155264425162341316315564163626514256346263562653614526352615341626352'
    prior_s = [0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0]  #probability to start from a state
    outcome = {'1': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 0.05, 0.05, 0.05, 0.05],
               '2': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 0.125, 0.125, 0.125, 0.125],
               '3': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 0.125, 0.125, 0.125, 0.125],
               '4': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 0.125, 0.125, 0.125, 0.125],
               '5': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 0.125, 0.125, 0.125, 0.125],
               '6': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 0.45, 0.45, 0.45, 0.45]}
    s_s = [[0, 0, 0, 0.75, 0, 0, 0, 0.25],
           [1, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0.25, 0, 0, 0, 0.75],
           [0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0]]
    val1 = calculate_alpha(seq, outcome, prior_s, s_s)
    print('sum of last alpha: ' + str(val1))


def Model2():
    seq = '1634163435146254263155264425162341316315564163626514256346263562653614526352615341626352'
    prior_s = [1]
    outcome = {'1': [1 / 6], '2': [1 / 6], '3': [1 / 6], '4': [1 / 6], '5': [1 / 6], '6': [1 / 6]}
    s_s = [[1]]
    val2 = calculate_alpha(seq, outcome, prior_s, s_s)
    print('sum of last alpha: ' + str(val2))


Model1()
print('---------------------------------------------------------------')
Model2()

if val1 > val2:
    print('Model 1 is better than Model 2')
else:
    print('Model 2 is better than Model 1')
