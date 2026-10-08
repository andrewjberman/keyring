# AMGT_RESAPP task order -- `AMGT-cc-4` -- SERVE FIVE STORED RESEARCH-NOTE SECTIONS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cc-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~311</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_C_NOTES.md) -- Over 95 covered names the five stored sections hold a value on 48, 18, 13, 13 and 13; no route serves any of them. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r79-311` (branch `wk-AMGT_RESAPP-311`, cut from the issuance commit with `--portal-ref d1b21c97`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r79-311`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-cc-4` (round 79, decomposition s.87)

The research notes we hold for a covered company carry five sections that no page can show, because nothing serves
them: the company description, why we own it, the positives, the negatives and the special items. Build ONE new pure
module that turns the already-read notes document into the block a page will be served. You do not serve it: another
cell of this round connects your function to the route.

Write `lib/research/api/dossier_sections.py` and `lib/research/api/tests/test_dossier_sections.py`. (A file named
`test_dossier_fields.py` already exists and tests something else. Do not edit it and do not reuse its name.)

The module exports these names:

- `FIELD_ORDER = ("company_description", "why_we_own", "positives", "negatives", "special_items")`
- `HEADINGS`, a dict: `company_description` -> `Company description`; `why_we_own` -> `Why we own it`; `positives` ->
  `Positives`; `negatives` -> `Negatives`; `special_items` -> `Special items`.
- `dossier_sections(document, read_failed=False)`, returning a list of exactly five dicts, one per name of `FIELD_ORDER`,
  in that order. Each dict has exactly these six keys, in this order:
  `field`, `heading`, `status`, `text`, `reason`, `citation`.

`document` is the notes document as stored (a dict with a `fields` dict), or `None` when the company has none.

Rules, applied per field name in `FIELD_ORDER`:

1. **A value.** If `document["fields"][name]` is a dict whose `value` is a string holding at least one character that is
   not whitespace: `status` is `"served"`, `text` is that string, `reason` is `None`, and `citation` is a deep copy of the
   stored `citation` when it is a dict, else `None`.
2. **The text is the stored text, unchanged.** Never strip it, trim it, re-join it, re-word it, shorten it, normalise its
   quotes or dashes, or remove the section name it opens with. A value that stops in the middle of a sentence is served
   exactly as it stops: there is NO special handling for it. The check compares bytes.
3. **Anything else is absent.** The field is missing, is `None`, is not a dict, or its `value` is `None`, an empty or
   blank string, or not a string: `status` is `"absent"`, `text` is `None`, `citation` is `None`, and `reason` is one
   plain sentence chosen by rule 4.
4. **The plain sentence**, from the stored `absent` text. `<H>` is the field's heading from `HEADINGS`. Match the stored
   text against these patterns in this order, with `re.match`, exactly as written:
   - `^no .+ section in class A (.+) or class B (.+)$`, the two groups being `a` and `b`:
     - `a` and `b` both equal `missing`: `No research report we hold for this company has a "<H>" section.`
     - only `b` equals `missing`: `The research pack of <a> has no "<H>" section.`
     - only `a` equals `missing`: `The research update of <b> has no "<H>" section.`
     - neither: `Neither the research pack of <a> nor the research update of <b> has a "<H>" section.`
   - `^.+ heading (has no prose following it|is followed by a table and no prose) in the extracted text of class ([AB]) (.+)$`:
     the report is `the research pack` for class `A` and `the research update` for class `B`, followed by ` of <label>`
     unless the label equals `missing`. Then
     `The "<H>" heading in <report> has no text under it.` for the first wording, and
     `The "<H>" heading in <report> is followed by a table and no text.` for the second.
   - no match, or the stored `absent` is not a string, or the field is missing:
     `This section is not in the research reports we hold for this company.`
   If the sentence you built holds a refused word (rule 7) or a character outside ASCII, use the last sentence instead.
5. **No document.** `document is None` and `read_failed` is false: five absent entries, each with the reason
   `We hold no research notes for this company.` `document is None` and `read_failed` is true, or `document` is not a
   dict: five absent entries, each with `The research notes for this company could not be read just now.` A dict with no
   `fields` dict is treated as having no fields (rule 3, five times).
6. **Only the five.** Every other section of the document is ignored, whatever it holds. The list always has five
   entries. The function never raises on any input and never changes the document it is given.
7. **Plain words.** No sentence the module writes (a heading or a reason) may contain, in any letter case: identity,
   unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger, bronze. These are
   matched as substrings, so "percentage" would fail on "stage". The stored `text` and the stored `citation` are not
   sentences you write and are passed through as they are, whatever words they hold.
8. **Pure.** The module imports from the Python standard library only (`copy`, `re`). It imports nothing from `lib`, opens
   no file, reads no store and makes no network call. Its source is ASCII.
9. **Bounds.** You do NOT edit `lib/research/api/scoped_amgt.py`, `lib/research/corpus/dossier.py` or
   `lib/research/api/tests/test_dossier_fields.py`. No deploy, no store write, no vendor, SEC or model call.

The test file: cover at least a served value with characters outside ASCII and blanks at both ends (assert equality of
the whole string), each sentence of rule 4, rule 5's two sentences, a section outside the five being ignored, and the
input left unchanged. Build planted documents in the test; it must not read the store.

Report: the five served counts over the covered names that AC2 prints, and anything in the store the rules above did
not foresee (file a surprise row for it and keep working; do not bend a rule to fit).

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W311-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited.
3. `lib/research/corpus/dossier.py` is READ, never edited. The stored text is served byte for byte: never re-worded, never trimmed.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/dossier_sections.py
lib/research/api/tests/test_dossier_sections.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~311/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cc-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc4.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>on planted documents a value is served byte-equal with its citation, each stored absence form reads as its plain sentence, a missing field and a section outside the five are handled, no sentence holds a refused word, the test file exists and passes; C1-C12 PASS; R79 CC4 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cc-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc4.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>the block is produced for 95 of 95 covered names; served equals stored per field at 48, 18, 13, 13 and 13 of 95; 105 of 105 served texts equal the stored text; ASML_NA_Equity and NU_US_Equity equal field by field; C1-C7 PASS; R79 CC4 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-cc-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc4.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>the api tests folder shows 828 or more passed and no failure other than test_harvest_prefixes.py::test_ii_registry_hash_matches; dossier.py is byte-unchanged against HEAD and is the blob at the cut; scoped_amgt.py carries no uncommitted edit; C1-C3 PASS; R79 CC4 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~311 <0.9.0_WK_AMGT_RESAPP~311@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~311/AMGT_RESAPP.TO-AMGT-cc-4.five-stored-sections-served.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line;
- the hookup another cell must make for your work to be served, or that none is needed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO ruling msg 31623 and round-78 analysis enrichment item 2. Drafted in `deliverables/2.0.0_SA_COO~Z/round79/GROUP_C_NOTES.md` (cell C1), committed before the cut, in the issuance commit's ancestry. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>79</round>
<slot>0.9.0_WK_AMGT_RESAPP~311</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
