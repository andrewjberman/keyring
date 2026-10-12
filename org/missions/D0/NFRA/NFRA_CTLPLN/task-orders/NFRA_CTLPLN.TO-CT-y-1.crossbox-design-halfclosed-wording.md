# TO NFRA_CTLPLN.TO-CT-y-1 -- round 9 CT-y-1: correct the HALF-CLOSED wording in the crossbox ack design (the CVO's note C-S31)

<to_id>NFRA_CTLPLN.TO-CT-y-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~72</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-y-1` (`decompositions/NFRA_CTLPLN_DECOMP.round9.md`) | **outcome_ref:** FWD-3, FWD-8 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

The CVO graded the crossbox ack design (`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~68/DESIGN_CROSSBOX_ACK_PER_BOX_FILE.md`) MET and noted one wording error, which the CTO asked to have corrected (ROUND_ANALYSIS.round8.md section 1). The design's states table has a row `HALF-CLOSED (status text only) | exactly one of A.closed, R.closed set | status_of :643 (today inside state ACKED)` (about line 64). The CVO's note: without an ack a half-closed call is inside OPEN today, not inside ACKED; the derivation already handles it because the base state still comes from the ack first (`derive_state` in `.tools/crossbox-call.py`, lines 194-197 at commit 2fbb74e87d: CLOSED-BOTH if closed.from_at and closed.to_at; else ACKED if ack.at; else OPEN).

### DO

1. In that one document, change ONLY the wording of the HALF-CLOSED row's last cell to say: `today inside whichever base state applies: ACKED when an ack exists, OPEN when it does not (the base state comes from the ack first)`. Keep the table's columns and every other row exactly as they are.
2. Add ONE sentence under section 1 or the states table (the nearest place the row is explained), no longer than 40 words, saying that the correction is the CVO's note C-S31 (ADJUDICATION_v10) and that the derivation is unchanged.
3. Do not change the counts line (`DESIGN-CROSSBOX-ACK fields=24 verbs=13 files_to_change=9 questions=5`) or any other section. Change no other file.

### RULES

Write surface is exactly the `<paths>`. No tool, no hook, no crossbox file, no aws, no terraform, no push. `.tools/safe-commit.sh` for the commit. No non-ASCII added. Do NOT commit the `portal` gitlink. CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to the surprise-channel file (id `NFRA_CTLPLN-W72-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTy1-AC1" cell_refs="CT-y-1"><invocation>grep -c "ACKED when an ack exists, OPEN when it does not" org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~68/DESIGN_CROSSBOX_ACK_PER_BOX_FILE.md</invocation><expect>1</expect></criterion>
`CTy1-AC1` -- the corrected wording is in the document once.

<criterion id="CTy1-AC2" cell_refs="CT-y-1"><invocation>grep -c "DESIGN-CROSSBOX-ACK fields=24 verbs=13 files_to_change=9 questions=5" org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~68/DESIGN_CROSSBOX_ACK_PER_BOX_FILE.md</invocation><expect>1</expect></criterion>
`CTy1-AC2` -- the counts line is untouched (a control).
</proof_of_spec>

<expected_criteria>CTy1-AC1,CTy1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~72/NFRA_CTLPLN.TO-CT-y-1.crossbox-design-halfclosed-wording.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTy1-AC1,CTy1-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round9.md</decomp_doc>
<owned_cells>CT-y-1</owned_cells>
</decomp_ref>

<paths>
org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~68/DESIGN_CROSSBOX_ACK_PER_BOX_FILE.md
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- an edit that changes the counts line or another section (CTy1-AC2 holds the counts line; the diff stat is reported); a wording that restates the derivation wrongly (the order quotes derive_state's three-way rule); BLIND: the CTO's other premises about the crossbox design (rows W68-S1..S6).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round8.md section 1 (the C-S31 note); ADJUDICATION_v10 C-S31.
