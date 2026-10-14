# TO COMM_ASSIST.TO-CA-i-11 -- round 17 CA-i-11: the muse reader's draft rows carry the draft's seq (the other half of closing row COMM_ASSIST-C-S5)

<to_id>COMM_ASSIST.TO-CA-i-11</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~17</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>SEQROW</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-11` (`decompositions/COMM_ASSIST_DECOMP.round17.md`, AMENDMENT 4) | **outcome_ref:** FWD-7 |
**depends_on:** CA-i-1 (merged @67043cf9d3)

---

## WORKER FACE

### THE CELL

The assistant is being changed (cell CA-i-10) so that a signed muse answer must name the draft it was shown by its `seq`, a number that never repeats on a chat. Muse reads each waiting draft from a row in
`drafts.json`, written by `data/transcripts/scripts/muse_reader/refresh.py` (`_draft_row`), so that row must carry the `seq`. You add that one field and one README sentence. Nothing else.

### BUILD

1. `_draft_row`: add `"seq": pending.get("seq")` to the row (a whole number, or `None` when the draft carries none; the key is ALWAYS present, so absent is never mistaken for zero). No other field changes.
2. The README text `refresh.py` writes gains one short sentence in the paragraph about drafts: a draft row's `seq` (null when it has none) and its `version` are what a signed answer must carry for that draft. Keep every existing sentence.
3. Edit nothing else. No non-ASCII. No AWS call beyond the reads the readers already make.

### RULES

- Edit nothing but the files in `<paths>`. Code change; not deployed here (the dell2 checkout picks it up through the box pass).
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi11-AC1" cell_refs="CA-i-11"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i11_seq.py"</invocation><expect>I11-SEQ ok=True</expect></criterion>
`CAi11-AC1` -- the issuer's check (read it; do not edit it): a draft with seq 7 yields a row with seq 7; a draft with no seq yields a row with the key present and null; the other fields are unchanged. It prints ok=False at the base.

<criterion id="CAi11-AC2" cell_refs="CA-i-11"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i1_live.py"</invocation><expect>I1-LIVE ok=True</expect></criterion>
`CAi11-AC2` -- the bound, a control that PASSES at the base and must still pass: the real refresh against the real sources (ages, object_id, answers/ untouched, README names answers/).
</proof_of_spec>

<expected_criteria>CAi11-AC1,CAi11-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~17/COMM_ASSIST.TO-CA-i-11.reader-rows-carry-the-drafts-seq.proof_of_spec.json`, validate it by running the WORKTREE'S OWN
`.tools/proof-of-spec-check.py` from inside the worktree: `python .tools/proof-of-spec-check.py <instance> CAi11-AC1,CAi11-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID. Your final report names the exact lines
you changed. Your surprise rows are `COMM_ASSIST-W17-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-11</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/muse_reader/refresh.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-11.reader-rows-carry-the-drafts-seq.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~17/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; the readers' existing read calls are unchanged.
comp-adversary: RUN -- a seq shown as 0 or omitted when a draft has none (refused: AC1 requires the key with null); another field disturbed (refused: AC1 compares object_id and tag; AC2 runs the whole refresh). BLIND: how muse puts the seq into the payload it signs is the signing instructions (a later card), not this cell.
lane: the <paths> block IS the grant (worker RULING 1). DIRECT-ACT: one line, LOCAL; no L8-L10; its close is the issuer's one real run.
</preflight>

Base: CAi11-AC1 base: FAIL as expected (seq absent); CAi11-AC2 base: PASS as expected (control). AC1 not exercised green before the build (a single dict key).
Source: CVO half "Carried" (row COMM_ASSIST-C-S5); CA-i-10; tenant.py `assign_seq`.
