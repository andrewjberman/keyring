# TO MDPF_SECCLASS.TO-SC-e9 -- round 3 SC-e-9: cusip-keyed-rows

<to_id>MDPF_SECCLASS.TO-SC-e9</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~4</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-9` (`decompositions/MDPF_SECCLASS_DECOMP_R3.md`) |
**outcome_ref:** FWD-2, FWD-7 | **depends_on:** SC-e-3 (queued on slot ~4); the contract field rides SC-e-1

---

## WORKER FACE

### THE CELL

`SC-e-9`, item E9, added by the CTO (cut as round 3: GATE (x) admits one issuance per round): RULING 103137 (hold the IRPT Holdings canonical release) and RULING
103140 (the key design). IRPT_BCKEND's post-backfill Holdings census (IB-mr-281) found 449 (49financial), 826
(inflection) and 565 (cottonwood) securities that would go from a bd-securities-derived class to unclassified. Most are
CUSIP-only bonds with no ticker, and `etf-classifications` is keyed by `ticker`.

**The key (CTO 103140, option a):**
- A bond's row is keyed `ticker = "CUSIP:<9 chars>"` and carries `identifier_namespace = "CUSIP"`.
- There is no table change, and a CUSIP key cannot collide with a ticker.
- The contract v0.2.0 (SC-e-1, which rides the field) gives C-FIELD `identifier_namespace` in `{TICKER, CUSIP}`; an
  absent value reads TICKER.

**CTO conditions before any CUSIP write:**
- A census of EVERY reader that scans or iterates the table, printed with its denominator. A prefixed key must not
  surface in a ticker-keyed list or page.
- The write is a conditional put on absence, like the scheduled path, under its own halves.

**Build (LOCAL build + record: no table write):**
1. **Planner.** Extend `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` so that, for one firm's
   held securities, a security with NO ticker and a valid 9-character CUSIP is planned under the key
   `CUSIP:<cusip>` with `identifier_namespace = "CUSIP"`.
   - Its class comes from inputs the estate already holds (a bond's security-type field in the firm's own holdings or
     security master, the Schwab master, or the BD asset type). Name each source.
   - No guess. A CUSIP with no held evidence stays unresolved, by name.
   - The same conditional put on absence applies, with `classified_by = "scheduled"`.
   - Andrew's rule applies: a bd-securities value may seed this NEW row and never writes into an existing one.
2. **Reader census.** Enumerate every reader of `etf-classifications` that scans, queries by index, or iterates rows,
   across Lambdas, the gold and silver scripts, seeders, the one client and its copies, and Positioning. For each,
   record whether a `CUSIP:`-keyed row would surface in a ticker-keyed list or page, and if so the guard it needs
   (e.g. filter `identifier_namespace != CUSIP`). Do not edit those readers; name them.
3. **Tests** in `infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_cusip.py`:
   - a no-ticker CUSIP plans a `CUSIP:`-keyed row;
   - an existing row is refused;
   - an unevidenced CUSIP stays unresolved;
   - a ticker never gets the prefix.
4. **Census and half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CUSIP_CENSUS_20260930.json`
   as `{"table_rows_at_build", "reader_denominator", "readers": [{"path", "how", "surfaces_cusip", "guard"}],
   "would_write", "rows": [{"ticker": "CUSIP:...", "identifier_namespace": "CUSIP", "asset_class", "sub_asset_class",
   "source", "firm"}], "unresolved": [...], "overwrites": 0, "guessed": 0}`, run over the three IRPT firms' held
   bonds (49financial, inflection, cottonwood) through each firm's own tree. Write the half
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CUSIP_ROWS_20260930.md`
   for the CUSIP write. It names the readers that need a guard before the write, and the follow-on: the IRPT Holdings
   classifier looks up a bond node by `CUSIP:<cusip>`, an IRPT_BCKEND cell.

**Standing rulings (as in round 2):**
- Andrew-direct 2026-09-30 ~02:2xZ: "yes, bd-securities values can seed new rows. THey just don't overwrite existing rows."
  So a bd-securities value may seed a NEW row and never writes into an EXISTING one. A write to an existing row from a
  bd-securities value is outside his word: stop, and name it in the half for his decision.
- CTO C-WRITER ruling (analysis @151c890591, section 1): `classified_by` is `seed` / `scheduled` / `constituents` /
  `legacy`; `seed` always wins; `scheduled` and `constituents` write only where no row exists; a missing label reads as
  `legacy`.
- The live `etf-classifications` holds 2,309 rows (release step 2, ledger CLOSED @f13cddd058). Read and print its row
  count at build time as `table_rows_at_build` in your evidence file.

### ACCEPTANCE

<criterion id="SC2-e9-AC1" cell_refs="SC-e-9"><invocation>python -m pytest infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_cusip.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC2-e9-AC1` -- CUSIP rows on the prefixed key, absent-only, never guessed, a ticker never prefixed.

<criterion id="SC2-e9-AC2" cell_refs="SC-e-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CHECKS/r2_evidence.py cusip</invocation><expect>CUSIP-CENSUS</expect></criterion>
`SC2-e9-AC2` -- every scanning reader censused with its guard named, and the planned CUSIP rows well-keyed.

<criterion id="SC2-e9-AC3" cell_refs="SC-e-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CUSIP_ROWS_20260930.md</invocation><expect>HALF-READY</expect></criterion>
`SC2-e9-AC3` -- the CUSIP write's half.

<expected_criteria>SC2-e9-AC1,SC2-e9-AC2,SC2-e9-AC3</expected_criteria>

Dry-run at the base 2026-09-30 03:4xZ (@1e8d1e6dc0): SC2-e9-AC1 no tests ran; SC2-e9-AC2 NOT-MET (evidence absent);
SC2-e9-AC3 NOT-READY -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No table write (dry-run only), no upload, no deploy, no IAM apply, no outside-model call.
  The readers are named, not edited.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W4-S<k>`), and do not weaken the test to pass.

<paths>
infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py
infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_cusip.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CUSIP_CENSUS_20260930.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CUSIP_ROWS_20260930.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R3.md</decomp_doc> (round 3), cell `SC-e-9`.
<owned_cells>SC-e-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC2-e9-AC1, SC2-e9-AC2, SC2-e9-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~4/MDPF_SECCLASS.TO-SC-e9.cusip-keyed-rows.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC2-e9-AC1,SC2-e9-AC2,SC2-e9-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the planner change, the class sources named, the reader census (denominator, which surface CUSIP keys,
and the guards), the CUSIP rows per firm, the unresolved, the pytest line, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is changed (the scheduled writer's grant is SC-e-7's).
comp-adversary: RUN -- 1 ruling read (CTO 103140, prefixed key + reader census + conditional put), 1 census read (IB-mr-281: 449/826/565 unclassified, mostly CUSIP-only bonds); BLIND: the scanning readers and the bonds' held class sources are unmeasured at the cut (this cell's census measures them).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO RULING 103137 (hold) and 103140 (E9 key design, option a); IRPT_BCKEND IB-mr-281 census.
