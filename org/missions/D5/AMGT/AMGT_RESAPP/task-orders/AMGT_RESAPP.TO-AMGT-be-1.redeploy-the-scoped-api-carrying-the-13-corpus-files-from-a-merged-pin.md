# AMGT_RESAPP task order -- `AMGT-be-1` -- REDEPLOY THE SCOPED API FROM A MERGED PIN CARRYING AMGT_CORPUS'S /13 CORPUS FILES (bd-1's serve KEPT) -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-be-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-be-1.redeploy-the-scoped-api-carrying-the-13-corpus-files-from-a-merged-pin</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; no IAM, route or schedule moves.
comp-adversary: RUN at the cut -- against the live base (`IpaCHo5h..`): aw4_compare.py on a base capture read against itself prints `aw4 compare build 0/1` (team_sheet_equals_stored13 0 of 95: the page serves /12) and `r89_deployed_close.sh --want amgt-corpus-dossier/13` reads NO (the package's METHOD is /12): both build arms FAIL; `r97_sector_serve_census.py --where deployed`, `r95_classification_census.py --where deployed` and `r94_name_census.py --where deployed` PASS at the base (the controls that bd-1's serve must still read after the apply).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-be-1` (round 98, decomposition s.106)

CTO~DELL1 round-97 analysis item 1 and the AMGT_CORPUS `aw-4` CTO half ADDENDA 1-2 (`org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND47_AW4_CTO_HALF.md`; C1's COO half
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND47_AW4_LEGP_SERVED_EFFECT.md` governs the served effect, THIS order's pair governs the redeploy). ONE
code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the MERGED pin the GO names (a `box/dell1` first-parent commit; the issuer's candidate is `a03d92221a`,
which carries `dossier.py` `13463426d0da` (METHOD /13), `team_sheet.py` `956e69d7be7e`, `template.py` `e03d6a8acf65`, `factset_descriptions.json` `76faa8d6a708` AND bd-1's
`scoped_amgt.py` `9b13bf0371d4` and `monthly_chatter.py` `38e9511ccc9c`). **It is NOT `box/dell1` HEAD (it carries the /14 files, whose write is not yet signed to be served), and it is
NOT either scratch pin.** If AMGT_CORPUS's /14 write read leg-v Branch A and the `aw-4` half was restated and re-signed BEFORE this issuance was cut, the leg would carry /14: it was
not, so this order carries /13 and /14 follows as a second redeploy (CTO ADDENDUM 2). **A pin whose `scoped_amgt.py` or `monthly_chatter.py` differs from bd-1's blobs is a STOP: it
silently reverts the listing-sector serve.** Before the apply, print the CONTENT-DIFF of the built package against the kept live package (`IpaCHo5hokQzWcEmw500HI6ax1otqL23vQZaogRWOh4=`,
downloaded and hash-checked) WHOLE; for each member the pair's BLAST RADIUS table names, its blob at the pin beside the table's column (`checks/r94_admission_table.py <pin> --pin
08d5ea2920` and `checks/r94_naming_replay.py --pin 08d5ea2920`, both YES); any member the table does not admit, or a blob that differs beyond the admitted change, is a STOP.
Rollback: the kept live package through the module, ONE `safe-apply`, same hour. Change-management entry opened before, closed after. The record step:
`record-terraform-deploy.sh`, the function's `lambda-source-map.json` entry printed before and after.

BEFORE the apply capture the live Thesis payloads of the whole population, immediately before the act (AMGT_CORPUS's instrument, read-only, 95 direct invokes; the output holds
client research content and STAYS LOCAL, uncommitted):
`PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_capture.py .scratch_be1/thesis_pre.json`; and the route tables the pair names (`checks/r94_name_table.py`, `r94_rankings_table.py`,
`r94_other_routes_table.py`, `r95_series_by_ticker_table.py`). AFTER the apply, BEFORE flipping anything, capture again to `.scratch_be1/thesis_post.json`, compare every route and print
each changed field before and after: the pair's table names every change that may appear, and the response bytes before and after per name are printed (growth may not exceed that
name's `team_sheet` delta; the maximum stays under 6,291,456 bytes with the margin printed; exceeding either is Branch C).
Both scratch branches are KEPT by this order (the issuer deletes them after the post-act reads close).

## 2. BOUNDS

1. The act and nothing else: the writes named, for the keys named; no function, role, route, schedule or other prefix beyond what the act names.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
5. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
6. 49 Financial data never goes into another firm's tree. The thesis captures stay local and uncommitted.
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
  <criterion id="AC1" cell_refs="AMGT-be-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round97_prep/checks/r97_sector_serve_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where deployed; echo "exit=$?"</invocation><expect>bd-1's serve is KEPT and nothing else of the round-97 reading moved: R97 SECTOR SERVE CENSUS: YES (6 of 6: SAN FP and CSL AU serve their listing sector with source and date), R95 CLASSIFICATION CENSUS: YES (6 of 6, the classification still withheld), R94 NAME CENSUS: YES (C1, C3, C4 at 0); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-be-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw4_compare.py" ".scratch_be1/thesis_pre.json" ".scratch_be1/thesis_post.json"; echo "exit=$?"</invocation><expect>AMGT_CORPUS's served effect, Branch A: `aw4 names 95 team_sheet_equals_stored13 95/95 others_equal 95/95`, the max response under 6,291,456 bytes with its margin, `growth_exceeds_delta 0`; `aw4 compare build 1/1`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-be-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/13 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_minor_unit_census.py" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_casing_deployed.py"; echo "exit=$?"</invocation><expect>the no-regression arm: R89 PEERS DEPLOYED: YES and R89 DEPLOYED CLOSE: YES (the package's dossier METHOD is now /13), R92 MINOR-UNIT CENSUS: YES, R95 CASING DEPLOYED: YES, with the function's CodeSha256 re-read, now DIFFERENT from IpaCHo5h.. (the act's own change); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and the recorded VersionIds (or the kept package's hash) as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-be-1.redeploy-the-scoped-api-carrying-the-13-corpus-files-from-a-merged-pin.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the change-management entry's slug and state;
- every criterion's output lines;
- the post-act compare file path, with the changed-path count, the response bytes per name (min, median, max, margin) and the count outside the table;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-97 analysis `ledger/ROUND_ANALYSIS.round97.md` section 2 item 1: "AMGT_CORPUS's served-effect leg from a MERGED pin, FIRST: it carries `dossier.py` at /13, or at /14 if ax-6's write reads Branch A and the aw-4 half is restated and re-signed BEFORE this issuance is cut. It does not wait for /14. The build's admission table must show bd-1's two blobs UNCHANGED. It retires both scratch pins. Its post-act read prints before and after response bytes per name, within the aw-4 bounds." STAGED. THE GO WAITS ON ALL OF: (1) THE PAIR, whose COO half is written from a route-by-route measurement of the merged pin against the live function (the four table scripts run from the PIN'S OWN worktree, as round 97 did; the admission table by blob over every member the pin changes, including other projects' (`opal_naming.py` by the builder replay, `analyze.py` producer-side, `infra/logic/registry/exemptions.json` and `name_rulings.json`); the writer census; both branches; the kept package), the CTO half signed on that table; (2) AMGT_CORPUS's served-effect half (the aw-4 CTO half: signed at /13 with ADDENDA 1-2) and `2.0.0_SA_COO~C1`'s pre-act capture taken immediately before the GO; (3) the pin: the issuer names its hash in the GO and re-reads that its `scoped_amgt.py` and `monthly_chatter.py` are bd-1's. The /14 write (AMGT_CORPUS `ax-6`) is NOT waited for. After the apply, the two scratch branches (`scratch/r95-aa5-pin`, `scratch/r97-bd2-pin`) are superseded and the issuer deletes them (the CTO: "their branches may then be deleted").

<status>pending -- GO 2026-10-11T22:0xZ by the issuer (2.0.0_SA_COO~R1) to 0.7.0_AE_CloudOps~RA1. Pair: COO half @926aa022b4 (ledger/NEVER_WIDEN_ROUND98_CORPUS13_REDEPLOY_COO_HALF.md), CTO half signed (CTO msg 4135, ledger/NEVER_WIDEN_ROUND98_CORPUS13_REDEPLOY_CTO_HALF.md). BUILD PIN a03d92221a, a box/dell1 first-parent commit (merged; NOT box/dell1 HEAD, NOT either scratch pin). GO conditions: (1) in a DETACHED worktree at a03d92221a, `r94_admission_table.py a03d92221a --pin 08d5ea2920` shows exactly the six lib members of the half's table at those blobs (dossier.py 13463426d0da, opal_naming.py 3902e0e93ee4, team_sheet.py 956e69d7be7e, template.py e03d6a8acf65, factset_descriptions.json 76faa8d6a708, analyze.py bf1d15b14ba1) and the two registry files, with scoped_amgt.py 9b13bf0371d4 and monthly_chatter.py 38e9511ccc9c byte-equal to the live package (a seventh member, or either api blob different, is a STOP), and `r94_naming_replay.py --pin 08d5ea2920` reads YES; (2) the kept live package IpaCHo5h.. downloaded and hash-checked before the apply, and the pre-act capture `aw4_capture.py` (95 names) taken by RA1 immediately before it; (3) the payload bound is graded on the LIVE post-act read, live before vs live after (both python3.11): a name whose live growth exceeds its own team_sheet delta, a response over 6,291,456 bytes, or any path outside model.team_sheet and the generation clocks is Branch 2 (STOP, rollback unless the CTO names KEEP). The float_repr paths of the pair are the measuring runtime's, never expected live. Both scratch branches are KEPT by RA1; the issuer deletes them after the compare reads Branch 1.</status>
<round>98</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
