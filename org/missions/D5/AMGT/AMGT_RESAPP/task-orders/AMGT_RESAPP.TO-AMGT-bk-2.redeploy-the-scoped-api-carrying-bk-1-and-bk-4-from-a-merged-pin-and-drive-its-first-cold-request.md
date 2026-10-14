# AMGT_RESAPP task order -- `AMGT-bk-2` -- THE SCOPED API CARRIES THE SUB-PHASE LINES, THE TOP BAND'S REUSE AND THE DERIVED P/E FROM A MERGED PIN, AND ITS FIRST REQUEST IS DRIVEN ALONE AND READ WITH THE SPLIT -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bk-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bk-2.redeploy-the-scoped-api-carrying-bk-1-and-bk-4-from-a-merged-pin-and-drive-its-first-cold-request</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route or schedule moves.
comp-adversary: RUN at the cut -- `r104_split_table.py` reads `R104 SPLIT TABLE: YES` on a synthetic lines file with the thirteen sub-phase lines (feed 900 ms, peers 90 ms), NO when one sub-phase is moved so the sum is wrong, NO on a file with no sub-phase lines, and NO on round 103's real request 9084a41d (the deployed build then printed none); `r104_pe_delta.py` reads YES on a synthetic pre/post whose only difference is the PE_RATIO rows and NO when a team_sheet moved; this order is a STAGED shell whose pin, numbers and pair are filled at its GO.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AMGT-bk-2` (round 104, decomposition s.113)

CTO round-103 analysis items 1 and 2 (iii). ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the MERGED pin the GO names: a `box/dell1` first-parent commit that carries `AMGT-bk-1`'s and `AMGT-bk-4`'s `lib/research/api/scoped_amgt.py` (its blob printed by the GO; the prepared candidates are `96642b55204d` after bk-1 and `351f9a1d7a8a` after bk-4, from base `84002d3fd559`) and any other member the merge brought (the `~R2` AIFILL workstream adds a region to the same file: the pair names it). **THE BUILD'S OWN CONTENT-DIFF SUMMARY IS THE AUTHORITY ON WHAT SHIPS**: the pair's table names every CHANGED member the build prints, each by blob, and a member the pair does not name is a STOP BEFORE UPLOAD. **Rollback is a REBUILD from the merged pin the live function was built from** (`c558bffbcc`, live `AaACnKtrQyDeTH/qljASGyCs1uPLHUHydW2c7FPzoU8=`), ONE `safe-apply`, same hour. Change-management entry opened before, closed after; the `lambda-source-map.json` entry printed before and after.

SEQUENCE, in this order and no other:
1. read the live `CodeSha256` and print it; print the stored coverage snapshot's `generated_at` (`r101_snapshot_equal.py`, its `snapshot generated_at` line: the request below is graded only when that stamp is today's 12:30Z write); capture the live Thesis payloads (`aw4_capture.py`, 95 names, local) to `.scratch_bk2/thesis_pre.json` and the 527-request route baseline IMMEDIATELY before the apply; re-run `r94_naming_replay.py --pin c558bffbcc` on the BUILT zip and print its denominator (non-zero differ is a STOP);
2. the apply;
3. **THE FIRST ACT AFTER THE APPLY, before any capture, replay or other reader:** `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/checks/r102_first_cold_request.py org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/BK2_FIRST_COLD_REQUEST.txt`. One overlay request for `ASML_NA_Equity`, driven alone (cold by construction: the first request on a new package). It reads RECORDED or NOT COLD (then say so and do NOT repeat it: the issuer decides). Commit the file with the rest;
4. the thesis capture to `.scratch_bk2/thesis_post.json` and the route replay, after, as in round 103's `AMGT-bj-2`;
5. the criteria below.

The effect is: the overlay prints sub-phase lines and its top band reuses the feed's rows (NO served byte moves), and the served fiscal P/E is `PX_LAST / IS_EPS` of the same year (the PE_RATIO rows of the /thesis fiscal figures move, and nothing else). **No other reader runs on the function during your capture and replay.**

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

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
  <criterion id="AC1" cell_refs="AMGT-bk-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round97_prep/checks/r97_sector_serve_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where deployed; echo "exit=$?"</invocation><expect>the earlier serves are KEPT: R97 SECTOR SERVE CENSUS: YES (6 of 6), R95 CLASSIFICATION CENSUS: YES (6 of 6), R94 NAME CENSUS: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bk-2"><invocation>cd C:/tmp/bk2-build &amp;&amp; git rev-parse --short=10 HEAD &amp;&amp; PYTHONPATH="$(pwd)" timeout 590 python "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round104_prep/checks/r104_thesis_normalized_compare.py" ".scratch_bk2/thesis_normalized_post.json" --workers 4 | grep -E "^thesis names|^status not|^R104"; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the pin head `d7a79c766a`, then `thesis names 95 | failed 0 | PE rows live 928 post 928 | PE unresolved entries added 0 | PE check-face rows live 464 post 464 | remaining changed paths K {...}` with only `clock` and `float_repr` kinds, `status not (200, 200): []`, and `R104 THESIS NORMALIZED: YES`; exit=0 (the live function is compared with the merged pin AFTER the apply, so a derived row serves 928 on both sides)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bk-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round104_prep/checks/r104_split_table.py" --id-file "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/BK2_FIRST_COLD_REQUEST.txt" --handler-max-ms 3000 | tail -44; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the request's table from its own log stream: the `REPORT:` line (handler time and Init), `PASS T1` to `PASS T5` and `R102 PHASE TABLE: YES`, the thirteen `SUBPHASE` lines, `PASS T6`, `PASS T7` and `R104 SPLIT TABLE: YES`; the `TARGET handler <= 3000 ms` and `R103 COLD TARGET` lines are PRINTED AS INFORMATION and are not this criterion's verdict; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback (the rebuild from the live function's merged pin, its blob table printed) as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-bk-2.redeploy-the-scoped-api-carrying-bk-1-and-bk-4-from-a-merged-pin-and-drive-its-first-cold-request.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the change-management entry's slug and state;
- every criterion's output lines;
- the post-act compare file path, with the changed-path count and the count outside the table;
- the first cold request's request id, handler time, Init Duration, its fourteen phase lines and its thirteen sub-phase lines;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** GO 2026-10-13T23:5xZ by the issuer (2.0.0_SA_COO~R1) -- the conditions, read by the issuer, not asserted: BOTH HALVES SIGNED (COO @54b2fdee31, CTO @33db5c0bb2; ledger/NEVER_WIDEN_ROUND104_SPLIT_AND_PE_REDEPLOY_{COO,CTO}_HALF.md). THE PIN: `d7a79c766a` (the merged pin the route tables were measured from). Build from a DETACHED worktree at it; the GO prints `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py d7a79c766a --pin c558bffbcc`, which reads FIFTEEN members (`scoped_amgt.py` `84002d3fd559` -> `351f9a1d7a8a` and `_harvest_prefixes.py` `71fbb35c01bb` -> `0ea0b31ad6b9` are the two the handler loads; thirteen others are NOT LOADED and named by blob in the half); the BUILT package's content diff against the live package is the authority: any member the half does not name, or another blob, is a STOP BEFORE UPLOAD and returns to the issuer for an addendum to both halves. LIVE PRE-ACT: CodeSha256 `AaACnKtrQyDeTH/qljASGyCs1uPLHUHydW2c7FPzoU8=`, LastModified 2026-10-13T18:56:24Z, read again by the issuer at 23:4xZ (unchanged). NO OTHER READER ON THE FUNCTION from this GO until you report: the issuer holds its readers; `2.0.0_SA_COO~R2` applies nothing to this function first. THE DAY'S 12:30Z WRITE has happened: print the snapshot `generated_at` as step 1 says. FIRST ACT AFTER THE APPLY: `r102_first_cold_request.py` (step 3), driven alone. The cell is graded on the SPLIT (AC3: T6 and T7); the 3,000 ms target lines are printed as information and a miss is a grade, not a rollback (CTO half). ROLLBACK: a REBUILD at `c558bffbcc` through one `safe-apply`, same hour. SEATING: `0.7.0_AE_CloudOps~RA1` was re-seated by the issuer at 23:4xZ (not on the live roster before), by `/mstr-spawn`. THE GRADE IS SPLIT ON PURPOSE (and this is a change from round 103's `bj-2`, stated): round 103's AC3 required the 3,000 ms target MET, the request read 3,770 ms, and the gate (which has no form for a foreseen miss) then held the round until the CTO ruled. This cell's output is the SPLIT and the reconciliation (T6, T7), which the cell can deliver; FWD-40 (b) is graded by the CVO on the handler time itself and the target lines are printed beside it. THE GO WAITS ON ALL OF: (1) `AMGT-bk-1` and `AMGT-bk-4` complete and MERGED, the candidates read by the CTO at the pair; (2) THE PAIR (COO half from the pin's own worktree: the route tables, `r98_thesis_fullbody_compare.py --after local`, `r94_naming_replay.py`, the admission table by `r94_admission_table.py <pin> --pin c558bffbcc`; the P/E section names the 95 x 10 cells and prints before/after for five names; CTO half signed); (3) no other reader on the function; (4) the `~R2` AIFILL workstream applies nothing to this function first (its serve change is its own pair AFTER this one).

<status>complete</status>
<round>104</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
