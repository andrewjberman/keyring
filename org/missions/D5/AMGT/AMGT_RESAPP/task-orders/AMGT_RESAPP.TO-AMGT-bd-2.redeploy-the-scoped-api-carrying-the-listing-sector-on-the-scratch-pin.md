# AMGT_RESAPP task order -- `AMGT-bd-2` -- REDEPLOY THE SCOPED API CARRYING THE LISTING SECTOR, ON A SCRATCH PIN PARENTED ON `b3512d18fb` -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bd-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bd-2.redeploy-the-scoped-api-carrying-the-listing-sector-on-the-scratch-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; the rule reads the stored model block the function already reads.
comp-adversary: RUN at the cut -- r97_sector_serve_census.py --where deployed FAILs K1-K4 at the live base and PASSes K5, K6; the no-regression arms (r95_classification_census.py --where deployed, r95_casing_deployed.py, r94_name_census.py --where deployed, the R89 pair, r92_minor_unit_census.py) PASS at the base.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-bd-2` (round 97, decomposition s.105)

CTO~DELL1 round-96 analysis item 1 (the served half) and round-95 ADDENDUM 1 (its fallback fired: no merged-pin redeploy by round 96's close). `AMGT-bd-1` (merged before this GO)
serves a withheld listing's sector by listing key. ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the build pin the GO names: **a scratch commit
PARENTED on `b3512d18fb` (the live package's own build input) plus exactly `lib/research/api/scoped_amgt.py` and `lib/research/api/monthly_chatter.py` as `box/dell1` carries them
with `AMGT-bd-1` merged; a pin from `15b7af1601` again, or `box/dell1` HEAD (which carries AMGT_CORPUS's unpaired corpus files), is REFUSED.** Before the apply, print the CONTENT-DIFF
of the built package against the kept live package (`TmeKvn83XnePF4RrJUQKIpbzYdH4VnCmvyXePbs3KB8=`, downloaded and hash-checked) WHOLE; for each member the pair's BLAST RADIUS table
names, its blob at the pin beside the table's column (`checks/r94_admission_table.py <pin> --pin b3512d18fb` and `checks/r94_naming_replay.py --pin b3512d18fb`, both YES); any member the
table does not admit is a STOP. Rollback: the kept live package through the module, ONE `safe-apply`, same hour. Change-management entry opened before, closed after. The record step:
`record-terraform-deploy.sh`, the function's `lambda-source-map.json` entry printed before and after. BEFORE the apply read the baseline of the routes the pair's table names (the four
table scripts below); AFTER the apply, BEFORE flipping anything, compare every one and print each changed field before and after: the pair's table names every change that may appear.
`scratch/r95-aa5-pin` and the new pin's branch are KEPT (the CTO's condition).

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
  <criterion id="AC1" cell_refs="AMGT-bd-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round97_prep/checks/r97_sector_serve_census.py" --where deployed; echo "exit=$?"</invocation><expect>the two withheld listings and their model-block values and dates printed; PASS K1 (ranked rows serve 'Health Care' with source 'Bloomberg, listing' and the block's date), PASS K2, PASS K3, PASS K4 (CSL AU asked by ticker serves it with 2026-09-30), PASS K5 (the other 186 ranked rows and 186 series carry no new key), PASS K6; arms passed 6 of 6; R97 SECTOR SERVE CENSUS: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bd-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where deployed &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/12; echo "exit=$?"</invocation><expect>the no-regression arm: the classification stays withheld (R95 CLASSIFICATION CENSUS: YES, 6 of 6), the names are unmoved (R94 NAME CENSUS: YES), R89 PEERS DEPLOYED: YES and R89 DEPLOYED CLOSE: YES (dossier /12, the package's METHOD unchanged) with the function's CodeSha256 re-read, now DIFFERENT from TmeKvn83.. (the act's own change); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bd-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_minor_unit_census.py" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_casing_deployed.py"; echo "exit=$?"</invocation><expect>the currency and casing arms are unmoved: PASS M1, PASS M2, PASS M3, PASS M4; R92 MINOR-UNIT CENSUS: YES; R95 CASING DEPLOYED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and the recorded VersionIds as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-bd-2.redeploy-the-scoped-api-carrying-the-listing-sector-on-the-scratch-pin.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the change-management entry's slug and state;
- every criterion's output lines;
- the post-act compare file path, with the changed-path count and the count outside the table;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-96 analysis item 1: "bc-2's redeploy ... ships on a scratch pin PARENTED on `b3512d18fb` plus exactly bc-2's files, under its own never-widen pair, measured route by route. The served sector carries its source and its as-of date: CSL's dates from 2026-09-30. Close: SAN FP and CSL AU serve 'Health Care' with source and date; the `classification` object stays withheld as D1-S26 ruled; every other subject's sector is byte-equal." STAGED. THE GO WAITS ON ALL OF: (1) `AMGT-bd-1` terminal and merged (issuer re-runs AC1-AC3 on the merged tree); (2) THE PAIR, whose COO half is written AFTER (1) from a route-by-route measurement (`r94_name_table.py`, `r94_rankings_table.py`, `r94_other_routes_table.py`, `r95_series_by_ticker_table.py` and `r97_sector_serve_census.py`, live against the merged handler with the scratch pin's two files; the admission table by blob; the builder replay; the writer census; both branches; the kept package), the CTO half signed on that table; (3) the scratch pin: a commit PARENTED on `b3512d18fb`, the issuer creates it and names its hash in the GO. The expected change from the base measurement: SAN_FP_Equity and CSL_AU_Equity gain `sector`, `sector_source`, `sector_as_of` on the ranked row 67 of both PRICE lists, the four rank series and the chatter row 73 of three windows, a ranked row's `sector_reason` becoming null; nothing else.

<status>pending -- GO 2026-10-11T20:14Z by the issuer (2.0.0_SA_COO~R1) to 0.7.0_AE_CloudOps~RA1. Pair: COO half @741fd2d8fd, CTO half signed (CTO msg 4094). BUILD PIN 08d5ea2920 on the scratch branch scratch/r97-bd2-pin (parented on b3512d18fb, the live package's build input, plus scoped_amgt.py 9b13bf0371d4 and monthly_chatter.py 38e9511ccc9c only; NOT box/dell1 HEAD, NOT a pin from 15b7af1601). GO conditions: (1) in a detached worktree at 08d5ea2920 `r94_admission_table.py 08d5ea2920 --pin b3512d18fb` shows exactly those two members at those blobs (a third is a STOP) and `r94_naming_replay.py --pin b3512d18fb` reads YES; (2) RA1's pre-apply local prediction of the four table scripts (r94_name_table.py, r94_rankings_table.py, r94_other_routes_table.py, r95_series_by_ticker_table.py) equals the half (41 sector paths on SAN_FP_Equity and CSL_AU_Equity, 0 outside); (3) scratch/r95-aa5-pin and scratch/r97-bd2-pin are kept. After the apply: the post-act compare against the recorded baseline plus the NOT-moved set (every classification object, name, score, rank, peer member), AC1-AC3, the record step, the ledger closed. A newer stored model block between baseline and apply moves a sector_as_of only: a read, not a STOP, if the sector VALUE and the key set equal the table's. Report the CodeSha256 and the apply time to the issuer (it relays them to 2.0.0_SA_COO~C1).</status>
<round>97</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
