import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema=cinema[~cinema['description'].str.contains('boring') & cinema['id']%2 ==1].sort_values('rating',ascending=False)
    return cinema
    