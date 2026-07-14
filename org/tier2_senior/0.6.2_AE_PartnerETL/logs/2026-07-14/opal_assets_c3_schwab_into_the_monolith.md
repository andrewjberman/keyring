# 0.6.2_AE_PartnerETL -- OPAL_ASSETS C3: Schwab into the monolith (prep -> apply -> land), and six instruments that lied until exercised

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, VALIDATE, DIAGNOSE, COORDINATE
**Date:** 2026-07-14 | **Window:** ~01:05Z -> 03:19Z | **Serial:** 0.6.2_AE_PartnerETL (respawned this session)

## Summary

Respawned as the worker Andrew's dispatch hold was waiting on. Ran OPAL_ASSETS C3 (Schwab into the new
consolidation monolith `opal-data-assets`) from PREP through APPLY to the first landed data source. Net end
state: **0833 (6,932 objects) is fully in the monolith, 3-tier verified, additive-only**; the producer IAM +
a scoped remap role + a Glacier RestoreObject grant are **APPLIED, 0-diff, and EXERCISED**; the daily puller
is retargeted to the monolith in code; and the 257 irreplaceable pre-floor objects are thawing from Glacier
in the background. Everything remaining on the main line is gated on ONE event -- the still-running 0824
wide-history pull terminating.

**Six instruments of mine lied tonight; every one was caught by a control, not by care** -- an all-zero
column census reading an inner zip as text (would have killed the 49F refactor on a false negative), a
head_bucket 403 reported as a nonexistent bucket (blamed C1 for my own condition), a `bc`-missing check
comparing two nulls and printing "stable," a half-verified apply matrix, the conditioned-ListBucket
`--context-entries` trap, and a `| head -3 && echo` reading a pipe's exit code instead of a 404.

## Work done

### 1. C3 PREP -- authored-not-applied (b8f3b79f7, a68d31ef7, e40854c23)
Monolith producer IAM (two identities: box write-only + a scoped remap role that cannot read the monolith or
delete anything), the remap script with a **3-tier ETag verify its ancestor never had**, catch-up + remap
plans. TWO findings that became PRD law: **F-1** "7,256" is a stale denominator still moving (would strand
~5,600 objects) -> ruling 13b (enumerate at run time); **F-2** ETag-verify false-fails on multipart sources
and the tempting fix removes the control -> ruling 13c (3-tier). Parser exercised on all 8,428 live objects,
0 quarantine, negative + positive controls separate. Surfaced the SSE fork to CTO rather than authoring a
speculative KMS grant; it was ruled AES256-only (13a adopted-then-REVERSED at v1.3.4) -- recorded the
reversal because a stale record states something false with authority.

### 2. The 01_raw pre-floor leg -- the ruling could not execute as written (6d030a99d, 7f3d725c6)
Andrew ruled the 257 pre-floor objects into the remap. Ground-truth found two blockers: **217 of 257 are in
GLACIER** (cannot CopyObject AND cannot read the H1 to observe the master), and the **TCF product uses a
different H1 layout** (master at field 3, not 2 -- and the naive fix reads a firm name out of an RLD file
without crashing). Built a position-independent H1 parser (scan-for-exactly-one-master; ratified, positional
indexing BANNED). Authored the RestoreObject grant per CTO's v1.3.8 ruling PLUS two statements he did not
name (ListBucket + GetObject -- flagged, not quiet: the master is only in the bytes, so an H1 read IS a
GetObject).

### 3. The 685MB blob incident + my orphaned commit
0.7.0's commit swept a 685MB terraform provider .exe into git; CLOUD went push-blocked for the whole fabric.
Diagnosed it, escalated (a forward delete-commit does NOT unblock -- the blob is in the pushed range), and
flagged that the obvious fix fails. Separately my RestoreObject commit `2d4dda428` was orphaned off the branch
by a `git reset HEAD~1` in the shared worktree (0.7.0's, owned by him). Reconstructed the mechanism from the
reflog, asked him not to gc/prune, and recovered it byte-identically (`git diff 2d4dda428` = 0 lines) as
`7f3d725c6`. Routed a gate candidate: `git reset HEAD~1` is unsafe in a shared worktree.

### 4. APPLY + the 22a triad closed (7f3d725c6, 1a7cbb3a5, tag schwab-si2-iam-v1.2.0)
safe-apply: 3 add / 0 change / 0 destroy, 0-diff verified. **22a simulate matrix on BOTH identities (15
calls, one --resource-arns each, controls separate):** the context-entries trap reproduced exactly as CTO
warned; every never-widen property provably denied incl. firm-sep explicitDeny and cannot-read-a-peer on the
monolith. Bulk restore kicked under the ASSUMED role: 217/217 issued, 0 errors -- DESIRED+APPLIED+EXERCISED,
no longer an inference. Caught my own --restore guard gating on the monolith (would make a C1-independent
thaw wait on C1) and the half-verified matrix (covered 1 of 2 applied identities).

### 5. C1 landed -> Schwab in the monolith (8ae4188ab, fd8dc016f, adea13886)
0833 remap executed: **6,932/6,932 copied, 0 failed**, 3-tier verify clean (set + size + ETag all
6,932/6,932), source intact, AC7 idempotency EXERCISED (re-run: 0 copied / 6,932 skipped / not error). 0824
NOT remapped -- still moving (13b). Caught the 403-vs-404 guard and the bc-null-comparison mid-execution.
Retargeted the daily puller to the monolith (C3(b) code, -Target monolith default + staging escape hatch, all
guards preserved, PS parse-clean). W4 landing-facts deliverable to DS with the container-chain provenance
grounded at the producer.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `terraform validate` / `plan` | monolith IAM + RestoreObject grant, plan-only then apply | PASS -- 3/0/0 twice; 0-diff after apply |
| `.tools/safe-apply.sh` | apply the grant (HALTGT checkpoint) | PASS -- 3 added, role live |
| `aws iam simulate-principal-policy` | 22a live matrix, both identities, 15 calls | PASS -- fully discriminating; comp-iam explicitly NOT used (fails green on new ARNs, cannot evaluate Conditions -- Rule 22a) |
| `.tools/commit-gate.sh` | Rule 14 on every .py touched | PASS (all clean) |
| `comp-grep` / `comp-which` | locate monolith grammar, PRD rows, OPAL_RUNNERS sec 4.3 | PASS |
| `aws s3api list-objects-v2` | run-time denominators, storage-class, ETag shape, container unwrap | PASS -- produced F-1, F-2, the Glacier finding, the zip-in-zip finding |

**What worked:** the 22a live matrix + separate controls caught the context-entries trap and proved
cannot-read-a-peer -- the load-bearing monolith property, now measured not commented.
**What failed:** the comp-rail correctly gated my raw `aws iam` matrix; re-ran with a `# rail-checked:`
marker (Rule 22a mandates the live primitive there -- comp-iam is structurally insufficient).
**GAP FOUND:** `git reset HEAD~1` is unsafe in a shared worktree (a claim about whoever committed last, not
your own commit) -- routed to CTO as a gate candidate with tonight's live instance.

## Deployment Sequence + Verification (AE)

```
IAM   monolith-iam.tf -> safe-apply -> 3 add / 0 change / 0 destroy -> 0-diff verified -> tag schwab-si2-iam-v1.2.0 (pushed --follow-tags)
      22a matrix: remap role (7 calls) + box role (8 calls), one --resource-arns each, positive controls separate -- all correct
RESTORE  Bulk/Days=14 under the ASSUMED scoped role: issued=217 already=0 errors=0 (217/217)
REMAP    0833: source 6,932 (run-time enumerated) | copied 6,932 | failed 0 | 3-tier verify 6,932/6,932 | AC7 re-run 0 copied/6,932 skipped
CODE     sdd-daily-pull.ps1 -Target monolith retarget (fd8dc016f) -- NOT deployed; box is mid-0824-pull
```
**LANDED (ground truth from S3):** `s3://opal-data-assets/schwab/08335338/bronze/` = 6,932 objects, 18 types,
monolith<->staging parity 6,932=6,932 verified. Source `opal-data-schwab/08335338/bronze/` UNTOUCHED.

## Blockers

**GATED (not blocked-broken) on ONE event: the 0824 wide-history pull terminating** (3,416 -> ~5,966 as of
03:19Z; a live REST pull under Andrew's direct GO). Downstream of it, in order: 0824 remap (13b -- waits for
terminal), C3(b) box-deploy + C3(c) NEW EventBridge schedule (my own discipline -- do not touch the box
mid-pull). Monitors armed on both the pull (terminal/stall) and the Glacier thaw (complete/progress/error).
Nothing is broken; the sequence is correct.

## Current State (handoff -- zero prior context assumed)

- **0833 IS IN THE MONOLITH.** `s3://opal-data-assets/schwab/08335338/bronze/{type}/{YYYYMMDD}/{vendor}.zip`,
  6,932 objects, byte-identical to `opal-data-schwab/08335338/bronze/` by 3-tier proof. Either location reads
  the same bytes.
- **IAM APPLIED + EXERCISED:** role `opal-schwab-monolith-remap-role` (scoped: read staging bronze, write
  monolith bronze, restore+read 01_raw; NO monolith read, NO delete anywhere) + box policy
  `quartz-si2-monolith-write` (write-only to schwab/{master}/bronze). Tag `schwab-si2-iam-v1.2.0`.
  **CLOSURE STEP PENDING (TO AC5):** the RestoreObject grant is REMOVED at migration completion, removal
  evidenced by a fresh live simulate showing implicitDeny.
- **257 GLACIER LEG:** Bulk restore issued 217/217, 14-day window, thawing unattended. When it completes:
  copy + 3-tier verify inside the window via `remap-bronze-to-monolith.py --source 01raw --execute`. BACKGROUND
  per Andrew (~02:41Z: "i dont care about the glacier schwab data that much to hold up our work here").
- **0824:** wide pull STILL RUNNING against `opal-data-schwab/08242234/bronze/` (~3,416/5,966). Its monolith
  remap runs when terminal: `remap-bronze-to-monolith.py --master 08242234 --execute`.
- **C3(b) CODE:** `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` -Target monolith (default) -- NOT
  deployed. Box-deploy (S3->box, Rule 12) waits for the 0824 pull to finish.
- **C3(c):** CREATE a NEW EventBridge schedule driving the REST puller (CTO ruled CREATE-NEW 030017Z; NO
  repoint). Dead GUI task + canonical-schwab-si2-download-schedule stay untouched.
- **Commits (all origin/CLOUD):** b8f3b79f7, a68d31ef7, e40854c23, 6d030a99d, 7f3d725c6, 1a7cbb3a5,
  8ae4188ab, fd8dc016f, adea13886. Tag schwab-si2-iam-v1.2.0.

## Next Steps

- **[0.6.2 self]** On 0824-pull-terminal: 0824 remap -> C3(b) box-deploy -> C3(c) new schedule. On
  Glacier-thaw-complete: 01raw copy+verify -> grant removal + implicitDeny evidence (AC5).
- **[0.4.0_DS_ClientPlatform]** W4 column half in flight; the JOINT gap list to Andrew is his+my call. Send
  him the terminal 0824 count when the pull lands.
- **[1.0.0_SA_CTO]** the `git reset HEAD~1` shared-worktree gate candidate (routed via COO).
- **[2.0.0_SA_COO]** C3(b) box-deploy + C3(c) schedule TF will route through you to CTO's gate when the box
  is free.

## MCP traffic

~30 messages. Significant: CTO rulings 13a(reversed)/13b/13c/v1.3.8-Glacier/C3(c)-create-new + the apply GO +
the W4 riders; COO relays (PREP GO, apply GO, RAVC-4 closes, Andrew priority inversion, the [STOP]/all-clear
on the blob rewrite); 0.7.0 (SSE answer, C1-live GO, the reset ownership); DS (W4 split, crs_reader T1
reconcile, the zip-in-zip save). Two Andrew-directs relayed via COO (01_raw kept; Glacier deprioritized) --
recorded verbatim in the TO chain.
