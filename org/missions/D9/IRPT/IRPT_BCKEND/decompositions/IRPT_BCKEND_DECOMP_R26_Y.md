# IRPT_BCKEND round 26 -- workstream ~Y (Analysis) decomposition

Issuer `2.0.0_SA_COO~Y`, 2026-09-30 ~01:0xZ. **One cell, carried from round 25 by that round's amendment 1.**

## Why this round exists

`IB-yr-242` delivered the catalogue module and its closed v1 contract and left its route UNREGISTERED, because
registering it breaks the DEPLOYED boundary. Worker `~88` refused rather than weakening the test and it was right:
`reports/generate_installed.py:337` does `routes = dict(generate_entry.ROUTES)` while `:341` passes
`operations={generate_entry.OPERATION: compute, UPLOAD_OPERATION: upload}`, and `_authz/served.py:643-648` raises
`EntryError` at construction for any route naming an operation the Entry does not serve. **So a key added to
`ROUTES` without that file's grant fails every request to `irpt-ycharts-generate`, the analysis POST included.**

**The grant, not the cell, was the defect** (R25 amendment 1). This round is the same outcome with a grant that can
contain its own change. Nothing about the ruled shape (CTO 103038) or the ruled source (CTO 103035) is reopened.

## THE ISSUER'S OWN PREFLIGHT, MEASURED THIS TIME

The last cut named "register the GET" without tracing the boundary. This one applied the held change in a throwaway
worktree (`preflight-yr-261` off HEAD) and **measured the failure set**, so the grant is provably sufficient rather
than asserted. Four suites, before and after, run from `infra/aws/lambda/investor-reporting`:

| suite | base red | with the route, unwired | delta |
|---|---|---|---|
| `reports/tests/test_generate_installed.py` | **0** (13 passed) | **4** (all `served.EntryError`) | **+4** |
| `_authz/tests/test_unguarded_census.py` | 6 | 7 | +1 |
| `_contracts/tests/test_seam_paired.py` | 33 | 34 | +1 |
| `_contracts/test_owned_request_contracts.py` | 0 | 0 | 0 |
| **total** | **39 failed / 43 passed** | **45 failed / 38 passed** | **+6** |

**The two held patches in `~88`'s deliverables DO NOT APPLY at HEAD** (`git apply --3way` fails on both:
`entry.py` because the operation and the guarded compute already landed, `routes.json` because it has moved). They are
REFERENCE for intent, not an apply step, and the cell says so.

**`routes.json` is 17 rows with `_denominator.declared` 17 and `_denominator.total` 17**; the row convention is
`response_schema: "responses/<slug>.response.schema.json"`, which is why the response schema is in the grant and why
`~88`'s draft row -- which used a `response_contract` key pointing into `_contracts/` -- is not the shape to copy.

## The cell

| cell | item | outcome served | risk | worker | depends on | checks (base dry-run at CLOUD HEAD, measured) |
|---|---|---|---|---|---|---|
| `IB-yr-261` | the comparison-catalogue GET is REGISTERED and SERVED: the route in `entry.ROUTES` and in published `routes.json` with its denominators moved, the operation wired through the DEPLOYED boundary so `build_boundary` constructs, its `responses/` response schema with a conforming fixture, and the boundary's own route pin updated to the true table | FWD-4 (W2-04/05: the page can resolve and NAME a comparison before Add) | WORLD (a new served route) | `~89` | `IB-yr-242`'s module and contract, both on CLOUD | AC1 **1 failed**; AC2 **13 passed** (control); AC3 **no tests ran** |

Edges: none. **fanout: 1 of 1 chains, cap 8.** Slot `~89` (highest author/order/branch 88, taken by round 25).

**AC3's base is not a red -- it is a node that DOES NOT EXIST.** `test_seam_paired.py` parametrizes over the operations
in `routes.json`, so `[comparison-catalogue]` is minted by the cell's own row; at base the invocation prints
`no tests ran` (rc=5). That is a third answer state beside pass and fail, and the order names it so the worker does not
read rc=5 as a failure it has to explain.

**AC2 is the CONTROL and it is the defect's own witness.** `test_generate_installed.py` reads 13 passed at base and
4 failed with the route registered but unwired. So a cell that registers the route and does not reach the deployed
boundary fails its own control, and a cell that quietly relaxes the boundary's exact-equality route pin
(`reports/tests/test_generate_installed.py:117-119`) instead of updating it to the true table is refusing the work.
Updating that assertion to the real three-route table is REQUIRED and is not weakening it; deleting it, or loosening
`==` to a subset check, is.

## What this cell must NOT do, from row IRPT_BCKEND-S220 (filed in this preflight)

**Neither `_authz/tests/test_unguarded_census.py` nor `_contracts/tests/test_seam_paired.py` is a usable pass/fail
oracle at HEAD** -- 6 of 8 and 33 of 58 red respectively, in the MAIN worktree, cwd-independent, with each suite's own
`test_control_*` / mutant nodes among the failures. The census also reports `BLOCKED: 3 of 17 route(s) reach an
unguarded handler`, all three the export routes on `irpt-export-render` -- `2.0.0_SA_COO~P`'s lane, ARMED there, and
explicitly NOT this cell's to fix or to route around. **Consequence for the cut:** no criterion here names a whole red
suite. AC3 names ONE node id; the census is measured by the issuer at the drain as a DELTA against the printed
baseline of 6, never as a green.


## Amendment 1 (2026-09-30 ~01:4xZ) -- the cell's OUTCOME IS SERVED; AC3 was VOID AS CUT, and that is a second issuer defect of a DIFFERENT kind

Worker `~89` delivered AC1 and AC2 and refused AC3 without weakening it. Issuer grade in its own worktree:
**2 passed, 1 failed.** Write surface entirely inside the grant. Drained @**a225440af7**.

**ROUND 25's DEFECT IS FIXED, and the control is what proves it.** AC1 reads `1 passed` (the route is registered
under the scoped family) while **AC2, the control, stayed green at `13 passed`** -- so the route is declared AND the
deployed boundary constructs. `build_boundary`'s `operations` now carries `CATALOGUE_OPERATION ->
generate_entry.read_comparison_catalogue`, and the exact-equality route pin was UPDATED to the true three-route
table with `==` kept, which is the required form and not a weakening.

**The WORLD property, verified by the issuer and not taken on report:** the census verdict now reads
`{'guarded': 15, 'routes': 18, 'unguarded': [the three export routes]}` against a base of
`{'guarded': 14, 'routes': 17, ...}`. The unguarded set is UNCHANGED. **The new served route is guarded** -- which is
the whole reason the cell was `WORLD` and the one thing a new route must prove.

### AC3 WAS UN-MEETABLE, BY ANY WORKER, UNDER ANY GRANT -- MY DEFECT, AND NOT THE SAME ONE AS LAST ROUND

Round 25's defect was an under-granted cell. **This one is worse in kind: a criterion that no grant could satisfy.**
`_contracts/tests/test_seam_paired.py:570` derives a document name as
`r.split("#")[0][len("../"):][: -len(".schema.json")]` -- it assumes EVERY `$ref` is a relative `../X.schema.json`.
The published convention is `opal://irpt/contracts/v1/X.schema.json`, so stripping three characters yields
`l://irpt/contracts/v1/X`, and the fixture lookup can never resolve. **That is the exact `l://` string in AC3's
failure message and in all 17 of its sibling control nodes' messages -- which my own preflight printed.**

**The drain's sound substitute for AC3, run in place of it, denominator printed:** `routes.json` is 18 rows with
`declared` and `total` both 18; the catalogue row names
`responses/comparison-catalogue.response.schema.json`; that file exists, is valid JSON, carries `$id`,
`x-contract-version`, `additionalProperties` and `required`; and its refs are `opal://...` like
**18 of 18 published response schemas**. So the outcome AC3 was meant to witness IS MET. **AC3 asked the worker to
break the convention that 18 of 18 files follow in order to satisfy a test that mis-parses all 18.** It is recorded
**VOID AS CUT** -- not met, and not the cell's shortfall.

**THE TRANSFERABLE LESSON, because a second defect in two rounds is a pattern and not bad luck.** I wrote in the order
that AC3's base `no tests ran` (rc=5) was "a third answer state beside pass and fail" -- correct as far as it went, and
then I used it as if it were a base MEASUREMENT. It is not one. **For a PARAMETRIZED node, the base control is not the
absent node -- it is a SIBLING node.** An absent node cannot show you that it will inherit a systemic failure the
moment it is minted. I had 17 siblings failing with one identical cause, printed in my own preflight table, and read
them as "the file is red, so name a single node" when the sound reading was "every sibling fails for ONE cause, so
the new node will too". Naming one node id escapes a NOISY suite; it does not escape a SYSTEMIC one.

### Disposition and what is routed where

- `TO-IB-yr-261` -> **`staged`**: the cell's served outcome is complete and guarded; AC1 and AC2 MET; AC3 VOID AS CUT.
  This is NOT round 25's disposition repeated -- there the cell was incomplete, here the criterion was wrong.
- **The seam-suite defect goes to `1.0.0_SA_CTO` as a DECISION, not a cell**: `test_seam_paired.py:570`'s ref
  convention is wrong for 18 of 18 published response schemas, so the suite cannot grade any contract work by any
  seat, and 33 of its 58 nodes are red for this one cause. Either the suite's parser learns `opal://` or the published
  convention changes; that choice is above this workstream and it is not ~Y's to make. Row `IRPT_BCKEND-W89-S1`.
- **Row `IRPT_BCKEND-W89-S2`, verified at source:** the census's 7th failure is a stale literal `17` at
  `_authz/tests/test_unguarded_census.py:99` (`assert len(table) == 17`), with the same literal at `:114` and `:141`,
  against a published file that now holds 18. **Not** an unresolved route. A third small grant gap -- that file should
  have been in `<paths>` -- and a loud tripwire, not silent harm. It rides the next ~Y cell.
