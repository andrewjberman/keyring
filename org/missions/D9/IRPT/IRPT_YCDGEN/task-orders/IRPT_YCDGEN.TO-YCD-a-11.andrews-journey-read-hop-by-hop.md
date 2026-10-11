# TO-YCD-a-11 -- Andrew's own journey, read hop by hop at HEAD, and the slug's 26 rows read against it (read-only)

<to_id>IRPT_YCDGEN.TO-YCD-a-11</to_id>
<project>IRPT_YCDGEN</project>
<issued_to>0.9.0_WK_IRPT_YCDGEN~14</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `YCD-a-11` (`decompositions/IRPT_YCDGEN_DECOMP_R11.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none.

---

## WORKER FACE

### Read first

- `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md` lines 36-60 (FWD-1) and 244-250 (C-SCOPE, C-SWITCH), and its section on the thread's hops
  (search the file for "Select." to find the numbered hops).
- `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/remediations/REMEDIATION_v9.md`: the slug. It names 26 row ids.
- `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md`: each of those 26 rows (find a row by its `"id"` field; the file is long, read the row, not the file).
- The portal is a separate checkout. Your worktree's `portal/` folder is EMPTY. Read the portal's files at the absolute path
  `C:/dev/ajb_workspace/portal/` and write its refs as `portal/<path>`. You may not write there.

### THE CELL

Nobody has re-read the backlog. Read it, against one journey. You change NO product file and you run NO generation, no
HTTP call and no AWS call. Evidence is code lines, fixtures and tests you can run offline.

**The journey.** Andrew, signed in as himself (`andrew@opalinvest.com`, an Opal-internal principal), submits one real
Cottonwood portfolio for an Overview from the portal's Analysis tab and opens the Opal-made report. Trace it at HEAD, hop by
hop, from the page to the opened report: the page and its composer, the upload or the picked-client path, the request the
browser sends, the route and its authorizer, acceptance, the queue message, the resident worker's choice of producer
(`producer_for`, the allow list), the Opal producer, retention and publish, the status and sections reads, and the page that
shows the report. Name each hop, cite the lines that implement it, and say in one or two sentences what it does for THIS
principal and firm.

**The rows.** For each of the 26 ids the slug names, say whether what the row states is still true at HEAD, and whether
Andrew's own submission passes through it.

Write TWO files in your deliverables folder:

1. `JOURNEY_READ_YCD-a-11.json`, exactly this shape:
   ```
   {"head": "<git rev-parse HEAD of your worktree>",
    "portal_head": "<git -C C:/dev/ajb_workspace/portal rev-parse HEAD>",
    "hops": [{"n": 1, "name": "...", "refs": [{"path": "...", "line": 123}], "finding": "..."}],
    "rows": [{"id": "IRPT_YCDGEN-...", "state": "OPEN" | "MET", "on_path": "YES" | "NO" | "NOT_DETERMINED",
              "needs_live_read": true | false, "evidence": [{"path": "...", "line": 123}], "note": "..."}]}
   ```
   - `rows` holds each of the 26 ids exactly once, and no other id.
   - `state` MET means the code or a test you ran shows the row's statement is no longer true; give the evidence. A row the
     code cannot settle (it needs a served read, live data, or a deployed version) is OPEN with `needs_live_read` true, and
     its note says which read would settle it. Never write MET on a guess.
   - `on_path` NOT_DETERMINED is allowed only with a note that says what you could not read.
   - Every `path` is a file that exists: repo-relative, or `portal/...`. Every `line` is a line of that file.
   - At least 8 hops, each with at least one ref.
2. `JOURNEY_READ_YCD-a-11.md`: the same content for a reader. First a table of the hops in order. Then, per hop, the rows
   that sit ON it and are OPEN: these are what stands in Andrew's way. Then the remaining rows, one line each. Then a short
   list headed "What this read could not establish".

Three rows were read by the issuer before this order was cut and are expected MET; confirm or contradict each with your
own evidence: `IRPT_YCDGEN-W1-S8` (fix @fc018ca6c7; `test_opal_page_no_vendor_wording`), `IRPT_YCDGEN-W3-S12` and
`IRPT_YCDGEN-W3-S18` (`reports/tests/test_resident_installed.py` run alone).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="A11-AC1" cell_refs="YCD-a-11"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r11/r11_checks.py a11</invocation><expect>^R11-A11-OK</expect></criterion>

<criterion id="A11-AC2" cell_refs="YCD-a-11"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r11/r11_checks.py a11md</invocation><expect>^R11-A11MD-OK</expect></criterion>

<expected_criteria>A11-AC1,A11-AC2</expected_criteria>

- AC1 reads the json: the 26 ids by subtraction from the slug, the two value sets, a ref on every MET row, every ref a real
  file and line, at least 8 hops. At base it FAILs (no file).
- AC2 reads the md: it names every one of the 26 ids and carries the heading "What this read could not establish". At base
  it FAILs.

## BOUNDS

- **Grant.** The `<paths>` block only. READ-ONLY on every product file and on the portal. No deploy, no AWS call, no HTTP,
  no installs, no generation. You may run offline tests.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_YCDGEN-D2-W14-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of the channel
  file below. Each row's `surfaced_at` is the output of `date -u +%Y-%m-%dT%H:%M:%SZ` at the moment you write it; never type
  a time. Gate: `python .tools/surprise-row-gate.py --check <path>`. A row is for something NEW you find broken on the
  journey that no existing row states; do not re-file the 26.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_YCDGEN~14" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_YCDGEN~14@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_YCDGEN~14 <0.9.0_WK_IRPT_YCDGEN~14@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - ASCII only. Use the native Grep/Glob/Read tools; a recursive shell grep over the repo is denied by a hook.

<paths>
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~14/
org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-a-11.andrews-journey-read-hop-by-hop.md
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R11.md</decomp_doc> round 11, cell `YCD-a-11`.
<owned_cells>YCD-a-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: A11-AC1, A11-AC2. Instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~14/IRPT_YCDGEN.TO-YCD-a-11.andrews-journey-read-hop-by-hop.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_YCDGEN.TO-YCD-a-11`.
- Validate with `python .tools/proof-of-spec-check.py <instance> A11-AC1,A11-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~13/IRPT_YCDGEN.TO-YCD-a-10.page-sentence-per-cause-no-raw-string.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the hops in order, one line each;
- the rows that are OPEN and ON his path, in hop order, one line each: this is the list the issuer cuts next;
- the rows you could not settle and the read that would settle each;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read. No product file, no deploy, no data moves.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission, no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- routes are read, none is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the issuer read three of the slug's rows at HEAD before cutting and found them MET (W1-S8, W3-S12, W3-S18), which is why this is a read and not eight builds. Traps: MET written from a commit subject and not from the code; a row called off-path because the trace stopped early; the portal read from the empty worktree folder; a line number past the end of a file.
lane: read-only; writes only its own deliverables folder.
</preflight>

Source: CTO round-11 analysis @457305b604 section 4 item 1; REMEDIATION_v9 @1f3e35873b.
