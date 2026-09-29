"""Reference implementation of the lexicon construction in Section IV of the paper.

The seed list matches Table XVIII. The procedure follows the settings confirmed in the
surviving original script: lower-cased whitespace tokens, words of at least four
characters, one candidate, cutoff 0.82, and a vocabulary taken from the whole corpus.
This file was written for the release; it is not the original run code.
"""
import difflib

SEEDS = {
    'good': 0.7, 'great': 0.9, 'awesome': 0.95, 'amazing': 0.95, 'excellent': 0.9,
    'love': 0.9, 'loved': 0.9, 'like': 0.6, 'best': 0.95, 'better': 0.7,
    'beautiful': 0.85, 'wonderful': 0.9, 'fantastic': 0.9, 'happy': 0.8,
    'hondai': 0.7, 'lassanai': 0.8, 'adarei': 0.9, 'sathutui': 0.8, 'supiri': 0.85,
    'maru': 0.8, 'niyamai': 0.8, 'patta': 0.8, 'subha': 0.7, 'jayawewa': 0.75,
    'bad': -0.7, 'worst': -0.95, 'terrible': -0.9, 'horrible': -0.9, 'hate': -0.9,
    'boring': -0.8, 'waste': -0.85, 'poor': -0.7, 'ugly': -0.8, 'stupid': -0.8,
    'trash': -0.9, 'fail': -0.8, 'disaster': -0.9, 'pathetic': -0.9, 'sucks': -0.85,
    'narakai': -0.8, 'weda': -0.5, 'kana': -0.7, 'hora': -0.8, 'modaya': -0.7,
    'avul': -0.7, 'kalakirima': -0.8, 'palayan': -0.8, 'slow': -0.6, 'scam': -0.9,
}
assert len(SEEDS) == 49

def build_vocab(texts):
    words = set()
    for t in texts:
        words.update(str(t).lower().split())
    return words

def expand(texts, cutoff=0.82):
    """Each new word of at least four characters inherits the polarity of its closest seed."""
    keys, out = list(SEEDS), dict(SEEDS)
    for w in build_vocab(texts) - set(keys):
        if len(w) >= 4:
            m = difflib.get_close_matches(w, keys, n=1, cutoff=cutoff)
            if m:
                out[w] = SEEDS[m[0]]
    return out
