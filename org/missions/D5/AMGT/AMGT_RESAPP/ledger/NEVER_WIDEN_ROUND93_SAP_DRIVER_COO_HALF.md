# NEVER-WIDEN CO-SIGN -- COO HALF. Round 93, `AMGT-ss-4`: re-verify SAP's stored driver under the mixed-scale rule and splice it into the drafting object

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~11:1xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND93_SAP_DRIVER_CTO_HALF.md`. Applier: `0.7.0_AE_CloudOps~RA1`. Order:
`task-orders/AMGT_RESAPP.TO-AMGT-ss-4.reverify-and-splice-sap-under-the-scale-rule.md`. Source: CTO round-92 analysis @1edd8be57d item 2, second half; row `D1-S22`.
Model: round 92's `NEVER_WIDEN_ROUND92_STOREDDRIVER_COO_HALF.md` (and its CTO half @ba7b18c715). Written from a dry re-verification and a simulated splice
on the MERGED code (`AMGT-ss-2` @f79fdc7f28), nothing written.

## THE ACT -- two ordered store writes, ONE name

1. `analyze.reverify_stored_thesis_driver('SAP_GY_Equity', '000110465926020058', dry_run=False)` rewrites
   `filings/v1/SAP_GY_Equity/000110465926020058.analysis.json` at its own key (`crosswalk.write_pool`, an ETag-conditional OVERWRITE kept as a VersionId).
2. `python -m lib.research.filings.drafting_build --splice-driver --only-keys SAP_GY_Equity` (dry run first, then with `--pre-act-dir`): `analyze.write_outputs(drafting_only=True)`
   overwrites `drafting/v1/SAP_GY_Equity.json`; only `thesis_driver` and `thesis_driver_provenance` may move.

## THE RE-READ -- all 12 stored analysis objects on the merged code (`r93_scale_table.py`, dry run)

12 objects listed; **11 equal their stored points, 1 changes: `SAP_GY_Equity`, stored 1 point (2024 = 18,078), expected 0.** ASML (0) and BABA (2) are the values round 92 wrote and
are equal; a simulated splice for each of them moves NOTHING (`moved=[]`), which is the control that round 92's two writes are stable under the new rule.

| key | accession | stored points | expected points | why |
|---|---|---|---|---|
| `SAP_GY_Equity` | 000110465926020058 | 1: 2024 = 18,078 (span 129709-129715) | **0** (3 held as a set) | the three verified points are 13,745 (2023) and 18,078 (2024) stated "million" and 21.05 (2025) stated "billion": one series on two scales; the rule holds the set whole, reason naming `million` and `billion` |

**The visible effect, stated:** SAP's driver chart loses its one point. That point is itself a scale error today (18,078 million under a unit text reading billions), so the page goes from
a mislabelled single point to an empty driver with the held reason. SAP's own 2025 figure (21.05 billion) and 2023-2024 millions are not shown until a later cell rescales a series
whose excerpt states the conversion (the analysis's exception clause, not built in `AMGT-ss-2`).

### Per-key rollback list (VersionIds read at the cut; RA1 re-reads and records them again before step 1)

| object | key | VersionId |
|---|---|---|
| analysis | `filings/v1/SAP_GY_Equity/000110465926020058.analysis.json` | `AWd0Tnoq3G8ZH4eirVrw8cfKKqrUwash` |
| drafting | `drafting/v1/SAP_GY_Equity.json` | `ppUca4bJJDMbWrhpDu178JeH8W2DxYnK` |

Simulated splice (production `splice_driver`, the re-verified document, then the served validator): `moved=['thesis_driver', 'thesis_driver_provenance']`, `served_validator=True`, points 1 -> 0.

## WRITER CENSUS (N printed)

As round 92's half: `filings/v1/.../analysis.json`: `analyze.reverify_stored_thesis_driver` and `analyze.write_outputs(write_pool=True)` (the analyze CLI): **N = 2 function paths read**, this act calls the first.
`drafting/v1/<key>.json`: ONE function, `analyze.write_outputs(drafting_only=True)`, 4 callers (`--rebuild-pool`, `--splice-driver`, `--hold-unspanned`, the analyze CLI): **N = 1 function, 4 callers read**; this act
calls `--splice-driver` only. Scheduled producers outside `lib/research` were NOT enumerated: the sweep of every live worktree's open deploys (condition 3) is the control.

## EXPECTED OUTCOME -- both branches

- **Branch 1:** the analysis object's `thesis_driver.points` is empty and `held_uncited` carries the three points with the scale reason; the drafting object's `thesis_driver` is the newest analysis's driver and
  `thesis_driver_provenance` names its analysis key and VersionId; every other top-level key byte-equal; the live `/thesis` for SAP serves a driver with no points. Exactly two VersionIds move.
- **Branch 2 (STOP, and restore the recorded VersionIds in the same hour unless the CTO names KEEP):** a key other than SAP written; a moved key beyond `thesis_driver` and `thesis_driver_provenance`;
  `served_validator=False`; the dry-run table differing from this one on the day of the GO; ASML or BABA read as changed after the act.

## ROLLBACK

Copy the recorded prior VersionId of the drafting object, then of the analysis object, to the same key (never a delete). No function, role or schedule moves.

## SEQUENCING (CTO half, rounds 91-92)

`AMGT-ss-4`, `AMGT-ss-5` and `AMGT-ss-6` never share a window; the later one re-measures against the state the earlier left. This act touches `filings/v1` and `drafting/v1` for ONE key and no peers object;
it is independent of the universe key and the rebuild, so any order is sound.

## CONDITIONS (issuer's, binding on the GO)

1. The pin carries `AMGT-ss-2` @f79fdc7f28 and `AMGT-qq-3`; blobs printed of `analyze.py`, `drafting_build.py` and `crosswalk.py` at the pin (they move: a different blob is diffed, not assumed).
2. Before step 1: record both VersionIds; run `r93_scale_table.py` and the dry splice on the pin and compare with this table; print each `served_validator` line and the moved keys.
3. Open a change-management entry first and close it last; sweep every live worktree's open deploys for entries naming `filings/v1` or `drafting/v1` (per-tree denominator printed).
4. After: `r92_driver_reverified.py --write-set SAP_GY_Equity` reads `R92 DRIVER REVERIFIED: YES`, and the no-regression arm (`r89_peers_deployed.sh`, `r89_deployed_close.sh --want amgt-corpus-dossier/11`) reads YES;
   the live `/thesis` driver for SAP, ASML and BABA is printed before and after.

-- 2.0.0_SA_COO~R1
