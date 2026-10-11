# AMGT_RESAPP task order -- `AMGT-ss-4` -- RE-VERIFY SAP'S STORED DRIVER UNDER THE MIXED-SCALE RULE AND SPLICE IT INTO THE DRAFTING OBJECT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ss-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ss-4.reverify-and-splice-sap-under-the-scale-rule</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two operator-run store writes, no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- the caller's own credentials write two prefixes the producers already write (`filings/v1/`, `drafting/v1/`); no role or policy moves.
comp-adversary: RUN at the cut -- `r92_driver_reverified.py --write-set SAP_GY_Equity` reads NO at the base (R1: SAP expects 3 points, serves 1) and reads NO after `AMGT-ss-2` only if the write has not landed; its controls PASS. The scale rule's own dry run over all 12 objects (r93_scale_table.py) moves SAP and no other name.
EGRESS CLASS, declared: NONE (S3 reads and puts; no vendor, SEC or model call).
</preflight>

## 1. THE ACT -- `AMGT-ss-4` (round 93, decomposition s.101)

CTO~DELL1 round-92 analysis item 2, second half. Round 92's `AMGT-qq-4` held `SAP_GY_Equity` out of the stored-driver write because its three
re-verified points mix EUR millions with EUR billions. `AMGT-ss-2` (merged before this GO) holds such a set whole, so the re-verification now
keeps 0 points for SAP. Two writes, in order, from the checkout at the GO's pin, each preceded by its dry run, for ONE name:

1. `python -c "from lib.research.filings import analyze; print(analyze.reverify_stored_thesis_driver('SAP_GY_Equity', '000110465926020058', dry_run=False)[2])"`
   rewrites `filings/v1/SAP_GY_Equity/000110465926020058.analysis.json` at its own key (`crosswalk.write_pool`, an ETag-conditional OVERWRITE kept as a VersionId).
2. `python -m lib.research.filings.drafting_build --splice-driver --dry-run --only-keys SAP_GY_Equity` must read `served_validator=True` and move
   `thesis_driver` and `thesis_driver_provenance` only; then the same with `--pre-act-dir <dir>` and without `--dry-run`.

BEFORE step 1 record the VersionIds of the two objects (the rollback list, in the change-management entry), run the pair's dry run and compare it
with the table (SAP 1 -> 0 points), and sweep every live worktree's open deploys for entries naming `filings/v1` or `drafting/v1` (print the
per-tree denominator). Open a change-management entry first and close it last. Rollback, if the CTO names it: copy each recorded prior VersionId
to the same key (never a delete).

## 2. BOUNDS

1. The act and nothing else: the writes named, for the keys named; no function, role, route, schedule or other prefix.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
5. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
6. 49 Financial data never goes into another firm's tree.
7. A change the pair's table does not name is a STOP and, inside the same hour, a restore of the recorded VersionIds unless the CTO names KEEP on the evidence.
8. The write set is `SAP_GY_Equity` only. ASML and BABA were written by round 92 and are NOT touched.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ss-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round92_prep/checks/r92_driver_reverified.py" --write-set SAP_GY_Equity; echo "exit=$?"</invocation><expect>every analysis object is listed; SAP_GY_Equity reads CHANGED with expected 0 point(s) and served equal to it (OK), ASML and BABA and every other name read OK; PASS R1, PASS R2, PASS R5; R92 DRIVER REVERIFIED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ss-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/11; echo "exit=$?"</invocation><expect>the no-regression arm: R89 PEERS DEPLOYED: YES and R89 DEPLOYED CLOSE: YES (dossier /11, the withhold and the listing byte-equal) with the function's CodeSha256 re-read, unchanged; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and the recorded VersionIds as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ss-4.reverify-and-splice-sap-under-the-scale-rule.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the VersionId list's file path;
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-92 analysis @1edd8be57d item 2. STAGED. THE GO WAITS ON: (1) `AMGT-ss-2` terminal and merged, with the issuer's `r93_scale_table.py` and a re-read of SAP's would-be points on the merged code; (2) the pair, the COO half written from that re-read (key, accession, stored points, expected points, both VersionIds, the writer census as qq-4's) and the CTO half signed; (3) the sequencing rule: this act, `AMGT-ss-5` and `AMGT-ss-6` never share a window, and the second and third re-measure against the state the earlier one left. The visible effect, for the pair: SAP's single served point (2024 = 18,078 under a billions unit text) leaves its driver chart. Precedent: round 92's qq-4 (instance, pair, ledger).

<status>staged</status>
<round>93</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
