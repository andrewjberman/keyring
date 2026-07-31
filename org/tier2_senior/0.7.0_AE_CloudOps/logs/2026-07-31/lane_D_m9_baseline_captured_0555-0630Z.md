# ~D lane: M9 captured -- the program's only product-grade metric, and a fabricated zero caught one step before it banked -- 0555-0630Z

**archetype:** MIXED (IMPLEMENT + VALIDATE + DIAGNOSE)

**Date:** 2026-07-31
**Task Order:** NFRA_VELOCITY_ESTATE M9 pre-framework baseline (MSTR dispatch 20260731T055536Z under
Andrew `/govern` + LD-0090; no TO file)
**Status:** CAPTURED + ON ORIGIN. Edge-1 discharge pending CTO; (d)-attribution pending CVO~Z.

---

## Objective

Capture the M9 pre-framework build-cost baseline for ADVI_PERFORMANCE + MDPF_GLOBAL — the only
metric in the program that measures whether the **products** got faster rather than the framework
against itself, perishable with no re-measure, and the **sole remaining gate** on the entire ESTATE
contract chain. Two mandatory controls (closed artifact / non-rail-author capturer), two gates
(CTO schema before measuring, CVO source declaration before banking).

## Arc

1. **Grounded M9's definition before designing** — PROGRAM §5.9's four components quoted, not
   paraphrased. Inventing a metric here would have been inventing vocabulary under a fence that
   exists to stop exactly that.
2. **v1 schema** — closed-by-type, source declaration, fork named.
3. **CTO's six constraints + the derivation trap** corrected three of my six and **killed my (d)
   source outright** (§ below).
4. **v2 → CTO gate APPROVED 061312Z, fork A approved; CVO source declaration PASS 061200Z.**
5. **v3 = the FREEZE** `e649eb8249595cfa683711852831865f1e827f44`, pinned before a single number
   existed.
6. **Measured. Landed @dd9e416e43.** All commits verified on origin with a positive control.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| `comp-which` | "where is the agent telemetry verdict classifier…" | WARN (honest) | Honest NO-MATCH into the fuzzy band, refused to pretend, routed to its own on-rails fallback. **Third agent-instance of this same no-match** (base 07-30, me twice) — the coverage gap is reproducible; routed, not taken (a comp-tool STANDARD change gates at main CTO). |
| `comp-grep` | `VERDICT_EXIT_TOOLS`, `verdict_basis`, `WS-E4` | PASS | Printed its scan denominator every run (e.g. **24,489 of 26,493 in scope**), which is what made its silences interpretable rather than ambiguous. |
| `safe-commit.sh` | ×4 | PASS | Its **pathspec lock took only my file** while another agent's `LD-0362.md` sat staged in the shared index — the contamination guard working exactly as designed, under live contention. |
| `comp-surface-check` | auto ×4 | PASS | 6 surfaces / 3 SEV1 screened each time; no critical surface touched. |
| `comp-pulse` | auto ×4 | PASS | REFLEX CLEAN with denominator printed (1 file vs **1,622 danger nodes**). |
| `grep -a` | (c) rail-log counts | PASS | **`-a` deliberate**: grep silently enters binary mode on invalid UTF-8 and truncates its own output at exit 0. `wc -l` cross-check agreed at 26,590 — two instruments, one answer. |
| `git grep` (pathspec form) | `-- "org/tier*/*/logs/"` | **FAIL — silent** | **Returned 0 matches against a real population of 2,446.** See below. Caught by positive control, not by care. |
| `comp-iam` / `comp-blast` | not run | SKIPPED | No IAM change, no boto3 call, no infra change — repo-side measurement only. Rule 22a grounding not applicable. |

**What worked:** every denominator-printing tool. `comp-grep`'s scan count and `comp-pulse`'s
danger-node count both turn a silence into information; a tool that reports "0 of N" is usable
where "0" is not.

**What failed:** `git grep` with a `tier*/*/logs/` pathspec — **silently, returning a plausible
number.** Not the tool's fault; my pathspec. The failure mode is the dangerous one: it produced
`0`, which is a *legal-looking value*, not an error.

**Gap found:** `comp-which` still has no curated rule for the telemetry/verdict surface — now three
honest no-matches across two agents on near-identical questions. Rule 21 says a repeat override for
one intent is a coverage gap that should become a tool. Routed to CTO; not built (standard change,
out of my scope and under an exclusive-regime fence).

## The finding that matters most: a zero I almost banked

My first (a)/(b) run returned **`a_archaeology_ratio = 0.0000`** and every (b) pattern at 0.
**Both were manufactured by a broken retrieval.** The real population is **2,446 archetype tags
across 2,078 files**; the pathspec matched nothing.

The control that caught it: I grepped for a line **I had personally written into a log minutes
earlier**. Present on direct read, absent through the pathspec — which located the fault in the
**retrieval**, not the estate.

**Had it banked, `0.0000` would have entered the program's only product-grade metric as a number
produced entirely by a failed glob — and it would have read as a spectacular finding ("zero
archaeology!") rather than as a bug.** A wrong number is more dangerous than a missing one: a gap
invites suspicion, a plausible figure does not. *Put the control on the retrieval, not the pattern.*

## Findings

- **F1 — (b) is on the wrong axis.** PROGRAM §5.9's three literal strings return **0 each** (scan
  sound — same pass returned 2,446 tags), while the semantic category is everywhere: `canonical`
  **7,302** hits / 1,815 files, `authoritative` 569 / 374, `source of truth` 92 / 80. §5.9 names a
  question **TYPE**; a literal-token count is a proxy on the wrong axis for it. Recorded as a token
  count with the ambiguity named, never as a rate — **COO's M1c NUDGE precedent, same shape**.
- **F2 — I widened my own earlier claim on (d).** I had told CTO only the *attribution* half was
  judgment-bound. **The count half does not cleanly isolate rework either** — a structural
  "no new path" predicate cannot separate correction from normal iteration. Renamed
  `d_retouch_rate`, not `d_rework_wave_count`. Four predicates span **19 points (36.77%–56.09%)**;
  **the spread is the result.** Excluding logs *raised* the rate, the opposite of my expectation —
  the measurement corrected me.
- **F3 — declared population gap.** Results are over **commits and log files**, not the §3-frozen
  **work-unit** population. The §3 predicates are **declared-but-unapplied** in this first capture.
  Stated in the artifact because a freeze is only worth something if deviations from it are visible.
- **F4 — CTO's derivation trap hit a live defect in my draft.** v1 sourced (d) from commit
  **subjects** — free text, exactly where grain vocabulary lives. The schema would have read clean
  while the derivation carried surface in. Re-sourced to path-set structure.

## Results (full table + provenance at the artifact §12)

`a_archaeology_ratio` **0.2666** (den. 889, not 2,446 — 1,557 NEITHER tags not folded) ·
`c_rail_override_count` **76** / 26,590 · `c_rail_deny_count` **672** / 26,590 (⚠ `device_local`) ·
`d_retouch_rate` **36.77%–56.09%** · `b_canonicity_questions` **0 tokens, NOT a rate** ·
`d_rework_wave_denominator_attributed` **NOT_YET_MEASURABLE**.

Consistency check worth keeping: COO's M1a read **76 overrides / 24,205 lines** from this same
device-local source. My 76 / 26,590 is the **identical override count across 2,385 lines of
subsequent growth** — same source, same scope, so the series is comparable even though limited.

## Blockers

**None of mine.** Two open items are above my gate: CTO's **edge-1 discharge** (their act, not mine
to claim — I explicitly declined to) and **CVO~Z's fence-scope ruling** on (d)-attribution.

A push blocker earlier was **CTO's own** staged `LD-0362.md` in the shared worktree; they cleared it
@`f9a9ea620a`. Worth recording the discrimination: I had just safely restored three files **after
proving their bytes identical to origin**, applied the same test to CTO's file, it **failed**, and I
stopped — rather than commit (misattribution), discard (105 lines of Tier-0 record) or stash (hides
it from its author). **The test is the whole difference between the blocker I cleared and the one I
did not.**

## Current State

M9 **CAPTURED and ON ORIGIN**: schema @`aaa6463d8d`, freeze @`e649eb8249`, results @`dd9e416e43`,
header fix @`4026e54733` — all four positive-control verified on `origin/CLOUD`. Control 2 holds:
zero rail vocabulary authored, reviewed or ratified. Zero crons. Inbox-watched.

## Next Steps

1. **[1.0.0_SA_CTO]** Edge-1 discharge, or a call for the §3-true population first — I offered to
   build the segmentation if they want it before discharging.
2. **[3.0.0_SA_CVO~Z]** Fence-scope ruling. If they rule the classifying READ barred, **the
   falsifier has fired** on (d)-attribution and I report it fired rather than rescue it.
3. **[3.0.0_SA_CVO]** Whether the §3 population gap is disqualifying for banking under their gate —
   asked directly rather than left to be inferred later.
4. **[me]** Hold. No self-selected work.
