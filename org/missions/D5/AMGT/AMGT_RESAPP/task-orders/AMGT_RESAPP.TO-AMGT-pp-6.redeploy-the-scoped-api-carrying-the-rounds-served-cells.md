# AMGT_RESAPP task order -- `AMGT-pp-6` -- REDEPLOY THE SCOPED API CARRYING THE ROUND'S SERVED CELLS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-pp-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-pp-6.redeploy-the-scoped-api-carrying-the-rounds-served-cells</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one code leg.
comp-iam: DECLARED-NOT-APPLICABLE -- the function's code only; the new decorator reads through the held-name index and the crosswalk the function already reads.
comp-adversary: RUN at the cut -- live l8egBo/rf.. (pin a943b1b412) after round 89; r91_name_match_deployed.py reads 18 candidate members across the 243 subjects' latest peers objects and 0 served (R91 NAME MATCH DEPLOYED: NO) at the base, with 0 leaked.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-pp-6` (round 91, decomposition s.99)

CTO~DELL1 round-90 analysis item 6. ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the build pin
the GO names (a box/dell1 commit carrying `AMGT-pp-1` merged, and `AMGT-pp-4` only if the GO says so). Before the apply, print the
CONTENT-DIFF of the built package against the kept live package (`l8egBo/rf..`, downloaded and hash-checked) and, for each member the
pair's BLAST RADIUS table names, its blob at the pin beside the table's column; any member the table does not admit, or a blob that
differs beyond the admitted change, is a STOP. `crosswalk.py` is admitted BY BLOB (the round-89 nn-5 guard; the function never calls
it). Rollback: the kept live package through the module, one `safe-apply`, same hour. Change-management entry opened before, closed
after. The record step: run `record-terraform-deploy.sh` so the function's entry in `infra/aws/lambda/ci/lambda-source-map.json` reads
THIS deploy's CodeSha256, commit and time, and print the entry before and after. Run AC1 in the build worktree (HEAD = the pin).

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
  <criterion id="AC1" cell_refs="AMGT-pp-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for m in lib/research/peers/numeric_tickers.py lib/research/api/scoped_amgt.py lib/research/peers/price_currency.py lib/research/identity/crosswalk.py; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round88_prep/checks/r88_package.py" --member "$m" --ref HEAD; done; echo "exit=$?"</invocation><expect>in the build worktree (HEAD = the pin), each of the four members is present in the deployed package and byte-equal to the pin's (K1 and K2 PASS four times, R88 PACKAGE: YES four times), and the function's CodeSha256 differs from l8egBo/rf..; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-pp-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_peers_deployed.sh" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_deployed_close.sh" --want amgt-corpus-dossier/11; echo "exit=$?"</invocation><expect>the no-regression arm: R89 PEERS DEPLOYED: YES (peer identity and subject cap unchanged) and R89 DEPLOYED CLOSE: YES (dossier /11, the withhold, the listing byte-equal), each with the function's CodeSha256 re-read; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-pp-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round91_prep/checks/r91_name_match_deployed.py"; echo "exit=$?"</invocation><expect>members examined and candidates printed (candidates at least 1), PASS D1 (every candidate serves its held key as company_name), PASS D2 (no company_name match the rule does not predict); R91 NAME MATCH DEPLOYED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-pp-6.redeploy-the-scoped-api-carrying-the-rounds-served-cells.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the build pin;
- the content-diff in full, each member with its admission and its blob;
- base and new CodeSha256;
- every criterion's output lines;
- the source-map entry before and after;
- the change-management entry's slug and state;
- any row.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-90 analysis @b462a02d8a item 6: "one redeploy, STAGED after items 1 and 4"; item 4 is `AMGT-pp-4` (the DEMQUE answer's reader and wiring), which has no order until the answer lands. Pair: COO half `ledger/NEVER_WIDEN_ROUND91_REDEPLOY_COO_HALF.md` (this issuance); the CTO's half is owed. STAGED. THE GO WAITS ON: (1) `AMGT-pp-1` terminal and merged (its AC1/AC2 re-run by the issuer on the merged tree); (2) the CTO half SIGNED, naming each admitted member's blob; (3) the pin's ancestry; (4) AMGT_CORPUS's answer on a riding leg. **THE COUPLING THE ANALYSIS CREATES:** read literally, the GO also waits on item 4, so 18 members' identities wait on a Bloomberg queue's answer that has no quote. The issuer asks the CTO in the round's message whether pp-1 rides alone (AC1's `price_currency.py` and AC3 are written to hold either way; pp-4's wiring would then ride a later redeploy). Not a redeploy per cell: this is the round's one. Checks dry-run at the base (shared tree HEAD, 2026-10-11): AC1 FAIL on `price_currency.py` and `crosswalk.py` (their merged bytes the live package does not carry) and PASS on `numeric_tickers.py` and `scoped_amgt.py` until pp-1 merges; AC2 PASS (the no-regression arm); AC3 FAIL (D1: 18 candidates, 0 served).

<status>staged</status>
<round>91</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<status>staged -- AMENDMENT 1 (issuer, 2026-10-11T07:2xZ): the expected count in AC3 and the record face is 15 candidates, not 18 (AMGT-pp-1's exact-name arm refuses a Class or Series designator; COO half ADDENDUM 1). r91_name_match_deployed.py was amended in step (base: examined 112, candidates 15, served 0, leaked 0: R91 NAME MATCH DEPLOYED: NO). Still STAGED: the GO waits on pp-1 merged (its amended order, re-seated), pp-3's entry closed (CTO sequencing condition), and the re-measure that condition names. Graded by no gate limb (a modification).</status>
