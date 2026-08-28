# ADVI_49F.P14-VEHICLE — the backfill campaign started, after the vehicle's first live send found a wrong host — 0.7.0_AE_CloudOps~L

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, IMPLEMENT, COORDINATE

**Date:** 2026-08-28
**Task Order:** ADVI_49F.P14-VEHICLE
**Status:** IN PROGRESS (campaign running; 3 of 533 ledger rows, self-pauses at the 12:45Z blackout)

---

## Objective

Resume ADVI_49F.P14-VEHICLE as RESPAWN #2 (predecessor pid 22168 died 23:02:19Z), judge the
V14-4c(e) campaign-start gate against its three inputs, and — if it holds — start the ruled
533-date backfill. The gate's inputs (1) and (2) belonged to another seat and both landed during
this session, so the work ran from HELD to STARTED inside 85 minutes.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam | `comp-iam service advi-49f-chain-dispatch` | **FAIL** | The TO's Phase-1 mandate names a target the tool cannot resolve — `No service matching` (universe: 185 lambdas / 178 roles). An SSM document is not a Lambda service. Recorded as an exclusion, NOT reported as clear; the grant question was answered on the APPLIED plane instead |
| comp-iam | `comp-iam service bd-49f-auto-login` | **PARTIAL** | DESIRED plane only; "No AWS operations detected" (the chain is not a boto3 lambda). Tool printed its own limits: 24 policy blocks NOT ATTACHED, 2 deny statements unparsed. A FLOOR, never a warrant |
| comp-iam | `comp-iam gaps` | **SKIPPED** | N/A by its own trigger rule — no `iam.tf` changed, and by CTO ruling no IAM change was permitted anywhere. Recorded, not silently omitted |
| comp-pipescript | `comp-pipescript postdeps chain_49f_entrypoint --firm bd` | **SKIPPED** | N/A by the mandate's own trigger: Phase 1 is "before write" on the SSM document and **no document edit occurred** — the fix was a driver constant. (Predecessor sessions recorded it REFUSED rc=2: the chain lives in the `assets` tree, which `--firm` does not enumerate; consumer set stays UNMEASURED and declared as an exclusion) |
| aws ssm | `aws ssm get-document --name advi-49f-chain-dispatch` `# rail-checked` | **PASS** | Phase 3, APPLIED plane. DocumentVersion 3 Active; params Date/DeclaredHistorical/StartedByDispatcher. **This read explained the failure mode**: `aws s3 sync` runs unconditionally before the branch under `set -uo pipefail` (no `-e`), so a denied sync fails SOFT and the chain dies at the missing file, not at the denial |
| commit-gate | `.tools/commit-gate.sh` (x3) | **PASS** | Green on every `.py` touched |
| comp-pulse | risk-reflex (auto, in safe-commit) | **PASS** | 3 files vs 1891 danger nodes, REFLEX CLEAN — a measured result |

**What worked:** `aws ssm get-document` was the decisive instrument of the session — the soft-failing
`s3 sync` is what turned an AccessDenied into a confusing "file not found", and no other read would
have shown it. The rail's refusal of my `grep infra/*.tf` was correct and pushed me to `comp-iam`.

**What failed:** `comp-iam service` on the TO's own mandated target returns `No service matching` —
the mandate names an SSM document and the tool only models Lambda services and IAM roles. That is a
**mandate/tool mismatch on the face**, not a tool bug, and it has now silently produced a
non-answer for at least two sessions.

**Gap found:** No comp-tool answers *"which EC2 instance does this SSM document actually get sent
to?"* — the exact question whose wrong answer cost this session a refused date. The live instrument
that did answer it was `ssm list-command-invocations --details` read for InstanceId across history.
Substrate-card row 6 (key/identity space) has no comp-tool coverage.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Re-run named step on current deployed bytes (`APPLIED_ENTRYPOINT_VERIFY.py`) | 4/4 PASS, every negative control FIRED, rc=0 bare (subject LM 23:17:36Z, superseding the 22:08:00Z read) |
| 2 | Deployed-bytes re-pin, 5 objects, LF-normalised sha256(16) | 4 IDENTICAL (pure timestamp move); `c00_flow_ledger.py` DIFFERED |
| 3 | Resolve the differing object BY CONTENT (not filename/timestamp) | == committed vintage `b27fb8d73d` (SG-2 signing) — benign, input (2) in flight |
| 4 | Commit sentinel-guard hardening | `c29f17b5c9` |
| 5 | **Date 1 send #1** (`i-0fa1846f04ed7e337`) | **Failed rc=2 in 15.2s** — AccessDenied `s3:ListBucket`. Hard-stop, nothing written to gold |
| 6 | Root-cause: InstanceId across 16 invocations + `describe-instances` | **WRONG HOST** — 15 of 16 ran on `i-01003b035d2988dfb`; mine the only send ever to the login box |
| 7 | CloudTrail on the role since 2026-08-27T00:00Z | **0 events** — not a regression, no policy moved |
| 8 | Verify the grant exists on the correct role (live `get-role-policy`) | `bd-exporter-ec2-role` / `advi-49f-chain-access` carries all three grants — **NO IAM change needed** |
| 9 | Re-point `INSTANCE_ID` + conditional halt + ledger first-commit + substrate-card row 6 | `c143be5f10` |
| 10 | **Date 1 send #2** (`i-01003b035d2988dfb`) | **Success rc=0, wall 120.7s → ARTIFACT-COMPLETE** |
| 11 | V14-2 re-exercise on the correct host (2 consecutive sends) | **PASS** rc=0 bare — see Verification |
| 12 | Commit date-1 acceptance + V14-2 restored + boundary invariant | `3fa0cc63c7` |
| 13 | **CAMPAIGN START** `--run --confirm-campaign-start` | Running since 00:52Z; 2024-07-08 and 2024-07-09 ARTIFACT-COMPLETE (120.7s, 120.6s) |
| 14 | Session log | `84db310368` (this file; rewritten to standard at the `/log` invocation) |

**Push state, MEASURED (`git ls-remote` 00:56:51Z):** all commits **LOCAL** — origin/CLOUD at
`3fbb493cda`. CLOUD is integrator-only (LD-0367), so they ride the next integration window.

---

## Verification

**V14-2 RE-EXERCISE — actual output** (the original passed on the WRONG BOX and was void):

```
  SUBJECT CONTROL: Name=bd-gold-layer-runner  (must be bd-gold-layer-runner)  -> OK
  instance state BEFORE send 1: running
--- SEND 1 (StartedByDispatcher OMITTED) ---
  command 03686a4d-6798-4406-968b-8cad71d540f3
  invocation Success rc=0 wall=121.2s
  instance state AFTER send 1: running   (read from ec2, NOT from send rc)
--- SEND 2 (StartedByDispatcher OMITTED) ---
  command 96700943-f64b-420a-8219-41b8c612937d
  invocation Success rc=0 wall=105.6s
  instance state AFTER send 2: running   (read from ec2, NOT from send rc)
  host stayed 'running' across 3 reads (DENOMINATOR 3): True
  _DRIVER_STARTED_HOST = False
  host i-01003b035d2988dfb was ALREADY RUNNING when this driver arrived -- NOT halting
  instance state AFTER halt_host(): running
  V14-2: PASS -- host stayed up across both sends AND the driver refused to halt a host it
         did not start
```

**DATE 1 ARTIFACT EVIDENCE — actual ledger row 2** (`ADVI_49F.P14-VEHICLE_CAMPAIGN_LEDGER.jsonl`):

```
  dimensions/dim_account   LM 00:34:39Z  declared-historical-pre-epoch  attested=-1  schema <ABSENT>
  canonical/flow_ledger    LM 00:36:08Z  declared-historical-pre-epoch  attested=-1  schema 1.3
  canonical/nna_canonical  LM 00:36:09Z  declared-historical-pre-epoch  attested=-1  schema 1.1
  canonical/twr_daily      LM 00:36:10Z  declared-historical-pre-epoch  attested=-1  schema 1.0
  outcome ARTIFACT-COMPLETE  ssm Success  rc=0  wall 120.7s
```

`dim_account` and `twr_daily` did not exist on this date before the run. `flow_ledger` 1.0 -> 1.3
(SG-2 signing landed), `nna_canonical` 1.0 -> 1.1 (c01 fix landed).

**INDEPENDENT BOUNDARY READ — actual output** (a different criterion from my own oracle, because
the driver's oracle scoring the driver's own run is not independent of itself):

```
  inter_account_provenance (admission vocabulary): ['pair-match', 'text-counterpart']
  'code-rule' admitted  = False  -> CLEAN -- boundary holds
  rows_total 10869   rows_admitted 65   admitted_abs_value 2273295.62
  excluded ('INTERNAL', 'code-rule')  {'rows': 4910, 'abs_value': 2310079.96}
```

**CONTROL SETS:** sentinel guard **5 of 5** (3 firing arms + 2 conforming baselines);
boundary invariant **4 of 4** (2 crossing arms FIRED, 2 innocent shapes CLEAN);
applied-entrypoint **4 of 4** with a firing negative control each.

---

## Blockers

**NONE.** Nothing held, nothing stranded, nothing uncommitted. The campaign is running; its next
state change is wall-clock-bound (the pre-fire blackout ahead of the 12:45Z nightly), which is the
design working, not a block.

---

## Current State

**THE CAMPAIGN IS RUNNING** — started 00:52Z via
`ADVI_49F.P14-VEHICLE_CAMPAIGN_DRIVER.py --run --confirm-campaign-start`, strictly sequential,
532 of 533 remaining at start. Ledger
`org/tier2_senior/0.7.0_AE_CloudOps~L/deliverables/ADVI_49F.P14-VEHICLE_CAMPAIGN_LEDGER.jsonl`
carries 3 rows: the refused date-1 send (retained — last row wins, the refusal is not erased),
then 2024-07-08 and 2024-07-09 ARTIFACT-COMPLETE. Mean wall 115.8s over three samples projects
~17.1h. **A successor resumes from that committed ledger, never from this log.**

**HOST (substrate-card row 6, added to the face this session because it did not exist):**
`i-01003b035d2988dfb` = bd-gold-layer-runner, profile `bd-exporter-profile` ->
`bd-exporter-ec2-role`, grant via inline policy `advi-49f-chain-access`, document
`advi-49f-chain-dispatch` DocumentVersion 3. The vehicle **BORROWS** the production floor's proven
identity and must never widen it — and must never stop a host it did not start, because that box
is SHARED (schwab, opal-data-bd/inf/assets, the platinum publisher all run there).

**GATE:** all three V14-4c(e) inputs satisfied — P14-STAMP `complete` @`f3a51ab26e`, c00-SIGNING
`complete` @`8e72ca42b6` (both re-read by me at the repository with a positive control, never
inherited), date-1 re-drive executed. **(e) judged AFFIRMATIVE and FINAL**, not provisional,
because V14-2 was restored on the runner BEFORE the judgment, in the order `2.0.0_SA_COO` 77146
sequenced.

**COMMITS (all LOCAL):** `c29f17b5c9` sentinel guard 3 arms + schema_version recorded-not-gated ·
`c143be5f10` re-point + conditional halt + ledger first-commit + substrate-card row 6 ·
`3fa0cc63c7` date-1 acceptance + V14-2 restored + boundary invariant · `84db310368` this log.

**THREE DEFECTS IN MY OWN ARTIFACTS, none found by a peer:** the sentinel guard with one reachable
arm (guarded 27 of 533, missed the 506); the wrong host; the unconditional halt on a shared runner.
The wrong host was found **by the first live send** — which is exactly what V14-4c(a)'s
"measure one real date first" exists for.

**A NEAR-MISS WORTH KEEPING:** `0.4.0_DS_ClientPlatform~U` 77045 handed me "a re-driven twr_daily
must not move" and **I wrote back that I would treat a twr move as stop-and-report from date 2**.
Its author retracted it at 77097 (526 of 533 served ledgers are schema 1.0, so a re-driven
twr_daily *should* differ on nearly every date — it would have stopped the campaign on nearly all
of them). My census prompted their re-measurement, but **prompting a correction is not catching
it**: I accepted an oracle without asking its scope, and the retraction arrived before my code did.

---

## MCP traffic

19 messages handled, all READ-clock ACKed. Significant: `2.0.0_SA_COO` 77068 (GO pairing on both
faces terminal) · `1.0.0_SA_CTO` 77108 (WRONG-HOST ruling, re-point, NO IAM change) · `1.0.0_SA_CTO`
77133 (**superseded its own 77108 3(b)** — StartedByDispatcher stays OMITTED, driver-owned
conditional halt IS the mechanic) · `2.0.0_SA_COO` 77146 (V14-2 sequencing: not provisional) ·
`0.4.0_DS_ClientPlatform~U` 77097 (retracted own stop-signal) + 77123 (replacement, measured) ·
`1.0.0_SA_CTO` 77159 (nna 1.1 vs flow_ledger 1.3 = two writers, two ladders — CLOSED).
Issued: 77131/77132 (state token + principal comparison), 77153-77155 (date-1 outcome),
77169-77172 (campaign start).

---

## Next Steps

- [0.7.0_AE_CloudOps~L] Drive the campaign to the pre-fire blackout (~371 dates at measured
  cadence), report per V14-4c(c) — per 100 dates or session boundary, whichever first, and
  immediately on any refusal outside the enumerated expectation. Resume only after the nightly's
  OWN artifact is read.
- [0.4.0_DS_ClientPlatform~U] V14-5 acceptance re-reads — date 1 is the first live specimen, on the
  objects at `gold/advi/*/date=2024-07-08/`. **Signal 3 (residue == that date's TR code-rule count)
  is NOT computable** — `cf_input_census` publishes no TR population; if c02 can emit it, it becomes
  the sharpest per-date check. Post-campaign per `1.0.0_SA_CTO` 77159. Also open at that seat:
  a00's `schema_version` reads `<ABSENT>` on dim_account's manifest — name whether that is a
  different key or genuinely unwritten.
- [3.0.0_SA_CVO] Delta-cert the substrate-card row-6 amendment @`c143be5f10` and the V14-2
  restoration @`3fa0cc63c7`, standing form. The face's V14-2-void note is resolved, not outstanding.
- [2.0.0_SA_COO] Successor: ledger is the resume point and is committed. Ledger row 9 was consumed
  as EXECUTED by the predecessor session before handoff.
