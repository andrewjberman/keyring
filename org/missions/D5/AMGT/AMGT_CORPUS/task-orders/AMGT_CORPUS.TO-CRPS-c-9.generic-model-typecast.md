# AMGT_CORPUS task order -- `CRPS-c-9` -- ROUND 1: the generic model typecast in gold, ONE object -- the shared mnemonic core, the extended ratio set and the Opal Case Assumptions block, each with the count of workbooks carrying it out of the workbooks read; FactSet codes typed onto the same lines only where a mapping is MEASURED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-c-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=7 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: RUN at L5 -- 214 roles on the DESIRED plane; BLIND to this box's credential; this cell's gold put measures the gold prefix.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **First act:** print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that `org/`,
  `.tools/`, `lib/research/corpus/extract.py`, `lib/research/corpus/gold.py`, `lib/research/corpus/tests/conftest.py` and
  `lib/research/harvest/store.py` exist. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~3;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. NEVER TOUCH THE RESEARCH LIBRARY** (the synced OneDrive
  folder). Every input here is a stored extraction in S3 (`opal-data-harvest`, the firm's own bucket).

## 1. THE CELL, inlined in full -- `CRPS-c-9` (manifest row R9, outcome FWD-7)

**FWD-7, verbatim:** *"The generic model shape the team uses for EVERY sector is readable as one typed template,
separately from the sector ones. DONE WHEN EXERCISED -- the typecast artifact lists the shared mnemonic core, the extended
ratio set and the Opal Case Assumptions block, each with the count of workbooks carrying it out of the workbooks read."*

**`C-TEMPLATE-IS-MEASURED`:** *"A sector template, a fund form and the typecast are MEASUREMENTS with printed
denominators (reports of that type read, of the total; per-term counts), never a designed list."*

**WHAT THE BRIEF'S SCAN MEASURED** (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922/RESEARCH_CORPUS_SCAN_20260922.md`
s.2, read-only). This is the BAR YOUR MEASUREMENT IS COMPARED WITH, never a list you copy:
- 58 of 60 workbooks with model content carry one Bloomberg mnemonic core (`PX_LAST`, `EQY_SH_OUT_TOT_MULT_SH`, `NET_DEBT`,
  `BEST_EPS`, `BEST_DPS`, ...).
- 35 carry an extended ratio set (`PX_TO_BOOK_RATIO`, `RETURN_COM_EQY`, `RETURN_ON_INV_CAPITAL`, ...).
- 23 are a FactSet-based variant with the same lines under FactSet codes (`FF_SALES`, `FF_EPS`, `FF_ROE`, ...).
- The **Opal Case Assumptions** block (REVENUE GROWTH and EARNINGS MARGIN, each with MIN / MAX / AVERAGE / MEDIAN)
  drives Upside / Base / Downside cases in 58 workbooks.
- K4, the PRD's question: *"whether the 23 FactSet-coded variants type onto the same mnemonics."*

**YOUR INPUT** is `CRPS-c-2`'s extraction documents at the `research-report-extract` prefix (one `extract.json` per
report), read through `lib/research/harvest/store.py` (`table_prefix`, a paginated `list_objects_v2`, `get_object`).
Their shape is documented at the top of `lib/research/corpus/extract.py`: read it first. For an XLSX, the extraction
carries `sheets`, per-sheet `labels`, `mnemonics` and `factset_codes`.

**THE GOLD ARTIFACT SHAPE, shared by every gold cell of this round:**
```
{ "artifact": "research-model-typecast", "method_version": "<n>",
  "subject": {"scope": "all-workbooks"},
  "inputs": [ {"key": "<s3 key>", "sha256": "<hex>"}, ... ],   # every extraction read, sorted by key
  "fields": {...},
  "content_sha256": "<hex>" }                        # sha256 of the canonical JSON of everything ABOVE it
```
- **Object name:** `<inputs_sha16>.json` (first 16 hex of sha256 over `method_version` + the sorted inputs).
- **Write through** `lib/research/corpus/gold.py` `gold_put("research-model-typecast", "scope=all-workbooks",
  "<inputs_sha16>.json", <bytes>)`, never overwriting.
- Expose `current_inputs()` (the inputs recomputed from the store now) so a consumer can pick the artifact whose
  `inputs` equal them.

**RULED -- what you build:**
1. **`lib/research/corpus/typecast.py`:**
   - `build()` reads every XLSX extraction and computes three things. Each member carries `count` of workbooks and
     `workbooks_read`, and cites up to 5 workbook keys:
     - **`mnemonic_core`:** every mnemonic carried by at least 90% of the workbooks that carry ANY mnemonic. The
       threshold is a stated working rule, printed.
     - **`extended_ratio_set`:** mnemonics carried by 25% to 90% of them.
     - **`opal_case_assumptions`:** the presence and count of the block, detected from labels (`Opal Case Assumptions`
       together with `REVENUE GROWTH` / `EARNINGS MARGIN` and `Upside Case` / `Base Case` / `Downside Case`), and
       the label lines found.
   - **FactSet typing:** a FactSet code maps onto a Bloomberg mnemonic ONLY where the SAME row label carries the
     Bloomberg mnemonic in one workbook and the FactSet code in another. That is measured by label, and the label
     is the evidence. Every other FactSet code is listed `unmapped` with its count. **No hand mapping.**
   - `python -m lib.research.corpus.typecast --write` puts the one object and prints: `workbooks_read <N>`,
     `with_mnemonics <m>`, one `core <MNEMONIC> <c> of <m>` line per core member, then `extended <n> members`,
     `opal_case_assumptions <c> of <N>`, `factset mapped <a> unmapped <b>`, and `written <uri> put_performed <bool>`.
   - `python -m lib.research.corpus.typecast --read-latest` reads the stored object whose `inputs` equal
     `current_inputs()` and prints the same summary lines from the STORED document.
2. **`lib/research/corpus/tests/test_typecast.py`**, offline, under the package poison (`tests/conftest.py`), with stub
   extractions:
   - a mnemonic in 9 of 10 workbooks is core, and one in 3 of 10 is extended;
   - **NO HAND MAPPING:** a FactSet code with no shared row label stays `unmapped`;
   - **MAPPING BY LABEL:** a shared label maps the code, and the label is recorded as evidence;
   - **THE DENOMINATOR IS PRINTED:** every core line carries `of <m>`.

**What this cell does NOT do:** no sector split (the scan found the model sheet sector-agnostic, and the sector lives
in `CRPS-c-7`'s templates), no workbook re-read from the library, no change to other modules.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @3c09ae6ce8, chain C, spawned on `CRPS-c-2`'s valid drain. `CRPS-c-10` reads your artifact.

## 3. SURFACES

<paths>
lib/research/corpus/typecast.py
lib/research/corpus/tests/test_typecast.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-9.generic-model-typecast.md
</paths>

**READ-ONLY:** every other `lib/research/corpus/` file, `lib/research/harvest/store.py`, `lib/opal_naming.py`, and the
scan file. Scratch in `.scratch/c9/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~3 <0.9.0_WK_AMGT_CORPUS~3@opal.agent>" -F <msgfile> -- <paths>`,
with the message file written by the Write tool.

## 4. BOUNDS
- **Pure ASCII, LF, Python 3.9-compatible.** S3 writes ONLY through `gold_put`, never overwriting; a refused put is a
  BLOCKING row with the error verbatim. **Run `--write` as a BUILD STEP.**
- **Surprise rows:** `AMGT_CORPUS-Z-W3-S<k>`, next unused `k`, `disarm_owner` `2.0.0_SA_COO~X`. Append, never edit.
- **REFUSE a criterion you cannot satisfy as written**, and report it with your measurement. Never repair or widen it.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 120`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-c-9"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_typecast.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-c-9"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.typecast --read-latest 2>&1 | tail -60</invocation><expect>(?s)workbooks_read (\d+).*with_mnemonics (\d+).*core PX_LAST \d+ of \2\b.*extended \d+ members.*opal_case_assumptions \d+ of \1\b.*factset mapped \d+ unmapped \d+</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-c-9" judgment="true"/>
  <criterion id="AC4" cell_refs="CRPS-c-9"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC5" cell_refs="CRPS-c-9"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/c9/hyg.py</invocation><expect>(?s)outside_allowed \[\].*changed_files \d+.*bad 0</expect></criterion>
</proof_of_spec>

- **AC3 (JUDGMENT, the CVO's):** AC2's printed typecast set beside the scan's section 2 (58 of 60 core, 35 extended, 23
  FactSet, 58 Opal Case Assumptions). Does the measurement agree, and where it differs, is the difference explained?
  Record AC2's output and one paragraph naming each difference, with NO verdict.
- **`.scratch/c9/hyg.py`** (write it): diff the worktree against `git merge-base HEAD SITEZ` over `lib` and `org`; print
  `outside_allowed [...]` (every changed path NOT in `<paths>`), `changed_files <n>`, per changed `.py` `compiles <bool>
  crlf <n> non_ascii <n>`, then `bad <n>`.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-c-9.generic-model-typecast.proof_of_spec.json`,
   each mechanical row carrying its `expect`, the judgment row `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO~Z`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5 --governing-order <this order>` returns rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes. Commit with `--only`.
4. Report ONCE: `workbooks_read`, the core list with counts, `opal_case_assumptions`, and the FactSet mapped/unmapped line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the 90% / 25% thresholds are working rules stated in the artifact, not tuned. The scan's figures are
the comparison bar for the CVO's judgment, never the answer the worker is asked to reproduce.

<status>pending</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
