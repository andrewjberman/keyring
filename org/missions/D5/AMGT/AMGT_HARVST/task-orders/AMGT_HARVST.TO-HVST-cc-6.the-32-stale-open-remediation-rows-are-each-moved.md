# AMGT_HARVST task order -- `HVST-cc-6` -- ROUND 88, workstream ROW-TRIAGE: EACH OF THE 32 STALE OPEN REMEDIATION ROWS IS MOVED (met, re-owned or dismissed) AND NONE IS LEFT UNMOVED (CTO round-87 analysis, section 1 and item 6)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cc-6.the-32-stale-open-remediation-rows-are-each-moved</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cc-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~153</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched, no installer change.
comp-iam: RUN at L5 -- RECORDS ONLY. You read files in this repository and write ONE JSON file and one note under your deliverables folder. NO S3 call, NO AWS call, NO publisher host, NO browser, NO runner or scheduled task, NO edit of any remediation, adjudication, investigation or task-order file.
comp-adversary: RUN at L5 -- the adversary is a row marked "met" on a read that does not meet its own close condition, a "dismissed" whose reason is a restatement of its title, a "re-owned" to a seat that is not live with no act and no condition, and a count of 32 reached by skipping the hard rows.
</preflight>

## 0. THE CELL

The project has 34 OPEN remediation rows (the issuer read `python .tools/comp-surprise.py --project AMGT_HARVST --json` at 2026-10-16 ~15:05Z, items whose `remediation.state` is `OPEN`). Two are this round's own work (`AMGT_HARVST-D1-S29` and `AMGT_HARVST-D1-W132-S4`, other cells). The other **32** are stale, owned by seats that are mostly gone (`2.0.0_SA_COO~H` 12, `~W1` 10, `~Y` 3, `1.0.0_SA_CTO~Z` 3, `1.0.0_SA_CTO~DELL1` 2, `0.0.0_AB_MSTR~Z` 1, `0.7.0_AE_CloudOps~ZW` 1). The CTO ruled: each of the 32 moves in this one cell and none is left unmoved, as exactly one of:
- **met:** its close condition is satisfied now, and you name the READ that shows it (a command whose output you ran, or a file and line at HEAD);
- **re-owned:** to a LIVE seat, with the reason, the concrete next act and the condition that un-parks it;
- **dismissed:** with the reason (the thing it guarded no longer exists, or a named later record supersedes it).

## 1. THE BUILD (LOCAL, records only)

Work in your worktree. Change only the files named in `<paths>`.
1. Read the issuer's population file `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round88/cc6_population.json` (the 32 ids, each with owner, round, fabric, the row's own `remedy` text, and the remediation document name). For each row read the full row in the remediation documents `org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/remediations/REMEDIATION_v<N>.md` (the round tag `v<N>` is in the population file; find the row by its id), the investigation row of the same id in `org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md` (read the fenced JSON with python and print ONE item, never the whole file), and any adjudication row naming it under `.../surprise-channel/adjudications/`. Read the order, ledger or commit the row names.
2. For each of the 32 write ONE row in `triage.json` (a JSON list) with the fields `id`, `verdict` (`met` | `re-owned` | `dismissed`), `reason` (at least 40 characters, specific to THIS row), and
   - for `met`: `read` (the command you ran and its key output line, or `path:line`);
   - for `re-owned`: `new_owner` (a LIVE seat serial; the live ones at the cut are `2.0.0_SA_COO~W1`, `1.0.0_SA_CTO~DELL1`, `0.0.0_AB_MSTR~DELL1`, `0.7.0_AE_CloudOps~SC1`; a row of another project's surface is re-owned to nobody in this project and is `dismissed` naming the brief or record that opens the owning surface) and `next_act` (at least 20 characters: what is done and the condition that un-parks it);
   - for `dismissed`: the `reason` alone, naming the superseding record, order or commit.
   A row whose close condition you cannot read from the repository is NOT `met`: it is `re-owned` with `next_act` saying what read is missing.
3. Write `triage.md` (a table of the 32 rows: id, verdict, one-line reason) for the CVO's next sweep, and `triage_counts.txt` with one line `met=<n> reowned=<n> dismissed=<n> total=32`.
4. Run the issuer's shape check from the root of YOUR worktree and put its output in `triage_check.out`: `python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round88/cc6_check.py org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/triage.json`. It checks the SHAPE only (every id present once, enums, reason lengths, `read` for met, `new_owner` and `next_act` for re-owned); the CVO reads whether each verdict is right.
5. Do not run anything against S3, AWS, a publisher or a box; do not edit any other file. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cc-6"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round88/cc6_check.py org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/triage.json</invocation><expect>(?m)^TRIAGE OK rows=32 population=32 </expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cc-6"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/triage_counts.txt</invocation><expect>(?m)^met=\d+ reowned=\d+ dismissed=\d+ total=32$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1):** AC1 FAIL as expected (`TRIAGE FAIL no triage file`); AC2 FAIL as expected (the file does not exist). The checker is shape-only: a fabricated file of 32 rows with 45-character reasons passes it, so YOUR rows must be real; the CVO grades them.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W153-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/AMGT_HARVST.TO-HVST-cc-6.the-32-stale-open-remediation-rows-are-each-moved.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cc-6.the-32-stale-open-remediation-rows-are-each-moved` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cc-6.the-32-stale-open-remediation-rows-are-each-moved.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-87 analysis (`ledger/ROUND_ANALYSIS.round87.md`, msg 6766), section 1 "The 32 stale OPEN owned rows" and enrichment item 6. The count: 34 OPEN remediation rows minus the two round-87 items (D1-S29, D1-W132-S4) = 32, read from `comp-surprise --json` at the cut; the population file is `deliverables/2.0.0_SA_COO_W1/round88/cc6_population.json`.
- **Not in this cell's lane:** the rows' CLOSE or state change in the remediation documents belongs to `3.0.0_SA_CVO` (lane `TREE_CVO`); this cell writes the triage RECORD, and the issuer sends it to the CVO for the next sweep. The cell does not edit any remediation, adjudication or investigation row.
- **Direct act:** ONE cell, LOCAL, records only, no code; no L2, L4-R or L8 to L10 for the cell itself (its close is the issuer's read of `triage.md` against five sampled rows).
- Slot ~153, worktree `C:/dev/wk-harvst-153`, branch `wk-AMGT_HARVST-153`. Widen the sparse set at provision with `org/tier1_exec/4.0.0_SA_CRO/scripts`, `org/missions/D5/AMGT/AMGT_HARVST/surprise-channel`, `org/missions/D5/AMGT/AMGT_HARVST/ledger`.
- **SENT:** with the round-88 issuance.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<direct_act>true</direct_act>
<status>pending</status>
<round>88</round>
<workstream>ROW-TRIAGE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
