"""Tokenizer coverage diagnostic (Table II): unknown-token rate and fertility by script.
Reference implementation written for this release. Small differences from Table II are
possible if the original applied text cleaning before splitting.

Usage: python3 tokenizer_coverage.py data.csv TEXT_COLUMN tokenizer [tokenizer ...]
"""
import re, sys
import pandas as pd
from transformers import AutoTokenizer

SIN = re.compile('[\u0D80-\u0DFF]')
LAT = re.compile('[A-Za-z]')

def coverage(texts, tok_name):
    tok = AutoTokenizer.from_pretrained(tok_name)
    stats = {'Sinhala': [0, 0, 0], 'Latin': [0, 0, 0]}  # words, words containing UNK, pieces
    for t in texts:
        for w in str(t).split():
            key = 'Sinhala' if SIN.search(w) else 'Latin' if LAT.search(w) else None
            if key is None:
                continue
            ids = tok(w, add_special_tokens=False)['input_ids']
            stats[key][0] += 1
            stats[key][1] += int(tok.unk_token_id in ids)
            stats[key][2] += len(ids)
    return stats

if __name__ == '__main__':
    texts = pd.read_csv(sys.argv[1])[sys.argv[2]].dropna().tolist()
    for name in sys.argv[3:]:
        st = coverage(texts, name)
        out = [f'{name:36s}']
        for k in ('Sinhala', 'Latin'):
            n, u, p = st[k]
            out.append(f'{k}: words={n} UNK={100*u/max(n,1):.2f}% pieces/word={p/max(n,1):.2f}')
        print('  '.join(out))
