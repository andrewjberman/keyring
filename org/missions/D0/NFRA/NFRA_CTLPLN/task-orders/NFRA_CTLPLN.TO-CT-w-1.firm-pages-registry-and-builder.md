# TO NFRA_CTLPLN.TO-CT-w-1 -- round 8 CT-w-1: the firm-access registry file, the builder edit, the generated module (FWD-28, the plan of record's steps 1-2)

<to_id>NFRA_CTLPLN.TO-CT-w-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~65</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-w-1` (`decompositions/NFRA_CTLPLN_DECOMP.round8.md`) | **outcome_ref:** FWD-28 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-28: the data proxy's two class-(i) routes (`POST /sentiment/keyword-intelligence`, `GET /aum/metrics`) must gain a firm check with NO firm name typed into any code file. The commit-time naming gate refuses a firm token in a file that is not a registry file or a generated carrier of `lib/opal_naming.py`. The CTO has approved the plan of record, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~64/PROPOSAL_FIRM_ACCESS_REGISTRY_ROW.md` (READ IT WHOLE FIRST: sections 2, 3, 5 and 7 are your spec, with the line numbers into `lib/opal_naming.py`), and ruled five points in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_CTLPLN_CT_V2_FIRM_ACCESS_REGISTRY_FIVE_POINTS_20261012.md`. You do steps 1 and 2 of its section 7: the registry file, the generator edit, and ONE regenerated module. Another cell (CT-w-2) patches the handler; you do not touch the handler.

### BUILD

1. **`infra/logic/registry/firm_pages.json`** (new), in the shape of proposal section 2: `_about`, `internal_firm`, `exempt_pages`, four `firms` rows (each firm's pages exactly as in the proposal, which read them from `portal/src/lib/firmAccess.ts`; RE-READ that file's `FIRM_ALLOWED_PATHS` and use its content, not the proposal's copy, if they differ, and say so), and two `open_routes` rows. **CTO RULING (point 3): no `"ALL"` token.** For `GET /aum/metrics`, `pages` is the explicit list of the TEN distinct page paths that are the union of the four firms' sets (print the ten in your report). The test tenant of proposal section 0 gets NO row (point 2, confirmed).
2. **The builder edit to `lib/opal_naming.py`**, as proposal section 3 specifies: the new name in `REGISTRY_FILES` and `OPTIONAL_REGISTRY_FILES`; the VIEWS entry `("infra/aws/lambda/portal_data_proxy/firm_page_access.py", "py", ("ROUTE_FIRMS",))`; the WHOLE_FILE_TARGETS entry; the `TARGET_REGISTRY_KEYS` entry (`("firm_pages", "scopes")` in the form that table uses); the BLOCKS entry and the renderer `_blk_route_firms`; the `validate()` rows that refuse: a firm value that is not a served tenant key; the value `null`; an `open_routes` route that is not a route of the data proxy (the 41 keys of `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~62/DATA_PROXY_ROUTE_CLASS_CENSUS.md`; you may carry that list as data in the registry file under a key such as `proxy_routes` if the validator needs it, and say where); a page path in a firm row that is not in the union of the ten. **Conditions (CTO point 1): the selftests gain one case per new row kind; the generated file carries the GENERATED header (the mark) and a drift check; THE GENERATOR EDIT IS ITS OWN COMMIT, passed through `.tools/commit-gate.sh`; commit it BEFORE the regenerated module and the registry file are committed.** Nothing already generated may move: after your edit, `python -I lib/opal_naming.py generate --out <a temp dir>` for ALL targets must reproduce every committed carrier byte for byte except the one new target (print the diff count).
3. **Regenerate ONE target into the repo**: `python -I lib/opal_naming.py generate --out . --target infra/aws/lambda/portal_data_proxy/firm_page_access.py`; run it a second time and show the bytes do not change. The module defines `ROUTE_FIRMS` = `{'POST /sentiment/keyword-intelligence': frozenset((...)), 'GET /aum/metrics': frozenset((...))}` between the generator's marks. It contains firm names ONLY because the generator wrote them.
4. **Tests**, new file `lib/tests/test_opal_naming_firm_pages.py` (model: `lib/tests/test_opal_naming_bronze_homes.py`, lines 50-53 for the drift check): T1 the committed module equals a fresh render; T2 the mark's first line carries the 16-hex hash and `over firm_pages.json,scopes.json`; T3 a firm token appears nowhere in `infra/aws/lambda/portal_data_proxy/*.py` outside `firm_page_access.py` (an in-process scan; it must not call the naming-gate subprocess); T4 the validate() refusals (one case each); T5 the ten page paths are named in the `GET /aum/metrics` row and no `ALL` token exists anywhere in the file; T6 `python -I lib/opal_naming.py targets` lists the module as SHIP lambda. Do NOT type any of the four firm names in the test file: read them from `scopes.json` or the registry at run time.

### RULES FOR THIS CELL

Your write surface is exactly the `<paths>` below. You do not touch the handler, any test under `infra/aws/lambda/portal_data_proxy/tests/`, `lambda-source-map.json`, `portal/`, or the portal carrier (another cell). You run no terraform, no aws call and no deploy; you push nothing. Use `.tools/safe-commit.sh` for every commit (it runs the naming gate; if the gate REFUSES, STOP and file a BLOCKING row: never wrap, encode or split a token). No non-ASCII added. Python 3.9-compatible additions in `lib/opal_naming.py` (match the file's idiom). The law files CLAUDE.md and org/XXX.md are LOCKED.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W65-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTw1-AC1" cell_refs="CT-w-1"><invocation>python -m pytest -q lib/tests/test_opal_naming_firm_pages.py</invocation><expect>passed</expect></criterion>
`CTw1-AC1` -- the new tests pass (T1-T6), including the drift check and the validate() refusals.

<criterion id="CTw1-AC2" cell_refs="CT-w-1"><invocation>python -I lib/opal_naming.py targets</invocation><expect>firm_page_access.py</expect></criterion>
`CTw1-AC2` -- the target list names the new module (SHIP lambda); `validate` also exits 0 (report its line).
</proof_of_spec>

<expected_criteria>CTw1-AC1,CTw1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~65/NFRA_CTLPLN.TO-CT-w-1.firm-pages-registry-and-builder.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTw1-AC1,CTw1-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID. Your queue then continues with `CT-w-2`, handed by the issuer.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round8.md</decomp_doc>
<owned_cells>CT-w-1</owned_cells>
</decomp_ref>

<paths>
infra/logic/registry/firm_pages.json
lib/opal_naming.py
lib/tests/test_opal_naming_firm_pages.py
infra/aws/lambda/portal_data_proxy/firm_page_access.py
portal/src/lib/firmAccess.ts
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a firm token typed into code (the gate refuses; T3 scans); a builder edit that re-marks an existing carrier (every other target is regenerated and compared); an `ALL` token that widens a route silently (CTO point 3; T5); a derived firm set that admits the registry's extra test tenant (explicit rows only; the test tenant has none); BLOCKED by design: the handler and the apply (CT-w-2, CT-w-3). `portal/src/lib/firmAccess.ts` is listed in <paths> as READ-ONLY.
risk: WORLD is declared because the L6 gate derives a floor from the infra and lib paths; this cell applies and deploys nothing.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `ROUND_ANALYSIS.round7.md` section 3 (E10 b), CTO ruling msg 108481, the proposal (CVO MET C-S23).
