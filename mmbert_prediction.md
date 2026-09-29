# Prediction for the held-out backbone mmBERT-base
As reported in Section VIII-F of the paper, two predictions were fixed before training:
1. Overall character-channel gain of +2.5 to +8 macro F1, interval excluding zero.
2. Gain concentrated on Sinhala-script sentences: at least +10 Sinhala-only, at least +5 mixed,
   Latin-only within +/-2.
Both failed. This file restates the predictions for the release; it is not a contemporaneous record.
