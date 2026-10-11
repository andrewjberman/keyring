# AMGT_RESAPP task order -- `AMGT-aa-5` -- REDEPLOY THE SCOPED API CARRYING THE WITHHELD CLASSIFICATION AND THE INITIALISM CASING -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aa-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-aa-5.redeploy-the-scoped-api-carrying-the-withheld-classification-and-the-initialism-casing</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; the rule reads the table and the crosswalk the function already reads.
comp-adversary: RUN at the cut -- r95_classification_census.py --where deployed FAILs K1-K3 at the live base and r95_casing_deployed.py FAILs D1; the no-regression pair r94_name_census.py --where deployed, r89_peers_deployed.sh, r89_deployed_close.sh --want amgt-corpus-dossier/12 and r92_minor_unit_census.py PASS at the base.
EGRESS CLASS, declared: NONE.
</preflight>


## 1. THE ACT -- `AMGT-aa-5` (round 95, decomposition s.103)

CTO~DELL1 round-94 analysis item 2 (the served half) and item 4. `AMGT-aa-2` and `AMGT-aa-4` (merged before this GO) withhold a disagreeing table row's classification and keep
'CSL' and 'JD' in capitals. ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the build pin the GO names (a box/dell1 commit carrying both
merged; ancestry read at the pin). Before the apply, print the CONTENT-DIFF of the built package against the kept live package (`VNcX9ntm83qe07/eOOD16AYsDmoEp20eCzj9ljfGvGE=`,
downloaded and hash-checked) WHOLE; for each member the pair's BLAST RADIUS table names, its blob at the pin beside the table's column (`checks/r94_admission_table.py <pin>
--pin <the live package's build pin>` and `checks/r94_naming_replay.py` at the pin, both YES); any member the table does not admit is a STOP. Rollback: the kept live package
through the module, ONE `safe-apply`, same hour. Change-management entry opened before, closed after. The record step: `record-terraform-deploy.sh`, the function's
`lambda-source-map.json` entry printed before and after. BEFORE the apply read the baseline of the routes the pair's table names; AFTER the apply, BEFORE flipping anything, compare
every one and print each changed field before and after: the pair's table names every change that may appear.

## 2. BOUNDS

1. The act and nothing else: the writes named, for the keys named; no function, role, route, schedule or other prefix beyond what the act names.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
5. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
6. 49 Financial data never goes into another firm's tree.
7. A change the pair's table does not name is a STOP and, inside the same hour, a restore of the kept package unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aa-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_casing_deployed.py"; echo "exit=$?"</invocation><expect>two disagreeing table rows listed; PASS K1, PASS K2, PASS K3, PASS K4, PASS K5; R95 CLASSIFICATION CENSUS: YES; PASS D1 (CSL_AU_Equity serves 'CSL Ltd'), PASS D2, PASS D3; R95 CASING DEPLOYED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aa-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where deployed &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/12; echo "exit=$?"</invocation><expect>the no-regression arm: R94 NAME CENSUS: YES (C1, C3, C4 at 0 different), R89 PEERS DEPLOYED: YES and R89 DEPLOYED CLOSE: YES (dossier /12) with the function's CodeSha256 re-read, now DIFFERENT from VNcX9ntm.. (the act's own change); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-aa-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_minor_unit_census.py"; echo "exit=$?"</invocation><expect>the currency arm is unmoved: PASS M1, PASS M2, PASS M3, PASS M4; R92 MINOR-UNIT CENSUS: YES; and exit=0</expect></criterion>
</proof_of_spec>


<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-94 analysis items 2 and 4: "a served change: its redeploy is under its own pair, measured route by route as ff-4 was"; "it rides item 2's redeploy". STAGED. THE GO WAITS ON ALL OF: (1) `AMGT-aa-2` and `AMGT-aa-4` terminal and merged (issuer re-runs AC1-AC3 on the merged tree); (2) THE PAIR, whose COO half is written AFTER (1) from a route-by-route measurement as round 94's was (`r94_name_table.py`, `r94_rankings_table.py`, `r94_other_routes_table.py` and the census, live against the merged handler; the admission table by blob and the builder replay; the writer census; both branches; the kept package), listing SAN FP's classification change and the withheld rows and series and chatter rows whole; the CTO half signed on that table; (3) the pin carries both; (4) `AMGT-aa-1` is producer-side and needs no served write (SAP's object is re-verified by nobody). The expected change from the base measurement: SAN_FP_Equity's and CSL_AU_Equity's classification withheld on ranked rows 67 (PRICE lists), rank series, collected-chatter rows; CSL_AU_Equity display name 'Csl Ltd' -> 'CSL Ltd'; nothing else.

<status>complete -- 0.7.0_AE_CloudOps~RA1, 2026-10-11T18:2xZ. Applied 2026-10-11T18:03:15Z (function LastModified 18:03:44Z), CodeSha256 VNcX9ntm83qe07/eOOD16AYsDmoEp20eCzj9ljfGvGE= -> TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8=; built in a detached worktree at b3512d18fb; r94_admission_table 2 members at the half's blobs, r94_naming_replay YES (0 of 88 differ); content diff 408 files, CHANGED 2, ADDED 0, off-list 0; one resource of 53 moved. Local prediction of the four table scripts = the half (3 + 6 + 24 + 6 = 39); baseline of 527 requests 17:56-18:01Z. AC1 YES (K1-K6, D1-D3), AC2 YES (dossier /12, function changed), AC3 YES (154 major-unit rows unchanged). Post-apply compare: 39 name and classification paths on SAN_FP and CSL_AU = exactly the half's table, 28 clock paths, 0 corpus paths, 0 outside, status moved 0; the not-moved set (186 ranked rows and 186 series of other subjects, all 2230 peer members, thesis, timeline) equal. CodeSha256 and apply time reported to the issuer at 18:04Z. scratch/r95-aa5-pin kept. Ledger amgt-resapp-r95-aa5-classification-redeploy-dell1 CLOSED 10 of 10. Proof instance deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-aa-5.*.proof_of_spec.json VALID rc=0. (was: pending -- GO 2026-10-11T17:30Z by the issuer (2.0.0_SA_COO~R1) to 0.7.0_AE_CloudOps~RA1. Pair: COO half @b38de315e7, CTO half signed (CTO msg 4042). BUILD PIN b3512d18fb on the scratch branch scratch/r95-aa5-pin (the live package's pin 15b7af1601 plus scoped_amgt.py ec7c8fde988b and monthly_chatter.py 5243b870cac5 only; NOT box/dell1 HEAD, which carries AMGT_CORPUS round 47's unpaired corpus files). GO conditions: (1) the build is a detached worktree at b3512d18fb and `r94_admission_table.py b3512d18fb --pin 15b7af1601` shows exactly two members differing, at the half's blobs (a third is a STOP); (2) RA1's pre-apply local prediction of the three table scripts and r95_series_by_ticker_table.py matches the half (39 name and classification paths, 0 outside); (3) scratch/r95-aa5-pin is kept (not deleted) until a merged-pin redeploy supersedes it. After the apply: the post-act compare against the recorded baseline plus the NOT-moved set (every other subject's classification object, every score and rank, every peer member), AC1-AC3, the record step, the ledger closed. Report the CodeSha256 and the apply time to the issuer (it relays them to 2.0.0_SA_COO~C1).)</status>
<round>95</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
