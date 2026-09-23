# AMGT_CORPUS task order -- `CRPS-c-6` -- ROUND 1: the per-name continuation artifact in gold -- thesis pillars, the name's own KPI set, fund of record, last stated position -- every field cited to the report and passage it came from, or ABSENT with a reason; never inferred, never defaulted

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-c-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=7 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: RUN at L5 -- 214 roles on the DESIRED plane; BLIND to this box's credential; this cell's first gold put measures the gold prefix.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, continued from `CRPS-c-3`. Work ONLY in your worktree.
- **First act:** print `git rev-parse --abbrev-ref HEAD`, and test that `lib/research/corpus/typed.py` and
  `lib/research/corpus/gold.py` exist. If either is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~1;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. NEVER TOUCH THE LIBRARY.** Every input is a stored object.

## 1. THE CELL, inlined in full -- `CRPS-c-6` (manifest row R6, outcome FWD-5)

**FWD-5, verbatim:** *"For a name the team has written up, its OWN thesis pillars, KPI set, fund of record and last
stated position are readable as typed data, each pointing at the report it came from. DONE WHEN EXERCISED -- for one
covered name, the continuation artifact is produced and every field in it resolves to a passage in a named report; a
field the reports do not state is ABSENT, never inferred and never defaulted."*

**`C-CITED-OR-ABSENT`:** *"Every field of a continuation artifact ... carries the report (and passage or sheet) it was
measured from. A field the corpus does not state is `null` with an explicit `absent` reason. Nothing in this project
infers, defaults or fills."* **`C-INPUT-HASHED`:** *"Every artifact this project serves carries `{key, sha256}` for each
input it was derived from, its own content hash, and the method version that produced it."*

**WHAT "CONTINUATION" MEANS, from the brief's scan** (`RESEARCH_CORPUS_SCAN_20260922.md` s.4, read-only):
- **fund of record** and **last stated position** come from the most recent report stating them. The
  class B earnings update's opening line `RECOMMENDATION: MAINTAIN x% POSITION IN <fund>` is the carrier, and so is a
  class A pack's `Initiate ~2% position in IDVZ`.
- **thesis pillars** are the bulleted pillars under INVESTMENT THESIS in the most recent class A research pack, each a
  bold lead plus a paragraph.
- **the name's own KPI set** is the KPI terms that NAME's own reports use, counted.

**THE KPI LEXICON IS MEASURED, NOT DESIGNED:** use the term keys of the scan's own census,
`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922/research_docx_kpi_census.json` (a list of rows,
each carrying a `kpi` dict of term -> count; read the key set from the file and cite it). Do not add a term the scan did
not count. The lexicon is a method input: its path and sha256 go in `inputs`.

**THE GOLD ARTIFACT SHAPE, shared by every gold cell of this round** (`CRPS-c-6`, `c-7`, `c-8`, `c-9`; `CRPS-c-10` reads
all four). It is stated here in full because you are its first writer:
```
{ "artifact": "<research-continuation | ...>", "method_version": "<n>",
  "subject": {...},                                  # here: {"security_key": ...}
  "inputs": [ {"key": "<s3 key>", "sha256": "<hex>"}, ... ],   # sorted by key
  "fields": {...},                                   # the typed data, every field cited or absent
  "content_sha256": "<hex>" }                        # sha256 of the canonical JSON of everything ABOVE it
```
- **Object name:** `<inputs_sha16>.json`, where `inputs_sha16` is the first 16 hex of the sha256 over
  `method_version` + the sorted inputs. The same inputs give the same object (a no-op put). A new input gives a NEW
  object, and the prior one stays.
- **Write through** `lib/research/corpus/gold.py` `gold_put(<table>, <partition>, <object>, <bytes>)`, never
  overwriting.
- **The LATEST artifact for a subject** is the object whose `inputs` equal the CURRENT inputs, recomputed at read time
  from the store. Name that rule in code (`current_inputs(subject)`), because `CRPS-c-10` depends on it.

**A citation is** `{"report_key": <bronze key>, "extract_key": <extraction key>, "locator": <page, paragraph index or
sheet!cell>, "passage": <the literal text, at most 300 chars>}`. The passage must be a substring of the extraction's
text at that locator.

**RULED -- what you build:**
1. **`lib/research/corpus/continuation.py`:**
   - `build(security_key)` returns the artifact above with `fields`: `fund_of_record`, `last_stated_position`,
     `thesis_pillars` (a list), and `kpi_set` (term -> {count, citations}). Each is cited or
     `{"value": null, "absent": "<reason>"}`.
   - `python -m lib.research.corpus.continuation --write` builds and puts one artifact per RESOLVED name at
     `gold_put("research-continuation", store.entity_partition("security_key", <key>), "<inputs_sha16>.json", ...)`.
     It prints per name `<key> fund <v|ABSENT> position <v|ABSENT> pillars <n> kpis <n> put_performed <bool>`, then
     `names <n> with_fund <f> with_position <p> with_pillars <t>`.
   - `python -m lib.research.corpus.continuation --show-first-covered` picks the first security key (sorted) whose
     artifact has a cited fund AND a cited position AND at least one pillar, prints `security_key <key>`, then each field
     with its value and its citation's `report_key` and `locator`.
   - `python -m lib.research.corpus.continuation --verify-citations` re-reads EVERY stored artifact's citations against
     their extractions and prints `citations_checked <n> resolved <n> unresolved <n>` (unresolved means the passage is
     not found at its locator), listing each unresolved one.
2. **`lib/research/corpus/tests/test_continuation.py`**, offline, under the poison, with stub stores:
   - **ABSENT, NEVER DEFAULTED:** a name whose reports state no position gives `last_stated_position.value` None with an
     `absent` reason, and NO number appears in the field;
   - **MOST RECENT WINS:** two dated reports with different positions give the later one, cited;
   - **VERIFY CAN FAIL:** a citation whose passage is altered by one character is counted `unresolved 1`;
   - **INPUT HASH MOVES:** adding one input changes the object name, and the same inputs twice give the same name.

**What this cell does NOT do:** no delta-writing and no prose (that is the `AMGT_RESAPP` addendum's), no Claude call, no
change to earlier modules.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @3c09ae6ce8, chain A, cell 5 of 7 on this slot, after `CRPS-c-3` drained VALID. Siblings on
other slots build the sector templates, the fund forms and the typecast **to the SAME gold shape**, which their faces
restate from this one.

## 3. SURFACES

<paths>
lib/research/corpus/continuation.py
lib/research/corpus/tests/test_continuation.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-6.per-name-continuation-artifact.md
</paths>

**READ-ONLY:** every earlier `lib/research/corpus/` module, `lib/research/harvest/store.py`, `lib/opal_naming.py`, and the
scan directory. Scratch in `.scratch/c6/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **Pure ASCII source, LF, Python 3.9-compatible.** Passages are stored with `ensure_ascii=True`.
- **S3:** writes ONLY through `gold_put`, never overwriting. **Run `--write` as a BUILD STEP.**
- **Surprise rows:** `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner` `2.0.0_SA_COO~X`. **REFUSE a criterion you cannot satisfy as
  written**, and report it with your measurement.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 120`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-c-6"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_continuation.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-c-6"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.continuation --verify-citations 2>&1 | tail -3</invocation><expect>citations_checked (\d+) resolved \1 unresolved 0\b</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-c-6"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.continuation --show-first-covered 2>&1 | tail -40</invocation><expect>(?s)security_key \S+.*fund_of_record .*report_key .*last_stated_position .*report_key .*thesis_pillars .*report_key </expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-c-6" judgment="true"/>
  <criterion id="AC5" cell_refs="CRPS-c-6"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC6" cell_refs="CRPS-c-6"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/c6/hyg.py</invocation><expect>(?s)outside_allowed \[\].*changed_files \d+.*bad 0</expect></criterion>
</proof_of_spec>

- **AC4 (JUDGMENT, the CVO's):** AC3's printed artifact for the covered name. Does each field say what the cited passage
  says, and is every absent field genuinely unstated? Record AC3's output and the artifact's S3 URI, with NO verdict.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-c-6.per-name-continuation-artifact.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6 --governing-order <this order>` returns rc 0.
3. Flip to `complete` only if every mechanical criterion passes. Commit with `--only`.
4. Report ONCE: the `names ... with_*` line, the citation line, and the covered name AC3 picked.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the gold shape is authored once, here, and restated verbatim in c-7, c-8 and c-9, so four writers in
three worktrees converge without a shared module they would race to create. `current_inputs` is what makes FWD-8's
"exactly the artifact that changed" gradable.

<status>pending</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
