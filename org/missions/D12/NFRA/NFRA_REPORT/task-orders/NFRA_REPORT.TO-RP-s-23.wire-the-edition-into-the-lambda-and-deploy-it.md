# NFRA_REPORT.TO-RP-s-23 -- Wire the edition into the Lambda and deploy it on the Terraform path

<!-- ============ WORKER FACE -- this is the WHOLE of the worker's context ============ -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R4.md</decomp_doc>
<owned_cells>RP-s-23</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~3</issued_to>

## THE CELL, INLINED IN FULL (outcomes FWD-13 deployed limb, FWD-14 deployed limb)

`RP-s-21` produced `edition.py` (the render logic, no facts). `RP-s-22` produced `edition_rows.py`
(the collector-output mapper). **Your cell joins them to the running function and ships it.**

**THE ONE LINE THAT CHANGES**, at `infra/aws/lambda/infrastructure_monitor/lambda_function.py:267`:

```
  now      email_body = format_report(report)
  becomes  rows, omissions = edition_rows.rows_from_report(report, _load_prior_report())

           # THE DELTA-ATTACH LOOP -- the CALLER's, and it is not optional.
           for r in rows:
               if r["family"] == "watch":
                   delta, note = edition.compute_delta_watch(r["prev"], r["curr"])
               else:
                   delta, note = edition.compute_delta(r["prev"], r["curr"])
               r["delta"] = delta
               r["rule_note"] = "(%s)" % note

           needs_andrew, breach_rows, worse_rows = edition.compute_verdict(rows)
           email_body = edition.render_markdown(rows, needs_andrew, breach_rows, worse_rows, <vintage>)
```

CORRECTED BY ISSUER RULING `NFRA_REPORT-Z-S20`, ADJUDICATING WORKER ROW `Z-W1-S7`. **This order's
first draft showed three lines and omitted the loop.** `edition.compute_verdict` reads `r["delta"]`
directly and `rows_from_report` does not attach it -- so without the loop the handler raises
`KeyError: 'delta'` on the first real invocation. The loop is the specimen's own, at
`compose_edition.py:549-555`, and it lives in the CALLER by design: `edition.py` is pure functions
over arguments, `edition_rows.py` is a mapper, and **composing them is this cell's job.**

`send_email(email_body, report)` at :270 is **unchanged**. `archive_report` and `publish_status_feed`
are **unchanged**. You are replacing a renderer, not a pipeline.

⚠ **`format_report` (:2023-2462, 439 lines) IS NOT DELETED IN THIS CELL.** `RP-s-24` compares the new
edition against the old one and needs the old renderer reachable to produce a reference rendering.
Leave it in place, unreferenced by `lambda_handler`. Removing it is a later act, not yours.

**THEN DEPLOY IT**, and the path is not negotiable:

```
  C-DEPLOY-PATH -- infra-monitor.tf:7 says it in the Terraform itself
  package  ->  s3://opal-<account>-lambda-artifacts/shared-infra/opal-infrastructure-monitor.zip
           ->  source_code_hash reads the object's metadata["content-sha256"]
           ->  safe-apply at infra/aws/terraform/shared-infra/infra-monitor.tf
               resource aws_lambda_function.infra_monitor
```

⛔ **NEVER `aws lambda update-function-code`.** It is a NEVER-class law line and this function's own
Terraform names it. ⛔ **NEVER bare `terraform apply`** -- `safe-apply` only.

## DEPENDENCIES

**RP-s-21 AND RP-s-22, both.** You are seated only when both are terminal with valid proof instances
at HEAD. Do not begin before your issuer hands you this order.

## BOUNDS -- what this cell may not cross

- ⛔ **THE ARTIFACT IS LAYER-SHAPED AND 40 KB, NOT THE FOLDER.** Measured at the cut:
  `CodeSize 40,015` with `layers = [anthropic_sdk_deps]` (`infra-monitor.tf:53`). The source folder
  `infra/aws/lambda/infrastructure_monitor/` ALSO contains vendored packages (`anyio/`, `httpx/`,
  `certifi/`, `pydantic`, ...) that belong to the LAYER. **A `zip -r .` of that directory ships a
  package that shadows the layer and bears no resemblance to what runs today.** Package the function
  modules only, and let the deployed CodeSize be your check.
- ⛔ **`C-CHANGE-LEDGER`, AND IT OPENS BEFORE YOUR FIRST DEPLOY ACT.** An entry under
  `org/critical_paths/change_management/` naming this change, opened before the first S3 put or apply,
  **closed in this same cell**. ⛔ NEVER-2: a confirmed deploy is never left half-landed -- finish in
  session or roll back and escalate loudly.
- ⛔ **NO ALARM, TOPIC, SUBSCRIPTION, SCHEDULE OR NOTIFICATION.** Andrew's clearance is verbatim
  *"this isnt creating an alarm, it is just swapping out the code of the existing lambda"* and it
  covers this swap and nothing else. The EventBridge rule, the SES identity and the recipient list are
  untouched.
- ⛔ **DO NOT CHANGE THE SCHEDULE, THE RECIPIENT OR THE DELIVERY PATH.** One morning email, same
  schedule, same recipient (addendum §5).
- ⚠ **DO NOT EDIT `edition.py` OR `edition_rows.py`.** They are `RP-s-21`'s and `RP-s-22`'s
  deliverables and are not in your paths. If one of them is wrong, that is a surprise ROW and you STOP.
- ⚠ **CENSUS FROM THE MAIN CHECKOUT, NEVER FROM YOUR WORKTREE** (`INSTRUMENT_LIMITS.md` LIMIT 4 / 4a).
- ⚠ **NO NON-ASCII in code, logs or anything reaching AWS.**

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/lambda/infrastructure_monitor/lambda_function.py
infra/aws/terraform/shared-infra/infra-monitor.tf
org/critical_paths/change_management/
org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~3/
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-23.wire-the-edition-into-the-lambda-and-deploy-it.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

⛔ **EVERY CRITERION BELOW SCORES THE DEPLOYED PACKAGE, NOT THE SOURCE.** The addendum §6 directs this
and it is not a generic caution: **a grep of the repo would pass while the shipped zip still carried a
frozen fact list.** This is the same rendered-vs-source trap that resized round 3, one layer down.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-23"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 180 .tools/aws lambda get-function-configuration --function-name opal-infrastructure-monitor --query '{Sha:CodeSha256,LM:LastModified,Size:CodeSize}' --output json</invocation><expect>Sha is NOT r/bjjp5dJMcxw4NnzSNFsUCpYlWrH+sJsVJu+JiWxs8= AND LM is NOT 2026-07-08T01:29:08.000+0000 -- both differ from the pre-state measured at the cut. A deploy that changed nothing reproduces both exactly, which is what makes this a criterion rather than a report</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-23"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 300 bash -c 'D=$(mktemp -d) && .tools/aws lambda get-function --function-name opal-infrastructure-monitor --query Code.Location --output text > "$D/u" && curl -s -o "$D/f.zip" "$(cat "$D/u")" && python -c "
import zipfile,sys
z=zipfile.ZipFile(sys.argv[1]); names=z.namelist()
want=[\"edition.py\",\"edition_rows.py\",\"lambda_function.py\"]
have=[w for w in want if any(n==w or n.endswith(\"/\"+w) for n in names)]
print(\"ENTRIES=%d PRESENT=%d of %d MISSING=%s\" % (len(names),len(have),len(want),[w for w in want if w not in have]))
" "$D/f.zip"'</invocation><expect>PRESENT=3 of 3 and MISSING=[] with ENTRIES printed as the denominator -- the DEPLOYED package actually contains both new modules alongside the handler. This downloads what AWS is serving; it does not read the repo</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-23"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 300 bash -c 'D=$(mktemp -d) && .tools/aws lambda get-function --function-name opal-infrastructure-monitor --query Code.Location --output text > "$D/u" && curl -s -o "$D/f.zip" "$(cat "$D/u")" && python -c "
import zipfile,sys,re
z=zipfile.ZipFile(sys.argv[1]); names=z.namelist()
pys=[n for n in names if n.endswith(\".py\")]
hits=[]
for n in pys:
    t=z.read(n).decode(\"utf-8\",\"replace\")
    if re.search(r\"ROW_FACTS\", t): hits.append(n)
print(\"PY_ENTRIES=%d ROW_FACTS_CARRIERS=%d NAMES=%s\" % (len(pys),len(hits),hits))
" "$D/f.zip"'</invocation><expect>ROW_FACTS_CARRIERS=0 with PY_ENTRIES greater than zero as the denominator -- FWD-14 scored where it must be scored: the transcribed fact list is absent from the DEPLOYED package. The PY_ENTRIES denominator is load-bearing: a zero over an empty or unreadable zip would otherwise pass vacuously</expect></criterion>
  <criterion id="AC4" cell_refs="RP-s-23"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "import re;src=open('infra/aws/lambda/infrastructure_monitor/lambda_function.py',encoding='utf-8').read();fr=len(re.findall(r'email_body\s*=\s*format_report\(',src));rm=len(re.findall(r'render_markdown\(',src));df=len(re.findall(r'def format_report\(',src));da=len(re.findall(r'\[.delta.\]\s*=',src));cd=len(re.findall(r'compute_delta(_watch)?\(',src));print('HANDLER_CALLS_format_report=%d HANDLER_CALLS_render_markdown=%d format_report_STILL_DEFINED=%d DELTA_ATTACHED=%d COMPUTE_DELTA_CALLS=%d' % (fr,rm,df,da,cd))"</invocation><expect>HANDLER_CALLS_format_report=0 AND HANDLER_CALLS_render_markdown of 1 or greater AND format_report_STILL_DEFINED=1 AND DELTA_ATTACHED of 1 or greater AND COMPUTE_DELTA_CALLS of 2 or greater -- the handler is rewired, the old renderer survives for RP-s-24, AND the delta-attach loop is present calling BOTH compute_delta and compute_delta_watch. The last two numbers were ADDED by issuer ruling NFRA_REPORT-Z-S20: without the loop the handler raises KeyError 'delta' on its first real run, and the original three-number form could not see that</expect></criterion>
  <criterion id="AC5" cell_refs="RP-s-23"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 bash -c 'ls org/critical_paths/change_management/*infra-monitor*edition* 2>/dev/null | wc -l && grep -l -i "closed\|COMPLETE" org/critical_paths/change_management/*infra-monitor*edition* 2>/dev/null | wc -l'</invocation><expect>the first count is 1 or greater AND the second equals the first -- a change-management entry for this deploy exists and every one found is closed. C-CHANGE-LEDGER and NEVER-2: an entry left open is a half-landed deploy by definition</expect></criterion>
  <criterion id="AC6" cell_refs="RP-s-23"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 grep -c -i 'update-function-code' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~3/DEPLOY.md</invocation><expect>a count of 0 -- the deploy record does not contain the forbidden verb anywhere, including in a transcript of a command that was tried. If the deploy was attempted that way at any point, this criterion is the place it becomes visible rather than a thing only the worker knows</expect></criterion>
</proof_of_spec>

### What each criterion means

- **AC1** (DEPLOYED, DISCRIMINATING): the artifact actually moved off its 2026-07-08 pre-state
- **AC2** (DEPLOYED PACKAGE): the shipped zip carries both new modules -- downloaded from AWS, not read from the repo
- **AC3** (DEPLOYED PACKAGE, FWD-14's real bar): no `ROW_FACTS` in what ships
- **AC4** (SOURCE, WIRING + PRESERVATION): the handler is rewired and the old renderer survives for `RP-s-24`
- **AC5** (LEDGER): a change-management entry exists and is closed
- **AC6** (LAW, NEGATIVE): the forbidden deploy verb appears nowhere in the deploy record

### THE RED ARM -- exercised against the world BEFORE this order was issued

```
AC1  Sha=r/bjjp5dJMcxw4NnzSNFsUCpYlWrH+sJsVJu+JiWxs8=
     LM =2026-07-08T01:29:08.000+0000  Size=40015          FAILS -- both match the
                                                           forbidden pre-state exactly.
                                                           A LIVE, MEANINGFUL red arm:
                                                           this is the deployed truth today.
AC2  the deployed zip predates both modules                FAILS  (expect PRESENT=3 of 3)
AC3  not run at the cut -- would require downloading the   NOT RUN, and stated: its pre-state
     artifact to prove a negative about the OLD package    is uninteresting (the old package
                                                           has no ROW_FACTS either, because it
                                                           has no edition code at all). ITS
                                                           DENOMINATOR IS THE GUARD, not a
                                                           red arm.
AC4  HANDLER_CALLS_format_report=1                         FAILS  (expect 0)
     HANDLER_CALLS_render_markdown=0                       FAILS  (expect >=1)
     format_report_STILL_DEFINED=1                         passes -- by design, and it must
                                                           STILL pass at the end
AC5  no entry exists                                       FAILS  (expect >=1, all closed)
AC6  no DEPLOY.md exists                                   FAILS  (grep on a missing file)
```

⭐ **`AC1` IS THE ONE THAT MATTERS AND IT WAS READ LIVE, NOT ASSUMED.** The pre-state above is what
`aws lambda get-function-configuration` returned at the cut. A criterion whose pre-state was never
measured cannot tell a real deploy from a no-op.

<!-- ============ RECORD FACE -- does NOT travel to the worker ============ -->

<status>open</status>
<round>4</round>
<sub_round>B</sub_round>
<slot>~3</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

<preflight>
SEATED 2026-09-10 ~15:40Z. Both dependencies are TERMINAL AND VERIFIED AT HEAD: RP-s-21 drained
@4e9d016fae (edition.py, 258 lines), RP-s-22 drained @30b690d33a (edition_rows.py, 548 lines); both
task orders read <status>complete</status> at HEAD; both proof instances VALID rc=0 read by their own
WORKTREE's checker, not by their author's report; both worktrees and branches reaped, 0 wk- branches.
ISSUER PRE-FLIGHT RUN BEFORE SEATING -- THE JOIN THE PARALLEL CUT RISKED, EXERCISED END TO END in the
main checkout against a synthetic 13-section report:
  rows_from_report      -> rows=10 omissions=3
  delta-attach loop     -> OK, 10 rows annotated (edition.compute_delta / compute_delta_watch)
  compute_verdict       -> needs_andrew=False breach=0 worse=0
  render_markdown       -> 9,984 chars, 19 table lines
The two cells COMPOSE. This cell is wiring, packaging and deploying -- not debugging an interface.
The frozen row shape held, which was the one assumption DECOMP_R4 s.1a named as able to fail.
comp-schedule: RUN at the round-4 cut -- 5 of 5 carriers, 17.328 s; REACHED-DENOMINATORS C1=23 C2=6 C3=12 C4=20 C5=335; GATES ARMED 25 (C1 7 + C2 6 + C3 12 POSITIVE_RESULT; C4/C5 are NOT-DECIDABLE and are listed, never counted). NOT COMPARABLE to round 3's '2 ARMED (G-3, G-7)': that figure named two gates this seat then judged relevant, this one is the tool's own POSITIVE_RESULT count over its five carriers. Stated as measured now rather than diffed against a number that counted something else. C3 MORATORIA denominator=12 is the one that touches this round and it is discharged in the cell, not here: C-MORATORIUM-CLEARED covers the code swap ONLY.
comp-iam: RUN at the round-4 cut (`comp-iam stats`) -- 195 IAM roles parsed, 188 services scanned (167 Lambda, 21 EC2), 1084 operations, 304 permission gaps. The tool's own NOTE at this run: TF role labels 'orchestrator' and 'scheduler' are reused across modules (astn-wsjft / estate-report / etfs-reports) and are now module-namespaced -- pre-fix this silently mis-linked inline policies into FALSE-MISSING. Recorded because `estate-report-*` appears in it and is explicitly OUT OF SCOPE for this round (a different directive, addendum s.5).
comp-adversary: RUN on NFRA_REPORT_DECOMP_R4.md at the cut (`comp-adversary compose ... --no-packet`), rc=0, validation_context_declaration produced. DECLARED EXCLUSIONS carried rather than hidden: (a) T11 decomposition-neighborhood NOT RESOLVED -- a decomposition carries no <decomp_ref>, so filesystem adjacency stood in as the neighborhood; (b) comp-blast/comp-trace CODE-graph expansion is not wired in v1, so the neighborhood is never a blast radius. A validator reading this round is told what the author's evidence context was NOT.
comp-iam BINDING: READ, AND THE ANSWER IS THAT THIS CELL ADDS NO PERMISSION. The deploy changes CODE only -- the function's execution role, its policies and its layer are untouched by this cell, so none of the 304 gaps is opened or closed by it. If the ported code needs a permission the current role lacks, that is a SURPRISE ROW and a STOP, never a policy edit under this order: no IAM path is in this cell's <paths>.
BLOCKED on RP-s-21 AND RP-s-22. Issued in the SAME issuance per rule 27 (one issuance covering every
cell); the worker is seated when both dependencies are terminal with valid proof instances at HEAD,
with NO second issuance.
NOTE, stated rather than discovered: 'blocked' is not in the owned-paths validator's
_TERMINAL_TO_WORDS (:128), so this order's <paths> grant is LIVE at HEAD from the moment it commits
even though no worker is seated on it. Harmless -- a grant nobody holds admits nobody -- but it means
the grant's existence is not evidence that this cell has started.
This cell performs a WORLD ACT (a deploy to the function that emails Andrew every weekday). It is
authorized: Andrew-direct, verbatim, 'wire it up so tomorrow's email is the new one'. No approval
gate is invented here and none is implied.
</preflight>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6, round 4) - **Project:** NFRA_REPORT - **Directive:** D12
**Authority chain:** Andrew-direct -> `1.0.0_SA_CTO~Z` L4 ADDENDUM 01 @`20c986bc70` -> L5 re-decomposition `org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R4.md` -> this issuance.
