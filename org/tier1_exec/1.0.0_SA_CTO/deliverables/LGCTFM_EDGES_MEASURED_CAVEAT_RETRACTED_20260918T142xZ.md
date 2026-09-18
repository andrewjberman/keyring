# `/legacy-transform`: the `edges: []` caveat I gave Andrew is RETRACTED, measured

**Written for Andrew**, closing a question I named as UNMEASURED in my ~14:2xZ answer and should not have left
open. Measured at `lib/opal_lgctfm.py` and the newest run's own artifacts.

## What I told him, and why it was a false alarm

I said: *"Dependency exists at the plan level ... but `contract.json.edges` is an empty list. So there's no
resource-level dependency graph in the contract. I'm not going to tell you whether that's unimplemented or correctly
empty."* ⛔ **THE PREMISE WAS WRONG: `edges` IS NOT A DEPENDENCY GRAPH AND NEVER WAS.**

**`lib/opal_lgctfm.py:1122-1171` -- `edges` is produced by the FORKS pass ONLY.** A FORK is *"two rows that are two
current spellings of ONE desired storage identity"* (a dual-write twin, or two surfaces sharing a registry mark).
Each edge is `{"from": member, "to": canonical, "type": "REPLACES"}`, emitted only when a group has **two or more
DISTINCT rows** and a canonical member can be chosen.

⭐ **SO `edges: []` IS A REAL MEASUREMENT WITH A MEANING: this subject has NO dual-spelling forks.** It is not an
unimplemented field. The PRD's line 176 -- the diagrams render *"from the contract's rows and edges"* -- is satisfied
by an empty edge set the same way a graph with no duplicate nodes is satisfied by no merge arrows.

## And the dependency half IS delivered, in full

**`plan.json`, measured: 1,074 packages = 179 tensions x 6 steps** (`MAP` -> `CLASSIFY` -> `RULE` -> `PORT` ->
`REPOINT` -> `PROVE`, 179 of each).

**Dependency-count distribution: `{0: 179, 1: 895}`.** ⭐ **895 of 1,074 packages (83.3%) carry a dependency, and the
179 that do not are exactly the `MAP` steps -- the first link of each chain.** Every non-first step depends on
precisely its predecessor: `R-0160-CLASSIFY` depends on `R-0160-MAP`.

⭐ **SO ANDREW'S "name and position and DEPENDENCY" IS MATCHED. The dependency is the EXECUTION ORDER, carried as a
strict six-step chain per tension, and it is complete rather than partial.** My caveat is retracted.

## One figure that bears on the MDPF-vs-ADVI question he asked in the same breath

⭐ **THE PLAN'S SIZE IS LINEAR IN TENSIONS: 179 tensions -> 1,074 packages, exactly 6 per tension.** A subject with
fewer tensions produces a proportionally smaller plan, and the per-package shape is identical. **That is a concrete
lever under his instinct that Model Portfolios is the lower-impact first run** -- not merely smaller in blast radius,
but smaller in plan by the same ratio, with nothing about the method changing.

⚠ **NOT MEASURED AND NOT CLAIMED: how many tensions an MDPF subject would produce.** No `/legacy-transform` run
exists for one -- `workflows/legacy_transform/` holds `blackdiamond-49financial` only. **The ratio is measured; the
MDPF numerator is not.**
