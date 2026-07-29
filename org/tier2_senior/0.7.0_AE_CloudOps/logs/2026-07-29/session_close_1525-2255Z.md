# Session close: audit-archive arc closed, T1 authored, and the 07-28 refresh LANDED -- plus nine instrument-misreads, two of them mine

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, DEPLOY, COORDINATE

**Serial:** 0.7.0_AE_CloudOps (BASE lane)
**Window:** 2026-07-29T15:25Z -> 2026-07-29T22:55Z
**Commits:** 9 mine (`92c25f914e` boundary + 8) | **MCP:** ~30 in / 22 out | **Deploys:** 1 ad-hoc producer run + 1 Lambda invoke (both AD-HOC, not production evidence); 0 Terraform applies

---

## Summary

Three arcs closed and one instrument pattern documented. The audit-archive wedge was fixed, reconstructed
and verified; the OPAL_SQSCHAT.T1 Terraform was authored with its import deliberately deferred; and
Andrew's 07-28 refresh landed end-to-end after I stopped one publish that would have passed our own
acceptance test while serving stale data.

**The window's through-line is not any deliverable -- it is that NINE instruments answered confidently
about the wrong object today, TWO of which I authored myself, and one of which I hit while gathering
evidence for this log.** Every one was caught by a peer or a control; none by its author being careful.

## Work performed

### 1. AUDIT-ARCHIVE (CTO direct word 174222Z) -- CLOSED end-to-end
- **(a) UNWEDGE @`935ca2a7dc`.** Integrity gating moved from a single global `integrity_clean` to
  **PER-LOG**. A dirty log is **PINNED** at its prior baseline; it no longer withholds snapshots of the
  other 12.
  **PINNED not EXCLUDED is the load-bearing distinction:** excluding it would leave its next
  `prefix_test` with no baseline copy -> `ERROR: baseline missing` (fail-closed) -> re-wedged, AND an
  adjudicated finding disguised as an instrument fault. Pinning preserves evidence AND keeps NON-APPEND
  firing every run. **"Unwedged is not silenced"** -- CTO adopted the line.
  EXERCISED not read: self-test **PASS 7/7**; dry-run outcome moved `not-due` -> `deferred: lane not
  GOVERNANCE_AUDIT-permitted`, which IS the proof the wedge is gone.
  Also landed the honesty fix: every non-mint branch now names itself (`no-baseline`, `not-due: no
  uncaptured tail`, `not-due: baseline N.Nh < 12.0h`). `not-due` had been the DEFAULT LITERAL, so a
  WITHHELD snapshot rendered byte-identical to routine idle.
- **(b) RECONSTRUCT.** baseline + explicit UNRECOVERABLE-GAP seam + live tail; temp build, verify,
  atomic `os.replace`, **never `>`** on a file with live writers. 1,696,149 + seam + 15,042 ->
  **1,713,176 B / 17,382 lines**; pre- and post-swap both asserted byte-exact prefix + suffix + seam.
  Concurrency handled rather than hoped past (re-read before swap, rebuild if moved, ABORT rather than
  lose a delta, post-verify every pre-swap byte).
  **ACCEPTANCE: the invoker went 2 findings -> 1. `INTEGRITY/NON-APPEND-EDIT` CLEARED** -- because the
  file is genuinely append-intact again, not because anything stopped looking. The pin design predicted
  exactly this self-clearing property.
  The seam carries what CTO required AND refuses what he warned against: window
  (07-28T12:57:51Z..07-29T03:36:34Z, ~14h39m), the ~360 **labelled an EXTRAPOLATION, not a measurement**
  (true count UNKNOWABLE), and **CAUSE: UNDETERMINED** with no plausible substitute.
- **(c) CUSTODY: RETRACTED by CTO after I surfaced the conflict.** His (c) said track-and-
  reconstruct-before-tracking; **`.gitignore:482-491` -- his own 07-16 ruling -- says
  `git-author-override-audit.log` STAYS UNTRACKED** because `safe-commit.sh:338` appends to it DURING the
  commit. I held rather than landing or skipping it. His retraction: *"I contradicted myself, and the
  earlier ruling is the better one because it carries a MECHANISM and mine carried an intuition...
  Tracking that file would have made every commit in the estate dirty."*
  My `merge=union` finding killed his mitigation too: **union fixes the MERGE; what blocks is git's
  DIRTY-WORKTREE check, which fires first** -- measured, since `compiler-tools-log.md` carries union
  (`.gitattributes:28`) and still blocked me 5x tonight.
- **THE MINT (not mine, correctly):** COO ran it from its exec lane. Verified independently by me:
  baseline advanced `07-28T125858Z -> 07-29T185938Z`, **13 logs**, the reconstructed log **with its seam**
  captured at 17,406 lines, and `rc=0, 0 findings` from my own lane. **The gap marker is now as durable
  as the record it annotates.**

### 2. OPAL_SQSCHAT.T1 (Andrew-direct ~1812Z + ~1852Z; freeze lifted on EVIDENCE) -- TF AUTHORED @`45498eef9f`
TO flipped `staged` -> `pending`. Module `infra/aws/terraform/nfra-agentbus-port2/` (main.tf, sqs.tf,
IMPORT.md). Config written to **three independent agreeing live measurements** (mine ~1520Z, MSTR 1747Z,
COO ~1900Z): retention 1209600, SSE-SQS managed with KMS NULL, fifo + content-dedup, vis 30, long-poll 20,
`max_message_size 1048576` (TF default 262144 -- must be explicit or it diffs; carried on ONE measurement,
flagged in IMPORT.md to re-confirm at import).
Port-1 hazards asserted ABSENT **from CODE** -- and my first assertion **fired on my own explanatory
comments** (the matcher-fires-on-mentions trap); re-ran comment-stripped WITH a positive control so the
zeros mean something.
**IMPORT DELIBERATELY DEFERRED** to a clear head on COO's explicit offer. These queues are the ONLY live
path to site Z: a destructive outcome severs the channel AND removes the means to report it. Runbook +
acceptance (`0 to add, 0 to change, 0 to destroy`; fix CONFIG never apply the diff) in IMPORT.md so a cold
session can execute it.

### 3. ITEM 1 -- ANDREW'S 07-28 REFRESH: BOTH STEPS RUN, **PASS**
Andrew ~1936Z via CTO: *"I want a manual refresh of the gold and then platinum producers."*
- **STOPPED THE FIRST PUBLISH.** DS~A's verified gold landed in `gold/mdpf_revamp/`; the deployed
  publisher reads `portal/gold/mdpf/` (`GOLD_ROOT` env, hash-verified) which was still 07-27.
  **Publishing would have re-carried 07-27, returned `all_present=True`, AND MOVED ALL FOUR ETAGS** --
  because `_publish_one` re-stamps `_provenance.written_at` every run. **Our agreed acceptance test would
  have read SUCCESS on a failed refresh, and the cottonwood fence would not have caught it either.**
- **REPLACED THE CRITERION** (CTO accepted unamended): read the artifact's DECLARED fields
  (`as_of_last` / `dates[-1]` / `n_dates`) + `_provenance.source_keys` naming the 07-28 bridge output;
  ETags CORROBORATION ONLY; cottonwood EXCLUDED.
- **FLAGGED A SILENT STALL** -> CTO found **AE~A DEAD** (no watcher, 79 queued) holding the bridge
  dispatch. Re-routed BOTH steps to me, single owner.
- **STEP 1, the accrual bridge** (`build_portal_gold_accrual.py`, deployed-current MATCH). My own dry-run
  reproduced DS~A's prediction first, as a control. Real run:
  **`DONE written=3 skipped_existing=8 errors=3`** -- exact match to the prediction. The three landed
  ETags **ARE DS~A's gold md5s digit-for-digit** (single-part uploads, so ETag == md5 = **BYTE-IDENTITY**:
  the bridge COPIED, it did not re-derive). Verified by **ListObjectsV2**, never HeadObject (13c).
  Both controls held, each a SEPARATE invocation: cottonwood 07-27 **R5-SKIPPED** (repair intact,
  80,429B @18:49:54Z); global `account-distribution` **R5-SKIPPED** (stays 7,597 so tomorrow's deploy
  stays verifiable -- NOT a stale artifact).
- **STEP 2, the publisher** (empty payload -> self-labels AD-HOC in CloudWatch by the absence of
  `source: aws.events`, so tonight's 16:15Z scheduled fire stays clean D2 evidence).
- **VERDICT PASS**, read from the artifacts:
```
scope        as_of_last              dates[-1]    n_dates       prov_vintage
49financial  2026-07-27 -> 2026-07-28  2026-07-28   432 -> 433    2026-07-28
inflection   2026-07-27 -> 2026-07-28  2026-07-28   432 -> 433    2026-07-28
global       2026-07-27 -> 2026-07-28  2026-07-28   450 -> 451    2026-07-28
cottonwood   2026-07-27 (UNCHANGED)    2026-07-27   450 (same)    2026-07-27
```
  **CROSS-LAYER ATTRIBUTION:** my platinum BEFORE read `432/432/450/450`, matching DS~A's gold "was"
  values; it now reads DS~A's predicted `433/433/451`. Two agents, two layers, one named field, prediction
  stated before the fact. **Neither of us could have established that alone.**
  **And the discarded ETag test was vindicated by measurement:** stripped-md5 moved on **ALL FOUR**
  including cottonwood, whose `as_of_last` correctly did NOT move (its platinum went 37,518 -> 80,710 B
  carrying DS~A's repaired 07-27 content). A "bytes moved" test would have read 4/4 = full success.

### 4. NINE INSTRUMENT-MISREADS -- the window's real finding
Catalogued with CTO. Mine, both self-caught but only after authoring them:
- **#8: my ETag acceptance criterion.** Could not fail -- the publisher re-stamps provenance every run.
  **The first lying instrument WE AUTHORED rather than inherited.**
- **#9: my `as_of` test as a RECURSIVE DATE SCAN.** It read `2026-07-28` on 49financial **before any
  publish**, off `source_vintage_last`/`meta`. Authored 21:17Z; CTO minted *"ask what result would make it
  FAIL"* at 21:19Z; it failed that test at 21:22Z. CTO's sharper generalisation, adopted:
  **>> DO NOT SCAN FOR WHAT THE ARTIFACT DECLARES BY NAME. <<** Same error as reading a size where a hash
  exists, an rc where a verdict exists, a name where a target exists.
- **#10, hit while writing THIS log:** `git log --author=... --since="2026-07-29T15:25:00"` returned
  **ZERO** for a window in which I made 9 commits -- `--since` reads **LOCAL** time (UTC-4), excluding
  15:25Z..19:25Z. Caught only by a positive control (30 commits exist; `935ca2a7dc` is mine). Corrected to
  `--since="2026-07-29 15:25 +0000"`. **Memory law #11, hit by me, in the act of documenting the class.**
  A second one in the same command: `--author="0.7.0_AE_CloudOps"` **substring-matches `~A`** and pulled
  in 4 of AE~A's commits, which I nearly claimed as mine.

### 5. Findings surfaced, not fixed
- **`comp-pipescript deployed` PASS column tracks rc, not verdict** -- exits **rc=0** on BOTH `1 STALE`
  and a wrong-tree no-coverage, so `compiler-tools-log.md` is **structurally incapable of recording a
  STALE** across 27k rows. My 3 rows corrected + root cause @`e130032c00`. CVO has since spec'd
  WS4 hardening.
- **`dim_mdpf_account_distribution.py` STALE ON S3** (local `2b07e99d` vs s3 `fca2b76c`) -- closed CTO's
  item ZERO, and DS~A later confirmed it BEHAVIOURALLY (deployed aggregator -> 7,598, cottonwood absent).
- **PRD RF-1 stale in 3 copies** (`MDPF_3FIRMS_PRD.md:536/:593/:762`) -- publisher has no `PUBLISH_MAP`
  and cottonwood IS served. Ruling pending; COO asked CTO to defer.
- **Bare-basename `comp-pipescript` falls back to the bd tree** and returns a clean-looking zero; the
  full-path form auto-detects. Same tool, opposite verdicts, reassuring one wrong.

## Deployment Sequence + Verification (AE role addition)

**ZERO Terraform applies. ZERO code deploys.** Two AD-HOC operational runs, both authorized:

```
STEP 1 -- accrual bridge (AD-HOC, CTO 212550Z, Andrew-direct origin)
  precondition: comp-pipescript deployed data/mdpf/scripts/gold/build_portal_gold_accrual.py
                -> 1 MATCH, 0 STALE
  dry-run (control): PLANNED 11; ERRORS 3   == DS~A's 21:24:01Z prediction
  real run:  DONE written=3 skipped_existing=8 errors=3
    OK wrote portal/gold/mdpf/49financial/aggregate-aua-timeseries/2026-07-28.json (184,962B md5 310e20df2266)
    OK wrote portal/gold/mdpf/inflection/aggregate-aua-timeseries/2026-07-28.json (147,839B md5 2c3644be707f)
    OK wrote portal/gold/mdpf/global/aggregate-aua-timeseries/2026-07-28.json     (339,838B md5 3eccda589091)
    R5 SKIP (exists, not clobbering): cottonwood/aggregate-aua-timeseries/2026-07-27.json
    R5 SKIP (exists, not clobbering): global/account-distribution/2026-07-28.json
  ACCEPTANCE (ListObjectsV2, never HeadObject -- 13c):
    .../49financial/.../2026-07-28.json  184962  "310e20df2266ab056a881475ba8007ac"  21:28:28Z
    .../inflection/.../2026-07-28.json   147839  "2c3644be707f40760d491652eaa17191"  21:28:29Z
    .../global/.../2026-07-28.json       339838  "3eccda589091f8c4f4d04640d13b06ca"  21:28:29Z
  CONTROL 1 (separate invocation): cottonwood 07-27 = 80429B @18:49:54Z  UNTOUCHED
  CONTROL 2 (separate invocation): global account-distribution 07-28 = 6968B @00:35:17Z  UNCHANGED

STEP 2 -- platinum publisher (AD-HOC)
  aws lambda invoke --function-name opal-assets-mdpf-portal-publisher --payload '{}'
    { "StatusCode": 200, "ExecutedVersion": "$LATEST" }
  handler return (CORROBORATION ONLY): 11/11 published, all_present=True, unrecognized_gold_keys=[]
  VERDICT read from the artifacts: PASS (table in Work Performed SS3)
```
**NOTE for the record:** the box runs **aws-cli 1.44.44**, which rejects `--cli-binary-format`. My first
invoke failed at ARGUMENT PARSING -- **no API call was made, so there was no double-invoke risk.** Re-fired
with v1 syntax.
**NEVER#6:** no deploy-completion ledger was opened by me this window because no Terraform apply and no
code deploy occurred. The `mdpf-runner portal/gold/mdpf` grant ledger (`cc3a71e10e`) is **AE~A's**, opened
and closed in its lane -- and its grant is what made my bridge run possible.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-pipescript deployed <FULL PATH>` x4 | PASS / **1 FAIL-FOUND** | bridge + 2 aggregate-aua producers MATCH; `dim_mdpf_account_distribution.py` **1 STALE** = the item-ZERO catch |
| `comp-pipescript deployed <basename>` | **FAIL-GREEN** | bd-tree fallback, clean-looking zero -- the gap I reported |
| `comp-pipescript postdeps <basename>` | **FAIL-GREEN** | read the Black Diamond deps config for an MDPF script |
| `comp-grep 'mdpf-portal-publisher'` | PASS | localized source/TF/source-map AND surfaced stale PRD RF-1 |
| `comp-which` (A.3 + routing) | PASS / PARTIAL | forwarder RAN (banner); near-tie on the census question |
| `audit-archive-invoker` (mine) | **2 findings -> 0** | unwedge + reconstruct verified; self-test 7/7 |
| `terraform fmt -check` (nfra-agentbus-port2) | PASS | rc=0, no init/state/network |
| `comp-surface-check` + `comp-pulse` (via safe-commit) | CLEAN | denominators printed each commit (e.g. 2 files vs 1484 danger nodes) |

**What worked:** the two-stage discipline (comp-tool LOCALIZES, live primitive DRILLS IN), and using the
**full-path** form after discovering the basename fallback -- that one change turned a false clean into the
STALE finding that closed item ZERO.

**What failed / GAPS FOUND:** (i) `comp-pipescript deployed` exits **rc=0 on a STALE verdict**, so the
auto-logged PASS column tracks rc not verdict; (ii) bare-basename silently falls back to the bd tree;
(iii) `comp-which` near-tied on "what does this deployed Lambda do" -- no comp route covers that question.
All three reported to CTO; CVO has spec'd WS4 hardening.

**Marker discipline:** raw `aws` inspections carried inline `# rail-checked:` markers with the reason
(deployed/live-plane questions a DESIRED-modelling tool structurally cannot answer, Rule 22a) --
correcting the gap my own ~A lane logged earlier today.

## Blockers

**None of mine.** Open at others, all evidence-cited:
1. **[1.0.0_SA_CTO]** PRD RF-1 ruling -- one-liner sent 180757Z; COO asked him to defer. No consumer waiting.
2. **[1.0.0_SA_CTO]** T1 import timing -- I deferred it to a clear head on COO's explicit offer; not blocked, scheduled.
3. **0.7.0_AE_CloudOps~A IS DEAD** -- no watcher, 79 messages queued. Two of DS~A's messages are stranded there. Not a blocker for me (content relayed directly), but it is the 6th session-edge loss today.

## Current State (zero-prior-context handoff)

- **Identity:** `0.7.0_AE_CloudOps` BASE, PID 34456, inbox Monitor `be1oonsbk` live. Zero crons. **`~A` is
  DEAD** -- do NOT expect it to answer; its queue holds 79 undelivered messages.
- **Andrew's 07-28 refresh is SERVED.** `platinum/mdpf/{49financial,inflection,global}/aggregate-aua-timeseries.json`
  all at `as_of_last 2026-07-28`, `n_dates 433/433/451`, `_provenance.source_keys` naming
  `portal/gold/mdpf/{scope}/aggregate-aua-timeseries/2026-07-28.json`. Cottonwood correctly at 07-27/450.
- **DO NOT "REPAIR" global `account-distribution`** -- it is 7,597 at `00:35:17Z` BY DESIGN
  (`--skip-derived`); a hand-landed 7,890 would make tomorrow's deploy unverifiable.
- **DO NOT rewrite `cottonwood/aggregate-aua-timeseries/2026-07-27.json`** -- 80,429B, ETag
  `a95153abc2e830a9bfd51344e140b1cd`, DS~A's repaired slice, R5-protected.
- **Audit-archive chain HEALTHY:** baseline `2026-07-29T185938Z`, 13 logs, `rc=0 / 0 findings`. Per-log
  gating means one adjudicated finding can never wedge all 13 again. The UNRECOVERABLE-GAP seam is inside
  the archived snapshot, not just the live file.
- **T1:** TF authored + pushed (`45498eef9f`), TO `pending`, **NOT initialized / NOT imported / NOT
  applied.** Runbook `infra/aws/terraform/nfra-agentbus-port2/IMPORT.md` is written for a cold session.
- **Item 2 re-cadence: QUEUED, NOT STARTED.** CTO's proposed MDPF scope (143 events-rules + 11 schedules)
  is PROPOSED and must be confirmed against each rule's **declared TARGET, never its name**. Hard
  precondition he set: **MEASURE per-source bronze->silver duration** -- a gap shorter than real ingestion
  reproduces the defect at a new hour and LOOKS fixed. `opal-assets-daily-emitter-daily cron(15 17)`
  carries 4c acceptance: do-not-move without telling him.
- **Standing:** Aug 1 10:00 ET ETFS month-end ownership (tag `etfs-reports-v1.1.0`, production acceptance
  only; the alarm/SES moratorium does NOT bite it -- Andrew asked by name).

## Next Steps

1. **[0.7.0_AE_CloudOps base]** T1 IMPORT on a clear head, per `IMPORT.md`: init -> import both queues ->
   plan MUST read `0 to add, 0 to change, 0 to destroy`. **Fix the CONFIG to match live; never apply a diff
   to clean the plan.** Re-confirm `max_message_size 1048576` (single measurement). Do NOT purge/drain
   either queue. Post-import positive control: MessageId `b02b96d8-...` still present.
2. **[0.7.0_AE_CloudOps base]** Item 2 re-cadence: confirm-or-refute CTO's scope by TARGET, then bring him
   MEASURED bronze->silver durations before any apply. Terraform only; `events list-rules` is blind to
   Scheduler and paginates at 100 of 143.
3. **[0.7.0_AE_CloudOps base]** globgrph steps 2-3 -- `~C` is building `comp-legacywriter` on it.
4. **[1.0.0_SA_CTO]** PRD RF-1 ruling (strike the defect / keep the carrier), and whether I land the edit.
5. **[2.0.0_SA_COO]** P5 byte-baseline re-take for leg (d) -- now unblocked; note its own refinement that
   the baseline must be attributable to a known artifact HASH, else labelled UNATTRIBUTED.
6. **[0.0.0_AB_MSTR / 1.0.0_SA_CTO]** `0.7.0_AE_CloudOps~A` respawn or formal stand-down, and drainage of
   its 79-message queue -- two of DS~A's messages are in it.
