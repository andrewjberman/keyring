# NFRA_SCHWABBF decomposition -- ROUND 1 (2026-10-20, issuer 2.0.0_SA_COO~SB)

Cut on the ratified PRD `org/missions/D8/NFRA/NFRA_SCHWABBF/prd/NFRA_SCHWABBF_PRD.md` v0.1 @ebad019c12, ADMITTED (ratified-text half
`3.0.0_SA_CVO` @ed7d0dc3db, review `org/tier1_exec/3.0.0_SA_CVO/deliverables/L4R_REVIEW_NFRA_SCHWABBF_v0.1_RATIFIED_TEXT_20261020.md`; brief half
auto, the CRO wrote the brief). Notifier `1.0.0_SA_CTO` msg 109892 (READ-acked). Seating ask: `1.0.0_SA_CTO` msg 109890 via MSTR msg 109891.

**Round 1 is the FWD-1 thread** (PRD: "key-form change, the move dry run, the cutover with the old-key delete held for Andrew, then 0840's
oldest day"). The thread, hop by hop: (1) the key grammar in the builder's form; (2) the writer lands a day there; (3) every stored object is
moved there and every reader follows; (4) Schwab's oldest 0840 day is pulled into it; (5) the existing event path converts it; (6) an analyst
reads the balances. Cells build hops 1-3 and the read of hop 6 plus the equality instrument; hops 4-5 and the cutover itself are RELEASE ACTS
(below), because a worker holds no AWS write and no Schwab session.

**Andrew-direct words carried into every face that touches them (verbatim, records cited):**
- "we need to start pulling all of these and also getting as much backfill as we can from them. Furthermore, we need full backfill from the
  0840 account as well if we have not already done so. When we begin pulling these, they should be organized in the opal-data-assets bucket in
  canonical LGIC_NAMING path form" (2026-10-19 ~21:0xZ, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_210xZ_SCHWAB_COTTONWOOD_MASTERS_PULL_AND_BACKFILL.md`).
- "1.) Yes as written. 2.) Yes, rec is accurate. 3.) We don't care about these at this time." (2026-10-20 ~13:0xZ,
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_130xZ_NFRA_SCHWABBF_DONE_WHEN_CONFIRMED_PATH_MOVE_YES_210_MASTERS_OUT.md`).
  Call 2 is the move: one cutover, same-day rollback, no side-by-side copy. Call 3: the other 210 masters are out of scope.

## The rectangle (round 1)

| cell | hop / item | PRD rows | outcome | status | placement | risk | worker_class | depends on (observed completion) |
|---|---|---|---|---|---|---|---|---|
| `BF-k-1` | hop 1: the shared key function in the builder's form, both mirrors, and the partition-listing helpers that read it | C-KEYFORM, C-NAMES | FWD-1, FWD-4 | NOT-EVALUATED | laptop | LOCAL | worker | -- |
| `BF-m-1` | hop 3a: the move script and its dry run (plan, copy, verify; NO delete) | C-MOVE steps 1-2 | FWD-1, FWD-4 | NOT-EVALUATED | laptop | LOCAL | worker | BF-k-1 |
| `BF-r-1` | hop 3b: the readers that parse the old grammar by hand, moved to the shared function | C-READERS | FWD-4, FWD-5 | NOT-EVALUATED | laptop | LOCAL | worker | BF-k-1 |
| `BF-w-1` | hop 2: the writer -- the daily puller lands the builder's form; one optional single-day filter for the backfill | C-DAILY, C-BACKFILL | FWD-1, FWD-6 | NOT-EVALUATED | laptop | WORLD (the gate's `infra/` floor; nothing deployed) | worker | -- |
| `BF-e-1` | the equality instrument: capture silver figures for named days before, compare after | C-EQUAL | FWD-5 | NOT-EVALUATED | laptop | LOCAL | worker | -- |
| `BF-t-1` | hop 6: the thread trace -- one master and day, bronze at the builder's address, no second form, balances read from silver | FWD-1 DONE WHEN | FWD-1 | NOT-EVALUATED | laptop | LOCAL | worker | -- (reads the store through the builder, not through BF-k-1) |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED (NOT-EVALUATED is the value before a cell's instance exists).

**Chains (M = 4, one worker each; fan-out 4 of 4, cap 8).**
- A = BF-k-1 -> BF-m-1 -> BF-r-1 (slot ~1: the move script and the readers import the shared function; the order inside the queue is the order shown).
- B = BF-w-1 (slot ~2: PowerShell, no Python import; its parity with the builder is graded in its own criterion).
- C = BF-e-1 (slot ~3: reads silver tables only).
- D = BF-t-1 (slot ~4: an INDEPENDENT oracle -- it asks the builder where the file should be, so it cannot agree with the function it grades).

**Write sets (disjoint).**
- BF-k-1: `data/black_diamond/scripts/bronze/_monolith_bronze.py`, `data/canonical/schwab/silver/_canonical_silver_lib.py`, `data/canonical/schwab/tests/test_bronze_key_form.py`.
- BF-m-1: `data/canonical/schwab/keyform/move_bronze_key_form.py`, `data/canonical/schwab/tests/test_move_bronze_key_form.py`, `data/canonical/schwab/tests/fixtures/move_listing.json` (SYNTHETIC listing only), `data/canonical/schwab/keyform/__init__.py`.
- BF-r-1: `data/canonical/schwab/build_canonical_daily.py`, `data/canonical/schwab/silver/build_fact_tax_1099div.py`, `data/canonical/schwab/tests/test_canonical_daily_date_axis.py`.
- BF-w-1: `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`, `data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py`.
- BF-e-1: `data/canonical/schwab/keyform/equal_sample.py`, `data/canonical/schwab/tests/test_equal_sample.py`.
- BF-t-1: `data/canonical/schwab/keyform/thread_trace.py`, `data/canonical/schwab/tests/test_thread_trace.py`.
- Hookups the issuer adds at the merge: none expected; a `requirements` line if a cell's report names one.

**Code home (this round's ruling, the issuer's).** The new Python tools live at `data/canonical/schwab/keyform/` (LOCAL class, no `infra/` path), beside the
pipeline they serve. They run from the repo (laptop or the box's checkout), never inside the bd-tree deployment. The two key-function files stay where
they are because the bd-tree copy deploys standalone to `s3://opal-data-bd/code/`.

**Census of the old grammar, measured at the cut (2026-10-20 ~13:5xZ; C-READERS says the issuer re-measures).** Denominator: native `Grep` over `*.{py,ps1,tf,yaml,yml,json,sh}`
under `data/ infra/ lib/ .tools/ deck_generation/` for `monolith_bronze_key|list_bronze_dates|latest_bronze_date|fetch_bronze_text|schwab/{master}/bronze|f"schwab/{`: **31 files**.
- Through the function (follow BF-k-1, no edit of their own): `_monolith_bronze.py` callers `convert_schwab_{acc,trn,lots}_to_*.py`, `convert_schwab_rps_to_parquet.py`, `rps_ingestion.py`;
  `_canonical_silver_lib.py` callers `build_dim_account.py`, `build_dim_asset.py`, `build_dim_relationship.py`, `build_fact_{lot_realized,lot_unrealized,position,schwab,transaction}.py`.
- Hand-parse the old grammar (edit): `build_canonical_daily.py:63,141` (lists partition directories as 8-digit tokens), `build_fact_tax_1099div.py:74` (lists `bronze/tnn/`),
  `test_canonical_daily_date_axis.py:203`; the puller `sdd-daily-pull.ps1:55,442,375-380,506-521`.
- Key-shape agnostic (verified, no edit): the silver Lambda `schwab_conversion.py` (`scope_from_key` reads segment 1; `feed_from_key` and `date_from_key` read the FILE NAME) and its
  deployed twin `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/`.
- Not Schwab bronze (named so the census is whole): `build_mdpf_wse_49f_non_model_aua.py` and `INF_D_08.nmec_nmnc_nna.py` read silver; `data/_contracts/vendor_asof_registry.yaml` carries `bronze/{date}/`
  for other sources and no Schwab bronze grammar (the PRD named it as a starting list; measured: nothing to edit).
- One-time legacy writers that would recreate the old form if re-run (`remap-bronze-to-monolith.py`, `sdd-backfill-08335338.ps1`, `sdd-history.ps1`): NOT edited this round; the retire-banner is on the round-2 list (FWD-4's census cell).
- IAM: grants are `schwab/<m>/bronze/*` under enumerated masters (`monolith-iam.tf:60-81,179-196`, `iam.tf`); the new form sits inside them. No IAM edit.
- Documents (listed apart, per the CVO's carried item 2): `docs/architecture/OPAL_ASSETS_CONSOLIDATION_PRD.md:36,477` and `docs/architecture/OPAL_ASSETS_PRD.md:494` carry the retired grammar. They are not this project's to edit; the supersession is named in the L10 slug to `1.0.0_SA_CTO`.

**Release acts (NOT cells; they run after the cells drain, each by the seat that holds the access).** `AWS applies go to the laptop NFRA CloudOps lane (rule 34)`.
R0. Re-read Schwab's served floor (CVO carried item 3): a wide `-Mode enumerate` for each master on the Schwab box under the session lock; if the floor moved from 2023-10-17, the order of R4/R8 is a call for the CTO.
R1. Open the change-management entry (`org/critical_paths/change_management/`) naming EVERY family that reads Schwab bronze (one `describe` sweep) and the never-widen pair (CTO + COO) with the blast radius and both branches.
R2. `equal_sample.py capture` on the named sample of days per master (BF-e-1), committed.
R3. `move_bronze_key_form.py` dry run against the LIVE listing: counts per master and type against the brief's 21,782 (7,960 + 7,758 + 6,064), and the S3-event count (below).
R4. Copy; verify by count and sha per master and type. Window: outside the pull fires (09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z).
R5. Deploy the writer (`sdd-daily-pull.ps1` to its code home on the box) and the bd-tree copies to `s3://opal-data-bd/code/`.
R6. `equal_sample.py compare`: any difference stops the cutover before R7 (C-EQUAL).
R7. HELD FOR ANDREW: delete the old keys (CLAUDE.md: S3 deletes take human confirmation). He names the window.
R8. FWD-1: pull 08403355's oldest served day through the new writer (`-OnlyAsOf`, session lock), let the existing event convert it, run `thread_trace.py`.

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: the hops of the FWD-1 thread (6) plus the two instruments the cutover needs (equality, trace) = the PRD rows C-KEYFORM, C-READERS, C-MOVE steps 1-2, C-DAILY, C-BACKFILL's writer half, C-EQUAL, and FWD-1's DONE WHEN.
  By subtraction from the PRD CONTRACTS table (C-SCOPE, C-NAMES, C-KEYFORM, C-READERS, C-MOVE, C-BACKFILL, C-PARSE, C-RECORD, C-EQUAL, C-DAILY, C-ONBOARD = 11 rows):
  C-SCOPE and C-NAMES are rules every cell obeys (no cell); C-KEYFORM = BF-k-1; C-READERS = BF-r-1 plus the writer inside BF-w-1; C-MOVE steps 1-2 = BF-m-1, steps 3-5 = release acts R4-R7;
  C-BACKFILL = BF-w-1's filter plus release act R8 (the full backfill is round 2); C-PARSE = the existing converters, exercised at R8; C-EQUAL = BF-e-1 plus R2/R6; C-DAILY = BF-w-1;
  C-RECORD and C-ONBOARD = round 2 (FWD-3, FWD-7). Remainder: none unaccounted.
- **Same grain.** One cell per write set; the key function pair is one cell because the PRD forbids the two copies to diverge ("both change in one commit").
- **Intent coherence.** `k` is the grammar; `m` moves bytes (plan and copy only); `r` and `w` are the two sides that follow the grammar; `e` and `t` only read.
- **State coherence.** No cell writes to S3, applies Terraform, deletes an object, deploys code to the box or a bucket, or pulls from Schwab. `BF-w-1` edits a script that is deployed by R5, not by the cell.
  The cells together move nothing served today: the bd-tree and canonical readers still read the old form until R5.

## Battery (round 1 of a threaded project)

- `comp-schedule`: DECLARED-NOT-APPLICABLE. Thread round; the lens runs on the enrichment round that touches its surface. The fire times (09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z) are inlined into BF-w-1 and R4.
- `comp-iam`: RUN, because the thread touches IAM. Read at the cut: `monolith-iam.tf` and `iam.tf` -- the box role writes `schwab/{08242234,08335338,08403355}/bronze/*` and `_ops`, has no GetObject and no DeleteObject on bronze
  (the write-only invariant, `monolith-iam.tf:19-25,73`); the C3(a) remap role "cannot read the monolith, cannot delete anything". Denominator: 2 Terraform files, 3 enumerated masters.
  - Consequence 1: the new key sits inside every existing grant, so no IAM statement changes this round.
  - Consequence 2: NO existing role can run the copy (box role has no read; remap role has no monolith read). The copy (R4) and the delete (R7) run under the NFRA CloudOps lane's admin identity from the repo, never on the box;
    this keeps the box write-only. BF-m-1's script is therefore built to run from a repo checkout under whatever identity the caller holds.
  - Blind: the live IAM plane was not scanned (0 roles read); the CloudOps identity's actual Get/Put/Delete on the monolith prefix is confirmed at R1, not assumed.
- `comp-adversary`: DECLARED-NOT-APPLICABLE as a lens run (thread round). Findings read at the cut and inlined into the faces:
  1. **The copy fires the silver converter once per object.** `silver.tf:242-244,769-780`: `s3:ObjectCreated:*` with prefix `schwab/<m>/bronze/` and suffix `.zip` invokes `opal-assets-silver-schwab` for ANY key under that prefix.
     A server-side copy to the new form is an ObjectCreated event, so ~21,782 invocations re-convert every stored day. The converter derives master from segment 1 and type and date from the FILE NAME, so it accepts the new key and
     rewrites the same silver partitions. Consequences inlined: BF-m-1's dry run prints the event count; R1's pair names the fan-out as blast radius; R6's compare is the check that the re-conversion changed nothing; the same event path is
     what converts the FWD-1 day at R8 ("converted the existing way").
  2. **Versioning is ON on the monolith and no noncurrent expiry exists** (`monolith.tf:142-147,194-227`). A delete at R7 writes a delete marker and keeps every version, so rollback after R7 is removal of the marker, and storage does not fall.
     The R7 card to Andrew states both. The same file records "historical bronze keys are NEVER rewritten in place"; this move is Andrew's explicit exception (call 2), recorded in the pair.
  3. **The puller's skip-if-landed index and its post-run guard parse the old layout by position** (`sdd-daily-pull.ps1:372-380` builds `filename -> landed`; `:510-526` splits `{type}/{yyyyMMdd}/{file}` by segment 0 and 1).
     A writer that only changes `$keyDir` would re-pull every day (the index misses) and fail its own guard. BF-w-1 owns every occurrence in the file.
  4. **The search is boundary-lossy and the partition date is the API's `AsOfDATE`, never the filename** (`sdd-daily-pull.ps1:14-26`; two types, `fam` and `slm`, ship `CS{MMDDYY}`). The key keeps the vendor name unchanged and the date folder from `AsOfDATE`.
     The builder's date segment is `date=YYYY-MM-DD` while the vendor name carries `CRS{YYYYMMDD}`; the key function and the puller must agree on the conversion.
  5. **`address()` accepts any type token** (measured: 17 type folders x 3 masters, no refusal), so a typo in a type folder would not be caught by the builder; the key function keeps the lower-case code the puller derives (`TypeFolder`).
  6. **Both mirrors carry only the CRS filename form** (`monolith_bronze_key` builds `{master}.CRS{YYYYMMDD}.{FEED}.zip`), so `fam` and `slm` objects (CS form) are unreadable through it today; that limit is unchanged and is stated, not fixed, in this round.

## Not in round 1 (enrichment backlog, PRD section 3 and the CVO's carried items)

FWD-2 (full backfill of the three masters), FWD-3 (the held-days record, C-RECORD), FWD-6's scheduled-fire proof beyond R8, FWD-7 (C-ONBOARD, to include the CVO's carried item 1: the fourth master list `si2_daily_builder_named` at `monolith-daily-schedule.tf:49-51`, to be inverted
so every master outside the legacy pair is builder-named), the retire-banner on the one-time old-form writers, and the supersession lines in the two ratified OPAL_ASSETS PRDs (their owner's edit).
