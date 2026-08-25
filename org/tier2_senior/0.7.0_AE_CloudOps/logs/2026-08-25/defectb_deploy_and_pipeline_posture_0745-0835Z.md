# 0.7.0_AE_CloudOps~Z -- DEFECT B DEPLOY + PIPELINE POSTURE 2026-08-25T07:45Z -> 08:35Z

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Seat:** `0.7.0_AE_CloudOps~Z`, site Z. **Window:** 07:45Z (relaunch) -> 08:35Z. **Commits:** 3.
**Directive:** Andrew-direct ~07:3xZ, *"fix this and only this, verify visually that it is fixed
(and confirm pipelines are scheduled/robust), commit, push / prod-deploy, and do all necessary
logging."* **My two legs: the deploy leg (rung 2) and the pipelines-scheduled/robust leg.**

---

## What this window delivered

**Both legs complete.** DEFECT B is fixed on the served artifact and proven there; the schedule and
robustness posture is measured, written and broadcast. **No third thing was touched** -- three
findings were FILED, not fixed, under the scope fence.

---

## Deployment Sequence (AE role addition) -- 1 ledger, CLOSED

```
08:12Z  ledger OPENED at deploy-START (NEVER#6)
        etfs-positioning-defectb-salxx-fxfxx-names, 4 legs declared
08:1xZ  PINNED tree shas BEFORE the build (so the comparison cannot be satisfied by
        whatever the build happens to produce):
          etf_positioning_publisher.py  d685a383ae83827ea147e89ede445ab622b0ef8a65cdf03acc4af7b3d0ca9b14
          etf_positioning_gold.py       35d3a35f04d1db905379b14c7043f02c5ca2ce3b0f6b2925060e3b9b55fb9b63
        build-and-upload.sh etfs-positioning etf-positioning-producer, BAU_PARITY_SKIP=1
          justification unchanged from tonight's four prior deploys: source_dir
          data/etfs/scripts/gold is SHARED, so parity reports every sibling as an extra
          write VERIFIED: size=32135, sha256 metadata match  (NOT inferred from rc=0)
          631ELit6nuAD0+... -> p/mc7hvScGyYxxMK9QY7qWQQ3gZqsWvH/GbJQVIbnvY=
        NOT used: infra/aws/lambda/etfs-pipeline/.../build_package.py -- FOUR members vs the
          deployed TWO; a packaged trading_calendar.py would sit at /var/task and SHADOW the
          layer copy (Rule 3). Disagreement FILED, not ruled.
08:16Z  commit 002cce2bfc  source map artifact_sha256 (Rule 2: commit before apply)
08:17Z  terraform plan -detailed-exitcode  rc=2, Plan: 0 add / 1 change / 0 destroy
          attribute delta EXACTLY: last_modified, s3_object_version, source_code_hash
          -- nothing else. Code-only; no IAM, env or config drift.
08:18Z  safe-apply BLOCKED rc=3 -- HALT-GATE identity unresolved, FAIL-CLOSED. Correct.
          Fixed by writing my serial to org/mcp/sessions/<session>.serial -- the gate's own
          prescribed remedy. NOT overridden.
08:18Z  safe-apply BLOCKED rc=1 -- HALT-GATE surfaced 2 pending messages (both 3-day-old
          COO~Z withdrawals explicitly stating nothing is asked and nothing held). Reviewed.
08:19:03Z safe-apply rc=0 with HALT_ACK=1
          comp-tagauthz PASSED, tombstone-gate CLEAN
          Apply complete: 0 added, 1 changed, 0 destroyed
08:19Z  0-diff replan rc=0 "No changes. Your infrastructure matches the configuration."
08:21Z  ledger CLOSED, 4/4 legs proven; committed e4b241a80f (close does NOT commit -- the
        gap I found and routed last session, applied to myself this time)
08:31:06Z rung 2b: lambda invoke -> published
```

## Verification (AE role addition) -- ACTUAL output

```
DEPLOYED PACKAGE, downloaded and hashed member-by-member -- 2 members, not 4:
  etf_positioning_gold.py       35d3a35f04d1db90...  MATCH (byte-identical to PRE-PINNED tree sha)
  etf_positioning_publisher.py  d685a383ae83827e...  MATCH (byte-identical to PRE-PINNED tree sha)
  applied CodeSha256 p/mc7hvScGyYxxMK9QY7qWQQ3gZqsWvH/GbJQVIbnvY=  LastModified 08:19:03Z

CONTENT of the DEPLOYED bytes (Rule 22a -- read the artifact, with controls):
  "State Street U.S. Government MMKT"          count=3
  "First American Treasury Obligations Fund"   count=1
  POSITIVE CONTROL "def run"                   count=1
  NEGATIVE CONTROL "zzz_no_such_token_9999"    count=0

INVOKE (rung 2b, ad-hoc QA):
  StatusCode 200, FunctionError None, platinum status "published"
  gold: as_of 2026-08-24, trading_days_behind 1, books 4, books_full 4, books_shell 0,
        holding_rows 187, sub_asset_class_vocab_size 13, run_class adhoc

SERVED ARTIFACT  platinum/etfs/positioning_data.json   (s3api, UTC-pinned, not `s3 ls`)
  BEFORE 2026-08-25T04:53:51Z  126,863 B  etag 18ed9ab01b66...
  AFTER  2026-08-25T08:31:06Z  126,809 B  etag 8914807b9e96...
  187 holding rows / 4 books
    DIVZ SALXX -> State Street U.S. Government MMKT
    IDVZ SALXX -> State Street U.S. Government MMKT
    PFDE FXFXX -> First American Treasury Obligations Fund
    PFOE FXFXX -> First American Treasury Obligations Fund
  NEGATIVE CONTROLS, all UNCHANGED:
    BP PLC · GSK PLC · MPLX LP · JPMORGAN CHASE & CO. · MARVELL TECHNOLOGY INC ·
    VERIZON COMMUNICATIONS INC
  RESIDUAL CRUFT: rows containing "ADMN CLASS" = 0 · rows containing "01/01/2040" = 0
```
**Meets COO~Z's AMENDED Z-S48 oracle exactly: TWO names change, the rest untouched.**
**The ad-hoc artifact is PROOF, never production evidence -- `cron(0 13)` remains the production
number, and rung 3 is `0.2.0_DT_PortfolioAnalytics~Z`'s, undischarged by this.**

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `terraform plan -detailed-exitcode` | 2 runs | PASS | **rc captured BEFORE any pipe.** rc=2 pre-apply (1 change), rc=0 post-apply (0-diff). Binary RESOLVED on PATH -- `.tools/terraform.exe` DOES NOT EXIST on this device, and Rule 26 warns against the baked path. |
| `.tools/safe-apply.sh` | 3 invocations, 1 apply | PASS | Two fail-closed blocks first (identity unresolved, then 2 pending messages). **Both were the gate working.** The identity fix was the gate's own prescribed remedy, not an override. |
| `build-and-upload.sh` | 1 build | PARTIAL | `BAU_PARITY_SKIP=1` required (shared gold `source_dir`). Write VERIFIED by sha256 metadata match. Parity check remains INACTIVE for this function -- residual, unchanged from prior sessions. |
| `deploy_ledger.py` | open / close-leg x4 / close | PASS | Opened at deploy-START. Committed the entry myself -- `close` removes the sentinel but does NOT commit. |
| `.tools/safe-commit.sh` | 3 commits, all `-F` | PASS | F-010: `-F` not `-m` for every non-trivial body. `[msg-verify] MATCH` on all three. Risk-reflex fired [HOLD] on the source map; read the citation. |
| live AWS primitives | `events list-rules`, `list-targets-by-rule`, `describe-rule`, `cloudwatch get-metric-statistics`, `cloudtrail lookup-events`, `lambda get-policy`/`get-function`/`get-function-configuration`/`invoke`, `logs describe-log-streams`/`describe-log-groups`, `s3api head-object`/`list-objects-v2`/`get-bucket-versioning` | PASS | The EXERCISED rung. **`cloudtrail lookup-events` is the one that prevented a false outage report** -- see Errors. |
| `comp-*` tools | none run | N/A | This window was a Lambda deploy plus an AWS-schedule census. The deploy rode the source-map/Terraform route (Rules 1/2/4) and the census questions -- rule inventory, invocation metrics, rule creation time -- have no comp-tool that answers them; `comp-freshness` answers artifact age, which was not the question. Stated rather than left blank. |

**What worked.** **Pinning the tree shas BEFORE the build.** It makes the L4 comparison unsatisfiable
by accident, covers every member at once, and needs no token guessing.

**What failed.** My first hour-11 count (see Errors). And a `for f in $(ls ...)` loop over the BBG
log directory **split on the space in `C:/Users/Opal Bloomberg/`** and printed `<NO ETF LEG LINE>`
for all 30 files -- which reads exactly like "the scheduled ETF leg has never run." The grep errors
were loud, which is the only reason it did not become a finding.

**Gap found.** `deploy_ledger.py close` still does not commit and still does not say so -- unchanged
from my last session's routing to `1.0.0_SA_CTO~Z`. Not re-routed; it is already on their list.

---

## Errors I made this window

1. **Reported EIGHT rules at hour 11 while correcting the claim that there were ZERO.** My regex
   required the hour field to EQUAL `11`, so the list form `cron(15 11,21 ...)` fell out --
   **and my own histogram had already printed `hour 11,21   1` on screen.** Caught by
   `0.4.0_DS_ClientPlatform~Z` @8783 before it reached Andrew. **I reproduced the exact defect I
   was correcting, one frame narrower.** Extended to the layered figure (9 / 10 / 19) and the
   framing retired in favour of the hour-independent claim.
2. **Nearly filed `LogonType: Interactive` as a robustness defect.** It is deliberate and
   documented -- the pull uses the signed-in Terminal's own bbcomm entitlement, and a
   SYSTEM-context task would fail every time. **Reading the `.cmd` source stopped it.** A
   settings-only read would have produced a confident, wrong finding.
3. **Nearly reported "the 13:00Z schedule has never fired" as an outage.** 0 invocations in 14
   days, ENABLED rule, valid target, correct resource policy -- it reads as broken. **CloudTrail
   showed the rule was created 2026-08-24T22:52:48Z, ten hours earlier, by my own apply.** The
   zero was correct and expected. **A false outage on infrastructure I built yesterday.**

>> **All three share one shape: a measurement that was TRUE about a narrower domain than the
>> sentence I was about to write.** Two were caught by going to the source, one by a peer. <<

---

## Blockers

**NONE at this seat.** Nothing held, nothing stranded, nothing uncommitted. The one deploy ledger
opened this window is CLOSED and COMMITTED.

---

## Current State (zero prior context)

**LIVE:** `etf-positioning-producer` CodeSha256 `p/mc7hvScGyYxxMK9QY7qWQQ3gZqsWvH/GbJQVIbnvY=`,
python3.11, 512 MB / 120 s, applied 2026-08-25T08:19:03Z. Rule
`etf-positioning-producer-daily` `cron(0 13 * * ? *)` ENABLED; **its first-ever scheduled fire is
today 13:00Z.**

**SERVED:** `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json` --
2026-08-25T08:31:06Z, 126,809 B, etag `8914807b9e96...`, `data_as_of 2026-08-24`, four full books,
187 rows, **both SALXX and FXFXX carrying their corrected display names.**

**COMMITS (all LOCAL on SITEZ, riding `0.0.0_AB_MSTR~Z`'s integration -- I do not push, LD-0367):**
```
002cce2bfc  ci: source map artifact_sha256
e4b241a80f  record: deploy ledger CLOSED, 4 legs
9443185ead  deliver: ETFS_POSITIONING pipeline posture report
```

**DELIVERABLE:** `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/ETFS_POSITIONING_PIPELINE_POSTURE_20260825.md`
@9443185ead -- SCHEDULED PASS, ROBUST QUALIFIED PASS, six findings, the layered hour-11 correction.

**MCP:** 21 messages read and ACKed; 1 six-recipient broadcast (6 DELIVERED / 0 QUEUED / 0 REFUSED).

---

## Next Steps

- [`0.7.0_AE_CloudOps~Z`] **~11:00Z TODAY -- THE A5 READ, held jointly with `0.0.0_AB_MSTR~Z`.**
  Every scheduled run so far produced `universe_count = 109`, the PRE-A5 count; today should be
  **~170**. Read `bbg/2026-08-24/run_manifest.json` for `run_class == "scheduled"` (not adhoc),
  the universe count, BBSEY/AMX coverage **matched on the ticker TOKEN** (the `security` column
  carries `AAPL US Equity` form), and whether `constituents/run_manifest.json` exists -- that leg's
  first scheduled fire. **Count, do not threshold: `>109` passes on a partial extension.**
- [`0.7.0_AE_CloudOps~Z`] ⛔⛔ **THE 13:00Z READ -- AND THIS ENTRY IS THE *PRIMARY* CARRIER FOR IT.**
  Owner proposed `2.0.0_SA_COO~Z` @8939, ratified `1.0.0_SA_CTO~Z` @8945; carrier ruled
  `1.0.0_SA_CTO~Z` @9007. **NOT a monitor, NOT an alarm -- a person, once. It builds nothing.**
  ```
  PRIMARY    THIS Next Steps entry. XXX.md Step 2 makes a successor at this seat read this log
             BEFORE anything else, so it is the one carrier that is both COMMITTED and
             STRUCTURALLY ENCOUNTERED. (DURABLE and DISCOVERABLE are two properties; a carrier
             needs both. MSTR~Z's WATCH file is durable and NOT discoverable -- no startup probe
             surfaces it and a successor has no reason to look in another seat's tree.)
  SECONDARY  org/critical_paths/WATCH_20260825T1300Z_ETFS_FIRST_SCHEDULED_FIRE.md (0.0.0_AB_MSTR~Z)
             ⛔ A SECONDARY MUST NOT CARRY ITS OWN COPY OF (d) -- POINT AT THIS ENTRY FOR IT.
             (d) has moved FOUR times; the secondary stopped at move three and went stale within
             the hour (`:72` still dated `2026-08-24`, caught by 2.0.0_SA_COO~Z @9031). It did NOT
             produce a wrong answer, because the secondary disclaims itself and names this entry
             PRIMARY -- that is the two-carrier discipline WORKING. **A secondary that carries no
             independent copy of a moving value cannot diverge from it again** (COO~Z's structural
             point, and it is the durable fix rather than re-syncing the line).
  NOT USED   a task order -- `task_orders/` is owned-paths-blocked for the ~Z lane (measured, with
             a positive control on the sibling deliverables/ path). DO NOT RE-ATTEMPT IT.
  ```
  **THE SIX CHECKS, after 13:00Z. Report the VALUES, never a bare verdict word:**
  ```
  (a) a NEW log stream for /aws/lambda/etf-positioning-producer, and run_class == "scheduled"
      NOT "adhoc"   -- the 14d window held exactly 4 streams pre-fire, ALL ad-hoc, so a 5th is the tell
  (b) generated_at ADVANCES past 2026-08-25T08:31:05Z
  (c) SALXX -> "State Street U.S. Government MMKT"        (DIVZ + IDVZ)   MUST HOLD
      FXFXX -> "First American Treasury Obligations Fund" (PFDE + PFOE)   MUST HOLD
      a regression here means the DEPLOY was reverted, NOT that the fix failed
  (d) data_as_of == THE LAST TRADING DAY BEFORE THE FIRE DATE, trading_days_behind == 1
      ANOMALY = data_as_of equal to the FIRE date (silver landed ~9h early). Explain it; do not
      wave it through and do not file it as a defect either.
  (e) the sha WILL differ from the 08:31:06Z object. EXPECTED, not a regression -- D5 cannot fire
      because generated_at sits inside the hashed body. Do not chase a no-op that cannot exist.
  (f) 187 holding rows / 4 books / 13 sub_asset_class values   UNCHANGED
  READ THE S3 OBJECT, not the page -- the edge cache lags truth by ~5 minutes.
  ```
  ⛔ **(d) IS DELIBERATELY RELATIVE, NOT DATED, AND IT TOOK FOUR SEATS AND SIX MESSAGES TO GET RIGHT
  while the fix it guards was correct on the first attempt.** Three superseded forms exist: "advance
  or the guard SKIPPED" (fires falsely on a healthy run), "2026-08-25 is healthy" (licenses a false
  pass), and any DATED constant (true today, silently wrong on every later fire). **THE INVARIANT
  that makes it structural rather than lucky: `silver/holdings/{D}.parquet` lands ~22:00Z on day D
  (measured 22:00:14 / :15 / :17 across three days) and the producer fires 13:00Z on day D+1 -- NINE
  HOURS BEFORE that day's silver. So at ANY 13:00Z fire the newest silver partition is ALWAYS the
  previous trading day.** NEVER#1's T-1 default therefore holds BY CONSTRUCTION.
  ⚠ **LIVENESS: the seat that accepted this cannot guarantee it is live at 13:00Z. ANY seat reading
  this log afterwards with no result reported should run the six checks -- no further authorisation
  needed, and an absent owner is worse than an unnamed one.** Report to `2.0.0_SA_COO~Z` +
  `1.0.0_SA_CTO~Z`.
- [`0.2.0_DT_PortfolioAnalytics~Z`] **Rung 3 is undischarged.** My rung 2 proves the DATA; only a
  production render proves CODE+DATA+DEPLOY together.
- [`1.0.0_SA_CTO~Z`] Two FILED-not-fixed items from the posture report: **`opal-data-etfs` is
  UNVERSIONED** (bbg partitions have no rollback), and the **as-of / universe-source grain
  divergence on Sunday and Monday runs** (`BDay(-1)` vs calendar day -1; no harm materialised).
- [`1.0.0_SA_CTO~Z` / `0.4.0_DS_ClientPlatform~Z`] The `build_package.py` FOUR-member vs deployed
  TWO-member disagreement -- reported, not ruled; a packaged `trading_calendar.py` would shadow the
  layer copy.
- [`2.0.0_SA_COO~Z`] The constituents leg has **never** run on the schedule; today 11:00Z is its
  first. Not a defect -- the leg is one day old -- but its first fire is unobserved.
