# ETFS_RIVALS task order -- `RIV-nm-2` -- ROUND 7 (ENRICHMENT): THE CUSIP-KEYED G4 REQUEST ASKS FOR A NAME (RFW-D11)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-nm-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~3</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~21:3xZ, --drift) -- carrier C1 PARTIAL inside the 90 s budget (446 of 65,153 files scanned, 0 gates armed); C2-C6 not scanned (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 7** makes the 09:00 ET sweep run the AI step itself (round 6 left no scheduled path to it), makes every run carry its trigger, has the census read the rankings' classification and agree with the header, gives one deterministic name per security, asks Bloomberg for the CUSIP lines' names, and carries the page-walk remainder (PRD v0.13). Nothing in round 7 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-nm-2` -- the CUSIP-keyed G4 request asks for a name (RFW-D11)
- The OFFLINE G4 plan (`enrichment_bloomberg.py` ~:103-114) requests a security-name field, and G4 rows carry it.
- The producers' name candidates include the G4 name, so `names.display_name` prefers it over a 30-character cut (IDVZ's
  "International Container Termin").
- The 2026-10-05 vehicle run does NOT fix these without this cell: the IDVZ CUSIP lines share no key with any named line.
- **Organic trigger:** the vehicle's 08:03 ET enrichment step. Its G4 object is the evidence.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 50761d39e9 (the package equals the deployed pin eb6e9f04ff))

- Field: LONG_COMP_NAME (not NAME -- NAME is measured ALL CAPS and cut at 28 chars in integrations/bloomberg/research/field_map.json, e.g. 'MITSUBISHI UFJ FINANCIAL GRO'; the estate already reads LONG_COMP_NAME first, NAME as fallback: lib/research/filings/battery.py:563-565). Written to a new G4 column `security_name`.
- Each producer reads G4 security_name from objects dated ON OR BEFORE the page day and adds it to display_name's candidates (a fix reading G4 only at the page day fails nm-2.AC2).
- TRAPS (measured by the check writer): adding LONG_COMP_NAME to the fields breaks the past-date historical test in `_market_pull` -- every past-date row would land as `pull` unless the name field is excluded from that test; tests/test_s4_security_market.py asserts the exact 10-field set (granted below, update it); the import-market path carries NAME only, so its security_name stays NULL.
- This file is run by the terminal vehicle from the CLOUD tree (the 08:03 ET enrichment step): the daily pull must keep landing; never call Bloomberg (the issuer proves the live field after the drain).
- Your previous order on this slot (nt-1) owns the name-map tie-break in the same producers; build on it.
- Organic trigger: the vehicle's 08:03 ET enrichment step; its G4 object is the evidence.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/` and rounds 5-6's `.../round5/checks/`, `.../round6/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.13), the round-6 analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round6.md`, the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-7 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r7nm2_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/gold_holding_contribution.py
data/etfs/scripts/rivalfunds/gold_buying_trend.py
data/etfs/scripts/rivalfunds/tests/test_r7nm2_*.py
data/etfs/scripts/rivalfunds/tests/test_s4_security_market.py
data/etfs/scripts/rivalfunds/tests/test_e1_enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_a1rk_contribution.py
data/etfs/scripts/rivalfunds/tests/test_a1tb_trend.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the OFFLINE G4 plan requests LONG_COMP_NAME and G4 rows carry it as security_name; control: a security without it stays NULL (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/nm-2.AC1.py`)
- **AC2** -- both producers name IDVZ's 30-char-cut securities by the G4 full name via display_name; control: an uncut name is unchanged (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/nm-2.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-nm-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/nm-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-nm-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/nm-2.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-nm-2.cusip-g4-asks-for-name.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-nm-2.cusip-g4-asks-for-name`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-6 analysis @94f682c868 (CTO~Z msg 28735) section 3 + the RFW register
graded against rv-publish-1002r6; decomposition round 7 v1.0; Andrew-direct max parallelization (cooRV record 141xZ). Chain `~3`, slot `~3`, position 2 of 2 (nt-1 -> nm-2). Checks dry-run at base CLOUD 50761d39e9 (the package equals the deployed pin eb6e9f04ff):
nm-2.AC1 FAIL (2; control OK) as expected; nm-2.AC2 FAIL (2; control OK) as expected; each PASSES under an in-memory fix.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>7</round>
<slot>~3</slot>
<fabric>site-z</fabric>
