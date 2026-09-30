# MDPF_SECCLASS decomposition -- ROUND 6 (drafted 2026-09-30 ~18:5xZ, issuer 2.0.0_SA_COO~M, on CTO RULING 103369)

**Status: DECOMPOSED, NOT ISSUED.** The CTO asked for cell 1 to be decomposed now (103369: "Decompose it now; my round-5
analysis carries it verbatim when the CVO's slug lands"). Issuance (L6) follows the CTO's round-5 analysis, in ONE
issuance, per GATE (x). Until then no task order is cut and no worker is spawned.

**Cut on:**
- 1.0.0_SA_CTO RULING 103369 (18:33Z): the BD_THREAD_R2 rollback is the signed half's own branch; the half is spent.
  Round 6 cell 1 ships the shared classifier client inside the gold code the runner syncs (the IRPT closure's
  pattern), covers E_18's identical hop, and proves the import on the runner's deployed flat layout by a real run.
  The redeploy needs a new half. E_18 stays deployed; 2026-10-01 04:00Z is the expected negative control.
- 1.0.0_SA_CTO DECISION 103371 (18:33Z, all laptop issuers): a cell whose diff changes an import in a script that runs
  from a deployed code prefix carries ONE criterion that imports the module from the deployed layout itself (on the
  runner, or on an exact extract of what the deploy ships), printed.
- CUSIP_ROWS CTO half @1f4792c45a condition 5: round 6 carries the `find_by_*` CUSIP filter (the one client and its two
  copies) and the seed scripts' PRE-READ count as cut cells; no caller of `find_by_asset_class` /
  `find_by_sub_asset_class` lands before the filter does.
- Row MDPF_SECCLASS-S5 (BLOCKING): `data/black_diamond/scripts/gold/lib/etf_classifier.py:19` resolves the shared client
  through `parents[5] / infra/aws/lambda/v2_portal/_shared`; E_18 through `parents[4]` (`:54`). The runner has neither.

**Measured constraints (read at the base, 2026-09-30):**
1. The BD gold runner syncs `s3://opal-data-bd/code/gold/` FLAT into `/tmp/gold_layer_scripts/` (bd-gold-trigger header;
   the 17:47Z traceback path). Nothing outside `code/gold/` reaches it.
2. `.tools/safe_deploy_core.py` maps only `data/<tree>/scripts/{gold,silver,bronze}[/lib]/*.py`; `AUX_CODE_PREFIXES["bd"]`
   is `{}`. The one client (`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`) has no deploy path to
   the BD prefix today.
3. PRD C-TABLE: no second client copy is made in the repo. Shipping the client's bytes as a deploy artifact (the way
   `_IRPT_HOLDINGS_CLOSURE` ships it into the Holdings bundle) is not a repo copy.
4. `data/black_diamond/scripts/silver/build_bd_assets_dim.py:56` imports `lib.etf_classifier` via `../gold` -- the silver
   runner's layout is UNMEASURED; the cell measures it before relying on it.

## The cells

| cell | item | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `SC-e-13` | THREAD-BREAKING FIRST. The BD thread imports the one shared client on the runner: (a) a declared deploy mapping in `.tools/safe_deploy_core.py` that ships the client's bytes (and, for E_18, `etf_classification_scheduled.py` plus anything either imports at load) into a sub-directory of `code/gold/` the runner syncs; (b) `lib/etf_classifier.py` and `E_18.detect_new_securities.py` resolve the client from their own deployed directory first and the repo path second, with the module-level `parents[N]` hop removed; (c) the silver builder's runner layout measured and covered; (d) the NEW half (BD_THREAD_R3) covering the redeploy, the ordinary run, the COO's FWD-1 page read for z08327149, and E_18's acceptance at its first scheduled run after the redeploy | FWD-1, FWD-7 (E_18), S5 disarm | NOT-EVALUATED | laptop | WORLD | A, `0.9.0_WK_MDPF_SECCLASS~10` |
| `SC-e-14` | CUSIP_ROWS condition 5: the `find_by_asset_class` / `find_by_sub_asset_class` filter excluding `identifier_namespace == "CUSIP"` in the one client and its two byte-identical copies (`yang-generate-holdings-attribution/`, `yang-generate-positioning/`), and the seed scripts' PRE-READ count excluding `CUSIP:` rows (`seed-etf-classifications.py`, `seed-etf-constituents.py`) | FWD-4 (reader hygiene), CUSIP_ROWS c5 | NOT-EVALUATED | laptop | SERVED | B, `0.9.0_WK_MDPF_SECCLASS~11` |

**By reference, not cut:** `SC-e-12` (W6-S2, shared-infra grant narrowing) stays PARKED on `0.7.0_AE_CloudOps` per CTO
RULING 103327 and re-enters the open round when that seat is live.

## Criteria the cells must carry (drafted; final text at issuance)

**SC-e-13** (at most three mechanical criteria, spine v3.18):
1. The BD thread suite passes in the repo tree (the round-1 thread tests plus a new test that the library resolves the
   client from its own directory when the repo path is absent).
2. **DEPLOYED-LAYOUT IMPORT (CTO 103371):** a check builds an EXACT extract of what `safe-deploy.sh` would upload to
   `code/gold/` (the mapping's own output, read from the tool, not a hand-built list), flattens it into a temp directory
   with NO repo on `sys.path`, and imports `C_06`, `D_03`, `D_04`, `E_18` and `lib.etf_classifier` from there, printing
   one line per module and the resolved client path. The silver builder is imported the same way from its measured
   runner layout.
3. The new half reads HALF-READY.
The real-runner exercise (an ad-hoc QA fire, the scheduled fire the acceptance) is the release act under the new half,
not a worker criterion.

**SC-e-14:**
1. The client suite plus a new test: a CUSIP-namespace row is filtered from both `find_by_*` methods; a ticker row is not.
2. A byte-compare prints the two copies identical to the one client after the edit (the FWD-4 copies stay in lock-step
   until they retire).
3. The two seed scripts' `--dry-run` against the live table print a PRE-READ count that excludes `CUSIP:` rows, with the
   excluded count printed beside it.
Import-path note (CTO 103371): this cell changes no import, so the deployed-layout criterion does not apply; the two
Lambda copies' bundles are unchanged in shape.

## Write sets (disjoint)

- `SC-e-13`: `data/black_diamond/scripts/gold/lib/etf_classifier.py`, `data/black_diamond/scripts/gold/E_18.detect_new_securities.py`,
  `data/black_diamond/scripts/silver/build_bd_assets_dim.py` (only if step (c) finds the silver layout needs it),
  `.tools/safe_deploy_core.py`, the BD thread tests, an R6 check, the BD_THREAD_R3 half, the surprise channel.
- `SC-e-14`: `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`, its two copies, the two seed scripts,
  the client's tests, an R6 check, the surprise channel.
- Ordering: SC-e-14 edits the client's bytes that SC-e-13 ships. Both drain before the redeploy, so the shipped bytes
  are the filtered client. No ordering between the builds.

## Issuer acts carried with round 6 (not cells)

1. W5-S2 drain hygiene: the second schema cites the contract's enum and carries no value of its own (CTO rounds 2-3
   analysis, section 2).
2. The issuance commit states the CTO's deployed-layout rule (103371's one ask).
3. After both drain: the BD_THREAD_R3 window under its new half (redeploy, ad-hoc QA exercise on the runner, the 23:00Z
   or 04:00Z scheduled fire as the acceptance, the FWD-1 page read), and E_18's moved acceptance.

`fanout: 2` (two chains, cap 8), at issuance.
