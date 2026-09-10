# NFRA_REPORT.TO-RP-s-22 -- Map the live collector's output into the edition row shape, with no transcribed fact anywhere

<!-- ============ WORKER FACE -- this is the WHOLE of the worker's context ============ -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R4.md</decomp_doc>
<owned_cells>RP-s-22</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~2</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-14)

The live Lambda already collects everything the morning email needs. The specimen already renders it
beautifully. **Nothing joins them, and that is your cell.**

Create `infra/aws/lambda/infrastructure_monitor/edition_rows.py` defining:

```
  rows_from_report(report, prior_report=None) -> (rows, omissions)
```

where `report` is exactly what `lambda_handler` assembles -- `report["sections"]`, a dict of **13**
keys -- and `rows` are dicts in the SAME SHAPE the specimen's `ROW_FACTS` entries already are.
`prior_report` is what `_load_prior_report()` returns, and it is the previous-state substrate the
per-row delta needs. **It already exists on the live side; you are not building it.**

**THE 13 SECTIONS, read from `lambda_function.py:185-293` at HEAD, in the order `lambda_handler` fills them:**

```
   1 lambda_health        5 producer_drift      9 aws_costs        13 openai_cost
   2 smartx_pipeline      6 sns_egress         10 cost_depth
   3 data_freshness       7 graph_head         11 security_sweep
   4 deploy_drift         8 contract_integrity 12 ai_analysis
```

⛔ **YOU MUST PARTITION ALL 13 INTO EXACTLY THREE BUCKETS AND PRINT THE DENOMINATOR:**

```
  MAPPED                  -- becomes one or more rows from the collector's own values
  OMITTED-WITH-REASON     -- cannot be collected live in the row shape; the REASON is recorded
                             and the section is ABSENT from the edition, never faked
  CONDITIONAL-BY-DESIGN   -- ai_analysis is None when lambda_health.functions_with_errors == 0.
                             This is CORRECT behaviour, not a regression, and the partition must
                             say so in its own output rather than leaving a reader to infer it
```

⛔ **`C-NO-FROZEN-FACTS` IS THE WHOLE POINT OF THIS CELL.** A row that cannot be collected live is
**OMITTED WITH A STATED REASON**, never rendered from a literal. *A frozen fact in a daily email is
worse than an absent row, because it looks current.*

## DEPENDENCIES

**NONE.** You are a ready root. `RP-s-21` runs beside you, porting the render logic into
`edition.py`; you never read or write that file and it never reads or writes yours.

⚠ **THE ROW SHAPE YOU TARGET IS THE SPECIMEN'S, AT HEAD, AND IT IS FROZEN.** Read it from
`org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/compose_edition.py`'s
`ROW_FACTS` entries. `RP-s-21` is forbidden from changing it. **If you find the shape cannot carry a
collector's output without changing, that is a surprise ROW and you STOP on the affected criterion** --
do not invent a shape and do not work around it.

## BOUNDS -- what this cell may not cross

- ⛔ **NO NEW DEPENDENCY AND NO NEW LAYER.** Python 3.12 standard library only. `AC5` refuses the rest.
- ⛔ **NO LIVE AWS CALL FROM THIS MODULE.** You map a `report` dict your caller hands you. You do not
  collect. `boto3` is refused by `AC5` exactly as any third-party import is.
- ⛔ **DO NOT EDIT `lambda_function.py`.** Wiring is `RP-s-23`'s cell. It is not in your paths.
- ⛔ **DO NOT EDIT the specimen `compose_edition.py`** -- round 3's terminal deliverable and the
  definition of the shape you target. It is not in your paths.
- ⛔ **NO ALARM, TOPIC, SUBSCRIPTION, SCHEDULE OR NOTIFICATION** may be minted. Andrew cleared this
  work as *"just swapping out the code of the existing lambda"* and that clearance covers nothing else.
- ⚠ **CENSUS FROM THE MAIN CHECKOUT, NEVER FROM YOUR WORKTREE.** A `comp-find` zero obtained inside a
  linked worktree is **not evidence of absence** (`org/modules/graph/INSTRUMENT_LIMITS.md` LIMIT 4 / 4a;
  msg 20822). Run any census from `C:/Users/Opal Bloomberg/Desktop/ajb_workspace`.
- ⚠ **NO NON-ASCII in code you write** -- `OK:` / `WARN:` / `ERROR:` / `SKIP:` / `BLOCKED:`.

## BATTERY FINDINGS THAT TOUCH THIS CELL

`comp-surprise --project NFRA_REPORT` at the cut: 30 items, 0 duplicate ids, 0 malformed, **OPEN 0,
ARMED 0.** No armed hazard is carried into this round. If you surface one, append a row and keep working.

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/lambda/infrastructure_monitor/edition_rows.py
org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~2/
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-22.map-the-live-collector-output-into-the-row-shape.md
</paths>

READ-ONLY references you will need (do not write them):
`infra/aws/lambda/infrastructure_monitor/lambda_function.py` (the collector -- `lambda_handler` :185-293 and each `check_*` it calls),
`org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/compose_edition.py` (`ROW_FACTS` -- the shape you target),
`org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD_ADDENDUM_01.md`,
`org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R4.md`.

⭐ **YOUR DELIVERABLE FOLDER IS `deliverables/0.9.0_WK_NFRA_REPORT~2/`, DERIVED FROM `<issued_to>`.**
Round 2 pointed all seven orders at `~1/` regardless of who was issued the order (row `Z-S8`); this
round names the right folder per worker. Do not write into `~1/`.

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

Your deliverable is `infra/aws/lambda/infrastructure_monitor/edition_rows.py`, plus
`.../deliverables/0.9.0_WK_NFRA_REPORT~2/SECTION_MAPPING.md` carrying the 13-section partition with
its denominator and, for every OMITTED section, the reason it cannot be collected live.

## PROOF OF SPEC

⛔ **`AC2` IS THE CELL AND `AC4` IS WHAT STOPS IT BEING FAKED.** A mapper can satisfy a partition
count while returning the same rows for every input. `AC4` feeds it two different reports and requires
two different row sets.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-22"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "import ast;src=open('infra/aws/lambda/infrastructure_monitor/edition_rows.py',encoding='utf-8').read();t=ast.parse(src);names={n.name for n in t.body if isinstance(n,ast.FunctionDef)};print('MODULE_LEVEL_DEFS=%d HAS_rows_from_report=%s' % (len(t.body),'rows_from_report' in names))"</invocation><expect>HAS_rows_from_report=True with MODULE_LEVEL_DEFS greater than zero -- the module exists and defines the entry point. POSITIVE arm: it exists so no later criterion can pass on an absent file</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-22"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 180 python -c "
import importlib.util,sys,json
s=importlib.util.spec_from_file_location('er','infra/aws/lambda/infrastructure_monitor/edition_rows.py');m=importlib.util.module_from_spec(s);sys.modules['er']=m;s.loader.exec_module(m)
KEYS=['lambda_health','smartx_pipeline','data_freshness','deploy_drift','producer_drift','sns_egress','graph_head','contract_integrity','aws_costs','cost_depth','security_sweep','ai_analysis','openai_cost']
rep={'timestamp':'2026-09-10T13:00:00Z','status':'success','sections':{k:{'status':'OK','probe':k} for k in KEYS}}
rep['sections']['ai_analysis']=None
rows,om=m.rows_from_report(rep,None)
covered=set()
for o in om: covered.add(o.get('section') if isinstance(o,dict) else o)
for r in rows:
    sec=r.get('section') or r.get('source_section')
    if sec: covered.add(sec)
missing=[k for k in KEYS if k not in covered]
print('SECTIONS=%d COVERED=%d MISSING=%s ROWS=%d OMISSIONS=%d' % (len(KEYS),len(covered&set(KEYS)),missing,len(rows),len(om)))
"</invocation><expect>SECTIONS=13 and COVERED=13 and MISSING=[] -- every one of the 13 collector sections is accounted for, either as a row or as a recorded omission. ROWS and OMISSIONS are printed as the partition's own denominators so a COVERED=13 achieved by omitting everything is visible rather than silent</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-22"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 180 python -c "
import importlib.util,sys
s=importlib.util.spec_from_file_location('er2','infra/aws/lambda/infrastructure_monitor/edition_rows.py');m=importlib.util.module_from_spec(s);sys.modules['er2']=m;s.loader.exec_module(m)
KEYS=['lambda_health','smartx_pipeline','data_freshness','deploy_drift','producer_drift','sns_egress','graph_head','contract_integrity','aws_costs','cost_depth','security_sweep','ai_analysis','openai_cost']
rep={'sections':{k:{'status':'OK','probe':k} for k in KEYS}};rep['sections']['ai_analysis']=None
rows,om=m.rows_from_report(rep,None)
noreason=[o for o in om if not (isinstance(o,dict) and str(o.get('reason','')).strip())]
print('OMISSIONS=%d WITHOUT_REASON=%d' % (len(om),len(noreason)))
"</invocation><expect>WITHOUT_REASON=0 with OMISSIONS printed as the denominator -- C-NO-FROZEN-FACTS' other half: every omission carries a stated reason, so an absent row is explained rather than merely missing</expect></criterion>
  <criterion id="AC4" cell_refs="RP-s-22"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 180 python -c "
import importlib.util,sys,json
s=importlib.util.spec_from_file_location('er3','infra/aws/lambda/infrastructure_monitor/edition_rows.py');m=importlib.util.module_from_spec(s);sys.modules['er3']=m;s.loader.exec_module(m)
KEYS=['lambda_health','smartx_pipeline','data_freshness','deploy_drift','producer_drift','sns_egress','graph_head','contract_integrity','aws_costs','cost_depth','security_sweep','ai_analysis','openai_cost']
def rep(st):
    r={'sections':{k:{'status':st,'probe':k,'functions_with_errors':(3 if st!='OK' else 0)} for k in KEYS}};r['sections']['ai_analysis']=None;return r
a,_=m.rows_from_report(rep('OK'),None)
b,_=m.rows_from_report(rep('BREACH'),None)
print('ROWS_A=%d ROWS_B=%d DIFFER=%s' % (len(a),len(b),json.dumps(a,sort_keys=True,default=str)!=json.dumps(b,sort_keys=True,default=str)))
"</invocation><expect>DIFFER=True with ROWS_A and ROWS_B both greater than zero -- two reports whose live state differs produce different rows. THE DISCRIMINATION ARM: a mapper that returned a transcribed literal would satisfy AC2 and AC3 and fail here, which is exactly the defect this cell exists to prevent</expect></criterion>
  <criterion id="AC5" cell_refs="RP-s-22"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "import ast,sys;src=open('infra/aws/lambda/infrastructure_monitor/edition_rows.py',encoding='utf-8').read();t=ast.parse(src);mods=set()
for n in ast.walk(t):
    if isinstance(n,ast.Import):
        for a in n.names: mods.add(a.name.split('.')[0])
    elif isinstance(n,ast.ImportFrom):
        if n.module: mods.add(n.module.split('.')[0])
std=set(sys.stdlib_module_names);bad=sorted(m for m in mods if m not in std)
print('IMPORTS=%d NON_STDLIB=%d NAMES=%s' % (len(mods),len(bad),bad))"</invocation><expect>NON_STDLIB=0 and NAMES=[] with IMPORTS printed as the denominator -- stdlib only, so no new dependency and no layer change, and no live read from this module (boto3 would appear here)</expect></criterion>
  <criterion id="AC6" cell_refs="RP-s-22"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "src=open('infra/aws/lambda/infrastructure_monitor/edition_rows.py',encoding='utf-8').read();bad=[(i+1,l) for i,l in enumerate(src.splitlines()) if any(ord(c)>126 for c in l)];print('LINES=%d NON_ASCII_LINES=%d FIRST=%s' % (len(src.splitlines()),len(bad),bad[:2]))"</invocation><expect>NON_ASCII_LINES=0 with LINES printed as the denominator -- production code carries no non-ASCII</expect></criterion>
</proof_of_spec>

### What each criterion means

- **AC1** (POSITIVE, structural): the module exists and defines `rows_from_report` -- the arm that stops the rest passing on an absent file
- **AC2** (COVERAGE, DENOMINATOR PRINTED): all 13 sections accounted for as row or recorded omission
- **AC3** (C-NO-FROZEN-FACTS, half one): every omission carries a stated reason
- **AC4** (DISCRIMINATION, the anti-literal arm): different live state produces different rows
- **AC5** (DEPLOYABILITY + no-live-read): stdlib only
- **AC6** (LAW): no non-ASCII in production code

### THE RED ARM -- exercised against the world BEFORE this order was issued

```
AC1  unparseable, file absent                       FAILS  (expect HAS_rows_from_report=True)
AC2  ModuleNotFoundError                            FAILS  (expect SECTIONS=13 COVERED=13)
AC3  ModuleNotFoundError                            FAILS  -- and note it would read
                                                    OMISSIONS=0 WITHOUT_REASON=0 on an
                                                    EMPTY mapper and PASS VACUOUSLY;
                                                    AC1 and AC2 are its positive controls
AC4  ModuleNotFoundError                            FAILS  (expect DIFFER=True)
AC5  unparseable, file absent                       FAILS  -- same vacuity trap, same guard
AC6  unreadable, file absent                        FAILS  -- same vacuity trap, same guard
```

⚠ **THE SYNTHETIC REPORT IN AC2/AC3/AC4 IS A FIXTURE, NOT THE LIVE SHAPE, AND THAT IS DECLARED.** It
carries the 13 real key names and a plausible value shape; it does not claim to be what the collector
actually returns. If the real per-section values do not fit your mapper's expectations, **that is a
finding worth a surprise ROW** -- the fixture is the criterion's instrument, and an instrument that
disagrees with the world is the thing this project keeps catching.

<!-- ============ RECORD FACE -- does NOT travel to the worker ============ -->

<status>open</status>
<round>4</round>
<sub_round>A</sub_round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

<preflight>
comp-schedule: RUN at the round-4 cut -- 5 of 5 carriers, 17.328 s; REACHED-DENOMINATORS C1=23 C2=6 C3=12 C4=20 C5=335; GATES ARMED 25 (C1 7 + C2 6 + C3 12 POSITIVE_RESULT; C4/C5 are NOT-DECIDABLE and are listed, never counted). NOT COMPARABLE to round 3's '2 ARMED (G-3, G-7)': that figure named two gates this seat then judged relevant, this one is the tool's own POSITIVE_RESULT count over its five carriers. Stated as measured now rather than diffed against a number that counted something else. C3 MORATORIA denominator=12 is the one that touches this round and it is discharged in the cell, not here: C-MORATORIUM-CLEARED covers the code swap ONLY.
comp-iam: RUN at the round-4 cut (`comp-iam stats`) -- 195 IAM roles parsed, 188 services scanned (167 Lambda, 21 EC2), 1084 operations, 304 permission gaps. The tool's own NOTE at this run: TF role labels 'orchestrator' and 'scheduler' are reused across modules (astn-wsjft / estate-report / etfs-reports) and are now module-namespaced -- pre-fix this silently mis-linked inline policies into FALSE-MISSING. Recorded because `estate-report-*` appears in it and is explicitly OUT OF SCOPE for this round (a different directive, addendum s.5).
comp-adversary: RUN on NFRA_REPORT_DECOMP_R4.md at the cut (`comp-adversary compose ... --no-packet`), rc=0, validation_context_declaration produced. DECLARED EXCLUSIONS carried rather than hidden: (a) T11 decomposition-neighborhood NOT RESOLVED -- a decomposition carries no <decomp_ref>, so filesystem adjacency stood in as the neighborhood; (b) comp-blast/comp-trace CODE-graph expansion is not wired in v1, so the neighborhood is never a blast radius. A validator reading this round is told what the author's evidence context was NOT.
comp-iam BINDING: NONE. This cell writes one pure-python module that maps a dict its caller supplies; it performs no AWS call (AC5 refuses boto3 as it refuses any non-stdlib import), touches no role and no policy.
Ready root: no unmet dependency. Write surface disjoint from RP-s-21 (different file, different
deliverables folder), from RP-s-23 and from RP-s-24.
Z-S8 honoured by construction: the deliverable folder is derived from <issued_to> and is ~2/, not ~1/.
Worker grant verified at the cut: .owned-paths.yaml:44-47 worker_grant stanza PRESENT
(serial_glob 0.9.0_WK_*, source task-order-paths); .tools/owned-paths-validate.py --self-test
returns 0 of 14 arms failed. The grant reads a NON-TERMINAL order at HEAD, which is why this order
is committed with <status>open</status> in the issuance itself.
</preflight>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6, round 4) - **Project:** NFRA_REPORT - **Directive:** D12
**Authority chain:** Andrew-direct -> `1.0.0_SA_CTO~Z` L4 ADDENDUM 01 @`20c986bc70` -> L5 re-decomposition `org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R4.md` -> this issuance.
