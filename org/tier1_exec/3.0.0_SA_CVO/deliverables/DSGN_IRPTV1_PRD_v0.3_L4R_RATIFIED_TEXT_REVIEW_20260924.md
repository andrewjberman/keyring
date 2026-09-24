# L4-R review -- DSGN_IRPTV1 PRD v0.3, ratified-text half (`3.0.0_SA_CVO`)

**PRD:** `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` @`118613ddb0` (v0.3). **Half:** ratified-text,
hash `4540ecd4e08a`, re-measured from HEAD's bytes with `prd_signoff_lib.half_hashes()` -- the same hash the v0.2
delivery named (@`6c708bcdb2`); the v0.3 bump changed the brief half only, so this review covers both deliveries.
**Deliveries:** `1.0.0_SA_CTO` msgs 100269 / 100271 (v0.2) and 100283 (v0.3), all three READ-acked.
**Verdict: REFUSE.** One defect against the counterpart PRD (R1) and one wrong count (R2). Both fixes are bounded to
the CONTRACTS section; nothing in the ENDPOINT pin moves.

## What holds

- **ENDPOINT is verbatim.** The fenced block in the PRD and the block in the endpoint record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_DSGN_IRPTV1_20260924.md` @`5daacc16db` are IDENTICAL: 91
  lines of 91, zero diff lines (`difflib.unified_diff`). The "Not promised" paragraph equals the record's "WHAT THE
  ENDPOINT DOES NOT PROMISE" paragraph under whitespace normalisation.
- **11 outcomes, FWD-1..FWD-11; DONE WHEN tags 7 EXERCISED (1, 2, 3, 5, 6, 7, 8) and 4 APPLIED (4, 9, 10, 11)**, which is
  exactly the record's own PROVENANCE line. Every outcome is provable by an act a seat can take on demand; none is a
  wait. FWD-1 is the thread.
- **No seat name, lane or history inside the ENDPOINT section** (the spine's clause is scoped to `_top_section` of
  ENDPOINT, `to-pipeline-gate.py` `def _top_section`): regex census over the section returns 0 serials, 0 `~lane`
  tokens, 0 commit hashes, 0 message ids. The SOURCE lines carry brief headings, card numbers and one "Andrew-direct
  ~05:4xZ", all verbatim from the pin.
- **The three rulings CONTRACTS cites exist and say what CONTRACTS says.** `IRPT-HOLDINGS-DISPLAY-NAMES-20260924`,
  `IRPT-HOLDINGS-VALUATION-FACTS-20260924`, `IRPT-DESIGN-RECON-CALLS-20260924` each resolve in
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` (comp-find: 17 / 6 / 9 hits over
  198,302 files). Ruled shapes match the section: `display` {label, symbol?, description?}; `CUSTODY_UNITS` with units
  `UNITS`, enum + units rule extended, both copies, portal-first; `spread` additive optional per comparison row, P,
  both copies. `PRICE REFUSED this round` matches "no price fact exists and none is rendered".
- **`display` is accepted by the portal since DEV `7975c3bb`, as written:** portal commit `bf3b971b` (wire type,
  validator, adapter) is an ancestor of `7975c3bb`, and `7975c3bb` is on DEV (`git merge-base --is-ancestor`, both
  arms).
- **The selection rule is the contract's:** `sel_[0-9a-f]{64}$` in
  `docs/contracts/investor-reporting/v1/SelectedAccounts.schema.json`; `POST /api/scoped/investor-reporting/selections`
  -> `selection-create` in `routes.json`.
- **"Summary.tsx: IT COMPUTES NOTHING" stands:** `portal/src/pages/InvestorReporting/render/performance/Summary.tsx:4`.

## Refusal items

### R1. CONTRACTS is silent on `unprojected_grant`, the one render obligation the counterpart PRD places on this page, and the ENDPOINT it sits beside moves that indicator behind a click

**The counterpart.** `IRPT_FNTEND_PRD.md` v0.10, CONTRACTS, the `(v0.7)` clause: *"THIS PROJECT OWES A RENDERING: a
VISIBLE partial indicator whenever `unprojected_grant.count > 0`, on every view that displays a scoped result"*, with
`(v0.8)` the two-shape rule (*"branch on the shape FIRST"* -- a refusal whose `public_reason_code` is
`UNPROJECTED_GRANT` carries no `unprojected_grant` key at all) and `(v0.9)` the `irpt-holdings` exemption (count is
STRUCTURALLY ZERO on that route until `IRPT_BCKEND.TO-IB-rtf-8` folds the fork). Its origin is CTO ruling
@`61627f39f9` condition 2, carried as row `IRPT_BCKEND-W1-S28`, which at HEAD reads `hazard_standing: ARMED`,
`disarm.state: ARMED`, `disarm.owner: 1.0.0_SA_CTO`, `remediation.state: OPEN`, with 0 later rows referencing it
(`REMEDIATION_v1.md`, 140 rows read). The row disarms *"when a cell here renders the indicator and captures it"*.
The served page renders it today: `portal/src/pages/InvestorReporting/header/ScopeSummary.tsx:111-112`
(`<PartialDisclosureFact>` when `count > 0`, FE-s-59, `data-slot="partial-disclosure"`) and the FE-s-58 status badge.

**This PRD.** Brief O1 names *"unprojected grant"* among the header bookkeeping to move into an "About this scope"
disclosure. FWD-2 ACCEPT: *"nothing about entitlements, revisions or cohorts is on it, and all of that is one click
away."* CONTRACTS' closing rule licenses exactly that move: *"the disclosure surfaces ... keep every envelope fact the
evidence rules require ... it moves, it does not vanish."* Nowhere in CONTRACTS does `unprojected_grant`, the
two-shape rule or the holdings exemption appear.

**Why it is a refusal and not a note.** Hop 5 of the round-1 thread is the identity card (C1), the surface that
carries the indicator today. A C1 cell cut from these bytes moves the partial indicator one click down and passes
every criterion in this PRD -- and the counterpart's own words for that outcome are *"a frontend that renders nothing
because `count == 0` and treats the present key as proof of health is CORRECT PER THIS CONTRACT AND WRONG IN FACT"*.
Two ratified texts would then state opposite things about one DOM fact, and an ARMED row owned by the CTO would be
re-opened by the very round that builds the header. This is the conjunction class: each section is right alone.

**Fix (CONTRACTS only; ENDPOINT untouched).** One paragraph under the additive members: `unprojected_grant` is a
PARTIAL-DATA fact, not entitlement bookkeeping. When `count > 0` a VISIBLE indicator in advisor words ("N of M
accounts not shown", or the counterpart's own wording) stays on the BODY of every view that displays a scoped
result, the header identity card included; `kinds`, the denominator and the revision go to the "About this scope"
disclosure. Branch on the shape first: a refusal whose `public_reason_code` is `UNPROJECTED_GRANT` renders its reason
and carries no count. On `irpt-holdings` the count is structurally zero until the fork is folded, so a present zero
on that route is not health. Cite `IRPT_FNTEND` CONTRACTS v0.7-v0.9, ruling @`61627f39f9` condition 2 and row
`IRPT_BCKEND-W1-S28`. FWD-2's ACCEPT names "entitlements, revisions or cohorts", not the partial indicator, so the
reconciliation lives in CONTRACTS and the pin does not move.

### R2. "the ten v1 operations" is the wrong count in the wrong unit

The brief (Part II) says *"the ten contracts in `contracts/index.ts`"*; the counterpart `IRPT_FNTEND` CONTRACTS
consumes ten of the counterpart's inventory of eleven and produces `RenderPackage`. CONTRACTS here writes *"the ten
v1 operations under `docs/contracts/investor-reporting/v1/`"* and then names 15 operations itself.
`docs/contracts/investor-reporting/v1/routes.json` @`124c0694b7` (2026-09-23) enumerates **17** operations: 14
`DECLARED` and 3 `NO-HANDLER-AT-HEAD` -- `analysis-input-upload`, `analysis-request-read`,
`analysis-request-history`, the three FWD-7 and FWD-8 stand on. The section's own SURFACE MANIFEST (brief half) says
"the ten v1 contracts", which is the right unit.

**Fix.** "the ten consumed contracts (the counterpart's inventory of eleven less `RenderPackage`) and the operations
that serve them", and add the three `NO-HANDLER-AT-HEAD` Analysis routes to the "Deferred, not blocking" list as
Y's, so no cell is cut against a route the register says has no handler.

## Measured state carried for L5 (no change to the text; the text says "ruled", which is true)

| member | ruling | portal wire type (`contracts/wire/*.ts`) | docs copy (`docs/contracts/.../v1/*.schema.json`) |
|---|---|---|---|
| `HoldingsSnapshot` node `display` | yes | PRESENT (`bf3b971b`, on DEV) | ABSENT (0 hits @HEAD) |
| `valuation_facts` `CUSTODY_UNITS` / `UNITS` | yes | ABSENT (enum = six `SMARTX_*` kinds) | ABSENT (same enum, units const `USD`) |
| `PerformanceReport` per-comparison `spread` | yes | ABSENT (0 hits) | ABSENT (0 hits) |

So at HEAD hop 7 and 8 can read `display` on DEV, and neither `spread` (hop 6) nor `CUSTODY_UNITS` exists on any
copy. "Each member lands in both schema copies" is the order rule, not a state; the COO cuts hops 6-8 knowing this.

## Observation routed to `1.0.0_SA_CTO`, not a defect of this half

v0.3's ENRICHMENT BACKLOG item 11 grades hop 6 on "not supplied" for `spread`, while FWD-1's ACCEPT requires the
user to name *"her year-to-date return and spread"*. Both are right: the round-1 trace can PASS its hops with the
spread NOT SUPPLIED and FWD-1 stays open until P serves `spread`. The round-1 analysis should say so in one line, so
nobody reads a passing trace as FWD-1 REALIZED. The ENDPOINT is verbatim from the pin and is Andrew's to confirm.

## Instruments

| question | instrument | result |
|---|---|---|
| ENDPOINT verbatim? | `difflib.unified_diff` on the two fenced blocks at their pins | 0 diff lines, 91 of 91 |
| half unchanged v0.2 -> v0.3? | `prd_signoff_lib.half_hashes()` at HEAD; `git diff 6c708bcdb2 118613ddb0` | `4540ecd4e08a` both; diff touches THE THREAD, ENRICHMENT BACKLOG, PATHS, PROVENANCE only |
| seat names in ENDPOINT? | regex census over the section | 0 / 0 / 0 |
| rulings exist? | `comp-find` over corpus=all | 17 / 6 / 9 hits across 198,302 files; each in RULINGS.md |
| `display` accepted on DEV? | `git -C portal merge-base --is-ancestor`, two arms | `bf3b971b` <= `7975c3bb` <= DEV |
| members on the wire? | word-boundary counts in both copies | table above |
| S28 standing? | JSON blocks of `REMEDIATION_v1.md` parsed, 140 rows | ARMED / OPEN / 0 later rows |
| operation count? | `routes.json` parsed | 17 distinct (14 + 3) |

-- `3.0.0_SA_CVO`, 2026-09-24 ~05:5xZ
