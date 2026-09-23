# AMGT_CORPUS task order -- `CRPS-c-7` -- ROUND 1: the sector template in gold, one per business type -- section names, KPI set and chart pages, each MEASURED with its denominator (that type's reports of the total) and the per-term counts behind each KPI; both sector vocabularies bridged through the engine's own map, never a new one

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-c-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~4</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=7 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: RUN at L5 -- 214 roles on the DESIRED plane; BLIND to this box's credential; this cell's gold put measures the gold prefix.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~4`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **First act:** print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that `org/`,
  `.tools/`, `lib/research/corpus/typed.py`, `lib/research/corpus/extract.py`, `lib/research/corpus/gold.py`,
  `lib/research/corpus/tests/conftest.py` and `lib/research/peers/taxonomy.py` exist. If any is absent, STOP with a
  BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~4;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. NEVER TOUCH THE RESEARCH LIBRARY** (the synced OneDrive
  folder). Every input is a stored object in S3 (`opal-data-harvest`, the firm's own bucket).

## 1. THE CELL, inlined in full -- `CRPS-c-7` (manifest row R7, outcome FWD-6)

**FWD-6, verbatim:** *"For a business type, the team's own report shape is readable as one typed template -- its section
names, its KPI set and its chart pages. DONE WHEN EXERCISED -- the template for one business type is produced from the
corpus and prints the denominator it was measured over (how many of that type's reports, of how many total) and the
per-term counts behind each KPI it lists. ACCEPT: A bank's page can carry CET1, cost of risk, NIM and RoTE because the
team's bank reports carry them -- and the evidence for that claim is a count, not an opinion."*

**`C-TEMPLATE-IS-MEASURED`:** *"A sector template, a fund form and the typecast are MEASUREMENTS with printed denominators
(reports of that type read, of the total; per-term counts), never a designed list."*

**WHAT THE BRIEF'S SCAN FOUND** (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922/RESEARCH_CORPUS_SCAN_20260922.md`
s.3, read-only). This is the comparison bar, never a list you copy:
- Ten business types are named in prose: banks, insurers, oil/gas/energy, telecoms, consumer staples, pharma/health,
  software/tech services, industrials/transport, utilities, materials.
- **The "Sector" header uses TWO vocabularies:** FactSet/RBICS (*Technology Services, Consumer Non-Durables, Health
  Technology, Finance ...*) and GICS (*Information Technology, Consumer Staples, Financials, Health Care ...*). *"A sector
  template keyed on either alone misses half the corpus; the engine's `GICS11_TO_SCANNER13_v1` map is the bridge."*
- The KPI term census was over the Word files only, so its counts are lower bounds.

**YOUR INPUTS** (read their shapes first, from the docstrings at the top of each module):
- `CRPS-c-3`'s silver typed records, via `lib/research/corpus/typed.py` (`reports_for`, or `store.silver_latest("amgt",
  "research-report", ("security_key", "report_id"))`). Each record carries `sector_as_written` with its evidence, and
  `report_class`.
- `CRPS-c-2`'s extractions (headings, text, per-page text) at the `research-report-extract` prefix.
- **The bridge:** `lib/research/peers/taxonomy.py` (`SECTOR_MAP_ID = "GICS11_TO_SCANNER13_v1"` at `:38`). Read how it
  maps and use it as it is. **A sector string the map does not cover is reported `unmapped` with its count and its
  reports. It is NEVER mapped by hand.**
- **The KPI lexicon:** the term keys of `research_docx_kpi_census.json` in the scan directory (a list of rows, each with a
  `kpi` dict). Cite its path and sha256 in `inputs`. Add no term the scan did not count.

**ISSUER AMENDMENT (the order is REOPENED on its own worker's refusal, row `AMGT_CORPUS-Z-W4-S1`): BUSINESS TYPE IS A
PROPERTY OF THE SECURITY, READ FROM ITS WORKBOOK -- NOT OF THE REPORT.** The first run measured the report-level source
correctly and REFUSED correctly: 0 of 13 business types reached a report, because 45 of 51 non-OTHER reports carry no
`Sector:` field. That was the ISSUER's cut defect: the brief's scan read the sector from each name's WORKBOOK `Sector`
cell. **Measured by the issuer on the stored extractions before this amendment:** 43 XLSX extractions carry 48 labels
equal to `Sector` (case-insensitive, trailing colon ignored), and the label that FOLLOWS each in its sheet's `labels`
order yields a value for **33 of 33** resolved securities. The values that bridge through `taxonomy.scanner_sectors_for`
include Information Technology x7, Consumer Staples x6, Financials x5, Energy x5, Utilities x4, Health Care x2 and
Industrials x1. `Communications`, `Energy Minerals`, `Electronic Technology`, `Consumer Non-Durables`,
`Technology Services` and two `#NAME?` Excel errors return an EMPTY sector tuple. **9 securities carry more than one
distinct value.** So, replacing `business_type_of(record)` above:
- **`business_type_of_security(security_key)`**: collect the value following every `Sector` label in that security's
  XLSX extractions (the labels are coordinate-free, so this ADJACENCY is a stated working rule; print it, and cite the
  extraction key and label index for each value). Map each value through `taxonomy.scanner_sectors_for(value)`, which
  returns `(sectors_tuple, basis)`; an EMPTY tuple means unmapped. The security's business type is the map's own output:
  - one sector -> that sector;
  - several sectors from one value (for example `Consumer Discretionary`) -> ONE type keyed on the sorted sectors
    joined by `+`, exactly as the map returned them, never a choice among them;
  - an empty tuple or an Excel error such as `#NAME?` -> `unmapped` with the raw value;
  - two DIFFERENT mapped types across the security's workbooks -> `unmapped` with reason `conflict: <types>`. Never
    pick one.
  - Report-level `sector_as_written` (c-3's) is carried as evidence only. It never overrides the workbook.
- **Every non-OTHER report of the security inherits that type.** The `reports <n> of <total>` denominator and everything
  else in `build(business_type)` are unchanged.
- **Output budget, because AC2 reads `tail -60`:** `--show-first-graded` prints the `business_type ... reports <n> of
  <total>` line, then at most the TOP 20 `kpi` lines by count, then at most the TOP 20 `section` lines by count, then
  `kpis_total <k> sections_total <s>`. The stored artifact keeps everything; only the printout is capped.
- The `--write` summary adds `securities_typed <t> of 33 unmapped_securities <u> conflicts <c>`.
- **NO S3 DELETE.** The first run's `business_type=unmapped` object stays. A new method_version gives new keys.

**THE GOLD ARTIFACT SHAPE, shared by every gold cell of this round:**
```
{ "artifact": "research-sector-template", "method_version": "<n>",
  "subject": {"business_type": "<scanner13 id or 'unmapped'>"},
  "inputs": [ {"key": "<s3 key or repo path>", "sha256": "<hex>"}, ... ],   # sorted by key
  "fields": {...},
  "content_sha256": "<hex>" }                        # sha256 of the canonical JSON of everything ABOVE it
```
- **Object name:** `<inputs_sha16>.json` (the first 16 hex of sha256 over `method_version` + the sorted inputs).
- **Write through** `lib/research/corpus/gold.py` `gold_put("research-sector-template",
  "business_type=<kebab id>", "<inputs_sha16>.json", <bytes>)`. The partition value is lowercase kebab ASCII. Never
  overwrite.
- Expose `current_inputs(business_type)` so a consumer can pick the artifact whose `inputs` equal the current ones.

**RULED -- what you build:**
1. **`lib/research/corpus/sector_template.py`:**
   - `business_type_of(record)` maps `sector_as_written` through the taxonomy bridge. It returns the business type, or
     `unmapped` with the raw string.
   - `build(business_type)` computes, over that type's REPORTS (classes A-D; OTHER is excluded and counted):
     - `reports <n> of <total>`;
     - `sections`: heading texts normalised (case and whitespace only), with the count of that type's reports carrying
       each, listed where the count is at least 2;
     - `kpi_set`: lexicon terms with `count` of that type's reports mentioning each (word-bounded, case-insensitive,
       over the extraction TEXT, Word AND PDF), with up to 3 cited passages each;
     - `chart_pages`: headings matching chart-page vocabulary the corpus uses (COMMON STOCK COMPARISON, HISTORICAL
       VALUATION, VALUATION 10/20 YEARS, TRADING MULTIPLES, PRICE CHART, EARNINGS ESTIMATE PROGRESSION, PERFORMANCE VS
       FUND, and any other upper-case chart title you MEASURE, named), with counts.
   - `python -m lib.research.corpus.sector_template --write` builds and puts one artifact per business type (including
     one for `unmapped`), and prints per type `business_type <id> reports <n> of <total> sections <s> kpis <k> charts <c>
     put_performed <bool>`, then `types <n> reports_typed <r> unmapped_reports <u> other_excluded <o>`.
   - `python -m lib.research.corpus.sector_template --show-first-graded` picks the first business type (sorted) with at
     least 3 reports and prints `business_type <id> reports <n> of <total>`, then one `kpi <term> count <c> of <n>` line
     per KPI and one `section <name> count <c>` line per section, all from the STORED artifact.
2. **`lib/research/corpus/tests/test_sector_template.py`**, offline, under the package poison, with stub records and
   extractions:
   - **THE BRIDGE IS USED:** a GICS-worded and a FactSet-worded sector for the same type land in ONE business type (only
     where the taxonomy module actually bridges them; assert through the module, not a copied table);
   - **NO HAND MAPPING:** an unknown sector string lands in `unmapped` with its raw text;
   - **THE DENOMINATOR:** `reports <n> of <total>` counts OTHER-class files out of the type and into `other_excluded`;
   - **A TERM ABSENT FROM THE TEXT HAS NO COUNT:** it is not listed, and never listed with 0 as a designed member.

**What this cell does NOT do:** no fund forms (that is `CRPS-c-8`), no model typecast (that is `CRPS-c-9`), no new
taxonomy map, no change to `lib/research/peers/`.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @3c09ae6ce8, chain D, spawned on `CRPS-c-3`'s valid drain. `CRPS-c-10` reads your artifacts.

## 3. SURFACES

<paths>
lib/research/corpus/sector_template.py
lib/research/corpus/tests/test_sector_template.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-7.sector-template-per-business-type.md
</paths>

**READ-ONLY:** every other `lib/research/corpus/` file, `lib/research/peers/taxonomy.py`, `lib/research/harvest/store.py`,
`lib/opal_naming.py`, and the scan directory. Scratch in `.scratch/c7/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~4 <0.9.0_WK_AMGT_CORPUS~4@opal.agent>" -F <msgfile> -- <paths>`,
with the message file written by the Write tool.

## 4. BOUNDS
- **NO S3 DELETE OF ANY KIND** (issuer amendment on row `AMGT_CORPUS-Z-S4`): a wrong object you wrote is superseded by a
  NEW key (bump `method_version`), never deleted. An S3 delete is a human-confirmed act on this estate.
- **Pure ASCII source, LF, Python 3.9-compatible.** S3 writes ONLY through `gold_put`, never overwriting; a refused put is
  a BLOCKING row. **Run `--write` as a BUILD STEP.**
- **Surprise rows:** `AMGT_CORPUS-Z-W4-S<k>`, next unused `k`, `disarm_owner` `2.0.0_SA_COO~X`. Append, never edit.
- **REFUSE a criterion you cannot satisfy as written**, and report it with your measurement. Never repair or widen it.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 120`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-c-7"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_sector_template.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-c-7"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.sector_template --show-first-graded 2>&1 | tail -60</invocation><expect>(?s)business_type \S+ reports (\d+) of \d+.*kpi \S.* count \d+ of \1\b.*section \S.* count \d+</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-c-7" judgment="true"/>
  <criterion id="AC4" cell_refs="CRPS-c-7"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC5" cell_refs="CRPS-c-7"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/c7/hyg.py</invocation><expect>(?s)outside_allowed \[\].*changed_files \d+.*bad 0</expect></criterion>
</proof_of_spec>

- **AC3 (JUDGMENT, the CVO's):** your `--write` run's full per-type summary and the `types ... unmapped_reports ...`
  line, plus AC2's template. Is the template the team's own shape, and is the unmapped residue small enough to trust
  the types? Record them verbatim, with NO verdict.
- **`.scratch/c7/hyg.py`** (write it): diff the worktree against `git merge-base HEAD SITEZ` over `lib` and `org`; print
  `outside_allowed [...]`, `changed_files <n>`, per changed `.py` `compiles <bool> crlf <n> non_ascii <n>`, then
  `bad <n>`.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/AMGT_CORPUS.TO-CRPS-c-7.sector-template-per-business-type.proof_of_spec.json`,
   each mechanical row carrying its `expect`, the judgment row `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO~Z`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5 --governing-order <this order>` returns rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes. Commit with `--only`.
4. Report ONCE: the `types` line, the graded type with its denominator, and its first five KPI lines.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the ACCEPT names banks, but the DONE WHEN grades "one business type", so AC2 grades the first type with
3 or more reports and the CVO reads the full run at AC3. If banks do not reach 3 reports through the bridge, that is a
finding, never a relaxed threshold.

<status>complete</status>
<round>1</round>
<slot>~4</slot>
<fabric>site-z</fabric>
