# COO~Z VALIDATION — W-F DETECTION HALF (`D7_TICKETING.WF-SITEZ`)

**2026-08-20 ~23:58Z · build `@bdd9aaa7c9` by `0.5.0_AE_OpalETL~Z` · validated by `2.0.0_SA_COO~Z`**

**VERDICT: PASS on the two load-bearing claims, both checked at this seat rather than accepted.**

## What I verified, and how

| claim | method | result |
|---|---|---|
| **INERT** — no production call site | `comp-find` whole-repo, denominator printed | ✅ **4 hits / 26,871 files**; the only source imports are `tests/test_sweep.py:16-17` |
| **STOPS AT PAYLOAD** — no transport | text grep, **then AST** | ✅ imports = `__future__, dataclasses, datetime, row_contract, typing`; **transport-shaped calls: NONE** of 25 distinct called names |
| module is non-empty (control) | function-def count | ✅ **5/5** named functions present |

### ⚠ My first check was the wrong instrument, on the exact axis being tested

My text grep for transport symbols returned **1** — which was **the module's own docstring** saying
*"resolves no recipient."* **The mentions-vs-use trap, inside the very check I ran to verify their
claim about it.** Re-ran by AST, which discriminates. *Their AST-over-text correction on their own
guards is why I knew to do that — the second time tonight a control they were forced to adopt turned
out to be the one I needed.*

## The WF-5 sourcing fork — it is not three-way

`CUTOFF_ET` lives as a ticket-api Lambda env var (live value 14:00, APPLIED plane). **Only the
`/submit` 201 echoes it (`lambda_function.py:355`); the LIST response the runner reads (`:410`) does
not.** So the runner cannot see the one source today.

**(a) cutoff in `runner_config.json` — EXCLUDED BY CRITERION, not preference.** WF-5 (`:302`):
*"the escalation boundary and the client-facing cutoff read from ONE source; a mutant changing the
cutoff moves the escalation with it (they cannot drift)."* **A config literal IS the second source.**

**(c) the clause thought to forbid it does not — and the cut is mine, so I can show it.**
`W-F:357-361` reads *"NO W-A [dependency] … touches the runner only, no Lambda leg and no laptop
apply"* — and the **struck line directly beneath** is *"~~if W-F needs `first_response_at`, this TO is
W-A-DEPENDENT and the Lambda leg is laptop-applied~~ — superseded."*

>> ⛔ **"NO LAMBDA LEG" IS A DESCRIPTION OF WHAT THE SHRUNKEN CUT NEEDED after Andrew removed the W-A
dependency. IT IS NOT A PROHIBITION.** It was written before this collision existed and answers a
different question — *"does this TO need W-A's Lambda work?"* — still no.
>> **SAME CLASS AS THE HOLD I MANUFACTURED AN HOUR AGO: a sentence true of its origin, read later as
a scope.** I wrote it; the builder caught it; **twice in one lane tonight.**

### What actually remains — one question

| option | WF-5 | cost |
|---|---|---|
| **(b)** `get-function-configuration` per pass | satisfied | **new AWS dependency on the live client-facing path, ~168 calls/day** |
| **(c)** add `cutoff_et` to the LIST response | satisfied **structurally**, free at read time | **one Lambda apply** (re-opens a laptop leg) |

**THE ONLY LIVE QUESTION IS WHETHER TO SPEND ONE LAMBDA APPLY TO AVOID A PERMANENT PER-PASS AWS CALL
ON A CLIENT-FACING PATH.** I recommend **(c)** and explicitly do **not** rule it — apply sequencing is
the `1.0.0_SA_CTO~Z` gate. **The analysis is done and the false constraint is cleared.**

## Why the fork holds nothing

The builder built with the cutoff **injected as a parameter**, so the detection logic is
**source-agnostic** — no rework either way, only a wiring line. **That is the difference between a
real dependency and the wrong-grain holds produced repeatedly tonight:** this one can sit at a gate
without stopping anything.

## Not covered, and correctly so

WF-2 / WF-6 / WF-7 / WF-8 all require the runner wiring — a separate act with its own A5–A7
obligation, deliberately not started while the transport question is open. **Moratorium satisfied by
explicit ask:** Andrew's ~20:45Z verbatim `@11d274f8c2` quoted in the module header as the
`andrew-asked` marker.
