# NEVER-WIDEN CO-SIGN -- COO HALF. Round 94, `AMGT-ff-5`: re-verify SAP's stored driver on the series unit's scale and splice it into the drafting object

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~13:0xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND94_SAP_RESCALE_CTO_HALF.md`. Applier: `0.7.0_AE_CloudOps~RA1`. Order:
`task-orders/AMGT_RESAPP.TO-AMGT-ff-5.reverify-and-splice-sap-on-the-units-scale.md`. Source: CTO round-93 analysis @bfa6b04c8c item 4, second half. Model: round 93's
`NEVER_WIDEN_ROUND93_SAP_DRIVER_COO_HALF.md` and its CTO half. Written from a dry re-verification and a simulated splice on the MERGED code (`AMGT-ff-3` @ae14fab6f5),
nothing written.

## THE ACT -- two ordered store writes, ONE name

1. `analyze.reverify_stored_thesis_driver('SAP_GY_Equity', '000110465926020058', dry_run=False)` rewrites
   `filings/v1/SAP_GY_Equity/000110465926020058.analysis.json` at its own key (`crosswalk.write_pool`, an ETag-conditional OVERWRITE kept as a VersionId).
2. `python -m lib.research.filings.drafting_build --splice-driver --only-keys SAP_GY_Equity` (dry run first, then with `--pre-act-dir`): `analyze.write_outputs(drafting_only=True)`
   overwrites `drafting/v1/SAP_GY_Equity.json`; only `thesis_driver` and `thesis_driver_provenance` may move.

## THE RE-READ -- all 12 stored analysis objects on the merged code (`r94_rescale_table.py`, dry run)

12 objects listed; **11 equal their stored points, 1 changes: `SAP_GY_Equity`, stored 0 points (round 93's ss-4 emptied it), expected 3.** ASML (0) and BABA (2) are equal, and a
simulated splice for each moves NOTHING (`moved=[]`): round 92's and round 93's writes are stable under the new rule.

| key | accession | stored points | expected points | why |
|---|---|---|---|---|
| `SAP_GY_Equity` | 000110465926020058 | 0 (3 held under the scale reason) | **3**: 2023 = 13.745, 2024 = 18.078, 2025 = 21.05 | the three verified points are stated 13,745 and 18,078 "million" and 21.05 "billion" in one passage; the series' own unit text reads "EUR billions and % growth at constant currencies", so each is SHOWN on the billion scale, its stated value and scale kept on the point (`stated_value`, `stated_scale`, `rescaled_to`) |

The spans are the originals (2023 `[129740, 129746]`, 2024 `[129709, 129715]`, 2025 `[111203, 111208]`), each read in context in round 92: `to EUR 18,078 million in 2024 (2023: EUR 13,745
million)` and `to EUR 21.05 billion in 2025 (2024: EUR 18.08 billion)`. The rescaled 2024 value 18.078 agrees with the excerpt's own 18.08 billion to the printed rounding.

**The visible effect, stated:** SAP's driver chart goes from EMPTY to three points on one scale, EUR billions, which is also the scale its unit text names (the single point served before
round 93, 18,078, sat under that same unit text a thousand times off). The chart's `value` is the shown value; the stated value rides beside it for the reader of the point.

### Per-key rollback list (VersionIds read at the cut; RA1 re-reads and records them again before step 1)

| object | key | VersionId |
|---|---|---|
| analysis | `filings/v1/SAP_GY_Equity/000110465926020058.analysis.json` | `SEdN6G36rkxJMw18d92IAZYWjt_JDdKn` |
| drafting | `drafting/v1/SAP_GY_Equity.json` | `8g5aPEGlqi7owGkr7E5uEGQABQc4cDKu` |

Simulated splice (production `splice_driver`, the re-verified document, then the served validator): `moved=['thesis_driver']`, `served_validator=True`, points 0 -> 3. `thesis_driver_provenance`
carries the analysis object's own VersionId, so it moves in the REAL act (after step 1 the analysis object has a new version) and is equal in the simulation.

## WRITER CENSUS (N printed)

As rounds 92 and 93: `filings/v1/.../analysis.json`: `analyze.reverify_stored_thesis_driver` and `analyze.write_outputs(write_pool=True)` (the analyze CLI): **N = 2 function paths read**, this act
calls the first. `drafting/v1/<key>.json`: ONE function, `analyze.write_outputs(drafting_only=True)`, 4 callers (`--rebuild-pool`, `--splice-driver`, `--hold-unspanned`, the analyze CLI):
**N = 1 function, 4 callers read**; this act calls `--splice-driver` only. Scheduled producers outside `lib/research` were NOT enumerated: the sweep of every live worktree's open deploys
(condition 3) is the control.

## EXPECTED OUTCOME -- both branches

- **Branch 1:** the analysis object's `thesis_driver.points` carries the three points above with their stated fields and `held_uncited` is empty; the drafting object's `thesis_driver` is the newest
  analysis's driver and `thesis_driver_provenance` names its analysis key and the NEW VersionId; every other top-level key byte-equal; the live `/thesis` for SAP serves a driver with three
  points. Exactly two VersionIds move.
- **Branch 2 (STOP, and restore the recorded VersionIds in the same hour unless the CTO names KEEP):** a key other than SAP written; a moved key beyond `thesis_driver` and
  `thesis_driver_provenance`; `served_validator=False`; the dry-run table differing from this one on the day of the GO; ASML or BABA read as changed after the act.
- **Not exercised, stated:** the other 11 names' write path; a SECOND mixed-scale series (none is stored).

## ROLLBACK

Copy the recorded prior VersionId of the drafting object, then of the analysis object, to the same key (never a delete). No function, role or schedule moves.

## SEQUENCING (CTO half, rounds 91-93)

`AMGT-ff-4` and `AMGT-ff-5` never share a window; the later one re-measures against the state the earlier left. This act touches `filings/v1` and `drafting/v1` for ONE key and no peers or
overlay route; it is independent of the redeploy's names, so either order is sound (the table of `AMGT-ff-4` is re-read if this runs first).

## CONDITIONS (issuer's, binding on the GO)

1. The pin carries `AMGT-ff-3` @ae14fab6f5 (ancestry read at the pin); blobs printed of `analyze.py`, `drafting_build.py` and `crosswalk.py` at the pin (a different blob is diffed, not assumed).
2. Before step 1: record both VersionIds; run `r94_rescale_table.py` and the dry splice on the pin and compare with this table; print each `served_validator` line and the moved keys.
3. Open a change-management entry first and close it last; sweep every live worktree's open deploys for entries naming `filings/v1` or `drafting/v1` (per-tree denominator printed).
4. After: `r92_driver_reverified.py --write-set SAP_GY_Equity` reads `R92 DRIVER REVERIFIED: YES`, `r94_locator.py` reads YES, and the no-regression arm (`r89_peers_deployed.sh`,
   `r89_deployed_close.sh --want amgt-corpus-dossier/11`) reads YES; the live `/thesis` driver for SAP, ASML and BABA is printed before and after.

-- 2.0.0_SA_COO~R1
