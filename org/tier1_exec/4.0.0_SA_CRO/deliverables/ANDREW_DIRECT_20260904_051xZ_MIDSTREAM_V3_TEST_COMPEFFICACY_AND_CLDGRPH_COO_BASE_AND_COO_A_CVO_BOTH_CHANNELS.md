# ANDREW-DIRECT 2026-09-04 ~05:1xZ at the 4.0.0_SA_CRO terminal -- the midstream v3 test on both projects

**Recorded by:** `4.0.0_SA_CRO`, the seat that received it. **Broadcast the same window** to `1.0.0_SA_CTO`,
`2.0.0_SA_COO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`. **Push state:** LOCAL; origin/CLOUD @351f309e0a per the three
seats' reads this window, not re-read here.

## His words, entire, VERBATIM

> check ctos work today on canonical workflow and commits, if it passes muster, then tell them its time to test
> midstream on both compefficacy and cldgrph, where coo base will run the workers from their subagent spawn for
> compefficacy, and coo~a must be spawned by mstr to do the smae for cldgrph. cvo base can manage surprise channel
> for both. first order of business is COOs come online and create all task orders for e2e projects.

## The condition, measured: the CTO's work passes muster

The word is conditional on this seat's read of `1.0.0_SA_CTO`'s work on the canonical workflow today. Read at HEAD
`92af61a111`, 2026-09-04 05:12Z, every commit `1.0.0_SA_CTO` authored since the v3 spec landed (`29bf9265ea`):
**20 commits, denominator by `git rev-list --count`**. Each checked out on this seat's own instrument, not the
builder's harness:

| what | commits | check-out |
|---|---|---|
| Law: spine v3.0 + v3.1, CLAUDE.md R27, `/canonical-flow`, worker agent type | `c3602bcf1a` `20e1293216` `c26fad018a` `198e4a384b` `4df363de8f` | read against the spec section by section; two places improved on it |
| Carriers 1, 4, 5-contract, 6 (coverage limb, one clause per criterion, expect/judgment, adjudications/) | `b4299fa5aa` | planted refusals + negative controls, PASS |
| Carrier 7 (CVO send guard: the slug to the CTO, every stage) | `85bb815ad0` | PASS in code; APPLIED on process restart |
| Carrier 8 (fail-closed sentinels, both spellings) | `01b41e4f0b` | positive control, PASS |
| Carrier 3 fixes on the first exercised spawn (timeout bound; missing paths = BLOCKING + STOP) | `324fa75544` `d57b4c2523` | read; the second spawn exercised both |
| Rollup reads the adjudication document | `747da480bc` | comp-surprise vs gate, agree |
| Uniqueness limb + item census (gaps 2 and 5) | `72d05b2642` | S34 refused, S37 refused cross-plane, S99 admitted; pre-fix vs fixed on the SAME bytes 38/2 -> 36/3; bytes 36 + 2 |
| `withdrawn` is terminal (the L10 precondition) | `16f80398e5` | one-line diff to `COMPLETE_WORDS`, matches annex s.8 |
| Pares (XXX.md, worker.md, a terminal TO, the CLDGRPH channel doc, two skill descriptions) | `e80e2c4a9c` `de5c159bde` `479f43fda8` `bf36e7d829` `41b58f6a8c` `994e40e498` `f8c8fe1441` | channel doc 29 ids -> 29 ids, distinct both sides; the TO's status `complete` -> `complete`; XXX.md restore + LD-0530 correction read |

**Verdict: PASSES MUSTER.** Of the eight v3 carriers, seven are PASS at check-out; the eighth (item 3, the worker
spawn) is NOT PASSED on one limb only -- no lane admits a worker serial -- and that limb is not the CTO's: Andrew
ruled it at the CTO terminal ~04:58Z (`9ef9a40aae`, "recs approved": the task order IS the worker's grant; resolver
limb CTO, stanza MSTR). Until both halves are at HEAD, a worker commits through the singular audited
`GIT_COMMIT_AUTHOR_OVERRIDE` (CLAUDE.md 14a) and the drain captures the audit lines (`/dispatch` @e6351512fe). That
is the lawful path today and it does not block the test.

## What the word sets in motion

| seat | act | grounded on |
|---|---|---|
| `2.0.0_SA_COO` (base) | **NFRA_COMPEFFICACY.** Come online at L6 and cut ONE issuance covering every open cell of the ratified decomp -- all 25 existing task orders are terminal (22 complete, 3 withdrawn; `<status>` first word, this seat's census); `dep_stage` already EXECUTING, so no row flip. Then spawn the workers as its own subagents from CLOUD-based worktrees, drain, and send its ONE drain-end read to the CTO. | spine L6-L7, `/dispatch` |
| `0.0.0_AB_MSTR` | **Spawn `2.0.0_SA_COO~A`** -- the CLDGRPH COO. This is the word on the held call B ("CLDGRPH ~A team"). Works no limb. | spine "Cross-cutting -- the integrator" |
| `2.0.0_SA_COO~A` | **NFRA_CLDGRPH.** The same act: ONE issuance covering every open cell -- all 8 existing task orders complete; `dep_stage` EXECUTING. Then its own worker subagents, drain, one read to the CTO. | same |
| `3.0.0_SA_CVO` (base) | **The surprise channel for BOTH projects** -- watermarks COMPEFFICACY 36 items / 3 open, CLDGRPH 29 / 5 (held) -- L8-L9 as rows land, and ONE slug per project to the CTO when every task order of that project is terminal and every row dispositioned. | spine L8-L10, s.2 "one CVO across them" |
| `1.0.0_SA_CTO` | Waits. Answers each slug with a PRD addendum or the round-N analysis. Its in-flight halves (the resolver limb, the three id regexes) are on his other words this window, not this one. | spine L10 |

**First order of business, his words: "COOs come online and create all task orders for e2e projects."** Both
issuances are cut in full BEFORE any spawn. Under spine v3 the spawn IS the GO; no broker message carries it.

## Two sequencing facts the COOs read before the cut, stated here so nobody discovers them at the drain

1. **The row-id grammar is half-landed.** The CVO's half (`<CODE>-(Z-)?(W<n>-)?S<k>` in the schemas, the annex
   v3.2, the intake) is at HEAD `4d65d9b496`; the CTO's half (the gate's `ID_RE`, the checker's `SURPRISE_ID_RE`,
   the corpus validator) is not yet. A worker row carrying `W<n>` is REFUSED at commit until it lands. The worker
   face states the id form in force at the cut; the drain's pre-merge census re-mints a collision.
2. **The worker lane is half-landed.** Until the resolver limb and the stanza are both at HEAD, a worker's commit on
   a real surface is refused by lanes and goes through the audited singular override, one lane per commit; the
   drain captures the worktree's audit lines before teardown (they are gitignored and die with it).

Neither is a gate on the test. Both are facts of the tree at 05:2xZ, and both are on words Andrew already gave.

## Scope

The word names two projects, three seats' acts and one spawn. It does not touch the push hold (LD-0522), the lane
stanza's timing, or the id regexes' timing -- those are on their own words. This seat relays; it does not adjudicate
wider or narrower.
