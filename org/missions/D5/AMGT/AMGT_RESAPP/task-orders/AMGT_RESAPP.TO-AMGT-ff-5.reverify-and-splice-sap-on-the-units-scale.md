# AMGT_RESAPP task order -- `AMGT-ff-5` -- RE-VERIFY SAP'S STORED DRIVER ON THE UNIT'S SCALE AND SPLICE IT INTO THE DRAFTING OBJECT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ff-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ff-5.reverify-and-splice-sap-on-the-units-scale</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two operator-run store writes, no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- the caller's own credentials write two prefixes the producers already write; no role or policy moves.
comp-adversary: RUN at the cut -- r92_driver_reverified.py --write-set SAP_GY_Equity reads NO at the base (R1: SAP serves 0, expects 0 under ss-2 and 3 under ff-3), its controls PASS; r94_rescale_table.py is the worker's table (candidate YES).
EGRESS CLASS, declared: NONE (S3 reads and puts; no vendor, SEC or model call).
</preflight>

## 1. THE ACT -- `AMGT-ff-5` (round 94, decomposition s.102)

CTO~DELL1 round-93 analysis item 4, second half. `AMGT-ff-3` (merged before this GO) shows a mixed-scale point set on the series unit's scale; the re-verification
of SAP now keeps 3 points (2023 = 13.745, 2024 = 18.078, 2025 = 21.05, EUR billions, each with its stated scale), where round 93's ss-4 left SAP empty. Two
ordered store writes, for ONE name, from the checkout at the GO's pin, each preceded by its dry run (round 93's ss-4 is the model):

1. `python -c "from lib.research.filings import analyze; print(analyze.reverify_stored_thesis_driver('SAP_GY_Equity', '000110465926020058', dry_run=False)[2])"`
   rewrites `filings/v1/SAP_GY_Equity/000110465926020058.analysis.json` at its own key (`crosswalk.write_pool`, an ETag-conditional OVERWRITE kept as a VersionId).
2. `python -m lib.research.filings.drafting_build --splice-driver --dry-run --only-keys SAP_GY_Equity` must read `served_validator=True` and move
   `thesis_driver` and `thesis_driver_provenance` only; then the same with `--pre-act-dir <dir>` and without `--dry-run`.

BEFORE step 1 record the VersionIds of both objects (the rollback list, in the change-management entry), print `r94_rescale_table.py` and the dry splice, and
sweep every live worktree's open deploys for entries naming `filings/v1` or `drafting/v1` (per-tree denominator). Open a change-management entry first and close it
last. Rollback, if the CTO names it: copy each recorded prior VersionId to the same key (never a delete).

## 2. BOUNDS

1. The act and nothing else: the writes named, for the keys named; no function, role, route, schedule or other prefix beyond what the act names.
2. No S3 delete, ever. No Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
5. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
6. 49 Financial data never goes into another firm's tree.
7. A change the pair's table does not name is a STOP and, inside the same hour, a restore of the recorded VersionIds (or, for a code leg, the kept package) unless the CTO names KEEP on the evidence.
8. The write set is `SAP_GY_Equity` only. ASML and BABA are NOT touched.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ff-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_sap_served.py"; echo "exit=$?"</invocation><expect>PASS V1 (SAP serves 2023 = 13.745, 2024 = 18.078, 2025 = 21.05, each with its stated scale and value), PASS V2 (ASML none), PASS V3 (BABA FY2025 and FY2026); arms passed 3 of 3; R94 SAP SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ff-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/11; echo "exit=$?"</invocation><expect>the no-regression arm: R89 PEERS DEPLOYED: YES and R89 DEPLOYED CLOSE: YES (dossier /11, the withhold and the listing byte-equal) with the function's CodeSha256 re-read; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and the recorded VersionIds as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ff-5.reverify-and-splice-sap-on-the-units-scale.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the dry-run and live output lines of every step;
- the VersionId list's file path;
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (issuer, 2026-10-11, on RA1's finding of 13:16Z):** AC1 took its expected points from a production re-verification of the stored object, and a re-verification of an object whose points already carry rescaled values keeps 1 of 3 (row `AMGT_RESAPP-D1-S24`: `reverify_stored_thesis_driver` reads `value`, not `stated_value`), so it could not read YES after its own write; the writes were correct (served: SAP 3 points, ASML none, BABA 2). AC1 now reads the live /thesis route against the pair's table (`r94_sap_served.py`). An issuer check gap: ff-3's checks had no idempotence arm. Gate limb: none grades a criteria edit on an issued order.

**ISSUER NOTES:** CTO~DELL1 round-93 analysis @bfa6b04c8c item 4. STAGED. THE GO WAITS ON: (1) `AMGT-ff-3` terminal and merged, with the issuer's `r94_rescale_table.py` and a re-read of SAP's would-be points on the merged code; (2) the pair, the COO half written from that re-read (key, accession, stored points, expected points with stated scale, both VersionIds, the writer census as round 92's qq-4 and round 93's ss-4) and the CTO half signed; (3) the sequencing rule: this act and `AMGT-ff-4` never share a window. The visible effect, for the pair: SAP's driver chart goes from empty to three points on EUR billions. NOTE for the pair: the series unit text reads 'billions' and the claim is the NTM-cloud-backlog series (SAP, P0344); the splice's served validator is the control.

<status>staged</status>
<round>94</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<status>complete -- 0.7.0_AE_CloudOps~RA1, 2026-10-11T13:3xZ. GO msg 3868 (run pin ae728f0680). Step 1 rewrote filings/v1/SAP_GY_Equity/000110465926020058.analysis.json (0 -> 3 points on EUR billions: 2024 18.078, 2023 13.745, 2025 21.05, each keeping stated_value, stated_scale and rescaled_to; the conversion stated by the filing); step 2 spliced thesis_driver and thesis_driver_provenance into drafting/v1/SAP_GY_Equity.json, served_validator=True, SPLICED 1 of 1. 24 objects of the 12 names re-headed: exactly 2 VersionIds moved (SAP's), 22 unchanged, ASML and BABA untouched. r94_rescale_table.py and the 12-row dry re-verification on the GO day equalled the half's table. AC1 as first written read NO (a re-verification of the rescaled object keeps 1 of 3: the verifier is not idempotent, row D1-S24; finding @56a8cd9e37); the CTO ruled ACCEPT (msg 3886) and the issuer's AMENDMENT 1 @090b13df6d made AC1 read the served route against the pair's table; the amended AC1 re-ran literally on a checkout at that commit: R94 SAP SERVED: YES (V1-V3). AC2 YES with the function CodeSha256 unchanged. SAP's analysis object is NOT re-verified by anyone until the idempotency cell lands. Ledger amgt-resapp-r94-ff5-sap-rescale-dell1 CLOSED 8 of 8. Proof instance deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ff-5.reverify-and-splice-sap-on-the-units-scale.proof_of_spec.json VALID rc=0.</status>
