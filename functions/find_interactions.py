def find_interactions(n, model, ind_train):
    """
    Returns n most predictive interactions based on low MSE.
    
    Parameters:
    n: int. the number of interactions selected.
    model: LinearRegression() object being tested. 
    ind_train: the independent variables in the training set.
    """
    combos = list(combinations(ind_train.columns, 2))
    print('Testing {} combinations.\n'.format(len(combos)))
    inters = [(0,0,0)]*n
    temp_X = ind_train.loc[:]
    for combo in combos:
        temp_X['interaction']=(ind_train.loc[:, combo[0]]
                               *ind_train.loc[:, combo[1]])
        linreg = LinearRegression()
        model = linreg.fit(temp_X, y_train)
        y_pred = model.predict(temp_X)
        score = round(r2_score(y_train, y_pred),3)
        if score > inters[-1][0]:
            inters.append((score, combo[0], combo[1]))
            inters = sorted(inters, reverse=True)[:n]
    for inter in inters:
        print('R^2 including interaction of {} and {}: {}'
              .format(inter[1], inter[2], inter[0]))
        plot_interaction(inter[1], inter[2])
    fin_inters = [i[1:] for i in inters]
    return fin_inters