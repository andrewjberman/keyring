# ETF net-assets LAPTOP -> CLOUD: TO-1 delivered, live, parity 1/3. TO-2 (49F) held and rescinded.
**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE

**Agent:** 0.5.0_AE_OpalETL
**Window:** 2026-07-13 22:10Z -> 23:15Z
**Session type:** fresh spawn (prior session closed 1936Z)

---

## Summary

Built and deployed `etfs-netassets-daily` -- the ETF net-assets producer, migrated off a Windows
Task Scheduler job on Andrew's personal laptop into AWS. **Bronze-first (Rule 17a), silver
contract frozen, deployed Terraform-only, deploy-completion ledger CLOSED 4/4.** It is LIVE but in
**PARITY PHASE**: silver is quarantined to a scratch prefix and **the laptop is still the real
producer** until >=3 trading days of artifact parity.

Also **held and escalated CTO's TO-2** (a 49F SmartX ingestion build), which crossed the standing
sovereign prohibition. Andrew ruled; TO-2 was rescinded.

**Andrew-direct, in-session (~2215Z), scoping the work:**
> *"I dont care what the laptop was doing or what it wasnt doing, the point is that this is a
> robust, daily cloud-based process that dumps total NAV and share counts daily in the designated
> cloud bucket."*

I had begun grounding *why* historical partitions went missing and **stopped on his word.** The
laptop forensics are not a deliverable; the robust daily cloud process is.

---

## What shipped

| item | detail |
|---|---|
| Lambda | `etfs-netassets-daily`, py3.11, 1024MB/300s, layer `pandas-pyarrow-requests-layer:1` |
| Schedule | EventBridge `cron(0 22 * * ? *)` -- unchanged from the laptop's fire time (deliberate) |
| Alarms | `etfs-netassets-daily-errors` + `etfs-netassets-daily-did-not-run` |
| IAM | `etfs-netassets-daily-role` -- `opal-data-etfs` ONLY, zero grants to any other data bucket |
| TF root | `infra/aws/terraform/etfs-netassets/` (state key `etfs-netassets/tfstate`) |
| Source | `infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py` |
| Gate tool | `.tools/etfs-parity-check.py` -- the cutover gate |
| Tag | `etfs-netassets-v1.0.0` |
| Commits | `00484e0f5` (build), `c8a343d85` (deploy + ledger close), `11ef72eff` (alarm fix + gate) |

**THREE deliberate deviations from the laptop probe** (it is otherwise a faithful PORT -- the
source ladder, row schema, parquet conventions and carry-forward semantics are unchanged; the
probe is the best-behaved component in the chain and was NOT hardened):

1. **BRONZE FIRST.** The laptop parsed issuer responses in memory and wrote parquet straight to
   `silver/` -- raw bytes never persisted. The code already anticipates the scrape breaking
   (`SourceError("TrueShares page layout changed")`); on the day that fires, every past day
   becomes unre-parseable. Raw issuer bytes now land in `bronze/{trueshares,filepoint,msn}/{date}/`
   byte-for-byte BEFORE any parse, and **the parser reads those same bytes** -- so bronze is
   derived *through*, not *beside*, the parse and cannot silently disagree with silver.
2. **WRITE FAILURES RAISE.** `etf_probe.py:948-953` swallowed S3 failures into a WARN, and
   `:955-963` computed the exit code from the worst SOURCE TIER -- structurally blind to whether
   the data ever left the machine. Carried forward as a BUILD REQUIREMENT, explicitly NOT as a
   diagnosis of the historical gaps (`run.log` retains 5 runs -> unfalsifiable; and Andrew ruled
   the question out of scope).
3. **`staleness_days` crosses the parquet boundary.** Verified contract-safe against the CONSUMER
   rather than assumed: `build_mdpf_wsd2_etf_netassets_feeder.py:97-101` reads with no `usecols`
   and no strict schema assert, `:153` projects onto its own column list. "FROZEN" means do not
   REMOVE/RENAME/RETYPE -- not "do not ADD". WS-D2 needed zero lines changed.

---

## Verification (exercised, not asserted)

```
PORT FIDELITY  vs the laptop's own 07-13 artifact       28 fields x 4 funds   0 mismatches
AC10           re-derive silver from BRONZE ALONE, NETWORK HARD-CUT   32 fields   0 mismatches
MUTANT         corrupt 1 NAV digit in the bronze bytes (38.05->99.99) -> AC10 FAILS correctly
LIVE INVOKE    StatusCode 200, no FunctionError -> the py311 layer IMPORTED (it wrote parquet)
PARITY 1/3     laptop(live silver/) vs cloud(_cloudprobe/), BOTH read from S3
               52 fields, 0 mismatches, sum(net_assets) delta $0.00
               0 columns dropped (freeze intact), +staleness_days
QUARANTINE     live silver/netassets/2026-07-13.parquet still carries the LAPTOP's 18:00:09
   CONTROL     stamp, NOT my 18:44 invoke -> the cloud has NOT become the source of truth
DOOR 6         opal-data-etfs notification config EMPTY (writes dispatch nothing);
               POSITIVE CONTROL on opal-data-inf returned the live inf-portal-publisher rule
               on prefix gold/meta/ -- proving the EMPTY was a TRUE empty, not a broken call
```

**Deploy-completion ledger:** `20260713T2235Z_etfs-netassets-cloud-lift` -- **CLOSED, 4/4 legs
proven, nothing stranded.**

---

## Two defects I shipped and caught myself

**1. The `did-not-run` alarm was DEAD ON ARRIVAL.** I encoded it as a single 26h period
(`period=93600`). **CloudWatch caps an alarm period at 86400s; the API accepted 93600 silently**
and produced an alarm reporting "no datapoints were received" *forever* -- while the Invocations
metric plainly showed `Sum=1.0`. **An alarm that can never go green carries no information; it
gets muted, and a muted absence-detector restores the exact silent-absence failure the migration
exists to end.** The estate spent the night cataloguing instruments that CANNOT FAIL; this is an
instrument that CANNOT PASS -- **same defect, the verdict is independent of the world.**
Fixed to 26 x 1h datapoints, all 26 must breach (fires on true absence only; one good invocation
clears it within the hour, so **its green is observable**). Applied, 0-diff.
**STATE TRANSITION NOT YET OBSERVED -- the fix is NOT yet claimed as verified.**

**2. `aws s3 cp` printed `rc=0` on a FAILED upload.** The rc I echoed belonged to `tail` in the
pipeline, not to `aws`. `head-object` returned **404** and caught it -- had I trusted the rc,
Terraform would have applied against a nonexistent artifact. This is the exact class CLAUDE.md
records. **I knew the failure mode by name and wrote it anyway; the control caught it, my care did
not.** Final artifact built by the canonical `ci/build-and-upload.sh`.

---

## TO-2 (49F SmartX): HELD, ESCALATED, RESCINDED

CTO issued TO-2 at 2256Z: build a scheduled ingestion for `wsb_49f_smartx_model_aua.py`
($1.6B, no scheduler anywhere in the estate, last hand-run 07-08 -- **a real and serious finding**).

**I refused to build it.** It writes `.../49financial/...` -- 49F work, under the standing
sovereign prohibition (Andrew 07-09: *"i do not want to deal with 49 right now... unless i
explicitly ask for it"*). **CTO's OWN TO-1, 50 minutes earlier, had fenced me out of exactly this**
(*"NOT 49F/Schwab (sovereign prohibition; 0.6.2 holds the carve-out)"*). Second, independent
blocker: it schedules a **recurring vendor egress** to SmartX, and CTO wrote *"I read it as
authorized"* -- an inference. **latest + most-restrictive: the intersection was EMPTY, so I
surfaced rather than adjudicated.** Touched nothing -- no design, no prefix, no ledger, **not even
a timing run** (the prohibition covers verifies; "just time the model walk to size the compute" is
the harmless-looking prep that would have breached it).

**Andrew ruled (via MSTR), and split the halves OPPOSITELY:**
> *"No 49 Yet, but we are getting there. Eventually we will make a refactored gold runner that
> draws exclusively on the 0833 schwab data."* + **"YES -- recurring SmartX egress authorized."**

**SmartX egress LIFTED (standing, joins Orion). 49F BUILD STILL HELD. TO-2 RESCINDED by CTO in
full.** New fabric law from this: **AN AUTHORIZATION TO *CALL* A VENDOR IS NOT AN AUTHORIZATION TO
*BUILD* A PIPELINE.** CTO guessed the vendor answer correctly and **was still wrong to guess** -- the
hold produced a RULING instead of a BREACH.

---

## Compiler Tools

| tool | why | result |
|---|---|---|
| `comp-grep`/raw (rail-checked) | locate the off-books probe + the WS-D2 feeder by exact basename; comp-tools do not index an untracked laptop dir or TF module internals | PASS -- found both; markers logged |
| `aws s3api get-bucket-notification-configuration` + POSITIVE CONTROL | Door-6: what FIRES on `opal-data-etfs` before writing any new prefix | PASS -- EMPTY on etfs; control on `opal-data-inf` returned the live sentinel rule, proving the empty was a true empty |
| `.tools/commit-gate.sh` | mandatory pre-commit on the new `.py` | PASS (ruff + py_compile clean) |
| `.tools/safe-commit.sh` (x3) | Rule 14a; surface-check rode along | PASS -- no critical surface touched |
| `.tools/safe-apply.sh` (x2) | Rule 18 / NEVER-rule: no bare `terraform apply` | PASS -- 10 added 0 changed 0 destroyed; then 0 added 1 changed |
| `.tools/deploy_ledger.py` | NEVER#6 -- ledger OPEN at deploy-start, CLOSED at completion | PASS -- 4/4 legs proven, closed in-session |
| `ci/build-and-upload.sh` | canonical artifact build (stamps `content-sha256` the TF module reads) | PASS after I first hand-rolled it wrong |
| `.tools/etfs-parity-check.py` (NEW, mine) | the cutover gate | PASS -- day 1 GREEN, verdict NOT CUTOVER-READY (1/3), exit 1 |

**What worked:** the positive control on the bucket-notification check did double duty -- it proved
my instrument worked AND independently re-confirmed Door 6.
**What failed:** my hand-rolled `aws s3 cp` (rc masked by a pipe) and my first `did-not-run` alarm
(out-of-spec period accepted silently). **Both caught by a control, neither by care.**
**Gap found:** the upload-verify gate exists on 1 of 4 call sites (routed to CTO). `MEMORY.md` is at
178/~200 lines with **silent** truncation past the cap -- routed to CTO/CTO~B/MSTR, deliberately NOT
actioned by me (deleting other agents' standing safety prohibitions from inside a narrow ETF lane is
how a guard dies).

---

## Blockers

**None self-actionable.** Parity 2/3 and 3/3 are gated on the scheduled 22:00Z runs of 07-14 and
07-15 -- a hard external gate (time), stated plainly, not a coast.

---

## Current State (handoff -- zero prior context assumed)

- **`etfs-netassets-daily` is LIVE in AWS** and will fire itself at 22:00Z daily. It writes
  **BRONZE to the LIVE prefix** (`s3://opal-data-etfs/bronze/...`, raw issuer bytes) and **SILVER to
  a SCRATCH prefix** (`s3://opal-data-etfs/_cloudprobe/silver/...`).
- **ANDREW'S LAPTOP TASK IS STILL RUNNING AND IS STILL THE PRODUCER OF RECORD.** Live
  `silver/netassets/` is written by the laptop, not the cloud. **DO NOT DISABLE IT.**
- **Cutover requires 3 trading days.** Day 1 (07-13) is GREEN and EXACT. **Run
  `python .tools/etfs-parity-check.py`** -- it reads both sides from S3, refuses a cutover verdict
  below 3 days, and exits non-zero. Do not re-derive the criterion; run the gate.
- **CUTOVER ORDER (do not reorder):** 3 days green -> flip `local.silver_root` to `""` in
  `infra/aws/terraform/etfs-netassets/main.tf` + `safe-apply` -> **VERIFY the cloud writes LIVE
  silver** -> **ONLY THEN** disable the Windows task, said out loud in the ledger.
- **`etfs-netassets-daily-did-not-run` alarm: fix applied, GREEN NOT YET OBSERVED.** Confirm it
  leaves ALARM state; if it does not, the 26x1h shape is wrong and needs a rethink.
- **A GREEN FEEDER IS NOT AN ALL-CLEAR FOR THE ETF CHANNEL.** This lift is the **NUMERATOR**.
  **LD-0292** (~$528mm of 49financial silently reclassified as public float) is the **SUBTRAHEND**,
  a different feeder, still open, still frozen. A successful migration makes that wrong number
  **fresher, not righter.** Do NOT close LD-0292 off the back of this. Do NOT re-run mdpf. Do NOT
  write the INF spine sentinel (the Lambda's IAM role cannot reach `opal-data-inf` at all).

## Next Steps

- **[0.5.0_AE_OpalETL]** (me): parity 2/3 (07-14) and 3/3 (07-15) via `.tools/etfs-parity-check.py`;
  then the 4-step cutover. Confirm the `did-not-run` alarm reaches a non-ALARM state.
- **[1.0.0_SA_CTO]**: the upload-verify gate on the remaining 3 `aws s3 cp` call sites; `MEMORY.md`
  cap compaction (silent truncation past ~200 lines).
- **[1.0.0_SA_CTO~B]**: OPAL_ASSETS PRD -- AC11 (expected-firms guard) + AC12 (residual-direction
  test) stay OPEN and are NOT gated on feeder health.
- **[0.4.0_DS_ClientPlatform]**: LD-0292 remains DS's lane; my green feeder is not evidence for it.
