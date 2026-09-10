# NFRA_REPORT.TO-RP-s-21 -- Port the edition engine into the Lambda, carrying no facts and no live reads

<!-- ============ WORKER FACE -- this is the WHOLE of the worker's context ============ -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R4.md</decomp_doc>
<owned_cells>RP-s-21</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~1</issued_to>

## THE CELL, INLINED IN FULL (outcomes FWD-13 structure limb, FWD-15 preservation limb)

The project built a SPECIMEN -- `compose_edition.py`, a worked proof of the edition FORMAT. It is
correct and it is the half that was hard. It also does **zero live reads**: its facts are `ROW_FACTS`,
a hard-coded list of hand-transcribed round-1 findings, and its own docstring says so.

**Your cell lifts the LOGIC out of that specimen and leaves the FACTS behind.**

Create `infra/aws/lambda/infrastructure_monitor/edition.py` containing, ported from
`org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/compose_edition.py`:

```
  compute_delta        (specimen :334-371)   compute_delta_watch  (specimen :374-385)
  compute_verdict      (specimen :388-396)   fmt_state            (specimen :399-408)
  gen_sentence         (specimen :411-417)   render_markdown      (specimen :420-545)
```

⛔ **`ROW_FACTS` DOES NOT TRAVEL. `main()` DOES NOT TRAVEL.** The module is pure functions over
arguments its caller supplies. It performs no AWS call, no HTTP call and no file read.

⛔ **THE ROW SHAPE IS FROZEN AND YOU MAY NOT CHANGE IT.** `render_markdown` must accept exactly the
row dicts the specimen's `ROW_FACTS` entries already are. A parallel cell (`RP-s-22`) is writing a
mapper against that shape RIGHT NOW, from the specimen at HEAD. **If you find you cannot port
`render_markdown` without changing the row shape, that is a surprise ROW and you STOP on the affected
criterion** -- do not change the shape and do not work around it.

## DEPENDENCIES

**NONE.** You are a ready root. `RP-s-22` runs beside you and writes a different file; you never read
or write its file and it never reads or writes yours.

## BOUNDS -- what this cell may not cross

- ⛔ **NO NEW DEPENDENCY AND NO NEW LAYER.** The deployed package is 40,015 bytes with
  `layers = [anthropic_sdk_deps]`. Your module must import only the Python 3.12 standard library.
  Third-party imports are refused by `AC5`.
- ⛔ **DO NOT EDIT `lambda_function.py`.** Wiring is `RP-s-23`'s cell, not yours. It is not in your paths.
- ⛔ **DO NOT EDIT the specimen `compose_edition.py`.** It is round 3's terminal deliverable and it is
  the oracle your port is graded against. It is not in your paths.
- ⛔ **NO ALARM, TOPIC, SUBSCRIPTION, SCHEDULE OR NOTIFICATION** may be minted. Andrew cleared this
  work as *"just swapping out the code of the existing lambda"* and that clearance covers nothing else.
- ⚠ **CENSUS FROM THE MAIN CHECKOUT, NEVER FROM YOUR WORKTREE.** A `comp-find` zero obtained inside a
  linked worktree is **not evidence of absence** -- the rail is blind to a linked worktree and returns
  a real-looking denominator over the wrong file set. `org/modules/graph/INSTRUMENT_LIMITS.md` LIMIT 4
  / 4a; ruled at msg 20822. If a criterion needs a census, run it from
  `C:/Users/Opal Bloomberg/Desktop/ajb_workspace`.
- ⚠ **NO NON-ASCII in code you write** -- `OK:` / `WARN:` / `ERROR:` / `SKIP:` / `BLOCKED:`. The
  rendered edition's own prose is the specimen's and travels as-is.

## BATTERY FINDINGS THAT TOUCH THIS CELL

`comp-surprise --project NFRA_REPORT` at the cut: 30 items, 0 duplicate ids, 0 malformed, **OPEN 0,
ARMED 0.** No armed hazard is carried into this round. If you surface one, append a row and keep working.

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/lambda/infrastructure_monitor/edition.py
org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-21.port-the-edition-engine-into-the-lambda.md
</paths>

READ-ONLY references you will need (do not write them):
`org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/compose_edition.py` (the source of the port),
`org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD_ADDENDUM_01.md`,
`org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R4.md`.

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

Your deliverable is `infra/aws/lambda/infrastructure_monitor/edition.py`, plus
`.../deliverables/0.9.0_WK_NFRA_REPORT~1/EDITION_PORT.md` recording what moved, what did not, and why.

## PROOF OF SPEC

⛔ **`AC2` IS THE CELL.** A port that imports cleanly and renders *something* is worth nothing; a port
that reproduces the specimen's own edition byte-for-byte from the specimen's own input is a proof that
nothing was lost in the move. Every other criterion guards a way that proof could be faked.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-21"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "import ast,sys;src=open('infra/aws/lambda/infrastructure_monitor/edition.py',encoding='utf-8').read();t=ast.parse(src);names={n.name for n in t.body if isinstance(n,(ast.FunctionDef,))};want={'compute_delta','compute_delta_watch','compute_verdict','fmt_state','gen_sentence','render_markdown'};print('DEFINED=%d of %d MISSING=%s' % (len(want&names),len(want),sorted(want-names)))"</invocation><expect>DEFINED=6 of 6 and MISSING=[] -- the module exists and defines all six ported functions at module level. This is the POSITIVE arm and it exists so no later criterion can pass on an absent file</expect></criterion>
  <!-- AC2 AMENDED by NFRA_REPORT-Z-S20 (2.0.0_SA_COO~ZZ, ISSUER RULING, commit 95b7d4ecd2220fdf8751028d7ee59694521b0bd8): the original AC2 below called compute_verdict()/render_markdown() directly on spec.ROW_FACTS, which never carries a "delta" key -- only main() (specimen :549-555, excluded by this cell's own bound) ever attached one. Reproduced against the UNMODIFIED SPECIMEN, independent of any port, by 0.9.0_WK_NFRA_REPORT~1 (surprise row NFRA_REPORT-Z-W1-S7): KeyError: 'delta'. UPHELD IN FULL, defect the issuer's. Recut below attaches delta via the PORT's OWN compute_delta/compute_delta_watch, over an independent deepcopy per side, before either side is rendered -- strictly stronger than the original (the original never called compute_delta or compute_delta_watch at all). -->
  <criterion id="AC2" cell_refs="RP-s-21"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 180 python -c "
import importlib.util,sys,copy
def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
spec=load('org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/compose_edition.py','spec_ce')
port=load('infra/aws/lambda/infrastructure_monitor/edition.py','port_ed')
def attach(rows,mod):
    for r in rows:
        if r['family']=='watch':
            d,n=mod.compute_delta_watch(r['prev'],r['curr'])
        else:
            d,n=mod.compute_delta(r['prev'],r['curr'])
        r['delta']=d;r['rule_note']='(%s)' % n
    return rows
a=attach(copy.deepcopy(spec.ROW_FACTS),port)
b=attach(copy.deepcopy(spec.ROW_FACTS),spec)
got=port.render_markdown(a,*port.compute_verdict(a),'PORT-FIDELITY-FIXED-VINTAGE')
want=spec.render_markdown(b,*spec.compute_verdict(b),'PORT-FIDELITY-FIXED-VINTAGE')
gl=[l for l in got.splitlines() if l.startswith('|')];wl=[l for l in want.splitlines() if l.startswith('|')]
print('SPEC_TABLE_LINES=%d PORT_TABLE_LINES=%d IDENTICAL=%s' % (len(wl),len(gl),got==want))
"</invocation><expect>SPEC_TABLE_LINES and PORT_TABLE_LINES are EQUAL and both greater than zero, and IDENTICAL=True -- fed the specimen's own rows at a fixed vintage, each side's delta attached independently via the PORT's own compute_delta/compute_delta_watch over an independent deepcopy (so neither module grades rows the other mutated), the ported module reproduces the specimen's edition exactly. AMENDED by NFRA_REPORT-Z-S20; see comment above</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-21"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "import ast;src=open('infra/aws/lambda/infrastructure_monitor/edition.py',encoding='utf-8').read();t=ast.parse(src);lits=[n for n in t.body if isinstance(n,ast.Assign) and any(isinstance(tg,ast.Name) and tg.id.isupper() and tg.id not in ('__all__',) for tg in n.targets) and isinstance(n.value,(ast.List,ast.Dict)) and len(ast.dump(n.value))>400];print('MODULE_LEVEL_DEFS=%d BIG_UPPERCASE_DATA_LITERALS=%d NAMES=%s' % (len(t.body),len(lits),[tg.id for n in lits for tg in n.targets]))"</invocation><expect>BIG_UPPERCASE_DATA_LITERALS=0 with MODULE_LEVEL_DEFS greater than zero -- no transcribed fact table travelled with the logic. C-NO-FROZEN-FACTS. The MODULE_LEVEL_DEFS denominator is printed so a zero over an unparsed file is visible</expect></criterion>
  <!-- AC4 AMENDED by NFRA_REPORT-Z-S20 (2.0.0_SA_COO~ZZ, ISSUER RULING, commit 95b7d4ecd2220fdf8751028d7ee59694521b0bd8): same defect, same fix as AC2 above -- base/mut carried no "delta" key so compute_verdict() raised KeyError: 'delta' before render_markdown was ever reached. Recut attaches delta via the port's own compute_delta/compute_delta_watch on each independently-deepcopied row list before rendering. Printed denominators (BASE_ROWS, MUT_ROWS, OUTPUTS_DIFFER) unchanged. -->
  <criterion id="AC4" cell_refs="RP-s-21"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "
import importlib.util,sys,copy
def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
spec=load('org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/compose_edition.py','spec_ce2')
port=load('infra/aws/lambda/infrastructure_monitor/edition.py','port_ed2')
def attach(rows,mod):
    for r in rows:
        if r['family']=='watch':
            d,n=mod.compute_delta_watch(r['prev'],r['curr'])
        else:
            d,n=mod.compute_delta(r['prev'],r['curr'])
        r['delta']=d;r['rule_note']='(%s)' % n
    return rows
base=attach(copy.deepcopy(spec.ROW_FACTS),port)
mut=attach(copy.deepcopy(spec.ROW_FACTS)[:1],port)
a=port.render_markdown(base,*port.compute_verdict(base),'V')
b=port.render_markdown(mut,*port.compute_verdict(mut),'V')
print('BASE_ROWS=%d MUT_ROWS=%d OUTPUTS_DIFFER=%s' % (len(base),len(mut),a!=b))
"</invocation><expect>BASE_ROWS greater than MUT_ROWS, both greater than zero, and OUTPUTS_DIFFER=True -- the renderer reads the rows it is GIVEN. This is the discrimination arm: a module that ignored its argument and printed a literal would pass AC2 and fail here</expect></criterion>
  <criterion id="AC5" cell_refs="RP-s-21"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "import ast,sys;src=open('infra/aws/lambda/infrastructure_monitor/edition.py',encoding='utf-8').read();t=ast.parse(src);mods=set()
for n in ast.walk(t):
    if isinstance(n,ast.Import):
        for a in n.names: mods.add(a.name.split('.')[0])
    elif isinstance(n,ast.ImportFrom):
        if n.module: mods.add(n.module.split('.')[0])
std=set(sys.stdlib_module_names);bad=sorted(m for m in mods if m not in std)
print('IMPORTS=%d NON_STDLIB=%d NAMES=%s' % (len(mods),len(bad),bad))"</invocation><expect>NON_STDLIB=0 and NAMES=[] with IMPORTS printed as the denominator -- no third-party import, so no new dependency and no layer change. boto3 and requests are equally refused here: this module performs no live read</expect></criterion>
  <criterion id="AC6" cell_refs="RP-s-21"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "src=open('infra/aws/lambda/infrastructure_monitor/edition.py',encoding='utf-8').read();bad=[(i+1,l) for i,l in enumerate(src.splitlines()) if any(ord(c)>126 for c in l)];print('LINES=%d NON_ASCII_LINES=%d FIRST=%s' % (len(src.splitlines()),len(bad),bad[:2]))"</invocation><expect>NON_ASCII_LINES=0 with LINES printed as the denominator -- production code carries no non-ASCII</expect></criterion>
</proof_of_spec>

### What each criterion means

- **AC1** (POSITIVE, structural): the module exists and defines all six functions -- the arm that stops every other criterion passing on an absent file
- **AC2** (PORT FIDELITY, the cell): fed the specimen's own rows, the port reproduces the specimen's edition exactly
- **AC3** (NEGATIVE, C-NO-FROZEN-FACTS): no transcribed fact table came across with the logic
- **AC4** (DISCRIMINATION): a smaller row list produces different output -- the renderer reads its argument
- **AC5** (DEPLOYABILITY): stdlib only, so no new dependency and no layer change
- **AC6** (LAW): no non-ASCII in production code

### THE RED ARM -- exercised against the world BEFORE this order was issued

```
AC1  DEFINED=0 of 6, file absent                    FAILS  (expect 6 of 6)
AC2  ModuleNotFoundError on the port                FAILS  (expect IDENTICAL=True)
AC3  unparseable, file absent                       FAILS  -- and this is why AC1 exists:
                                                    AC3 alone would read 0 literals on an
                                                    absent file and PASS VACUOUSLY
AC4  ModuleNotFoundError on the port                FAILS  (expect OUTPUTS_DIFFER=True)
AC5  unparseable, file absent                       FAILS  -- same vacuity trap, same guard
AC6  unreadable, file absent                        FAILS  -- same vacuity trap, same guard
```

⚠ **THREE OF THE SIX ARE ABSENCE-SATISFIABLE AND THAT IS STATED RATHER THAN HIDDEN.** `AC3`, `AC5`
and `AC6` all measure "there is none of the bad thing", which an empty file satisfies perfectly. `AC1`
is their positive control and every one of them prints a denominator, so a zero over nothing is
visible. This is the `AC4`-vacuity lesson from round 3 applied at the cut instead of after it.

<!-- ============ RECORD FACE -- does NOT travel to the worker ============ -->

<status>complete</status>
<round>4</round>
<sub_round>A</sub_round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

<preflight>
comp-schedule: RUN at the round-4 cut -- 5 of 5 carriers, 17.328 s; REACHED-DENOMINATORS C1=23 C2=6 C3=12 C4=20 C5=335; GATES ARMED 25 (C1 7 + C2 6 + C3 12 POSITIVE_RESULT; C4/C5 are NOT-DECIDABLE and are listed, never counted). NOT COMPARABLE to round 3's '2 ARMED (G-3, G-7)': that figure named two gates this seat then judged relevant, this one is the tool's own POSITIVE_RESULT count over its five carriers. Stated as measured now rather than diffed against a number that counted something else. C3 MORATORIA denominator=12 is the one that touches this round and it is discharged in the cell, not here: C-MORATORIUM-CLEARED covers the code swap ONLY.
comp-iam: RUN at the round-4 cut (`comp-iam stats`) -- 195 IAM roles parsed, 188 services scanned (167 Lambda, 21 EC2), 1084 operations, 304 permission gaps. The tool's own NOTE at this run: TF role labels 'orchestrator' and 'scheduler' are reused across modules (astn-wsjft / estate-report / etfs-reports) and are now module-namespaced -- pre-fix this silently mis-linked inline policies into FALSE-MISSING. Recorded because `estate-report-*` appears in it and is explicitly OUT OF SCOPE for this round (a different directive, addendum s.5).
comp-adversary: RUN on NFRA_REPORT_DECOMP_R4.md at the cut (`comp-adversary compose ... --no-packet`), rc=0, validation_context_declaration produced. DECLARED EXCLUSIONS carried rather than hidden: (a) T11 decomposition-neighborhood NOT RESOLVED -- a decomposition carries no <decomp_ref>, so filesystem adjacency stood in as the neighborhood; (b) comp-blast/comp-trace CODE-graph expansion is not wired in v1, so the neighborhood is never a blast radius. A validator reading this round is told what the author's evidence context was NOT.
comp-iam BINDING: NONE. This cell writes one pure-python module with no AWS surface, no role and no policy; the 304 gaps do not touch it and are recorded for the denominator only.
Ready root: no unmet dependency. Write surface disjoint from RP-s-22 (different file), from RP-s-23
(does not touch lambda_function.py or terraform) and from RP-s-24.
Worker grant verified at the cut: .owned-paths.yaml:44-47 carries the worker_grant stanza
(serial_glob 0.9.0_WK_*, source task-order-paths) and .tools/owned-paths-validate.py --self-test
returns 0 of 14 arms failed with "REGISTRY worker_grant stanza: PRESENT". The grant reads a
NON-TERMINAL order at HEAD, which is why this order is committed with <status>open</status> in the
issuance itself -- a terminal order grants nothing.
</preflight>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6, round 4) - **Project:** NFRA_REPORT - **Directive:** D12
**Authority chain:** Andrew-direct -> `1.0.0_SA_CTO~Z` L4 ADDENDUM 01 @`20c986bc70` -> L5 re-decomposition `org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R4.md` -> this issuance.
