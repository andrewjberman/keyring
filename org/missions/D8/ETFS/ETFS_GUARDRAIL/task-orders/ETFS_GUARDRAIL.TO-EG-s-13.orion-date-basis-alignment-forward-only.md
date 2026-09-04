# TO ETFS_GUARDRAIL.TO-EG-s-13 -- the three partners' figures describe the same day: Inflection's series re-labelled to the settled close it reflects, through `orion_normalize_as_of`, FORWARD-ONLY -- restate nothing, notify no partner -- the prerequisite to the automated send and nothing else

<to_id>ETFS_GUARDRAIL.TO-EG-s-13</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO paired at cut (the spawn IS the GO). Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance; Andrew-direct 2026-09-01 ruling cards 1 and 2, and 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S13; s.3 OWNS, the CVO-found gap; s.0 rulings table cards 1 and 2; s.6 ruling 5; brief s.6a) | **Decomp cell:** `EG-s-13` | **outcome_ref:** FWD-6 | **verb:** align | **depends_on:** --

---

## THE CELL

`EG-s-13` (PRD s.7.2 S13): `orion_normalize_as_of` -- claim `held`, evidence *"brief s.6a -- 0 calls / 19 files, the brief's denominator"*. Bound: *"PREREQUISITE TO THE SEND ONLY. Guardrail lands first. Forward-only: restate nothing, notify no partner."* Ruling 5: *"Orion date-basis alignment gates the automated send -- not the guardrail."* Ruling card 1: APPROVED, a prerequisite to the send. Ruling card 2: *"APPROVED FORWARD-ONLY. No restatement, no partner notification."* Brief s.6a: *"Inflection's series is labelled one NYSE trading day forward of the settled close it reflects; 49F and Cottonwood are correctly labelled."* FWD-6 DONE WHEN: *"APPLIED -- the alignment is in place."* ACCEPT: *"a figure shown for one partner on a given date can be set beside another partner's figure for that same date without the two being a day apart."*

**Where the function is and where the alignment belongs (measured by the issuer, to be re-grounded by you first):** `orion_normalize_as_of` is DEFINED in `data/inf/scripts/silver/_orion_vendor_asof.py` (the inf silver lane; 339 content hits across the corpus, DEF=1) and CALLED 0 times under `data/etfs/`. The Inflection ETFS slices (`daily/inflection/<date>.json`) are written by the relied-on producer `inf-etf-ownership-daily` (NOT owned, NOT modified: PRD S3's bound) with `date` = the `fact_positions` partition key. The ETFS consumer is `data/etfs/scripts/presentation/render_month_end.py` (`load_all_daily`, `:91-113`, returns `date -> etf -> {v, n, as_of}`), and the AVGCAP monthly artifact is recomputed there from each partner's daily series. **So the alignment lands at the ETFS consumer's read of the Inflection series** -- read-time re-labelling of each Inflection slice's `date` to the settled close it reflects via `orion_normalize_as_of` (read the function's own contract and docstring in `_orion_vendor_asof.py` before deciding the exact mapping; it is the estate's one implementation of the Orion date rule and you build no second one) -- applied to EVERY month the renderer produces from the cutover forward.

**FORWARD-ONLY, made mechanical:** a module constant `ORION_ALIGNMENT_CUTOVER = "2026-09"` (the first month rendered with the alignment); a month before the cutover renders as it always did (published figures are not restated); the cutover month and later render aligned. The July 2026 correction Andrew already received (`ETFS_ORION_LABEL_CORRECTION`, the orchestrator's `send_correction` mode) is NOT re-sent and not touched.

## DELIVERABLE

1. In `render_month_end.py`: `_align_inflection_series(series: dict, month: str) -> dict` applying `orion_normalize_as_of` to each Inflection date key when `month >= ORION_ALIGNMENT_CUTOVER` (collisions -- two raw dates mapping to one settled date -- resolved by the LATER raw date winning, stated in a comment and tested); called from `render_month` for `partner == "inflection"` only, on the ETFS-only series, before `_carry_forward_avg`, the charts, the matrix and the CSVs, so every artifact the month produces shares the one date basis. Import the function from `data/inf/scripts/silver/_orion_vendor_asof.py` by path when run from the repo, else from a sibling `_orion_vendor_asof.py` beside the coverage package on the reporter box, which the DEPLOY (EG-s-6) places at build time and which is NEVER committed (AMENDED BY THE ISSUER AT THE DRAIN on row ETFS_GUARDRAIL-W1-S1: no committed copy of a first-party module -- CTO~Z's ruling @1da1e2b73b; if the module cannot run standalone on the box, that is a ROW, not a copy). A committed `data/etfs/scripts/coverage/_orion_vendor_asof.py` is REFUSED by this face: remove it before the flip.
2. `data/etfs/scripts/presentation/tests/test_orion_alignment.py` -- ZERO AWS calls; arms: (a) an Inflection slice keyed 2026-09-08 (a Tuesday) aligns to the settled close `orion_normalize_as_of` returns for it (assert against the function's own answer, and separately that the aligned date is strictly earlier); (b) 49F and Cottonwood series pass through unchanged; (c) a month BEFORE the cutover leaves Inflection unchanged (forward-only); (d) the cutover month is aligned; (e) a collision keeps the later raw date's values.
3. `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~3/orion-date-basis-alignment-forward-only.result.md` -- criteria verbatim with rc and denominators; the function's contract as read; the mapping decision; where the call sits.

**No deploy in this order.** The renderer's ONE artifact upload is `EG-s-6`'s (slot 2, after every renderer cell merges). FWD-6's APPLIED grade reads the first aligned render on the box after that upload.

## ACCEPTANCE

<criterion id="S13-AC1" cell_refs="EG-s-13"><invocation>python -m pytest data/etfs/scripts/presentation/tests/test_orion_alignment.py -q</invocation><expect>passed</expect></criterion>
`S13-AC1` -- the five-arm battery is green (record N passed).

<criterion id="S13-AC2" cell_refs="EG-s-13"><invocation>python -c "import re; s=open('data/etfs/scripts/presentation/render_month_end.py').read(); import os; print('ALIGN_CALLS=%d CUTOVER=%s SECOND_IMPL=%d COMMITTED_ORION_COPY=%s' % (len(re.findall(r'orion_normalize_as_of\(', s)), re.search(r'ORION_ALIGNMENT_CUTOVER\s*=\s*\"([0-9-]+)\"', s).group(1) if re.search(r'ORION_ALIGNMENT_CUTOVER\s*=\s*\"([0-9-]+)\"', s) else 'ABSENT', len(re.findall(r'def orion_normalize_as_of\(', s)), os.path.exists('data/etfs/scripts/coverage/_orion_vendor_asof.py')))"</invocation><expect>CUTOVER=2026-09 SECOND_IMPL=0 COMMITTED_ORION_COPY=False</expect></criterion>
`S13-AC2` -- the renderer CALLS the estate's function (at least once; the count is recorded), carries the forward-only cutover as a constant, and defines no second implementation.

<criterion id="S13-AC3" cell_refs="EG-s-13"><invocation>python data/etfs/scripts/presentation/render_month_end.py --month 2026-09 --out .scratch/eg_s13_sept.html</invocation><expect>OK: 2026-09</expect></criterion>
`S13-AC3` -- the LIVE render of the cutover month (in progress) completes with the alignment in place (etfs-only reads; no PDF, no upload).

<criterion id="S13-AC4" cell_refs="EG-s-13"><invocation>python data/etfs/scripts/presentation/render_month_end.py --month 2026-08 --out .scratch/eg_s13_aug.html</invocation><expect>OK: 2026-08</expect></criterion>
`S13-AC4` -- a pre-cutover month still renders, unaligned (forward-only; the August deck's Inflection dates are what they were -- record one date key from each run side by side in the result).

<criterion id="S13-AC5" cell_refs="EG-s-13"><invocation>bash .tools/commit-gate.sh data/etfs/scripts/presentation/render_month_end.py data/etfs/scripts/presentation/tests/test_orion_alignment.py</invocation><expect>pre-commit gate clean</expect></criterion>
`S13-AC5` -- the commit gate is clean.

<criterion id="S13-AC6" cell_refs="EG-s-13" judgment="true"/>
`S13-AC6` -- graded by the CVO at L9: the three partners share one date basis from the cutover month forward; nothing published is restated and no partner is notified; the alignment gates the SEND (`EG-s-9` is handed only after this order is terminal) and not the guardrail. RECORD; NO VERDICT.

<expected_criteria>S13-AC1, S13-AC2, S13-AC3, S13-AC4, S13-AC5, S13-AC6</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** (Restated by the issuer at the drain on row ETFS_GUARDRAIL-W1-S2: the flip was always admitted; the wording withheld it.) A path you need that it does not name is a BLOCKING row, never an override. `_orion_vendor_asof.py` (the inf silver lane) is named for READING; you do not edit it. The relied-on producer `inf-etf-ownership-daily` is not touched.
- **FORWARD-ONLY (ruling card 2):** no published month is re-rendered, re-uploaded or re-sent; no partner is notified; the cutover is the first month not yet published.
- **No deploy, no `--s3-out`, no PDF in this order.** Local HTML only.
- **No firm bucket:** the renderer reads `opal-data-etfs` only (the `--inf-canonical-preview` flag is a LOCAL-ONLY diagnostic and is not used).
- **EVERY invocation is bounded.** `timeout 120`; the live renders list three partners' daily prefixes; retry once on a timeout, then record.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W3-S<k>` (`W3` = your slot; your first is `W3-S1`). Append inside the fenced json array per `org/surprise_channel/schemas/investigation_item.schema.json`, cite `path@commit`, never edit an existing row, keep working.
- **NEVER `git push`.** Report push state as MEASURED (`git ls-remote origin refs/heads/CLOUD`).

<paths>
data/etfs/scripts/presentation/
data/etfs/scripts/coverage/
data/inf/scripts/silver/_orion_vendor_asof.py
lib/trading_calendar.py
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~3/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-s-13`.
<owned_cells>EG-s-13</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL, the renderer or the Orion helper.
comp-iam: DECLARED-NOT-APPLICABLE -- a repo presentation change reading the aggregation bucket under existing grants; no policy or resource is changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`); `data/etfs/scripts/coverage/` is named only for a vendored copy of the Orion helper if the box needs one (stated in the deliverable), and `_orion_vendor_asof.py` for reading.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S13-AC1` .. `S13-AC6`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~3/ETFS_GUARDRAIL.TO-EG-s-13.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> S13-AC1,S13-AC2,S13-AC3,S13-AC4,S13-AC5,S13-AC6` BEFORE the complete flip, which the assignee commits itself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
