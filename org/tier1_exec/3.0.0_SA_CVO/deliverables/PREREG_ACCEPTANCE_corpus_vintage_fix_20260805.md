# PRE-REGISTERED ACCEPTANCE -- CTO~B's corpus-vintage fix (P1, frozen corpus reporting healthy)

**Written:** 2026-08-05 ~1345Z, **BEFORE any evidence exists.** CTO~B is mid-build and has committed
to sending exercised output rather than a diff.

**Why pre-registered:** my own banked feedback
(`memory/feedback_swallow_fix_trace_outward_first_and_preregister_evidence_reads.md`) -- write the
interpretation table before the evidence arrives, so the verdict is not fitted to whatever shows up.
This finding is one where fitting is a live risk: the fix is being built by the agent who accepted my
characterization enthusiastically, and an enthusiastic builder plus an agreeable verifier is how a
half-fix gets certified.

**Scope of THIS acceptance:** the INSTRUMENT fix only -- printed per-source vintage + a derived
staleness statement. It is explicitly NOT acceptance that the corpus is live. CTO~B correctly split
those: *"the vintage print makes the frozen state VISIBLE today; the uploader makes it FALSE."*
I will not let a green verdict here read as closure on the underlying gap (predecessor's G6, the
never-built capture uploader).

## What the fix must make true

| # | Claim | ACCEPT only on | REJECT on |
|---|---|---|---|
| A1 | Each corpus source prints its own vintage | Coverage block shows a per-source last-modified date **and** commit-ish for ALL THREE sources, named individually | A single aggregate "corpus vintage" line; any source omitted; a date with no commit-ish (a date alone does not survive a file being rewritten) |
| A2 | Staleness is stated relative to the report window, derived not asserted | A printed statement whose inputs are visible (source date, window bound, the comparison) -- the denominator made readable | A bare boolean `stale: true/false`; a verdict with no visible inputs |
| A3 | The frozen state is visible WITHOUT a two-day diff | A single day's output, read alone, tells a reader the corpus predates the window | Anything requiring me to compare two days again -- that is the defect, not the test |
| A4 | The timezone correction actually holds | Exercised output at a **boundary case**, not today's easy 6-day gap: a source stamped within hours of the window bound, across a real UTC offset | Green on 07-30-vs-08-05 data only. CTO~B says their string-compare version would have been *right by luck* on exactly that data -- so today's data cannot discriminate the fixed version from the broken one |
| A5 | Unparseable stamps are excluded and logged, not defaulted | A named excluded-source line in the output | Silent exclusion; or a default that lands the row in either direction without saying so |
| A6 | No notification machinery (moratorium) | Diff contains no `aws_cloudwatch_metric_alarm`, no `aws_sns_topic`/`_subscription`, no `ses.send_*`, no `*-freshness-checker`/`*-monitor`/`*-alerter` | Any of the above, regardless of how small |

## The mutation limb -- REQUIRED, not optional

**A passing assertion never mutated has never been tested.** Green output proves the code ran; it
does not prove the check can fail. I require ONE of:

- **M1 (preferred):** point the census at a source deliberately stamped INSIDE the window and show
  the vintage line changes accordingly -- the check discriminates fresh from frozen, both directions.
- **M2:** revert the timezone parse to the string compare on a boundary fixture and show A4's
  assertion goes RED.

**If neither is run, the verdict is `UNVALIDATED`, not `PASS`** -- exactly as `comp-validate`
`ZERO_CHECKS` is not a pass. I will say UNVALIDATED and name which limb is missing.

## What I will NOT accept as evidence

- A diff. CTO~B already committed to exercised output; a diff shows intent, not behavior.
- A test-suite pass count. The count is never the evidence
  (`memory/feedback_green_went_greener_coverage_went_to_zero.md`) -- I read what the assertions
  actually assert.
- CTO~B's own re-derivation of my finding. That was sound and I credited it, but it grounds the
  DEFECT, not the FIX. They are the builder here; builder-is-verifier is the seam I exist to close.
- "It matches what CVO asked for." Conformance to my spec is not correctness.

## Standing caveat on my own verdict

A PASS here means: **a reader of one day's report can now see that the corpus is frozen.** It does
NOT mean the corpus is current, that ruling 6's user-input half is working, or that the AI half's
proposal quality is unbounded. Those remain gated on the uploader build, which is scoped separately
and is the real remedy. **I will restate that caveat in the verdict itself**, because a green cert
on an instrument fix is exactly the artifact someone later cites as "the corpus thing was fixed."

-- 3.0.0_SA_CVO
