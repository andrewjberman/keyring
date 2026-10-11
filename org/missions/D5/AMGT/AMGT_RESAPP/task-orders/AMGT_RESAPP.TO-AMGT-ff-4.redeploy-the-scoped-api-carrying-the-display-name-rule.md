# AMGT_RESAPP task order -- `AMGT-ff-4` -- REDEPLOY THE SCOPED API CARRYING THE DISPLAY-NAME RULE (SANOFI AND CSL NAMED AS THEMSELVES)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ff-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ff-4.redeploy-the-scoped-api-carrying-the-display-name-rule</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; the rule reads the crosswalk's names the function already reads.
comp-adversary: RUN at the cut -- r94_name_census.py --where deployed reads 2 DIFFERENT companies at the base (live SOzAz9..), 243 of 243 judged; r94_display_name.py is the worker's; r89 arms PASS at the base.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-ff-4` (round 94, decomposition s.102)

CTO~DELL1 round-93 analysis item 1, the served half. `AMGT-ff-1` (merged before this GO) makes the name chain serve the registered name when a classification name
disagrees with it. ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the build pin the GO names (a box/dell1 commit carrying
`AMGT-ff-1` merged; ancestry read at the pin). Before the apply, print the CONTENT-DIFF of the built package against the kept live package (`SOzAz9/gfKE..`, downloaded
and hash-checked) WHOLE; for each member the pair's BLAST RADIUS table names, its blob at the pin beside the table's column; any member the table does not admit, or
a blob that differs beyond the admitted change, is a STOP. Rollback: the kept live package through the module, ONE `safe-apply`, same hour. Change-management entry
opened before, closed after. The record step: `record-terraform-deploy.sh`, the function's `lambda-source-map.json` entry printed before and after.
BEFORE the apply read the baseline of the peers AND overlay routes of all 243 subjects; AFTER the apply, BEFORE flipping anything, compare every subject and every
member of both routes and print each changed field before and after: the pair's table names every change that may appear.

## 2. BOUNDS

1. The act and nothing else: the writes named, for the keys named; no function, role, route, schedule or other prefix beyond what the act names.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
5. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
6. 49 Financial data never goes into another firm's tree.
7. A change the pair's table does not name is a STOP and, inside the same hour, a restore of the recorded VersionIds (or, for a code leg, the kept package) unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ff-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where deployed; echo "exit=$?"</invocation><expect>judged 243 of 243 subjects, UNJUDGED 0, DIFFERENT company 0 (the base reads 2: SAN_FP_Equity and CSL_AU_Equity), the spelling variants listed; PASS C1; R94 NAME CENSUS: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ff-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/11; echo "exit=$?"</invocation><expect>the no-regression arm: R89 PEERS DEPLOYED: YES and R89 DEPLOYED CLOSE: YES (dossier /11, the withhold and the listing byte-equal) with the function's CodeSha256 re-read, now DIFFERENT from SOzAz9.. (the act's own change); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ff-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_minor_unit_census.py"; echo "exit=$?"</invocation><expect>the currency arm is unmoved: PASS M1, PASS M2, PASS M3, PASS M4; R92 MINOR-UNIT CENSUS: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and the recorded VersionIds as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ff-4.redeploy-the-scoped-api-carrying-the-display-name-rule.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the VersionId list's file path;
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-93 analysis @bfa6b04c8c item 1: "a served change, under its own pair, measured subject by subject." STAGED. THE GO WAITS ON ALL OF: (1) `AMGT-ff-1` terminal and merged (issuer re-runs AC1-AC3 on the merged tree); (2) THE PAIR, whose COO half is written AFTER (1) from a subject-by-subject measurement: the merged tree's handler against the live function over all 243 subjects' overlay AND peers routes (every changed field before and after, with its route), the content-diff admission table for the closure members (blobs at the live pin and at the cut, including any other project's change the package carries: round 92's ss-3 `engine.py` and `lib/opal_naming.py` are candidates), the writer census of the moved property (the name chain's callers), both branches, the per-key rollback (the kept package); the CTO half signed on that table; (3) the pin carries ff-1; (4) the sequencing rule with `AMGT-ff-5` (never one window; the second re-measures). The expected change from the base measurement: SAN_FP_Equity's served name 'Banco Santander S.A.' -> 'Sanofi' and CSL_AU_Equity's 'Carlisle Cos Inc' -> 'CSL Ltd' on every route that serves a name, and every member whose key is one of those two in other subjects' sets; the classification sector of those two names is the same table's row and is NOT moved by this cell (stated in the pair).

<status>staged</status>
<round>94</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
