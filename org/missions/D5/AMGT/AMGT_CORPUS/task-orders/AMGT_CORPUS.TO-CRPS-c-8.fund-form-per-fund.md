# AMGT_CORPUS task order -- `CRPS-c-8` -- ROUND 1: the fund form in gold, one per fund of record -- the report skeleton each fund's reports keep, every section counted against that fund's reports; where two funds' skeletons differ, BOTH are kept and labelled

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-c-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~5</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=7 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: RUN at L5 -- 214 roles on the DESIRED plane; BLIND to this box's credential; this cell's gold put measures the gold prefix.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~5`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **First act:** print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that `org/`,
  `.tools/`, `lib/research/corpus/typed.py`, `lib/research/corpus/extract.py`, `lib/research/corpus/gold.py` and
  `lib/research/corpus/tests/conftest.py` exist. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~5;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. NEVER TOUCH THE RESEARCH LIBRARY** (the synced OneDrive
  folder). Every input is a stored object in S3 (`opal-data-harvest`, the firm's own bucket).

## 1. THE CELL, inlined in full -- `CRPS-c-8` (manifest row R8, outcome FWD-6)

**Manifest R8:** *"fund form, one per fund of record | harvest / gold / research-fund-form, by fund | FWD-6."*
**`C-TEMPLATE-IS-MEASURED`:** *"A sector template, a fund form and the typecast are MEASUREMENTS with printed
denominators ... never a designed list. Where the two funds' skeletons differ, BOTH are kept and labelled; the fund of
record picks at serve time."*

**WHAT THE BRIEF'S SCAN FOUND** (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922/RESEARCH_CORPUS_SCAN_20260922.md`
s.1 and s.3, read-only). This is the comparison bar, never a list you copy:
- *"The two funds write differently and the layer must know which fund a name is in."*
- **IDVZ** (43 names; Word; the international-dividend PM) carries RECOMMENDATION + TRADING HISTORY + PERFORMANCE VS FUND
  and dividend language in nearly every file.
- **PFOE** (18 names; PDF; the US-growth PM) carries a fixed five-section skeleton (*Headline results, Geographic
  highlights, Segment highlights, Headwinds and risks, Guidance*) and *"Fund: PFOE"* in the header.
- **DIVZ** appears 3 times as a candidate fund.
- *"The fund is a field of the report, not of the security."*

**YOUR INPUTS** (read their shapes first, from the docstrings at the top of each module):
- `CRPS-c-3`'s silver typed records via `lib/research/corpus/typed.py` or `store.silver_latest("amgt",
  "research-report", ("security_key", "report_id"))`. Each carries `fund` with `fund_evidence` or `fund_absent_reason`,
  and `report_class`.
- `CRPS-c-2`'s extractions (headings in order) at the `research-report-extract` prefix.

**THE GOLD ARTIFACT SHAPE, shared by every gold cell of this round:**
```
{ "artifact": "research-fund-form", "method_version": "<n>",
  "subject": {"fund": "<as the corpus writes it>"},
  "inputs": [ {"key": "<s3 key>", "sha256": "<hex>"}, ... ],   # sorted by key
  "fields": {...},
  "content_sha256": "<hex>" }                        # sha256 of the canonical JSON of everything ABOVE it
```
- **Object name:** `<inputs_sha16>.json` (the first 16 hex of sha256 over `method_version` + the sorted inputs).
- **Write through** `lib/research/corpus/gold.py` `gold_put("research-fund-form", "fund=<lowercase kebab>",
  "<inputs_sha16>.json", <bytes>)`. Never overwrite.
- Expose `current_inputs(fund)` so a consumer can pick the artifact whose `inputs` equal the current ones.

**RULED -- what you build:**
1. **`lib/research/corpus/fund_form.py`:**
   - `build(fund)` computes, over the reports whose record states that fund (classes A-D):
     - `reports <n>`;
     - `skeleton`: section headings normalised (case and whitespace only), in their MEDIAN order position, each with
       `count <c> of <n>` and up to 3 cited reports;
     - `by_class`: the same, split per report class, so an initiation skeleton and an update skeleton are not blended.
   - Funds are the values the records STATE. No fund is added, merged or renamed. A record with no fund is counted in
     `absent_fund_reports` and belongs to no form.
   - `python -m lib.research.corpus.fund_form --write` puts one artifact per fund and prints per fund
     `fund <name> reports <n> sections <s> put_performed <bool>`, then `funds <n> fund_reports <r> absent_fund_reports <a>`.
   - `python -m lib.research.corpus.fund_form --compare` reads the STORED artifacts and prints, for each pair of funds,
     `pair <a> <b> shared <s> only_<a> <x> only_<b> <y>` and the differing section names. This is the
     "both kept and labelled" evidence.
2. **`lib/research/corpus/tests/test_fund_form.py`**, offline, under the package poison, with stub records:
   - **NO FUND INVENTED:** a record with `fund` None lands in `absent_fund_reports` and in no form;
   - **BOTH KEPT:** two funds with different skeletons produce two artifacts, and `--compare` reports the differing
     sections;
   - **THE DENOMINATOR:** each section line carries `of <n>`.

**What this cell does NOT do:** no sector templates, no typecast, no position or fund-of-record choice for a security
(that is the continuation artifact's), no change to other modules.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @3c09ae6ce8, chain E, spawned on `CRPS-c-3`'s valid drain. `CRPS-c-10` reads your artifacts.

## 3. SURFACES

<paths>
lib/research/corpus/fund_form.py
lib/research/corpus/tests/test_fund_form.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-8.fund-form-per-fund.md
</paths>

**READ-ONLY:** every other `lib/research/corpus/` file, `lib/research/harvest/store.py`, `lib/opal_naming.py`, and the
scan file. Scratch in `.scratch/c8/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~5 <0.9.0_WK_AMGT_CORPUS~5@opal.agent>" -F <msgfile> -- <paths>`,
with the message file written by the Write tool.

## 4. BOUNDS
- **NO S3 DELETE OF ANY KIND** (issuer amendment on row `AMGT_CORPUS-Z-S4`): a wrong object you wrote is superseded by a
  NEW key (bump `method_version`), never deleted. An S3 delete is a human-confirmed act on this estate.
- **Pure ASCII source, LF, Python 3.9-compatible.** S3 writes ONLY through `gold_put`, never overwriting; a refused put is
  a BLOCKING row. **Run `--write` as a BUILD STEP.**
- **Surprise rows:** `AMGT_CORPUS-Z-W5-S<k>`, next unused `k`, `disarm_owner` `2.0.0_SA_COO~X`. Append, never edit.
- **REFUSE a criterion you cannot satisfy as written**, and report it with your measurement. Never repair or widen it.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 120`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-c-8"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_fund_form.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-c-8"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.fund_form --compare 2>&1 | tail -40</invocation><expect>(?s)fund \S+ reports \d+ sections \d+.*pair \S+ \S+ shared \d+ only_\S+ \d+ only_\S+ \d+</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-c-8" judgment="true"/>
  <criterion id="AC4" cell_refs="CRPS-c-8"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC5" cell_refs="CRPS-c-8"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/c8/hyg.py</invocation><expect>(?s)outside_allowed \[\].*changed_files \d+.*bad 0</expect></criterion>
</proof_of_spec>

- `--compare` must also print the per-fund `fund <name> reports <n> sections <s>` lines from the STORED artifacts, before
  the pairs.
- **AC3 (JUDGMENT, the CVO's):** the `--write` summary and AC2's comparison beside the scan's description of the two
  funds. Record them verbatim, with NO verdict.
- **`.scratch/c8/hyg.py`** (write it): diff the worktree against `git merge-base HEAD SITEZ` over `lib` and `org`; print
  `outside_allowed [...]`, `changed_files <n>`, per changed `.py` `compiles <bool> crlf <n> non_ascii <n>`, then
  `bad <n>`.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~5/AMGT_CORPUS.TO-CRPS-c-8.fund-form-per-fund.proof_of_spec.json`,
   each mechanical row carrying its `expect`, the judgment row `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO~Z`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5 --governing-order <this order>` returns rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes. Commit with `--only`.
4. Report ONCE: the `funds` line and each pair line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** `by_class` exists because a fund's initiation pack and its quarterly update are different skeletons;
blending them would produce a form neither report actually keeps.

<status>complete</status>
<round>1</round>
<slot>~5</slot>
<fabric>site-z</fabric>
