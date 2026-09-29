"""Recompute per-seed macro F1 (Table VIII) from the released predictions."""
import numpy as np, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

def mf1(y, p, K):
    f = []
    for c in range(K):
        tp = ((p == c) & (y == c)).sum(); fp = ((p == c) & (y != c)).sum(); fn = ((p != c) & (y == c)).sum()
        pr = tp / (tp + fp) if tp + fp else 0; rc = tp / (tp + fn) if tp + fn else 0
        f.append(2 * pr * rc / (pr + rc) if pr + rc else 0)
    return 100 * np.mean(f)

def scores(model, cfg, seeds, y):
    return [mf1(y, np.load(f'{ROOT}/predictions/varco_sinhala_{model}_{cfg}_s{s}_test_probs.npy').argmax(1), 3) for s in seeds]

y = np.load(f'{ROOT}/predictions/test_labels_sinhala.npy')
for model, seeds in [('LaBSE', (42, 43, 44)), ('xlm-roberta-base', range(42, 47)),
                     ('bert-base-multilingual-cased', (42, 43, 44)), ('muril-base-cased', (42, 43, 44)),
                     ('SinBERT-large', (42, 43, 44)), ('mmBERT-base', (42, 43, 44))]:
    for cfg in ('baseline', 'char'):
        v = scores(model, cfg, seeds, y)
        print(f'{model:30s} {cfg:9s} {np.mean(v):.2f} +- {np.std(v, ddof=1):.2f}')
