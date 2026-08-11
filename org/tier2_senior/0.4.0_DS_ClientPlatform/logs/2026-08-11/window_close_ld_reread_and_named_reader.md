# Window close delta: L-D re-read PASS, named-reader discharge, WINDOW CLOSED @d45823dea5 — 0.4.0_DS_ClientPlatform

**archetype:** VALIDATE

**Date:** 2026-08-11 (~0330-0345Z; delta since @f3b2e9772f)
**Status:** MDPF atomic window 20260811T0150Z CLOSED @d45823dea5. Seat idle for the night per COO
033939Z; 13:30Z bar unattended by design; C-2/C-3 producer-fix TOs expected post-bar-adjudication.

## Delta

1. **AE landed L-D-canonical (033331Z):** function now runtime-pulls from
   s3://opal-data-assets/portal/gold/mdpf/_code/ with env stamp MDPF_GOLD_COMMIT=bf74d031c1 (full
   hash live-verified); live CodeSha256 t0w3vTNV0CpImT1EqzIdtVhUZlkwNzCrx3zA0zpM8/c= (CHANGED from
   XuLlClWT... — the loader swap; AE's "unchanged-by-design" is the FUTURE env-stamp-only property,
   precision-noted to all three seats), LastModified 03:29:24Z.
2. **Item-2 re-read on the re-fire (033045-033146Z run, 12/12 green): PASS at label grain, every
   oracle point.** custody[08-07]=209,373,343.50; model_aua[08-07]=145,329,103.38;
   custody[08-04]=209,431,383.43 (D-4 anchor at true Tuesday); old mislabel value 208,325,960.35 at
   EXACTLY ONE label (2026-08-06, its true day — full 441-vector search, not anchors only);
   label 08-05=None (orion gap at TRUE label = the landed-code discriminator); sv truthful;
   aum-metrics tie the timeseries to the cent. Validated + WINDOW CLOSED @d45823dea5.
3. **Named-reader (COO 033542Z, ledger @588bb50018): discharged at glance grain by COO 033939Z;
   deep read deliberately NOT commissioned** (belongs to CTO causation thread, CRO~A @562cbd444d).
   My deeper read completed in the crossing and was BANKED as evidence, not a thread:
   build_cottonwood_mdpf_slice.py:257-318 (pin==HEAD) — earliest-wins provably correct (ascending
   assignment_date sort, group[0] chosen); every collision reaches the report by construction;
   re-fire census COMPLETE (13 partitions, exactly 2 value_dates with 2 partitions each, both
   reported); 08-06 DIFFERING case carries grounded vendor-re-labelling cause (:296-300); 08-07
   collision is the benign equal-dollar shape (asserted-equal 140,029,264.18). Zero discrepancies.
   Instrument boundary stated honestly to CTO: an in-band report surfaces deltas, it cannot itself
   distinguish vendor restatement from corrupted second write.
4. **Residue flags recorded @d45823dea5 (CTO routing, post-window):** (a) TWO live code channels for
   mdpf gold — s3://opal-data-mdpf/code/scripts/gold/ (runner) vs
   s3://opal-data-assets/portal/gold/mdpf/_code/ (lambda) — comp-pipescript deployed covers only the
   first; measured live: the rekey module exists ONLY on the newer channel. (b) Rule-17b grammar:
   executable code under a portal/gold serving prefix.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find "value_date_rekey" data/mdpf` | PASS (honest zero) | measured 0/57 with denominator — implementation lives in SHARED data/assets tree, found via git grep at the pin (comp-find is working-tree-only; vintage search is its coverage gap) |

(Windowed reads otherwise rode Read/python over the machine-local QA response + live aws primitives
per Rule 22a — rail-checked markers on each; no code/infra change this delta.)

## Next Steps

1. [2.0.0_SA_COO] adjudicates the 13:30Z bar (unattended); C-2/C-3 producer-fix TOs to follow.
2. [1.0.0_SA_CTO] routes the two-code-channel residue + owns the cottonwood causation thread (my
   source-cited evidence delivered 034120Z).
3. This seat: idle until morning TOs or bar-adjudication fallout.
