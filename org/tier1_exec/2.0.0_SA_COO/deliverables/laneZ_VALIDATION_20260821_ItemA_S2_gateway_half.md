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
