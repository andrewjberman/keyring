# COT session-chain parity R1 restored + Andrew-direct MDPF cottonwood rerun — 0.7.0_AE_CloudOps~Z

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, VALIDATE

**Date:** 2026-08-27
**Task Order:** ad-hoc — `ctoZ_SPEC_COT_SESSION_CHAIN_PARITY_20260827` (R1/R2), then ANDREW-DIRECT MDPF cot rerun
**Status:** COMPLETE

---

## Objective

Build COT session-chain parity with the 49F pattern per Andrew-direct via `1.0.0_SA_CTO~Z`: the COT
BD cookie hit its 7d bound, the mint SUCCEEDED, and bronze never ran because the rule carrying
`session-fetch Success -> bronze` did not exist. Then, on a second Andrew-direct received mid-session,
ad-hoc rerun the MDPF path so cottonwood served T-1 today rather than tomorrow.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | A.3 startup exercise probe | PASS | forwarder RAN (produced its own banner); PATH 98 of 102 comp-tools resolve bare |
| comp-rail (HUD gate) | 3 x DENY on `infra/` greps | PASS | gate fired correctly each time; twice I rerouted to a better instrument (`terraform plan` over grep), once used `# rail-checked:` for a Python-token search no comp-tool covers |
| `deploy_ledger.py` | open / close-leg x12 / close x2 | PASS | two ledgers, 7/7 and 5/5 legs |
| `safe-apply.sh` | `-chdir=cot-pipeline apply` | PASS | HALTGT fired on 2 pending msgs; read both, `HALT_ACK=1`; comp-tagauthz PASSED, tombstone-gate CLEAN |
| `safe-commit.sh` | x8 | PASS | all `-F` msgfiles written by python (non-shell writer, F-010) |
| `/mdpf-refresh` | `status`, then `gold` | PASS | the skill, not hand-invoked lambdas — Build Ladder rung 2 |
| `lib.trading_calendar` | `trading_days_behind` x9 | PASS | resolved carry-gap anomalies on the TRADING calendar, not weekday counts |

**What worked:** `aws events test-event-pattern` as a pre-apply A3 control — it discriminates in both
directions (8/8), so its zeros are measurements. `deploy_ledger.py` refusing to close on an unproven leg.

**What failed:** nothing tool-side.

**Gap found:** **there is no broad SSM Command-Status oracle in this estate.** I went looking for one
to prove a non-Success event reached the bus; the only candidate (`moltbot-ssm-sendcommand-alert`) is
a CloudTrail `AWS API Call` rule scoped to a different instance and cannot see command-status events.
Recorded as a stated LIMIT on A3 rather than papered over. No instrument built (moratorium).

---

## Deployment Sequence

### Deploy 1 — R1, restore `cot-session-complete` (ledger `20260827T1511Z_cot-session-complete-restore`)

| Step | Action | Result |
|------|--------|--------|
| 1 | Grounding pass (49F applied rule read LIVE, not the spec table) | `bd-49f-session-complete` pattern + target captured |
| 2 | Restore rule+target+permission in `cot-pipeline/eventbridge.tf` | `57a373d336` |
| 3 | Pre-apply A3 control: `aws events test-event-pattern` | **8/8** both directions |
| 4 | `terraform plan` | **3 to add, 0 to change, 0 to destroy** |
| 5 | Ledger OPEN (7 legs) at deploy-start | `20260827T1511Z_...md` |
| 6 | `.tools/safe-apply.sh` (HALT_ACK=1 after reading 2 pending msgs) | **Apply complete: 3 added, 0 changed, 0 destroyed** |
| 7 | 0-diff replan `-detailed-exitcode` (rc captured BEFORE any pipe) | **rc=0** — "No changes." |
| 8 | Tag + integrator push | `cot-pipeline-v0.7.6` -> peels to `57a373d336`, ON remote |
| 9 | Post-merge re-verify at HEAD after 1122-commit merge | **rc=0** — DESIRED still == APPLIED |

**R2: NOTHING BUILT.** Already satisfied by `cot-bd-session-daily-et` on the EventBridge **Scheduler**
plane. Ratification deliverable `7fdf1979b3`.

### Deploy 2 — ANDREW-DIRECT MDPF cot rerun (ledger `20260827T1538Z_mdpf-cot-adhoc-rerun-20260827`)

| Step | Action | Result |
|------|--------|--------|
| 1 | BEFORE snapshot of assets bronze prefix (keys + ETags) | 47 objects; `2026-08-26.json` **404** |
| 2 | `opal-assets-ingest-mirror {firm:cot}` | 200; 695 enumerated / 13 written / 0 failed |
| 3 | Live verify + restatement diff | 47 -> 48, **ETag CHANGED = NONE** |
| 4 | Silver leg — **NOT FIRED** (mirror already produced it) | `fact_holdings_s2/date=2026-08-26` present |
| 5 | Issuer `[STOP HAND-INVOKING]` -> switch to `/mdpf-refresh` | finished leg in flight, then switched |
| 6 | `/mdpf-refresh status` (read-only preflight) | cottonwood **as_of_last=2026-08-25 [LAG behind=2]** |
| 7 | `/mdpf-refresh gold` (form chosen `gold`, not `full`) | floor green (12 objs), accrual SSM Success, publisher 14 published |
| 8 | Verify served bytes | cottonwood **as_of_last=2026-08-26 [PASS]** |

---

## Verification

**A2 — the rule actually FIRES (CloudWatch, new stream `2026/08/27/[$LATEST]98cc3dc1`):**
```
15:21:09Z  cot-bd-session-trigger invoked at 2026-08-27T15:21:09.571377+00:00 mode=bronze-run
15:21:10Z  SSM RunCommand sent: dcbeb71a document=opal-cot-bronze-run attempt=1
```
Two seconds from mint Success (15:21:07Z) to bronze dispatch. Attribution BY CONSTRUCTION: only this
rule sends `{"mode":"bronze-run"}` to that Lambda. Control: the morning stream sat frozen at 11:30:32Z.

**A3 — negative control on REAL events (`AWS/Events TriggeredRules[cot-session-complete]`):**
```
TOTAL = 1   (baseline over preceding 3h = 0 datapoints)
  15:21:07Z  opal-cot-bd-session-fetch  Success  -> FIRED
  15:23:01Z  opal-cot-bronze-run        Success  -> EXCLUDED
  15:22:56Z  opal-cot-silver-run        Success  -> EXCLUDED
  15:24:16Z  opal-cot-gold-run          Success  -> EXCLUDED
  15:29:21Z  opal-cot-bronze-run        Success  -> EXCLUDED
```
Four real different-document Success events excluded while the positive fired in the same window.
**Cannot pass by absence.** LIMIT STATED: no observed live InProgress event — that exclusion rests on
`test-event-pattern`, not on an observation.

**A6 — skip leg unregressed (verbatim):**
```
15:27:56Z  Lever A: cot cookie POSITIVE-live (probe positive (captured_at=2026-08-27T15:21:04.412Z,
           age 0.0d <= 7d)) -> SKIP OIDC-login mint, direct bronze-run
```
`captured_at` is the secret my mint wrote — a downstream reader observing the effect, not a self-report.

**MDPF served artifact (payload bytes, not the key name):**
```
platinum/mdpf/cottonwood/aggregate-aua-timeseries.json   written 2026-08-27T15:42:49Z
  as_of_last = 2026-08-26
  dates[] = 463 entries ending ['2026-08-21','2026-08-24','2026-08-25','2026-08-26']
  account_count_total tail = 320
```
Weekend correctly absent — trading-calendar clean.

---

## Decisions Made

1. **R2 NOT built.** `aws events list-rules` (137) and `aws scheduler list-schedules` (18) are two
   planes with no overlap. The spec's ABSENT verdict was correct on its plane and blind to the other.
   Building it would have created a dual trigger AND re-introduced the DST drift the tz-pinned
   Scheduler exists to prevent. Issuer amended the spec to RATIFY-WHAT-EXISTS.
2. **Form `gold`, not `full`, for the MDPF rerun** — stated before firing. Preflight showed the vendor
   leg already done; the skill's own ceilings note says a COT session before the ~01:02 ET BD bake
   re-lands the PRIOR snapshot, so `full` risked regressing the data just landed.
3. **Unstaged a prior-session diff found in the index at launch** rather than letting it be swept into
   the integrator's merge commit; reported to MSTR~Z, committed after the window closed.
4. **Did NOT resolve the 9 conflict-held gold keys** — reserved-category, and the tool cannot express
   the 3-not-9 disposition Andrew authorized. Zero relands, zero dry-runs.

---

## Files Modified

see commit messages: `57a373d336`, `7fdf1979b3`, `45010504ee`, `dd17e5f892`, `66a34bbc54`,
`a9fc23f691`, `c4fbf7dcb5`, `bc0b07e9fd` — all ON `origin/SITEZ` (verified `git ls-remote` +
`branch -r --contains`, not from a push report).

---

## Blockers

**NONE at this seat.** Nothing held, nothing stranded, nothing uncommitted. Both ledgers CLOSED
(7/7 and 5/5). Zero crons.

**Not blockers — items OWNED ELSEWHERE, listed so they are not read as mine:**
- 9 conflict-held gold keys: at **Andrew**. `1.0.0_SA_CTO~Z` resolved 6/9 as pure run metadata and
  3/9 (`global`) as real-because-the-recovery-worked. Hold in force.
- Roster cadence propagation: **QUEUED, not started** — rescoped by the issuer to FOUR homes / THREE
  contents, with the gold lambda bundling a pre-edit build artifact (remedy = redeploy, not edit).
- Late-July carry cluster (`07-29 <- 07-27`, `07-30 <- 07-27`): SURFACED, not chased.

---

## Current State

**LANDED AND LIVE:** `cot-session-complete` exists, ENABLED, in `opal-data-cot`'s chain —
pattern `{source:[aws.ssm], detail-type:[EC2 Command Status-change Notification],
detail:{document-name:[opal-cot-bd-session-fetch], status:[Success]}}`, target
`cot-bd-session-trigger` input `{"mode":"bronze-run"}`, lambda resource-policy statement
`EventBridgeCotSessionComplete`. Source: `infra/aws/terraform/cot-pipeline/eventbridge.tf`
@`57a373d336`, tag `cot-pipeline-v0.7.6`. DESIRED==APPLIED re-verified post-merge (rc=0).

**WHAT IT FIXES:** the Lever-A MINT leg terminated at
`infra/aws/lambda/cot-pipeline/cot-bd-session-trigger/lambda_function.py:277` with no bronze dispatch.
Measured 4-for-4 on `aws ssm list-commands`: both PRE-kill mint days (08-03, 08-11) kept their bronze;
both POST-kill mint days (08-19, 08-27) lost it. The rule had been KILLED at `5b989deb27` (2026-08-14,
by this serial's base lane) on the reasoning that it "fired 1x/7d while the chain completed DAILY
without it" — inverted, because the 1x/7d IS the mint day.

**ANDREW-CLARIFIED, RECORDED @`a9fc23f691`:** there is NO daily mint and this change adds none. The
daily Scheduler fires `mode=session-refresh`, which Lever-A SKIPS on a young cookie — mint ran 4x at
~8d intervals, bronze ran 30 of 32 days. **`MAX_SESSION_AGE_DAYS=7` is a POLICY CHOICE, not a measured
cookie lifetime** — his words: *"we do not even know if the cookie would ever die."* The fix is neutral
to the bound.

**MDPF SERVING:** all four scopes read `as_of_last=2026-08-26` (target T-1). **Cottonwood's own scope
is genuinely accurate** (real 08-26 data). ⚠ The firm-level `global` aggregate reads PASS but
**CARRIES cottonwood at 08-25** — `cohort_provenance[-1].cottonwood =
"carried_at_declared_cadence(as_of=2026-08-25)"`. The accurate recomputation is one of the 3
conflict-held `global` keys, so the guard serves the carried version and holds the accurate one.
Corrected into the closed ledger @`c4fbf7dcb5`.

**RETRACTED @`bc0b07e9fd`:** my claim that the carry ledger independently replicated the mint-day
finding 4-for-4. It corroborates ONCE (`08-21 <- 08-19`). Re-measured on the trading calendar: 3 of 9
carries anomalous, 6 ordinary T+1. The primary SSM evidence is untouched.

---

## Next Steps

- [ANDREW] **The 9 conflict-held gold keys.** He approved re-landing the 3 `global` and leaving the 6
  alone; `reland()` selects ALL conflict rows with no per-key scoping, so **the tool cannot express the
  authorization**. Fork: run it and accept all 9 (the 6 re-land business-identical), or delete exactly
  3 by hand (improvisation, advised against). Nobody has run any reland.
- [ANDREW] **Surprise-channel filer gap.** Rule 27 files to `3.0.0_SA_CVO~Z`; **no CVO seat exists on
  this fabric**, so surfaced items have no filer. `0.0.0_AB_MSTR~Z` is carrying this up.
- [`1.0.0_SA_CTO~Z`] **Roster propagation — their word to start.** Three acts, three mechanisms:
  (1) `data/mdpf/config/` DONE; (2) emitter copy edit + F-3 publish [my lane]; (3) `mdpf-gold-lambda`
  REDEPLOY so its bundled copy re-bakes (Terraform, Rule 1). **Verify (3) by downloading the deployed
  package and hashing the member — not `plan 0-diff`.** ⛔ Determine FIRST whether the cadence field
  alters computed output or only provenance (`_cot_carry_policy` computes from `max_lag` alone); if
  provenance-only this is a correctness-of-the-record fix and must be described that way.
- [`1.0.0_SA_CTO~Z` / whoever holds D8] **Late-July carry cluster** — `07-29 <- 07-27` (2 trading days)
  and `07-30 <- 07-27` (3 trading days) on a client-facing aggregate. 07-27 is NOT a mint day and this
  predates the 08-14 kill, so it is a different defect or a different explanation. Not established, not
  urgent, 4 weeks old.
- [ANY SEAT TOMORROW] **Check the prediction, do not assume it.** `1.0.0_SA_CTO~Z` predicted the mirror
  runs ~11:45Z, 08-26 reaches assets -> silver, and the 13:00Z sweep carries it to MDPF. **CHECKABLE and
  UNVERIFIED.** If it does not hold, the 24-hour recovery floor is not the whole story.

---

## Notes for the next reader

**Three errors I made and corrected in-session, recorded because the mechanism is reusable:**
1. **A5 overstated as "end to end"** — I measured COT's medallion and my sentence implied the serving
   path. The instrument was fine; the question I asked it was not the question my sentence answered.
2. **A bare "you" in a two-recipient send** misattributed a finding to the wrong seat. The pronoun
   rebinds per reader. **Address seats BY SERIAL in the body of any multi-recipient send.**
3. **A corroboration reached for too eagerly** — I found a second instrument agreeing with a conclusion
   I had ALREADY reached and never asked what it says on days the conclusion is FALSE. Agreement is
   cheap; a corroboration found after you are convinced is the one you are least likely to control.
