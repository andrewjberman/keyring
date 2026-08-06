# SEVEN DEFECTS FOUND BY RUNNING THE SUBDIVISION, NOT BY READING IT — and six would have shipped invisibly

**Seat:** `3.0.0_SA_CVO`. **Date:** 2026-08-06 ~16:00–19:30Z. **Andrew present and directing.**
**Method:** build the subdivided pipeline LOCALLY and walk it call by call BEFORE production code
exists. Andrew-direct: *"I want to locally run through this process so i can see for myself that it
works properly"* and *"find the failure points, and run a full run once those failure points are
rectified."*
**Egress:** every vendor call carried his explicit per-use word.
**Harness:** `kimi_pipeline.py` (this lane). **Spec implemented:** `SPEC_kimi_call_subdivision…` §4.

## Why this document exists

The layout was reviewed and sound. **Seven defects were found in the first two hours of RUNNING it,
and I had reviewed the same design without finding any of them.** Every one presents as clean output.

> **A DESIGN REVIEW READS WHAT THE AUTHOR MEANT. A RUN READS WHAT THE CODE DOES. Six of these seven
> produce a plausible number rather than an error, so no amount of reading finds them.**

## The seven

| # | Defect | Presented as | Found by |
|---|---|---|---|
| 1 | comp-tools not exec'able by shebang from native Windows; 3 of 4 strata dead | `INSTRUMENT_FAILED` (correctly) | first dry run |
| 2 | **DETECT budget 12,000 starved group B** | **`candidates_raw: 0`** | reading telemetry |
| 3 | A failed call recorded identically to an honest zero | `0 candidates` | consequence of 2 |
| 4 | Canon universe 386, prompt showed 80, undisclosed | nothing | self-review |
| 5 | **Evidence-citation control accepted fabrications** | **7 of 7 accepted** | mutation test |
| 6 | My own non-ASCII audit was structurally blind | `0 of 13 files` | re-derivation |
| 7 | **Degraded attribution load → empty canon → confident zero** | `0 candidates — the funnel working` | diffing two runs |

## The three that generalise

### 2+3 — THE STARVATION WAS HIDING FINDINGS, NOT PRODUCING AN ERROR

Group B at 12,000: `finish_reason: length`, **11,997 of 12,000 completion tokens on reasoning,
content 0 bytes.** Recorded as `candidates_raw: 0`.
At 32,000: `finish_reason: stop`, **15,572 completion tokens, 10 CANDIDATES.**

15,572 is **above the ceiling it was given**, so this is measured, not inferred. And the direction is
the dangerous one: **a tight ceiling fails silently, toward false confidence.** A day on which group
B starved would have read "no relationship drift found" when the truth was "nobody looked."

**Zero candidates is a RESULT. A failed call is an ABSENCE OF MEASUREMENT.** They must never share a
representation. Fixed: `status: DETECT_FAILED`, `unmeasured: true`, `candidates_raw: null`.

### 5 — A PREFIX MATCH ON A STRUCTURED STRING TESTS THE FORMAT, NOT THE CONTENT

The predicate was `ref[:24] in cited or cited[:24] in ref`. A stratum row renders as
`stratum row {"label": "producer:x", "paths": 4, …}` — **the first 24 characters are boilerplate
shared by every row.** A wholly invented `producer:NOPE-invented` PASSED.

**It accepted 7 of 7 live author calls and I was about to record that as the control working.**

> **A CONTROL THAT HAS NEVER REJECTED ANYTHING HAS NOT BEEN SHOWN TO WORK — IT HAS BEEN SHOWN TO
> RUN.** Only a deliberately fabricated input separated the two.

Repaired to require a content-bearing token to survive into the citation. Mutation 6/6: accepts real
citations and real nugget ids; rejects empty, unrelated, fabricated-row, and format-only mimicry.

### 7 — GRACEFUL DEGRADATION UPSTREAM IS A CONFIDENT ZERO DOWNSTREAM

One run reported *"0 candidates — a zero-candidate day costs nothing. This is the funnel working."*
**The canon universe was EMPTY (386 → 0).** Every candidate was rejected by construction; five vendor
calls were spent manufacturing a zero indistinguishable from a clean day.

Mechanism: a concurrent commit moved HEAD mid-run; `load_attribution_maps` runs
`git checkout <branch> -- <registry>` and **degrades gracefully by design** — each hop independently
optional, documented as such. The resolver hop failed, `prod_to_thread` returned empty, and nothing
downstream asked whether the result was USABLE.

> **GRACEFUL DEGRADATION IS CORRECT FOR ATTRIBUTION AND WRONG AS A SILENT INPUT TO A GATE.**

⚠ **THIS IS LIVE IN THE DEPLOYED RUNNER, NOT ONLY IN THE HARNESS.** If the resolver fails to load on
EC2, every path falls back to `area:*` and chain-resolution collapses — **which reads as "the
resolver is bad" rather than "the resolver did not load."** `maps["degraded"]` is computed and, as
far as I can see, never surfaced into the artifact. **Whether any historical chain-rate figure is
actually this is an OPEN QUESTION routed to `1.0.0_SA_CTO~B`** — I have NOT measured it, and it is
recorded here as a hypothesis, not a finding.

Fixed here: attribution health recorded in Call 0; DETECT **refuses to fire** on an unusable universe.
Mutation-proven both directions — healthy universe attempts the call, empty universe skips.

### 6 — I BROKE MY OWN AUDIT, AND IT REPORTED THE REASSURING ANSWER

My non-ASCII scan read raw file text. `json.dump` defaults to `ensure_ascii=True`, so the file
contains `\uXXXX` escapes and **the scan was structurally incapable of finding what it looked for.**
It returned `0 of 13`. Re-run against parsed values: **2 of 13.**
*Put the control on the RETRIEVAL, not the pattern.* Fifteenth-odd instance of that class at this
seat, committed while cataloguing it.

**AND MY FIRST MUTATION TEST OF FIX 7 WAS ITSELF WRONG** — it reported FAIL on the healthy case
because in dry-run *every* call is legitimately unmeasured, so `unmeasured` was never the
discriminator. **The test was wrong, not the code.** I would have "fixed" working code had I not
asked why it failed.

## What worked — keep it

- **Runner-side canon rejection FIRED LIVE.** Group A returned 8 candidates; **4 were killed in code**
  for naming entities that do not exist — `opal-assets-daily-emitter`, `inf-etf-monolith`,
  `mdpf-canrte-w1a-aggregate-aua-repoint`, `NFRA_COMPTOOL_USEPATHS`. Plausible, entirely invented.
  **That is the rejected-proposal class killed structurally instead of by hand**, and it validates
  CTO~B's `:26` line: prompt discipline is not a control.
- **Strata carrying denominator + vintage + an explicit `INSTRUMENT_FAILED` state** caught a real tool
  failure nobody planted, and the prompt correctly told the model the question was UNMEASURED.
- **Quality delta is real.** The monolith produced ONE proposal, *about the tool itself*. Subdivided
  produced **17 candidates** against actual naming and propagation drift, each citing a stratum row,
  with the model self-qualifying its weaker inferences.

## Rulings taken this session (Andrew, 2026-08-06)

1. **Canon scope: ORDER, never FILTER.** All 386 stay reachable; in-window entities sort first.
   Filtering to changed entities would structurally delete *"should have changed and did not"* — a
   legitimate Group A/B finding. *(Implemented; set-preservation verified 386 → 386.)*
2. **`.claude/` classifies as RECORDS, not resource.** A skill is instructions-to-an-agent, not an
   artifact a producer emits. 1–2 paths/day, so it changes no conclusion — but per Rule 24 a
   taxonomy value is **decided, not defaulted.** *(CTO~B leaned the same way independently.)*
3. **Cost/egress (§7 param 3) is PRICED.** See SPEC §7b.
4. **B6 capture uploader is the highest-value remaining item.** Everything built today makes the
   pipeline *correct* over evidence six days stale and topically one cost-audit session. **The
   subdivision is proven; the evidence feed is now the bottleneck.** Ahead of further subdivision
   polish.

## Standing limitation — not fixed by any of the above

**All 153 corpus nuggets predate the window** (newest source 2026-07-31; 120 dated 07-30/07-31,
33 undated, **zero in-window**). The runner declares this itself, which is the honest-degradation
path working. **Delivering 153 nuggets makes the model SEE them; it does not make them CURRENT.**
Until B6 lands, the corpus half of every report is frozen background.

-- 3.0.0_SA_CVO
