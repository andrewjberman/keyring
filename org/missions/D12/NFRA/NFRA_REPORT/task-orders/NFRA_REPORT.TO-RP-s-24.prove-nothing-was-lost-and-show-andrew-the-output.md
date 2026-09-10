# NFRA_REPORT.TO-RP-s-24 -- Prove nothing a reader relies on was lost, and put the output in front of Andrew

<!-- ============ WORKER FACE -- this is the WHOLE of the worker's context ============ -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R4.md</decomp_doc>
<owned_cells>RP-s-24</owned_cells>
</decomp_ref>
<issued_by>2.0.0_SA_COO~ZZ</issued_by>
<issued_to>0.9.0_WK_NFRA_REPORT~4</issued_to>

## THE CELL, INLINED IN FULL (outcomes FWD-15, FWD-13 manual-trigger limb)

The new edition is deployed. **Your cell proves nothing a reader relies on disappeared in the swap,
and puts the output where Andrew can see it without waiting for 9 AM.**

**PART ONE -- THE BEFORE/AFTER, over the real denominator of 13.**

The old renderer `format_report` is still defined in `lambda_function.py` (`RP-s-23` was forbidden
from deleting it, precisely so you have a reference). The archive holds real prior reports:
`_load_prior_report()` (`lambda_function.py:775-792`) reads the most recent one from S3, and
`archive_report()` (:2567-2581) is what wrote it.

Produce a named comparison covering all **13** collector sections:

```
   1 lambda_health        5 producer_drift      9 aws_costs        13 openai_cost
   2 smartx_pipeline      6 sns_egress         10 cost_depth
   3 data_freshness       7 graph_head         11 security_sweep
   4 deploy_drift         8 contract_integrity 12 ai_analysis
```

Each section is exactly one of:

```
  PRESENT      -- it appears in the new edition
  REMOVED      -- it does not, AND the reason is recorded
  CONDITIONAL  -- ai_analysis is None when lambda_health.functions_with_errors == 0.
                  ABSENT-BY-DESIGN is not a removal and must not be recorded as one
```

⛔ **NO SECTION MAY VANISH SILENTLY.** That is the whole of `FWD-15` and the whole of `C-NO-REGRESSION`.

**PART TWO -- THE MANUAL TRIGGER.** Andrew asked to see the output without waiting for 9 AM:
*"wire it up so tomorrow's email is the new one, then run a manual trigger so i can see the output."*
Invoke the DEPLOYED function once and capture what it produced.

⛔ **THE MANUAL INVOCATION IS QA. THE SCHEDULED FIRE REMAINS THE ACCEPTANCE** (`C-MANUAL-TRIGGER`).
Nothing you do here grades `FWD-13` REALIZED. **A cell can produce the edition; it cannot produce the
reading**, and the reading is Andrew's.

## DEPENDENCIES

**RP-s-23.** You are seated only when it is terminal with a valid proof instance at HEAD and the
deployed artifact has moved off its pre-state.

## BOUNDS -- what this cell may not cross

- ⛔ **DO NOT EDIT `lambda_function.py`, `edition.py`, `edition_rows.py` OR ANY TERRAFORM.** You are
  measuring what was shipped, not changing it. None of them is in your paths. If the comparison finds
  a real regression, that is a surprise ROW and a finding for the issuer -- **not a fix you make**.
- ⛔ **DO NOT SEND ANDREW AN EMAIL, AND DO NOT ADD A RECIPIENT.** The function's own send path is the
  only delivery, it already exists, and it is untouched. Your output is a file and a captured
  invocation result.
- ⛔ **NO ALARM, TOPIC, SUBSCRIPTION, SCHEDULE OR NOTIFICATION.** Andrew's clearance covers the code
  swap and nothing else.
- ⛔ **NEVER `aws lambda update-function-code`; NEVER bare `terraform apply`.**
- ⚠ **A MANUAL INVOCATION OF THE REAL FUNCTION SENDS THE REAL EMAIL.** That is intended -- Andrew
  asked for it -- but it is a world act and it happens ONCE. Do not loop it, and record the invocation
  id and timestamp so a later reader can tell your run from the scheduled one.
- ⚠ **CENSUS FROM THE MAIN CHECKOUT, NEVER FROM YOUR WORKTREE** (`INSTRUMENT_LIMITS.md` LIMIT 4 / 4a).
- ⚠ **NO NON-ASCII in anything reaching AWS or a log.**

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~4/
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-24.prove-nothing-was-lost-and-show-andrew-the-output.md
</paths>

Your deliverables are `.../deliverables/0.9.0_WK_NFRA_REPORT~4/BEFORE_AFTER.md` (the 13-section
comparison with its denominator) and `.../MANUAL_TRIGGER.md` (the invocation, its id, its timestamp,
and the rendered body it produced).

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-24"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "
import re
t=open('org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~4/BEFORE_AFTER.md',encoding='utf-8').read()
K=['lambda_health','smartx_pipeline','data_freshness','deploy_drift','producer_drift','sns_egress','graph_head','contract_integrity','aws_costs','cost_depth','security_sweep','ai_analysis','openai_cost']
named=[k for k in K if re.search(r'\b'+re.escape(k)+r'\b',t)]
print('SECTIONS=%d NAMED=%d MISSING=%s' % (len(K),len(named),[k for k in K if k not in named]))
"</invocation><expect>SECTIONS=13 and NAMED=13 and MISSING=[] -- the comparison names every collector section by its own key, so no section is skipped by being forgotten rather than judged</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-24"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "
import re
t=open('org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~4/BEFORE_AFTER.md',encoding='utf-8').read()
K=['lambda_health','smartx_pipeline','data_freshness','deploy_drift','producer_drift','sns_egress','graph_head','contract_integrity','aws_costs','cost_depth','security_sweep','ai_analysis','openai_cost']
verdicts={}
for line in t.splitlines():
    for k in K:
        if re.search(r'\b'+re.escape(k)+r'\b',line):
            for v in ('PRESENT','REMOVED','CONDITIONAL'):
                if v in line: verdicts.setdefault(k,set()).add(v)
one=[k for k in K if len(verdicts.get(k,()))==1]
none_=[k for k in K if not verdicts.get(k)]
many=[k for k in K if len(verdicts.get(k,()))>1]
print('SECTIONS=%d EXACTLY_ONE_VERDICT=%d NO_VERDICT=%s AMBIGUOUS=%s' % (len(K),len(one),none_,many))
"</invocation><expect>EXACTLY_ONE_VERDICT=13 with NO_VERDICT=[] and AMBIGUOUS=[] -- every section carries exactly one of PRESENT / REMOVED / CONDITIONAL. A section with none was never judged; a section with two was judged twice and neither reading governs</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-24"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "
import re
t=open('org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~4/BEFORE_AFTER.md',encoding='utf-8').read()
lines=[l for l in t.splitlines() if 'REMOVED' in l]
noreason=[l for l in lines if not re.search(r'(reason|because|REASON)',l,re.I)]
print('REMOVED_LINES=%d WITHOUT_REASON=%d' % (len(lines),len(noreason)))
"</invocation><expect>WITHOUT_REASON=0, with REMOVED_LINES printed as the denominator -- FWD-15's bar exactly: a section may be removed, but never silently. REMOVED_LINES=0 is a legitimate pass and the denominator makes it visible that nothing was removed rather than nothing checked</expect></criterion>
  <criterion id="AC4" cell_refs="RP-s-24"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 120 python -c "
import re
t=open('org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~4/MANUAL_TRIGGER.md',encoding='utf-8').read()
req=len(re.findall(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',t))
ts=len(re.findall(r'20\d\d-\d\d-\d\dT\d\d:\d\d',t))
body=len(re.findall(r'^\|',t,re.M))
print('REQUEST_IDS=%d TIMESTAMPS=%d RENDERED_TABLE_LINES=%d' % (req,ts,body))
"</invocation><expect>REQUEST_IDS of 1 or greater AND TIMESTAMPS of 1 or greater AND RENDERED_TABLE_LINES of 1 or greater -- the manual invocation is recorded with an id and a timestamp so a later reader can tell it from the scheduled fire, and the body it produced carries the edition's row table rather than a claim that it did</expect></criterion>
  <criterion id="AC5" cell_refs="RP-s-24"><invocation>cd "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" && timeout 180 .tools/aws lambda get-function-configuration --function-name opal-infrastructure-monitor --query '{Sha:CodeSha256,LM:LastModified}' --output json</invocation><expect>Sha is NOT r/bjjp5dJMcxw4NnzSNFsUCpYlWrH+sJsVJu+JiWxs8= AND LM is NOT 2026-07-08T01:29:08.000+0000 -- re-read INDEPENDENTLY of RP-s-23's own claim. A producer's self-report is never the oracle: this cell verifies against the live plane that what it is comparing is in fact the new deployment</expect></criterion>
</proof_of_spec>

### What each criterion means

- **AC1** (COVERAGE, DENOMINATOR PRINTED): all 13 sections are named in the comparison
- **AC2** (PARTITION, EXHAUSTIVE AND UNAMBIGUOUS): each gets exactly one verdict
- **AC3** (FWD-15's bar): no silent removal
- **AC4** (EVIDENCE OF THE ACT): the manual trigger is recorded with id, timestamp and the body produced
- **AC5** (INDEPENDENT RE-READ): the deployment is verified from the live plane, not from `RP-s-23`'s report

### THE RED ARM -- exercised against the world BEFORE this order was issued

```
AC1  BEFORE_AFTER.md absent                         FAILS
AC2  BEFORE_AFTER.md absent                         FAILS
AC3  BEFORE_AFTER.md absent                         FAILS  -- and note it would read
                                                    REMOVED_LINES=0 WITHOUT_REASON=0
                                                    on an EMPTY file and PASS VACUOUSLY;
                                                    AC1 and AC2 are its positive controls
AC4  MANUAL_TRIGGER.md absent                       FAILS
AC5  Sha=r/bjjp5dJMcxw4NnzSNFsUCpYlWrH+sJsVJu+JiWxs8=
     LM =2026-07-08T01:29:08.000+0000               FAILS -- a LIVE red arm; this is the
                                                    deployed truth today and it must move
```

<!-- ============ RECORD FACE -- does NOT travel to the worker ============ -->

<status>blocked</status>
<round>4</round>
<sub_round>C</sub_round>
<slot>~4</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

<preflight>
comp-schedule: RUN at the round-4 cut -- 5 of 5 carriers, 17.328 s; REACHED-DENOMINATORS C1=23 C2=6 C3=12 C4=20 C5=335; GATES ARMED 25 (C1 7 + C2 6 + C3 12 POSITIVE_RESULT; C4/C5 are NOT-DECIDABLE and are listed, never counted). NOT COMPARABLE to round 3's '2 ARMED (G-3, G-7)': that figure named two gates this seat then judged relevant, this one is the tool's own POSITIVE_RESULT count over its five carriers. Stated as measured now rather than diffed against a number that counted something else. C3 MORATORIA denominator=12 is the one that touches this round and it is discharged in the cell, not here: C-MORATORIUM-CLEARED covers the code swap ONLY.
comp-iam: RUN at the round-4 cut (`comp-iam stats`) -- 195 IAM roles parsed, 188 services scanned (167 Lambda, 21 EC2), 1084 operations, 304 permission gaps. The tool's own NOTE at this run: TF role labels 'orchestrator' and 'scheduler' are reused across modules (astn-wsjft / estate-report / etfs-reports) and are now module-namespaced -- pre-fix this silently mis-linked inline policies into FALSE-MISSING. Recorded because `estate-report-*` appears in it and is explicitly OUT OF SCOPE for this round (a different directive, addendum s.5).
comp-adversary: RUN on NFRA_REPORT_DECOMP_R4.md at the cut (`comp-adversary compose ... --no-packet`), rc=0, validation_context_declaration produced. DECLARED EXCLUSIONS carried rather than hidden: (a) T11 decomposition-neighborhood NOT RESOLVED -- a decomposition carries no <decomp_ref>, so filesystem adjacency stood in as the neighborhood; (b) comp-blast/comp-trace CODE-graph expansion is not wired in v1, so the neighborhood is never a blast radius. A validator reading this round is told what the author's evidence context was NOT.
comp-iam BINDING: READ-ONLY. This cell invokes an existing function once and reads artifacts; it grants nothing and edits no policy. A permission failure surfacing during the manual invocation is a FINDING for the issuer (a surprise ROW), not something this cell fixes.
BLOCKED on RP-s-23. Issued in the SAME issuance per rule 27; the worker is seated when RP-s-23 is
terminal with a valid proof instance at HEAD, with NO second issuance.
'blocked' is non-terminal in the owned-paths validator (:128), so this order's grant is live at HEAD
before its worker is seated -- stated in RP-s-23's preflight too, and harmless.
This cell's manual invocation SENDS A REAL EMAIL. It is authorized verbatim by Andrew ('run a manual
trigger so i can see the output') and it is bounded to ONE invocation. The scheduled fire, not this
one, remains the acceptance.
</preflight>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6, round 4) - **Project:** NFRA_REPORT - **Directive:** D12
**Authority chain:** Andrew-direct -> `1.0.0_SA_CTO~Z` L4 ADDENDUM 01 @`20c986bc70` -> L5 re-decomposition `org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R4.md` -> this issuance.
