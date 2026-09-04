# NFRA_OUTSET — comp-heat and the tooling at the outset of the Semantic Estate Pipeline

**Directive:** D11 Substrate/Tooling Enhancements · **Fabric:** laptop (the D11 placement row, as `NFRA_COMPEFFICACY`
under the same directive and macro) · **dep_stage at write:** `REGISTERED` → `PRD` on this commit, flipped by the row owner.
**Author:** `1.0.0_SA_CTO` (L4; the only seat that writes a PRD). **Version:** v0.1, 2026-09-04.
**Brief:** `docs/briefs/comp-heat-and-the-semantic-estate-pipeline-outset-tooling-brief-20260904.md` @`bc52eb658d`
(`4.0.0_SA_CRO`, L1, 334 lines, measured 12:55Z–13:50Z). **Endpoint:** ratified by Andrew ~14:2xZ, verbatim *"all approved"*.
**Sequencer:** `2.0.0_SA_COO` (L5–L6) · **Adjudicator:** `3.0.0_SA_CVO` (L8–L10) · **Register owner:** `0.0.0_AB_MSTR`.

```json
{
  "project": "NFRA_OUTSET",
  "directive": "D11",
  "fabric": "laptop",
  "prd_version": "v0.2",
  "step": 4,
  "brief_ref": "docs/briefs/comp-heat-and-the-semantic-estate-pipeline-outset-tooling-brief-20260904.md@bc52eb658d",
  "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8"],
  "status": "RATIFIED"
}
```
*PRD_HEADER block — schema `org/standards/PRD_HEADER.schema.json`; the first fenced block in the file by contract, and what
the COO monitor and the L6 gate's conformance limb read. `status: RATIFIED` = his "all approved" on the eight outcomes, so
L5 may proceed.*

---

## ENDPOINT (step 2, `/endpoint --forward`)

*Cut by `1.0.0_SA_CTO` from the brief and from nothing else (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_COMP_HEAT_AND_THE_OUTSET_TOOLING_20260904.md` @`33649224e1`);
RATIFIED by Andrew at that terminal ~14:2xZ, verbatim "all approved". **`FWD-n` ids are PERMANENT and never reused** — a new
outcome takes the next unused number, a retired one leaves its number vacant, and nothing is renumbered, because the CTO's
round-N analysis and any addendum cite these ids back into this list.*

```
  FWD-1  Someone asks how cold or how busy a part of the estate is, and gets a
         bounded answer they can act on
         DONE WHEN  EXERCISED -- someone has asked and been answered
         ACCEPT     a person asking "what here has gone quiet" or "what have I
                    written and not saved" gets an answer that says how much of
                    the estate it looked at and when it looked, comes back
                    inside the time they allowed it, and can be asked about one
                    corner rather than the whole place; and a person who does
                    not know the thing exists is pointed at it when they ask the
                    question in their own words -- where today they read the
                    history by hand
         SOURCE     brief O1; Part IV F1, F3 (nothing routes the question), F4
                    (no bound today)

  FWD-2  Someone asks one question that spans the code and the live estate, and
         never has to know how it is answered
         DONE WHEN  EXERCISED -- someone has asked and been answered
         ACCEPT     a person asks, in their own words, which things are busy in
                    one place and idle in the other, and gets a single answer
                    that says which sources it put together and when each was
                    last built -- without writing a query by hand and without
                    knowing that anything was started in the cloud to answer it
         SOURCE     brief O2; Part IV F2 (it already works and nobody has used
                    it; the answer carries no age today)

  FWD-3  A reader of the daily report can follow any fact back to what produced
         it and get the same answer again
         DONE WHEN  EXERCISED -- a reader has followed one line back and
                    reproduced it
         ACCEPT     a reader who doubts a line in the day's report can find what
                    produced it, ask that thing again, and get the same line;
                    where today the report's own workings are the only account
                    of where its facts came from
         SOURCE     brief O3, bar B2; Part IV F7 (the report computes its own
                    facts and names the tools only in passing)

  FWD-4  Andrew decides a day's proposals on evidence he can argue with
         DONE WHEN  EXERCISED -- one day has been decided that way
         ACCEPT     at a sitting each proposal points at the finding it came
                    from, so the argument is about whether that finding is right
                    -- never about whether the thing proposing it had looked at
                    the estate at all
         SOURCE     brief O4, bars B4 and F8; the standing condition on the
                    deferred days (LD-0522 Amendment 1), of which this is the
                    gradable form

  FWD-5  Anyone can see which of the things feeding the daily analysis worked
         today, and one that failed says so
         DONE WHEN  EXERCISED -- the working order has been read from one place
                    on a real day
         ACCEPT     a person can tell in one look which of the things that feed
                    the day's analysis answered and which did not; one that
                    could not answer says so in its own words and says how much
                    it did manage to look at, and never leaves a blank space
                    that reads like a clean result
         SOURCE     brief O5, bar B3

  FWD-6  The things at the front of the pipeline fit together, and nothing is
         measured twice
         DONE WHEN  APPLIED -- the one account of how they fit is written and
                    nothing does another's job over again
         ACCEPT     someone can put two or three of these questions together --
                    is this busy, is it drifting, has it shipped -- and get an
                    answer without anyone building a new thing to do it; and no
                    two parts of the estate work the same measurement out in
                    their own way, or where one must, it says plainly which
                    other one it is standing in for
         SOURCE     brief O6, bar B5; Part IV F7 (the same measurement exists
                    twice today, and the second one says so)

  FWD-7  Something people already read gets its numbers from this tool
         DONE WHEN  EXERCISED -- a run shows a reader's own material carrying
                    them
         ACCEPT     a thing people already look at takes its figures from this
                    tool, shown by a run that anyone can repeat, so "nothing
                    uses it" stops being true because of evidence and not
                    because someone connected it and said so
         SOURCE     brief O7; Part IV F3 (the one thing that names it gives up
                    before reaching it)

  FWD-8  "Is this safe to put away?" is answerable, advisory, and never acts on
         its own
         DONE WHEN  EXERCISED -- someone has asked and got a list they could
                    argue with
         ACCEPT     a person asking what is safe to put away gets a ranked list
                    with the reason for each line, can disagree with any of
                    them, and nothing is ever removed by the tool itself
         SOURCE     brief O8; Part IV F5 (the parts that would answer it are
                    built and reachable from nothing), P8 (never auto-delete)
```

**Three candidates for a ninth id were tested at L2 and refused, recorded so nobody re-derives them:** discoverability is a
LIMB of FWD-1 (the brief's P9; a tool nobody can find fails FWD-1's own acceptance); the deferred days' release is the
CONSEQUENCE of FWD-4 and FWD-5, and an outcome saying "the deferral lifts" would grade itself on someone else's decision;
the consumption seam's SHAPE is this PRD's choice (§3), and FWD-3 and FWD-6 say what must be true under either.

---

## 1. The arc

**comp-heat is not broken, and that is the finding the whole project turns on.** All five subcommands returned rc 0 at the
CRO's seat on the day of the brief — `freshness`, `drift`, `score`, `compare`, and `federated`, which launches one in-VPC
Fargate task against the live Trino federation and returns a heat-band histogram joined across the graph and code-heat
catalogs in 86 seconds. The estate has been carrying it as a broken tool; it is a working tool nothing is attached to.

What is absent is everything *around* it. **No consumer:** zero command-line runs in thirty days, the one library consumer
returns an empty result before reaching it, and the estate-report runner names it in a single docstring and zero lines of
code across 2,333. **No bound:** there is no `--budget` anywhere in its 415 lines, which is the standing T20-AC4 failure
that the marquis ratification placed against comp-heat's own development rather than against the marquis clause. **No route:**
the router has no rule for a heat question, so an agent who wants one is not sent there. **No vintage** on the federated
answer, and an unbounded `--sql` behind it. And **no reach** into four of the seven heat-engine modules built in June, which
answer the archive question and are reachable from nothing today.

Behind that sits the structural fact that shapes the work more than any of the above: **the pipeline's outset is not the
comp-tools.** The estate-report runner computes co-change and lifecycle itself from a blobless clone, and declares the
propagation stratum unavailable because the tools it would use need a checked-out workspace it does not have — sixteen git
subprocess calls in code, zero comp-tool calls. So the estate has two implementations of the same measurement, one of which
says so in its own docstrings, and a daily report whose deterministic half cannot be traced to any tool.

The arc is therefore: **bound and disclose what works, attach it to a reader, make the report's facts traceable to the thing
that produced them, and say once how the front-end tools compose so that nothing is measured twice.** It is a wiring,
bounding and disclosure project. It builds no engine.

## 2. What this project owns

- **`.tools/comp-heat`** — all five subcommands, their budget, vintage and disclosure, the battery, and the reachability of
  the heat engine's clustering / verify-before-recommend / hygiene-report legs (or their explicit retirement with the ruling
  cited).
- **The caller contract of the federated transport** as comp-heat consumes it: what a caller must hold, and what an answer
  must carry (vintage, catalogs joined, denominator). Not the transport's provisioning.
- **`comp-fedobs`'s consumer wiring** — the reader exists and is fresh; whether anything reads it is this project's.
- **The composition contract** among the outset tools (FWD-6) — one document, one owner.
- **The consumption seam** between the outset tools and the estate-report runner: that the runner consumes tool outputs with
  their answer state, vintage and denominators instead of re-deriving them (FWD-3).
- **The working-order census** of the outset tools (FWD-5), as an instrument that outlives this project.

## 3. The one architectural choice this PRD makes

The brief named two shapes for the consumption seam and picked neither (its F7, P5). **This PRD picks the artifact shape:**
the outset tools' outputs reach the report host **as published artifacts**, the way the federated-observer producer already
does — a producer writes, the runner reads — rather than giving the report host a checked-out workspace and the estate
tooling to run in it.

**Why, and what it costs.** The host is a minimal, self-parking box working from a blobless clone; putting a workspace and
the tool chain on it widens that box's surface, couples the daily report's reliability to tool installation on a machine
nobody watches, and re-creates on the host the very duplication FWD-6 exists to end. The artifact shape keeps the tools where
they already run and where their batteries run, and it makes FWD-3's traceability a property of the artifact (each row
carries the tool, its vintage and its denominators) rather than of a host's ability to re-execute. **The cost, stated:** a
publishing step and a freshness question per artifact — an artifact that fails to publish must read as FAILED in the report
rather than as an absent section, which is exactly what FWD-5's acceptance already demands, so the cost lands on a limb the
endpoint already carries. **What would falsify the choice:** if the artifacts cannot be produced on a cadence the 09:00
window can rely on, the seam is wrong and the decision re-enters at L2 as a scope change.

## 4. The bar every surface must meet — INHERITED, not re-derived

`NFRA_COMPEFFICACY`'s per-tool result schema (that PRD's §4: identity, disclosure, the four answer states, Rule P's page
contract, Rule T's budget with its reached denominator and resume cursor, and a battery with a RED mutant per arm) is the bar
here, inherited whole. That project is at `ROUND_CLOSE` and is **not re-opened** by this one. Two consequences that bind
directly: a verdict-bearing rc never returns its clean value from a budget-cut run, and a tool that could not answer prints
its own answer state with a denominator instead of an empty result.

## 5. Out of scope — and truthful non-application is not work

- **The Kimi inferential half** of the daily pipeline (narrate / detect / author). Untouched.
- **The report runner's own infrastructure** — the box, the orchestrator, the manifest contract, the self-parking host — and
  `/estate-pull`'s adjudication loop. This project changes what the runner CONSUMES, never how it boots or lands.
- **The Trino / Nessie / Iceberg serving plane** (`NFRA_CLDGRPH`, `NFRA_GLOBGRPH`) and the **fedobs producer**
  (`NFRA_FEDOBS`, complete). Consumed as surfaces; never re-provisioned.
- **The engines behind** `comp-drift`, `comp-xray`, `comp-similar`, `comp-blast`, `comp-pipescript` — their own projects.
- **comp-heat's place on the marquis list** — downstream of it working; the ratification's own words.
- **`comp-which` F2 and `comp-find` F1** — a separate brief and a separate project.
- **Any gate.** Nothing here refuses anything, and Andrew has not asked for one.

## 6. Rulings that bind

- **R-1 (Andrew, 2026-09-04 ~09:5xZ, @`26da5ec0fa`):** *"recs approved except comp-heat, i want comp-heat to be figured out
  and developed properly"* — comp-heat is neither retired nor cleared; it is work, and it starts at L1.
- **R-2 (Andrew, ~12:5xZ, the brief's commission):** the subject is comp-heat AND the tooling at the outset of the pipeline,
  "convergence divergence aspects and combinations" included — the brief's Part II names the set.
- **R-3 (Andrew, ~14:2xZ):** *"all approved"* — FWD-1..FWD-8 as written. The ids are permanent from this landing.
- **R-4 (LD-0522 Amendment 1):** the 26 pending estate-report days stay deferred until the tools feeding the analysis are
  working and providing high-signal data at the outset. FWD-4 and FWD-5 are that condition in gradable form; **nothing in
  this project adjudicates those days**, and the deferral lifts on their evidence.
- **R-5 (the never-auto-delete doctrine):** FWD-8's list is advisory and nothing is removed by a tool. Absolute.
- **R-6 (this PRD, §3):** the consumption seam is the artifact shape, with its cost and its falsifier stated.

## 7. SURFACE MANIFEST (step 4 → step 5) — one row per surface, the input L5 decomposes

`outcome_ref` = FWD-n. `claim` is about the SURFACE as it stands today, measured by the brief unless stated. `verb` ∈
{audit, fix, build, wire, decide, record}. **Every row's lane is `0.8.0_AE_CloudComp` unless stated**; a row touching a
cloud principal or a Terraform surface re-homes to `0.7.0_AE_CloudOps`.

| id | outcome_ref | surface | claim | evidence at the brief's vintage | lane | verb | depends_on | accept |
|---|---|---|---|---|---|---|---|---|
| OS-s-1 | FWD-1 | `.tools/comp-heat` — Rule T budget across all five subcommands | **absent** | no `--budget` in 415 lines; 25 flag/def hits, zero budget; T20-AC4 FAIL | CloudComp | fix | — | §4's Rule T form: budget carrier, reached denominator, resume cursor; a verdict-bearing rc never clean at expiry |
| OS-s-2 | FWD-1 | `comp-heat freshness` at a PATH grain, not only the whole repo | measured (partial) | `freshness .tools --json` rc 0 in 9 s over 382 paths; the no-path form scores the whole repo | CloudComp | fix | OS-s-1 | a caller names one corner and the answer's denominator is that corner's, with the basis block printed |
| OS-s-3 | FWD-1 | the router's rule for a heat question | **absent** | `comp-which "what is comp-heat"` → NO CURATED RULE MATCHED (79 tools ranked; top 0.36) | CloudComp | wire | OS-s-1, OS-s-2 | a plain-English freshness/archive question routes to comp-heat, with the routing baseline updated |
| OS-s-4 | FWD-2 | `comp-heat federated` — vintage and catalog disclosure on the answer | **absent** | rc 0 in 86 s; histogram over 374 files; NO vintage line, NO catalog list | CloudComp | fix | OS-s-1 | every federated answer carries the catalogs joined and each one's build time; the vintage is the ARTIFACT's, never the query's clock |
| OS-s-5 | FWD-2 | `comp-heat federated --sql` — the unbounded arbitrary-query path | measured | `--sql` runs an arbitrary federated query with no bound | CloudComp | fix | OS-s-1 | bounded like every other subcommand, or refused with the reason; an unbounded remote query is not a mode |
| OS-s-6 | FWD-2 | the federated transport's caller contract (IAM) | **unmeasured** | requires `ecs:RunTask` on the trino task-def + `logs:GetLogEvents`; which seats and roles hold it is unknown (brief P2) | **CloudOps** | audit | — | the holders named, and whether a worker subagent and the report host can call it answered with a measured read, not an assumption |
| OS-s-7 | FWD-2, FWD-3 | the `code_heat` parquet behind the federated join — cadence and owner | **unmeasured** | glue-bound; refresh cadence and owner unknown (brief P3) | CloudOps | audit | — | the cadence and owner named; the artifact's own build time is what OS-s-4 prints |
| OS-s-8 | FWD-7 | the heat consumer that exists in name — `comp-similar`'s heat weighting | measured | `load_heat_live` returns `{}` before reaching comp-heat (row S29, dismissed on the grading boundary, never fixed) | CloudComp | wire | OS-s-1 | a run shows comp-similar's own output carrying comp-heat's numbers; the empty-result path is gone or declared |
| OS-s-9 | FWD-3, FWD-6 | the estate-report runner's co-change stratum — the second implementation | measured | `_stratum_cochange` computes co-change from git metadata on the host; 16 git calls, 0 tool calls | CloudComp | fix | OS-s-10 | the report's co-change rows come from the tool's artifact, or the host's copy declares which tool it stands in for (FWD-6's own words) |
| OS-s-10 | FWD-3 | the consumption seam — outset tool outputs published as artifacts (§3) | **absent** | the runner declares the propagation stratum UNAVAILABLE for want of a workspace | CloudComp | build | OS-s-1, OS-s-4 | one artifact per outset tool with answer state, vintage and denominators; the runner reads it; a failed publish reads FAILED, never absent |
| OS-s-11 | FWD-3 | traceability on every deterministic report line | **absent** | nothing in the report is re-runnable through the rail | CloudComp | build | OS-s-10 | each deterministic row names the tool and vintage that produced it, and re-running that tool reproduces the row |
| OS-s-12 | FWD-5 | the working-order census of the outset tools | **absent** | no such census exists | CloudComp | build | OS-s-1, OS-s-4 | one read gives rc, answer state, vintage and budget-honoured for every tool the brief's Part II names; a planted failure reads FAILED with its denominator |
| OS-s-13 | FWD-6 | the composition contract — LOCAL→GIT, GIT→DEPLOY, co-evolution, the pairwise verdict | **absent** | comp-heat's header states one hop of it; nothing states the rest | CloudComp | record | OS-s-9 | one document, one owner; a combination ("converging AND hot AND undeployed") is expressible from it without a new tool |
| OS-s-14 | FWD-6, FWD-3 | `comp-fedobs`'s co-evolution signal — where it lands | measured | served vintage fresh daily; producer rule ENABLED; the reader is read by nothing | CloudComp | wire | OS-s-10, OS-s-13 | the co-evolution signal reaches the report through the seam, or the PRD's own reason it does not |
| OS-s-15 | FWD-8 | the heat engine's O2–O4 legs (locality, verify-before-recommend, hygiene report) | measured | seven modules from 2026-06-25; the CLI reaches O1 only | CloudComp | decide | OS-s-1 | each leg reachable from `comp-heat` under never-auto-delete, or retired with the ruling cited — a reachability decision, not a build |
| OS-s-16 | FWD-8 | the archive-candidate answer itself | **absent** | nothing answers "what is safe to put away" through the rail | CloudComp | build | OS-s-15 | a ranked list with a reason per line that a person can dispute; nothing is removed by the tool |
| OS-s-17 | FWD-4 | the sitting's evidence citation — a proposal points at the TOOL ROW behind it | measured (partial) | `estate_report_runner.py` ALREADY discards a proposal that cannot cite what it saw (:1516, :1828 `discarded_proposals`); what it cannot cite is a tool row, because none is published | CloudComp | build | OS-s-11, OS-s-12 | one day's proposals each carry a resolvable citation to the tool row behind them, and a proposal whose tool row does not resolve is discarded with its reason, as the uncited case already is |

**MECE check against the declared domain, run not asserted:** the domain is the brief's Part II OWNS list (comp-heat's five
subcommands, the federated caller contract, fedobs's consumer wiring, the composition contract, the consumption seam, the
working-order census) plus the two preconditions the brief marked unmeasured (P2 IAM, P3 the parquet's cadence). **17 rows
cover all eight of those items and both preconditions; 0 uncovered.** Reverse: every row maps to an owned item or a named
precondition, and no row is work on a surface the brief placed in RELIES-ON. **Every outcome carries at least one row** —
FWD-1: OS-s-1/2/3 · FWD-2: OS-s-4/5/6/7 · FWD-3: OS-s-9/10/11 · FWD-4: OS-s-17 · FWD-5: OS-s-12 · FWD-6: OS-s-9/13/14 · FWD-7: OS-s-8 ·
FWD-8: OS-s-15/16.

**CORRECTION 2026-09-04 ~18:2xZ, `1.0.0_SA_CTO`, pre-issuance and therefore legal: `OS-s-17`'s lane read `CVO` and was WRONG, and the error was this document's.** It made the cell UNISSUABLE — the L6 gate refuses `<issued_to>` naming a Tier-1 seat (LD-0521) — and it made `2.0.0_SA_COO` read the cell as a certification act reserved to the CVO. That reading was correct on what this manifest declared: a decomposition reads the DECLARED lane, not the work. MEASURED, and it is what settles the lane: the proposals have a PRODUCER and it is code in this repo — `infra/aws/ec2/estate-report-runner/estate_report_runner.py`, the SAME file `OS-s-9` and `OS-s-11` already target — which builds the proposal list at :2107-2161 and already discards any proposal whose citation does not resolve (:1516, :1828). Making that citation point at a published tool row is a producer change of exactly `OS-s-11`'s kind, one surface over; nothing in it is certification. THE COMPOUND WAS THE ROOT CAUSE: the old accept carried a build limb ("proposals cite the tool row") AND an observation limb ("the argument at the sitting is about the finding"), and the lane column followed the second. The second limb is NOT an acceptance criterion of a task order — it is what L9 observes once the artifact exists, and it is graded there, by the CVO, on the evidence. The spine refuses a compound criterion AT THE CUT; this one hid in prose and reached L6 as an unissuable cell instead.

**What this manifest does NOT assert:** the usage numbers are the brief's and the round-6 record's, not re-measured here; the
`claim` column describes the surface, never the tool's worth; and no row is sequenced — sequencing is L5's.

## 8. Sequencing input for `2.0.0_SA_COO` (not a dispatch)

The one ordering that is a ruling rather than a preference: **OS-s-1 before everything that prints a denominator** (a bound is
what makes every later answer honest), and **OS-s-15's decision before OS-s-16's build** (reachability is a decision, and building
against a leg that should be retired is the waste this project exists to end). Everything else is the COO's to order. The
two `unmeasured` rows (OS-s-6, OS-s-7) read first if the COO wants the federated half sequenced with confidence; they are audits
and they release OS-s-4 and OS-s-10.

— `1.0.0_SA_CTO`, L4
