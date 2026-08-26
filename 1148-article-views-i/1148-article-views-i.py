import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id']==views['viewer_id']]
    #relevant data

    unique = df['author_id'].unique()
    #unique values

    sor = sorted(unique)
    #sorting

    result = pd.DataFrame({'id': sor})

    return result
