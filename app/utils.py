import pandas as pd

def load_data(country):
    file_map = {
        'Benin': 'data/benin-malanville_clean.csv',
        'Sierra Leone': 'data/sierraleone_clean.csv',
        'Togo': 'data/togo-dapaong_qc_clean.csv'
    }
    return pd.read_csv(file_map[country], parse_dates=['Timestamp'])

def get_summary_stats(df):
    return df[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std']).round(2)

def top_regions_table(dfs):
    table = {}
    for name, df in dfs.items():
        table[name] = {
            'Avg GHI': round(df['GHI'].mean(), 2),
            'Avg DNI': round(df['DNI'].mean(), 2),
            'Avg DHI': round(df['DHI'].mean(), 2),
        }
    return pd.DataFrame(table).T
