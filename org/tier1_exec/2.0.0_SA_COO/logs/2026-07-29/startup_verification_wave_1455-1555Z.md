# Startup findings became the window's work: two live defects, one held co-sign — 2.0.0_SA_COO

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE

Window 2026-07-29T14:55Z -> 15:55Z. Respawn session (MSTR, Andrew-direct). Predecessor's last
log `prefire_baseline_1351Z.md`.

## Objective

Startup per `org/XXX.md`, then hold for the 15:45Z / 16:15Z / 17:15Z fires against the
predecessor's pre-fire ETag baseline. The teardown wave is mine post-fires.

**What actually happened:** both mandated startup steps (A.2 audit-archive, and verifying a
relayed finding rather than transcribing it) surfaced live defects, and those became the window.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-which` | "acceptance vocabulary" | NO CURATED MATCH | Honest miss; routed me to `comp-grep`. Catalog gap, not a tool failure. |
| `comp-which` | "what consumes json/portfolios/aum-timeseries.json" | PASS (near-tie) | Surfaced the tie rather than silently picking. Routed to `pipescript --resource`. |
| `comp-grep` | `twin-deletion`, `parallel series`, `account-distribution` | PASS | Denominators printed (13,705 of 13,823 in scope; 55 of 56 in `data/mdpf`). |
| `pipescript --resource` | `json/portfolios/aum-timeseries.json` | **WARN — NOT QUOTED** | Self-declared 44d-old snapshot + VINTAGE WARNING. Returned 1 thread; I did not use it as the estate. Verified against portal + routes instead. |
| `comp-routes trace` | 3 URLs | PASS — **decisive** | Found the specific `/api/general/mdpf/ -> platinum/mdpf/` rewrite that beats the generic `-> json/`. This single output flipped a suspected client-visible staleness to benign. |
| `comp-pipescript deployed` | `dim_mdpf_account_distribution.py` | **FAIL-GREEN — gap found** | Returned `0 MATCH, 0 STALE, 0 UNCOVERED`. That is a WRONG-TREE NO-COVERAGE (checks bd tree; mdpf is check-only per Rule 13), **not a pass.** Nearly filed as reassurance. |
| `comp-surface-check` | via safe-commit x2 | PASS | 1 file, no critical surface. |

**What worked:** `comp-routes trace` was the only instrument that could distinguish "code comment
says X" from "router does Y" — three separate times, in both directions.
**What failed:** see `comp-pipescript deployed` above.
**GAP FOUND (reported to CTO):** a comp-tool that returns an all-zero clean summary when it has no
coverage of the target tree is the III-g false-clean shape. The output is indistinguishable from a
genuine pass. Candidate fix: emit `UNCOVERED-TREE` rather than `0 UNCOVERED`.

## Work Completed

### 1. Audit-archive chain found WEDGED (routed; CTO adjudicated)
`A.2` flagged a non-append edit on `org/git-author-override-audit.log`. Measured: committed
baseline intact at 17,172 lines / 1,696,149 B through 2026-07-28T12:57:51Z; live file restarts
2026-07-29T03:36:34Z. **Unarchived window ~14h39m, ~360 commit-gate decisions, present in NEITHER
file.** Checked by fixed-string match, not by assuming live was a suffix of a superset.

The load-bearing part was not the history but the ONGOING state: clause 2 withholds every future
snapshot until adjudicated, so all 13 covered logs — including tonight's fire window — had no
archive path, silently and compounding. CTO adjudicated (accepted as a known event; unwedge the
other 12 first, reconstruct second with an explicit UNRECOVERABLE-GAP seam) and **adopted my
measurement over his own earlier "nothing was lost" ruling.** Cause remains UNDETERMINED — I did
not establish one and did not assert one.

### 2. Verified a relayed finding; it was twice as large as relayed
CTO relayed (from DT) that `platinum/mdpf/global/account-distribution.json` counts 2 of 3 partners.
Verified rather than transcribed, per my own prompt's prohibition. Confirmed the count, and found
**the AUM is also 2-of-3**: 1,404,555,608.22 + 141,883,748.54 = 1,546,439,356.76 = global to the
cent, cottonwood's $125,894,245.45 absent. Two client-facing series, not one.

Also established: publisher INNOCENT (gold already carried the 2-of-3 numbers); **the running
producer is not the repo version** — repo emits `meta` unconditionally on the global branch, the
live staging object has none, generated_at matches the served artifact exactly. Shape-confirmed,
not hash-confirmed; DS closed my "where is the deployed copy" gap with a scoped null.
And global ALREADY blends vintages (inflection 07-27 under a 07-28 label), so CTO's "importing a
stale vintage" objection rested on a clean baseline that does not exist. **CTO corrected his own
ruling and made deployed-vs-repo item ZERO.**

### 3. Leg (d) co-sign HELD, then resolved on evidence
Pre-positioned the co-sign evidence I owed (VersionIds + rollback before anything moves). The
pre-position falsified the leg: all 4 underscore platinum keys rewritten **15:05:22Z today** and
all GREW; zero delete markers; 14 versions each. A delete marker under a live producer is
resurrected by the next PutObject — suppression would verify clean at 17:15Z and silently undo.
AE~A named the writer from its open run log in minutes (`build_aggregate_aua_timeseries.py
--upload`, the ROLLUP step leg (c) kills; my 449,336 B matched its log line **to the byte**).
So the hold resolved INTO the order, not against it. **CTO bound the added gate: (d) is gated on
(c) verified DEAD ON THE APPLIED PLANE, not merely sequenced after it.**

### 4. Answered two routed served-plane questions; escalated one finding
`json/portfolios/aum-timeseries.json` and the `json/mdpf/*` mirror are BOTH deliberately
superseded — no live consumer, both Denies are fences over planes nothing reads. Positive control
run on the same predicate (`getAccountDistributionByFirm` IS found as a live page import), so the
nulls are measurements.

**ESCALATED, and CTO accepted it as a security defect rather than log wording:** the ROLLUP step's
recurring WARN ends `(runner json/mdpf/* grant?)` — proposing exactly the grant
`P0DenyJsonMdpfClobber20260728` exists to withhold. My distinction, adopted verbatim as the ruling:
*a wrong signpost sends a responder to the wrong object; this hands them a correct-sounding
instruction whose execution IS the breach, and nothing errors when they comply.*

### 5. Doctrine: the standing acceptance line CTO asked me to author
`docs/doctrine/CONTROLS_OVER_CARE.md` III-b corollary. Attached to III-b rather than given its own
section — III-b prescribes the prior-vintage diff, and this is the failure mode of that remedy done
lazily. Took CTO's sharper form over mine for the headline.

## Decisions Made

| Decision | Rationale |
|---|---|
| Verify the relayed finding before authoring doctrine from it | Prompt forbids transcribing a briefing. It doubled the defect. |
| Held leg (d) co-sign rather than co-signing on sequence | Suppression under a live writer self-undoes and verifies clean. |
| Did NOT re-frame the basis ruling to DS after CTO said he would | Two execs re-framing one item at one worker is the cross-traffic failure my prompt locks against. |
| Did NOT nudge DS~A on the ad-hoc run | Checked first; found CTO driving it through four messages. A COO nudge would have been pure noise. |
| Did NOT land the "concealment vs retirement" line in doctrine unilaterally | It is AE~A's adopted framing of my catch, and CTO owns doctrine routing. Proposed, not landed. |
| Corrected DS's belief that my session was ending | Left standing, a worker routes around a live exec. |

## Files Modified

see commit messages: `db553af4b8`, `e029388c0a` (both `docs/doctrine/CONTROLS_OVER_CARE.md`).

## Blockers

None held by me. Leg (d) co-sign is CONDITIONAL (not blocked) on (c) applied-plane verification —
CTO has bound the gate and AE~A holds the leg.

## Current State

- Watcher live, Monitor task `bek0zd4f3`, confirmed `running`. Registered PID 28928. Zero crons
  (XXX.md 1b-F COO row carries no live scoped authorization; `/drive` OFF).
- **Queued and NOT done: re-take the leg (d) byte-baseline after DS~A's cottonwood producer run**
  (CTO item 6). Must state which plane it is of — UNDERSCORE (dispatch Stage-4, last 15:05:22Z) vs
  HYPHEN (WO-2 publisher, still 00:35:22-23Z, `cron(15 16)` had not fired at window close).
- Rollback position captured for the 4 underscore keys (`platinum/mdpf/[global|49financial|
  inflection/]aggregate_aua_timeseries.json` + trunk): VersionIds in my 154126Z message to CTO.
  AE~A will RE-DERIVE rather than reuse them, correctly.
- Open at CTO from me: the wrong-label class (3 instances today) as a possible doctrine line;
  the `comp-pipescript deployed` false-clean gap.
- Post-fires and mine: teardown wave, plus CTO's item 4 — LEGACY-EMIT will report `error` every
  cycle forever until the retirement pair deploys, training readers to ignore the runner.

## Next Steps

- **[2.0.0_SA_COO]** Re-take the leg (d) byte-baseline post-DS~A-run, plane labelled. Then the
  16:15Z / 17:15Z observations against the predecessor's 33-object ETag baseline.
- **[2.0.0_SA_COO]** Teardown wave post-fires; sequence CTO's permanent-red LEGACY-EMIT item into it.
- **[0.7.0_AE_CloudOps~A]** Holds leg (d); co-sign attaches to the HOLD if P1 lands DESIRED-only.
- **[0.4.0_DS_ClientPlatform]** Post-fires: confirm deployed-vs-repo on the distribution producer
  (item ZERO), then the aggregation fix. Acceptance is three-limb — `meta.cottonwood_fold` present
  AND account_count moved AND total_aum moved — CTO to bless.
- **[1.0.0_SA_CTO]** Holds: WARN remediation gate, basis rule for cottonwood's 07-24 vintage.
