# TO MDPF_SECCLASS.TO-SC-k1 -- the FWD-7 scheduled classification, the backfill census, BD's detection as its first caller

<to_id>MDPF_SECCLASS.TO-SC-k1</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~1</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-k-1` (`decompositions/MDPF_SECCLASS_DECOMP.md`) |
**outcome_ref:** FWD-7 (feeds FWD-1) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-k-1`. The canonical per-security table is DynamoDB `etf-classifications` (hash key `ticker`; 344 rows today; GSIs
`asset-class-index`, `sub-asset-class-index`). Its one client is
`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`, and its seed source is
`infra/aws/lambda/v2_portal/_shared/etf_classification.py`. The Black Diamond fork `bd-securities` (10,929 rows) is
retiring. FWD-7 (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`): "A security that newly appears in
any firm's daily holdings gets its entry in the shared list on a regular schedule". CTO 103040 orders the backfill of
every held security first, through this same path, with bd-securities as reviewed INPUT only.

**THE RULE THAT BINDS THIS CELL (Andrew-direct 2026-09-29, verbatim): "the canonical table should not be overwritten by
anything in bd-securities."** So also PRD C-WRITER, per `org/standards/MDPF_SECCLASS_CONTRACT.json`:
- A scheduled write lands only for a ticker with NO row. It is a conditional put on the row's absence
  (`attribute_not_exists(ticker)`), and it carries `classified_by = "scheduled"`.
- It never replaces or edits an existing row, GLD, PHYS and VXX included.
- A value read from bd-securities is an INPUT to a new row only, and each such row is listed for review.

**Build (LOCAL build + record: no table write, no deploy, no schedule):**
1. **Module.** Write `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`, beside the one client, and
   import the client from there (do not copy it). Given ONE firm's held securities (ticker, name), it plans a row for
   each ticker the table lacks. Classify from inputs already held, in this order (PRD C-VENDOR):
   - (i) the ticker's bd-securities row, read once as input. Map its `asset_class` to the table's own class
     vocabulary (read it from the seed source and the live table). A value that maps only through a fold (e.g.
     hedge -> alternatives, or alternatives/Gold for a gold fund) is NOT mapped: that ticker stays unresolved, listed
     by name;
   - (ii) Bloomberg GICS fields where the estate already holds them;
   - (iii) the Schwab security master where held.
   No outside model is called, and no guess is made: an unresolved ticker gets no row.
   Each planned row also carries `instrument_kind` (`fund` / `single_security`, with the contract's definitions) and
   `industry`: the GICS industry-group name through the one client's `resolve()`, Bloomberg as input (CTO 103036).
   Where kind or industry is unknown, the attribute is absent, never defaulted. Name `updated_by` after the job.
   Provide a `write(plan)` that uses the conditional put, and a CLI with `--firm <firm> --dry-run`, where dry-run is the
   only mode you run.
2. **Caller.** In `data/black_diamond/scripts/gold/E_18.detect_new_securities.py`, BD's daily detection step feeds its
   new tickers to the module instead of writing stubs to bd-securities. Keep the detection; retire the bd-securities
   stub write. The BD gold layer runs E_18 on its schedule, so this is FWD-7's first scheduled caller (firm tree kept,
   C-FIRM).
3. **Tests** in `infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_scheduled.py`, on a stubbed table:
   - an absent ticker gets one scheduled row;
   - an attempt to overwrite GLD with its bd-securities value (alternatives/Gold) is REFUSED by the condition, and the
     GLD row is unchanged;
   - a fold-only value leaves the ticker unresolved;
   - no outside-model client is constructed;
   - `instrument_kind` and `industry` are absent when unknown.
4. **Census**, in dry run, over each firm's latest held securities. Read each firm through its own tree:
   - `bd`: `opal-data-bd` gold/holdings_lots;
   - `49financial`, `inflection`, `cottonwood`: each firm's own latest holdings source, where one exists.
   Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BACKFILL_CENSUS_20260929.json` as:
   - top level: `{"overwrite_refused_control": true|false, "firms": [...]}`;
   - each firm: `{"firm", "as_of", "held_tickers", "already_present", "would_write", "unresolved": [names],
     "overwrites": 0, "vendor_calls": 0, "rows": [...]}`;
   - each row: `{"ticker", "asset_class", "sub_asset_class", "instrument_kind", "industry", "classified_by": "scheduled",
     "input": "bd-securities|gics|schwab"}`.
   Record `overwrite_refused_control` from a REAL conditional put against the live table's GLD row, not a stub. Use a
   no-op put that must fail on the condition: prove refusal only, and change nothing.
5. **Half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BACKFILL_20260929.md`
   (`## The act`, `## Blast radius`, `Rollback per key`), for the first real scheduled write:
   - the rows per firm, from the census;
   - every caller of `find_by_asset_class` / `find_by_sub_asset_class` (the one client, :116-158), whose results grow
     by about 10k rows;
   - the IAM change as desired, not applied: PutItem on `etf-classifications` for E_18's principal, and removal of its
     bd-securities write;
   - rollback: delete exactly the rows with `classified_by = scheduled` that this write added;
   - the schedule: the BD gold-layer run that already calls E_18. Any new name comes from `lib/opal_naming.py`
     `name()` (C-NAMES: `mdpf-secclass-lambda` / `-role` / `mdpf-secclass-daily`).

### ACCEPTANCE

<criterion id="SC1-k1-AC1" cell_refs="SC-k-1"><invocation>python -m pytest infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_scheduled.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC1-k1-AC1` -- absent-only scheduled rows, the GLD overwrite refused, no fold, no outside model.

<criterion id="SC1-k1-AC2" cell_refs="SC-k-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_CHECKS/r1_backfill_census.py</invocation><expect>BACKFILL-CENSUS</expect></criterion>
`SC1-k1-AC2` -- the dry-run backfill per firm: every held ticker accounted for, zero overwrites, zero vendor calls, the
live overwrite control refused.

<criterion id="SC1-k1-AC3" cell_refs="SC-k-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BACKFILL_20260929.md</invocation><expect>HALF-READY</expect></criterion>
`SC1-k1-AC3` -- the half for the first scheduled write, for the issuer to sign and send.

<expected_criteria>SC1-k1-AC1,SC1-k1-AC2,SC1-k1-AC3</expected_criteria>

Dry-run at the base 2026-09-29 22:0xZ: AC1 "no tests ran", AC2 NOT-CENSUSED (census absent), AC3 NOT-READY -- FAIL as
expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** No table write except the one no-op conditional put in step 4, which must fail. No deploy,
  no schedule, no IAM apply, no outside-model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W1-S<k>`), and do not weaken the test to pass.

<paths>
infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py
infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_scheduled.py
data/black_diamond/scripts/gold/E_18.detect_new_securities.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BACKFILL_CENSUS_20260929.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BACKFILL_20260929.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP.md</decomp_doc> (round 1), cell `SC-k-1`.
<owned_cells>SC-k-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC1-k1-AC1, SC1-k1-AC2, SC1-k1-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~1/MDPF_SECCLASS.TO-SC-k1.scheduled-classification.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC1-k1-AC1,SC1-k1-AC2,SC1-k1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the module's API, the input order and the unmapped (fold-only) values found, E_18's change, the census per
firm (held, present, would-write by input, unresolved), the live overwrite control's response, the find_by_* callers,
the pytest line, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no schedule is created; E_18 already runs on the BD gold-layer schedule and the half names it.
comp-iam: RUN -- bd-pipeline/iam.tf defines the BD roles; E_18's production principal and its etf-classifications rights are unmeasured at the cut (the half drafts PutItem-on-absence and the bd-securities write removal, desired only).
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; decomposition findings inlined (344 vs 10,929 rows; the fold values; find_by_* growth).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 (ADMITTED @b9680cfe86); CTO 103040, 103036; Andrew-direct 2026-09-29 ~21:4xZ.
