# AMGT_CORPUS task order -- `CRPS-at-1` -- ROUND 44: each name's own team sheet rows are read and served (FWD-12, lib half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-at-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only S3 GETs of stored workbooks under the existing harvest-bucket read the corpus already uses; no new grant.
comp-adversary: RUN by the issuer at the cut on HEAD 732412e179 -- at1_check.py: team_sheet reader absent, served 95, partitions with a workbook 53, build 0/2 control 0/1. Blind spot: the master template is not in the store (42 names read master_absent until it is ingested).
EGRESS CLASS, declared: NONE beyond Opal's own S3 reads. No Bloomberg, no vendor call, no write to S3.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 44. Your worktree is the absolute path the issuer gives you; work and commit only there.

## 1. THE CELL -- `CRPS-at-1`

Outcome FWD-12 (PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` lines 433-456, read them): the Model tab's rows must be
each served name's OWN research-team sheet, in its order and labels. Today the portal shows one hard-coded 62-row list for every name.
This cell builds the lib half: read the team sheet's rows and serve them; a parallel cell (`CRPS-at-2`) renders them.

The workbooks are stored in S3 bronze (`lib/research/corpus/extract.py`: `store.table_prefix(extract.SOURCE, "bronze",
extract.BRONZE_REQUEST)`, keys `security_key=<KEY>/<report_id>/<file name>`; list with `extract._list_keys`, read bytes with
`client.get_object(Bucket=store.HARVEST_BUCKET, Key=...)`). The served names are `continuation._resolved_security_keys(client)`.

**Build:**
1. New module `lib/research/corpus/team_sheet.py` with:
   - `rows_for(security_key, client=None)` -> `{"class", "workbook_key", "sheet", "rows", "model_rows_beside", "reason"}`;
   - `census(client=None)` -> `{security_key: rows_for(...)}` over the served names;
   - a `--census` CLI (`python -m lib.research.corpus.team_sheet --census`) printing, per name, the class, workbook and sheet, then
     `team_sheet classes own_new <a> own_model <b> master <c> master_absent <d> sum <s> served <n>`.
   The rules (they are round 40's measured instruments; the issuer's check re-derives them independently, so follow them exactly):
   - over rows 1-400 and columns 1-60 of a sheet, a row's LABEL is the first non-empty string in its first 4 cells, and the row
     counts when it also holds two or more numbers (bool is not a number); a sheet CARRIES FIGURES when >= 10 rows count;
   - a workbook (`.xlsx`/`.xlsm`) is figure-carrying when `Model NEW VERSION` or `Model` carries figures; the team sheet is
     `Model NEW VERSION` when it carries figures, else `Model`; `rows` = that sheet's counted labels, in sheet order, as written
     (whitespace collapsed); when BOTH sheets carry figures, `model_rows_beside` = the `Model` sheet's labels, else None;
   - of two or more figure-carrying workbooks in one name's partition, read the one with the newest stored modified date (the
     object metadata `source-mtime` or `mtime` when present, else its S3 LastModified); class `own_new` or `own_model` by sheet;
   - a name with no figure-carrying workbook: the master `FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx` by the same rule,
     found by that exact file name anywhere in bronze; when the store holds none, class `master_absent`, rows `[]`, and `reason` a
     sentence a PM reads: "The research team's model template is not in the stored library, so this name's rows cannot be read
     from it." Never invent rows.
2. `lib/research/api/scoped_amgt.py`, `read_thesis_bundle` (about line 3643): add `model["team_sheet"] = team_sheet.rows_for(key)`
   (the exact field shape above). Change nothing else in that function's output.
3. Tests `lib/research/corpus/tests/test_team_sheet_round44.py`: a fixture workbook built in memory with openpyxl covering the
   label/number rule, the sheet choice, `model_rows_beside`, the newest-of-two pick and `master_absent`; and that
   `read_thesis_bundle` carries `model.team_sheet` (stub the store as the existing scoped_amgt tests do).

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's checks. No portal file.
2. NO S3 write, NO deploy, NO push, NO Bloomberg or vendor call. S3 reads for your own testing are allowed.
3. Write code with the Edit/Write tools, never a shell heredoc, sed or `python -c` rewrite. ASCII only.
4. Rows are `AMGT_CORPUS-D1-W1-S<k>` (next free k across every file under `surprise-channel/`), `disarm_owner 2.0.0_SA_COO~C1`.
5. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.
   Your proof instance's `to_id` is this order's FULL id: `AMGT_CORPUS.TO-CRPS-at-1.team-sheet-rows-served`.

## 3. SURFACES

<paths>
lib/research/corpus/team_sheet.py
lib/research/corpus/tests/test_team_sheet_round44.py
lib/research/api/scoped_amgt.py
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_method_bump.py
lib/research/corpus/tests/test_dossier_case_body.py
lib/research/corpus/tests/test_dossier_case_unit.py
lib/research/corpus/tests/test_dossier_case_positional.py
lib/research/corpus/tests/test_dossier_heading_only_round40.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-at-1.team-sheet-rows-served.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-at-1.team-sheet-rows-served.md
</paths>

Read-only: the whole repository, in particular `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round44/at1_check.py`.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-at-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round44/at1_check.py"</invocation><expect>(?m)^at1 build 2/2 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-at-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest -q -p no:cacheprovider lib/research/corpus/tests/test_team_sheet_round44.py 2&gt;&amp;1 | tail -1 | sed 's/\x1b\[[0-9;]*m//g'</invocation><expect>(?m)^\d+ passed in [\d.]+s$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-at-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; grep -c "team_sheet import\|import team_sheet\|team_sheet\.rows_for" lib/research/api/scoped_amgt.py</invocation><expect>(?m)^0$</expect></criterion>
</proof_of_spec>

- AC3 (AMENDMENT 1): the serving API never calls the team-sheet reader; it reads the field from the served dossier.
- AC1: the classes sum to the served names, every both-sheet workbook carries `model_rows_beside`, and your rows equal the check's
  independent derivation on every name with an own workbook; the control names read the classes the check derives.
- AC2: your tests pass.

## 5. WHEN YOU ARE DONE

1. Run `python -m lib.research.corpus.team_sheet --census` and put its class line in your report.
2. Write the instance at the proof path (genre BUILD), with its mutant control; run `python .tools/proof-of-spec-check.py <instance>
   AC1,AC2 --governing-order <this order>` AFTER your final commit; rc 0.
3. Only if AC1 and AC2 pass, append a new status tag reading complete at the END of this file, in the SAME commit as your instance.
4. Report ONCE: the change, AC1's lines (classes, rows match, build/control), AC2's line, the census class line, your commit hashes, any row.

## 6. AMENDMENT 1 (2026-10-09 ~21:2xZ, the issuer's own, on the CTO's ruling msg 3196)

The serving API's role holds no read on the bronze workbooks, and the CTO ruled it gets none: the API reads only served tiers. So
`team_sheet` is computed ONCE, at dossier build time, and stored in the gold dossier, which the API already reads. Your reader stays
(`team_sheet.rows_for` / `census` and its rules are unchanged, and AC1 still grades them); only WHERE it runs changes.

**Do, and only this:** take the amendment by merging `box/dell1` into your branch (`git merge --no-edit box/dell1`), then:
1. `lib/research/corpus/dossier.py` `build` (about line 1461): add `fields["team_sheet"] = team_sheet.rows_for(security_key,
   client=client)` (the same shape; a raised read stores class None, rows [], and a reason in words). Bump `METHOD_VERSION` from
   `amgt-corpus-dossier/9` to `amgt-corpus-dossier/10` and update ONLY that literal in the five tests now in `<paths>` that pin it.
2. `lib/research/api/scoped_amgt.py` `read_thesis_bundle` (about line 3691): `model["team_sheet"]` is read from the served dossier
   document the function already reads (`dossier_read`, about line 3686), field `team_sheet`, as stored. When the served dossier has
   no such field (an older method), serve `{"class": None, "workbook_key": None, "sheet": None, "rows": [], "model_rows_beside":
   None, "reason": "This name's served dossier was written before the team sheet was added."}`. Remove `_team_sheet_rows` and every
   import or call of the team-sheet module from that file (AC3 greps for them).
3. Tests: `build` stores the field (stub the reader); the bundle serves the stored field and the older-dossier reason.

Re-run AC1, AC2 and AC3, the five method-pinning tests, update your instance (AC3 added), run the checker after your final commit,
and append the status tag reading complete at the END of this file only if AC1-AC3 pass. Report once.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** close read @987284b18e item 1. Base HEAD 732412e179: at1 build 0/2 control 0/1. Served only after AMGT_RESAPP redeploys the scoped API (read_thesis_bundle is its served product) -- an issuer ask at the drain, as /9's leg p. Master template absent from the store: CTO asked at the cut.
<risk>LOCAL</risk>
<status>pending</status>
<round>44</round>
<slot>~1</slot>
<fabric>dell1</fabric>
<status>complete</status>
<!-- REOPENED 2026-10-09 ~21:3xZ by the issuer 2.0.0_SA_COO~C1 for AMENDMENT 1 (row D1-W1-S6: the order was terminal, so the gate refused the amendment's paths). -->
<status>pending</status>

## 7. AMENDMENT 2 (2026-10-09 ~21:5xZ, the issuer's own, on the CTO's ruling msg 3213)

The served /9 lost the team cases on six PDF names (row D1-S2: the /8 and /9 writes ran with fitz stubbed). The CTO ruled a fix-forward
/10 now, DECOUPLED from team_sheet, which moves to /11. `CRPS-at-8` made `METHOD_VERSION` `amgt-corpus-dossier/10` on box/dell1
(@548315f918, literal only) and the issuer is writing /10. Your AMENDMENT 1 work (team_sheet in the dossier, served from it) is right;
only its version number changes.

**Do, and only this:** merge `box/dell1` into your branch (`git merge --no-edit box/dell1`). The METHOD literal will conflict in
`dossier.py` and the five pinning tests: resolve each to `amgt-corpus-dossier/11`, keeping box/dell1's `/10` comment line and adding
`# /11 (CRPS-at-1 AMENDMENT 2): team_sheet stored in the dossier.` above the assignment. Keep everything else of yours. Re-run AC1-AC3 and
the five pinning tests, update your instance, run the checker after your final commit, and append a status tag reading complete at the
END of this file only if AC1-AC3 pass. Report once.

<status>pending</status>
