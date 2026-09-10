# NFRA_REPORT ROUND 5 -- HANDOFF TO THE INCOMING COO

**From** `1.0.0_SA_CTO~Z` (L4 owner) · **2026-09-10 ~19:0xZ` · **ferried by Andrew personally**

> ⛔ **THIS IS A HANDOFF, NOT A SPEC. IT RESTATES NO OUTCOME AND NO CONSTRAINT ON PURPOSE.**
> The spec is the PRD and it is the only carrier. **A second document holding the same obligations
> is the exact defect that cost this project round 4** -- read section 2 before anything else.
>
> **THE SPEC:** `org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md` @`2b6cf72067`
> `ENDPOINT` = `FWD-1`..`FWD-21` · `§5a`/`§5b` = the recut constraints · `§8a` = the recut surfaces

---

## 1. WHAT HAPPENED, IN FOUR LINES

Round 4 replaced the daily 9 AM infrastructure email with a new renderer. It deployed correctly and
**lost the report's content**: AWS costs, OpenAI costs, the named error list, the written analysis
and the security trend all stopped appearing. Andrew read it and said *"This output is completely
inexplicable... we are lacking so many fields the old version had."*

**The engineering was sound. The specification it was built to is what failed, and that is L4's --
this seat's.** Nothing in section 2 is a finding against the outgoing COO lane or its workers.

---

## 2. THE THREE DEFECTS, SO THE RECUT DOES NOT REPEAT THEM

**(a) THE CARRIER.** Three outcomes were written in a separate addendum file and **never folded into
the PRD.** Round 4 was cut from the addendum, so 3 outcomes and 6 constraints stood in the room
instead of 12 and a full constraint set. **`C-COST-15` -- Andrew's own verbatim cost detector --
was simply not there.** Measured: the PRD carries `15%` three times; the addendum carried it zero.
⭐ **FIXED:** all 21 outcomes are now in the PRD's own `ENDPOINT` section and the addendum is a
pointer. **Do not create a second spec document for any reason.**

**(b) AN UNTESTED ARCHITECTURE CLAIM.** The addendum asserted the join was *"one substitution"* onto
*"the same row shape the compute functions already accept"* and told the cut to *"exploit it rather
than re-architect around it."* The shape holds a state and a change and **has no cell for a dollar
figure, a ranked list or free text.** The decomposition then asked whether the port preserved the
shape; **the question was whether the shape could carry the report.**

**(c) THE CHECK RAN AFTER THE IRREVERSIBLE ACT.** `C-NO-REGRESSION` existed, and the cell scoring it
was sequenced *after* the deploy. The check could not fire until the loss was live and had emailed
the reader. ⛔ **In this round, the before/after comparison gates the deploy. It does not follow it.**

---

## 3. THE SEQUENCE. `S21` IS THE ROOT AND NOTHING BYPASSES IT

| # | surface | why it is where it is |
|---|---|---|
| 1 | **`S21`** the thirteen-section renderer | **everything else renders through it.** Cutting any other recut surface first builds onto the shape that caused the regression |
| 2 | `S24` the day's file | independent of the renderer's look; can run alongside `S22`/`S23` |
| 3 | `S22` the readable HTML edition | needs `S21`'s output to have something to lay out |
| 4 | `S23` the lead lines | needs `S21`'s sections to write one line about each |
| 5 | `S25` the subject line · `S26` the security placement | both cheap, both after `S21` |

⛔ **THE BEFORE/AFTER COMPARISON IS NOT A SURFACE. IT IS THE DEPLOY GATE.** No deploy happens until
a named comparison against a saved copy of the old email shows every section present or its removal
recorded with a reason.

---

## 4. THE TRAPS. EACH HAS ALREADY BITTEN SOMETHING

| trap | what happens if it is missed |
|---|---|
| **`max_tokens` vs `max_completion_tokens`** | the AI call is rejected. Chat Completions wants `max_completion_tokens`; `max_tokens` is deprecated and refused by reasoning models; the Responses API wants a **third** name, `max_output_tokens`. The current code passes `max_tokens` at 4 sites -- correct for Anthropic, first thing to break on the switch |
| **the model identifier** | a wrong string **does not fail at build time. It fails at 9 AM in front of the reader.** Resolve `gpt 5.6` against the live models endpoint before hardcoding it, and say what you found |
| **reasoning tokens** | they are billed and live inside `completion_tokens_details`. A cost line rebuilt from response length instead of read from `usage` **understates spend silently** -- on a line this same report prints |
| **the provider is not what it looks like** | today's AI analysis is **Anthropic**, not OpenAI. The `openai_cost` section tracks OpenAI spend *elsewhere in the estate*. This is a provider switch: new SDK, new secret, layer change |
| **thirteen AI calls** | timeout. The function's limit is 300s and a live run already hit **174.6s**. One call returns all thirteen lines |
| **the archive bucket is public-adjacent** | `opal-data-portal-v2` is fronted by CloudFront. Whether `infrastructure/reports/` is reachable through it **was not measured and must not be assumed either way** -- establish it before adding a legend that makes every finding legible |
| **`aws lambda update-function-code`** | forbidden. The function's own Terraform says so. Artifact -> S3 -> `source_code_hash` -> `safe-apply`, and a change-management entry opened **before** the first deploy act |

---

## 5. WHAT IS ALREADY BUILT AND MUST NOT BE RE-BOUGHT

- **The port is faithful** -- 35 spec lines / 35 port lines / identical.
- **The 13-way section partition is complete**, every omission reasoned and its discrimination
  proven. The best artifact round 4 produced.
- **The deploy path works** -- right package, right wiring, ledger opened before and closed after,
  cold-start clean.
- **The prior-report loader already works** and is the delta substrate. Nothing to build for it.
- **The raw numbers were never lost.** Both dropped collectors still run every cycle and their
  values are still archived verbatim. **This is a rendering fix, not a data recovery.**

---

## 6. STATE AT HANDOFF

| | |
|---|---|
| deployed now | the round-4 edition, live since 2026-09-10T16:35:55Z |
| next fire | 13:00Z daily. **It will send the deficient edition.** Andrew has ruled this NOT time-critical and **no rollback is authorised** |
| rollback, if he changes his mind | one `safe-apply`. `format_report()` is intact and unreferenced at `lambda_function.py:2053-2492`; revert the call site at `:277` |
| open orders | `RP-s-23` and `RP-s-24`, both open, worker stopped mid-cell |
| preserved worktree | `C:/tmp/wk-report-4-4` holds **uncommitted** `BEFORE_AFTER.md` and `MANUAL_TRIGGER.md`. ⛔ **Do not `git clean` or remove it** |
| undiagnosed, carried | three manual sends fired where one was authorised (17:39:18 / 17:40:17 / 17:41:21Z); and today's 13:03:39Z scheduled run fired but no email from it reached Andrew. **Whether the OLD report had already stopped arriving is unanswered** |

---

## 7. WHAT ANDREW OWES, AND IT IS NOTHING

Every decision this recut needed has been given: all thirteen sections; the existing bucket rather
than a new one; OpenAI and `gpt 5.6`; OPSEC findings distributed into the thirteen; clinical voice;
no alarm vocabulary in the subject. **The cut proceeds without another word from him.**

⭐ **RULED 2026-09-10 ~21:1xZ AND NO LONGER OPEN.** Andrew-direct, verbatim: **"all recs approved
but call 3, dont need alarm."** He was asked whether *"runs every day without fail"* also meant being
told when it **breaks**. It did not. ⛔ **NO ALARM, NO DEAD-LETTER QUEUE AND NO FAILURE NOTIFICATION
IS AUTHORISED FOR THIS REPORT** -- not in this round, and not in a later one on the strength of a seat
re-noticing that the gap exists. The gap is known, named, and accepted by the only party who could
accept it.

**SUPERSEDED, PRESERVED AS WRITTEN:**

⚠ **The one thing he has NOT ruled on**, carried from earlier and still open: whether *"runs every
day without fail"* also means he wants to be told when it **breaks**. That would be an alarm, which
the standing moratorium reserves to his explicit word. **It is not in this round and must not be
built into it.**
