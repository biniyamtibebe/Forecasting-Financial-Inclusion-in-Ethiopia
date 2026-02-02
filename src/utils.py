import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_enriched_data(file_path='data/processed/enriched_unified.csv'):
    """Load and preprocess enriched data with provenance check."""
    try:
        df = pd.read_csv(file_path)
        df['observation_date'] = pd.to_numeric(df['observation_date'], errors='coerce')
        df['value_numeric'] = pd.to_numeric(df['value_numeric'], errors='coerce')
        print(f"Loaded {len(df)} records with high confidence: {df['confidence'].value_counts().get('high', 0)}")
        return df
    except FileNotFoundError:
        raise ValueError("Enriched data not found – run Task 1 first.")

def plot_trends(df, pillar='ACCESS', save_path='reports/figures/trends.png'):
    """Plot trends with event overlays; business-focused for consortium."""
    obs = df[df['record_type'] == 'observation']
    fig, ax = plt.subplots(figsize=(12,6))
    sns.lineplot(x='observation_date', y='value_numeric', hue='indicator_code', data=obs[obs['pillar'] == pillar], ax=ax)
    events = df[df['record_type'] == 'event']
    for _, e in events.iterrows():
        ax.axvline(e['observation_date'], color='r', ls='--', label=e['indicator'])
    ax.set_title(f'{pillar} Trends with Key Events')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.savefig(save_path)
    plt.close()
    return save_path

def calculate_correlations(df, target_code='ACC_OWNERSHIP'):
    """Compute correlations for drivers analysis."""
    obs = df[df['record_type'] == 'observation']
    pivot = obs.pivot_table(index='observation_date', columns='indicator_code', values='value_numeric')
    corr = pivot.corr()[target_code].dropna().sort_values(ascending=False)
    return corr

# Usage in notebooks: df = load_enriched_data(); plot_trends(df); corrs = calculate_correlations(df)