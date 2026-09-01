# The DE minimum I logged as a FAIL against myself, closed CLEAN — 0.4.0_DE_ClientPlatform~D

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Date:** 2026-09-01
**Task Order:** ADVI_PERFRP.TO-R1-DE (ad-hoc close-out of a self-reported gap)
**Status:** COMPLETE
**Portal DEV commits:** unchanged — `7d0ca60c` (origin/DEV tip)
**Workspace CLOUD commit:** this entry; prior window at `79d13d12c7` + `815767dad4`

---

## Objective

Close the one outstanding item that was mine and unblocked: the `comp-cache collisions` run I
recorded as a FAIL against myself in the previous log, having threaded `firmId` through seven
call sites including React Query keys without it. Short window, one check, one amendment.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-cache | `comp-cache collisions` | PASS | 118/118 call-sites captured, 0 unparseable, 0 type mismatches, 0 perfrp keys shared |

Verbatim, the two lines that carry the verdict and its denominator:

```
CACHE KEY COLLISIONS -- captured 118 of 118 useQuery call-site(s); 0 unparseable
  (useQueries / useInfiniteQuery / useAutoSaveQuery are NOT audited by this tool)
17 shared key(s); 0 with a TYPE MISMATCH (the bug-class).
```

**What worked:** the tool prints its own denominator and its own non-coverage on the same line as
the verdict, which is the shape that makes a green readable. The 17 shared keys are legitimate
sharing — one fetcher called from two components with identical arguments — and the tool separates
that from the actual bug-class rather than reporting both as findings.

**What failed:** MY FIRST RUN, and the failure was mine not the tool's. I piped it through
`tail -30` and read a truncated middle with no summary line and no denominator. That is CLAUDE.md's
"never `head` ANY census" verbatim, and it bites for the stated reason — a truncated pass and a
clean pass are indistinguishable. Re-ran unpiped to a file and took the summary and the denominator.
I have now hit this rule twice in one session from opposite ends: this, and reading `ls -l` local
time as UTC on a peer's merge.

**Gap found:** none new. The gap this run existed to close was a PROCESS gap with no defect behind
it, which is the honest outcome and the reason to run a minimum you skipped rather than reason about
whether it would have mattered.

---

## Work Completed

### 1. The DE minimum, closed

Zero of the 17 shared keys are perfrp keys. The keys added in `AdvisorBookView.tsx` for the
allocation and transactions leaves do not collide with anything, and estate-wide there are no type
mismatches — the bug-class the check exists for. The tool's declared blind spot (`useQueries`,
`useInfiniteQuery`, `useAutoSaveQuery`) does not cover my additions, which are plain `useQuery`, so
the green applies to them rather than merely not excluding them.

### 2. Amended the prior log so a closed item stops reading as open

Marked Next Step 3 CLOSED in `perfrp_r1de_delivery_and_chain_diagnosis.md` with the measured
result inline, rather than deleting the row. Same discipline as that log's steps 4 and 5: a
next-step a reader acts on after it is discharged is the stale-carrier failure the log's own
Postmortem is about.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Run the skipped minimum rather than argue it was unnecessary | I had no evidence either way; "the keys look namespaced" is not a measurement |
| Record it CLOSED-CLEAN, not retroactively downgrade the earlier FAIL | The FAIL was about the process gap and it was real. A clean result does not make skipping it correct |
| Keep the tool's non-coverage clause in the log | A green whose bound is not written down gets quoted later without it |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DE_ClientPlatform~D/logs/2026-09-01/perfrp_r1de_delivery_and_chain_diagnosis.md` | Next Step 3 marked CLOSED with measured result | this commit |
| `org/tier2_senior/0.4.0_DE_ClientPlatform~D/logs/2026-09-01/comp_cache_minimum_closed_1600-1620Z.md` | NEW — this entry | this commit |

No source changed in this window.

---

## Blockers

None. Nothing at this seat is waiting on another agent, and nothing is gated.

---

## Current State

TO-R1-DE's DE-lane scope remains COMPLETE on `origin/DEV` at `7d0ca60c1d` with no source change in
this window; the only open TO criteria are producer-side (`PRFR1DE-AC11` scoring barred pending the
weighting harness, `PRFR1DE-AC8` a producer-owned enum). The self-reported compiler-tools gap from
the previous log is now CLOSED CLEAN — `comp-cache collisions` reports 118 of 118 call-sites,
0 unparseable, 17 shared keys, 0 type mismatches, and none of the shared keys are perfrp. The chain
diagnosis this seat contributed measurements to has resolved to a FRAME defect rather than a
mechanism (08-29/08-30/08-31 all re-processed `asof=2026-08-28`, so three `built=6` observations
were one result repeated and the before/after comparison had no valid before); every mechanism
candidate is dead, including the dependency story its own author killed. The one finding of mine
that survives is unremediated and producer-lane: `chain_49f_entrypoint.py::_run_perfrp_projection`
has no floor on `built`, so `built=0 refused=11 hard_fail=0` prints `STAGE OK rc=0`.

---

## Next Steps

1. **When a publish lands, re-list the served plane BEFORE reading the render** — carried forward
   unchanged from the previous log; the pre-registered predictions are still unfalsified and the
   input state in that file is a measurement with a timestamp, not a constant.
2. **Build AC11 as `PRF-inv-3`'s RECOMPUTE** — recompute each level from the level below on the
   served block, print all three. Scoring stays BARRED until the weighting harness is live.
3. **[0.4.0_DS_ClientPlatform~G]** The missing `built` floor on the chain's perfrp stage — surfaced,
   not chased. A total failure and a by-design refusal set are currently byte-identical at the
   stage's own verdict line, which is how four days of a repeated as-of went unseen.
