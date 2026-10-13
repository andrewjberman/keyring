# AMGT_RESAPP task order -- `AMGT-bi-2` -- THE SCOPED API CARRIES THE PHASE LOG LINES (`AMGT-bi-1`) FROM A MERGED PIN, AND ITS FIRST REQUEST IS DRIVEN ALONE -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bi-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bi-2.redeploy-the-scoped-api-carrying-the-phase-log-lines-from-a-merged-pin-and-drive-its-first-cold-request</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route or schedule moves.
comp-adversary: RUN at the cut -- against the live base: r102_phase_table.py reads NO on a live request (no phase lines exist yet) and YES, WARM and NO on three control files built from the candidate's own lines; r102_first_cold_request.py writes its file and reads RECORDED on the live base; this order is a STAGED shell whose pin, numbers and pair are filled at its GO.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-bi-2` (round 102, decomposition s.110)

CTO~DELL1 round-101 analysis item 1. ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the MERGED pin the GO names: a `box/dell1` first-parent commit that carries
`AMGT-bi-1`'s `lib/research/api/scoped_amgt.py` (its blob printed by the GO; the prepared candidate is `02627c18a0ea`), with every other member of the package UNCHANGED from the live function. The change is
ONE member and LOG LINES ONLY: `AMGT_PHASE route=overlay` lines for fourteen phases. Before the apply print the CONTENT-DIFF of the built package against the kept live package WHOLE; the pair's table names
the one member and its two blobs; any other member is a STOP. **Rollback is a REBUILD from the merged pin the live function was built from (the function keeps only `$LATEST`; the CTO, msg 4287): the pair
names that pin (`7da642c1ff`, live `j+j1k5r7..`) and its blob table, and the rebuild is ONE `safe-apply`, same hour.** Change-management entry opened before, closed after; the
`lambda-source-map.json` entry printed before and after.

SEQUENCE, in this order and no other:
1. read the live `CodeSha256` and print it (the pair names it); capture the live Thesis payloads (`aw4_capture.py`, 95 names, local) to `.scratch_bi2/thesis_pre.json` and the 527-request route baseline,
   IMMEDIATELY before the apply;
2. the apply;
3. **THE FIRST ACT AFTER THE APPLY, before any capture, replay or other reader:** `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/checks/r102_first_cold_request.py org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/BI2_FIRST_COLD_REQUEST_20261013.txt`. One overlay request for `ASML_NA_Equity`, driven alone: the first
   request on a new package runs in a new execution environment, so it is COLD by construction, and the lines it prints are the close's evidence. It reads RECORDED (a cold container) or NOT COLD (then say
   so and do NOT repeat it: the issuer decides). Commit the file with the rest;
4. the thesis capture and the route replay, after, as in round 101's `AMGT-bh-2`;
5. the criteria below.

The effect is: the overlay request prints fourteen `AMGT_PHASE` lines; NO served byte moves. **No other reader runs on the function during your capture and replay.** A request over 20 s in the replay:
three re-invokes, 200, identical bytes (a cold container's first request is expected near 20 s and is recorded, not repeated).

## 2. BOUNDS

1. The act and nothing else: the writes named, for the keys named; no function, role, route, schedule or other prefix beyond what the act names.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
5. The thesis captures stay local and uncommitted.
6. A change the pair's table does not name is a STOP and, inside the same hour, a rebuild from the live function's merged pin unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bi-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round97_prep/checks/r97_sector_serve_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where deployed; echo "exit=$?"</invocation><expect>the earlier serves are KEPT: R97 SECTOR SERVE CENSUS: YES (6 of 6), R95 CLASSIFICATION CENSUS: YES (6 of 6), R94 NAME CENSUS: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bi-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round49/ay4_compare.py" ".scratch_bi2/thesis_pre.json" ".scratch_bi2/thesis_post.json"; echo "exit=$?"</invocation><expect>no served byte of the corpus field moved: `ay4 names 95 team_sheet_equals_stored15 95/95 others_equal 95/95`, `growth_exceeds_delta 0`, the max under 6,291,456 bytes; `ay4 compare build 1/1`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bi-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/checks/r102_phase_table.py" --id-file "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/BI2_FIRST_COLD_REQUEST_20261013.txt" | tail -12; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the request's phase table from its own log lines: `PASS T1` (all fourteen phases once each), `PASS T2` (a cold container), `PASS T3` and `PASS T4` (the inner phases sum to read_security_overlay and the outer phases to the handler time within 5 percent or 5 ms), `PASS T5`, then `R102 PHASE TABLE: YES`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback (the rebuild from the live function's merged pin, its blob table printed) as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-bi-2.redeploy-the-scoped-api-carrying-the-phase-log-lines-from-a-merged-pin-and-drive-its-first-cold-request.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the change-management entry's slug and state;
- every criterion's output lines;
- the post-act compare file path, with the changed-path count and the count outside the table;
- the first cold request's request id, handler time, Init Duration and its fourteen phase lines;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's close (round-101 analysis item 1): "ONE driven cold request after 15 quiet minutes (ASML_NA), its 20 s split by phase on Lambda, and the phases summing to the total within 5 pct."
THE ISSUER'S SUBSTITUTION, to be ratified in the pair: a first request on a freshly replaced package is cold by construction, which is stronger than 15 quiet minutes (a quiet window does not guarantee a
recycled container); the quiet condition is held by the pair (no other reader). `AMGT-bg-3`'s and `AMGT-bh-2`'s live readings put the cold request at 20 to 24 s with a current snapshot; this order
attributes it and changes nothing. STAGED. THE GO WAITS ON ALL OF: (1) `AMGT-bi-1` complete and MERGED, its candidate reviewed by the CTO at the pair; (2) THE PAIR, whose COO half is written from the
pin's own handler against the live function (route tables and `r98_thesis_fullbody_compare.py` from the pin's tree: log lines only, so every path must read equal); (3) no other reader on the function.

<status>complete -- 2026-10-13T16:42Z by 0.7.0_AE_CloudOps~RA1: applied 16:15:54Z, function CodeSha256 bKCGUhXppwg1WJxnI/SunRQ/paJXq9m1qOGqHTp2kdc= (was j+j1k5r7..); AC1, AC2, AC3 PASS; no served byte moved (527 requests, status moved 0, 36 clock paths only; thesis 95/95 growth 0); first cold request 4737aa2a-fb3f-4092-84d8-42cfabfc8a8a: 20.566 s, Init 744 ms, 14 phase lines, feed 18796 ms; one STOP before the apply on the twelfth member exemptions.json, ruled by CTO ADDENDUM 1 and COO ADDENDUM 1 (row D1-S27); ledger amgt-resapp-r102-bi2-phase-log-redeploy-dell1 CLOSED; instance VALID; THE CLOSE (the phase table re-read) is the issuer's. (was: pending -- GO 2026-10-13T16:0xZ by the issuer (2.0.0_SA_COO~R1) to 0.7.0_AE_CloudOps~RA1. THE PAIR IS SIGNED: COO half @97304bbc62, CTO half msg 4919 (ledger/NEVER_WIDEN_ROUND102_PHASE_LOG_REDEPLOY_{COO,CTO}_HALF.md). GO CONDITIONS, on the face: (1) PIN 6ecb5bc567, a detached build worktree; `r94_admission_table.py 6ecb5bc567 --pin 7da642c1ff` must print EXACTLY the TWELVE members of the pair's table and its ADDENDUM 1 at their blobs (plus infra/logic/registry/exemptions.json bc909dc105ff -> ccaf6c9f3481, admitted by the CTO, msg 4929; the instrument now diffs every registry file) (scoped_amgt.py 9f72b58aa87e -> 02627c18a0ea; opal_naming.py 3902e0e93ee4 -> 7730d500f16a; trading_calendar.py f54f5589c4e4 -> 72178007dd03; scopes.json cb297c4faed9 -> b53fb599f250; the six opal_data_harvest files and install-cycle-schedule.ps1); any other member or blob is a STOP. (2) THE CTO'S CONDITION: `r94_naming_replay.py --pin 7da642c1ff` re-run on the BUILT ZIP before the apply, its denominator printed (the pair read 35 requests, 78 builder calls, 16 distinct); a non-zero DIFFER is a STOP. (3) The live CodeSha256 is read and printed first and must read j+j1k5r7IY1ZCh9NijT8GSLaqEL3FhamwT8V3tYofCk= (LastModified 2026-10-13T13:17:52Z); anything else is a STOP. (4) The rollback is a REBUILD from merged pin 7da642c1ff, its blob table printed before the apply. (5) The 95 thesis payloads and the 527-request route baseline are captured IMMEDIATELY before the apply and again after; no other reader runs on the function (the issuer holds its readers; 2.0.0_SA_COO~C1's lane is not registered). (6) THE FIRST ACT AFTER THE APPLY is `r102_first_cold_request.py` (the order's act 2), before any capture or replay. (7) Branch 2 (a path changed outside the generation clocks, a status other than 200, a member the table does not name) is STOP and a rebuild unless the CTO names KEEP. (8) Change-management entry opened before, closed after; the lambda-source-map.json entry printed before and after. THE CLOSE: AC3's phase table (all fourteen phases, a cold container, the sums within 5 percent or 5 ms); the issuer re-reads it from the request id.)</status>
<round>102</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
