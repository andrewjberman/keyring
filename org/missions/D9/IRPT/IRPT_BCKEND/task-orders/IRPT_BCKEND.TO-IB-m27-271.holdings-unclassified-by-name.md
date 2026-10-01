# TO IRPT_BCKEND.TO-IB-m27-271 -- Holdings serves a security the table lacks as unclassified by name (no build refusal)

<to_id>IRPT_BCKEND.TO-IB-m27-271</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~84</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>superseded</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-271`
(`decompositions/IRPT_BCKEND_DECOMP_R27_M.md`) | **outcome_ref:** FWD-5 (Holdings classes) | **depends_on:** IB-mr-261

---

## WORKER FACE

### THE CELL

`IB-mr-271` -- row IRPT_BCKEND-W84-S3, the issuer's defect from cutting IB-mr-251. The 251 face said a security the
table does not know "refuses loudly by name". The build now raises `ValueError: REFUSED: <ticker> is not in
etf-classifications` (`holdings_snapshot.py` `classify_security`, ~:859-862), and that has two effects:
- A SECURITY node with NO ticker, such as the Schwab cash-sweep row `A_CLIENT` with identity
  `{'namespace': 'UNKNOWN', 'value': 'schwab:CASH'}` (`tests/test_holdings_49f.py:85-86,217`), fails the whole build.
- A real firm build refuses on any held ticker the table lacks. After the MDPF_SECCLASS backfill, 76-601 per firm
  stay unresolved, so a refusing build would never complete.

The governing rule is MDPF_SECCLASS PRD FWD-2: "a security with no entry is shown as unclassified by name, never
quietly put into some class".

This order runs AFTER IB-mr-251 and IB-mr-261 in the same worktree (your branch @bb9e765c4d). Build on them.

**Build (LOCAL build + record -- no upload, no mint, no deploy):**
1. **Unclassified by name.** A ticker the table lacks gets the producer's existing unknown classification
   (`_unknown_classification`, ~:1102, or its equivalent at your HEAD), carrying the security's own symbol and
   display, and a basis that says `etf-classifications: no row`. It is never refused and never guessed.
   `class_totals` (261) carries these under the unknown class, so no mass drops.
2. **No lookup without a ticker.** `annotate_classification` never calls the table for a SECURITY node whose
   identity namespace is not a ticker (e.g. `UNKNOWN`). That node keeps the classification it had before 251: the
   cash rules, the BD `CASH -- CASH` rule (CTO 101547), or unknown. No existing refusal other than 251's new one
   changes.
3. **Tests.** The full `data/assets/scripts/gold/investor_reporting/tests` suite passes WHOLE. The 15 tests from
   W84-S3 pass with their assertions untouched, including `test_holdings_49f.py:217`. Add tests in
   `tests/test_holdings_unclassified.py`:
   - a ticker absent from a stubbed table is unclassified with its symbol and not refused;
   - a no-ticker node is never looked up;
   - GLD, PHYS and VXX still land as placed.
4. **Census** from REAL local Holdings builds at all three firms, reading the LIVE etf-classifications, which since
   MDPF_SECCLASS release step 1 holds 375 rows with PHYS. Write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R27_UNKNOWN_CENSUS_20260930.json` as
   `{"firms": [{"firm", "as_of", "completed": true, "securities", "refused": 0, "guessed": 0, "unclassified",
   "unclassified_names": [...], "no_ticker_nodes", "placed": {"GLD": [class, sub], ...}}]}`.

### ACCEPTANCE

<criterion id="IBM27-271-AC1" cell_refs="IB-mr-271"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R27_CHECKS/r27_suite_whole.py data/assets/scripts/gold/investor_reporting/tests</invocation><expect>SUITE-WHOLE</expect></criterion>
`IBM27-271-AC1` -- the whole investor_reporting suite passes, with no assertion weakened.

<criterion id="IBM27-271-AC2" cell_refs="IB-mr-271"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R27_CHECKS/r27_unknown_census.py</invocation><expect>UNKNOWN-CENSUS</expect></criterion>
`IBM27-271-AC2` -- real builds complete at all three firms with every unknown unclassified by name, nothing refused,
nothing guessed.

<expected_criteria>IBM27-271-AC1,IBM27-271-AC2</expected_criteria>

Dry-run 2026-09-30 00:5xZ:
- AC1 at CLOUD @6c0317e55c: SUITE-WHOLE 314 passed. That is a control, since CLOUD lacks 251.
- AC1 at the worker's base wk-IRPT_BCKEND-84 @bb9e765c4d: SUITE-BROKEN 6 failed, 315 passed, 9 errors -- FAIL as
  expected.
- AC2 at both: NOT-CENSUSED (census absent) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** No upload, no mint, no deploy. The builds READ the firm buckets and the table.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W84-S<k>`), and do not weaken the test to pass.

<paths>
data/assets/scripts/gold/investor_reporting/
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R27_UNKNOWN_CENSUS_20260930.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R27_M.md</decomp_doc> (round 27, workstream ~M), cell `IB-mr-271`.
<owned_cells>IB-mr-271</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM27-271-AC1, IBM27-271-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~84/IRPT_BCKEND.TO-IB-m27-271.holdings-unclassified-by-name.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM27-271-AC1,IBM27-271-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the classifier's change, the no-ticker path, the suite line, the census per firm (securities,
unclassified, no-ticker nodes, GLD/PHYS/VXX), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change; 251/261/271 release together under their halves after the MDPF_SECCLASS backfill.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant change (251's desired GetItem/Query stands).
comp-adversary: RUN -- 1 row read (W84-S3: 15 of 37 failures share the A_CLIENT no-ticker fixture), 1 code read (classify_security raises on a falsy or absent ticker), 1 census read (MDPF_SECCLASS backfill unresolved per firm: bd 207, 49financial 601, inflection 76); BLIND: the per-firm count of no-ticker nodes in real builds is unmeasured at the cut (step 4 counts it).
lane: the <paths> block IS the grant.
</preflight>

Source: row IRPT_BCKEND-W84-S3 (0.9.0_WK_IRPT_BCKEND~84); MDPF_SECCLASS PRD FWD-2; the issuer's own defect in IB-mr-251's face.

## AMENDMENT (2.0.0_SA_COO~M, 2026-10-01 ~04:4xZ) -- SUPERSEDED, on the CTO's sweep-5 analysis

Issuer act on 1.0.0_SA_CTO's ruling: `org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.sweep5.md`
@a50d8207bc section 2 item 4 ("RE-CUT, not drained and not retired"). This order reads `complete` only on
branch `wk-IRPT_BCKEND-84` @00b88da890, which was built on IB-mr-251's table-only classifier before IB-mr-291
(@9fef6a7e9c) changed the same files on CLOUD; that branch is not merged. No criterion of this order is claimed
as passed on CLOUD. The order is superseded, not complete.

**Superseded by:** superseded by FAST lease, drive-mode.log line 30 (`ARM IRPT_BCKEND~M`, 2026-10-01T04:31:33Z, on Andrew-direct
~04:2xZ via 1.0.0_SA_CTO 103440). The round-30 re-cut the analysis named is not issued: under the lease the
seat builds the port itself. On the 291 base the classifier already serves an unknown ticker
as unclassified without a refusal; the tests that hold it there are next-list item 2 of `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~M.md`.

The branch ref `wk-IRPT_BCKEND-84` is kept until the port lands on CLOUD (it is the port's source).
Gate limb: none graded this modification (a status change on an existing order; no placeholders declared).
