# MDPF_SECCLASS decomposition -- ROUND 10 (2.0.0_SA_COO~M1, dell1, 2026-10-07 ~13:2xZ)

**Status: DECOMPOSED.** The issuer is this seat. Order: 1.0.0_SA_CTO~DELL1 msg 253: "recut round 10 in ONE issuance from section 3. The
thread comes first: a read-only BD pages trace, then the fix of its failing hop. Next are W38-S4 and W38-S6 with SC-e-22. Every worker
face carries the no-install, no-download clause."

**Cut on:**
- PRD v0.14 @9b6348f15e (`org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`), ADMITTED. v0.14 is a contract note only, so
  no half re-opens. Its text: `Cash` is a sub-class of `cash` only.
- The round-9 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_9_20261007.md` @9b6348f15e.
  Section 3 items 1-9 are this round's rectangle, read with the section 2 rulings 2.1-2.6.
- The round-9 drain-end read `deliverables/2.0.0_SA_COO~M1/DRAIN_END_R9_20261007.md` @bed8db3116, and ADJUDICATION_v8 @bfffc520d8.

**State the round starts from (measured this session):**
1. The round branch `coo-m1-secclass-r8` carries 0 shipped files. It is published as `q/dell1/secclass-r8/r6` (90ac5cc3e9).
2. These held branches are on origin and DO NOT MERGE:
   - `q/dell1/secclass-r9-held-32/r1` (b0132b22a8): e42, the a07 switch. Its halves are signed, and TO-DEPLOY-e42 is pending on
     0.7.0_AE_CloudOps~S.
   - `q/dell1/secclass-r9-held-34/r1` (18f721a1e8): e44, the producer input module `canonical_lookup_from_records`.
   - `q/dell1/secclass-r9-held-38/r1` (4cb237fe22): e55 (d06), e56 (the Holdings CUSIP fallback) and e57 (sector out of sub-class).
3. Two rows block the round, both armed and owned by this seat:
   - W38-S4: with e57's module, `is_unresolved_us()` in `new-security-classifier/lambda_function.py` (~:229) treats every US listing as
     unresolved, so 7 of its 24 tests fail.
   - W38-S6: with e56, `multi_asset` leaves `ASSET_CLASS_VALUES`. That fails `test_holdings_snapshot.py:427` and
     `test_holdings_narrowed.py`, and the three `HoldingsSnapshot.schema.json` copies still enumerate it.
4. Rows W31-S1, W34-S1 and W34-S2 apply:
   - W31-S1: E_18 (BD and COT) hands `plan_rows` only keys absent from the old list. Its only lookup is the old list, so
     `e18-scheduled` writes 0.
   - W34-S2: no shipped caller passes `canonical_lookup`.
   - W34-S1: `rivalfunds_classification.py` is not one of the push gate's three `lib/_shared` members (`.tools/safe_deploy_core.py`).
5. CASH: a canonical row reads `fixed_income/UltraShortDuration`. Its seed source is
   `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py` (`build_row("CASH", ..., "Fixed Income", "Ultra Short Duration")`;
   tests `test_seed_fields.py:131`, `test_classified_by_v2.py:269`).
6. C-S13 (CTO msg 219): the served 49F mix is `opal-data-bd platinum/firm/mix_summary.json`, D_04's key. Its file is
   `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`. The close condition: the served file sums to 1.0.
7. dell1's principal is denied the firm buckets (W25-S1), so held sets and served bytes read from dell1 are `inferred` (item 9).

## Rule 24 record

- **Domain (declared):** section 3 items 1-9, every step of each.
- **(i) MECE by subtraction.** The denominator is 9 items with 22 steps. Each step is placed once, as one of:
  - a cell: 7 cells, SC-e-58 to SC-e-64;
  - an issuer act;
  - a deferred cell: SC-e-45 and SC-e-46 are re-cut at round 11 when their issuer acts land;
  - a carried environment item (item 9).
- **(ii) Same grain.** One cell is one write set, served by one worker in one worktree. Uploads, table writes, applies and model calls are
  issuer acts under their own pairs.
- **(iii) Intent coherence.** One intent per cell. W34-S1's fourth shipped member rides SC-e-63, because its one purpose is to let the
  E_18 caller import the lookup at run time.
- **(iv) State coherence -- what a remedy does not move.**
  - The trace (SC-e-58) changes no byte.
  - A re-keyed gate (SC-e-61) does not land e57; e57's pair does.
  - A seed-source fix (SC-e-64) does not rewrite the live CASH row; its pair's write does.
  - An E_18 caller (SC-e-63) writes nothing until it is deployed and runs.

## The cells

| cell | item | what | serves | base | risk | depends on |
|---|---|---|---|---|---|---|
| `SC-e-58` | 1 | Read-only trace of the BD pages journey, hop by hop: page, API, platinum key, gold producer (D_03/D_04), silver dim, classifier library, canonical source. Each hop is graded PASS / FAIL / UNREAD with its evidence. The ONE first failing hop is named, with the file and line a fix would change. GLD, PHYS and VXX are read on each hop. | FWD-1 | round HEAD | LOCAL | -- |
| `SC-e-59` | 1 | The fix of the failing hop SC-e-58 names, when that hop is a code hop in `etf_classifier.py`, `build_bd_assets_dim.py` or `D_03.composition_artifacts.py`. GLD/PHYS read commodities and VXX reads hedge at that hop, against SC-e-58's fixture. Any other hop: the worker files a row and stops; the issuer recuts. | FWD-1 | round HEAD (after SC-e-58) | SERVED | `SC-e-58` |
| `SC-e-60` | 7 | C-S13: D_04 serves the residual as its own `Unclassified` line, so `mix_summary.json`'s top-level mix sums to 1.0. If D_04 already writes no residual, a test-only cell that shows it. Yields to the thread: if SC-e-58 names D_04 as the failing hop, the fix lands here. | FWD-13, FWD-1 | round HEAD (after SC-e-59) | SERVED | `SC-e-58` |
| `SC-e-61` | 2 | W38-S4: re-key `is_unresolved_us()` off `sub_asset_class`. A bare-ticker US listing that the module resolved is not unresolved. A new test: a new US stock with no sub-class and a resolved `gics_sector` is planned and written. The producer's 24 existing tests pass over e57's module. | FWD-10 | held-38 (4cb237fe22) | WORLD (infra floor) | -- |
| `SC-e-62` | 3 | W38-S6 + SC-e-22: `multi_asset` leaves the three `HoldingsSnapshot.schema.json` class enums, which then read equal; a CHANGELOG entry; the two Holdings tests encode the six-class rule. Laptop CTO review before DEV or release (2.3). | FWD-2, FWD-13, FWD-16 | held-38 (4cb237fe22) | WORLD (infra floor) | -- |
| `SC-e-63` | 4 | W31-S1 + W34-S1: E_18 (BD and COT) passes `canonical_lookup` (from `canonical_lookup_from_records`, e44's module) to `plan_rows`, so a first-held key can be planned from the canonical leg. `rivalfunds_classification.py` becomes the fourth shipped `lib/_shared` member in `.tools/safe_deploy_core.py`. A dry run on a fixture plans more than 0 canonical rows. | FWD-5, FWD-7 | held-34 (18f721a1e8) | WORLD | -- |
| `SC-e-64` | 6 | 2.4: the constituents seeder maps `CASH` to `cash`/`Cash`, never `fixed_income`. The contract's `fixed_income` list carries no `Cash`; `cash` carries it. Tests are updated (`test_seed_fields.py`, `test_classified_by_v2.py`), with the contract pin. | FWD-17, FWD-2 | round HEAD | WORLD (infra floor) | -- |

7 cells. All are placed on dell1.

## Write sets (disjoint; `M/` = `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/`, `R12/` = `M/R12_CHECKS/`)

- **SC-e-58:** `M/BD_PAGES_THREAD_TRACE_20261007.md`; `M/BD_PAGES_THREAD_TRACE_20261007.json`.
- **SC-e-59:** `data/black_diamond/scripts/gold/lib/etf_classifier.py`; `data/black_diamond/scripts/silver/build_bd_assets_dim.py`;
  `data/black_diamond/scripts/gold/D_03.composition_artifacts.py`; new tests `data/black_diamond/scripts/gold/tests/test_thread_hop_fix.py`.
- **SC-e-60:** `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`; `data/black_diamond/scripts/gold/tests/test_d04_unclassified_line.py`;
  `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D04_UNCLASSIFIED_20261007.md`.
- **SC-e-61:** `infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py`; `.../new-security-classifier/tests/test_new_security_classifier.py`.
- **SC-e-62:** `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`; `infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json`;
  `infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json`; `infra/aws/terraform/investor-reporting/CHANGELOG.json`;
  `data/assets/scripts/gold/investor_reporting/tests/test_holdings_snapshot.py`; `data/assets/scripts/gold/investor_reporting/tests/test_holdings_narrowed.py`.
- **SC-e-63:** `data/black_diamond/scripts/gold/E_18.detect_new_securities.py`; `data/cot/scripts/gold/E_18.detect_new_securities.py`;
  `data/cot/scripts/gold/tests/test_e18_scheduled_caller.py`; `data/black_diamond/scripts/gold/tests/test_e18_canonical_caller.py`; `.tools/safe_deploy_core.py`.
- **SC-e-64:** `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py`; `org/standards/MDPF_SECCLASS_CONTRACT.json`;
  `infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py`; `infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py`.
- Every cell may append its own rows to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.

## Dependency edges

- `SC-e-58` -> `SC-e-59` and `SC-e-58` -> `SC-e-60`: the trace names the hop, and the thread's files yield to it (2.1). One worker's queue.
- Independent: `SC-e-61`, `SC-e-62`, `SC-e-63`, `SC-e-64`.

**Chains:** A {58 -> 59, 60}; B {61}; C {62}; D {63}; E {64}. M = 5. First wave: 58, 61, 62, 63, 64. Fan-out 5 of 5, cap 8.
**Drains:**
- A and E: to the round branch. SC-e-59 and SC-e-60 touch BD gold, a shipped tree, so their merges go to a held branch until their
  halves sign.
- B and C: to `secclass-r9-held-38` r2.
- D: to `secclass-r9-held-34` r2.

## Outcome coverage (denominator 17)

| outcome | this round | carried or deferred |
|---|---|---|
| FWD-1 | `SC-e-58`, `SC-e-59`, `SC-e-60` | -- |
| FWD-2 | `SC-e-62`, `SC-e-64` | e42 deploy (issuer act) |
| FWD-3, FWD-4, FWD-8, FWD-9 | -- | as round 9 |
| FWD-5 | `SC-e-63` | e44 deploy, "producer live", then SC-e-45 at round 11; the delete is Andrew's |
| FWD-6 | -- | SC-e-46 at round 11 (after the sector writer's apply and write) |
| FWD-7 | `SC-e-63` | -- |
| FWD-10 | `SC-e-61` | e57's release under its pair (issuer act) |
| FWD-11, FWD-15 | -- | e49 AI run under its pair (issuer act) |
| FWD-12 | -- | sector writer apply (laptop cloud-ops `safe-apply`) and the sector write (issuer acts) |
| FWD-13 | `SC-e-60`, `SC-e-62` | e55 and e56 releases (issuer acts; e56 through IRPT_BCKEND) |
| FWD-14 | -- | e48 clean-name write under its pair |
| FWD-16 | `SC-e-62` | -- |
| FWD-17 | `SC-e-64` | e32/e50 reclassification write and the CASH row write under their pairs |

## Issuer acts (not cells)

- Halves and releases: e57 (after SC-e-61), e56 via IRPT_BCKEND (after SC-e-62 and the laptop review), e44 deploy (after SC-e-63) with
  a "producer live" run, e55, e48, e49, e32/e50, and the CASH row write (after SC-e-64). Each has its own never-widen pair and ledger.
- TO-DEPLOY-e42: the deploy runs on 0.7.0_AE_CloudOps~S. This seat reads the post-run leg.
- TO-DEPLOY-e21: the flip is ~S's, placed with this seat's instance (90ac5cc3e9, MSTR msg 257).
- The E_18 next-run read (SC-e-21 condition 3, BD 23:00Z).
- Item 9: the read-only fence join (NFRA_CTLPLN ~C).

## Battery

- `comp-schedule`: the R9 read stands (no armed gate for this serial). The BD 23:00Z run is the timing input for any BD gold release.
- `comp-iam`: SC-e-63 names the role E_18 runs under (`bd-exporter-ec2-role`, which already allows Scan on `etf-classifications`
  per TO-DEPLOY-e42's preflight).
- `comp-adversary`, for every face:
  - an install or download (refused, 2.5);
  - a worker that sees a firm bucket deny and guesses served bytes (graded `inferred`, row filed);
  - a trace that stops at the first plausible hop (each hop is graded, UNREAD is a value).

## Not read at this cut

- Which hop fails. SC-e-58 measures it.
- Whether D_04 already writes the residual. SC-e-60's first step reads it.
- Whether a BD E_18 test file exists. SC-e-63 creates `test_e18_canonical_caller.py`.
