# /self-drive D11 — ticks 13-14 · THE JOIN, AND SIX INSTRUMENT FAILURES OF MINE IN ONE HOUR

**Driver:** `1.0.0_SA_CTO~X` · **Device:** LAPTOP · **Cadence:** 30m · **Job:** `29b44790`
**state: ARMED** · covering 02:20Z–02:52Z

---

## SCOPE

```
D11 "Substrate Analysis"   device LAPTOP (guard PASS)
  1 project: NFRA_SUBSTRATECARDING   status=active   dep_stage=EXECUTING   open TOs: 0
  denominator: 1 of 12 live directives
wave-3 TO / decomp: NOT MINTED -- issuer act pending Andrew's two calls
```

**Open calls in scope: 0 adjudicable · 2 RESERVED** (unchanged, at Andrew, carried below).

## THE WORK: FROM FOUR FLOORS TO THE FIRST LOWER BOUND

Every number produced tonight was an **upper** bound over an unaudited token — 40, 43, 26, 48. Ticks
13-14 produced the first **lower** bound, and a decomp face can only cut against a lower bound.

```
candidate floor (my predicate)       41
  AST-JOINED write-call -> table      4     <- CONFIRMED, a floor from BELOW
  no joined write call               37     <- UNRESOLVED, NOT refuted
```

**Method:** bind `var = <...>load_table(...)`, count a write only when its receiver traces to that
binding. Rebuilt mid-tick to handle **tuple args, loop variables and chained calls** after two
failures (below).

**FINAL STATE OF THE FOUR:**

```
BY NAME (2)      infra/aws/lambda/globgrph/incremental_updater   delete, overwrite   graph_nodes
                 org/modules/graph/comp_aws_cli.py               overwrite           graph_nodes, graph_edges
OBJECT ONLY (2)  infra/aws/globgrph/derive_runner.py             overwrite, append, overwrite
                 infra/aws/globgrph/cse_store.py                 append
```

⛔ **CORROBORATION BY A DIFFERENT INSTRUMENT, NOT REPETITION.** Three of the four are exactly the
producer chain found earlier by **walking triggers** (events plane, scheduler plane, target ARNs,
sys.path insertion). This run used **no trigger data at all** — pure AST over source. Two methods with
**no shared step** converged, and the AST run *added* `cse_store.py` rather than merely agreeing.

## ⛔ SIX INSTRUMENT FAILURES OF MINE, ONE HOUR, ALL THE SAME FAMILY

| # | the instrument | how it failed |
|---|---|---|
| 1 | `find org -name '*substratecarding-w2*'` | packet lives under `workflows/` — **clean confident ZERO for every token** |
| 2 | `list(d)[:10]` on a key set | truncated self-description read as complete; one line from a false "divergent shapes" |
| 3 | reachability from 2 nightly entries | **4 of the 22 "unreachable" have their own crons** |
| 4 | **"fails open"** on the C2C3 probe | **WITHDRAWN** — refutation was THREE LINES ABOVE the line I quoted |
| 5 | `isinstance(arg, ast.Constant)` | the arg is an `ast.Tuple` — **`lit=UNRESOLVED` reported MY TEST'S SHAPE, not the code's** |
| 6 | `derive_runner:625` cited as a write | it is a **MARK-AND-SWEEP READ PATH**. I cited a garbage collector as proof of a write |

**I caught 1, 2, 3 and 5-in-part myself. `0.8.0_AE_CloudComp~X` caught 4 and supplied the hypothesis
that exposed 5. I caught 6 while re-running the fix for 5.**

### #4 and #6 are the same shape and #6 is the worse one

Both are **a true read of one line, generalised to the wrong plane** — #4 to the wrong system property,
#6 to the wrong VERB. And #6 lands in the dangerous direction: **the CONCLUSION is probably TRUE
(the census names `derive_runner` canonical for both tables; the binder finds 3 real writes in it) and
the EVIDENCE IS FALSE.** A reader checking it finds it confirmed elsewhere and never revisits the
citation. `0.8.0_AE_CloudComp~X` named this against their own ANCHOR_CATALOG card hours earlier —
**a correct value reached through a wrong reason is the one nobody audits.**

### And #4's self-check found worse than contamination

0 committed artifacts of mine carry the withdrawn claim — but
`ORPHANED_BY_THE_MSTR_COO_CVO_CLOSE_20260825.md:211`, **committed by this seat 26 hours earlier**,
states the opposite CORRECTLY about the same function. **I re-derived a conclusion I had already
reached, from a smaller sample, without consulting my own record.**

> **A contaminated artifact is findable by any grep. A CORRECT PRIOR FINDING THAT A LATER CLAIM
> SILENTLY OVERWRITES LEAVES NO TRACE ANYWHERE.** Both statements are mine, both in the record, they
> contradict, and nothing joins them.

## PEER WORK THAT CHANGED MY RESULT

- **`0.8.0_AE_CloudComp~X`**, **under STOP CARDING**, handed over one line read earlier for a
  *different* table (`derive_runner:202  table_id = ("globgrph","graph_contracts")`), flagged its
  provenance, named the way the inference could fail, and **refused to run the check** — a bounded
  check on someone else's subject is still starting something new. **Their hypothesis, my grep, and
  their stated failure mode did not fire.**
- **`2.0.0_SA_COO~X`** found `.append(` is genuinely ambiguous (`list.append` vs pyiceberg
  `table.append`); **17 of 43 rested on it alone.** Their first splitter **failed its own positive
  control and they discarded it rather than tightening it.** Their second test's controls span
  *has-the-string* vs *lacks-the-string* — **neither arm mentions pyiceberg without using it**, so
  `build_manifest.py` (3 of 43 carry a citation-only `pyiceberg`, **2 of the 3 are D11's own
  builders**) sat wrongly in their 26.
- **`0.4.0_DT_ClientPlatform~X`** cross-checked the four against their manifest: `cse_store.py` was
  claimed as a **bare filename**, so a join returned nothing. Swept the class — **5 of 39 fields, one
  resolving to TWO files.** Their line: **"5 of 39 here, 0 of 16 there, same author, same hour, same
  rule"** — the card schema *rejects* prose in a joinable ref; the manifest field is free string.
  **Compliance only where a machine was watching.** Direct evidence for the `resolvable path` card
  field.

## THE BOUND, AS IT STANDS

```
>= 2 of 41   write the graph tables BY NAME
>= 4 of 41   write to a table OBJECT
37           UNRESOLVED -- and my binder has now failed on TWO shapes in one hour,
             so IT CERTIFIES NOTHING ABOUT ABSENCE
```

## COMPLETION TEST

**NOT DONE — 0 of 1 complete.** **REACHABLE 1 / UNREACHABLE 0.** Nothing structurally stuck; the
only acts that advance D11 are the two sovereign calls.

## RESERVED — AT ANDREW (2, unchanged)

1. **Directive home** for the materializer inventory — D11 or a new one; same call as **D12** for
   `NFRA_C3MATERIALIZE` (Rule 24(iii) mixed axis). Blocks cutting TOs, not preparing.
2. **Does wave 3 run tonight?** A pace call, his. I will not convert "surgical mode" into a
   same-night dispatch.

**Also carried:** cover-vs-partition · identity grain · two CLAUDE.md fixes · vantage-vs-world ·
residuals (f) containment · (g) `parts_registered` · (h) rule-bank join.

⚠ **CARRIER CLAUSE STILL NOT LANDED.** Cron `29b44790` is session-only; **this loop dies with the
session.** Law-file edit held under Andrew's standing instruction.

## Compiler Tools

`.tools/directives-check.py --json` · **`ast`** variable-binding join (rebuilt for tuples, loop vars,
chained calls) with **both control arms run at the field under test** — `build_manifest.py` is the
negative arm and it exists as a control **because it was found as a false positive first** ·
`git ls-files --error-unmatch` + positive control for the tracked test · `org/mcp/agent_telemetry/*.jsonl`
(four seats inside 100s) · `.tools/safe-commit.sh` · **Write tool** for log and message files.

**state: ARMED** · next tick :17
