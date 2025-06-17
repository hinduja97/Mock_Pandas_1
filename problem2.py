import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers=my_numbers.groupby('num')['num'].count().reset_index(name='counter')
    my_numbers=my_numbers[my_numbers['counter']==1].sort_values(by=['num'],ascending=False)
    if my_numbers.empty:
        return pd.DataFrame([None],columns=['num'])
    return my_numbers[['num']].head(1)
