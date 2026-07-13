# 0.7.0_AE_CloudOps~A -- G6 close + OPAL_ASSETS P0-A (Andrew-direct table) + NFRA_IDENTITY G-A guard

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, IMPLEMENT, VALIDATE, COORDINATE
**serial:** 0.7.0_AE_CloudOps~A | **date:** 2026-07-13 | **window:** ~2354Z(07-12) -> ~0456Z(07-13) | second log of session (prior: 6e87751ab, NFRA_WEBSITE phase 2)

## Summary
Three deliverables, all landed. (1) **G6** -- per-cohort mdpf freshness stamp+alarm (COO P0): built,
deployed, CVO~A PASS on all 6 assertions, CLOSED. (2) **OPAL_ASSETS P0-A** -- Andrew intervened directly
and bluntly ("i dont want fucking alarms, i want functional structured dynamo db daily records of those 14
asset values"); he was right -- the fabric had been building alarms + contracts while the actual value
table sat unstarted in another lane. I took it, built the real table + emitter, backfilled it, and handed
him a queryable result. COO independently verified it. (3) **NFRA_IDENTITY.G-A** -- broker PID identity
guard (the chokepoint for the 07-12/13 mis-adoption SEV): built + exercised 8/8, routed to base CTO (org/mcp
is BASE_EXEC; my AE commit correctly refused).

## The Andrew intervention (the important part of this session)
He asked three questions: do we have it, is it clean and clear, did you work on that. Honest answers were
NO / the values yes but not in Dynamo / no -- I built the ALARM layer, not the table. I did NOT defend the
alarm work; I grounded the gap (checked DynamoDB: no such table existed), showed him the 14 real values that
DO exist daily in served S3, and built the table. Lesson banked: a monitoring layer is not the deliverable
when the deliverable is the record. The fabric's coordination (contracts, gates, hand-offs) was correct in
form but had not produced the artifact he asked for.

## 1. G6 -- per-cohort mdpf freshness (COO P0) -- CLOSED
Built additively on mdpf-freshness-checker: reads the daily PARTITION (per-cohort OWN-field as_of, never the
cross-partner min -- resolves CVO~A's vintage discrepancy), emits MDPF/DailyChain.CohortStalenessDays per
Cohort dim; 14 per-cohort alarms (ETF threshold 3, partner 1; treat_missing_data=breaching reserved for
dead-checker; MISSING/incomplete = explicit 99). Static EXPECTED_COHORTS taxonomy (COO ruling (a)) makes
cohort-8's 08335338 gap LOUD with ZERO sovereign touch. Deployed `mdpf-pipeline-v1.5.0`; ledger
`g6-mdpf-percohort-freshness` 4/4; ops heads-up published to opal-infrastructure-alerts (the ~11-alarm burst
is G6 correctly surfacing PRE-EXISTING silent staleness, not a new incident). **CVO~A verdict: PASS, all 6
assertions** -- and her own cohort-8 expectation was wrong while my partner_multi_master semantics were right.

## 2. OPAL_ASSETS P0-A -- the canonical daily 14-cohort AUM table (Andrew-direct) -- LIVE
- **Table** `opal-assets-daily-aua` (TF): PK run_date + SK cohort_id (a day's 14 rows = one strongly-consistent
  single-partition query) + GSI `cohort_history` (cohort_id, run_date); PAY_PER_REQUEST, PITR, SSE.
  **CTO~B arch-gate = ACCEPT-AS-BUILT, no re-key** -- he ruled my run_date orientation BETTER than his own
  031139Z criterion (the served read must not ride the eventual GSI).
- **Emitter** (`infra/aws/lambda/opal-assets/opal-assets-daily-emitter/`): served mdpf partition -> 14 rows
  {value, as_of, as_of_basis, state, staleness, source_masters(LIST), value_class, source_field}. State/as_of/
  staleness are G6-PARITY by construction, so the 14 alarms remain the acceptance oracle. Deployed as a
  scheduled Lambda (EventBridge 17:15 UTC) + least-priv IAM (served mdpf read only; table+GSI write only).
- **BACKFILLED** 2026-06-12..07-10 = 19 days x 14 = **266 real rows**. Two live query patterns proven.
- Ledger `opal-assets-p0a-table-emitter` 4/4; tag `opal-assets-v0.1.0`.
- **COO independently queried the live table** (did not relay my self-report): Count=14, honest states,
  own-field as_of, values match PRD. Verified.
- Sovereign-safe throughout: served opal-data-portal-v2 only; cohort-8 lands honest `incomplete`/99
  (08335338 NOT pulled = G2).

## 3. NFRA_IDENTITY.G-A -- broker PID identity guard -- BUILT+EXERCISED, routed to CTO
register_agent/heartbeat now REFUSE + name the conflict verbatim when (1) this PID is already LIVE under a
DIFFERENT serial [the SEV chokepoint -- one process, one identity] or (2) the claimed serial is held by a
different STILL-ALIVE process [protects the real lane from a phantom]. `identity_override="reason"` forces,
audited. **No-regression is load-bearing and is the whole design risk:** a freshness-only guard would refuse
every restart and break the fabric, so direction (2) rides an OS `_pid_alive()` probe (ctypes OpenProcess on
Windows -- NEVER os.kill, which TERMINATES there; os.kill(pid,0) on POSIX) and FAILS OPEN when undeterminable.
EXERCISED 8/8 (`org/mcp/test_identity_guard.py`): AC1 replay falsifier = the 07-12/13 sequence REFUSED;
AC2 = same-PID re-register / restart-with-dead-incumbent / first-register / stale-incumbent ALL ALLOWED;
AC3 = serial-held-by-live-PID REFUSED; AC4 = _pid_alive true/false.
**org/mcp is BASE_EXEC -> owned-paths correctly refused my AE commit.** Patch + test + exercise output
preserved in MY lane (`c27213899`, pushed = reboot-safe); diff routed to base CTO with ONE design question I
did NOT decide unilaterally: direction (2) hard-vs-advisory (residual = a respawn inside 120s while the dead
session's process lingers would be refused; evidence it's narrow: an MCP server DOES exit on session end --
3.0.0_SA_CVO~A pid 7704 -> pid_alive False).

## Deployment Sequence + Verification (AE)
| Deploy | Commits | Verify (EXERCISED, not config-read) |
|---|---|---|
| G6 (mdpf-pipeline-v1.5.0) | `46d8be80d` `bbedefb95` `b6d70910f` `b14b4b11c` | safe-apply 14 alarms + IAM + lambda; 0-diff; invoke rc200 -> 14 CohortStalenessDays w/ correct states; 14 alarms live |
| OPAL_ASSETS table | `70687ba8a` `4fb0ffeaf` | safe-apply 1 added; 0-diff; live query = 14 rows |
| OPAL_ASSETS emitter | `ee6ade7f0` `472f37881` `b49f6ef59` `f872b169f` `7c6d34439` `a660a087c` | safe-apply 8 added; 0-diff; **deployed-Lambda invoke rc200 wrote 14 rows via its OWN IAM role** (applied+exercised); backfill 19d/266 rows; GSI history query |
| (tag) | `opal-assets-v0.1.0`, `mdpf-pipeline-v1.5.0` | pushed --follow-tags |
Both ledgers CLOSED 4/4. `check --red` clean of mine.

## Findings (2 real bugs caught, both the same class)
1. **build-and-upload.sh FALSE SUCCESS** -- printed "Complete -- uploaded" + the s3:// line while the ZIP
   404'd in S3 (PowerShell `aws s3 cp --quiet` silent no-op). terraform then failed the data.aws_s3_object
   read. I re-uploaded direct + head-object-VERIFIED. Routed to CTO -> fix landed `da5af3c8c` (I confirmed it
   is on origin/CLOUD; base-AE added the LOCAL_SIZE whitespace amend).
2. **My own false-empty patch** -- `git diff org/mcp/server.py` printed NOTHING because safe-commit had
   already STAGED the file before owned-paths refused it; I committed a 0-line patch. Caught it, regenerated
   with `git diff HEAD` (230 lines), unstaged the shared index. **Same class as (1): a command that
   "succeeded" and produced nothing. Verify the ARTIFACT, not the rc.**
3. **DLM snapshot policy ERROR** (prior window, closed here): duplicate Project tag -> ZERO EBS snapshots.

## Compiler Tools
| Tool | Situation | Result | Note |
|---|---|---|---|
| comp-iam gaps / service | after 2 iam.tf changes (AE minimum) | ses/dynamo = COVERAGE-UNKNOWN; checker calls GRANTED/UNRESOLVABLE | comp-iam does NOT model ses; and models (action) not (action,resource,condition) -> Rule 22a live primitives are the authority |
| comp-blast register_agent | MANDATED before the broker contract change | **NOT-FOUND** | the graph does not model MCP-server tool functions. Per the tool's own words this is NOT a "nothing breaks" clear -- **coverage gap, logged**. Mitigated by reading every caller + the 8/8 exercise |
| commit-gate | every .py edit (server.py, emitters) | PASS after fixes | server.py could NOT pass the universal gate before this: pre-existing lint (unused signal import, E402, 2x E741, missing future-annotations). Cleared. |
| comp-which HUD | gated raw aws/grep several times | rail-checked | SES/DLM/DynamoDB/support-case state are not comp-modeled -> `# rail-checked:` markers |

**What worked:** live AWS primitives + deployed-role invokes were the authoritative proofs throughout (the
L4 SES exercise earlier, the emitter's own-role write here). **What failed:** nothing tool-side; the two
false-successes were script/VCS behaviour, both caught by verifying the artifact. **Gap:** comp-blast has no
coverage of org/mcp broker functions; comp-iam models neither ses nor dynamodb resource-conditions.

## MCP traffic
~24 significant. Inbound: COO P0 GO (G6) + ruling (a) + P0-A endorsement + independent verification + G-A GO;
CVO~A protocol/sharpenings/PASS; CTO~B schema ACCEPT-AS-BUILT + forward-compat; base CTO design input +
build-and-upload handoff; 0.8.0 contract asks + G4 fold + CTO~B condition; CTO~B stale pre-reboot alarm
(checked -> already landed, stood down). Outbound: G6 plan/design/landing, ops heads-up, P0-A handoff
(ARNs + row shape), G-A diff routing, 0.8.0 unblock (record_type (B) + I own the safe-apply).

## Blockers
**None self-owned.** Open items are correctly gated elsewhere:
- G-A diff -> base CTO arch-gate + land (BASE_EXEC lane; patch preserved+pushed, not stranded).
- 0.8.0's G4 fold -> they author+commit, I safe-apply (ONE applier, no TF race). Unblocked 045627Z.
- NFRA_WEBSITE (prior window): GoDaddy DKIM CNAMEs + W3 cutover = Andrew's calls; Patricia reply drafted in
  his Outlook, unsent.

## Current State (handoff surface)
- **`opal-assets-daily-aua` LIVE**: 266 rows (19 days x 14 cohorts), auto-updating daily via
  `opal-assets-daily-emitter` (EventBridge 17:15 UTC). Table ARN
  `arn:aws:dynamodb:us-east-1:313476888478:table/opal-assets-daily-aua`, GSI `cohort_history`.
  TF `infra/aws/terraform/opal-assets/{main.tf,emitter.tf}`. Deeper history (~380 older partitions) is
  available to backfill on Andrew's word -- offered, not yet actioned.
- **G6 LIVE**: 14 `mdpf-cohort-freshness-stale-*` alarms (12 ALARM / 2 OK, correctly discriminating on prod
  truth). CVO~A PASS. Fixtures left at `platinum/mdpf/_g6_fixture/` as the re-exercise pack (inert; S3-delete
  is human-confirm-gated -- NOT deleted unilaterally).
- **G-A**: guard live in the working tree (`org/mcp/server.py` + `test_identity_guard.py`, unstaged);
  patch+test+evidence committed at `c27213899`. Base CTO lands it. INERT until MCP servers restart.
- Zero unpushed commits (`git log origin/CLOUD..HEAD` = 0) -- reboot-safe.

## Next Steps
- **[1.0.0_SA_CTO]** arch-gate + land the G-A guard (patch `c27213899`); rule direction-2 hard-vs-advisory.
- **[0.8.0_AE_CloudComp]** author+commit the G4 ownership fold + the emitter.tf IAM read grant; ping me ->
  I safe-apply + re-backfill (with `record_type`) in one pass + open the ledger.
- **[0.7.0_AE_CloudOps~A]** add `record_type` to build_rows + re-backfill on 0.8.0's commit; deeper P0-A
  backfill on Andrew's word.
- **[Andrew]** GoDaddy DKIM CNAMEs + website W3 cutover; send/edit the Patricia draft; say how far back to
  backfill the AUM table.
