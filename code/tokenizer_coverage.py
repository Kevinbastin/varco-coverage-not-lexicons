"""Tokenizer coverage diagnostic (Table II): unknown-token rate and fertility by script.

Reference implementation written for this release. Words are the whitespace-separated
tokens of the sentence text. A word counts as Sinhala-script if it contains a character
of the Sinhala block, and as Latin-script if it has no Sinhala character but at least one
letter A-Z. On the released corpus it reproduces the unknown-token rates of Table II
(mBERT 98.38% vs 98.37%; XLM-RoBERTa 1.72%) and XLM-RoBERTa's Sinhala-script fertility
(1.98). Other fertility figures differ from Table II (mBERT Sinhala 1.23 vs 1.19, Latin
1.79 vs 1.56; XLM-RoBERTa Latin 1.71 vs 1.49), probably because of how words were
segmented or cleaned in the original computation.

Usage: python3 tokenizer_coverage.py sentence-level-annotation.csv Sentence tokenizer [tokenizer ...]
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
