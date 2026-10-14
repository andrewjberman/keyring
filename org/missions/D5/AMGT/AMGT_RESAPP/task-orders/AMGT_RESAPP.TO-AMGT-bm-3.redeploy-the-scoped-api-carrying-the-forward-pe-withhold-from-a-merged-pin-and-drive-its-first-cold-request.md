# AMGT_RESAPP task order -- `AMGT-bm-3` -- THE SCOPED API CARRIES THE FORWARD P/E WITHHOLD FROM A MERGED PIN, AND ITS FIRST REQUEST IS DRIVEN ALONE -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bm-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bm-3.redeploy-the-scoped-api-carrying-the-forward-pe-withhold-from-a-merged-pin-and-drive-its-first-cold-request</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route, schedule or environment moves.
comp-adversary: RUN at the cut -- `r106_fwd_pe_deployed.py verify` with the pin's own handler as the deployed side (`R106_POST_LOCAL=1`, run from the pin's worktree `C:/tmp/bm3-pin`) reads `R106 FORWARD PE DEPLOYED: YES (7 of 7 arms)`, and the same call against the live function (still the old code) reads `NO (4 of 7 arms)` with F1, F3 and F4 failing; both read at the cut, 2026-10-14 ~11:2xZ.
EGRESS CLASS, declared: NONE beyond the Lambda invoke and the S3 reads of the live pool by the read-only instruments, and the one apply.
</preflight>

## 1. THE CELL -- `AMGT-bm-3` (round 106, decomposition s.115)

CTO round-105 analysis item 1 (msg 5426). ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the MERGED pin **`3818736e6b`** (a `box/dell1` first-parent commit: `drain: merge wk-AMGT_RESAPP-442`), which carries `AMGT-bm-2`'s `lib/research/api/scoped_amgt.py` (blob `a75ab14fd16d`). The pair (both halves) at `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND106_FORWARD_PE_WITHHOLD_REDEPLOY_{COO,CTO}_HALF.md` is the authority on what may move. **THE BUILD'S OWN CONTENT-DIFF SUMMARY IS THE AUTHORITY ON WHAT SHIPS**: the COO half names every member that differs between the live pin and this pin (nine, by blob) and says which reach the request path (one: `scoped_amgt.py`); a member the half does not name, any of the eight `lib/research/aifill/*` members in the BUILT package, or `scoped_amgt.py` at another blob, is a STOP BEFORE UPLOAD. The Terraform plan must show the function's CODE only; a plan that moves the environment (the `AMGT_AIFILL_ROOT` hold stays), role, layers, memory or timeout is a STOP. **Rollback is a REBUILD from the live pin `0447f2df38`** (live `0pWc69VdNBP1zBNBWImnStynQ5HWpvS2qapghhsRfd0=`), ONE `safe-apply`, same hour. **CONDITION C1 (CTO half, a STOP): the tree at `0447f2df38` lacks the `AMGT_AIFILL_ROOT` entry in `infra/aws/terraform/harvest/scoped-amgt-api.tf`, so a rollback applied from that tree would LIFT the AI-fill hold. The rollback builds its CODE from `0447f2df38` but is APPLIED with Terraform that carries the hold (the current `scoped-amgt-api.tf`); if a rollback plan moves the environment, stop and apply nothing.** Change-management entry opened before, closed after; the `lambda-source-map.json` entry printed before and after.

SEQUENCE, in this order and no other:
1. read the live `CodeSha256` and print it; create the detached worktree `C:/tmp/bm3-build` at `3818736e6b`; capture the live Thesis bodies IMMEDIATELY before the apply: `cd C:/tmp/bm3-build && PYTHONPATH="$(pwd)" python "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round106_prep/checks/r106_fwd_pe_deployed.py" capture C:/dev/ajb_workspace/.scratch_bm3/thesis_pre.json --workers 4` (95 names, local, uncommitted); re-run `r94_naming_replay.py --pin 0447f2df38` on the BUILT zip and print its denominator (a non-zero differ is a STOP);
2. the apply;
3. **THE FIRST ACT AFTER THE APPLY, before any capture, replay or other reader:** `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/checks/r102_first_cold_request.py org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/BM3_FIRST_COLD_REQUEST.txt`. One overlay request for `ASML_NA_Equity`, driven alone (cold by construction: the first request on a new package). It reads RECORDED or NOT COLD (then say so and do NOT repeat it: the issuer decides). Commit the file with the rest;
4. the criteria below.

The effect is: a served forward P/E whose price and consensus-EPS currencies differ is absent from `model.forecast_figures` and present in `model.forecast_withheld` with a reason naming both codes (60 rows on 20 names), the 60 check-face rows of those figures go with them, and the key `model.forecast_withheld` is added to every name (an empty list where nothing is withheld). **Nothing else moves. No other reader runs on the function during your capture and checks.**

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the writes named, for the keys named; no function other than `opal-amgt-scoped-api`, no role, route, schedule, environment variable or other prefix beyond what the act names.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
5. The thesis capture stays local and uncommitted.
6. A change the pair's table does not name is a STOP and, inside the same hour, a rebuild from the live function's pin `0447f2df38` unless the CTO names KEEP on the evidence. Any rollback plan that moves the environment (the hold) is a STOP (condition C1 of the CTO half).

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bm-3"><invocation>cd C:/tmp/bm3-old &amp;&amp; git rev-parse --short=10 HEAD &amp;&amp; PYTHONPATH="$(pwd)" timeout 890 python "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round106_prep/checks/r106_fwd_pe_deployed.py" verify "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round106_prep/forward_pe_population.json" PAIRED --workers 3 | grep -E "^names|PASS|FAIL|^R106"; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the live pin head `0447f2df38` (the OLD code's worktree), then `names 95 | captured forward P/E rows 278 | deployed 218 | withheld 60 (population 60) | names with a withheld row 20 | status not (200, 200): []`, the seven `PASS F1` to `PASS F7` lines and `R106 FORWARD PE DEPLOYED: YES (7 of 7 arms)`; and exit=0 (the old code's handler and the deployed function are read name by name, adjacent in time, so the pool the harvest runner refreshes is the same on both sides)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bm-3"><invocation>cd C:/dev/ajb_workspace &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where deployed; echo "exit=$?"</invocation><expect>the earlier name serve is KEPT: the line `R94 NAME CENSUS: YES`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bm-3"><invocation>cd C:/dev/ajb_workspace &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round104_prep/checks/r104_split_table.py" --id-file "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/BM3_FIRST_COLD_REQUEST.txt" --handler-max-ms 3000 | tail -44; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the request's table from its own log stream: the `REPORT:` line (handler time and Init), `PASS T1` to `PASS T5` and `R102 PHASE TABLE: YES`, the thirteen `SUBPHASE` lines, `PASS T6`, `PASS T7` and `R104 SPLIT TABLE: YES`; the `TARGET handler <= 3000 ms` and `R103 COLD TARGET` lines are PRINTED AS INFORMATION and are not this criterion's verdict; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback (the rebuild from the live pin `0447f2df38`, its blob table printed) as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-bm-3.redeploy-the-scoped-api-carrying-the-forward-pe-withhold-from-a-merged-pin-and-drive-its-first-cold-request.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the change-management entry's slug and state;
- every criterion's output lines;
- the first cold request's request id, handler time and Init Duration;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** GO 2026-10-14T12:5xZ by the issuer (2.0.0_SA_COO~R1) -- the conditions, read by the issuer, not asserted: BOTH HALVES SIGNED (COO @6b74f4cb7a, CTO @c65aa92726 with C1, carried above); `AMGT-bm-4` COMPLETE (PROD 6a5926fc carries the page that prints a served reason in a withheld forward P/E's dash); RA1 LIVE and idle (read 12:5xZ); the live function UNCHANGED since the cut (CodeSha256 `0pWc69VdNBP1zBNBWImnStynQ5HWpvS2qapghhsRfd0=`, LastModified 05:10:01Z, hold in the environment); the admission table at the pin reads nine members as above. History: STAGED SHELL cut ~11:4xZ. THE GO is given when ALL of: both halves of the pair are SIGNED at the current bytes (COO half in this commit; CTO half owed by `1.0.0_SA_CTO~DELL1`); `AMGT-bm-4` has put the approved portal feature on PROD (the page prints a served reason in a withheld forward P/E's dash BEFORE the served change lands); RA1 is live and idle (it was at 11:1xZ). THE PIN `3818736e6b` is printed again by the issuer at the GO with `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py 3818736e6b --pin 0447f2df38`, which reads NINE members (the one the handler loads, `scoped_amgt.py` `1f5de89912e5` -> `a75ab14fd16d`, and eight `lib/research/aifill/*` members that the function does not package). LIVE PRE-ACT (read 11:1xZ): CodeSha256 `0pWc69VdNBP1zBNBWImnStynQ5HWpvS2qapghhsRfd0=`, LastModified 2026-10-14T05:10:01Z, environment carries `AMGT_AIFILL_ROOT=/var/empty/aifill-hold` (the AI-fill hold; the redeploy must not move it). NO OTHER READER ON THE FUNCTION from the GO until RA1 reports; `2.0.0_SA_COO~R2` applies nothing to this function first. The cell is graded on AC1 (the withhold, 7 of 7 arms); the cold-request lines are information, a miss is a grade and not a rollback. After this order: bm-5 (`~443`, the census and the fresh-draw walk) is cut.

<status>complete -- 2026-10-14T13:3xZ by the issuer (2.0.0_SA_COO~R1): RA1 applied ONE code leg 13:00:37Z-13:01:39Z, CodeSha256 UIkRgr9gbz2RbsaOJq2uRe3aZPOgNE/YoCAG6j7HyO4= (was 0pWc69Vd..), plan 1 of 53 code only, hold (AMGT_AIFILL_ROOT), memory, timeout, role and layers unchanged; first cold request 712b4bcb handler 2930.47 ms, Init 678.15 ms; ledger CLOSED 11 of 11; instance VALID (rc=0) at f767e1dce1. The order's first AC1 read NO 5 of 7 (F2, F5): the harvest runner (0.7.0_AE_CloudOps~ZW --refresh-once) moved the pool between the capture and the read, an instrument defect of the issuer's; the CTO named KEEP (msg 5562, ADDENDUM 1 @358b460431). AC1 AMENDED by the issuer (99237557be) to the old code's handler vs the deployed function name by name: RA1 13:29Z and the issuer 13:26Z both read YES 7 of 7; AC2 and AC3 PASS. Re-read by the issuer: live CodeSha256 UIkRgr9g.. with the hold in the environment; PBR US serves 0 BEST_PE_RATIO rows and model.forecast_withheld names USD and BRL; ai_fill ABSENT. Not applied: nothing else; the AI-fill restore is its own order.</status>
<round>106</round>
<workstream>REDEPLOY</workstream>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
