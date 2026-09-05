# TO ETFS_GUARDRAIL.TO-EG-s-5 -- the report states how complete it is, on its own face: a per-partner coverage line in every rendered month, whatever the verdict

<to_id>ETFS_GUARDRAIL.TO-EG-s-5</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO paired at cut (the spawn IS the GO); HANDED to the slot only after EG-s-4's proof instance is VALID at HEAD (the classifier this line calls). Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance; Andrew-direct at the 1.0.0_SA_CTO terminal 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S5; s.2 DONE item 2; s.4 property 6; brief s.4 "The report must carry its own coverage line regardless of verdict") | **Decomp cell:** `EG-s-5` | **outcome_ref:** FWD-3 | **verb:** wire | **depends_on:** `EG-s-4` (slot 1, merged before this hand-off)

---

## THE CELL

`EG-s-5` (PRD s.7.2 S5): `data/etfs/scripts/presentation/render_month_end.py` (778 lines at HEAD), claim MEASURED. Bound: *"coverage line prints regardless of verdict."* FWD-3 DONE WHEN: *"APPLIED -- the statement is in the report itself."* ACCEPT: *"someone reading the report can tell, without asking anyone and without opening anything else, how much of the month it really covers and how much was filled by repeating the previous day."* Property 6: *"Every rendered report carries a per-partner coverage line regardless of verdict."*

**The renderer as it is** (read `render_month`, `:318-479`, and `_html`, `:482-629`, before writing): `load_all_daily(partner)` returns `date -> etf -> {v, n, as_of}`; `present` = partners with in-month dates; the SUMMARY rows per partner (`summary_rows`), the marquis average recomputed from each partner's daily series by `_carry_forward_avg` (full calendar month, carry-forward through no-data days), the DAILY MATRIX rendered from `_carried_daily` -- which is exactly why a gap and a held position look identical: the carry fills both. The classifier (`data/etfs/scripts/coverage/classifier.py`, from `EG-s-4`, merged at HEAD before this order) gives you `classify_month(partner, month, series=daily[partner])`, `summarize(classes)` and `coverage_line(partner, summary)` -> `"<covered>/<trading_days> trading days; <carried> carried for missing data"`. Import it through the package (`from coverage import classifier` with `data/etfs/scripts` on `sys.path`, resolved relative to `__file__`), never by a copied second implementation.

## DELIVERABLE

1. In `render_month_end.py`: (a) compute `coverage = {p: coverage_line(p, summarize(classify_month(p, month, series=daily[p]))) for p in present}` inside `render_month` (etfs-only reads, no probe: the line counts trading days without a slice as "carried" whatever their class, because the artifact carries them forward whatever their class); (b) render it in `_html`: one line per partner directly beneath that partner's SUMMARY row (or a COVERAGE block above the daily matrix -- your call, stated), plain text in the brand palette, no chart; (c) a per-partner `# coverage: <line>` comment row as the LAST row of each firm's CSV in `write_month_csvs` (the CSV is the Excel-facing artifact and Andrew opens it; a reader of either artifact can tell) -- keep the numeric rows exactly as they are so `AVERAGE()` still reproduces the deck's average; (d) the line is computed and rendered on EVERY path through `render_month`, so `EG-s-6`'s REFUSE branch (which still writes the HTML under `refused/`) carries it too -- do not gate it on anything.
2. `data/etfs/scripts/presentation/tests/test_coverage_line.py` -- ZERO AWS calls (monkeypatch `load_all_daily`, `load_universe`, `load_monthly_avg`); arms: (a) a fixture month where cottonwood has 16 of 21 trading days -> the HTML contains `16/21 trading days; 5 carried for missing data`; (b) all 21 -> `21/21 trading days; 0 carried for missing data`; (c) three partners -> three lines; (d) the CSV's last row for the partner starts with `# coverage:` and the numeric rows above are unchanged in count and values.
3. `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/the-coverage-line-in-the-report.result.md` -- criteria verbatim with rc and denominators; where the line renders (line numbers).

**No deploy in this order.** The renderer's ONE artifact upload to the reporter box's prefix is `EG-s-6`'s (the last renderer cell), so the box never runs a half-merged renderer.

## ACCEPTANCE

<criterion id="S5-AC1" cell_refs="EG-s-5"><invocation>python -m pytest data/etfs/scripts/presentation/tests/test_coverage_line.py -q</invocation><expect>passed</expect></criterion>
`S5-AC1` -- the four-arm battery is green (record N passed).

<criterion id="S5-AC2" cell_refs="EG-s-5"><invocation>python data/etfs/scripts/presentation/render_month_end.py --month 2026-08 --out .scratch/eg_s5_aug.html</invocation><expect>OK: 2026-08</expect></criterion>
`S5-AC2` -- the LIVE render of August 2026 still completes (etfs-only reads; no PDF, no S3 upload).

<criterion id="S5-AC3" cell_refs="EG-s-5"><invocation>python -c "h=open('.scratch/eg_s5_aug.html',encoding='utf-8').read(); print('COVERAGE_LINES=%d' % h.count('trading days;'))"</invocation><expect>COVERAGE_LINES=3</expect></criterion>
`S5-AC3` -- the rendered August deck carries one coverage line per present partner (three; if a partner has no August data the honest count is lower and the criterion reads as it reads).

<criterion id="S5-AC4" cell_refs="EG-s-5"><invocation>bash .tools/commit-gate.sh data/etfs/scripts/presentation/render_month_end.py data/etfs/scripts/presentation/tests/test_coverage_line.py</invocation><expect>pre-commit gate clean</expect></criterion>
`S5-AC4` -- the commit gate is clean.

<criterion id="S5-AC5" cell_refs="EG-s-5"><invocation>python -c "import re; s=open('data/etfs/scripts/presentation/render_month_end.py').read(); print('CLASSIFIER_IMPORTED=%s SECOND_IMPL=%d' % ('from coverage import classifier' in s or 'import classifier' in s, len(re.findall(r'def (?:classify_month|coverage_line)\(', s))))"</invocation><expect>CLASSIFIER_IMPORTED=True SECOND_IMPL=0</expect></criterion>
`S5-AC5` -- the renderer imports the classifier and re-implements none of it (PRD s.5: one implementation of one convention).

<criterion id="S5-AC6" cell_refs="EG-s-5" judgment="true"/>
`S5-AC6` -- graded by the CVO at L9: a reader of the PDF or the CSV can tell, without opening anything else, how much of the month is covered and how much was carried; the line is on every path (the REFUSE path too, verified at `EG-s-6`); the CSV's numeric grid is unchanged. RECORD; NO VERDICT.

<expected_criteria>S5-AC1, S5-AC2, S5-AC3, S5-AC4, S5-AC5, S5-AC6</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** (Restated by the issuer at the drain on row ETFS_GUARDRAIL-W1-S2: the flip was always admitted; the wording withheld it.) A path you need that it does not name is a BLOCKING row, never an override. You do NOT touch `data/etfs/scripts/coverage/` (slot 1's), the orchestrator, or any producer.
- **No probe, no invoke, no firm bucket:** the line reads `opal-data-etfs` only.
- **No PDF, no `--s3-out`, no upload in this order.** Local HTML only.
- **Restate nothing:** the line describes the month; it changes no figure.
- **EVERY invocation is bounded.** `timeout 120`; the live render lists three partners' daily prefixes (about 400 objects); if it exceeds the bound, retry once, then record.
- **Scratch:** `<your worktree>/.scratch/` only (the `.scratch/` in the invocations is that directory, relative to the worktree root).
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W2-S<k>`.
- **NEVER `git push`.** Report push state as MEASURED.

<paths>
data/etfs/scripts/presentation/
data/etfs/scripts/coverage/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-s-5`.
<owned_cells>EG-s-5</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL or the renderer.
comp-iam: DECLARED-NOT-APPLICABLE -- a repo presentation script reading the aggregation bucket under existing grants; no policy or resource is changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`); `data/etfs/scripts/coverage/` is named for READING (the import), and a write there is outside this cell.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S5-AC1` .. `S5-AC6`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-5.the-coverage-line-in-the-report.proof_of_spec.json`
(AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W3-S2: the instance file is named by the TASK ORDER'S OWN BASENAME stem, which is what `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`; the short `to_id` form this face carried before would have refused every flip. ONE instance file, this name, no duplicate.),
validated with `python .tools/proof-of-spec-check.py <instance> S5-AC1,S5-AC2,S5-AC3,S5-AC4,S5-AC5,S5-AC6` BEFORE the complete flip, which the assignee commits itself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
