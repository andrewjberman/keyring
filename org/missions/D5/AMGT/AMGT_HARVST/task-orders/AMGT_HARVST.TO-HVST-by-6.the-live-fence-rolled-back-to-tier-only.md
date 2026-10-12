# AMGT_HARVST task order -- `HVST-by-6` -- ROUND 81, WORKSTREAM DEVREVERT (`1.0.0_SA_CTO~DELL1` msg 4463, `ledger/ROUND_ANALYSIS.round79.md` ADDENDUM 3 @b5915fba35): THE LIVE `opal-research-pull-enqueue` FUNCTION IS ROLLED BACK FROM THE DEV-ADMITTING CODE TO THE TIER-ONLY, REFUSAL-LOGGING CODE OF HVST-by-2

<!-- ===================== SEAT ORDER -- the executing seat reads the whole file ===================== -->

<to_id>AMGT_HARVST.TO-HVST-by-6.the-live-fence-rolled-back-to-tier-only</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-by-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~HV1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- the change is the function's CODE only, back to a state this seat deployed under HVST-by-2. `comp-iam service opal-research-pull-enqueue` is read before and after; no role, policy, route or authorizer changes.
comp-adversary: RUN at L5 -- the adversary is a rebuild from a file that is not 31590746f1's, a package whose source nobody read back (a code hash can differ for identical source, because the zip carries file times), an arm that carries a real ticker, or a rollback that leaves the Dev-admitting clause in the live code.
</preflight>

## 0. THE CELL

`1.0.0_SA_CTO~DELL1` WITHDREW the Dev-admit ruling (msg 4463, ledger `ROUND_ANALYSIS.round79.md` ADDENDUM 3 @b5915fba35): on the laptop
CTO's read (msg 108607) the token's `tier` derives from `firmId`, so an opal-capital Dev login already carries `tier: internal`, and the fence
stays tier-only. The order `HVST-by-5` had already DEPLOYED the Dev-admitting code (your commit @33189f2667, code hash `Q342L4Vn...`,
LastModified 2026-10-12T14:40:46Z) before the withdrawal reached the issuer. **This cell puts the live function back to the code your
`HVST-by-2` deployed, `lambda_function.py` at commit `31590746f1`.** It changes nothing else and adds no code.

**START CONDITION:** none beyond `HVST-by-5`'s ledger being CLOSED (it is). The issuer's lane (`TREE_COO`) cannot write `infra/aws`,
so the repo revert is a step of THIS order, taken by your lane (`CLOUD_OPS_OR_ETL`: any AE agent).

## 1. THE ACT (this box, once)

0. **Revert the repo first, so the tree tells the truth while the live act runs.** In this order: `git checkout 31590746f1 -- infra/aws/lambda/research/pull_enqueue/lambda_function.py`, `git rm infra/aws/lambda/research/pull_enqueue/test_by4_dev_admitted.py`, then run `python -m pytest infra/aws/lambda/research/pull_enqueue -q -p no:cacheprovider --color=no` (expect 22 passed: the 15 bx-1 and 7 by-1 tests), print `git show 31590746f1:<file> | sha256sum` against the working file's, and commit exactly those two paths with `.tools/safe-commit.sh`. Do NOT use `git revert` of the by-4 merge: it would also remove the channel rows and the by-4 proof instance, which are append-only.
1. **Before, read only:** `get-function-configuration` into `by6_before.out` (`CODESHA256`, `LASTMODIFIED`; expected `Q342L4Vn...`), `T0`.
2. **Open the ledger:** `python .tools/deploy_ledger.py open --slug harvst-by6-enqueue-rollback-tier-only-20261012 --title "HVST-by-6 roll
   back opal-research-pull-enqueue to the tier-only code" --author 0.7.0_AE_CloudOps~HV1`, legs `BUILD`, `UPLOAD`, `APPLY`, `ARMS`.
3. **Restore the artifact by VERSION, do not rebuild it** (the CTO's proof, msg 4465: the post-rollback `CODESHA256` must EQUAL the hash
   recorded at by-2's own deploy, `cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo=`; a rebuilt zip carries file times and can hash
   differently for identical source). Read the S3 object version that by-2's apply deployed from `by2_plan.out` (the `s3_object_version`
   after-value of the by-2 plan) or from `by5_before.out`/`by5_plan.out` (the before-value of by-5's plan is that same version), and
   The issuer read it: by-2's plan (`by2_plan.out` line 19) changed `s3_object_version` from `bSNW5xyLGyzTAHsP2xN.9BfjDIT2SF79` to
   **`S9217s5ck1gZJvwSC.Ayeg4vFAkV063z`**, and by-5's plan (`by5_plan.out` line 19) changed it from that value to
   `kwFo21Dq805CaW24uAodJu5WJY.nbvVx` (the Dev-admitting code, `Q342...`). Re-read both before you copy; then
   verify it is a version of `s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip` whose own metadata
   `content-sha256` matches. Then COPY that version over the key so it becomes the latest object with its metadata intact:
   `aws s3api copy-object --bucket opal-313476888478-lambda-artifacts --key research/opal-research-pull-enqueue.zip --copy-source
   "opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip?versionId=<by-2 version>" --metadata-directive COPY`
   (through the `.tools/aws` shim). Record the version id, the copy's response and the new latest version id in `by6_restore.out`.
   If that version is gone, or the copy is refused, DO NOT rebuild silently: stop, file a row with the read verbatim, and tell the issuer
   (the CTO then decides whether a rebuild's different hash is acceptable). `build-and-upload.sh` is not run by this order.
4. **Plan, then read:** targeted at `module.harvest_enqueue`, into `by6_plan.out`: `Plan: 0 to add, 1 to change, 0 to destroy`, the one
   change the code hash. Anything else: STOP and file a row.
5. **Apply once** with `safe-apply`; `by6_apply.out`.
6. **Read the deployed SOURCE back, not only its hash.** `aws lambda get-function --function-name opal-research-pull-enqueue --query
   Code.Location --output text`, download the package, read `lambda_function.py` from it, and write to `by6_package.out`:
   `DEPLOYED SOURCE SHA256 <sha256>`, `EXPECTED SHA256 (31590746f1) <sha256>`, then one line `SOURCE SHA256 MATCHES 31590746f1: yes` or
   `... : no`, a line `REPO FILE SHA256 MATCHES 31590746f1: yes|no` (the working file after step 0), and a line `USERTYPE CLAUSE PRESENT: no` (or `yes`) from a search of the deployed source for `userType`. Also record
   `CODESHA256 <value>` and then one line `CODESHA256 EQUALS BY-2 DEPLOY (cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo=): yes` or `: no`.
7. **The arms on the DEPLOYED function**, each one `aws lambda invoke` with a payload file, **no payload carrying a `ticker`**.
   Write to `by6_arms.out`:
   - `ARM dev_non_internal_tier: statusCode <n>` for `{"requestContext": {"authorizer": {"lambda": {"tier": "advisor", "userType": "Dev"}}}}` (expected **403**: the Dev clause is gone);
   - `ARM advisor_non_dev: statusCode <n>` for `{"requestContext": {"authorizer": {"lambda": {"tier": "advisor", "userType": "Advisor"}}}}` (expected **403**);
   - `ARM no_context: statusCode <n>` for `{}` (expected **403**);
   - `ARM internal_no_ticker: statusCode <n>` for `{"requestContext": {"authorizer": {"tier": "internal"}}}` (expected **400**).
8. **Close the ledger** when all four legs carry proof.

## 2. BOUNDS AND ROLLBACK

- Blast radius: the function's code, once, back to a state already deployed and proved. One population changes: a login admitted only
  by `userType == Dev` with a non-internal tier is refused again. Per the laptop CTO, an opal-capital Dev login already carries
  `tier: internal`, so the count of affected real logins is expected to be zero; NOT measured by this seat.
- Roll forward (should the CTO re-rule): the Dev-admitting code is `git show f94560218c:infra/aws/lambda/research/pull_enqueue/lambda_function.py`.

<paths>
infra/aws/lambda/research/pull_enqueue/lambda_function.py
infra/aws/lambda/research/pull_enqueue/test_by4_dev_admitted.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-by6-enqueue-rollback-tier-only-20261012.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-by-6"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round81/by6_arms.out</invocation><expect>(?s)ARM dev_non_internal_tier: statusCode 403.*ARM advisor_non_dev: statusCode 403.*ARM no_context: statusCode 403.*ARM internal_no_ticker: statusCode 400</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-by-6"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round81/by6_package.out</invocation><expect>(?s)SOURCE SHA256 MATCHES 31590746f1: yes.*REPO FILE SHA256 MATCHES 31590746f1: yes.*USERTYPE CLAUSE PRESENT: no.*CODESHA256 EQUALS BY-2 DEPLOY .cWiraC3E[^)]*.: yes</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-by-6"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round81/by6_plan.out</invocation><expect>Plan: 0 to add, 1 to change, 0 to destroy</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. Write every `.out` file under
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round81/`.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS (about 500 CRLF lines).** Append a row by BYTES and check the diff reads N insertions.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/AMGT_HARVST.TO-HVST-by-6.the-live-fence-rolled-back-to-tier-only.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-by-6.the-live-fence-rolled-back-to-tier-only`.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ`; mint the next free `AMGT_HARVST-D1-S<n>` (the gate refuses a lane tag).
- Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
   This order writes the code artifact bucket and one Lambda only.
2. 49 Financial data never goes into another firm's tree. This order touches none.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4463: "Take by-4 to a terminal state without merge, and revert it if it has merged ... The by-5 CTO
  half is VOID ... by-2 and by-3 stand." The live deploy had already happened (14:40:46Z) because the STOP reached the issuer at 15:30Z.
  The rollback restores the artifact `HVST-by-2` deployed under its signed pair (COO @49b5ed47f3 and the CTO's halves
  `ledger/NEVER_WIDEN_ROUND81_BY2_BY3_CTO_HALVES.md`), so no widening act is performed. Told to the CTO in msg 4463's reply.
- The AC2 source read answers a trap named in the preflight: a rebuilt zip's code hash can differ for byte-identical source.
- by-4 is cancelled and its code reverted in the commit that carries this order; by-5 is cancelled (its deploy stands in the record).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>81</round>
<workstream>DEVREVERT</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>

**COMPLETE 2026-10-12 ~15:5xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** `0.7.0_AE_CloudOps~HV1` @37e6f3cdea (the repo revert: `lambda_function.py` back to its `31590746f1` bytes, `test_by4_dev_admitted.py`
  removed, 22 tests passing) and @a373db5f1d (the deploy record), both on box/dell1 HEAD. Proof VALID rc 0 at HEAD (re-run by this seat
  with `--governing-order`). Ledger `harvst-by6-enqueue-rollback-tier-only-20261012` CLOSED.
- **Restored by VERSION, not rebuilt** (the CTO's proof, msg 4465): S3 object version `S9217s5ck1gZJvwSC.Ayeg4vFAkV063z` (read from by-2's
  plan, its own metadata `content-sha256` verified) was copied to be the latest object (new version `pHqpZEyj...`). The function's
  `CODESHA256` is `cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo=`, EQUAL to by-2's deploy; before it read `Q342L4Vn...` (by-5).
- **AC1 PASS** the four deployed arms read 403 (Dev with an advisor tier: the clause is gone), 403, 403, 400. **AC2 PASS** the served
  package's `lambda_function.py` sha256 equals `31590746f1`'s (`1778584a...`), the repo file equals it too, no `userType` clause.
  **AC3 PASS** the plan `0 to add, 1 to change, 0 to destroy`.
- **Window of exposure, measured by the seat:** the Dev-admitting code was live from 14:40:46Z to 15:38:20Z. In 14:40 to 15:39Z, 0 real calls
  reached the function (log read). The CTO's own read: nil under his PRE-1. Not an incident.
- **State of the fence now:** `tier == internal` only, no context 403, a refusal writes `DENIED: tier=<tier>` (by-1 and by-2, standing).

<status>complete</status>
