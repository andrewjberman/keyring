# AMGT_RESAPP task order -- `AMGT-ar-3` -- THE SCOPED API CARRIES THE AI-FILL SERVE FROM A MERGED PIN, ITS FIRST REQUEST IS DRIVEN ALONE, AND THE SERVED `ai_fill` IS READ BACK (FWD-41, STEPS 3 AND 4 READ OF THE NEVER-WIDEN PAIR; A WORLD ACT) -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ar-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ar-3.the-scoped-api-carries-the-ai-fill-serve-and-its-first-cold-request-is-driven-alone</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; the read grant is `AMGT-ar-1`'s and is re-read (not changed) here by `check_ar1_grant.py`.
comp-adversary: RUN at the cut -- `check_ar3_aifill_served.py` reads `AIFILL AR-3 SERVED: NO (0 of 6)` at the base on the live function (no `ai_fill` key; no stored document), and its pre-apply `capture` mode wrote two live bodies; this order is a STAGED shell whose pin, numbers and GO are filled by the issuer when its conditions hold.
EGRESS CLASS, declared: NONE beyond the function's own S3 reads and Lambda invokes (GET); no Bloomberg, no model call, no S3 write.
</preflight>

## 1. THE CELL -- `AMGT-ar-3` (round 104, workstream AIFILLREL, decomposition s.10)

STEPS 3 AND THE READ OF STEP 4 of the never-widen pair for FWD-41 (both halves SIGNED: `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND104_AIFILL_STORE_GRANT_REDEPLOY_{COO,CTO}_HALF.md`; their blast radius is this order's bound). ONE code leg on us-east-1
`opal-amgt-scoped-api`, built from a DETACHED worktree at the MERGED pin the GO names (a `box/dell1` first-parent commit that carries `AMGT-fa-7`'s `scoped_amgt.py` region and `AMGT-fa-9`'s regenerated `_harvest_prefixes.py` (merges
`cd31b97501` and `957b04a764`) on top of `2.0.0_SA_COO~R1`'s round-104 code already live). **THE BUILD'S OWN CONTENT-DIFF SUMMARY IS THE AUTHORITY ON WHAT SHIPS**: the pair names every CHANGED member by blob, and a member it does not name is a STOP BEFORE UPLOAD. Rollback is a REBUILD from the
merged pin the live function was built from at the GO (printed there), ONE `safe-apply`, same hour. Change-management entry opened before, closed after; the `lambda-source-map.json` entry printed before and after.

SEQUENCE, in this order and no other:
1. read the live `CodeSha256` and print it; confirm `check_ar1_grant.py` reads YES (the read grant is live) and that the stored AMD document exists (`store.read_document`, step 2(a) of the pair, done by the issuer); capture the live `/thesis` bodies of the three names the GO lists to `.scratch_ar3/thesis_pre.json` IMMEDIATELY before the apply with `check_ar3_aifill_served.py capture`;
   print the admission table (`r94_admission_table.py <pin> --pin <live pin>`) and the built package's content diff; re-run `r94_naming_replay.py --pin <live pin>` on the BUILT zip (non-zero differ is a STOP);
2. the apply;
3. **THE FIRST ACT AFTER THE APPLY, before any capture or other reader:** the first-cold-request script `r102_first_cold_request.py` (the same one `AMGT-bk-2` ran; its path is in the GO) driven ALONE: one overlay request for `ASML_NA_Equity`. It reads RECORDED or NOT COLD (then say so and do NOT repeat it: the issuer decides). Its handler time is PRINTED AS INFORMATION: this code adds no read to any overlay path, so it must not worsen `2.0.0_SA_COO~R1`'s measured split;
4. the verification of AC1;
5. the criteria below.

The effect: the `/thesis` body gains the key `ai_fill` (additive; every other key byte-equal), served from the stored document by ONE S3 GET per request on that route only. **No other reader runs on the function during your capture and verification.**

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. The act and nothing else: the function's code package for `opal-amgt-scoped-api`, the members the pair names. No role, route, schedule, other function or other prefix.
2. No S3 write or delete, no Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. The captures stay local and uncommitted.
5. A change the pair's table does not name is a STOP and, inside the same hour, a rebuild from the live function's merged pin unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ar-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; AIFILL_SERVED_FUNCTION=opal-amgt-scoped-api PYTHONPATH="$(pwd)" timeout 900 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_ar3_aifill_served.py" verify --pre ".scratch_ar3/thesis_pre.json" --stored-name AMD_US_Equity; echo "exit=$?"</invocation><expect>no `FAIL` arm line and the line `AIFILL AR-3 SERVED: YES (N of N)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ar-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round97_prep/checks/r97_sector_serve_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where deployed; echo "exit=$?"</invocation><expect>the earlier serves are KEPT: R97 SECTOR SERVE CENSUS: YES (6 of 6), R95 CLASSIFICATION CENSUS: YES (6 of 6), R94 NAME CENSUS: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback (the rebuild from the live function's merged pin, its blob table printed) as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ar-3.the-scoped-api-carries-the-ai-fill-serve-and-its-first-cold-request-is-driven-alone.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the change-management entry's slug and state;
- every criterion's output lines;
- the content-diff table (changed members by blob, and the count outside the pair's table);
- the first cold request's request id, handler time and Init Duration;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED SHELL: the pin, the live pre-act numbers, the three names and the first-cold-request script path are filled at the GO (`<status>pending -- GO ...</status>`). THE GO WAITS ON ALL OF: (1) `2.0.0_SA_COO~R1`'s `AMGT-bk-2` complete and read back (ONE applier at a time on the function; its pin is the live function's); (2) `AMGT-ar-1` complete (the grant is live); (3) step 2(a) of the pair done: `run --key AMD_US_Equity --to-s3 --confirm-write` by the issuer, read back equal; (4) no other reader on the function. The seat is told by the broker with the path when the GO is written. A miss of the cold-start target is not this order's grade (R1's cell carries it); a worsening against R1's measured split, if the order's request shows one, is a row. ROLLBACK: a rebuild at the live function's merged pin through one `safe-apply`.

<status>staged</status>
<status>pending -- GO 2026-10-14T01:2xZ by the issuer (2.0.0_SA_COO~R2). THE CONDITIONS, read by the issuer: (1) `2.0.0_SA_COO~R1`'s `AMGT-bk-2` complete (its pin `d7a79c766a` is the live function's; CodeSha256 `Wkt48Y6vf4o4Dhyb9gVkfaf9IIJ75ThoI+hiMUoGrS4=`, LastModified 2026-10-14T00:07:07Z, re-read at 01:2xZ unchanged); (2) `AMGT-ar-1` complete, `check_ar1_grant.py` YES 7 of 7 (re-run by the issuer); (3) step 2 done: all 95 documents stored and read back (`round104/store_readback_census.json`), `AMD_US_Equity` among them; (4) BOTH HALVES SIGNED and the CTO's concurrence with ADDENDUM 1 (msg 5333). THE PIN: `0447f2df38`; build from a DETACHED worktree at exactly it. The admission table, run by the issuer: `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py 0447f2df38 --pin d7a79c766a` reads EIGHT members that differ (the table is in the COO half, ADDENDUM 1, by blob: `scoped_amgt.py` `351f9a1d7a8a` -> `1f5de89912e5`, loaded; seven `lib/research/aifill` modules, not loaded); `_harvest_prefixes.py` is byte-equal. ANY member beyond the eight, or another blob, is a STOP BEFORE UPLOAD. THE THREE NAMES for the pre/post captures: `AMD_US_Equity,ASML_NA_Equity,COST_US_Equity` (`AIFILL_SERVED_FUNCTION=opal-amgt-scoped-api python .../check_ar3_aifill_served.py capture --names ... --out .scratch_ar3/thesis_pre.json`). THE FIRST-COLD-REQUEST SCRIPT: `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round102_prep/checks/r102_first_cold_request.py org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AR3_FIRST_COLD_REQUEST.txt`. NO OTHER READER on the function from this GO until you report: the issuer holds its reads. ROLLBACK: a REBUILD at `d7a79c766a` through one `safe-apply`, same hour.</status>
<round>104</round>
<workstream>AIFILLREL</workstream>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<proof_genre>DEPLOY</proof_genre>
