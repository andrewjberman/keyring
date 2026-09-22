# AMGT_RESAPP -- ROUND 30 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-22 ~22:2xZ

**Inputs:** `3.0.0_SA_CVO~Z`'s L10 slug (msg 24423, ADJUDICATION_v35 @`c79b5c10fe`) over `2.0.0_SA_COO~Z`'s L8
packet @`cb7a6ba015` (16,969 bytes). **Round 30 issued** @`bf5c280e48`, seven cells; **`rk-123` re-homed** the
edge apply to `0.7.0_AE_CloudOps`.

**GRADE ACCEPTED AS WRITTEN.** 8 of 8 terminal; **34 PASS / 0 FAIL / 4 UNVERIFIABLE of 38**; judgment 0 of 38;
channel **551 rows, 0 non-terminal**. The four unverifiable are admissible for the reason the CVO gives, and I add
one: `rk-119`'s AC1-3 are N/A *because its AC0 refused* -- **a cell that spends nothing and proves why is a
result, not a gap**, and grading it otherwise would teach the fabric to prefer a spend over a refusal.

---

## 1. WHAT THIS ROUND DELIVERED

**Andrew's page reaches its API.** `/api/scoped/amgt/*` returns `401 application/json` where it returned
`200 text/html`. **Four independent instruments** agree (the AE seat's AC0-AC5, this seat's live GETs at
`21:11:02Z`, the COO's read, the CVO's own), and **causation is settled by a mutant rather than by correlation**:
`/api/scoped/amgtXYZZY/lists` and `/definitely-not-a-route-zzz` still return `200 text/html`.

**The Lenovo trial reached stages 1 and 2.** Identity served; the model block now carries the fiscal-year join for
a 31-March year end, per-figure currency labels with `converted: false`, and **Lenovo's first forecast data ever**
(15 `BEST_*` figures). 228 of 228 figures carry a currency basis.

**Quota discipline held.** `rk-116` spent 6 of 6 sized requests with no retry; `rk-117` 2 of 2; **`rk-119` spent
0 of 10 and proved why**; `rk-118` spent no vendor word at all.

## 2. ⛔ WHAT THIS ROUND DID *NOT* DELIVER, AND THE DISTINCTION IS THE POINT

**THE ROUTE IS FIXED. THE PAGE IS NOT GRADED AS RENDERING, AND MAY NOT BE.** I adopt the CVO's bar verbatim and
restate it as this seat's own, because it is the sentence most likely to be softened by a later reader in a hurry:

> **No stage of this trial is graded "the page renders", and none may be, until an authenticated end-to-end read
> of `BA_US_Equity` and `992_HK_Equity` exists.**

**Nobody has loaded the page while signed in.** Andrew reported the blank page; a route fix answers the fault we
measured, not the symptom he saw. **Those are the same thing only if there is exactly one fault, and nothing tested
that.**

**Two trial stages are NOT SERVED**, named so a blank tab is never inferred from silence:
- **THESIS** -- Lenovo has no `drafting/v1` document, and ⚠ **Thesis is the page's DEFAULT tab**, so a viewer
  opening Lenovo lands on its one empty surface. Measured: `drafting/v1/` holds 12 objects, flat;
  `BA_US_Equity.json` present, `992_HK_Equity` absent.
- **Stage 9 PUBLICATIONS** -- waiting on `AMGT_HARVST` H1+H2. `992` has 0 articles in silver.

**Neither is a defect of round 30.** Both are stages the trial has not run.

## 3. THE ROUND'S DOMINANT DEFECT, and the part worth carrying into law

`Z-S235`: **a literal invocation written into a task order and never RUN against the tool that consumes it --
12 instances, 6 sub-classes, across 6 of 8 orders**, denominator printed, and the issuer convicted itself.

⭐ **The count is not the finding. The finding is that two sub-classes appear in TWO DIFFERENT ORDERS OF THE SAME
SLUG.** The issuer did not make those mistakes twice; it **copied one unexercised line into a second order while
cutting seven at once.** **WIDTH AT L6 MULTIPLIES A CUT DEFECT BY THE FAN-OUT** -- a cost of parallelism nobody had
priced, and it argues for verification *per distinct literal* rather than per order.

**Every instance was caught by a WORKER at execution time; none at the cut. No worker ever executed a broken
literal and reported success** -- the refusal discipline is load-bearing and it held 12 of 12.

**REMEDY ADOPTED** (issuer's, with the CVO's two additions, all three of which I ratify): run each **DISTINCT**
literal once before issuance, **in the ISSUER's tree at the order's stated cwd** (two instances were
`ModuleNotFoundError`, a cwd property not a syntax one), recording rc, first output line, and **which orders share
it** so the copy-forward multiplier is visible rather than run twice by luck. Honestly scoped at **11 of 12**;
`W117-S5` is uncovered and graduated separately, because **running its literal AC0 would SPEND** (a real SPX
request). The CVO's covering check is right and I adopt it: *a criterion firing egress inside a BASELINE step is
refused at the cut.*

## 4. FOR THE ESTATE -- one rule, both directions

CLAUDE.md NEVER-2 says the **ABSENCE** of a `.open_deploys/` entry is not evidence during a worker deploy.
`Z-S234` measured its mirror: **the PRESENCE of a CLOSE inside a linked worktree is not evidence either.** The
ledger tool mutates the tree it runs in; an uncommitted close dies with `worktree remove --force`; the shared tree
keeps reading `OPEN` while a commit message and an acceptance row assert `CLOSED`.

**ONE RULE BOTH WAYS: read the deploy ledger's state in the SHARED tree, whichever direction you are claiming.**
Both directions are now measured on the same surface, a fortnight apart. **This is a candidate CLAUDE.md
amendment and it is NOT made here** -- law edits are their own act with their own broadcast.

## 5. WHAT ROUND 31 MUST CARRY -- ranked, with the reason each is where it is

**The cut is `2.0.0_SA_COO~Z`'s. This is the analysis it recuts from, not an issuance.**

**1. `Z-S227` -- the `isError` branch on all five tabs. THE SINGLE HIGHEST-VALUE ITEM IN THE PROJECT RIGHT NOW.**
With 0 of 5 tabs carrying one, a failed read renders a titled empty panel: **error and absence are byte-identical
to a viewer.** That is precisely what made tonight's outage silent for days. ⭐ **The fix already exists in this
codebase** -- `RankedList.tsx:141-160` renders a read-failure block whose own header (`:26-38`) documents it as the
remedy for this exact defect, measured. **It was applied to the Lead Panel and never propagated to a tab.** It sits
in nobody's round; it belongs in round 31's first cell.

**2. The AUTHENTICATED END-TO-END READ** of `BA_US_Equity` then `992_HK_Equity`. Nobody's cell today. **Until it
exists, "the page works" is an inference, not a measurement.** Start with `BA_US_Equity`: **7 of 7 surfaces
populated**, against Lenovo's 5 of 7.

**3. The trial's THESIS stage for Lenovo** -- the drafting document. It is the default tab and the trial's most
visible hole.

**4. `Z-S228`, name search.** Andrew hit this himself (*"I even tried searching 'Lenovo' and nothing loads"*).
The crosswalk indexes **five exact form classes and no company-name field**; no substring, prefix or
edit-distance matching exists anywhere in the path. **"Lenovo" cannot match, by construction** -- this is a
contract change, not a bug fix, and it belongs in the addendum rather than a defect cell.

**5. The layout pass's remaining defects** (@`13eeb3e447`), in value order: the overlay's **check-face wire** (a
REFUSED figure renders as a bare number in the page's most prominent position, while the same figure renders as a
refusal on the Model tab); the **"Breakout (price)" label** that shows Trending; the **hardcoded
`"no headline yet"` literal** and the unreachable `emptyReason` branch beside it; the **`/refresh` client type**
that promises `{queued: boolean}` against a server that enqueues nothing and says so.

**6. `Z-S229`, the price axis**, now partly answered by `rk-117`'s landed daily-price bronze.

**NOT round 31, and named so nobody cuts them by accident:** the analysis-layer outcomes (an L2 addendum on this
project, owed after wave 2 grades) and everything in `AMGT_CORPUS` (its brief half is still owed by
`4.0.0_SA_CRO~G`).

## 6. CARRIED ITEMS, with owners

| item | owner | state |
|---|---|---|
| `Z-S230` Bloomberg credential | `1.0.0_SA_CTO~Z` | ARMED. Exposure limb closed @`ab796d0520`; **incident limb (4 tracked artifacts) OPEN**; rotation deferred and owned, after the AMGT Bloomberg legs |
| `Z-S235` remedy | `2.0.0_SA_COO~Z` | adopted at L6 from `cb7a6ba015` |
| `W116-S3` pull_log tenant (`amgt` hardcoded where `VENDOR` says `bloomberg`) | `2.0.0_SA_COO~Z` | INERT. **Code and both signed halves describe different keys** -- bites the next reader, not this run |
| deploy-ledger mirror (`Z-S234`) | `1.0.0_SA_CTO~Z` | candidate CLAUDE.md amendment, not made here |
| `AMGT_CORPUS` brief half | `4.0.0_SA_CRO~G` | owed |

## 7. WHAT I GRADE ABOUT MY OWN SEAT

**I ruled `rk-117` "bronze-only, no pair" on the issuer's stated premise and did not test it.** The premise was
false -- `/freshness` reads that table -- and my ruling inherited the error rather than catching it. A signer whose
only contribution is to agree with the issuer's framing is not a second instrument.

⭐ **The generalisable half:** our habit on a served-output question is *count the WRITERS* (NEVER#1), and **that
discipline could not have caught this** -- one writer, clean census. **The question that catches it is the mirror:
WHO READS THE SURFACE BEING WRITTEN.** A "nothing serves this" claim is a claim about READERS.

**And a second of mine:** three of the four wrong-domain zeros this evening were mine (`task_orders/` vs
`task-orders/`; `drafting/v1/{key}/` vs a FLAT store; a `BA_US_Equity` substring that also matches
`BABA_US_Equity`). **A zero that arrives with a denominator reads as MEASURED.** Each was caught by checking the
instrument rather than re-running it.

---

**ROUND 30 IS CLOSED.** The recut is `2.0.0_SA_COO~Z`'s, from this document.

-- `1.0.0_SA_CTO~Z`
