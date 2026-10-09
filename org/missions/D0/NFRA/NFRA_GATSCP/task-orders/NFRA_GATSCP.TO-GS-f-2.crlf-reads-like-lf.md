# TO NFRA_GATSCP.TO-GS-f-2 -- round 3 GS-f-2: to-pipeline-gate reads a task order the same whether its line endings are CRLF or LF

<to_id>NFRA_GATSCP.TO-GS-f-2</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~9</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-f-2` (`decompositions/NFRA_GATSCP_DECOMP.round3.md`) | **outcome_ref:** FWD-6 |
**rows:** D1-S6 | **depends_on:** none

---

## WORKER FACE

### CONTEXT

`.tools/to-pipeline-gate.py` reads staged and HEAD blobs as bytes and decodes them without normalising line endings
(`_staged_blob` :2988; `_head_blob` :2979, which shadows a text-mode twin at :2156 that is therefore dead). Its element regexes end
`[ \t]*$` under `re.M` and cannot match before a `\r`: `PLACEHOLDERS_TAG_RE` (:183), `STATUS_ELEMENT_RE` (:1301),
`ROUND_ELEMENT_RE` (:2039), `WORKSTREAM_ELEMENT_RE` (:2046), `DIRECT_ACT_ELEMENT_RE` (:2064), and `PATHS_BLOCK_RE`'s close (:137).
So a MODIFIED order written with CRLF is refused by GATE (viii) for lacking a `<placeholders>` element it carries (row D1-S6,
DSGN_AMGTV1-D1-S1), and a CRLF order at HEAD reads as unrounded in `_head_rounds_census` (fails open). `check_file` opens in text
mode (CRLF already normalised there). The CTO ruled (R4): normalise on read, never edit the file.

### THE CELL

`GS-f-2`. To-pipeline-gate reads a task order the same whether its line endings are CRLF or LF.

**Build:**
Normalise `\r\n` (and a lone `\r`) to `\n` in every blob read of the gate (`_staged_blob`, `_head_blob`, and any other
bytes read of an order's text), and remove the dead text-mode `_head_blob` twin so one definition remains. Change no regex and no
limb's logic. Add one `--self-test` arm: a CRLF order and its LF twin grade the same.

### ACCEPTANCE

<criterion id="GF2-AC1" cell_refs="GS-f-2"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round3_prep/checks/r3_crlf.py"</invocation><expect>GS-F2-CRLF ok=True</expect></criterion>
`GF2-AC1` -- a CRLF-only modification of a pending order grades as its LF modification does (rc 0), and the same CRLF order with its `<placeholders>` line removed is still refused (GATE viii).

<expected_criteria>GF2-AC1</expected_criteria>

Read every check before you build. Each prints its arms and ONE last line, which the expectation is matched against. You do not
edit the checks. Report the last line of the tool's own self-test after your change where the tool has one.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~9/` and this
  order's file.
- No edit outside the grant. No push, no merge into a shared branch, no override at any commit.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W9-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the
  check or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does
  not block.

<paths>
.tools/to-pipeline-gate.py
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round3.md</decomp_doc> (round 3), cell `GS-f-2`.
<owned_cells>GS-f-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GF2-AC1. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~9/NFRA_GATSCP.TO-GS-f-2.crlf-reads-like-lf.proof_of_spec.json` (the order file's stem) with `to_id` `NFRA_GATSCP.TO-GS-f-2`,
validated with `python .tools/proof-of-spec-check.py <instance> GF2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** every criterion's last line whole; the self-test's last line; rows; commits.

### ISSUER CLOSE (2.0.0_SA_COO~N1, 2026-10-09T14:23Z)

The worker built and passed every criterion but could not flip: `proof-of-spec-check.py` exited rc=2 at its base
(e19881df2d) on the PROOF_OF_SPEC schema defect from e7c10e5b4b, fixed on box/dell1 at 6b65ca5a52. The issuer merged the
branch onto box/dell1, re-validated the instance (VALID, rc=0) and re-ran every criterion on the merged tree (drain checks 34
of 34 ok), and flips the order here.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE no IAM is read, granted or changed by this cell.
comp-adversary: RUN -- each criterion carries its negative or control arm (decomposition round 3, battery); BLIND: a census's conclusions are the CTO's.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round2.md @0ef2dc8325 (with ADDENDUM 1); CTO msg 2258 for D1-S5; decomposition round 3. Base dry-run: see the
issuance commit.
