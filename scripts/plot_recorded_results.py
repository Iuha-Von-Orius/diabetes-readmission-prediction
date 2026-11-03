"""Plot archived result CSVs without fitting models or modifying their values."""
from pathlib import Path
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})

def read_rows(name):
    with (ROOT / 'results' / name).open() as stream:
        return list(csv.DictReader(stream))


def main():
    # Full-dataset class counts verified against the included CSV.
    fig, ax = plt.subplots(figsize=(7, 4.5), constrained_layout=True)
    bars = ax.bar(['No recorded readmission', 'Recorded readmission'], [54864, 46902],
                  color=['#2878a3', '#e09e32'])
    ax.bar_label(bars, fmt='%d', padding=4)
    ax.set_ylim(0, 65000)
    ax.set_ylabel('Hospital encounters')
    ax.set_title('Binary outcome distribution', loc='left', weight='bold')
    fig.savefig(ROOT / 'figures' / 'target_distribution.png', dpi=180)
    plt.close(fig)

    rows = read_rows('model_comparison.csv')
    positions = np.arange(len(rows))
    fig, ax = plt.subplots(figsize=(9, 4.8), constrained_layout=True)
    for offset, key, label, color in [(-0.19, 'test_f1', 'Held-out F1', '#2878a3'),
                                      (0.19, 'test_roc_auc', 'Held-out ROC-AUC', '#e09e32')]:
        values = [float(row[key]) for row in rows]
        bars = ax.bar(positions + offset, values, width=0.36, label=label, color=color)
        ax.bar_label(bars, fmt='%.3f', padding=4, fontsize=10)
    ax.set_xticks(positions, [row['model'] for row in rows])
    ax.set_ylim(0, 0.82)
    ax.set_ylabel('Score')
    ax.set_title('Recorded model comparison', loc='left', weight='bold')
    ax.legend(loc='upper left', frameon=False, ncol=2)
    fig.savefig(ROOT / 'figures' / 'model_comparison.png', dpi=180)
    plt.close(fig)

    rows = read_rows('feature_selection.csv')
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), constrained_layout=True,
                             gridspec_kw={'width_ratios': [1.6, 1]})
    metrics = ['precision', 'recall', 'f1', 'roc_auc']
    positions = np.arange(len(metrics))
    colors = ['#2878a3', '#e09e32']
    labels = ['Random forest', 'With feature selection']
    for i, row in enumerate(rows):
        values = [float(row[f'bootstrap_test_{metric}_mean']) for metric in metrics]
        errors = [float(row[f'bootstrap_test_{metric}_std']) for metric in metrics]
        axes[0].bar(positions + (i - 0.5) * 0.36, values, width=0.34,
                    yerr=errors, capsize=3, label=labels[i], color=colors[i])
    axes[0].set_xticks(positions, ['Precision', 'Recall', 'F1', 'ROC-AUC'])
    axes[0].set_ylim(0, 0.84)
    axes[0].set_ylabel('Bootstrap mean score ± SD')
    axes[0].legend(loc='upper left', frameon=False, fontsize=9)
    axes[0].set_title('Recorded test estimates', loc='left', weight='bold')
    bars = axes[1].bar(['Before\nselection', 'After\nselection'],
                       [int(row['encoded_features']) for row in rows], color=colors)
    axes[1].bar_label(bars, padding=4)
    axes[1].set_ylim(0, 165)
    axes[1].set_ylabel('Encoded predictors')
    axes[1].set_title('139 → 25 features', loc='left', weight='bold')
    fig.savefig(ROOT / 'figures' / 'feature_selection_comparison.png', dpi=180)
    plt.close(fig)


if __name__ == '__main__':
    main()
