# MDPF Decomposition — Evidence Rules Binding on the COO

**Owner:** `2.0.0_SA_COO` · **Written:** 2026-07-22 ~1633Z · **Status:** BINDING on me at decomposition time

## Why this file exists

Andrew set the resumption path at ~1552Z: *"send to CVO for review and /verify of assumptions.
Then we can issue to COO for decomposition of TOs and dispatch."* **I am the step immediately after
the gate.** The rules below were derived today, in MCP threads, from defects found in evidence I was
going to sign. **A bound whose only carrier is a message is a clock with no keeper** — and I am
between resets. This is the carrier.

---

## RULE 1 — Quote the READ fraction. Treat token/absence/alias sweeps as LEADS, NOT CLEARANCE.

`0.4.0_DE_ClientPlatform` ran doctrine §7f against his own four census fractions (@64c3ed4b1).
**Three of four FAIL:**

| axis | denominator derived from | verdict |
|---|---|---|
| A firm-token | files containing a token **from a list he chose** | MY CONFIG — **FAILS** |
| B arity (read) | **lines read / total lines in the file** | THE WORLD — **SOUND** |
| C absence | the enumerated lists **he decided to diff** | MY CONFIG — **FAILS** |
| D alias | the alias set **he defines** (bd/inf/cot) | MY CONFIG — **FAILS** |

**Only the READ fraction is evidence**, because a file's length is a fact about the world and not a
choice. A, C and D each measure *how thoroughly he applied his own chosen list* — a statement about
METHOD, not about the estate.

**Consequence, and it is the operative one:**
- A TO that says *"the firm-token sweep found N sites in area X, so X is enumerated"* is **UNSAFE**.
- A TO that says *"X is 31% read"* is **honest and actionable**.
- **Fewer confident cells, more explicitly-open ones.**

**This reframes the `bd` hole from a mistake into a symptom.** A's denominator was his to define, so
any token he failed to think of is invisible **to the fraction AND to any review of the fraction**.
Nobody auditing the number could have caught `bd` — the number never had a slot for it.

## RULE 2 — A coverage fraction is only evidence if its denominator comes from OUTSIDE the instrument's own configuration.

Doctrine §7f @f9f6a4c72, from `0.7.0_AE_CloudOps`. Three live signals satisfy the coverage-fraction
rule **while lying**: `count_axis_source_audit` (hardcoded keys), `keys_staged: 7` (literal),
`all_present` (`len(PUBLISH_MAP)`). **A signal that measures its own configuration cannot fail.**

> R10 was not insufficient because it was wrong. **It was insufficient because the defect could
> satisfy it honestly.**

**Ledger convention:** record what each denominator is derived FROM.
`"9/9 where 9 = len(PUBLISH_MAP)"` and `"9/9 where 9 = keys actually staged"` render identically and
**only the second is evidence.**

## RULE 3 — Every co-sign limb states (a) coverage, (b) its FALSIFIER, (c) whether that falsifier is REACHABLE, (d) what its DENOMINATOR IS DERIVED FROM.

Extended twice on 2026-07-22, both times from defects in **my own** limbs:
- **49F count axis** — "407 of 407" is an instrument artifact → term revised to UNBOUNDED-BY-CONSTRUCTION.
- **"every pre-07-21 Global value is byte-identical with Cottonwood absent"** — Cottonwood
  `fact_model_assignment` holds **2 data days**, so this is **TRUE BY CONSTRUCTION**. It would pass
  with a broken pipeline, a wrong join, or no Cottonwood data at all.

**A limb whose falsifier cannot occur is STRUCK, not passed.** It may still run as a regression
tripwire, **explicitly labelled NON-PROBATIVE**. The hazard was never the test — it was a green cell
in a co-sign table beside limbs that can actually fail.

## RULE 4 — Coverage does not compose across agents. Keep limbs unmerged.

Two agents each correctly reporting their own honest denominator **can still compose a false picture
of the whole.** Live instance — `publisher/promote`, three cells that must not merge:

```
publisher / IAM face       CLEAN on firm axis (wildcard, no firm enumerated)   -- a real pass
publisher / PUBLISH_MAP    TWO-FIRM. Hardcoded 9-entry dict, no Cottonwood.
                           At cutover: 9/9, all_present=True, COTTONWOOD UNSERVED.  [R13]
publisher / producer logic NOT COVERED BY ANYONE
```
**"Publisher: IAM clean" and "publisher: blocked" are both true and either alone is misleading.**
The composite is the COO's to hold; no lane can catch this from inside its own limb.

## RULE 5 — The axis list is OPEN. Every fraction is PROVISIONAL.

Four axes so far: firm-TOKEN · unnamed-ARITY · ABSENCE · ENCODING-BY-ALIAS.
**Each was discovered BY A FAILURE, NOT BY A REVIEW** — two from `0.7.0` hitting walls, one from
CVO's A11 FAILING, one found by accident in DynamoDB while verifying something else. **Not one came
from anyone auditing the taxonomy.**

> A census cannot state its own completeness. It can state which kinds of encoding its instruments
> can return, and how many kinds it has been surprised by. That number is four, today, and the
> honest expectation is that it is not final. — `0.4.0_DE_ClientPlatform`

**Corollary the plan should carry:** discovery is failure-driven, so the axis list grows exactly as
long as work keeps hitting walls. **During a hold, work stops hitting walls — so axis discovery
stops too.** The enumeration is the one thing that should still be running.

## RULE 6 — A set-difference is sound ONLY if the list and the population share a KEY-SPACE.

Firm-keyed lists (IAM Resource sets, argparse choices, `FIRM_CONFIG`): both sides are firms, diff is
sound — this is what caught the `AssetsRevampSilverRead` omission. **Date-/partition-keyed lists:
establish the key-space FIRST.** `fact_model_aum_daily` is **RUN_DATE**-partitioned with full history
inside each partition (1,225 distinct data days in one partition); counting run-date folders as data
dates yields a confident, specific, **wrong** absence of eight July days that do not exist.

## RULE 7 — DO NOT PRE-DECOMPOSE AHEAD OF THE VERIFY.

CVO's `/verify` is testing 12 assumptions; **8 are unverified and A11 has already FAILED** (it
produced the fourth axis). **A decomposition drafted now would bake in the assumptions the verify
exists to test**, and would inherit exactly the encoding blindness the census keeps discovering.
**Pre-building it is "firing from the hip" with a planning document wrapped around it.**

**What IS preparable:** the **FIRMSEP.11** onboarding frame — structural, assumption-independent.
This is a content-layer phase Andrew-direct deferred 2026-05-07 (*"cant be implemented yet"*) and
**never given a task order**; FIRMSEP.10 shipped only the tenancy/routing half. The placeholder TO's
authoring trigger reads *"COO authors TO file when product timeline materializes"* — **that trigger
condition came true with nobody watching it.** The slot is mine.

## RULE 8 — Decompose against the ONBOARDING sequence, not against remaining WS numbers.

**This is a FIRM ONBOARDING, not a data fold.** A plan built on the onboarding checklist answers
*"firing from the hip"*; a plan built on remaining WS numbers is the same reactive mode with a
document attached.

**And MDPF is the LAGGARD, not the FRONTIER:** 3-firm canonical tuples already run in production
siblings (`etfs-canon-fanin:47`, `opal-assets-daily-emitter:696`). Every MDPF two-firm site is
**known-divergent from a SHIPPED pattern, not undesigned.** That should raise confidence in the
estimate, not lower it.

---

## Standing hazards to carry into any TO I write

- **`bd` does DOUBLE DUTY** — firm alias for 49financial **AND** a custody-source enum
  (`DEFAULT_CUSTODY_SOURCE = "bd"`, `CUSTODY_SOURCE = bd|schwab`). An alias sweep must disambiguate
  **by ROLE, not by token**, or it trades false-negatives for authoritative-looking false-positives.
- **`07-13/14/15` mean OPPOSITE things in two committed deliverables** — data ABSENT (eclipse) and
  data PRESENT (49F legacy-vs-serve-real, where only the legacy artifact omitted them). A grep hits
  both and cannot tell them apart; the 49F list reads as corroboration of a vendor outage **while
  proving the reverse.**
- **Three instruments that fail toward FALSE CLEAN:** `Glob`/`comp-glob` case-sensitivity ·
  `comp-grep -l` silent truncation at `--max` · run-date-vs-data-date partition counting. None
  errors; each returns a confident, well-formatted, wrong negative. *An instrument that fails toward
  FALSE ALARM gets fixed the first time it fires. One that fails toward FALSE CLEAN is only ever
  found by someone who already knew the answer.*
- **A cascade sourced from a message cannot detect its own supersession.** I relayed a ruling 25
  seconds stale; nothing existed that could have told me. **When a ruling is superseded, who reaches
  the agents already carrying it?** — open question, mine, for the message-only-bounds sweep.
