# TO ADVI_COTBKF.TO-CB-g-2 -- round 7 CB-g-2: the FWD-8 read -- the applied crosswalk read back, one old account lined up with today's, the near-matches awaiting a person

<to_id>ADVI_COTBKF.TO-CB-g-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~22</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-g-2` (`decompositions/ADVI_COTBKF_DECOMP.round7.md`) |
**outcome_ref:** FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-g-2`, FWD-8: every Commonwealth account (the old firm's custody) is mapped to today's Cottonwood account where the evidence holds, and
a person can follow that mapping. The crosswalk is APPLIED at
`opal_naming.address("commonwealth", "cottonwood", "silver", "crosswalk", "date=2026-06-23")` (`crosswalk.parquet`, 1,533 rows, 439
MATCHED, applied 2026-10-07 09:38Z). The 21 near-matches (scored 0.65 to 0.8) are in
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~14/near_matches.csv`; they are NEVER linked by Opal -- they await a
person at Cottonwood.

You build `data/assets/scripts/analysis/commonwealth_fwd8_read.py`, read-only, which:
1. reads the APPLIED crosswalk from S3 (the builder address, never a local copy) and counts its MATCHED rows;
2. picks ONE MATCHED old account (deterministically: the first by `commonwealth_account` sort order) and writes a person-readable path
   for it: the old account number, its Commonwealth advisor id(s) and its last activity date from silver transactions; the matching
   rule and score; the new Cottonwood account and the positions that carried over (security and quantity from the old account's end
   positions and today's positions on 2026-06-23), each line citing the table it came from;
3. lists the 21 near-matches with status `AWAITING A PERSON` and their scores, from the deliverable above;
4. writes `FWD8_READ.md` to `--out` and prints as its LAST line exactly:
   `FWD8-READ matched_read=<n> lined_up=<1|0> near_matches_awaiting=<k> near_matches_linked=<j>`.
   Expected: `matched_read=439 lined_up=1 near_matches_awaiting=21 near_matches_linked=0`.

**Tests** `data/assets/scripts/analysis/tests/test_commonwealth_fwd8_read.py` (stubs, no AWS): a stub crosswalk of 3 rows (2 MATCHED)
reads `matched_read=2`; the lined-up account is the first MATCHED by sort order; a stub near-match list of 2 prints
`near_matches_awaiting=2 near_matches_linked=0`, and a near-match that also appears as MATCHED in the crosswalk makes
`near_matches_linked=1` (the control that the count can move).

### ACCEPTANCE

<criterion id="CB7g2-AC1" cell_refs="CB-g-2"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_fwd8_read.py</invocation><expect>passed</expect></criterion>
`CB7g2-AC1` -- the read on stubs, with the linked-count control.

<criterion id="CB7g2-AC2" cell_refs="CB-g-2"><invocation>python data/assets/scripts/analysis/commonwealth_fwd8_read.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~22</invocation><expect>FWD8-READ matched_read=439 lined_up=1 near_matches_awaiting=21 near_matches_linked=0</expect></criterion>
`CB7g2-AC2` -- the real applied crosswalk.

<expected_criteria>CB7g2-AC1,CB7g2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **Read-only.** No S3 write; no `--apply` of anything; no near-match is ever linked.
- **No typed bucket or key.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W22-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_fwd8_read.py
data/assets/scripts/analysis/tests/test_commonwealth_fwd8_read.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round7.md</decomp_doc> (round 7), cell `CB-g-2`.
<owned_cells>CB-g-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB7g2-AC1, CB7g2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~22/ADVI_COTBKF.TO-CB-g-2.fwd8-read.proof_of_spec.json`, validated with
`python .tools/proof-of-spec-check.py <instance> CB7g2-AC1,CB7g2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the FWD8-READ line, the lined-up account's path in three lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time read.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity on opal-data-assets (listed and read this session); denominator 1 bucket; BLIND: none needed.
comp-adversary: RUN -- the applied table, never a local copy; near-matches never linked, with a control that the linked count can move; BLIND: Cottonwood's own CRM view of the client.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-6 analysis @1c9c98e652, E2; ledger advi-cotbkf-r5-crosswalk-apply-20261007.
