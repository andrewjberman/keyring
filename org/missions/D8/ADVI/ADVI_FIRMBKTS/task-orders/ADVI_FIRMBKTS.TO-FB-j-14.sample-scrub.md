# ADVI_FIRMBKTS task order -- `FB-j-14` -- THE TEN-ADVISOR SAMPLE FILES HOLD NO RAW RELATIONSHIP ID (SCRUB FORWARD, HASH AT WRITE TIME)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-14</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two record files in the tree; no cron, rule, schedule or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act and no grant.
comp-adversary: RUN by the issuer -- at base `scrub` reads FAIL on the two files (3 and 2 raw ids, found by the issuer); a file with every id replaced by a hash reads OK. Blindness: the scrub proves no `z`-prefixed id of six or more digits remains in these two files; it does not rewrite history (the CTO: that is Andrew's word, and he recommends against it).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-j-14` (round 7; the CTO's ruling, msg 4747: "have FB1 hash the relationship ids in its files now, and hash at write time from now on")

`DRYRUN10_ARTIFACTS.json` and `DRYRUN10_FIGURES.json` (your `FB-j-10`, commit `acbc7c99d6`) hold raw relationship ids of the form `z` followed by
digits inside the `top_nna_mover` bullets and their figures; the commit is already on `origin/box/dell1`. No history is rewritten. You scrub
FORWARD and change how you write from now on:

1. In both files replace EVERY raw relationship id (the pattern `z[0-9]{6,}`, a standalone token, in strings, keys and figure values) by
   `h_` plus the first 12 hex characters of `sha256(<the raw id>)`, the same replacement everywhere in a file (so a reader can still see that two rows
   name one relationship), including inside the `headline` and `detail` texts. Do not change any other character or number.
2. From now on, in every record and sample file you write under this project, hash relationship ids AT WRITE TIME (never write the raw
   form to disk), starting with `FB-j-13`'s `SLOT_SWITCH_ARTIFACTS.json` and `SLOT_SWITCH_FIGURES.json`.
3. Commit the two files in ONE commit. The mapping from raw id to hash is NOT written anywhere.

## 2. BOUNDS

1. Two files edited, one commit; no other file, no AWS call, no push beyond the usual integration.
2. If a file holds a different shape of identifier (an account number, a client name), do NOT print it: record its COUNT in a surprise row.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN10_ARTIFACTS.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN10_FIGURES.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-14.sample-scrub.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-14"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py scrub --files org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN10_ARTIFACTS.json org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN10_FIGURES.json</invocation><expect>^SCRUB: OK files=2 ids=0$</expect></criterion>
</proof_of_spec>

AC1 reads the two files for any raw relationship id.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-14.sample-scrub.proof_of_spec.json`. Commit the two files FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes.
Row ids `ADVI_FIRMBKTS-D1-S<k>`. Report once to `2.0.0_SA_COO~B1`: AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's msg 4747 (ADDENDA 4-5 of his FB-j-6 half): "the DRYRUN10 files are ALREADY on origin; FB1 scrubs forward now; hash at write time
from now on; no history rewrite (Andrew's word; I recommend against it)." The issuer's own scan: `z`-prefixed ids of six or more digits appear in
those two files (5 occurrences) and, as S3 key path components, in older tables (`mapping*.json`, `F7_DELTA_ROLLBACK.tsv`, round close pairs): those are the
estate's own key names, not served text, and are NOT this order's scope. Class WORLD only by the privacy of the content; no served change.

<status>complete</status>
<round>7</round>
<workstream>SAMPLESCRUB</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-14</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
