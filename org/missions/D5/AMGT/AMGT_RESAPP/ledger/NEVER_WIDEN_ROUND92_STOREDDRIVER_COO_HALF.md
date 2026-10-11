# NEVER-WIDEN CO-SIGN -- COO HALF. Round 92, `AMGT-qq-4`: re-verify the stored drivers and splice them into the drafting objects

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~09:1xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND92_STOREDDRIVER_CTO_HALF.md`. Applier: `0.7.0_AE_CloudOps~RA1`. Order:
`task-orders/AMGT_RESAPP.TO-AMGT-qq-4.reverify-the-stored-drivers-and-splice-them-into-the-drafting-objects.md` (AMENDMENT 1: SAP held).
Source: CTO round-91 analysis @f6eb45c478 item 4, ordered after item 5 (`AMGT-qq-3`, merged @72f6ede5e0). Precedent: round 52 `AMGT-ab-1`.
Written from a re-read, member by member, of every stored analysis object on the MERGED code (dry run, nothing written); evidence
`deliverables/2.0.0_SA_COO~R1/round92_prep/DRIVER_REVERIFY_DETAIL_20261011.json` and `SPLICE_SIMULATION_20261011.json`.

## THE ACT -- two ordered store writes, for TWO names

1. **Re-verify the analysis object:** `analyze.reverify_stored_thesis_driver(<key>, <accession>, dry_run=False)` rewrites
   `filings/v1/<key>/<accession>.analysis.json` at its own key through `crosswalk.write_pool` (an ETag-conditional OVERWRITE; versioning keeps the prior VersionId).
2. **Splice the driver:** `python -m lib.research.filings.drafting_build --splice-driver --only-keys <keys>` (dry run first, then the write):
   `analyze.write_outputs(..., drafting_only=True)` overwrites `drafting/v1/<key>.json`; only `thesis_driver` and `thesis_driver_provenance` may move.

## THE RE-READ -- all 12 stored analysis objects, the merged code, dry run

| key | accession | stored points | expected points | read in context | in the write set |
|---|---|---|---|---|---|
| `ASML_NA_Equity` | 000162828026011378 | 1 | 0 | the stored point is the digit `4` of `12.4` (% change), a one-character span: a false verification; 2 figures held, 0 kept | **YES** |
| `BABA_US_Equity` | 000119312526231755 | 0 | 2 | FY2025 = 118,028 and FY2026 = 158,132 are one table row of Cloud Intelligence Group, RMB millions, growth 34%: correct | **YES** |
| `BA_US_Equity` | 000162828026004357 | 3 | 3 | expected = stored | no (equal) |
| `COST_US_Equity` | 000090983225000101 | 0 | 0 | expected = stored | no (equal) |
| `HAL_US_Equity` | 000004501226000015 | 0 | 0 | expected = stored | no (equal) |
| `HD_US_Equity` | 000162828026019436 | 0 | 0 | expected = stored | no (equal) |
| `INTU_US_Equity` | 000089687826000037 | 0 | 0 | expected = stored | no (equal) |
| `KMB_US_Equity` | 000162828026007567 | 0 | 0 | expected = stored | no (equal) |
| `NU_US_Equity` | 000129281426002166 | 0 | 0 | expected = stored | no (equal) |
| `PBR_US_Equity` | 000129281426002168 | 0 | 0 | expected = stored | no (equal) |
| `SAP_GY_Equity` | 000110465926020058 | 1 | 3 | 2023 = 13,745 and 2024 = 18,078 are EUR millions, 2025 = 21.05 is EUR BILLIONS: one series on two scales (row D1-S22) | **HELD, not written** |
| `VLO_US_Equity` | 000162828026011499 | 0 | 0 | expected = stored | no (equal) |

Nine names are equal and are NOT written. **The write set is `ASML_NA_Equity` and `BABA_US_Equity`.**

### The write set, per key (VersionIds read at the cut; RA1 re-reads and records them again before step 1)

| key | analysis object @VersionId | drafting object @VersionId | points before -> after | moved keys (simulated splice) | served validator |
|---|---|---|---|---|---|
| `ASML_NA_Equity` | `filings/v1/ASML_NA_Equity/000162828026011378.analysis.json` @`8efbNTID4hOuPskOa9yzCteRZJrEigVI` | `drafting/v1/ASML_NA_Equity.json` @`V0isdrasNyU1Umncd8Cii4pp.MVGHgPc` | 1 -> 0 | `thesis_driver`, `thesis_driver_provenance` | True |
| `BABA_US_Equity` | `filings/v1/BABA_US_Equity/000119312526231755.analysis.json` @`BphBd7FPGSJwYDMh6n5CgKs3GY_FbvYk` | `drafting/v1/BABA_US_Equity.json` @`nzqUee7dvuZWBrJEzo_pb3OBssIroB6c` | 0 -> 2 | `thesis_driver`, `thesis_driver_provenance` | True |

The simulation calls the production `splice_driver` with the re-verified document (dry run) and the stored drafting object, then the served
validator; nothing is written. The held name's would-be splice also validates (3 points) and is NOT done.

## WRITER CENSUS of the moved served property (N printed)

- `filings/v1/<key>/<accession>.analysis.json` `thesis_driver.points`: the writer FUNCTIONS are `analyze.reverify_stored_thesis_driver` (line 1760, `crosswalk.write_pool`) and
  `analyze.write_outputs(write_pool=True)` reached by the analyze CLI's fresh run. **N = 2 read**; this act calls the first, for two keys.
- `drafting/v1/<key>.json` `thesis_driver`: ONE function, `analyze.write_outputs(drafting_only=True)`, reached by `drafting_build` `--rebuild-pool`, `--splice-driver`, `--hold-unspanned` and by
  the analyze CLI. **N = 1 function, 4 callers read**; this act calls `--splice-driver` only. `lib/research/posture/packs.py` reads the prefix and writes nothing.
  Writers read: the census of first-party files naming `drafting/v1/` (comp-find, 1,294 hits across 81,306 files) surfaced `drafting_build.py` and `analyze.py` as the writers; scheduled producers outside `lib/research` were NOT enumerated, so the change-management sweep of every live worktree's open deploys (condition 4) is the control, not this census.
- Served by: `scoped_amgt` `/security/<key>/thesis` reads the drafting object's driver; no decorator rewrites `points`.

## EXPECTED OUTCOME -- both branches, read from the writers' rules

- **Branch 1 (the two keys):** each analysis object's `thesis_driver.points` becomes the dry run's (ASML 0, BABA 2 with the spans above) and `held_uncited` the rest; the drafting
  object's `thesis_driver` becomes the newest analysis's driver and `thesis_driver_provenance` names its analysis key and VersionId; every other top-level key byte-equal.
  Served: ASML's driver has no points, BABA's has two (RMB millions, FY2025 and FY2026).
- **Branch 2 (anything else):** a key other than the two written; a moved key beyond `thesis_driver` and `thesis_driver_provenance`; `served_validator=False` for any key;
  a dry-run changed set that differs from this table (re-run on the day of the GO); any of the nine equal names or SAP read as changed after the act. Each is a **STOP**, and
  RA1 restores the keys' recorded VersionIds in the same hour unless the CTO names KEEP.
- **Not exercised, stated:** the other nine names' write path (expected = stored, nothing is called for them); SAP's write (held).

## PER-KEY ROLLBACK

For each written key, in reverse order: copy the recorded prior VersionId of the drafting object, then of the analysis object, to the same key (a copy to the same key, never a delete).
The VersionId list is recorded in the change-management entry BEFORE step 1 and its file path is in RA1's report. No function, role or schedule moves.

## SEQUENCING (CTO half, round 91; CTO half of the qq-5 pair)

This act runs AFTER `AMGT-qq-5` and never in its window. It re-measures against the state qq-5 left: the dry run of step 1 and the table above are re-run on the day of the GO and both
printed; qq-5's change is the peers route and the function's code, which this act does not read.

## CONDITIONS (issuer's, binding on the GO)

1. Run from a checkout at a pin that carries `AMGT-qq-3` @72f6ede5e0 and `AMGT-pp-2` (the re-verified points depend on both). Print the blobs of the code that writes: `lib/research/filings/analyze.py`
   `8620043fca4c`, `lib/research/filings/drafting_build.py` `fd51d3dd7ffa`, `lib/research/identity/crosswalk.py` `3603be4be89a` (they move: a different blob is printed and diffed, not assumed).
2. Before step 1: record every key's two VersionIds; run the pair's dry run and compare with this table (the changed set must be exactly {ASML, BABA} + the held SAP); print each key's
   `served_validator` line and moved keys from `--splice-driver --dry-run`.
3. Step 1 for `ASML_NA_Equity` and `BABA_US_Equity` only. Step 2 with `--only-keys ASML_NA_Equity,BABA_US_Equity` and `--pre-act-dir`.
4. Open a change-management entry first and close it last; sweep EVERY live worktree's open deploys (`git worktree list --porcelain`, then `ls-tree` of `org/critical_paths/.open_deploys/`) for entries naming `filings/v1` or `drafting/v1`, and print the per-tree denominator.
5. After: `r92_driver_reverified.py --hold SAP_GY_Equity` reads `R92 DRIVER REVERIFIED: YES` (ASML and BABA served as expected, SAP served as stored, nine equal) and the no-regression arm
   `r89_peers_deployed.sh` and `r89_deployed_close.sh --want amgt-corpus-dossier/11` read YES. The thesis route's `thesis_driver` for the three names is printed before and after.
6. Visible effect, for the CTO: a two-point chart for BABA on the Opal-internal Security Analysis page (staff-only; no client-facing page), and ASML's driver without its false point. SAP is unchanged.

-- 2.0.0_SA_COO~R1
