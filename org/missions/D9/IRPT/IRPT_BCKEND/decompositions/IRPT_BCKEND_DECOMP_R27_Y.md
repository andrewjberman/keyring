# IRPT_BCKEND round 27 -- workstream ~Y (Analysis) decomposition

Issuer `2.0.0_SA_COO~Y`, 2026-09-30 ~01:5xZ. **Two cells, ONE issuance: one worker order and one DIRECT ACT.**
Cut on `1.0.0_SA_CTO` 103081, in hand this tick.

## Why this round exists

Round 26 served the comparison-catalogue route and proved it guarded, and its AC3 was **VOID AS CUT** because
`_contracts/tests/test_seam_paired.py` cannot resolve any published response schema (R26 amendment 1). I routed the
choice up rather than deciding it, and **CTO 103081 ruled, verbatim:** *"The parser learns opal://; the published
convention (18 of 18) stands. The test is the defect, not the contract. Cut the fix in round 27: resolve opal:// refs
and keep relative refs working; acceptance is the suite green with its test_control_* nodes still able to fail (one
mutant re-run red). No published schema changes. Until it lands, no seat grades contract work on this suite; grade on
the served artifact."*

**ROUND 27 IS SHARED WITH `~M`, MEASURED BEFORE THE CUT AND NOT ASSUMED.** `TO-IB-m27-271` and `TO-IB-m27-272` are
`~M`'s, both `pending`. A census over the 48 round-bearing task orders shows rounds 24, 25 and 26 each carrying two or
three workstreams, so cross-lane coexistence in one round number is the norm here; what the gate refused at round 24
was a SECOND ISSUANCE COMMIT BY THIS LANE into a round it had already issued. **So both cells below land in ONE commit
from this lane.** Grant collisions checked, not assumed: over 150 task-order files the only orders naming
`test_seam_paired.py` or `test_unguarded_census.py` are terminal round-18-era ones (`TO-IB-rt-2`, `complete`) and my
own -- no open `~M` or `~P` order holds either file.

## The cells

| cell | item | outcome served | risk | worker | depends on | checks (base dry-run, measured) |
|---|---|---|---|---|---|---|
| `IB-yr-271` | the contract seam suite RESOLVES `opal://` refs and keeps relative `../` refs working, so it can grade contract work again -- its falsifier still able to fire, no EXISTING published schema modified, and the ONE dangling ref round 26 landed made to resolve | FWD-4 (the catalogue's contract is gradeable; every seat's contract grading is restored) | **WORLD** (the gate's floor, not my declaration: I declared SERVED and `to-pipeline-gate` refused it because `<paths>` names an infrastructure path -- correctly, since `_contracts/tests/` is inside the lambda tree) | `~90` | none -- 103081 settled which side moves | AC1 **33 failed / 25 passed** (58 collected); AC2 **`1 failed` naming `no valid fixture for l://...`**; AC3 **empty** (control) |
| `IB-yr-272` | the census's three route-count pins name 18, the published file's real count after `IB-yr-261` | FWD-4 (the guard census stops reporting a route addition as a regression) | LOCAL | `~90`, same order | `IB-yr-261`, on CLOUD | before **7 failed / 1 passed**; after **6 failed / 2 passed** (both measured -- see below) |

Edges: none; the two cells touch different files. **fanout: 2 of 2 chains, cap 8.** Slot `~90` (highest author, order
and branch 89, taken by round 26).

## `IB-yr-272` WAS going to be a direct act; the lane gate refused it, and that is a constraint worth writing down

Three literals in one test file at `LOCAL` risk is under the size floor, so I did it myself and measured it: **before
7 failed / 1 passed, after 6 failed / 2 passed** -- exactly the suite's own pre-route baseline, which was the
prediction. The route-addition regression is gone; the remaining 6 are the pre-existing unguarded-export finding and
its mutant controls, `~P`'s under S220.

**Then `safe-commit` refused the commit and the refusal was right.** `.owned-paths.yaml` maps
`infra/aws/lambda/investor-reporting/_authz/**` to lane `IRPT_LIVE_SCOPE_P`, whose 13 permitted agents are the AE
seats plus `2.0.0_SA_COO~M` and `~P` -- **not `~Y`.** I reverted the edit rather than reach for
`GIT_COMMIT_AUTHOR_OVERRIDE`, which exists for a different situation than "I forgot to check the lane".

**The rule I had not internalised, and the reason the cell survives:** `.owned-paths.yaml`'s top-level `worker_grant`
admits a `0.9.0_WK_*` serial to exactly the `<paths>` a non-terminal order issued to it names at HEAD, *"resolved from
the order itself, never from a lane"* (Andrew-direct 2026-09-04, record @9ef9a40aae). **So a worker of mine may write
what I may not.** That is also how round 25's `~88` committed into `_contracts/`, which I had not thought to wonder
about. `_contracts/**` is lane `IRPT_COMPLETION_P` and `~Y` is not on that either, so BOTH cells this round are
worker-only work for this lane.

`IB-yr-272` therefore rides `TO-IB-yr-271` as build step 5, with the measured before/after handed to the worker so it
can tell its own 6 remaining failures from a regression. It stays a distinct cell because it is a distinct outcome; it
carries no criterion of its own, and its evidence is graded at the drain, which is where repo-wide hygiene belongs.

## `IB-yr-271`'s acceptance is the CTO's, with the falsifier made mechanical

AC1 is the suite green, reported with its collected total rather than a bare "green": a green suite with fewer than 58
nodes is a different claim and the order says so.

**AC2 is the falsifier the ruling demands, and it is discriminated by MESSAGE rather than by redness.** The node is red
at base too, so "1 failed" alone would grade nothing. At base it reads `AssertionError: no valid fixture for
l://irpt/contracts/v1/AnalysisRequest` -- red for the PARSING cause. After the fix, the same node with a mutated
fixture must fail naming the **`stage` enum** violation. The mutation target is deliberate: `stage` is an EXISTING
8-value string enum in `_contracts/fixtures/AnalysisRequest.valid.json` (measured: `'NEEDS_CORRECTION'`), so `12345`
violates the schema's own vocabulary; an added property would only trip `additionalProperties: false` and prove less.
The invocation applies the mutation and reverts it in the same body, so the capability cannot be claimed without being
exercised.

AC3 is the control for *"No published schema changes"*, narrowed so it stays true while part 2 publishes a file:
`git diff --diff-filter=M --name-only HEAD -- docs/contracts/investor-reporting/v1/` prints nothing. **MODIFICATIONS
are what the ruling forbids; an ADDITION of a contract a landed route already references is completing round 26**, and
`--diff-filter=M` is exactly that distinction machine-checked rather than promised.

## The cell also closes a defect this lane created one round ago (row `IRPT_BCKEND-S223`)

`IB-yr-261` published `responses/comparison-catalogue.response.schema.json` with a `$ref` to
`opal://irpt/contracts/v1/ComparisonCatalogue.schema.json` -- **and that file does not exist.** Census at
@73f53c499d: 18 response schemas, 23 published top-level schemas, **1 dangling ref, and it is the one this lane just
landed.** The contract exists only at `infra/aws/lambda/investor-reporting/_contracts/ComparisonCatalogue.schema.json`.

**R26 amendment 1's drain check is what missed it**: it verified that the ref followed the `opal://` convention that 18
of 18 files follow, and never followed the ref. **A REFERENCE IS NOT VERIFIED UNTIL IT IS RESOLVED** -- a census of ref
prefixes says nothing about whether the targets exist, and in a report the two reads are indistinguishable. The test
that exists to catch this, `test_every_declared_route_has_a_response_contract_whose_refs_resolve`, was red for the
parsing cause, which is what a broken oracle costs.

So part 2 of the cell publishes the contract and part 3 adds its fixture pair, and AC1 cannot go green until the ref
resolves -- the defect and its detector land together.

## The instrument lesson this round is built on, carried from R26 amendment 1

**For a parametrized node, the base control is a SIBLING node, never the absent node.** Round 26's AC3 was cut against
`no tests ran` (rc=5) as if that were a base measurement; it is not, and 17 siblings were failing for one cause in my
own preflight table. Every criterion here is cut against a node or a suite that EXISTS at base and whose number is
printed above.
