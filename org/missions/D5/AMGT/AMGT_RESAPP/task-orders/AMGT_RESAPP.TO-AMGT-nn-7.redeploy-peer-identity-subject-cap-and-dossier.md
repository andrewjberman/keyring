# AMGT_RESAPP task order -- `AMGT-nn-7` -- REDEPLOY THE SCOPED API CARRYING PEER IDENTITY, THE SUBJECT CAP VINTAGE AND THE AMGT_CORPUS DOSSIER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-nn-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only.
comp-adversary: RUN at the cut -- live KlosR/ap8O (pin 4d006edc74, dossier /10) after round 88; the two serve-time decorators read through readers the function already has (`_resolve_held_form`, `_read_model_block_pool`), so no IAM moves; r89_peers_deployed.sh and r89_deployed_close.sh FAIL at the base as expected (peer identity 0 of 7; subject cap on 2026-09-19; dossier reads /10).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-nn-7` (round 89, decomposition s.97)

CTO~DELL1 round-88 analysis item 8 (with items 3 and 4). ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED
worktree at the build pin the GO names (a box/dell1 commit carrying `AMGT-nn-2` and `AMGT-nn-3` and AMGT_CORPUS's dossier method).
Before the apply, print the CONTENT-DIFF of the built package against the kept live package (`KlosR/ap8O..`, downloaded and
hash-checked); any member the pair's BLAST RADIUS does not admit is a STOP. Rollback: the kept live package through the module, one
`safe-apply`, same hour. Change-management entry opened before, closed after. The record step: run `record-terraform-deploy.sh` so the
function's entry in `infra/aws/lambda/ci/lambda-source-map.json` reads THIS deploy's CodeSha256, commit and time, and print the entry
before and after. Run AC1 in the build worktree (HEAD = the pin).

## 2. BOUNDS

1. The act and nothing else: this function's code; no IAM, route, memory, schedule or store write.
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
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-nn-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for m in lib/research/api/scoped_amgt.py lib/research/peers/listed_identity.py lib/research/peers/subject_cap.py; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round88_prep/checks/r88_package.py" --member "$m" --ref HEAD; done; echo "exit=$?"</invocation><expect>in the build worktree (HEAD = the pin), each of the three members is present in the deployed package and byte-equal to the pin's (K1 and K2 PASS three times, R88 PACKAGE: YES three times), and the function's CodeSha256 differs from KlosR/ap8O3..; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-nn-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh"; echo "exit=$?"</invocation><expect>on the live function every resolvable United States peer of ASML serves its MEASURED identity (R89 PEER IDENTITY: YES) and the subject cap equals the current model block's (R89 SUBJECT CAP: YES); R89 PEERS DEPLOYED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-nn-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/11; echo "exit=$?"</invocation><expect>the live package's dossier.py METHOD_VERSION reads amgt-corpus-dossier/11 (P1 PASS), no FAILED description carries a sentence and every drafted name answers (R87 WITHHELD AC1: YES), typed ASML still resolves and the rest are byte-equal (R84 LISTING AC1: YES); R89 DEPLOYED CLOSE: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-nn-7.redeploy-peer-identity-subject-cap-and-dossier.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the build pin;
- the content-diff in full, each member with its admission;
- base and new CodeSha256;
- every criterion's output lines;
- the source-map entry before and after;
- the change-management entry's slug and state;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-88 analysis @6ad172c28d item 8 (the one redeploy; not cut a second time in round 90). Pair: COO half `ledger/NEVER_WIDEN_ROUND89_NN7_COO_HALF.md` (this issuance); the CTO's half is owed and names AMGT_CORPUS leg p's modules. STAGED. THE GO WAITS ON ALL OF: (1) `AMGT-nn-2` and `AMGT-nn-3` terminal and merged; (2) AMGT_CORPUS reporting its legs w and v done; (3) `CRPS-at-4`'s master-template read in (the method is /12 if it finds the master, else /11 -- the GO re-points AC3's `--want` and the post-act reads); (4) the CTO half signed; (5) the issuer's own re-run of AC2's local arm on the merged tree. It is a dependency between two projects, never a wait on time. Item 2 (D1-S14) is NOT in this order: no store holds a currency for a non-held peer (decomposition s.97a). Checks dry-run at the base: AC1 FAIL (HEAD differs from the live member); AC2 FAIL (peer identity 0 of 7; cap on 2026-09-19); AC3 FAIL (P1: reads /10, R87 and R84 PASS).

<status>staged</status>
<round>89</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<status>staged -- AMENDMENT 1 (issuer, 2026-10-11T04:2xZ): the pair is complete -- CTO~DELL1 half SIGNED @7d031abbc4 (ledger/NEVER_WIDEN_ROUND89_NN7_CTO_HALF.md, msg 3466). Conditions 1-4 of the COO half bind, and the CTO half adds: the build pin's bytes for lib/research/corpus/dossier.py (blob 1ad2fc824173), lib/research/corpus/team_sheet.py (9a6bf6a19381) and lib/research/api/scoped_amgt.py (cbccb2d08b3f) must equal those blobs, a differing blob is a STOP (AC1's package check reads scoped_amgt.py byte-equal to the pin; the applier prints all three blobs at the pin before the build); the dossier method is /11 (CRPS-at-4 found no master template, no /12; AC3's --want amgt-corpus-dossier/11 stands); CONDITION 5: AMGT_CORPUS's leg p pair reads SIGNED by both halves before the GO. THE GO WAITS ONLY ON: (a) that pair, and (b) AMGT_CORPUS's pin ask (2.0.0_SA_COO~C1 msg 3449); nn-2 and nn-3 are merged (@a943b1b412) and the issuer re-ran AC2's local arm on the merged tree (R89 PEER IDENTITY YES, R89 SUBJECT CAP YES @04ecb2d528). Graded by to-pipeline-gate on a modification.</status>
<status>pending -- GO 2026-10-11T04:2xZ by the issuer to 0.7.0_AE_CloudOps~RA1. Build pin: box/dell1 @8f2f3339c2 -- issuer-measured: carries AMGT-nn-2 and AMGT-nn-3 (merge @a943b1b412 and @04ecb2d528 are ancestors), AMGT_CORPUS's at-1 drain @3bff293266 and c8f7662637; the three blobs at the pin read dossier.py 1ad2fc824173, team_sheet.py 9a6bf6a19381, scoped_amgt.py cbccb2d08b3f, each EQUAL to the CTO half's table (a differing blob is a STOP); scoped_amgt.py at the pin has 0 imports of team_sheet. Dossier method /11 (no /12). GO conditions MET: CTO half @7d031abbc4 (msg 3466); AMGT_CORPUS's leg p pair SIGNED by both halves, COO half @53e92c0f89 and CTO half @cba65ded11 (CTO msg 3473, C1 msg 3474), so condition 5 is met. Pair: COO ledger/NEVER_WIDEN_ROUND89_NN7_COO_HALF.md @16d359ecc3; CTO half @7d031abbc4; the leg p pair is AMGT_CORPUS's. Binding: the COO half's conditions 1-4 (ancestry read at the pin by the applier; the whole content diff printed before any upload; AC2 and AC3 after the act with the function's CodeSha256 re-read in the same output; the source-map record step with the entry before and after). Rollback: the kept KlosR/ap8O.. package, same hour; it serves dossier /10. Report to the issuer; AMGT_CORPUS (2.0.0_SA_COO~C1) reads TSM US, SAN FP and ROG SW on the live function after it closes. Graded by no gate limb (a modification).</status>
