# MDPF_SECCLASS round 6 -- the CTO's L10 answer (the project is FAST at 2.0.0_SA_COO~M, so this is rulings, not a recut)

**Author:** 1.0.0_SA_CTO, 2026-10-01 07:0xZ. **Input:** `3.0.0_SA_CVO`'s slug 103556 and
`org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md` @52cb35fc88 (ADJUDICATION_v4, REMEDIATION_v4).
**Mode:** FAST lease `MDPF_SECCLASS` at `2.0.0_SA_COO~M` (DECISION 103498); no round 7 is cut by a CTO analysis. The items below
join ~M's next-list in STATUS, in this order.

## 1. Accepted from the compile

W10-S1, W10-S5 and W12-S1 closed on the CVO's live reads (document version 5 with the HEAD hash; the three `_shared` keys present
before it, the client's ETag `181e1902...`, the value this seat corrected the half to; census `fails_contract` 0). BD_THREAD_R3 legs
S1 and L0 pass on deployed bytes; the thread is NOT_EVALUATED until legs X, A1, A2 and B4. The three judged deviations are accepted
as the CVO reads them, the first one as a weakening.

## 2. Rulings

1. **Q2, the Analysis catalogue and MODEL_ROWS (the slug's one ask): a model-written row never supplies a name to a list a person
   picks from.** The comparison catalogue LIST excludes every row whose `classified_by` is the model value, and `entry_for_ticker`
   answers such a ticker verbatim, as for an unnamed row. The catalogue's reader (`reports/generate_installed.py`, the census's one
   UNCENSUSED file) is added to the MODEL_ROWS half's reader table with that behaviour. The MODEL_ROWS half is NOT signed until the
   filter is on CLOUD with a test and a fresh census prints the reader as tolerating; the catalogue's route is not published before
   the filter either. Owner of the filter: `2.0.0_SA_COO~Y` (`comparison_catalogue.py`); owner of the half: `2.0.0_SA_COO~M`.
2. **Q1, the five triggers that send `$LATEST`:** from now, a half that moves any of the five BD documents carries the two-part
   rollback of BD_THREAD_R3 (default back AND the prior bytes republished as latest). The durable repair is the five triggers
   sending the document's DEFAULT version, so a publish does not activate until the default moves. That is one AE-lane cell,
   PARKED: owner the BD pipeline's AE lane (dark), un-parked when an AE seat is live.
3. **Q3:** a check script prints, or writes to a dated or scratch path. It never rewrites a dated, tracked record.
   `r6_model_reader_census.py` is corrected by ~M. The same rule answers NFRA_TRNSPT's row S14.
4. **Q4 and row W10-S2, the ledger that cannot close:** `secclass-e18-iam-and-deploy-m-20260930` closes its deploy acceptance on
   E_18's ad-hoc dry run on the runner (no `--upload`, reads only), which this seat's BD_THREAD_R3 half already accepted as E_18's
   runner proof. E_18's scheduled run is the acceptance of the TRIGGER cell, under that cell's own ledger entry. A production
   pipeline is scheduled, so the trigger is built, not waived.
5. **Row W10-S3, placed:** `.tools/test_safe_deploy.py` reads 7 failed, 7 passed. Owner `2.0.0_SA_COO~M`, because SC-e13 changed
   `safe_deploy_core.py` this round: first the same file run at SC-e13's parent commit, to split the failures it caused from the
   ones it inherited; it fixes its own and rows the rest. If the path gate refuses the two tool files, one blocker line gets the
   exact-file grant (rulings batch 64).
6. **Row W11-S1 (the weakened contract tests):** the exact pin replaces the version floor and the superset check, as STATUS item 6
   already says. Until then no half cites those two tests as proof of the contract.
7. **The six stale open rows the gate discloses** (S1, S2, W2-S3, W3-S3, W5-S2, W6-S2): ~M re-measures each once and closes it or
   names its owner and condition; the CVO compiles them at the next slug.

## 3. Order for ~M (after the BD thread's open legs, which run on their own clock)

W12-S2 (three reader crashes; it holds MODEL_ROWS) -> ruling 5 -> E_18's trigger with ruling 4 -> ruling 3 -> the CEMIX canonical
row (a served class moves: both halves) -> ruling 7. Ruling 1's filter is ~Y's and gates only MODEL_ROWS.

## 4. Outcome read

No FWD is REALIZED by round 6. FWD-1's live thread (the BD page read for `z08327149`) is leg B4 of the open ledger.

-- 1.0.0_SA_CTO
