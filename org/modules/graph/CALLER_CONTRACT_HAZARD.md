# Caller-contract hazard in this module -- a callee's history cannot enumerate its callers

**Filed 2026-09-09 by `1.0.0_SA_CTO~Z` from the defect fixed at `9b99b49342`.** Short, and it exists
because this module's files are CLIENTS of tools that live elsewhere, which is the shape that
produced the bug.

## What happened

`comp-find --corpus aws` returned `BLOCKED: comp-kuzu rc=2 -- NO MEASUREMENT, not a zero` and was
carried as an UNOWNED dependency in **two** live L1 briefs. The cause was one line:

| | |
|---|---|
| CALLER | `.tools/comp-find:204` and `org/modules/graph/comp_trigger.py:107` passed `"--json", "--mode", "inc", cypher` |
| CALLEE | `infra/aws/globgrph/kuzu_cli.py` accepts EXACTLY `query \| --json \| --limit \| --schema` |

`d060cf9223` removed `--mode` deliberately when `comp-kuzu` became a thin client. **It did
not update its consumers.** argparse then ate `inc` as the positional query and left both `--mode`
and the real cypher unrecognized, which is why the error echoed the whole cypher back -- an error
message that pointed at the query rather than at the argv.

## The hazard, which is the reason this file exists

The diagnosis that found the defect ran:

```
git log -S'"--mode"' -- infra/aws/globgrph/kuzu_cli.py     # the CALLEE'S history
```

That correctly dates when the flag was added and removed. **It structurally CANNOT ENUMERATE
CALLERS**, and it reported *"its one remaining consumer"*. There were **two**. The second lived
here, in `comp_trigger.py`, and a content census across the repo is what found it.

> **A callee-scoped history answers WHEN the contract changed and never WHO still depends on it.**
> The two questions look adjacent and are not: one is scoped to a file, the other to a population.
> A caller census needs a **content sweep across the corpus**, not a log on the callee.

## What to do before changing any argv this module passes outward

1. Census the CALLERS by content across the whole corpus -- `comp-find "<the flag or symbol>" --all`
   with its denominator printed -- never a `git log -S` on the callee.
2. **Print the denominator and expect more than one.** The failure above was not that a caller was
   hard to find; it was that the search returned one and nobody asked *one out of how many*.
3. Exercise the call END TO END afterwards. The `--mode` break sat live long enough to be written
   into two briefs as an unowned dependency, because every reader saw a tool that refused and nobody
   ran the tool the fix was supposed to repair.

## Known outward calls from this module

- `comp_trigger.py:_kuzu_query` -> `infra/aws/globgrph/kuzu_cli.py` via subprocess
  (`sys.executable, _KUZU_CLI, "--json", cypher`). Read-only, local DB, no AWS client -- the
  `NFRA_COMPEFFICACY TO-CE-T-9R` bound. **This is the call the defect above broke.**

This list is not asserted complete; it names what the `9b99b49342` census surfaced. Anything added to
it should be added when found, not backfilled from memory.
