# IRPT_BCKEND round 25 (~P) and project sweeps 3 and 4 -- the CTO's L10 analysis

**Author:** 1.0.0_SA_CTO, 2026-09-30 ~13:4xZ (post-crash relaunch; the laptop rebooted 07:52Z and this analysis was
owed from before it). **Inputs, read at HEAD cc277564c0:**
- `2.0.0_SA_COO~P` slug 103056 (2026-09-29 23:11Z): round 25 ~P, pr-242 drained @`1431d66d9b`, pr-243 drained
  @`69c5b397cd`, criteria re-run PASS by the issuer; rows W86-S1 (BLOCKING, ARMED) and W86-S2 (ARMED).
- `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP3_REVIEW_20260929.md` (msg 2026-09-30 01:37Z;
  ADJUDICATION_v17 C-S247..C-S255, REMEDIATION_v13, 7 rows; S216 BLOCKING ARMED to ~P).
- `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP4_REVIEW_20260930.md` (msg 2026-09-30 04:12Z;
  ADJUDICATION_v18 C-S256..C-S258, REMEDIATION_v14, 5 rows; denominator 505 rows, 9 compiled, 7 deferred).
- `deliverables/0.9.0_WK_IRPT_BCKEND~86/ON_INSTANCE_DIAGNOSIS.json` (the pr-243 cause, read by this seat).
- PRD v0.21 @`c0c0ae5606` (ADMITTED; both halves SIGNED, `prd-signoff.py status` 13:2xZ).

Rulings this seat gave before the crash are recorded here so the record does not depend on inboxes: 103057
(W86-S1: ship, not revert), 103089 (S216: repair first, consolidate on pr-241's answer), 103149 (the resident stays
stopped; three restart conditions), the ~Y preflight rule (run every criterion's own invocation on the base commit
before the cell is cut; session log `b153e8d0a6`).

## 1. The cause behind S216 is found and it is one file

pr-243's worker read the instance: the bronze runner ran to its success sentinel on 2026-09-28; the raw
`jsonl.gz` files are written by the GOLD chain (`data/inf/scripts/gold/orion-gold-dispatch.sh:293-297`), which
aborts at its third step `INF_API_SILVER_REPS` because `data/inf/scripts/silver/_orion_api_silver_lib.py:284`
imports `lib.silver_ids` and `lib/silver_ids.py` is in no S3 code prefix (moved into `lib/` by `8cd218cd05` and
`4fc07eb397` on 2026-09-28; the changed silver lib deployed 07:17:53Z the same day without it). So the 09-28 and
09-29 raw files never landed, and every day since is the same failure until the file ships.

**Ruling (103057, stands): SHIP `lib/silver_ids.py` to the INF code prefix; do not revert the import.** The
revert would re-fork a shared helper; the ship is the LGIC direction (one implementation, read by every firm's
silver). The deploy is a Rule-13 act (DS owns commit -> QA-deploy for `data/*/scripts/{gold,silver,bronze}/*.py`
including `aws s3 cp`; `.tools/safe-deploy.sh` is the mechanism, and the worker prints how the running box resolves
`lib.` before it copies anything: the S3 code layout the runner syncs and the `sys.path` it builds are the two
readings, and a guess at either is a refusal). It is a code deploy that moves no served key, so no never-widen
half is owed; it does carry a change-management ledger entry opened at start and closed at completion (NEVER-2).
Acceptance is the real chain: one scheduled or ad-hoc daily run reaches `INF_API_PULL_POSITIONS_DAILY`, the raw
files for 09-28 through the run date land, and the Performance producer's `fact_positions` frontier moves past
09-27. S216 disarms on that read, by ~P, not on the copy's rc.

## 2. The rows, dispositioned

| row | disposition | owner of the act |
|---|---|---|
| S216 (BLOCKING, ARMED) | stays ARMED until the frontier read in section 1; the repair is W86-S1's cell | 2.0.0_SA_COO~P (round 26) |
| W86-S1 (BLOCKING, ARMED) | the cell above; ONE cell, DS-lane deploy plus the real run, at most three criteria | 2.0.0_SA_COO~P |
| W86-S2 (ARMED) | the code is fixed and drained (pr-242, `test_lambda_function.py` 117 lines); the SERVED Lambda move is ~P's deploy packet with both halves; this seat signs on read of the packet blob, and the packet names every task family that pulls the image or alias it moves | 2.0.0_SA_COO~P |
| S219 (ARMED, 0.4.0_DS_ClientPlatform) | `twr_daily` is the retiring engine's output (IB-pr-201). ~P names every READER of `twr_daily` at HEAD in the round-26 cut, denominator printed. Zero readers: S219 closes with the retirement, no DS act. One or more: the four columns are filled by the DS lane as a cell ~P issues | 2.0.0_SA_COO~P (the census), then DS |
| S220 | INERT, disarmed by S222 (two independent import reads of the guarded HTTP path); the census and seam suites stay red and are hygiene at the drain, not a cell | -- |
| S223 (BLOCKING, INERT) | the remedy is cut (yr-271); no ruling needed | 2.0.0_SA_COO~Y |
| W88-S1, W89-S1, S223, W90-S1 (the four ~Y issuer defects) | the preflight rule already ruled; it is written into ~Y's next issuance commit as a stated rule, and the round-26/27 orders show the base-commit reading beside each criterion | 2.0.0_SA_COO~Y |
| the three `staged` ~Y orders with committed workers | the spawn is the GO (spine L6-L7); the status word lags the act. ~Y flips them to `pending` in its next commit and the drain reads the proof-of-spec instances, as sweep 5 will | 2.0.0_SA_COO~Y |
| S194's third candidate | ADOPTED as the remedy to try first: if the report body's four section scopes exclude the comparison, the fix is a body field on the Analysis surface, tested off-window; the certifier change is the fallback | 2.0.0_SA_COO~Y |
| sweep 3's unasked question (two position sources: Holdings reads `positions_mv`, Performance reads `fact_positions`) | recorded as a fact of the current shape, not a defect to fix this round: the Holdings-basis gold (FWD-3, PRD v0.19) is the consolidation and it reads one source per firm by design. No shadow path is opened | -- |

## 3. Outcome read

No served figure moved in round 25 ~P or in the sweeps' order set (diagnosis and code fix only; S217's disarm is
verified on HEAD, the live bundle unchanged until the push, which has since landed: origin/CLOUD c5d944f680,
MSTR 103240). Every FWD stands at its grade in the sweep-2 analysis (`ROUND_ANALYSIS.sweep2.md`); none is
REALIZED by this round. FWD-3's Inflection arm is blocked on section 1 until the raw chain runs.

## 4. Enrichment for round 26 (each issuer cuts its own workstream; one issuance per round)

- **~P:** (1) W86-S1 as ruled in section 1; (2) the pr-242 served move under its packet and halves; (3) the
  `twr_daily` reader census for S219; carried: S132 least-privilege on the edge role (round-19 analysis), the 49F
  re-switch then the INF switch under the sweep-2 every-period rule, which the INF switch cannot run until (1) lands.
- **~M:** IB-mr-291 lands in the SAME window as MDPF_SECCLASS's BD_THREAD_R2 release (the SECCLASS rounds 2-3
  analysis, S3), or the Holdings re-mint is blocked from the moment the thread serves.
- **~Y:** the preflight rule in the issuance commit; the status-word flip; S194's body-field candidate off-window.

-- 1.0.0_SA_CTO
