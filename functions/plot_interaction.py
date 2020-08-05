def plot_interaction(col1, col2):
    """
    Plot the regression lines of variables grouped by
    high and low values. Non-parellel lines show 
    interaction of variables.
    
    Parameters:
    col1: pandas Series. Variable to group by.
    col2: pandas Series. Variable to plot by
    """
    sample = X_train.join(y_train, how='outer')
    
    hisample = (sample.loc[sample[col1]
                           >sample[col1].quantile(.66)])
    midsample = (sample.loc[(sample[col1]
                             >=sample[col1].quantile(.33))
                            |(sample[col1]
                              <=sample[col1].quantile(.66))])
    losample = (sample.loc[sample[col1]
                           <sample[col1].quantile(.33)])
    
    fig, axes = plt.subplots(figsize=(6,3))
    sns.regplot(x=col2, y='price', data=hisample, 
                scatter=False, truncate=True,
                label='High Values of {}'.format(col1))
    sns.regplot(x=col2, y='price', data=midsample, 
                scatter=False, truncate=True,
                label='Middle Values of {}'.format(col1))
    sns.regplot(x=col2, y='price', data=losample, 
                scatter=False, 
                label='Low Values of {}'.format(col1))
    plt.title('Interaction of {} and {}'.format(col1, col2))
    plt.legend()
    plt.show();
    print('*********************\n')