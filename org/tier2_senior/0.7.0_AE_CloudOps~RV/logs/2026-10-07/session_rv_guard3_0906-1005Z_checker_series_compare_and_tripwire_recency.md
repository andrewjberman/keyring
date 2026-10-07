# Both Bloomberg detection gaps are closed and live: the checker now grades each benchmark series, the tplus1 tripwire each custom CIX series — 0.7.0_AE_CloudOps~RV

**archetype:** MIXED (IMPLEMENT + VALIDATE + DEPLOY)

**Date:** 2026-10-07
**Task Order:** `OPAL_BBGTML.TO-GUARD-3.checker-series-compare-and-tripwire-recency` (`<risk>WORLD</risk>`)
**Status:** IN PROGRESS — the build, the proofs and the merge are COMPLETE; V1 (the first live read at 11:00Z/11:30Z) is open by construction

---

## Objective

Close the two detection gaps Andrew approved at ~05:55Z: the 07:30 ET checker passed while a
benchmark series was days behind (gap 1), and the pull's tripwire passed while a custom CIX series
was frozen (gap 2, row `OPAL_BBGTML-Z-S5`). Site-Z Scheduled Tasks run the WORKING TREE, so the
build had to happen in a linked worktree and the merge is the deploy.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find 'CIX' integrations/bloomberg --files --limit 40` | PASS | Found the four CIX-bearing source files including the tzero tripwire's prior art and the pull notebook. 27 hits / 95 files, bands printed. |
| comp-find | `comp-find 'bbg_pkl_tripwire\|publish_to_portal' integrations/bloomberg --all` | PASS | **The decisive read of the session.** 12 hits / 95 files surfaced `publish_to_portal.py:64` pointing at the TZERO copy, which is what became row Z-S12. A filename-only search would have missed it. |
| comp-read | `comp-read publish_to_portal.py --for "how are custom CIX tickers defined..."` | PASS | Its QUALIFIERS band put line 62 ("Use tzero's regardless of...") in front of me without my asking the right question. That is the hit that found the asymmetry. |
| comp-read | `comp-read org/surprise_channel/OPAL_BBGTML/INVESTIGATION_v1.md --enumerate 'OPAL_BBGTML-Z-S[0-9]+'` | PASS | 25 hits, 11 HEADING / 13 FENCE / 1 PROSE — gave the next row id (S12) with its denominator rather than a guess. |
| comp-which | `comp-which "open a NEVER-2 change management deploy ledger entry"` | WARN | Correctly said NO CURATED RULE MATCHED instead of ranking a wrong tool as right. The honest miss sent me to `.tools/deploy_ledger.py`, which is the real contract tool. This is the WARN behaving exactly as designed. |
| comp-estate / comp-pipescript / comp-iam / comp-blast | — | SKIPPED | Non-application, stated rather than skipped silently: the AE minimums in `org/XXX.md` are scoped to gold-run triggers, `iam.tf` changes and infra changes. This order fires no gold run, changes no IAM and touches no infra — it edits two local Python files whose deploy is a git merge. `comp-pipescript deployed` has no S3 code prefix to grade here. |

**What worked:** `comp-find --all` plus `comp-read --for` found the tzero/tplus1 consumer split that
the task order itself did not know the full shape of. The order asked "say whether anything scheduled
runs it" — the comp-tools answered *yes, and here is the exact line*, which turned a one-line report
sentence into a grounded surprise row.

**What failed:** nothing returned a wrong answer. Two rail denials cost a round trip each
(`comp-find | head` and `comp-read | head` are refused because a pipe receiver can erase the
denominator) — correct behaviour, and the fix is the tool's own `--limit`/`--files` flags.

**Gap found:** none in the tools. One gap in *my* use of them is recorded under Decisions: I asserted
"no ticker is hardcoded" over the raw file bytes, which fired on a ticker named in a *comment*. The
assertion had to be narrowed to the executable path by tokenizing and dropping COMMENT/STRING tokens.

---

## Work Completed

### 1. Cell GUARD-3a — the checker (`integrations/bloomberg/pipeline/freshness_check.py`)

Added `grade_benchmark_series(payload) -> dict`: **pure**, body in / result out, no S3, no summons, no
log, no exit. After the existing date check passes, the **same already-read body** is graded per
series — every model's `benchmark_last_date.index` and `.etf` against `data_as_of`. No second GET, so
the new limb cannot fail for a reason the date check did not.

| new result | exit | Kind (existing `summon()`) |
|---|---|---|
| a graded series' date `!=` `data_as_of` | **4** | `SERIES-BEHIND` |
| the body cannot be graded per series | **5** | `SERIES-NOT-MEASURED` |

`entry_step()` answers both new Kinds, and both route **away from Step 2**: in this state the pull,
the Terminal and the pipeline are all healthy, so a credentialed sign-in cannot move a series that
stopped calculating at the vendor and would spend the lockout budget for nothing. The `SERIES-BEHIND`
text routes to "confirm at source, then the CIX owner re-saves and re-pulls"; `SERIES-NOT-MEASURED`
routes to the producer (the guard Lambda that emits the field).

**Precedence, outermost first:** SCHEDULE-GAP (non-returning) → CHECK-ERROR (3) → STALE (2) →
SERIES-NOT-MEASURED (5) → SERIES-BEHIND (4) → PASS (0).

### 2. Cell GUARD-3b — the tripwire (`.../tplus1/tools/bbg_pkl_tripwire.py`)

Added `grade_cix_series(return_daily, asof) -> dict` (pure) and `_check_cix_recency()`, which wires it
into `check_data_pkl` through the **existing** `_fail` path. Recognition is **read, never typed**: a
Bloomberg custom index carries a dot-prefixed ticker, so the graded set is derived from the frame's own
`bbg_ticker` column every run — 13 custom series out of 84 tickers, with the 71 vendor series named as
not-graded. UNGRADED is not PASS: a frame missing the columns, or carrying no dot-prefixed ticker at
all, FAILS, because this is a send gate and an absent check reads exactly like a clean one.

### 3. The proofs, on real objects

Both proof scripts live under `deliverables/`, read existing objects only, and write nothing to S3.
They also write nothing to `C:\opal-elev\freshness_check.log` or any inbox: the checker's
`LOG`/`ESCALATION` constants and `summon()` are redirected to a scratch recorder before `main()` is
called, so the artifact the first live read is measured from stays clean.

| | measured |
|---|---|
| `Qbef40yV...` 16:16:52Z | `SERIES-BEHIND`, 10 graded, **9 behind** — index 09-29 ×5, etf 09-29 ×4 (INT etf current) |
| `fxNfvcQ8...` 01:28:18Z | `CURRENT`, **10 of 10** on `data_as_of` |
| 10-06 12:29Z pull | **7 of 13** custom CIX behind, all at 2026-09-29, exactly the CRO trace's seven |
| 10-07 01:26Z re-pull | **13 of 13** reach the as-of |

`GUARD-3A: PASS` exit 0 (6 arms) and `GUARD-3B: PASS` exit 0 (5 arms), re-run from the **shared tree**
after the merge. Battery `12/12`, exit 0. AC3 reads `2 files changed` under `integrations/bloomberg/`.

### 4. The landing

NEVER-2 entry opened **before** the act (`7a8aa5e827`), merge `80bcd69f78` at **09:54Z — 36 minutes
inside the window**, both tasks read Ready/not-Running and zero live pipeline processes beforehand.
The merged blobs equal the worktree blobs I proved (`cfebeaf6af`, `b0551c6a59`); pre-merge shared bytes
were `9401801aa7` and `7e701740f8`, so the act moved both. Worktree and branch removed.

### 5. Row `OPAL_BBGTML-Z-S12` — the tzero asymmetry

The order asked whether anything scheduled runs the tzero copy. **It does**, and the answer needed a
carrier that outlives a report. `scheduled_daily_pull.cmd:180` runs `publish_to_portal.py`, which at
line 64 deliberately invokes the **tzero** tripwire as "the STRICTER instrument on the send path".

The scheduled path is nonetheless **closed by the tplus1 edit alone**, and that is measured, not
assumed: `run_daily_pull.py:246-256` runs the tripwire from its own `TOOLS_DIR` and returns its rc, and
the `.cmd` reaches the SEND LEG only on `RC==0`. The residual is the **hand-run** send, which two
documents instruct — it re-runs tzero only, which still has no per-series limb. An inversion of that
comment's own intent. INERT today because all 13 series currently reach the as-of.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| 3b compares against `maxd`, the as-of the tripwire already resolves — I did **not** rewrite `expected_asof()`/`BDay` to `lib/trading_calendar` | How the as-of is *resolved* is a different act from *grading series against it*, and only the second is in this order. The as-of resolution gates whether a pull is sendable at all; changing it as a rider on a detection cell would be the larger, unproven change. Flagged to the issuer as overrulable. |
| `SERIES-NOT-MEASURED` outranks `SERIES-BEHIND` | A body missing the field cannot have been graded completely, so reporting "behind" would overstate what was measured. Both facts still appear in the one summons detail. Proved by a dedicated precedence arm. |
| An AHEAD series folds into the `SERIES-BEHIND` summons rather than getting a sixth exit code | A benchmark dated past the model data is the same class of defect — the two dates disagree — and must never read as current. The direction is named in the detail, so no reader is misled. |
| New exits are 4 and 5 | In neither the checker's 0/2/3 nor the vehicle's 0/9/50 / 1,20,30,40 / 60-63 / 70-73. Two independent reasons, the second being that the checker is a separate task with its own log. |
| The NEVER-2 entry was opened in the **shared** tree, not on the branch | The merge had not happened yet; if it half-failed the shared tree must still carry the OPEN state for a peer reading `.open_deploys/`. The documented worker pattern (entry rides the branch to the drain) exists for workers, and the exposure window here is the merge itself. |
| The surprise row went to the **shared** tree, not the worktree | Rule 14b inverts for an append-only shared file: two branches appending to one channel land at the same offset and guarantee a conflict. Verified append-only by asserting the pre-image is a byte prefix of the post-image. |
| Merged at 09:54Z rather than waiting for the post-12:00Z gap | The window was open with 36 minutes to spare, both tasks were Ready, and merging before the fires means the first live read happens *today* at 11:00Z/11:30Z instead of tomorrow. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `integrations/bloomberg/pipeline/freshness_check.py` | per-series benchmark compare; pure grader; 2 new Kinds + exits 4/5; `entry_step()` branches | Yes — `cd455fddab`, merged `80bcd69f78` |
| `integrations/bloomberg/pipeline/tplus1/tools/bbg_pkl_tripwire.py` | per-series custom-CIX recency via the existing `_fail`; `CIX_PREFIX`; pure grader | Yes — `a3c816be51`, merged `80bcd69f78` |
| `.../deliverables/guard3a_checker_proof.py` | AC1 proof, 6 arms | Yes — `cd455fddab` |
| `.../deliverables/guard3b_tripwire_proof.py` | AC2 proof, 5 arms | Yes — `a3c816be51` |
| `org/surprise_channel/OPAL_BBGTML/INVESTIGATION_v1.md` | row `OPAL_BBGTML-Z-S12` appended | Yes — `c405c95512` |
| `org/critical_paths/.open_deploys/bbgtml-guard3-*.json` + its `change_management/*.md` | NEVER-2 entry, M1 closed | Yes — `7a8aa5e827` |
| `.../deliverables/TO_GUARD_3_REPORT_1_MERGE_LANDED_20261007.md` | report 1 of 2 | Yes — `2e50c18d45` |

**Push state, MEASURED:** **LOCAL @`80bcd69f78`** — `git ls-remote origin CLOUD` read `75c5672586`
at 09:57Z. Nothing of this act is on origin; this seat commits and never pushes.

---

## Blockers

**None owed by this seat.** V1 is open by construction, not blocked: it waits on today's 11:00Z
vehicle fire and 11:30Z checker fire, which are scheduled events, and a waiter is armed on both logs.

---

## Current State

The two edits are **LIVE in the shared working tree** as of merge `80bcd69f78` at 09:54Z — on site Z
the Scheduled Tasks run the working tree, so there is no separate activation step. `freshness_check.py`
(363 lines, blob `cfebeaf6af`) now exits 4/5 with a `SERIES-BEHIND`/`SERIES-NOT-MEASURED` summons when
the body date is fresh but a `benchmark_last_date` is not, and `tplus1/tools/bbg_pkl_tripwire.py`
(299 lines, blob `b0551c6a59`) fails the pull when any of the 13 dot-prefixed CIX series in
`return_daily` misses the resolved as-of. NEVER-2 entry
`org/critical_paths/change_management/20261007T0949Z_bbgtml-guard3-checker-tripwire-merge-20261007_deploy_completion.md`
has **M1 CLOSED, V1 open**, window 5.0h from 09:49Z. Report 1 is delivered to `2.0.0_SA_COO~Z`
(msg at 09:59:58Z); the `<status>` flip and row `Z-S12`'s disposition are the issuer's.

---

## Next Steps

1. **Read the first live read and grade V1** — today's 07:00 ET vehicle tripwire result (11:00Z) and
   07:30 ET checker result (11:30Z), from their own logs. **A caveat stated now rather than discovered
   later:** the 2026-10-06 fire read `LastTaskResult 267014` with DAPI down and the pull never
   attempted (row `Z-S11`). If today's fire repeats that, the tripwire leg **NOT RUN**, never PASS —
   I will say which happened rather than read silence as success.
2. **Send report 2 and close the ledger** — or, on a FAIL against CURRENT data, revert the two edits
   within the hour (one revert commit) and report that instead. A FAIL because the data really is
   behind is the build working: report, do not revert.
3. **[`2.0.0_SA_COO~Z`] Flip `<status>` and disposition `OPAL_BBGTML-Z-S12`** — the residual hand-run
   send path needs a new order or an amendment; this seat's bounds name only the tplus1 copy. Three
   remedies are listed in the row, the smallest being to port the same limb into the tzero copy.
4. **[`0.0.0_AB_MSTR~Z`] The push** — CLOUD is diverged (MSTR~Z reported 4 ahead / 132 behind at
   launch); everything above is LOCAL and waits on the integrator's merge on Andrew's word.
