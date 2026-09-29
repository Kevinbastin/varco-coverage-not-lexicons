
## Layout of prediction folders
- `predictions/` — three-class runs (2,010-sentence test partition): Tables V, VI and VIII-XV.
- `predictions_4class/` — four-class 85/15 five-fold ensembles (2,028-sentence test partition): Table VII, "85/15" rows.
- `predictions_4class_matched/` — four-class 80/10/10 single models, seeds 8, 42, 77 (1,352-sentence test partition): Table VII, "80/10/10" rows.

## Note on rounding
Table means are averages of per-seed scores rounded to two decimals, so recomputing from the raw prediction files can differ by 0.01.

## Known gaps in this release
- Table XVII (Tamil-English control): prediction files were not retained; the reported values are in the paper.
- Table III (lexicon tests, earlier recipe): prediction files are not part of this release.
