# TO ETFS_GUARDRAIL.TO-EG-s-4 -- the coverage classifier: four kinds of empty day told apart, reading ONLY the aggregation bucket plus the calendar, with the upstream discriminator injected as a probe and UNKNOWN as an honest value

<to_id>ETFS_GUARDRAIL.TO-EG-s-4</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO paired at cut (the spawn IS the GO). Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance (s.6a: the discriminator's principal); Andrew-direct at the 1.0.0_SA_CTO terminal 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S4; s.7.4 the home; s.4 property 4; brief s.2 the taxonomy) | **Decomp cell:** `EG-s-4` | **outcome_ref:** FWD-4 | **verb:** classify | **depends_on:** `EG-s-10` (terminal in your own queue before this order)

---

## THE CELL

`EG-s-4` (PRD s.7.2 S4): NEW `data/etfs/scripts/coverage/classifier.py` (ABSENT at HEAD; home RULED in PRD s.7.4: *"One home, importable by the renderer"*). Bound: *"Class B is the trap. Discriminator = read upstream partition + count priced. Must not 'fix' the ZERO-vs-MISSING contract."* Accept: property 4 -- *"A day with an upstream partition and nothing priced is classified expected, not a hole, and no backfill is attempted against it."*

**The taxonomy (brief s.2), which the module MUST implement and MUST NOT collapse:**

| class | case | detect by | correct action |
|---|---|---|---|
| A | market closed (weekend/holiday) | `trading_calendar`: not a trading day | NOTHING; carry-forward is the true value |
| COVERED | a slice exists for the trading day | `daily/<partner>/<date>.json` present | nothing |
| B | source present but UNPRICED | upstream partition exists, `priced == 0` | NOTHING; the producer's ZERO-vs-MISSING contract wrote no slice on purpose; filling it FABRICATES |
| C | producer never fired, upstream present | trading day + partition EXISTS + priced > 0 + no slice | re-run the producer for that date (the ladder's rung 1, `EG-s-7`) |
| D | upstream genuinely absent | trading day + partition MISSING | targeted egress candidate (rung 3, a person decides) |
| UNKNOWN | no probe answered for this day | trading day + no slice + no probe | NEVER guessed; the ladder's rung 0/1 resolves it |

**THE PRINCIPAL, decided at L5 (decomposition v0.1.1 s.6a, row `ETFS_GUARDRAIL-S1`):** this module reads ONLY `opal-data-etfs` (`daily/<partner>/*.json`, `config/etf_universe.json`) plus the trading calendar. It NEVER reads a firm bucket or a firm prefix in `opal-data-assets` -- the ETFS layer holds no such grant by NEVER#1 design and this order grants none. The upstream check (partition exists? priced count?) is the PRODUCER's: the classifier takes it as an injected callable `probe(partner, date) -> {"partition": bool, "priced": int, "output_exists": bool} | None`. With no probe, or a probe returning None, a non-covered trading day is `UNKNOWN`. (`EG-s-1`/`EG-s-2` add the probe mode to the two owned producers in another queue; the ladder `EG-s-7`, next in yours, supplies the live probe by invoking them. You build and test against a STUB probe.)

## DELIVERABLE

1. `data/etfs/scripts/coverage/__init__.py`, `data/etfs/scripts/coverage/classifier.py` -- ASCII only, stdlib + boto3 only (no new dependency). Public API, exactly:
   - `classify_month(partner: str, month: str, *, s3=None, probe=None, series=None) -> dict[str, dict]` -- `date -> {"class": one of A/COVERED/B/C/D/UNKNOWN, "reason": str, "probe": <the probe's answer or None>}` for EVERY calendar day of the month (to the month cap: a complete month runs to its end; an in-progress month to yesterday UTC); `series` lets a caller pass an already-loaded `date -> row` map (the renderer's `load_all_daily` shape) so the renderer does not list the bucket twice.
   - `summarize(classes: dict) -> dict` -- counts per class plus `trading_days`, `covered`, `holes` (= C + UNKNOWN + D; B is NOT a hole), `expected_empty` (= B).
   - `coverage_line(partner: str, summary: dict) -> str` -- the per-partner line in exactly this shape: `"<covered>/<trading_days> trading days; <carried> carried for missing data"` where `carried` = trading days with no slice (B + C + D + UNKNOWN), because the renderer's carry-forward fills every one of them visually and the line's job is to say so (PRD FWD-3, brief s.4).
   - a CLI: `python data/etfs/scripts/coverage/classifier.py --partner <p> --month YYYY-MM [--no-probe]` printing one line `CLASSIFY: partner=<p> month=<m> trading_days=<n> COVERED=<n> A=<n> B=<n> C=<n> D=<n> UNKNOWN=<n>` then the coverage line. `--no-probe` is the only live mode this order exercises.
   - the calendar: import `trading_calendar` through a small resolver -- `lib/trading_calendar.py` when run from the repo, else a sibling `trading_calendar.py` beside the package on the reporter box, which the DEPLOY places at build time from `lib/` (EG-s-6's artifact upload) and which is NEVER committed (AMENDED BY THE ISSUER AT THE DRAIN on row ETFS_GUARDRAIL-W1-S1: CTO~Z's ruling @1da1e2b73b forbids a fifth in-repo copy of the calendar; the layer pattern -- copy from `lib/` at build time, commit nothing -- is the model; the renderer on the reporter box has no `lib/`).
2. `data/etfs/scripts/coverage/tests/test_classifier.py` -- ZERO AWS calls (stub `series` and `probe`); arms: (a) a trading day with a slice -> COVERED; (b) a Saturday -> A; (c) probe `{partition: True, priced: 0}` -> B, and B is NOT in `holes` and IS in `expected_empty`; (d) probe `{partition: True, priced: 5}` and no slice -> C; (e) probe `{partition: False}` -> D; (f) no probe -> UNKNOWN, never B/C/D; (g) THE AUGUST FIXTURE: cottonwood August 2026 with slices for every trading day EXCEPT 08-04, 08-18, 08-20, 08-21, 08-31 and a probe answering present+priced for those five -> exactly 5 C, `holes == 5`, and the coverage line reads `16/21 trading days; 5 carried for missing data`; (h) the same fixture with all 21 present -> `21/21 trading days; 0 carried for missing data`. Both arms of the empty/non-empty pair are REQUIRED (a scan that cannot find a hole and a scan that finds nothing are different claims).
3. `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/the-coverage-classifier.result.md` -- each criterion's invocation and output verbatim with rc and denominator; the resolver's two paths; the module's API as built.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`; a `judgment="true"` criterion is RECORDED with NO verdict.

<criterion id="S4-AC1" cell_refs="EG-s-4"><invocation>python -m pytest data/etfs/scripts/coverage/tests/test_classifier.py -q</invocation><expect>passed</expect></criterion>
`S4-AC1` -- the battery is green, all eight arms (record the N passed).

<criterion id="S4-AC2" cell_refs="EG-s-4"><invocation>python data/etfs/scripts/coverage/classifier.py --partner cottonwood --month 2026-08 --no-probe</invocation><expect>UNKNOWN=0</expect></criterion>
`S4-AC2` -- the LIVE read of August 2026 cottonwood as it stands after the 09-01 repair classifies no trading day UNKNOWN (every trading day has a slice). If it does not, that is a real hole today: the honest output, and a row.

<criterion id="S4-AC3" cell_refs="EG-s-4"><invocation>python data/etfs/scripts/coverage/classifier.py --partner inflection --month 2026-08 --no-probe</invocation><expect>CLASSIFY: partner=inflection month=2026-08</expect></criterion>
`S4-AC3` -- the live read runs for a calendar-day-delivered partner too (Inflection writes weekend files; A and COVERED must not collide -- record the counts).

<criterion id="S4-AC4" cell_refs="EG-s-4"><invocation>python -c "import os; print('COMMITTED_CAL_COPY=%s' % os.path.exists('data/etfs/scripts/coverage/trading_calendar.py'))"</invocation><expect>COMMITTED_CAL_COPY=False</expect></criterion>
`S4-AC4` -- AMENDED on row W1-S1: NO committed copy of the calendar inside the package; the resolver reaches `lib/` in the repo and the deploy-time sibling on the box.

<criterion id="S4-AC5" cell_refs="EG-s-4"><invocation>bash .tools/commit-gate.sh data/etfs/scripts/coverage/classifier.py data/etfs/scripts/coverage/__init__.py data/etfs/scripts/coverage/tests/test_classifier.py</invocation><expect>pre-commit gate clean</expect></criterion>
`S4-AC5` -- the commit gate is clean on every .py this order adds.

<criterion id="S4-AC6" cell_refs="EG-s-4"><invocation>python -c "import re; s=open('data/etfs/scripts/coverage/classifier.py').read(); print('FIRM_BUCKET_REFS=%d' % len(re.findall(r'opal-data-(?:assets|inf|cot|bd|schwab)', s)))"</invocation><expect>FIRM_BUCKET_REFS=0</expect></criterion>
`S4-AC6` -- the module names no firm bucket: the etfs-only principal is a property of the bytes, not a promise.

<criterion id="S4-AC7" cell_refs="EG-s-4" judgment="true"/>
`S4-AC7` -- graded by the CVO at L9: class B is EXPECTED and never a hole (property 4), the ZERO-vs-MISSING contract is untouched, UNKNOWN is never guessed, and the taxonomy is MECE over "a calendar day of the month". RECORD the evidence (test arms, the live counts); NO VERDICT.

<expected_criteria>S4-AC1, S4-AC2, S4-AC3, S4-AC4, S4-AC5, S4-AC6, S4-AC7</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** (Restated by the issuer at the drain on row ETFS_GUARDRAIL-W1-S2: the flip was always admitted; the wording withheld it.) A path you need that it does not name is a BLOCKING row, never an override. You do NOT touch the renderer (`EG-s-5`/`EG-s-6`, another queue), the producers, or the ladder (`EG-s-7`, your next order).
- **NO FIRM BUCKET, NO FIRM PREFIX, NO PROBE OF YOUR OWN.** The only live reads are `opal-data-etfs` (`daily/<partner>/`, `config/`). No `lambda invoke`, no read of `opal-data-assets`.
- **No fabrication anywhere:** the module writes nothing to S3, ever.
- **No new dependency; no second implementation** of the calendar (vendor the library byte-identical).
- **EVERY invocation is bounded.** `timeout 120`; a timeout is RECORDED AS THE OUTPUT. The live reads list one partner-month (~31 objects); if listing exceeds the bound, retry once, then record.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W1-S<k>` (`W1` = your slot; `<k>` the next unused in your coordinate -- `S1` is a seat row, not yours; your first is `W1-S1`). Append inside the fenced json array, cite `path@commit`, never edit an existing row, keep working.
- **NEVER `git push`.** Report push state as MEASURED.

<paths>
data/etfs/scripts/coverage/
lib/trading_calendar.py
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-s-4`.
<owned_cells>EG-s-4</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL or the renderer.
comp-iam: DECLARED-NOT-APPLICABLE -- a repo module that reads the aggregation bucket under existing grants and changes no policy; the one IAM change of the ladder belongs to EG-s-7.
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`).
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S4-AC1` .. `S4-AC7`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-4.the-coverage-classifier.proof_of_spec.json`
(AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W3-S2: the instance file is named by the TASK ORDER'S OWN BASENAME stem, which is what `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`; the short `to_id` form this face carried before would have refused every flip. ONE instance file, this name, no duplicate.),
validated with `python .tools/proof-of-spec-check.py <instance> S4-AC1,S4-AC2,S4-AC3,S4-AC4,S4-AC5,S4-AC6,S4-AC7` BEFORE the complete flip, which the assignee commits itself with the module, the tests and the result. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
