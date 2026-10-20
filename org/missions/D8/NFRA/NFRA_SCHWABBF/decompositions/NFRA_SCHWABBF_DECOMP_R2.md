# NFRA_SCHWABBF decomposition -- ROUND 2 (2026-10-20, issuer 2.0.0_SA_COO~SB): the firm-form rework, bronze side

Cut on the CTO's round-1 analysis `org/missions/D8/NFRA/NFRA_SCHWABBF/ledger/ROUND_ANALYSIS.round1.md` @b7c14b77b2 (msg 109909) and PRD v0.5, ADMITTED (ratified-text half `3.0.0_SA_CVO` current at
@99555e0048; brief half auto). Round 1 is `decompositions/NFRA_SCHWABBF_DECOMP.md`; its cells are terminal and merged on `box/laptop` on the MASTER form, nothing deployed, nothing moved.

**Scope (CTO ruling 2 of the analysis).** BRONZE side only. Silver, meta and `_ops` scope is OPEN at Andrew; no silver cell is cut here. The Alongside workstream (FWD-8, C-ALONGSIDE) is a separate workstream and is not in this rectangle.

**Andrew-direct words carried into every face (verbatim, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_143xZ_SCHWABBF_FWD8_CONFIRMED_BUILD_VENDOR_FIRM_PATHS.md`):**
"abiding by the path structure that already exists in that bucket ... its just schwab vendor and 49 firm for the 0840 and cottonwood firm for the various master accounts".
And, from round 1 (`ANDREW_DIRECT_20261020_130xZ_...`): one cutover, same-day rollback, no side-by-side period; the old keys are deleted only on his confirmation; the other 210 masters are out.

## The firm-form contract (fixed here; every cell builds against it)

Key: `schwab/{firm}/bronze/{feed lower-case}/date={YYYY-MM-DD}/{vendor file name}` = `address('schwab', <firm>, 'bronze', <feed>, 'date=YYYY-MM-DD')` with `s3://opal-data-assets/` removed, plus `/` plus the vendor file name UNCHANGED.
Firm of a master (registry rows `infra/logic/registry/scopes.json`, the `masters` list of each firm row): `49financial` = 08242234, 08335338, 08403355; `cottonwood` = 08719286, 08134043, 08165601, 08480305. Several masters share a firm folder and a partition path; they are told apart by the file name's master prefix `{master}.`.
Old (master) form, the move's source only: `schwab/{master}/bronze/{feed}/{YYYYMMDD}/{vendor file name}`.
Key-function API (both mirrors, same names): `firm_of(master)`, `bronze_partition_prefix(master, feed, date_compact)`, `bronze_key_for_file(master, feed, date_compact, filename)`, `monolith_bronze_key(feed, date_compact, master)`, `parse_bronze_key(key)`,
`parse_legacy_bronze_key(key)`, and the listers `list_bronze_dates` / `latest_bronze_date`, which FILTER BY MASTER inside the shared firm folder (see `TO-BF-k2` for the exact rules).

## The rectangle (round 2)

| cell | item | PRD rows | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `BF-z-2` | restore the five round-1 master-form files to their pre-round bytes (CTO ruling 3), the first merge of the round | C-KEYFORM | FWD-4 | NOT-EVALUATED | laptop | LOCAL | worker-light | -- |
| `BF-k-2` | R2-1: the key function pair in firm form, parsers, master-filtering listers | C-KEYFORM, C-NAMES | FWD-1, FWD-4 | NOT-EVALUATED | laptop | LOCAL | worker | BF-z-2 |
| `BF-m-2` | R2-4: the move tool in firm form (plan/copy/verify, no delete) | C-MOVE steps 1-2 | FWD-1, FWD-4 | NOT-EVALUATED | laptop | LOCAL | worker | BF-k-2 |
| `BF-r-2` | R2-3: the two hand-parsing readers in firm form | C-READERS | FWD-4, FWD-5 | NOT-EVALUATED | laptop | LOCAL | worker | BF-k-2 |
| `BF-w-2` | R2-3: the puller lands the firm form, guard and resumability index filter by master | C-DAILY, C-BACKFILL | FWD-1, FWD-6 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing deployed) | worker | -- |
| `BF-t-2` | R2-3: the trace oracle in firm form | FWD-1 DONE WHEN | FWD-1 | NOT-EVALUATED | laptop | LOCAL | worker | -- (asks the registry and the builder, not BF-k-2) |
| `BF-c-2` | R2-2: the converter takes the master from the vendor file name; deployed twin and manifest | C-KEYFORM consequence | FWD-1, FWD-5 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing deployed) | worker | -- |
| `BF-i-2` | R2-5: IAM statements per master by file-name prefix, and the event rules, for the firm prefixes (Terraform text; NO apply, NO plan against AWS) | C-ALONGSIDE (shape), C-MOVE step 3 | FWD-1, FWD-6 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing applied) | worker | -- |

`BF-e-1` (round 1, the equality tool, merged `39f21f2064`) is reused as built and is not re-cut.

**Chains (M = 6, one worker each; fan-out 6 of 6, cap 8).**
- Z = BF-z-2 (slot ~1, first; merged alone before any other slot is provisioned, so every other worktree is based on the restored bytes).
- A = BF-k-2 -> BF-m-2 -> BF-r-2 (slot ~2).
- B = BF-w-2 (slot ~3). C = BF-t-2 (slot ~4). D = BF-c-2 (slot ~5). I = BF-i-2 (slot ~6).

**Write sets (disjoint).**
- BF-z-2: `data/black_diamond/scripts/bronze/_monolith_bronze.py`, `data/canonical/schwab/silver/_canonical_silver_lib.py`, `data/canonical/schwab/build_canonical_daily.py`, `data/canonical/schwab/silver/build_fact_tax_1099div.py`, `data/canonical/schwab/tests/test_canonical_daily_date_axis.py`.
- BF-k-2: the first two files of BF-z-2, plus `data/canonical/schwab/tests/test_bronze_key_form.py`.
- BF-m-2: `data/canonical/schwab/keyform/move_bronze_key_form.py`, `data/canonical/schwab/tests/test_move_bronze_key_form.py`, `data/canonical/schwab/tests/fixtures/move_listing.json`.
- BF-r-2: `data/canonical/schwab/build_canonical_daily.py`, `data/canonical/schwab/silver/build_fact_tax_1099div.py`, `data/canonical/schwab/tests/test_canonical_daily_date_axis.py`.
- BF-w-2: `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`, `data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py`.
- BF-t-2: `data/canonical/schwab/keyform/thread_trace.py`, `data/canonical/schwab/tests/test_thread_trace.py`.
- BF-c-2: `data/assets/scripts/silver/schwab_conversion.py`, `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/schwab_conversion.py`, `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/BUILD_MANIFEST.json`, `data/assets/scripts/silver/tests/test_schwab_scope_from_filename.py`.
- BF-i-2: `infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf`, `infra/aws/terraform/canonical-schwab-ec2/iam.tf` (only if the census names a statement there), `infra/aws/terraform/opal-assets/silver.tf`, `data/canonical/schwab/tests/test_firm_prefix_grants.py`.
- The overlap of BF-z-2 with BF-k-2 and BF-r-2 is ordered by the chain edge (z-2 merges first; k-2 and r-2 start from its result), never concurrent.

**Release acts (NOT cells; after the cells drain, each by the seat that holds the access; the re-cut of round 1's R0-R8 on the firm form).** R0 re-read the served floor; R1 change entry + never-widen pair (CTO + COO) naming the blast radius and BOTH branches, including the event-rule order (CTO ruling: the cutover cell's choice in its pair);
R2 `equal_sample.py capture`; R3 move plan on the LIVE listing; the Terraform `safe-apply` of `BF-i-2` and the Lambda redeploy of `BF-c-2` (NFRA CloudOps lane, rule 34) BEFORE any copy; R4 copy + verify; R5 push (deploy of the bd-tree reader) and puller upload; R6 `equal_sample.py compare`;
R7 old-key delete HELD FOR ANDREW; R8 FWD-1 pull of `08403355`'s oldest served day, convert, trace. The release plan is written after the cells drain.

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: the CTO's enrichment list R2-1..R2-5 plus the restore ruling (3) = six members. By subtraction: R2-1 = BF-k-2; R2-2 = BF-c-2; R2-3 = BF-r-2 + BF-w-2 + BF-t-2 (three write sets, three cells);
  R2-4 = BF-m-2; R2-5 = BF-i-2; restore = BF-z-2. Remainder: none. Not cut by ruling: silver/meta/_ops scope; the Alongside workstream.
- **Same grain.** One cell per write set. **Intent coherence.** `z` restores bytes; `k`,`m`,`r`,`w`,`t` follow the firm grammar; `c` makes the consumer tolerate it; `i` lets the cloud permit it. **State coherence.** No cell writes to S3, applies Terraform, deletes an object, deploys code or pulls from Schwab; the three `infra/` cells are text and tests only.

## Battery (round 2)

- `comp-schedule`: DECLARED-NOT-APPLICABLE. The pull-fire times are inlined into BF-w-2 and the release window.
- `comp-iam`: RUN. Read at the cut: `monolith-iam.tf:60-81` (box write, `schwab/{08242234,08335338,08403355}/bronze/*`) and `:179-196` (the C3(a) remap role); `silver.tf:242-244` (event rules); 2 Terraform files, 3 enumerated masters. Firm-folder statements are enumerated PER MASTER by file-name prefix
  (`schwab/49financial/bronze/*/date=*/<master>.*`), never a wildcard over the folder (PRD C-ALONGSIDE shape). The old master-prefix grants STAY until the old keys are deleted (R7). Blind: the live IAM plane (0 roles read); the converter's execution role was not read (BF-i-2 names it from `silver.tf`).
- `comp-adversary`: DECLARED-NOT-APPLICABLE as a lens run. Findings inlined: (1) the three masters share one partition, so a lister that does not filter by master SUMS 0824 and 0833, which the purpose law forbids; (2) the puller's resumability index and post-run guard list the whole firm folder, so they must filter by master or report surplus;
  (3) the converter reads master from path segment 1 (`schwab_conversion.py:133-143`), which under the firm form is the FIRM, and its deployed twin carries a `BUILD_MANIFEST.json` that must follow the source; (4) a new-prefix key fires NO converter until the event rule exists, and fires it once per object after (row `NFRA_SCHWABBF-S1`); (5) round-1 rows W2-S3 (a legacy-only file is skipped by the puller's index) and W3-S1/S2 (ruled: `_source_file` excluded) carry over.

## Not in round 2

Silver, meta and `_ops` scope (open at Andrew); FWD-2 full backfill; FWD-3 held-days record; FWD-7 C-ONBOARD including the CVO's carried item 1 (the `si2_daily_builder_named` inversion) and C-ONEWRITER's map edits; the Alongside workstream; the retire-banner on the one-time old-form writers.
