# BRIEF: head truncation → page-1 semantics (INFRASTRUCTURE.TOOLS)

**Author:** 3.0.0_SA_CVO, 2026-07-29 ~16:05Z, Andrew-directed ("I want a brief about this, which
we will return to"). **Status: PARKED — decision-ready, no work authorized yet.**
**Purpose sentence:** when we return to this, the reader can decide whether to make
denominator+page-1 the estate's default output shape, without re-deriving the measurements.

## The observation (Andrew's)

Agents attach `| head -N` / `--limit N` to nearly every command. The Ns are neither random nor
instructed — they are three different regimes, only one governed:

| layer | who picks N | governed? | measured state |
|---|---|---|---|
| tool-internal `[:N]` slices | the tool's AUTHOR, frozen at write time | no | **81 of 93 comp tools** hard-slice; only **48 of 93 declare their denominator in output** (5-axis profile @9da30535c6 §5) |
| agent pipe-heads (`\| head -12`) | the AGENT, judgment at call time | no | ungoverned entirely; a wrong guess silently truncates evidence with zero disclosure |
| harness output cap (~30KB → file) | the harness | yes | discloses + persists overflow |

## The reframe (the part to return to)

The sin was never truncation — it is **undisclosed** truncation. The fix is not "bigger heads" or
classic pagination round-trips; it is **denominator + page-1 in one call**: every bounded output
states the population it was cut from and that a page 2 exists. The O2-fixed comp-grep is the live
reference: `200 matches; scanned 20,763 of 26,190; TRUNCATED at --max 200 — true total >=200`.
That is a LABELED PAGE. The agent then decides, informed, whether the tail matters (usually not).

Pagination primitives already exist everywhere (Grep `head_limit`+`offset`, Read `offset/limit`,
AWS `--max-items`+NextToken, S3 continuation tokens) — capability is not the gap; the default
output SHAPE is.

## The two-track fix (both already have homes; neither authorized yet)

1. **Tool side — rides T-3 as-is:** `o2_footer()` (SPEC_T3_O2_REFERENCE_COMP_FRESHNESS_20260729)
   retrofits page-1 semantics onto all 93 tools: examined-N-of-M + excludes + the C3a zero line.
   Reference implementation comp-freshness, then comp-pipescript/comp-glob. Owner: rail lane
   (0.8.0), already CTO-routed. **This brief adds no scope to T-3 — it names T-3's second
   dividend.**
2. **Agent side — one doctrine line + optional gate candidate:** *"a `| head -N` on evidence
   carries its count beside it"* (the Rule-22 print-the-denominator law applied to pipe heads;
   the count-first pattern is already banked practice — `wc -l` then head). Optional HUD nudge:
   flag `| head` with no adjacent count in the same command. CTO prices; moratorium-compatible
   (a gate/nudge, not a monitor).

## Economics (why default-pagination wins here specifically)

A wrong one-shot head either wastes context (guessed big) or double-pays the call (guessed small,
re-run — observed live: a head-80-then-tail-85 pair doing manual pagination badly). Count+page-1
in one pass is strictly cheaper than either failure mode, and the labeled footer costs one line.

## When we return: the two decisions

(1) Adopt the doctrine line into CLAUDE.md (candidate reconstruction already carries Rule-22's
denominator law — this would be one clause on it, not a new rule). (2) Build the HUD nudge or not.
Everything else rides T-3, which is already in flight.

— 3.0.0_SA_CVO
