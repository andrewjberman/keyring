# Post-crash relaunch to round 29 closed, the service principal created, W27 gated on the API half -- 2.0.0_SA_COO~Y
**archetype:** COORDINATE
**secondary_archetypes:** DEPLOY, VALIDATE

**Date:** 2026-09-30
**Task Order:** IRPT_BCKEND round 29 ~Y (TO-IB-yr-291, -292, -293) + ledger irpt-svc-analysis-principal-20260930
**Status:** IN PROGRESS (round 29 CLOSED at this lane; W27 gated on 2.0.0_SA_COO~P; round 30 gated on 1.0.0_SA_CTO)

---

## Objective

Relaunch workstream Y of IRPT_BCKEND after the 07:52Z laptop reboot (relaunch brief
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAUNCH_BRIEF_20260930_130xZ_POST_CRASH.md`): assess state from artifacts,
clean residue, continue `/canonical-drive` under the LIVE_ARMS RELAUNCH row. The limb in hand was the W27 window
(Andrew-direct ~06:5xZ: prove the three YCharts variants under a durable service identity, record the endpoints).

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-which` / PATH check (startup A.3) | PASS | 104 of 104 comp-tools resolve; a forwarder ran |
| `comp-find` / `comp-read` | FAIL (usage) | three calls refused by the rail for piping a census into `head`/`tail`; re-done with native Grep/Read |
| `.tools/to-pipeline-gate.py` (via safe-commit) | PASS after 3 refusals | GATE (ix) output-vocabulary refused bars carrying prose, a `.` inside the literal, and a two-argument print; fixed by one literal verdict line per check |
| `.tools/surprise-row-gate.py` | PASS after 1 refusal | S234 lacked `dismissal_reason`; a "keep both sides" channel merge spliced fences (malformed_blocks 2) -- replaced by a resolver that appends only the branch's new row blocks |
| `.tools/proof-of-spec-check.py` | PASS | 3 instances VALID; must run from INSIDE the worker's worktree (from the main tree it reports CHECKER-SCOPE INVALID) |
| `.tools/safe-merge.sh` | PASS x4 | 96, 95, 94's refusal record, 94; refused many times by other seats' staged sets / open merges / an uncommitted row |
| `.tools/deploy_ledger.py` | PASS | open -> close-leg x4 -> close for irpt-svc-analysis-principal-20260930 |
| `aws iam simulate-principal-policy` (via boto3) | PASS | 24 of 24 irpt/investor/ycharts roles explicitDeny on the new secret |

**What worked:** the base-run check FILES (CTO 103159) caught nothing wrong in the cut but made three gate refusals cheap
to fix; `simulate-principal-policy` with the resource policy turned "readers = walker only" into a printed 24-of-24.
**What failed:** the output-vocabulary gate refused prose in `<expect>` three times before the rule was clear;
`simulate-principal-policy` rejects a resource policy whose `Resource` is `*` (re-put the policy naming the secret ARN).
**Gap found:** the shared index is held by another seat's live work most of the time with 6+ committing seats -- a drain
waited nine ticks; there is no queue, only retries.

## Work Completed

### 1. Relaunch
Watcher armed, registered, serial file written, one OFFER-EXHAUSTED message (CRO 103230) read and acked. Residue: none of
mine (the two IRPT worktrees present were ~M's; no index lock; no lapsed lease).

### 2. Round 29 cut, dispatched, drained -- 3 of 3
- Issued @64a37ccbd5 (decomposition `decompositions/IRPT_BCKEND_DECOMP_R29_Y.md`), dispatched @0aa45f7188, workers ~94/~95/~96.
- 293 drained @784ac650d0 (allowedFirmIds projected; `decide()` refuses ACTOR_FIRM_NOT_ALLOWED).
- 292 drained @f39c3b0617 (opt-in Playwright HAR + `har_scrub.py` proven by a planted value).
- 291 refused on MY defect (the replay transport records an eleventh key) -> amendment 1 @641dc0411c -> respawned -> drained @1561789a42.
- Real run on CLOUD: 9 of 9 criteria at their stated reading. Drain-end packet @a8c85aaa9e, READ by the CVO 18:58Z;
  the CVO's sweep 5 (ADJUDICATION_v19, REMEDIATION_v15) is at HEAD.

### 3. The service principal (DEPLOY-class act)
Ledger `irpt-svc-analysis-principal-20260930` opened @a06fb4794f, CLOSED @4303ef0b2e: `svc-irpt-analysis@opalinvest.com`
(admin / service / opal-capital / active / allowedFirmIds cottonwood) in opal-users-v2; secret
`irpt/svc-irpt-analysis/password` (1 version, value never printed), readers = the walker's user only. Script
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/svc_principal.py`.

### 4. CTO condition 4 fired
The API served one inflection directory entry to the principal. Row IRPT_BCKEND-S238 (BLOCKING, ARMED, disarm owner the CTO).
CTO ruling 103317: the API half is a precondition of W27. Y handed ~P an exact patch @4a3cabe67d; ~P cut it as
TO-IB-pr-271 @22b99e32fd and caught a defect in it (a catch-all over a lazy import absent from 5 of 7 bundles);
correction recorded @de7719d376.

## Decisions Made

- R29 amendment 1: the replay conforms to production; no key stripped in production code.
- S228 disarmed by record (row S234): contract v1 never routed the two operations.
- W95-S1 and W96-S1 accepted as recorded definitions; W94-S2 and two base-red test files carried to round 30.
- The W27 gate triggers my live re-read on the SERVED move (IB-pr-275), never on a CLOUD commit.
- Row IRPT_BCKEND-S241 (OBSERVATION/INERT, ~P's): pr-271 still reads a missing module as "allowed nowhere" at runtime.

## Files Modified

See commit messages: 64a37ccbd5, 0aa45f7188, 641dc0411c, a06fb4794f, 4303ef0b2e, 4a3cabe67d, a8c85aaa9e, 5c19dcc1fe,
de7719d376, fe000c9aca, plus the hourly drive logs (daee98b79f, 41bd4deea9, 9a38ae6fe9, 160e9a904e) and the 21Z log in this commit.

## Blockers

- **W27 window -- BLOCKED on 2.0.0_SA_COO~P.** Evidence: `TO-IB-pr-271` is `pending` on CLOUD; worker ~98's commit
  c716489be8 is not an ancestor of CLOUD; no change-management ledger names pr-271 or pr-275. The window also needs
  `irpt-analysis-resident` running (STOPPED since 03:50Z; ~P's restart under CTO 103150).
- **Round 30 -- BLOCKED on 1.0.0_SA_CTO.** Evidence: no ~Y round-N analysis in `org/missions/D9/IRPT/IRPT_BCKEND/ledger/`
  since 19:00Z; the CVO's sweep 5 is at HEAD, so the slug is the CVO's and the analysis follows it.

## Current State

- Round 29 is closed at this lane: `infra/aws/lambda/investor-reporting/ycharts/generate/{job.py,transport.py,current_authority.py}`,
  `_scope/canonical_profile_reads.py` and `infra/aws/ec2/investor-reporting-ycharts/{ycharts_session.js,har_scrub.py}`
  carry the three cells on CLOUD (commits above). No ~Y worktree or branch remains.
- The durable principal exists and is live (login 200). Retirement is `svc_principal.py disable`, never delete.
- Open rows owned elsewhere: S238 (CTO), S241 (~P). STATUS: `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~Y.md` section 0.
- Loop: cron 4256a6ee, every 10 min at off-peak minutes, prompt carries the three live checks. Watcher re-armed each expiry.
- Push state: LOCAL (no seat but 0.0.0_AB_MSTR pushes CLOUD).

## Next Steps

1. **[2.0.0_SA_COO~P]** drain TO-IB-pr-271 and run the served move IB-pr-275 (packet + both halves).
2. **[2.0.0_SA_COO~Y]** on that deploy: `svc_principal.py negcontrol` (inflection REFUSED, cottonwood 200) -> both prints to the CTO.
3. **[1.0.0_SA_CTO]** read both prints, disarm S238; post the ~Y round-N analysis after the CVO's sweep-5 slug.
4. **[2.0.0_SA_COO~Y]** cut round 30 the same tick the analysis lands (certifier data path measured @5c19dcc1fe; S231's terminal state; one hygiene cell).
5. **[2.0.0_SA_COO~P]** restart `irpt-analysis-resident` under CTO 103150; then the W27 window runs (three bodies, cap 150 min).
