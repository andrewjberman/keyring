# AMGT_RESAPP task order -- `AMGT-kk-1` -- RE-PUBLISH TODAY'S NAME LIST WITH ITS RESEARCH-FOLDER COUNT, UNDER JJ-4'S PAIR, WITH THE PRE-PUBLISH DIFF WIDENED TO EVERY TOP-LEVEL FIELD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-kk-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one hand-run publish.
comp-iam: RUN by round85_prep/GROUP_LISTING_BUILD_NOTES.md -- the writer's existing grant on crosswalk/v1/; no grant moves.
comp-adversary: RUN at the cut (round86_prep/GROUP_REPUBLISH_NOTES.md) -- the published 2026-10-09.json carries research_universe absent (2026-10-07.json held 97 folders): crosswalk.main reads the research library and, on LibraryAbsentError, publishes absent (crosswalk.py:975-990, :1606); dell1 has no library root. --write-pool overwrites today's key when the content differs (IfMatch).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-kk-1` (round 86, decomposition s.94)

CTO~DELL1 round-85 analysis R1 (row W341-S1). Re-write `s3://opal-data-harvest/crosswalk/v1/2026-10-09.json` with the crosswalk's
own `--as-of 2026-10-09 --write-pool`, run WHERE THE RESEARCH LIBRARY IS READABLE (the laptop's Opal Research folder, or
`OPAL_RESEARCH_LIBRARY_ROOT` pointed at a synced copy -- the GO names the box and the root), so `research_universe` carries its
folder count. BEFORE the put print the WIDENED pre-publish diff: every top-level field (and every key one level inside a top-level
object) of `2026-10-07.json` present with an equal value or a printed, admitted change, plus the record checks (243 kept, issuer
unchanged). Record the prior VersionId; rollback is a versioned re-put of the prior bytes, never a delete. Read
`round86_prep/GROUP_REPUBLISH_NOTES.md` whole first.

## 2. BOUNDS

1. The act and nothing else: today's crosswalk key only, no other store write, no deploy, no schedule.
2. No S3 delete, ever.
3. No Bloomberg call. No `bun`, `npm` or `pip install`.
4. Standing: no push of shared branches.
5. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal
   outside the runner's own job, is told to the laptop FIRST.
6. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
7. 49 Financial data never goes into another firm's tree.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-kk-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85_prep/checks/r85_crosswalk.py" --crit AC1 --reference crosswalk/v1/2026-10-07.json --admit as_of,denominators.with_issuer_cik,research_universe.read_at,research_universe.folders,denominators.research_folders_live; echo "exit=$?"</invocation><expect>the latest stored name list keeps every record, carries issuer.cik as before, and every top-level field of 2026-10-07.json is present with an equal value or an admitted change, with research_universe.folders 1 or more; C1-C5 PASS; R85 CROSSWALK AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-kk-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_listing.py" --crit AC1 --where deployed; echo "exit=$?"</invocation><expect>a typed ASML still resolves to ASML_NA_Equity, Micro still lists, the other answers byte-equal; R84 LISTING AC1: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-kk-1.republish-the-name-list-with-research-folders.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the commit hash;
- the box and library root used, the folder count;
- the widened pre-publish diff in full;
- prior and new VersionIds;
- every criterion's output lines;
- the change-management entry's slug and state.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-85 analysis @2b173f8e66 R1 (the widening binds every later crosswalk publish). Under jj-4's pair (COO @263271c6db + CTO @29112515f4; its condition 3 named the same-key rewrite). STAGED: the GO names the executing box and library root (dell1 has none). Checks dry-run at the base: AC1 base FAIL as expected (C5: 6 fields not admitted, folders None); AC2 base PASS (a bound).

<status>staged</status>
<round>86</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
