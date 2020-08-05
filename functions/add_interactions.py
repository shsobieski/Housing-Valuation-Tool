def add_interactions(interactions, ind_train, ind_test):
    """
    Use forward selection based on lowest MSE to select
    and add most predictive interactions to a new model.
    
    Parameters:
    interactions: list of tuples outputed by find_interaction
    function.
    ind_train: independent variables training data.
    ind_test: independent variables test data.
    
    Returns:
    (new_model, new_x_with_interactions)
    """
    additions = interactions
    X_temp_tr = ind_train.loc[:]
    X_best_tr = ind_train.loc[:]
    X_best_t = ind_test.loc[:]
    scores = []
    baseline = 0
    while additions:
        for inter in additions:
            X_temp_tr[inter[0]
                      +' * '
                      +inter[1]]=(X_temp_tr.loc[:, inter[0]]
                                  *X_temp_tr.loc[:, inter[1]])
            linreg = LinearRegression()
            model = linreg.fit(X_temp_tr, y_train)
            y_pred = model.predict(X_temp_tr)
            score = round(r2_score(y_train, y_pred),5)
            scores.append((score, inter[0], inter[1]))
            best = sorted(scores, reverse=True)[0]
            X_temp_tr = X_best_tr.loc[:]
        scores = []
        if best[0] >= baseline:
            additions.remove(best[1:])
            baseline = best[0]
            X_best_tr[best[1]
                      +' * '
                      +best[2]]=(X_temp_tr.loc[:, best[1]]
                                 * X_temp_tr
                                 .loc[:, best[2]])
            X_best_t[best[1]
                     +' * '
                     +best[2]]=(X_best_t.loc[:, best[1]]
                                *X_best_t.loc[:, best[2]])
            X[best[1]
              +' * '
              +best[2]]=(X.loc[:, best[1]]
                         *X.loc[:, best[2]])
            linreg = LinearRegression()
            model = linreg.fit(X_best_tr, y_train)
            y_pred = model.predict(X_best_tr)
            t_pred = model.predict(X_best_t)
            print('Interaction Added: {} * {}'
                  .format(best[1], best[2]))
            print('Current R^2: {}'
                  .format(best[0]))
            print('Current Test MSE: {}'
                  .format(round(mean_squared_error
                                (y_test, t_pred),5)))
            print('Current MSE Difference: {}\n'
                  .format(round(best[0]
                          -round(mean_squared_error
                                 (y_test, t_pred),5),5)))
        else:
            print('complete')
            break
    linreg = LinearRegression()
    new_model = linreg.fit(X_best_tr, y_train)
    return(new_model, X_best_tr, X_best_t)