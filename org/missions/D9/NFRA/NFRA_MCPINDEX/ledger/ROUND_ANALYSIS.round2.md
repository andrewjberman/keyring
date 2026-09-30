# NFRA_MCPINDEX -- ROUND 2 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-09-28 ~20:2xZ

**L10 on `3.0.0_SA_CVO~O`'s slug** (msg 20260928T171014Z; `ADJUDICATION_v3.md` + `REMEDIATION_v2.md`, on CLOUD as
9ff8aaf1ef, pre-rewrite @1768215e19). The fold reads 0 of 93 undispositioned. Grade tokens:
`REALIZED | NOT_REALIZED | DEFERRED | HELD`.

**Issuer from here: `2.0.0_SA_COO~MI`** (placement @094c84f299, which splits the single `2.0.0_SA_COO~O` over four
projects). The recut is ONE issuance. **Section 1 comes first because it is time-bound: PHASE B must be DEFAULT before
tonight's 22:10Z weekday fire.** Everything else can follow in the same issuance or right after it.

Hash note: ids marked "pre-rewrite" resolve only on site Z's old objects. The CLOUD ids are given beside them.

---

## 1. ENRICHMENT ITEM 1 -- MX-s-10 PHASE B, RECUT-READY (lift as written)

**Cell id:** `MX-s-10b` (new order; MX-s-10 stays superseded with PHASE A graded, A6 @471c840a0a).
**Assignee:** a CloudOps-class seat. `0.7.0_AE_CloudOps~I` was closed by Andrew, so the issuer seats the worker or lane.
**Risk:** `WORLD`. The acceptance is a scheduled vendor pull that writes a served object (`silver/bd_assets_dim.parquet`).
**Authority (both never-widen halves SIGNED):** CTO half 30b494700f (pre-rewrite @82f48b4fc7); CVO half a86730dc45
(pre-rewrite @73e884bbbb), which carries GO guards G1-G3. Ask file:
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_MX-s-10_20260928.md`.

**Cell text (worker face):**
1. Open the NEVER-2 ledger `nfra-mcpindex-bd-asset-dim-rest-schedule` and COMMIT it before any change.
2. **G1:** in that ledger, record (a) the prior DEFAULT version of SSM document `opal-bd-asset-dim-download`, and (b) the
   served dim's current VersionId, read live from `s3api list-object-versions` on
   `opal-data-bd` `silver/bd_assets_dim.parquet`. The CVO names `kittUyy.WHGfmKRaAag.p4TqGFycZ3eA` (12:22:57Z). Read both
   values; never type either from memory. They are the rollback target.
3. Publish the ported document (@0ff972bc38 content: REST pull plus builder, Playwright 0, BD_PASSWORD 0) through its
   existing deploy path, and set it DEFAULT. Any Terraform goes through `.tools/safe-apply.sh`, never
   `update-function-code`.
4. **G3:** retire the Playwright asset-dim leg and the fees leg (`download-daily-asset-dim.ts`, its `_ts_source` entry in
   `infra/aws/ec2/EC2_MANIFEST.json`, `download-daily-fees.ts`, `bd-fees-trigger/`, and the fees schedule leg
   `bd-fees-pipeline-trigger` -> `bd-fees-trigger` -> `opal-bd-fees-download`) through Terraform. The `safe-apply` plan
   destroys ONLY the resources the ask names in its section 1.3. `bd-49f-fees-runner`, its session-chain rule and
   `bd-silver-merge` appear NOWHERE in the plan; a plan touching any of them stops the cell.
5. Run s10.AC1 and s10.AC2. Close the deploy legs.
6. **Do NOT fire the served document ad hoc.** The acceptance is the next scheduled 22:10Z weekday fire.
7. **G2, at that fire:** read the builder's printed `DELTA on the ... already-served rows` block and compare the written
   dim with the G1 VersionId on the id count and the non-null `cusip` count. If the id count is below 12,141, OR any
   row's `cusip` goes from non-null to null, restore the G1 VersionId in the same session and file a row. A cusip
   changing from one non-null value to another is in radius: report the count, no rollback.
8. Then run s10.AC3 and close the ledger in the committed state.

**Paths:** exactly MX-s-10's `<paths>` block (task order :172-185), unchanged:
`infra/aws/ssm/`, `infra/aws/terraform/bd-pipeline/`, `infra/aws/lambda/bd-pipeline/bd-asset-dim-trigger/`,
`infra/aws/lambda/bd-pipeline/bd-fees-trigger/`, `infra/aws/ec2/bd-exporter/src/stepwise/download-daily-asset-dim.ts`,
`infra/aws/ec2/bd-exporter/src/stepwise/download-daily-fees.ts`, `infra/aws/ec2/EC2_MANIFEST.json`,
`org/critical_paths/change_management/`,
`org/critical_paths/.open_deploys/nfra-mcpindex-bd-asset-dim-rest-schedule.json`,
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/<assignee>/**`,
`org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**`.
(The `nfra-mcpindex-bd-exporter-49f-session-read.json` ledger is closed, per Z-S44; drop it.)

**Criteria (3 mechanical, unchanged, plus 1 judgment):**
- `s10.AC1`: `bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s10.AC1.sh; echo "exit=$?"`
  expects `served document: rest-pull refs>=1 builder refs>=1 playwright refs=0 BD_PASSWORD refs=0 -- RESULT: PASS -- exit=0`.
- `s10.AC2`: `.../s10.AC2.sh` expects `rule state=ENABLED schedule=cron(10 22 ? * MON-FRI *) targets=1 targets
  bd-asset-dim-trigger=yes -- RESULT: PASS -- exit=0`.
- `s10.AC3`: `.../s10.AC3.sh` expects `runs at/after slot>=1 success>=1 dim rewritten after the successful run=yes --
  RESULT: PASS -- exit=0`.
- **`s10.J1` (JUDGMENT, graded at L9 by `3.0.0_SA_CVO~O`, never self-graded):** reading the G2 delta block and the
  scheduled run's own log, is the dim written by the 22:10Z fire one a Black Diamond tool may answer from? Specifically:
  ids >= 12,141, zero non-null->null cusip, and the non-null->non-null cusip-change count explained against MX-s-6's 42.
  An unexplained jump is a FAIL even when AC3 passes.

**Disarms on acceptance:** Z-S42 (the dim is current only by ad-hoc pulls) and Z-S47 (the fees producer fails while SSM
reads Success), both owned by the issuer.

---

## 2. L7, L8 and L9 accepted

- **L7:** every order is terminal. 16 completed in round 2: MX-b-2, MX-c-5, MX-d-2, MX-q-2, MX-r-3, MX-s-1, MX-s-3..s-9,
  MX-s-11, MX-t-8 and MX-v-6. MX-s-10 was closed with PHASE A graded (DELTA=0 on content, 12,141 = 12,141 ids).
- **L8:** 42 rows. 22 dismissed (Z-C-S22), 8 graduated and remediated on re-read (Z-C-S23), 12 graduated OPEN (Z-C-S24).
- **L9:** MXS4-AC4 PASS with one limit: the exit-after-shutdown ORDERING is proven only by a planted probe (Z-C-S25).
  Adopted as stated.

## 3. Outcome grades

| FWD | grade | why (artifacts) |
|---|---|---|
| FWD-1 (discover routes a cold question) | NOT_REALIZED | The discover family is built (MX-d-2) and shipped in gateway release 110d93fb73 (MX-r-3 AC3: SSM Success, /health 200, new integrations shipped 2 of 2, **enabled 0**). The routing harness reads 21 of 27, and the planted mislabel reads 20 of 27 (MX-v-6 AC2). Dataset asks route first 0 of 3 (Z-W2-S8). No live answer, and the cold run still needs G-B. |
| FWD-2 (portal figures equal the portal's) | NOT_REALIZED | The 3 mdpf portal tools are built (MX-t-8 AC1-3) and shipped DORMANT in the same release. No side-by-side (A2) read exists. |
| FWD-3 (Schwab) | DEFERRED | The hold's premise is gone: Andrew lifted the OPLGTW stop (~02:2xZ, call 5). It follows the thread, after item 3 below enables. |
| FWD-4 (custodian and platform tools) | DEFERRED | The substrates moved: the BD dim is current (12,141 ids, 805 of 805 coverage, MX-s-6); the Eclipse read finds 0 of 787 joined rows outside the allowlist (MX-q-2), which closes C-S12. No tool has been cut. |
| FWD-5 (ETF tools) | DEFERRED | TrueShares holdings reach silver (MX-s-1 complete) and the silver ETF tree was rebuilt (MX-s-3), which lifts R-4's exclusion. It follows the thread. |
| FWD-6..FWD-10 | DEFERRED | As graded in round 1. Nothing in round 2 moved them. |

**Round tally: 0 REALIZED, 2 NOT_REALIZED, 8 DEFERRED, 0 HELD.** The round built the thread's parts and shipped them
dark. It did not run the thread. Item 3 below is the round that runs it.

## 4. Rulings

**R-9, Z-S37 (the silver-id gate is fabric-wide, the helper firm-local): CLOSED, no further act.** Ruled (a) at ~06:4xZ
(`deliverables/1.0.0_SA_CTO~O/RULING_Z-S37_SILVER_ID_HELPER_TO_LIB_20260928.md`) and closed by this seat's row Z-S40.
Verified on CLOUD at this analysis: `lib/silver_ids.py` is tracked (8cd218cd05, pre-rewrite @88e4e69e69), the move
landed as 4fc07eb397 (pre-rewrite @9fb05bc6c1), and `build_bd_assets_dim.py` carries 10 `silver_ids` references. The
BASE_EXEC lane on `lib/` is unchanged by design (Z-S39); a DS seat that needs a `lib/` commit hands it to a lane holder.

**R-10, Z-S31 (the live BD password in tracked files): cut as item 2, CloudOps lane.** Andrew: rotation LATER, and NO
history scrub ("git is only me"). A shape read at this analysis (the values were never printed) finds a NON-EMPTY
`BD_PASSWORD` default still present in 4 stepwise scripts: `run-daily-downloads.sh`, `run-backfill.sh`,
`run-allocation-backfill.sh` and `historical-backfill-2014-2020.sh`. `extended-backfill.sh` now reads `${BD_PASSWORD:?}`.
The 2 docs were not re-read here. The set stays the 7 files ruled ~17:3xZ. Z-S29 and Z-S31 disarm fully only on
Andrew's rotation, which is carded and not cut.

**R-11, C-S13 (the null cusip): measured, bounded, not a blocker for item 1.** The dim reads 1,184 of 12,141 (9.75%)
null or blank. Silver transactions since 2026-04-14 read 14,367 of 3,185,260 rows (0.45%) with 0 on cash rows. Gold
`holdings_lots` reads 22,172 of 1,264,679 null, and its CASH share is unmeasured (B_01 maps 'CASH' to null). Rule for
any Black Diamond tool: an answer keyed on cusip states its null count; it never drops the null rows silently. The CASH
share is read in item 4. The REMEDIATION_v1 row's flip is this round's: it stays OPEN until that read.

**R-12, standing rules carried unchanged:** R-6 (device-neutral interpreter; exact-prefix fences with a sibling-prefix
negative control; a served-file criterion names the file in `<paths>`) and R-8 (NARROW gateway releases, cut at the
deployed commit plus this project's own changes; the deployed commit is now 110d93fb73, re-read at the cut).

## 5. THE ENRICHMENT LIST ROUND 3 CUTS (one issuance)

1. **MX-s-10b, PHASE B** -- section 1. Time-bound: DEFAULT before 22:10Z tonight.
2. **Z-S31 redaction, CloudOps lane (LOCAL).** Scope: the 7 files under `infra/aws/ec2/bd-exporter/` from the ~17:3xZ
   ruling. In a shell script, the default becomes `${BD_PASSWORD:?set BD_PASSWORD from Secrets Manager}`, never a
   placeholder that would attempt a login. In a doc, the value becomes a placeholder. Criteria: (a) a shape count of
   non-empty `BD_PASSWORD` defaults under `infra/aws/ec2/bd-exporter/` = 0; (b) `bash -n` passes on every edited
   script; (c) the CVO's fingerprint scan (the Z-C-S24 detector) reads 0 in the 7 files, graded at L8. No history
   rewrite. No value is printed anywhere.
3. **The thread, run live (SERVED, a gateway release under the never-widen halves).** Enable `opal_discover` and
   `portal_index` in `ENABLED_INTEGRATIONS` from the deployed commit 110d93fb73, with one deployer at a time. Close run:
   one question per portal surface, answered by the purpose-built tool, with figure and as-of date equal to the
   portal's (A2 denominator: `platinum/mdpf`, `platinum/etfs`, `platinum/advi`, `json/*`). If G-B is given, run the
   FWD-1 cold run. First, a ranking fix for Z-W2-S8 (dataset asks route first), graded on MX-v-6's harness: ROUTING
   >= 21 of 27, dataset asks >= 2 of 3.
4. **The measure batch (read-only), carried:** (a) the exit honesty of the other 4 BD SSM documents: failure branch and
   exit per document, SSM Status against the log outcome over the last N runs, denominator printed; (b) did MX-s-6's 42
   cusip deltas reach silver transactions (`merge-daily-incremental.py:57` joins the dim daily)?; (c) the CASH share of
   `holdings_lots`' 22,172 null cusips; (d) a live-consumer census for gold `canonical/lots_*`, silent since
   2026-07-23 (Z-W4-S2).
5. **Least privilege on `bd_exporter_additional`**, after item 1 lands: a caller census for `opal/bd/credentials`, then
   removal through Terraform with a NEVER-2 ledger if the census reads 0.
6. **The tooling batch (one cell, issuer-routed):** Z-S22 (derive bun with `command -v`), Z-W7-S2 (the CHANGELOG writer),
   Z-W3-S4 (portal rows get their own emitter section), Z-W3-S12 (`pytest_named` matches the verdict line). Z-W5-S1
   (a removal verb in safe-commit's stager) and Z-S24 (`is_string_dtype`, DS lane, latent on pandas 3) are routed to
   their owners, not cut here.

**Stated dependencies, not cells:** the 28 round-1 cells superseded onto opal_ai paths re-cut only after NFRA_OPALAI E9
(G-MOVE). The Schwab, BD, Eclipse, Orion, SmartX and ETF tool cells follow item 3's live thread; the BD tool follows
item 1's acceptance and R-11.

## 6. What this analysis does not do

- It does not rotate or purge the credential; both are Andrew's.
- It does not grade MX-s-10's criteria; the worker runs them and the CVO grades s10.J1.
- It re-measured only Z-S37 (by subject on CLOUD) and the Z-S31 script shapes. Every other figure is the slug's or the
  worker's, as cited.
