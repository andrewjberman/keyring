# TO NFRA_GATSCP.TO-GS-f-3 -- round 3 GS-f-3: round-close-check reads an order's terminal state and judgment flag as the order declares them

<to_id>NFRA_GATSCP.TO-GS-f-3</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~10</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-f-3` (`decompositions/NFRA_GATSCP_DECOMP.round3.md`) | **outcome_ref:** FWD-6 |
**rows:** D1-S9 | **depends_on:** none

---

## WORKER FACE

### CONTEXT

`.tools/round-close-check.py` reads each order's last `<status>` with `last_status` (:270-277,
`re.finditer(r"^<status>(.*?)</status>", text, re.M)`) and keeps the WHOLE stripped text only if it is in `STATUS_WORDS`; it then
counts `done = [o for o in orders if o["status"] == "complete"]` (:435) and open orders against a six-word tuple (:436). Judgment
criteria are read from the order (`CRIT_TAG` :60, `ATTR` :61, `judgment="true"` at :292) but counted only over `done` (:454-458).
LGIC_BLANKFIX's TO-BF-aa-1 reads `<status>complete -- landed by 0.7.0_AE_CloudOps~DELL1. ...</status>`, so it reads as no status, is
not done, and its `judgment="true"` criterion is never counted: round 12 reads complete=0, judgment=0. The terminal word sets
disagree across tools (seat-list.py:72, to-pipeline-gate.py:2949 and :1302, surprise-row-gate.py:171). The CTO ruled (R3): read
the order, not a spelling; re-run on LGIC round 13 and DSGN round 65.

### THE CELL

`GS-f-3`. Round-close-check reads an order's terminal state and judgment flag as the order declares them.

**Build:**
Read the status by its LEADING word (the first token of the `<status>` text, lowercased, trailing punctuation
stripped). Terminal-complete words: `complete`, `completed`, `done`, `closed`. Other terminal (not complete, not open):
`superseded`, `cancelled`, `canceled`, `withdrawn`, `retired`, `parked`. Count `done` and `open_` from those sets; leave the
judgment read as it is (it now sees the orders it was missing). `--staged` (round 2) keeps working. `--selftest` stays green; add
one arm for a `complete -- <note>` status.

### ACCEPTANCE

<criterion id="GF3-AC1" cell_refs="GS-f-3"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round3_prep/checks/r3_close_terminal.py"</invocation><expect>GS-F3-CLOSE ok=True</expect></criterion>
`GF3-AC1` -- LGIC_BLANKFIX round 12 reads complete=1 and judgment=1; round 13 (orders=3 judgment=1) and DSGN_AMGTV1 round 65 (judgment>=1) are unchanged controls.

<criterion id="GF3-AC2" cell_refs="GS-f-3"><invocation>python .tools/round-close-check.py --selftest</invocation><expect>ok=True</expect></criterion>
`GF3-AC2` -- the tool's own selftest stays green with the new arm.

<expected_criteria>GF3-AC1,GF3-AC2</expected_criteria>

Read every check before you build. Each prints its arms and ONE last line, which the expectation is matched against. You do not
edit the checks. Report the last line of the tool's own self-test after your change where the tool has one.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~10/` and this
  order's file.
- No edit outside the grant. No push, no merge into a shared branch, no override at any commit.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W10-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the
  check or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does
  not block.

<paths>
.tools/round-close-check.py
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round3.md</decomp_doc> (round 3), cell `GS-f-3`.
<owned_cells>GS-f-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GF3-AC1, GF3-AC2. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~10/NFRA_GATSCP.TO-GS-f-3.close-check-reads-the-order.proof_of_spec.json` (the order file's stem) with `to_id` `NFRA_GATSCP.TO-GS-f-3`,
validated with `python .tools/proof-of-spec-check.py <instance> GF3-AC1,GF3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** every criterion's last line whole; the self-test's last line; rows; commits.

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
