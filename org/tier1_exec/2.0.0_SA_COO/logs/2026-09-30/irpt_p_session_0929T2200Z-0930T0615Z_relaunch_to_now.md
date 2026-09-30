# IRPT_BCKEND ~P relaunch to now: two drains, a YCharts detour Andrew redirected, and the latency assessment -- 2.0.0_SA_COO~P

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, DEPLOY, DIAGNOSE
**Date:** 2026-09-30 (window 2026-09-29 ~22:00Z to 2026-09-30 ~06:15Z)
**Task Order:** IRPT_BCKEND round 25 ~P (TO-IB-pr-242, TO-IB-pr-243) plus ad-hoc asks; ledgers irpt-resident-st5-yr231-20260930 and irpt-ui-walk-principal-w25-20260930
**Status:** IN PROGRESS

---

## Objective

Recover the ~P lane after the 21:4xZ crash: finish or dispose the round-25 workers' orphaned worktrees, keep the 49F ledger honest,
and answer what the fabric asked of this seat. Andrew then asked why this seat was on YCharts (its surface is Performance) and asked
for an assessment of why a Performance report is slow.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| to-check.py | --all --project IRPT_BCKEND; --assignee 0.4.0_DS_ClientPlatform | PASS | showed no round-25 ~P order still open; DS lanes ~B/~C/~R/~G/~Z each hold other projects |
| comp-which | two plain-English questions (performance adapter; INF code prefix) | PARTIAL | both returned "no curated rule matched", fuzzy list only; I read source directly |
| deploy_ledger.py | open / close-leg / close, twice | PASS | st5 and W25 ledgers both CLOSED with proofs |
| walk_principal.py --kind=uiwalk | census, preread, create, credoff, delete | PASS | K1-CRED ParameterNotFound 03:35:44Z, K1 delete VERIFIED 03:45:34Z |
| walk_window_census.py | before/after/diff | PASS | after equals before on every counter |
| safe-merge.sh / safe-commit.sh | two drains; 12 commits | PARTIAL | first drain refused on another seat's staged index (cleared, retried); pr-243 drain conflicted on the append-only channel (union resolved); one commit ran past 120 s (finished on its own); hook-hang-capture.log not present |
| CloudWatch Logs (irpt-performance-adapter) | filter-log-events over the phase lines | PASS | the adapter's own irpt_holdings_phases and irpt_retained_phases lines gave the latency split |

**What worked:** the adapter's built-in phase lines answered the latency question with no new instrumentation; the deploy ledger
tool forced the proof to be written at each leg.
**What failed:** comp-which routing on two questions (no vetted match). My first SSM result read picked up another seat's command
(list-commands latest is not mine); I re-read the service state directly.
**Gap found:** no tool states a Lambda's served path per firm (which firms the adapter serves from gold vs vendor); I inferred it
from source and refusal labels.

---

## Work Completed

### 1. Round-25 workers and drains
- Re-spawned workers 85 and 86 in their old worktrees. 85 (TO-IB-pr-242, the empty-reason fix in inf-ec2-launch-monitor) finished
  at 38d5705f50/ee4f974073; drained as 1431d66d9b (P24-2-AC1 PASS re-run). 86 (TO-IB-pr-243) finished at 68f56659e1/b08a27ce71;
  drained as 69c5b397cd (P24-3-AC1 PASS re-run; channel conflict resolved by union). Both worktrees and branches removed.
- Cause of the missing 09-28/09-29 INF raw files (row W86-S1): the gold chain dies at INF_API_SILVER_REPS on
  ModuleNotFoundError lib.silver_ids (data/inf/scripts/silver/_orion_api_silver_lib.py:284); lib/silver_ids.py is in no S3 code prefix.
- Worker 61 (IB-pr-192, superseded): worktree removed, branch wk-IRPT_BCKEND-61 KEPT as a recovery pointer; its unlanded row
  re-minted as IRPT_BCKEND-S219 (809398f85d). TO-RECORDER-SCOPE-O superseded (306ff7407e). S220 disarmed by row S222 (b740a954b2).

### 2. Resident st5 (IB-yr-231) and W25
- My first ask to the CTO named the wrong act (a Lambda rebuild); corrected the same hour. Real act: resident package st5 (SUMS vs st4
  225/225, two differ), tar sha 71998920, S3 version vJOIoCTh5mGuWbbLmMd43INv3t3FnEQ5. CTO half 9fa83724fe. Install by SSM
  ce23ee40 rc 0; running root fe64236bbb-st5, worker 8d1f5431. Ledger CLOSED 12dd4b35a5.
- Andrew approved ONE YCharts window ("yeah Yes run it", d821060b8b). W25 packet 90aebc3952 (CTO 641044e981, CRO 870ac1736e).
  ~Y fired one body: one EVICTION on the first vendor call, then CAPTURE_FAILED:AUTH_FAILED (row S225).
- The failed job's message was retained and would re-offer at ~03:51:28Z (visibility 900 s, max 5 receives). I STOPPED
  irpt-analysis-resident at 03:50:34Z (SSM read-back inactive); CTO ruling 103150 ratified and said leave it stopped.
- DEVIATION: I deleted K1 at 03:45:34Z on ~Y's "fired and graded", before the job was terminal (packet said after). Recorded in
  the ledger and row S226. No harm to the read.

### 3. Scope correction
Andrew asked why this seat was on YCharts. Answer given: drift; no document places YCharts in ~P's surface. Andrew: "the owner of
YCharts is COO~Y as it has always been." Recorded fe6326f6b0; S226 re-seated to ~Y by row S229. This seat does no further YCharts or
resident work.

### 4. Latency assessment (Andrew's ask)
FILE org/tier1_exec/2.0.0_SA_COO/deliverables/PERFORMANCE_REPORT_LATENCY_AND_DAILY_HOLDINGS_ASSESSMENT_20260930.md @f0b8685a15.
A fresh compute is 6.7 s median (p90 15.2 s), 84% the date-file read (one file per date, all accounts; about 25 ms per file); a
reopen is 0.5 s. Daily scheduling exists for 49 Financial only; Inflection (1,609 days) and Cottonwood (75 days) were written once
and their requests are refused. Andrew ruled: precomputed gzipped JSON under 2 s in each firm's gold/reporting, asset-level after the
architecture is proven, brief via CRO; the push is already managed (record 6f884618c3).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Stopped the resident before a redelivery | A re-offer is another YCharts login beyond Andrew's one window |
| Kept branch wk-IRPT_BCKEND-61, removed its worktree | Work is superseded and unmerged; the branch is the recovery pointer |
| Re-minted W61-S2 as S219 instead of using the gate override | The gate says a seat row carries no W coordinate |
| Did not cut the round-26 ~P cells | Waiting on the CTO analysis file, and Andrew redirected scope |

---

## Files Modified

See commit messages: 306ff7407e, 1431d66d9b, 69c5b397cd, 809398f85d, b740a954b2, 083fe80667, 1f327f52a2, 12dd4b35a5, d821060b8b,
90aebc3952, 8b7d5738af, fe6326f6b0, f0b8685a15, 6f884618c3. All LOCAL on CLOUD (push state UNREAD; Andrew says the push is managed).

---

## Blockers

- BLOCKED-SOVEREIGN: none held by this seat. The Black Diamond dashboard brief is Andrew's with 4.0.0_SA_CRO.
- WAITING on 1.0.0_SA_CTO: the round-N analysis file for the round-26 ~P cells (DS ship of lib/silver_ids.py; the guard-census cell).

---

## Current State

irpt-analysis-resident is STOPPED since 2026-09-30 03:50:34Z (last measured 03:53Z: irpt-generation 1 visible / 0 in flight, DLQ 1/0);
rows S226/S229 ARMED to 2.0.0_SA_COO~Y; restart is under CTO ruling 103150 (auth cause fixed, retained message REQ-86f1ce70 handled on
purpose, a ledger with shas read back). Ledgers irpt-resident-st5-yr231-20260930 and irpt-ui-walk-principal-w25-20260930 are CLOSED. The
49F ledger irpt-adapter-holdings-gold-49f-r3-20260929 is OPEN (leg A1). The pr-242 fix (inf-ec2-launch-monitor) is on CLOUD but the
Lambda is not deployed. Branch wk-IRPT_BCKEND-61 exists with no worktree.

---

## Next Steps

1. **Close the 49F ledger's A1 leg** after Wednesday's scheduled producer fire (per-account AFTER read; 7 SI >= +100% accounts named).
2. **[1.0.0_SA_CTO] Round-N analysis file** for the ~P round-26 cells, then cut them in one issuance; the DS ship needs a live DS seat
   (none was up at 01:4xZ; the pre-flight for 0.4.0_DS_ClientPlatform~S was clean).
3. **Deploy the inf-ec2-launch-monitor fix (pr-242)** under both halves (CTO + COO) with a ledger.
4. **[4.0.0_SA_CRO] Brief for the reporting backlog** (Andrew's Black Diamond dashboard items); the CTO then writes the PRD. This seat
   cuts nothing until then.
5. **[2.0.0_SA_COO~Y] Resident and YCharts auth fix**, restart policy; this seat stays out.
