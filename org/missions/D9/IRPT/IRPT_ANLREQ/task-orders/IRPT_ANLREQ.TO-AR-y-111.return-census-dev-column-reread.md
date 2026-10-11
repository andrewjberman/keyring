# TO IRPT_ANLREQ.TO-AR-y-111 -- the return census's DEV column re-read at the current DEV head, and the ticket page's reader named on each trunk

<to_id>IRPT_ANLREQ.TO-AR-y-111</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (reads of git refs in two repositories; no live call)
**Decomp cell:** `AR-y-111` (`decompositions/IRPT_ANLREQ_DECOMP_R11_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W52-S<k>`. The worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either.

### THE CELL (`AR-y-111`, inlined)

*The return census's DEV column, re-read at the DEV head of this hour; and the Ticket Center's report reader named on each trunk.*

Why. The census for the next release of `irpt-status`,
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r10/RETURN_CENSUS_IRPT_STATUS.json`, names for each member
that changes a served answer (`served_effect` = `CHANGES_SERVED_ANSWER`, five rows) the portal code that reads that answer on
`origin/PROD` and on `origin/DEV`. Its DEV column was read at DEV `9ca634c6`. Since then DEV moved (to `3ebc35ebf2` at this cut) and
gained a NEW reader: the Ticket Center's report read now SENDS a `ticket_id` (`src/pages/TicketCenter/analysisRequest.ts`,
`readTicketReport`, used by `openReport` and by `openPackageFile` in `AnalysisRequestParts.tsx`). The reviewer's limit: a DEV column
read before that landing does not describe DEV.

Read the portal repository at `C:/dev/wk-irpt-anlreq-51/portal` by REFS ONLY: first `git -C <portal> fetch origin DEV PROD`, then
`git -C <portal> show origin/DEV:<path>`, `... show origin/PROD:<path>`, `git -C <portal> grep -n <term> origin/DEV -- src`. Another
worker edits that worktree's files: never read its working files, never check anything out.

1. Record `dev_ref` and `prod_ref` = the full hashes of `origin/DEV` and `origin/PROD` after your fetch.
2. For EACH of the five served members of the census: re-read its DEV reader at `dev_ref`. Write `portal_reader_dev`:
   `{"file_function": "<file>:<function>", "admits_new_shape": true|false, "deciding_line": "<file:line and the line's text>"}`, or
   `{"found": false, "searched": "<terms and paths>"}`; and `changed_since_first_read`: true if the reader's file differs between
   `9ca634c6ea089796c127a9a1399cfa279323a154` and `dev_ref` (`git -C <portal> diff --stat 9ca634c6 <dev_ref> -- <file>`), else false.
   Search again at `dev_ref` for any reader of each route the first census did not name; say what you searched.
3. `ticket_page_reader`: `{"file_function": "...", "sends_ticket_id": true, "on_dev": true|false, "on_prod": true|false,
   "deciding_lines": ["<file:line text>", ...], "fallback": "<what it does on which served reason, with the line>",
   "after_reads": ["<words>", "<words>"]}`. `on_prod` is read at `prod_ref` (does PROD's Ticket Center send a ticket id on the report
   read at all?). `after_reads` are two reads a signed-in Opal person can make on the Ticket Center after the release, in words
   with no real id, name or figure: (i) Open on a ticket whose recorded report belongs to that ticket: what the page shows;
   (ii) Open on a ticket whose recorded report was filed under ANOTHER ticket: what the page shows (name the sentence constant the
   page uses). For each say on which trunk the read can be made today.
4. Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r11/RETURN_CENSUS_DEV_REREAD.json`:
   `{"read_at": "<UTC>", "dev_ref": "...", "prod_ref": "...", "first_read_dev_ref": "9ca634c6ea089796c127a9a1399cfa279323a154",
   "served_members": [{"packaged_as": "...", "portal_reader_dev": {...}, "changed_since_first_read": true|false}, ...],
   "ticket_page_reader": {...}, "prod_must_carry_first_changed": true|false, "prod_must_carry_first_note": "<one sentence>"}`.
   `prod_must_carry_first_changed` answers: does anything you read ADD a portal change that must be on PROD before the release?
   Do NOT edit the round-10 census. Commit the new file.

### ACCEPTANCE

<criterion id="AR111-y-AC1" cell_refs="AR-y-111"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r11/ar11_checks.py y111-dev --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y111-DEV-OK</expect></criterion>
`AR111-y-AC1`: the re-read names a DEV head other than the first read's, one complete row for each served member of the census, and
the ticket page's reader with its trunks and two after-reads. It grades the record's form, not whether a reading is right.

<expected_criteria>AR111-y-AC1</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's
  file (status flip only).
- READ only: everything else. No push, no deploy, no upload, no apply. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R11_Y.md</decomp_doc>
<owned_cells>AR-y-111</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR111-y-AC1. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-111.return-census-dev-column-reread.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-111`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR111-y-AC1`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 census of 16 rows (5 served, counted by the check) and 2 ref heads (DEV 3ebc35ebf2, PROD 37aa1247ee at this cut); NOT seen: the DEV readers at this head (the worker reads them). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change
comp-adversary: RUN -- by reading 1 adjudication limit against 5 rows; the lens: a column copied forward without a re-read. The check refuses the first read's head and requires changed_since_first_read per row. NOT seen: readers outside the portal repository.
lane: the worker's deliverables; read-only on both repositories.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-11 analysis @6385a12ed2, item 1. `AR111-y-AC1` base: FAIL as expected (no re-read file).
- The issuer writes the after-reads into the apply order from this record.
- Seating: slot ~52 is reused; its earlier order is terminal.
