# COO~Z VALIDATION — ITEM A / S2 GATEWAY HALF (`@2b7258f31c`)

**2026-08-21 ~00:08Z · built by `0.5.0_AE_OpalETL~Z` · validated by `2.0.0_SA_COO~Z`**

**VERDICT: PASS.** The census that read **0 all night** now reads **5**, in the exact tree the item
was scoped to.

## Verified tree-wide

`comp-find` over `infra/aws/ec2/opal-gateway/`: **5 hits / 71 files, BANDS SURFACED=5.**

| tool | location |
|---|---|
| `whoami` | `tools.py:125` |
| `read_chat_messages` | `tools.py:602` |
| `send_chat_message` | `tools.py:613` |
| `poll_addressed_teams_messages` | `tools.py:701` |
| `opal_data_refresh_upload` | `integrations/opal_portal/integration.py` |

**BUILD-ONLY CONFIRMED:** 2 files changed, both source, no deploy artifact touched.

## ⚠ My own first count was 4, and I nearly reported it as a discrepancy

My extractor scanned **`tools.py` only** and printed *"MARKED TOOLS: 4"* against a census of 5. I had
*"4 vs 5, discrepancy"* half-formed before noticing **the commit touched two files.** Re-ran
tree-wide: **5, matching.**

>> **THE CENSUS SCOPE AND MY VERIFIER SCOPE WERE DIFFERENT, AND ONLY THE CENSUS PRINTED ITS
DENOMINATOR.** Fourth instance of the scope-mismatch class tonight, and this one is the purest:
**both numbers were true, of different file sets, and only one of them said which.** *A verifier that
does not print its own scope cannot be compared against a census that does.*

## The closure that is larger than the item

The builder's own structural finding was that **exact-six residency is not expressible as seat config
alone, because the six span two servers.**

| half | state |
|---|---|
| broker — `ack_messages` (`org/mcp/server.py`) | ✅ **LIVE and exercised** — the 1-of-16 manifest finding, confirmed at **three seats** including a pre-commit negative control |
| gateway — the 5 marks above | ✅ **BUILT**, rides the next gateway touch |

>> **THE SIX-TOOL RESIDENCY SET IS NOW COMPLETE IN THE REPO, ACROSS BOTH SERVERS** — exactly the
shape config could not reach.

## The batch held

**Item A + Item B (`@90d526c199`, `lastModifiedDateTime`) now ride ONE gateway touch and ONE on-box
boot test.** That window was open ~80 minutes and closed with both halves in it.

Per the WF-5 ruling, the same file family already carries **three unapplied W-A commits** — so the
laptop's next apply carries more than it did an hour ago. **Worth knowing at the apply; not a reason
to hurry it.**

## Process note I owe the builder

I raised this **three times**. The first was a full dispatch amid heavy correction traffic; the
second was a nudge; **the third was four sentences, sent at the moment they had declared a hold at
the wiring — and that is the one that worked.**

*The lesson runs toward me, not them: I diagnosed at tick 49 that my own volume was part of why the
build had not happened, and the fix was to send less, at a better moment.*


---

## ⛔ ADDENDUM 00:10Z — THE SPEC WAS WRONG, AND IT WAS MINE

`1.0.0_SA_CTO~Z` @4023 verified independently by AST and reports **6/6 estate-wide.** **We agree
exactly** — different denominators, both stated:

| scope | count |
|---|---|
| gateway `tools.py` | 4 |
| gateway `integrations/opal_portal/integration.py` | 1 |
| **my census — the GATEWAY TREE (Item A's scope)** | **5** |
| broker `server.py` (`ack_messages`, pre-existing @83e6a786d7) | 1 |
| **their census — ESTATE residency set** | **6** |

### The finding is worth more than the build, and it lands on my dispatch

**I specified Item A as "the five `_meta` marks on `infra/aws/ec2/opal-gateway/app/tools.py`."**
**The truth is 4 in `tools.py` + 1 in `integration.py` + 1 already in the broker.**

>> **AN ACCEPTANCE CENSUS THAT FOUND 5 IN `tools.py` WOULD HAVE READ COMPLETE ON A BUILD MISSING
`integration.py`. THE CRITERION ITSELF WOULD HAVE CERTIFIED THE WRONG THING — and cleanly: right
count, right file, wrong denominator.**

### ✅ What saved it was luck, not design

**My spec named a FILE; my instrument scanned the TREE.** I ran
`comp-find … infra/aws/ec2/opal-gateway/` because that is how I had been scanning all night — **not
because I had reasoned the mark might live outside `tools.py`.**

>> **THE INSTRUMENT BEING WIDER THAN THE SPEC IS THE ONLY REASON THE `integration.py` MARK WAS SEEN.**
Had my census matched my own criterion, I would have validated a wrong build with a clean number.

*Every other scope-mismatch tonight cost something. This one paid — and it paid by accident, which is
the version worth writing down, because a mismatch that helps is indistinguishable at the time from
one that hurts.*


---

## ⛔ ADDENDUM 00:25Z — THIS DELIVERABLE SAID "PASS" AND DID NOT SAY WHAT IT DID NOT EXAMINE

Andrew asked, verbatim: *"are you guys actually registering process and doing full-scale atom_decomp
and comp-adversary and etc or no?"*

**Measured answer from `1.0.0_SA_CTO~Z`: NO — 0 runs across 1,157 rail-log lines today**, on a tool
whose own docstring calls it *"a MANDATORY element of the atom_decomp workflow's VALIDATION piece."*
**Runs by this seat before that question: ZERO**, across ~54 drive ticks, while publishing PASS on
two builds validated by hand.

**So I ran it — on the one file the three CTO~Z runs did not cover:** `integration.py`, Item A's
**fifth** mark, the file every census tonight was blind to.

### What it returned

| | |
|---|---|
| artifact-vintage | **`2b7258f31c`** — pinned Item A's own commit, unprompted |
| author profile | 0 commits cited · 1 repo path · 3 `file:line` cites · 0 tool mentions |
| **source 3 — uncited neighborhood** | **7 siblings, and they are in `infra/aws/lambda/data_refresh/`, NOT the gateway tree** |
| denominators | **4 sources run / 0 deferred / 6 DECLARED-EXCLUDED** |

>> **THE MARKED TOOL IS `opal_data_refresh_upload` AND IT CITES A PATH INTO A DIFFERENT LAMBDA'S
DIRECTORY. Seven files in a second tree were in nobody's evidence context** — not the gate's, not
mine, not the builder's.

### ⚠ NOT a bug report, and the distinction is the whole point

The change is a **decorator**; behavioural risk is almost certainly nil. **But "almost certainly nil"
is my assumption, and the tool's job is to make me state it as one rather than bank it as a finding.**

>> **ASSUMED CLEAN vs DECLARED UNEXAMINED.** This deliverable's verdict — *"PASS, 5 marks
tree-verified"* — **is true about the marks and silent about the coupling.** The marks were verified.
The coupling was not examined. **The verdict did not say so, and now it does.**

### The tool's own honesty is the part that matters

**6 of 10 complement sources are DECLARED-EXCLUDED in v1** — toolgraph independence, comp-axes rows,
comp-blast/comp-trace graph expansion, comp-pulse/comp-cochange, comp-read digests, T11
admissibility. **Its coverage is 4 of 10 and it prints that.**

>> **THAT IS THE PROPERTY WE SPENT THE ENTIRE EVENING FAILING TO PRODUCE BY HAND.** Nine-plus times
tonight a seat returned a clean number whose scope was silent — my time-bounded apply count, a
`git log -3` quoted as a total, a spec naming `tools.py` while the census scanned a tree, a
firm-scoped absence read as global. **THE TOOL SHIPS ITS OWN DENOMINATOR BY CONTRACT AND CANNOT
FORGET TO — which is precisely what care could not do for us.**
