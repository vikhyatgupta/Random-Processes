def calculate(seq, outcome, s_s, prior_s):
    for i in range(len(seq)):
        a = outcome.get(seq[i])
        alpha_p = []
        for j in range(len(a)):  # calculating the transition probabilities
            p = []
            b = s_s[j]
            for k in range(len(b)):
                p.append(a[j] * b[k])
            alpha_p.append(p)

        lst = [[] for _ in
                  range(len(alpha_p))]  # multiplying transition probabilities with the maximum delta for each state
        for l in range(len(prior_s)):
            for k in range(len(alpha_p)):
                lst[k].append(prior_s[l] * alpha_p[l][k])

        newPrior_s = []  # get the delta and the sai values for each state
        for m in range(len(lst)):
            index = 0
            maximum = lst[m][0]
            for mn in range(1, len(lst[m])):
                if maximum < lst[m][mn]:
                    maximum = lst[m][mn]
                    index = mn
            states[i].append(index)
            newPrior_s.append(maximum)
        maxim.append(newPrior_s)
        prior_s = newPrior_s

        print('sai index ' + str(i) + str(states[i]))
        print('delta value ' + str(newPrior_s))
        print("-------------------------")

    print('states ' + str((states)))
    print('maximum ' + str(maxim))

    last_max = maxim[-1:][0]  # getting maximum state and the index for the last element of sequence
    f = max(last_max)
    idx = last_max.index(max(last_max))
    print('max at last step ' + str(f) + ' ' + ', Index for the last max ' + str(idx))

    stateOnIndex = []  # getting the sequence
    for t in range(len(states) - 1, -1, -1):
        stateOnIndex.append(states[t][idx])
        idx = states[t][idx]

    stateOnIndex.reverse()
    print('states traversed ' + str(stateOnIndex))


seq = '1634163435146254263155264425162341316315564163626514256346263562653614526352615341626352'
prior_s = [0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0]
outcome = {'1': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 0.05, 0.05, 0.05, 0.05],
           '2': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 0.125, 0.125, 0.125, 0.125],
           '3': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 0.125, 0.125, 0.125, 0.125],
           '4': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 0.125, 0.125, 0.125, 0.125],
           '5': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 0.125, 0.125, 0.125, 0.125],
           '6': [1 / 6, 1 / 6, 1 / 6, 1 / 6, 0.45, 0.45, 0.45, 0.45]}
s_s = [[0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0],
       [0.75, 0, 0, 0, 0.25, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 1],
       [0.25, 0, 0, 0, 0.75, 0, 0, 0]]

states = [[] for _ in range(len(seq))]
maxim = []

calculate(seq, outcome, s_s, prior_s)  #calling the function


