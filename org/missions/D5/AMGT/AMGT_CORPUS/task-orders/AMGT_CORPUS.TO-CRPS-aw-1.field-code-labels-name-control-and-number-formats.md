# AMGT_CORPUS task order -- `CRPS-aw-1` -- ROUND 47: the team-sheet reader labels field-code rows in words (cited), classes override and fund-year rows CONTROL by name, and carries each team cell's own number format (FWD-20, lib half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-aw-1, CRPS-aw-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the reader's S3 GETs of stored workbooks are the existing harvest-bucket reads; no new grant, and this order writes nothing.
comp-adversary: RUN by the issuer at the cut on HEAD cbd78d8653 -- aw1_check.py: `aw1 build 0/4 control 2/2` at the base, `build 4/4 control 2/2` on a reference implementation (not shipped). Blind spot: the check is a miniature workbook; the 32 real own workbooks are the issuer's /13 write leg.
EGRESS CLASS, declared: NONE beyond Opal's own S3 reads. No Bloomberg, no vendor call, no write to S3.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 47. Your worktree is the absolute path the issuer gives you; work and commit only there.

## 1. THE CELL -- `CRPS-aw-1`

Outcome FWD-20 (PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` lines 593-606, read them). The Model tab shows each name's own
research-team sheet rows. Measured on the live served payloads (32 own workbooks): 1348 of the 3381 FIGURE rows carry a raw field code as their
label (`BEST_EBIT`, `FF_EBITDA_OPER`), and 72% of the team's float cells print past 4 decimals. The ruling: a code row is labelled in words from
its vendor's own description, with the claim held; override and fund-year rows are CONTROL by name; each team cell's Excel number format is
captured so the page can print by it. This cell builds the lib half; a parallel cell (`CRPS-aw-2`) renders it.

`lib/research/corpus/team_sheet.py` already reads each name's workbook (bronze, S3 GETs only, `openpyxl` `read_only=True, data_only=True`) and
returns `rows_for(security_key, client=None)` with `class`, `workbook_key`, `sheet`, `rows`, `model_rows_beside`, `reason` and the round-46 class
keys (`row_classes`, `row_numbers`, `row_values`, `periods`, `row_counts`). `dossier.build` calls it ONCE and stores the answer in the gold
dossier's `team_sheet` field; the serving API returns that stored field as stored.

**Build, in `lib/research/corpus/team_sheet.py`:**

1. Keep every existing function and behavior: `sheet_labels`, `sheet_reading`'s existing keys, `rows_for`, `census`, the counting rule, the
   round-46 class rule and its values (`row_values` stays verbatim), `model_rows_beside`, the newest-workbook rule, `master_absent`.
2. **CONTROL by name.** A counted row whose label matches `^[A-Z][A-Z0-9]*(_[A-Z0-9]+)*_OVERRIDE$`, or equals `EQY_FUND_YEAR`, is class
   CONTROL wherever it sits (above or below the period header) and whatever its cells hold; its `row_values` entry is None. Such a row is never
   the period header: the header search skips it (a fund-year row of increasing years above the real header must not become the header).
   **AMENDMENT 1 (issuer, 2026-10-11 ~17:1xZ; the period header itself).** Round 46's header test required ALL of a row's numeric cells to be
   integer years; measured on the live store it took the `EQY_FUND_YEAR` row as the header on CLX, ML FP and BABA (their true header
   `Financial Summary` carries a side-panel number far to the right) and classed ~190 model rows above it HEADING. Replace the test, in the
   header search and in the later-year-row rule alike: a counted row is a YEAR ROW when its integer-year cells (integers 1990..2100) number at
   least 3, are strictly increasing in column order, and make up at least 80% of the row's numeric cells; a non-year number elsewhere on the
   row (a side panel) does not disqualify it. The period columns are the YEAR cells' columns (a stray number is not a period). A named
   CONTROL row is never the header and, being a year row, stays CONTROL by name. Every other class rule is unchanged. The refreshed check is in
   `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw1_check.py` (the header row now carries a stray number in
   column Y): your current code reads `aw1 build 1/4 control 2/2` on it. Add a case to your round-47 test for it.
3. **Labels.** `reading` gains `row_labels`, aligned with `rows`: None unless the label matches `^[A-Z][A-Z0-9]*(_[A-Z0-9]+)+$`; for such a
   label a dict `{"text", "source", "claim", "cite", "code", "why"}`:
   - the code is a `mnemonic` of `integrations/bloomberg/research/field_map.json` (key `fields`, a list): `text` = that field's
     `basis["definition"]` AS STORED (never edited), `source` "bloomberg", `claim` "held", `cite` "integrations/bloomberg/research/field_map.json",
     `code`, `why` None;
   - else the code starts with `FF_`, `FFI_`, `FG_`, `FE_` or `P_` (a FactSet data item): when `lib/research/corpus/factset_descriptions.json`
     (`{"entries": {"<code>": {"text": "...", "cite": "..."}}}`) holds the code, `text` = its text AS STORED, `source` "factset", `claim`
     "held", `cite` = its cite; otherwise `text` "FactSet line", `source` "factset", `claim` "absent", `cite` None, `why` = "FactSet data item;
     no published FactSet description was found; the meaning is not inferred from the name.";
   - else (any other identifier): `text` "Bloomberg line", `source` "bloomberg", `claim` "absent", `cite` None, `why` = "Bloomberg field name;
     the estate's field metadata does not describe it.".
   Read both JSON files from the repository root derived from the module's own path (`Path(__file__).resolve()`; never a typed drive path),
   once per process; a missing or unparsable field map RAISES (an absent dictionary must never read as "no label"). Create
   `lib/research/corpus/factset_descriptions.json` as `{"entries": {}}` (ASCII, no other keys).
4. **Formats.** `reading` gains `row_formats`, aligned with `rows`: None unless the row is FIGURE; for a FIGURE row the list of that row's cells'
   `number_format` strings in the period columns, in period order, aligned with `row_values[i]`: the saved string (`'General'` where the
   workbook says General), None where the sheet carries no cell at all. To read formats iterate cells (`values_only=False`); the counting rule,
   labels and values must come out byte-identical to today's.
5. `rows_for` and `census` answers gain, aligned with `rows`, the keys `row_labels` and `row_formats`; a `master_absent` answer carries both
   empty (`[]`). Every existing key is untouched. The `--census` CLI keeps its lines and adds, after the class line,
   `team_sheet labels bloomberg_held <n> factset_held <n> factset_line <n> bloomberg_line <n> none <n> sum <s> rows <r>` over the served names
   (`s` equals `r`; `none` counts rows whose `row_labels` entry is None).

**AMENDMENT 2 (issuer, 2026-10-11 ~17:3xZ; cell `CRPS-aw-9` folded into this order; build it AFTER AMENDMENT 1 and commit it separately).**
The CTO ruled (round-46 ADDENDA 2 and 3): the template is its own bronze table `research_template` under the harvest root, partition
`template=<SharePoint item id>`, addressed as the builder prints today; the master-arm reader reads that table; and the team's own labels of the
code rows are MEASURED from the workbook, cited, claim measured, count printed. Build:

A. New `lib/research/corpus/template.py` (standard library plus `lib.research.harvest.store` only): `TABLE = "research_template"`;
   `put_template(body, item_id, client=None, source_mtime=None, file_name=None)` stores the bytes with `store.bronze_put("amgt", TABLE,
   "template=<item_id>", store.form_b_object(<first 16 hex of the sha256>, <file_name, default team_sheet.MASTER_NAME>), body,
   content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", metadata={...}, client=client)` and returns its result dict;
   the metadata carries `source-item-id` and, when given, `source-mtime` (read `lib/research/harvest/store.py` `_validate_bronze_metadata` first;
   mirror `lib/research/corpus/ingest.py`'s call). Write-once is `bronze_put`'s own (a second put of the same bytes: `existed` True,
   `put_performed` False). CLI `main(argv=None)`, `python -m lib.research.corpus.template`:
   - `--labels <xlsx path>` prints exactly one line
     `template_labels measured <n> metric_name <m> pass_through <p> two_label_left <t> fallback <f> bloomberg_held <b> codes <c>` (rc 0) over the
     identifier-form code rows of the file's team sheet: `m` rows labelled by a column-B metric name, `p` by a single-row pass-through,
     `n = m + p`; `t` FactSet-prefix codes that two or more distinct labels reference; `f` codes with no measured label that are not
     two-labelled; `b` codes the Bloomberg field map describes; `c = n + t + f + b`;
   - `--put <xlsx path> --item-id <id> [--source-mtime <iso>] [--write] [--any-name]`: dry-run by default
     (`template_put DRY-RUN key <key> sha256 <hex>`); `--write` performs `put_template` and prints
     `template_put key <key> sha256 <hex> put_performed <True|False> existed <True|False>`; refuses (rc 2) a file whose base name is not
     `team_sheet.MASTER_NAME` unless `--any-name`.
B. In `team_sheet.py`: (i) the master arm (`_master_reading`, and the once-per-census master search) takes the newest object under
   `store.table_prefix(SOURCE, "bronze", "research_template")` whose base name is `MASTER_NAME`, by the existing newest-reading rule; it no
   longer scans the `research-report` prefix for the master; with none stored the answer is `master_absent` as today. (ii) MEASURED LABELS: for a
   code row the Bloomberg field map does NOT describe and `factset_descriptions.json` has no entry for (precedence: field map, held; entries
   file, held; MEASURED; the fallback line), read the workbook again with `data_only=False` (`read_only=True`, rows 1-400, columns 1-60) and
   apply, in order: **column-B metric name**: the code row's column-B cell is a string that is not identifier-form: that string (whitespace
   collapsed) is the label, `cite` = `"<sheet name>!B<row>"`; **single-row pass-through**: the distinct labels (the first non-identifier string in
   the first four cells) of all OTHER rows with a cell in a PERIOD column (the year row's year cells' columns) that is exactly the formula
   `=<col><code row>` (optional `$`, optional spaces, the SAME column letter as the cell itself): exactly ONE distinct label gives that text, `cite`
   = `"<sheet name>!<the referencing cell, e.g. D4>"` (the first period column where found); two or more, or none: no measured label. A measured
   label is `{"text", "source": "factset" for a code starting FF_ FFI_ FG_ FE_ or P_ else "bloomberg", "claim": "measured", "cite", "code", "why": None}`.
   The `--census` CLI's labels line gains `measured <n>` after `factset_held`; update the test that pins the line.
C. Tests `lib/research/corpus/tests/test_template_round47.py` with a fake S3 client (put_object with `IfNoneMatch`, head_object, get_object,
   `get_paginator("list_objects_v2")`): the put and its no-op second put, the table prefix and key shape, the master arm reading the table and
   nothing under `research-report`, a column-B metric name, a pass-through, a two-label code left as "FactSet line", a code with no reference
   left as the fallback, a Bloomberg-described code keeping its held description, an entries-file entry winning over a measured label, and the
   CLI count line.
D. Criteria: the order now carries a FOURTH mechanical criterion, AC4 (reason: the template table and measured labels are a second outcome
   folded into this order because the round's one-issuance gate adds no file). `<paths>` gains `template.py` and `test_template_round47.py`.
   Do NOT edit `dossier.py` again (the method stays `/13`); no real S3 write, only the fake client. Row ids `AMGT_CORPUS-D1-W1-S<k>` as
   before. The issuer's check is `.../checks/round47/aw9_check.py` (copied into your worktree, uncommitted).

**Then, in `lib/research/corpus/dossier.py`:** the stored field is the whole `rows_for` answer, so the new keys flow with no change to `build`.
Bump `METHOD_VERSION` from `amgt-corpus-dossier/12` to `amgt-corpus-dossier/13`, add the comment line `# /13 (CRPS-aw-1): team_sheet carries
row labels in words, override and fund-year rows are CONTROL, and each team cell's number format.` above it, and update ONLY that literal in the
six tests that pin it (listed in `<paths>`).

**Tests** `lib/research/corpus/tests/test_team_sheet_round47.py`: a workbook built in memory with openpyxl covering a Bloomberg code row (its
definition as stored), a FactSet code row with no entry (`FactSet line`, claim absent, why), a FactSet code row WITH an entry (monkeypatch the
loader's cache so `text` and `cite` come from it and claim is held), another Bloomberg identifier the map lacks (`Bloomberg line`), an
`*_OVERRIDE` row with numbers in the period columns and an `EQY_FUND_YEAR` row above the header (both CONTROL, neither the header), formats
per period cell (`#,##0`, `0.0%`, `General`, an absent cell None), `rows` equal to `sheet_labels`, and the `master_absent` keys empty.

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's checks. No portal file, no `scoped_amgt.py` change (the API serves the stored
   field as stored).
2. NO S3 write, NO deploy, NO push, NO Bloomberg or vendor call. S3 reads for your own testing are allowed.
3. Write code with the Edit/Write tools, never a shell heredoc, sed or `python -c` rewrite. ASCII only (also in the JSON file and the test).
4. Rows are `AMGT_CORPUS-D1-W1-S<k>` (next free k across every file under `surprise-channel/`), `disarm_owner 2.0.0_SA_COO~C1`, and
   `surfaced_at` = `date -u +%FT%TZ` at filing.
5. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.
   Your proof instance's `to_id` is this order's FULL id: `AMGT_CORPUS.TO-CRPS-aw-1.field-code-labels-name-control-and-number-formats`.

## 3. SURFACES

<paths>
lib/research/corpus/team_sheet.py
lib/research/corpus/factset_descriptions.json
lib/research/corpus/tests/test_team_sheet_round47.py
lib/research/corpus/template.py
lib/research/corpus/tests/test_template_round47.py
lib/research/corpus/tests/test_team_sheet_round44.py
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_method_bump.py
lib/research/corpus/tests/test_dossier_case_body.py
lib/research/corpus/tests/test_dossier_case_unit.py
lib/research/corpus/tests/test_dossier_case_positional.py
lib/research/corpus/tests/test_dossier_heading_only_round40.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-aw-1.field-code-labels-name-control-and-number-formats.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-aw-1.field-code-labels-name-control-and-number-formats.md
</paths>

Read-only: the whole repository, in particular `integrations/bloomberg/research/field_map.json` and the issuer's check
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw1_check.py`.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-aw-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw1_check.py" 2&gt;&amp;1 | tail -1</invocation><expect>(?m)^aw1 build 4/4 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-aw-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest -q -p no:cacheprovider lib/research/corpus/tests/test_template_round47.py lib/research/corpus/tests/test_team_sheet_round47.py lib/research/corpus/tests/test_team_sheet_round46.py lib/research/corpus/tests/test_team_sheet_round44.py lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_dossier_case_body.py lib/research/corpus/tests/test_dossier_case_unit.py lib/research/corpus/tests/test_dossier_case_positional.py lib/research/corpus/tests/test_dossier_heading_only_round40.py 2&gt;&amp;1 | tail -1 | sed 's/\x1b\[[0-9;]*m//g'</invocation><expect>(?m)^\d+ passed in [\d.]+s$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-aw-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; grep -c '^METHOD_VERSION = "amgt-corpus-dossier/13"$' lib/research/corpus/dossier.py</invocation><expect>(?m)^1$</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-aw-9"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw9_check.py" 2&gt;&amp;1 | tail -1</invocation><expect>(?m)^aw9 build 4/4 control 2/2$</expect></criterion>
</proof_of_spec>

- AC4: the template table and its no-op second put, the master arm reading the table, the measured labels, the CLI count line (AMENDMENT 2).
- AC1: the by-name CONTROL rule and the header skip, the three label shapes cited or claim-absent, the formats aligned with the values, with `rows`
  and `sheet_labels` and the round-46 values unchanged.
- AC2: your tests, round 46's and 44's, and the six method-pinning tests pass (every one of them reads `/13`).
- AC3: the method literal is `/13`.

## 5. WHEN YOU ARE DONE

1. Run `python -m lib.research.corpus.team_sheet --census` if the store is reachable and put its summary lines in your report; if it is not
   reachable, say so.
2. Write the instance at the proof path (genre BUILD), with its mutant control; run `python .tools/proof-of-spec-check.py <instance>
   AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit; rc 0.
3. Only if AC1-AC3 pass, append a new status tag reading complete at the END of this file, in the SAME commit as your instance.
4. Report ONCE: the change, AC1's line, AC2's line, AC3's line, the census lines (or why not), your commit hashes, any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-46 analysis ADDENDUM 1 (msg 3972): a vendor-described row takes the vendor's description plus its cite, claim held; a FactSet code with no source found is "FactSet line", code and why in the title; `*_OVERRIDE` and `EQY_FUND_YEAR` are CONTROL by Bloomberg's naming convention, cited; team cells render by their own number format captured at a /13 write under its own pair. Measured at the cut (live /12 team_sheet, 32 workbooks): 1348 code-labelled FIGURE rows, 646 on 56 Bloomberg mnemonics the field map describes, 702 on 50 it does not; a bounded web search (2 searches, 2 fetches, 2026-10-11) found no FactSet published description, so `factset_descriptions.json` ships empty. Four Bloomberg names the map lacks read "Bloomberg line" (the issuer's reading, stated to the CTO). Base at the cut: AC1 FAIL (`build 0/4`), AC2 FAIL (the new test file is absent), AC3 FAIL (the literal reads /12). The /13 dossier write (aw-3) and the API redeploy (aw-4) are SEPARATE paired acts after this drains.
<risk>LOCAL</risk>
<status>pending</status>
<round>47</round>
<slot>~1</slot>
<fabric>dell1</fabric>
<status>complete</status>
