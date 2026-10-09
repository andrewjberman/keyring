# AMGT_RESAPP task order -- `AMGT-mm-4` -- REDEPLOY THE SCOPED API CARRYING AMGT-MM-3 (THE WATCHLIST SELECTOR CONTRACT AND THE FILING-SENTENCE FLAG)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-mm-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only.
comp-adversary: RUN at the cut -- live b7Lj1J (pin 9c32fb942d) after round 87; the schema change in mm-3 is read by the reader's validator at request time, so every stored draft must still validate (the five drafts carry generated true today).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-mm-4` (round 88, decomposition s.96)

CTO~DELL1 round-87 analysis items 3 + D1-W345-S2 (deploy half). One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a
DETACHED worktree at the build pin the GO names (a box/dell1 commit carrying AMGT-mm-3). Before the apply, print the CONTENT-DIFF
of the built package against the kept live package (`b7Lj1J`, downloaded and hash-checked); any member the pair's BLAST RADIUS does
not admit is a STOP. Rollback: the kept live package through the module, one `safe-apply`, same session. Change-management entry
opened before, closed after. Run AC1 in the build worktree (HEAD = the pin).

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
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-mm-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round88_prep/checks/r88_package.py" --member lib/research/api/scoped_amgt.py --ref HEAD; echo "exit=$?"</invocation><expect>in the build worktree, the deployed scoped_amgt.py is byte-equal to the pin's; K1-K2 PASS; R88 PACKAGE: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-mm-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round87_prep/checks/r87_withheld.py" --crit AC1; echo "exit=$?"</invocation><expect>on the live function no FAILED description carries a sentence and every drafted name answers with the section (every stored draft still validates under the new schema); W1-W2 PASS; R87 WITHHELD AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-mm-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_listing.py" --crit AC1 --where deployed; echo "exit=$?"</invocation><expect>a typed ASML still resolves to ASML_NA_Equity, Micro still lists, the other answers byte-equal; R84 LISTING AC1: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-mm-4.redeploy-the-selector-refusal-and-filing-sentence-flag.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the build pin;
- the content-diff in full, each member with its admission;
- base and new CodeSha256;
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-87 analysis items 3 + W345-S2 (deploy). Pair: NEW -- COO half `ledger/NEVER_WIDEN_ROUND88_MM4_COO_HALF.md` (this issuance); CTO~DELL1's half owed. STAGED: GO waits on AMGT-mm-3 merged and the CTO half. Checks dry-run at the base: AC1 base PASS (nothing new merged yet: the live member equals HEAD) -- it discriminates once mm-3 merges (then FAIL until the redeploy); AC2, AC3 base PASS (bounds).

<status>staged</status>
<round>88</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<status>staged -- AMENDMENT 1 (issuer, 2026-10-09T20:4xZ) on row AMGT_RESAPP-D1-S19: the round-87 redeploy b7Lj1J was never recorded -- infra/aws/lambda/ci/lambda-source-map.json still reads HZoC2x (round 85). This order's deploy runs its record step (record-terraform-deploy.sh, as jj-5 did) so the function's entry reads THIS deploy's CodeSha256, commit and time; the report prints the entry before and after. Criteria unchanged. Graded by to-pipeline-gate on a modification.</status>
<status>staged -- AMENDMENT 2 (issuer, 2026-10-09T20:5xZ): the pair is complete -- CTO~DELL1 half SIGNED (ledger/NEVER_WIDEN_ROUND88_MM4_CTO_HALF.md @53232200a1, msg 3148). Its five conditions bind: (1) the GO waits on AMGT-mm-3's L9 grade (the CVO, not the issuer); (2) the pin carries mm-3 and dossier /9, with r87_dossier and r87_withheld re-run live; (3) pre-act, every stored draft validates under the new schema, denominator printed; (4) post-act, one refused OPAL_GLOBAL off-list selection plus two byte-equal reads (absent selector; a firm principal's selection); (5) the whole content diff printed first. AMENDMENT 1's record step stands. Criteria unchanged. Graded by to-pipeline-gate on a modification.</status>
<status>staged -- AMENDMENT 3 (issuer, 2026-10-09T21:1xZ): CTO~DELL1 mm-4 half ADDENDUM 1 @c2b5454449 (msg 3185) replaces condition 4 -- after the act an off-list selected_tenant reads byte-equal to the absent-selector read, plus one unselected request byte-equal to pre-act; the selector has ONE branch, so any selector-handling change in the content diff is a STOP (AMGT-mm-3 part (a) dismissed, AMENDMENT 1 of mm-3). Conditions 1-3 and 5 stand; the GO still waits on the CVO's L9 grade of mm-3. Graded by to-pipeline-gate on a modification.</status>
