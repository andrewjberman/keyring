# ANDREW-DIRECT 2026-09-24 ~15:3xZ -- IRPT portal frontend candidates hand to 2.0.0_SA_COO~D to land on DEV

**Channel:** the 1.0.0_SA_CTO terminal, Andrew's answer to the CTO's AskUserQuestion, ~15:31Z.
**Recorded by:** 1.0.0_SA_CTO. **Context:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CRASH_RECOVERY_ADOPTION_20260924.md`
section 4. The question came from the placement of his earlier word to 2.0.0_SA_COO~D (msg 100713, ~14:0xZ):
"I think that you should be leading frontend for IRPT as a whole, none of the other COOs on IRPT are doing fucking
anything on frontend anyway."

## The question, verbatim

"You told 2.0.0_SA_COO~D it 'should be leading frontend for IRPT as a whole'. I've placed that as spoken: ~D leads
IRPT frontend and lands on DEV directly, with no gate on any other seat. Does 'leading' also mean the other IRPT
seats hand their portal frontend candidates to ~D to land? Today that's ~P's candidate 8, the DirectoryPage wire
contract."

The options offered, verbatim:
- "Yes, hand to ~D (Recommended)" -- "~P/~M/~Y keep backend and commit their own contract/fixture files, then hand
  portal candidates to ~D, which lands them on DEV. One integrator for IRPT frontend, matching 'none of the other
  COOs... on frontend'. ~P still saves candidate 8 first (A2 loss prevention)."
- "No, ~D's own work only" -- "~D leads its own IRPT frontend work. ~P/~M/~Y keep landing their own portal
  candidates under the current rules (test-only by the author; product files reviewed by the CTO)."

## The answer, verbatim

"Yes, hand to ~D (Recommended)"

## What it binds, and what it does not

- **2.0.0_SA_COO~D is the one integrator of IRPT portal frontend onto portal DEV.** This covers its own work and
  every IRPT portal candidate from 2.0.0_SA_COO~P, ~M and ~Y.
- **~P, ~M and ~Y keep the backend**, and each commits its own contract and fixture files on its own candidate
  branch. They hand the candidate to 2.0.0_SA_COO~D: one message naming the branch, the tip hash and the suites run
  on that tip. They do not land IRPT portal candidates on DEV themselves.
- **~P's A2 is unchanged and runs first:** commit candidate 8's two files and merge them up to origin/DEV's tip at
  the act. Its hand-off to ~D follows A2.
- **Not changed:** the CLAUDE.md Portal section as written. It is not a new gate and adds no approval step. No seat
  stops. Non-IRPT portal work is untouched.
