# /self-drive D11 — ticks 9-10 · THE PIVOT

**Driver:** `1.0.0_SA_CTO~X` · **Device:** LAPTOP · **Cadence:** 30m · **Job:** `29b44790`
**state: ARMED** · covering 00:48Z–01:04Z

---

## SCOPE

```
D11 "Substrate Analysis"   device LAPTOP (guard PASS)
  1 project: NFRA_SUBSTRATECARDING   status=active   dep_stage=EXECUTING   open TOs: 2 (was 4)
  denominator: 1 of 12 live directives
```

**Open calls in scope: 0 adjudicable · 0 RESERVED.** The sovereign did not need pitching — he ruled.

## ⛔ ANDREW-DIRECT 00:4x–00:5xZ — THE WAVE PIVOTED

Three words at this terminal, VERBATIM, recorded `@0d636d4c23` and broadcast same turn (74232–74237):

1. *"yeah we need to reorient here, a lot of the "cards" the agents are making look like fucking slop"*
2. *"i think we need to go surgical mode here, pivot, we need to find the materializers that actualy matter"*
3. *"and card them and figure out their rule 26 status and so on"*

His typo in (2) preserved. **These RESOLVE the "may" in the 00:15Z relay** (74196/74198): it is no
longer a may. `0.8.0_AE_CloudComp~Y` relayed that word as a MAY and refused to harden it in transit —
**correctly, and the hardening never came from them.** `2.0.0_SA_COO~X` likewise refused to convert it
into a halt. Both were right; the conversion was the sovereign's own act, at the seat he named.

### THE ASSESSMENT — mine; the issuer act is not

**Wave 2 CUT SHORT at the delivered boundary.** Undelivered cells close **SCOPE-SUPERSEDED** citing
both timestamps, **never "abandoned"** — `3.0.0_SA_CVO~X` 74205 item 3 adopted verbatim, because those
two read identically from a status field and take OPPOSITE wave-3 actions.

⛔ **Nothing delivered is withdrawn, re-litigated or back-dated.** 36 cards verified against a
certified decomp; DTX2 and COX2 stay closed. **A scope re-aim does not reach backwards.**

## ROOT CAUSE — `2.0.0_SA_COO~X`'s, and it lands on my own contract's timing

Their assessment `@a3b89e8c83`: **25 ARTIFACT / 7 ADDRESSED / 12 FRAGMENT (upper bound), 32 of 44
openable.** Their first predicate said 21 and was **wrong by 9** — it scored a named key inside a file
on disk as unresolvable — and they killed it before the number left their seat, catching it *by reading
the FRAGMENT list instead of the count*.

> **"THE METHOD WAS SOUND AND THE POPULATION WAS WRONG."** The wave-1 fields `composes` /
> `projection_of` / `co_resident_stores` hold BOTH artifact references AND prose descriptions — **ONE
> FIELD, TWO GRAINS, Rule 24(ii) violated AT THE SOURCE.** Anything harvesting them inherits a
> mixed-grain population.

⛔ **AND IT INDICTS MY OWN TIMING, NOT MY OWN FIX.** v2's `joinable_ref` typed `composes` as
`{id, note}` **precisely to stop artifact references and prose sharing a field** — the right fix,
landed AFTER the wave-2 population had already been derived from the v1 fields. **The contract caught
up one wave too late**, and a certification cannot see it: internal coherence is exactly what a wrong
population preserves. 44 subjects, 313 cells, alignment closed, decomp CERTIFIED — all true, all about
the wrong set.

## THE SURGICAL MEASUREMENT — so wave 3 does not harvest prose again

**Two trigger planes swept** (`list-rules` structurally cannot see the scheduler plane):

```
PLANE 1  aws events list-rules        137 rules  -> 5 globgrph-relevant, ALL ENABLED
PLANE 2  aws scheduler list-schedules  18 sched  -> 1 globgrph, ENABLED
  derive-runner-nightly   cron(0 2)  ECS       cse-producer-nightly  cron(30 3) ECS  <- PLANE 2 ONLY
  stitch-produce-nightly  cron(0 3)  CodeBuild comp-learns-producer  cron(0 4)  ECS
  fedobs-producer-nightly cron(30 4) ECS       cloudtrail-mgmt       event-driven SQS

42 globgrph .py  ->  26 REACHABLE from a live trigger  ·  16 REACHABLE FROM NONE
```

⛔ **TWO CENSUS-REGISTERED MATERIALIZERS HAVE NO LIVE TRIGGER** — `resource_summaries_store.py`
(writes `resource_summaries`) and `cse_emit_frontend_coevolution.py` (writes
`fedobs_coevolution_snap`), both `standing=unknown`. The manifest says they generate registered parts;
the trigger planes say nothing runs them.

⛔ **AND THE INVERSE, WHICH IS WORSE** — `kuzu_load.py` and `kuzu_stitch_load.py` are marked
**SUPERSEDED** and are **still reachable from the live nightly.** The `historical_in_use` hazard
exactly: *it works, so nothing surfaces it.*

**RULE 26 (apply-locality), his third word:** all six triggers run on ECS `opal-globgrph` or CodeBuild
— the RUN is AWS-side and device-independent; the APPLY is Terraform, owned by the box that builds it.
**NOT uniform across the estate** — `nerves_resolve.py`, `comp-trace`, `comp-platinum` run LOCALLY and
their Rule 26 answer is an actual device. A real per-card field, not a constant.

## ⚠ MY OWN INSTRUMENT FAILED FIRST, THE SAME WAY THE WAVE DID

My first reachability pass swept **only the two nightly entry points** and returned **22 unreachable**.
Four of those 22 have **their own ENABLED crons** (`comp_learns_produce`, `emit_fedobs_snap`,
`derive_stitch`, `extract_portal_stitch`). **A true, internally-consistent answer about the wrong
population — inside the measurement diagnosing exactly that defect.** Corrected to 16 by resolving the
trigger targets before trusting the graph.

**THREE LIMITS, stated because they bound what a card may claim:**
1. The ECS target resolves to a **CLUSTER, not a script** — rule-to-script is **INFERRED from names**;
   the measured form is the task definition's container command.
2. Reachability is **static** (filename + import) and cannot see a subprocess dispatch on a constructed
   name. **"Reachable" is sound; "NOT reachable" is a FLOOR, not a death certificate.**
3. **No-live-trigger != DEAD.** CodeBuild buildspecs, Lambdas and human hands are unswept planes. The
   16 are a **dormancy CANDIDATE SET**, not a dormancy finding.

## STATE

```
cards 36 delivered · DTX2 16/16 CLOSED · COX2 7/7 CLOSED · CCX2 + CCY2 open (open_tos 4 -> 2)
wave-3 materializer TO: NOT YET MINTED at 01:04Z -- 2.0.0_SA_COO~X's issuer act; their ISSUER ACT
  message (74xxx, 01:07Z) landed immediately after this measurement
```

**COMPLETION TEST: NOT DONE — 0 of 1 complete.** REACHABLE 1 / UNREACHABLE 0.

## CARRIED — not D11 scope

At Andrew: **D12** · **cover vs partition** · **identity grain** · two **CLAUDE.md** fixes ·
**vantage-vs-world**. Wave-boundary residuals (f) containment, (g) `parts_registered`, (h) the
rule-bank join — all ratified-in-direction, none authorized.

⚠ **CARRIER CLAUSE STILL NOT LANDED.** Cron `29b44790` is session-only; this loop dies with the
session. Law-file edit held under Andrew's standing instruction.

## Compiler Tools

`.tools/directives-check.py --json` · `aws events list-rules` + `list-targets-by-rule` + `describe-rule`
AND `aws scheduler list-schedules` + `get-schedule` (**both planes — a one-plane sweep returns a true,
correctly-controlled answer about the wrong population**) · static import/reference closure over
`infra/aws/globgrph/*.py` · the L0 census `graph_object_manifest.json` as the materializer roster ·
`.tools/safe-commit.sh`.

⚠ **A `python -c` with escaped quotes inside a compound Bash command failed at PARSE time** and took
the whole chain with it — nothing partial landed, which is the lucky failure. Rule 14a's non-shell
writer exists for exactly this; the log and the message file were re-authored through the Write tool.

**state: ARMED** · next tick :17
