# Coverage, Not Lexicons: code and predictions

Code and per-seed test predictions for "Coverage, Not Lexicons: When Character-Level Modeling Helps Sinhala-English Code-Mixed Sentiment Analysis" (Kattakayam and R).

## Data
Not redistributed here.
- NLPC-UOM Sinhala-English Code-Mixed-Code-Switched Dataset: https://huggingface.co/datasets/NLPC-UOM/Sinhala-English-Code-Mixed-Code-Switched-Dataset. File `sentence-level-annotation.csv`, 13,518 rows, MD5 `f93b2ee27c3f30b738d2f6667f721b71`.
- TamilMixSentiment (Chakravarthi et al., 2020).

## Layout
- `predictions/`: three-class runs on the 2,010-sentence test partition (Tables V, VI, VIII-XV).
- `predictions_4class/`: four-class 85/15 five-fold ensembles, 2,028-sentence test partition (Table VII, "85/15" rows).
- `predictions_4class_matched/`: four-class 80/10/10 single models, seeds 8, 42, 77, 1,352-sentence test partition (Table VII, "80/10/10" rows).
- `code/`: notebooks and scripts (see below).
- `mmbert_prediction.md`, `requirements.txt`, `ENVIRONMENT.md`, `CITATION.cff`.

## File naming
`varco_sinhala_<model>_<config>_s<seed>_test_probs.npy` holds the softmax probabilities on the test partition, averaged over the five fold models of that seed (shape (2010, 3) for three classes). The matching `.json` is the run record. `test_labels_*.npy` are the gold labels.

## Which files back which table
| Table | Files |
| --- | --- |
| V, VI (ablation, XLM-R-base, seeds 42-46) | `predictions/varco_sinhala_xlm-roberta-base_{cls,baseline,char,variant,rdrop,full_wc0.5}_s42..s46` |
| VIII, IX, X, XI, XIV, XV (backbones) | `predictions/varco_sinhala_{LaBSE,xlm-roberta-base,bert-base-multilingual-cased,muril-base-cased,SinBERT-large,mmBERT-base}_{baseline,char}_s42..s44` (XLM-R-base also s45, s46) |
| XII (masking) | `predictions/varco_sinhala_xlm-roberta-base_{baseline,char}_{mask50,crippled}_s42..s46` (`crippled` = all Sinhala-script types masked) |
| XIII (romanization) | `predictions/varco_sinhala_{bert-base-multilingual-cased,muril-base-cased}_baseline_translit_s42..s44` |
| VII (four-class) | `predictions_4class/` and `predictions_4class_matched/` |
| XVI (examples) | derived from the mBERT `baseline` and `char` files above |

Tables III (lexicon tests, earlier recipe) and XVII (Tamil-English control) have no prediction files in this release.

## Reproducing
- `python3 code/verify_tables.py` recomputes the per-seed macro F1 of Table VIII from `predictions/` (needs only numpy).
- Training environment: `requirements.txt` and `ENVIRONMENT.md` (Kaggle, one 16 GB GPU).

## Code
- `code/notebook5abb1466ef.ipynb`: Kaggle notebook from the experiments.
- `code/TAMIL_XLM_ROBERTA MODEL.ipynb`: notebook for the Tamil-English control.
- `code/tokenizer_coverage.py`: reference implementation of the tokenizer-coverage diagnostic (Table II).
- `code/lexicon_reference.py`: reference implementation of the lexicon construction in Section IV: the 49 seeds of Table XVIII and the matching rule. Written for this release from the settings of the original script; it is not the original run code.
- `code/verify_tables.py`: recomputes Table VIII from `predictions/`.

## Note on rounding
Table means are averages of per-seed scores rounded to two decimals, so recomputing from the raw prediction files can differ by 0.01.

## Known gaps
- Table XVII (Tamil-English): prediction files were not retained; the reported values are in the paper.
- Table III (lexicon tests): prediction files are not part of this release.

## Licence
MIT. See `CITATION.cff` for how to cite.
