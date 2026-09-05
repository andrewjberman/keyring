---
name: verify
description: Validate that something is actually COMPLETE and correct on three axes -- MECHANICAL (does it really work, run, connect, exist), DECLARATIVE (does the record match the implementation), SEMANTIC (is the output the right thing with validated quality). Grounds against the real artifact or live state, never a self-report; could-not-verify is a finding; the verifier is not the do-er. `/verify <target>`; the completion gate in /goal-set. Any agent.
---

# /verify -- is it actually done + right? (mechanical / declarative / semantic)

One grounded completeness check across three axes. The rule it exists for:
**"complete" is a CLAIM, not evidence** -- a status marked done, a step said finished,
a config that looks wired -- none prove the thing actually works, matches its own record,
and carries the right content. `/verify` proves it against ground truth.

## Grounding discipline (binds all three axes -- non-negotiable)
1. **Ground vs the REAL artifact / live state** -- the actual file, output, or running
   thing; never a self-report, a "ran fine" claim, or stale memory. Read it yourself.
2. **Sharpest-test-binds** -- pick the check most likely to FAIL. A coarse pass that
   misses a sharp defect is not a pass.
3. **Could-not-verify is a FINDING** -- "UNVERIFIED, here's why," never an assumed clean.
4. **Verifier != the do-er** -- whoever built the thing doesn't get to bless it; bring a
   second set of eyes where it matters.
5. **Exercise-or-evidence** -- a configured path is not a firing path. Trigger it and
   observe the effect, or find real evidence it ran -- not just that it's set up.

## The three axes -- run each, name a verdict + cite the evidence
| Axis | The question | PASS = | FAIL = |
|---|---|---|---|
| **MECHANICAL** | Does it actually work -- run / connect / exist / fire / take effect? | the flow demonstrably happens (exercised or evidenced) | no-ops / mis-routes / never fires / errors / built-but-not-live |
| **DECLARATIVE** | Does the record (name / doc / status / spec) match the real implementation? | claim == reality (knowledge parity) | drift -- "claims X, actually Y"; a name that lies; a stale "done" |
| **SEMANTIC** | Is the content/output the RIGHT thing, quality-validated? | correct values + sane magnitude/sign/units + decision-useful | wrong values / stale / right-shape-wrong-meaning / wrong grain |

For each axis: state the verdict and the **evidence** (the number, the file, the live
read) -- not "looks fine." Skip an axis only with a one-line "N/A because..." (a pure
function has no live state), never silently.

## Verdict
- **SOUND** -- all three axes PASS, evidence cited. Only now is the thing "done."
- **BROKEN@<axis>** -- name the axis + the exact break (expected vs actual).
- **UNVERIFIED@<axis>** -- couldn't reach ground truth; say why. Never silently upgraded to PASS.

A thing is complete only when `/verify` is **SOUND** against its acceptance criteria. If
BROKEN / UNVERIFIED: STOP, report the finding (don't fix it if you're not the owner) +
route it back to whoever owns it.

## Notes
- This is the **gate in `/goal-set`** -- the loop runs `/verify` at completion; if it's not
  SOUND, the loop adjusts and keeps driving.
- **Verify-not-fix:** finding the defect IS the deliverable; route the fix to the owner.
- A render / display claim verifies on the path the **real user hits**, not the source data.
- Scale-flexible: a single function/file (just the relevant axes), a producer->consumer
  handoff (all three), or a whole pipeline (decompose into links, weakest-link binds).
