# Custody eligibility controls prepared for the producer interface

Owner: `2.0.0_SA_COO~Y`. State: PREPARED SPECIFICATION, NOT IMPLEMENTED OR EXECUTED.
Authority: CTO disposition `7a3fd28e112707065a990416ae2e85c519e0de32` and exact inbox message `20260923T153214Z_1.0.0_SA_CTO_IRPT_CTO_policy_disposition7a3fd28e11_an.md`.
Consumer baseline: `819c9e399086cffb2876a21fbc2cee01724b0bd7`.
Source census: M `abfb3eaf8242cf5df26c7e1074e0e555245d969a`.

## Interface that must be identified before implementation

The concrete consumer ports already exist in `ycharts/generate/custody_submission.py`:
`authorize_snapshot(principal, owner)` must return strict True for the current exact accepted binding; `load_normalized(browser, principal, owner)` must return the frozen `{input_id, content_sha256, document}`. These are injection contracts, not located production source adapters.

No concrete producer providing the complete original security-position census has been identified. `holdings/snapshot.py:load_snapshot(firm_id, ..., as_of=None, ..., account_ids=None)` and `HoldingsPublication.load(as_of=None, account_ids=None)` are located readers but cannot supply that missing guarantee: they select a current date index, do not take the admitted snapshot identity, and their display hierarchy is not the required complete actual-security inventory. A selected/redecorated document hash is not the whole-publication revision. M's actual-position producer proposal is the prerequisite; do not implement against guessed field names or model leaves.

Update: consumed M proposal `a20a1a1bd28c2cf76d5b80aae0d9a745ab5c7d2c`, `IRPT_MVP_M/ACTUAL_POSITION_REPAIR_PROPOSAL_20260923.md`. It locates 49F Schwab master08335338 B01 positions, COT Black Diamond fact_holdings through B01, and INF Orion positions_mv through B01. This replaces a missing-source-location question with specific producer work, not a callable accepted consumer interface. M proposes edits to `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` after CTO adjudication; minimal output field spellings still require P/M/Y agreement. Complete current objects, security/currency/cash/sign semantics, independent account tie and exact snapshot binding remain unproved where the proposal says so. Do not directly call or execute B01 runners from the Y factory. The original-row controls apply before the recipe's security/account consolidation; COT's sanctioned relationship-grain collapse must separately preserve raw provenance and prove exact equality of consumed fields, rather than hide an unsupported economic row.

The handoff needed from that proposal is an exact commit, module/export/call signature, server-owned snapshot locator and revision contract, and row field mapping for account/position identity, original decimal spelling, units/currency, security identifier and mapping revision, clocks, complete account census, source receipts, correction lineage and independent reconciliation. It must state which per-firm sources are located and which remain missing. P owns shared callback integration and any public mapping. Y will map the controls below to that concrete producer only after it is identified and within CTO's admitted scope.

## Required ordering and observable boundaries

At the future producer-to-normalizer seam: authorize exact current selection/snapshot; read the original accepted position census; validate completeness/provenance and per-account reconciliation; classify every original position for current recipe eligibility; only then resolve/consolidate supported positive positions and freeze. Recheck exact source and authorization before retention/acceptance. No unsupported position may disappear before classification.

Observe counters for source read, normalization/consolidation, NORMALIZED_PORTFOLIO write, request acceptance, queue dispatch, and vendor transport. Unsupported inputs must produce no normalized success object, no analysis acceptance, no dispatch and no vendor effect. Existing source evidence stays unchanged; do not introduce a new evidence artifact family. Use the supported refusal envelope; internal diagnostics must not become new public enum values without P's paired contract.

## Control matrix

All numbers below are synthetic exact USD strings. These cases define expected behavior, not results.

| ID | Original census / perturbation | Required assertion |
| --- | --- | --- |
| Y-EL01 | Complete accepted A/security-X `12.03`, B/security-Y `7.97`, exact authorized snapshot | Eligible only when identity, source, dates, accounts and reconciliation all pass. Preserve both original rows, exact `20.00` value and every contribution after any allowed positive aggregation. Numeric representation may follow existing canonical decimal formatting. |
| Y-EL02 | X `12.03` and Y `0`; repeat with `-0.00` | Refuse entire selection before consolidation. Preserve original zero spelling and row identity in source evidence; no omitted row or fabricated epsilon. |
| Y-EL03 | Same security X, account A `100`, account B `-20` | Refuse even though consolidated X/net is positive `80`. Inspect both original rows, not only the aggregated security value. |
| Y-EL04 | Same security X `100` and `-100`; repeat all-zero or wholly negative | Refuse; no dropped zero aggregate, absolute-value or gross-notional portfolio. |
| Y-EL05 | CASH `-5` with security X `100`; repeat CASH `0` | Refuse unsupported cash row; no synthetic cash or netting against securities. Positive CASH alone still needs canonical CASH identity and complete source proof. |
| Y-EL06 | Missing/null amount versus explicit `0`; duplicate position ID; missing selected account | Distinguish unknown valuation, zero and census defects internally. All refuse. No account remainder or display-parent substitution. |
| Y-EL07 | SHARES with missing/zero/stale/mismatched-currency quote; target weights masquerading as custody | Refuse. Positive price is independently required; signed shares cannot be made eligible by price multiplication. No model/weight source substitution. |
| Y-EL08 | Changed same-day accepted revision, wrong snapshot/tenant/account, revocation during read | Refuse exact binding; never advance to latest index implicitly. No normalized artifact write after failed final current check. |
| Y-EL09 | Accepted positive request retried after source changes | Reuse exact retained accepted bytes under current access checks or refuse when current binding no longer authorizes them. Never rerun normalization to replace the accepted source under the same request. |
| Y-EL10 | Unsupported signed/zero retained artifact supplied directly with freshly computed digest | Current normalized upload/recipe path refuses before transport. A matching hash is not semantic eligibility. Submission-side pre-dispatch control must also cover the concrete producer, rather than relying solely on a later worker refusal. |
| Y-EL11 | Large decimal, nonfinite, boolean, ambiguous currency, mismatched clock, parent and child money counted twice | Refuse without rounding/truncation/coercion. Independently sourced account reconciliation must catch duplicate parent/child accounting; equal internally computed totals alone are insufficient. |

## Existing behavior versus work still required

The current pure freezer rejects negative/zero original rows before its consolidation loop can complete. The normalized upload bridge and recipe independently require positive dollar values. Existing checks support the intended boundary, but they do not prove a concrete producer preserved the original census before calling them. Do not report this matrix as producer integration PASS.

Implementation remains deferred until the producer interface is identified. No helper relaxation, source adapter, new family, public enum or runtime installation is part of this artifact. Once the producer contract is concrete, pair its real reader with owned eligibility checks and the actual Entry, assert counters at all effect boundaries, and route the exact source/consumer pin and results to CTO. Retained historical requests and existing positive-only recipe versions keep their semantics.

## Direct-review evidence consumed

CTO `8653eb6cd4d4da9e4e36b447a77822e0bf2df71f` records bounded source PASS: factory30/30, original scalar-adapted driver20/20, Portal49/49 with67 assertions. It verified declared package member hashes but explicitly found generate's import gate UNENFORCED because BUILD_MANIFEST.json and declared jsonschema/referencing dependencies were missing. Runtime closure remains P's assignment. These are CTO executions, not a new Y run; no production or complete-journey PASS transfers to this control specification.
