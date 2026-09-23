import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    Res = person.merge(address , on='personId',how='left')

    return Res[['firstName','lastName','city','state']]
    