# TO POSN_ASTTAX.TO-V9-1 -- THE EDGE ROUTER ADMITS `holdings.json` AND `characteristics.json` on `/api/scoped/satellites/` (a leaf ALLOWLIST beside `registry.json`; the refusal branch kept), published and associated through Terraform under the two B5 halves -- FIVE behaviors move, four of them must read identical (AT5-s-9, B5; the READ PATH for FWD-6 on the Satellites mode)

<to_id>POSN_ASTTAX.TO-V9-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~23</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-14</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.7** @`99cc431075`
(C-SATELLITE-SOURCE's read path; C-DONE) - **Decomp cell:** `AT5-s-9` - **Issuance:** round 5, wave 1. Andrew-approved ~18:1xZ
(record @`730b3309fa`, msg 22888). **GATES `AT5-s-7` (F3), `AT5-s-8` (R1).**

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~23`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~23;`. First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`. Commit only via
`bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_ASTTAX~23 <0.9.0_WK_POSN_ASTTAX~23@opal.agent>" -F <msgfile> -- <paths>`,
msgfile by the Write tool, PURE ASCII. Never push, merge, rebase, `checkout --`, `clean`.

## THE CELL

Measured at the cut: `infra/aws/lambda-edge/shared-advisor-router/index.mjs:95-101` defines `SATELLITES_PREFIX
"/api/scoped/satellites/"`, `SATELLITES_REGISTRY_LEAF "registry.json"`, `SATELLITES_REGISTRY_KEY "platinum/satellites/registry.json"`;
`:340-357` REFUSES every other leaf with 404 `{error: "unknown_satellites_resource"}` (rule `satellites_unknown_leaf`) BY DESIGN
("an unrecognised suffix is REFUSED rather than rewritten into a guess"); `:358` rewrites the one leaf to the one key. So B2's
`holdings.json` and B4's `characteristics.json` are unreachable by the page until this cell lands.

**Your edit, confined to that branch and its constants:** a leaf ALLOWLIST `{registry.json, holdings.json, characteristics.json}`
mapped to `platinum/satellites/<leaf>`; same prefix, same bucket resolution (firm = bucket, from the JWT-injected X-Firm-Id), same
firm assertion, **the refusal branch KEPT for every other leaf** (the honest branch; do not widen to a prefix rewrite). The router's
own gate script (the TO-7-AE ledger records 27 pass / 0 fail across 2 files) gains arms for the two new leaves and one for a refused
leaf; print its counts.

**THE RADIUS IS FIVE BEHAVIORS, NOT ONE -- read both halves before the first command:**
`org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND5_B5_CTO_HALF.md` @`f5a744f412` and
`.../NEVER_WIDEN_ROUND5_B5_COO_HALF.md` (this issuance's commit). `shared-advisor-router` is the `origin-request` function on five
ordered behaviors of distribution `EVTSA9VEHNZVH` (`cloudfront-distribution.tf:342, :373, :404, :634, :882`; `comp-routes behaviors`
counts the same five: `/api/scoped/advisor-intelligence/artifacts/*/*`, `/artifacts/*`, `/entities/*/*`, `/advisor-intelligence/*.json`,
`/api/scoped/satellites/*`). A new published version re-points ALL FIVE through `local.shared_advisor_router_arn` (`:66`). Behaviors
1-4 are the live Advisor Intelligence serving path for every partner firm. **The halves sign the act ONLY AS BOUNDED**: the plan
shows the function version + the five associations (+ at most the WAF `version ""` vs `null` no-op, IB-s-15) and NOTHING else;
after the apply the four Advisor Intelligence behaviors read IDENTICAL before/after.

**The deploy path (the TO-7-AE precedent, `org/critical_paths/change_management/20260828T0228Z_etfs-satellites-to7-ae-scoped-route-
portal-auth_deploy.md`):** `bash infra/aws/lambda/ci/build-nodejs-lambda.sh portal-auth shared-advisor-router` -> the artifact
`portal-auth/shared-advisor-router.zip` (current `content-sha256 qrL3PFqRnq5RUyQ4SDJvZQWDreLnl7rmNWZ25IF8cx0=`, VersionId
`N3w_OHAikHzTkuf.iIGPCXPM8_4ygJlL`) -> LITERAL probe on the new zip (`bun build` mangles identifiers; probe the three leaf strings, with
the NEGATIVE control on the previous artifact where `holdings.json` is ABSENT) -> plan (`aws_lambda_function.shared_advisor_router[0]`
+ the distribution) -> `safe-apply` -> 0-diff -> wait for the distribution's `Status: Deployed` -> the five-path verify.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.
A plan line outside the bound is a STOP before `safe-apply`; a post-apply read outside the bound is a same-turn re-association of
the prior version on all five, then the row.

## SURPRISE ROWS

ONE row per off-cell finding, `POSN_ASTTAX-Z-W23-S<k>`, appended to
`org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working.

**AMENDED AT THE DRAIN OF YOUR FIRST RUN (rows W23-S1..S4; issuer rows Z-S80, Z-S81):** the deploy is LANDED and its
evidence stands (V9-AC1..AC8, AC10..AC13 as recorded, the ledger CLOSED at 2713aec236). Two things change on this face. (a)
`V9-AC9` was unsatisfiable as written: the WAF `version` "" -> null normalisation both halves classify as a no-op at `V9-AC7`
is PERPETUAL (waf-cloudfront.tf:183-186, 202-205, 221-224 declare no version attribute), so an unqualified 'No changes.' can
never be read; the bar now admits exactly that classified no-op and nothing else, with the two cell resources' ABSENCE from
the plan as the printed discriminator. (b) `V9-AC12`'s three named expectations were met, but the recorder's banner claimed
a CHANGELOG write it did not make (W23-S4): the portal-auth CHANGELOG entry for shared-advisor-router :25 -> :26 is written
by you, in the helper's shape, in ONE follow-up commit -- the recorder is NOT re-run. `V9-AC7`, `V9-AC8` and `V9-AC12`'s
invocations are NOT rewritten after the fact (W23-S3 discloses the plan path you actually used; the instance's output carries
it); their instance rows stand. RE-RECORDED on this face: `V9-AC9`; APPENDED: `V9-AC12`'s output. Then the status flip.
**SECOND AMENDMENT (~20:5xZ, after your second run):** `V9-AC11`'s expectation now ADMITS the deployed-bytes arm you ran
(16 of 16 comparisons, 0 outside the bound) as the criterion's instrument under the measured credential gap (Z-S92); re-record
`V9-AC11` as PASS-by-output on that arm with the authenticated arm stated NOT EXERCISED, then flip the status. Nothing is re-run.

## CRITERIA -- structured, one clause each

<criterion id="V9-AC1" cell_refs="AT5-s-9"><invocation>timeout 60 git ls-tree HEAD -- org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND5_B5_CTO_HALF.md org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND5_B5_COO_HALF.md</invocation><expect>both blobs listed at HEAD. Absent either: STOP, row.</expect></criterion> `V9-AC1` -- THE B5 HALVES ARE AT HEAD.

<criterion id="V9-AC2" cell_refs="AT5-s-9"><invocation>timeout 120 python .tools/deploy_ledger.py open --slug posn-round5-b5-satellites-router-leaves --title "POSN_ASTTAX B5: shared-advisor-router admits holdings.json + characteristics.json on /api/scoped/satellites/ (five behaviors re-pointed)" --author 0.9.0_WK_POSN_ASTTAX~23 --leg "L1|git|SITEZ commit of index.mjs + gate arms|hash" --leg "L2|s3-prefix|opal-313476888478-lambda-artifacts portal-auth/shared-advisor-router.zip|sha256 + literal probe" --leg "L3|verify|PRIOR live qualified ARN read from the distribution and printed|the ARN" --leg "L4|verify|plan bounded: function version + five associations (+ WAF no-op)|plan summary" --leg "L5|activation|safe-apply|summary" --leg "L6|verify|0-diff re-plan|No changes" --leg "L7|verify|distribution Status Deployed|status read" --leg "L8|verify|five-path verify: registry byte-identical; new leaves 200 or S3-404 envelope; unlisted leaf router-404; four AI behaviors identical before/after|the table"</invocation><expect>the entry path with 8 legs OPEN, opened before any edit.</expect></criterion> `V9-AC2` -- THE LEDGER, WITH THE FIVE-PATH VERIFY AS A LEG.

<criterion id="V9-AC3" cell_refs="AT5-s-9"><invocation>timeout 60 git diff --stat HEAD~1 -- infra/aws/lambda-edge/shared-advisor-router/</invocation><expect>index.mjs (and its gate/test file) only; the hunk headers printed all fall inside :89-101 and :330-360 of the pre-edit file; no other hunk. The allowlist reads exactly three leaves; the refusal branch is present in the diff's context, unchanged.</expect></criterion> `V9-AC3` -- THE EDIT, CONFINED TO THE SATELLITES BRANCH.

<criterion id="V9-AC4" cell_refs="AT5-s-9"><invocation>timeout 300 bash <ROUTER_S_OWN_GATE></invocation><expect>N pass / 0 fail with N printed and N >= 27 + 3 (the two new admitted leaves and one refused leaf are new arms; name them).</expect></criterion> `V9-AC4` -- THE ROUTER'S GATE, WITH THE NEW ARMS COUNTED.

<criterion id="V9-AC5" cell_refs="AT5-s-9"><invocation>timeout 600 bash infra/aws/lambda/ci/build-nodejs-lambda.sh portal-auth shared-advisor-router</invocation><expect>the artifact uploaded; s3api head-object prints the new VersionId and content-sha256 (different from qrL3PFqRnq5RUyQ4SDJvZQWDreLnl7rmNWZ25IF8cx0=); the LITERAL probe on the NEW zip finds 'holdings.json' and 'characteristics.json' and 'platinum/satellites/' PRESENT, and the same probe on the PREVIOUS artifact version finds 'holdings.json' ABSENT (the negative control fires).</expect></criterion> `V9-AC5` -- BUILT, UPLOADED, CONTENT-VERIFIED BY LITERALS ON BOTH VERSIONS.

<criterion id="V9-AC6" cell_refs="AT5-s-9"><invocation>timeout 120 comp-routes edge-versions</invocation><expect>the PRIOR live qualified ARN (function version number) of shared-advisor-router as associated on the distribution, printed BEFORE the apply -- this is the rollback target; if the tool cannot read the live plane, read it with the aws CLI under a `# rail-checked:` marker naming this criterion and print it. A live association count other than FIVE is Branch B: STOP.</expect></criterion> `V9-AC6` -- THE PRIOR VERSION, READ LIVE, PRINTED BEFORE ANYTHING MOVES.

<criterion id="V9-AC7" cell_refs="AT5-s-9"><invocation>timeout 900 terraform -chdir=infra/aws/terraform/portal-auth plan -out=.scratch/b5.tfplan</invocation><expect>exactly: aws_lambda_function.shared_advisor_router[0] updated in place (s3_object_version / source_code_hash / a new published version) and aws_cloudfront_distribution.portal updated in place with ONLY the five origin-request association ARNs changing (print the five diff lines), plus at most the classified WAF version-normalisation no-op. Any other resource or attribute: STOP, no apply, row.</expect></criterion> `V9-AC7` -- THE PLAN, BOUNDED TO THE HALVES.

<criterion id="V9-AC8" cell_refs="AT5-s-9"><invocation>timeout 1800 .tools/safe-apply.sh -chdir=infra/aws/terraform/portal-auth apply .scratch/b5.tfplan</invocation><expect>Apply complete with the counts matching V9-AC7's plan; HALTGT output pasted.</expect></criterion> `V9-AC8` -- THE APPLY.

<criterion id="V9-AC9" cell_refs="AT5-s-9"><invocation>timeout 900 terraform -chdir=infra/aws/terraform/portal-auth plan</invocation><expect>the plan's changed set is EMPTY (No changes.) or EXACTLY the one WAF version-normalisation no-op classified at V9-AC7 (print its diff lines: every changed attribute a rule `version` "" -> null on the web ACL and nothing else), AND aws_lambda_function.shared_advisor_router[0] and aws_cloudfront_distribution.portal are ABSENT from the plan -- print `0 of 2 cell resources in the plan` as the discriminator. Any lambda or distribution attribute in the plan is a FAIL with a row.</expect></criterion> `V9-AC9` -- 0-DIFF.

<criterion id="V9-AC10" cell_refs="AT5-s-9"><invocation>timeout 1800 bash -c "until [ \"\$(.tools/aws cloudfront get-distribution --id EVTSA9VEHNZVH --query 'Distribution.Status' --output text)\" = Deployed ]; do sleep 30; done; echo Deployed"</invocation><expect>Deployed printed; the associated qualified ARN on the satellites behavior EQUALS the newly published version (print both), and the same new ARN on the other four behaviors. (The rail: this is a status read under a named criterion, mark it `# rail-checked: V9-AC10 live status read`.)</expect></criterion> `V9-AC10` -- REPLICATED, AND THE ASSOCIATION IS THE NEW VERSION ON ALL FIVE.

<criterion id="V9-AC11" cell_refs="AT5-s-9"><invocation>timeout 600 python <FIVE_PATH_VERIFY_AUTHENTICATED></invocation><expect>a table: /api/scoped/satellites/registry.json 200 with body hash IDENTICAL before/after; holdings.json and characteristics.json 200 with the served bodies if B2/B4 have landed, else the S3 404 envelope (printed, and stated as NOT the router's 404); a fourth unlisted leaf (e.g. nope.json) 404 with rule satellites_unknown_leaf; and for EACH of the four Advisor Intelligence behaviors one request, same firm, same key, status + body hash IDENTICAL before/after. Any row outside this: re-associate the prior version (V9-AC6's ARN) on all five the SAME TURN, then the row. ISSUER'S RULING (Z-S92, after row W23-S1 measured that NO authenticated session is obtainable on this fabric -- every committed credential fixture returns mfaRequired=true with no accessToken, 3 of 3, and a second factor is credential-equivalent and unauthorized): the DEPLOYED-BYTES arm is ADMITTED as this criterion's on-demand instrument (Rule 27: the proof is an act a seat can take on demand, and the authenticated probe is not one here) -- `aws lambda invoke` of the PRIOR and the NEW published versions with the same synthetic origin-request events (the headers auth-validator-edge injects) for every one of the five behaviors' paths: status + body hash IDENTICAL between the two versions for the four Advisor Intelligence paths and registry.json, the two new leaves admitted and an unlisted leaf refused by the NEW version only (the negative control), N of N comparisons printed with 0 outside the bound. Graded PASS-by-output on that arm with the authenticated arm recorded NOT EXERCISED (never faked) and the credential gap cited by row id; what the arm cannot grade -- authorization at the viewer-request gate, which this deploy did not touch -- is stated in the instance.</expect></criterion> `V9-AC11` -- THE BOUND, EXERCISED ON ALL FIVE BEHAVIORS.

<criterion id="V9-AC12" cell_refs="AT5-s-9"><invocation>timeout 300 bash infra/aws/lambda/ci/record-terraform-deploy.sh portal-auth --plan .scratch/b5.tfplan --author "0.9.0_WK_POSN_ASTTAX~23 <0.9.0_WK_POSN_ASTTAX~23@opal.agent>"</invocation><expect>recorded (commit hash printed, VERIFIED by `git show --stat` listing lambda-source-map.json, never by the recorder's stdout); legs L1-L8 closed with proofs; the entry closed. CHANGELOG.json: the recorder's JS helper CANNOT run on this device (W23-S4: record-terraform-deploy.sh:218 tests a hardcoded bun path that does not exist here, falls to python3 and hands it a .js file; its banner 'Source map + CHANGELOG.json committed' is then FALSE and is not evidence) -- write the entry YOURSELF in the helper's exact shape (the entry object built at record-terraform-deploy.sh:600-700: version, deployed_at, deployed_commit, deployed_commit_short, previous_commit, branch, agent, functions_updated, commits, artifacts, scoped to exactly the functions this cell deployed) at the HEAD of `entries`, written with json.dump(ensure_ascii=False, indent=2) plus a trailing newline in UTF-8 so the file's non-ASCII count is UNCHANGED (print `len(b) - len(b.decode('utf-8'))` before and after), and commit it under your grant. The recorder's other two device defects (a cp1252 text-mode read; an unquoted python3 path with a space) are worked around by ENVIRONMENT ONLY (PYTHONUTF8=1; a space-free python3 shim directory first on PATH), never by editing the script.</expect></criterion> `V9-AC12` -- RECORDED AND CLOSED.

<criterion id="V9-AC13" cell_refs="AT5-s-9" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether an allowlist of three literal leaves is the right shape versus a prefix rewrite -- the halves chose the allowlist to keep the refusal branch; whether that trade is right for the next leaf. Record the readings and offer NO verdict.</expect></criterion> `V9-AC13` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>V9-AC1, V9-AC2, V9-AC3, V9-AC4, V9-AC5, V9-AC6, V9-AC7, V9-AC8, V9-AC9, V9-AC10, V9-AC11, V9-AC12, V9-AC13</expected_criteria>

<placeholders>FIVE_PATH_VERIFY_AUTHENTICATED, ROUTER_S_OWN_GATE</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-V9-1.the-edge-router-admits-the-two-new-leaves.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~23/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda-edge/shared-advisor-router/
infra/aws/terraform/portal-auth/CHANGELOG.json
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round5.md</decomp_doc> round 5, cell `AT5-s-9`.
<owned_cells>AT5-s-9</owned_cells>
Read-dependencies, NOT claimed: none upstream (B2/B4 landing is NOT required for your verify -- the S3 404 envelope is a valid
observed state for the new leaves). DOWNSTREAM: `AT5-s-7` (F3) fetches the two new leaves through your route; `AT5-s-8` (R1)
renders through it.
</decomp_ref>

<preflight>
comp-schedule: RUN at the cut -- the NEVER clauses bind: safe-apply only, never-widen (both B5 halves at HEAD), no monitor; your
ledger entry is opened at V9-AC2. The TO-7-AE deploy ledger is the precedent and is CLOSED.
comp-iam: DECLARED-NOT-APPLICABLE for grants -- the router's role and policies do NOT change; only the function's code version and
the distribution's associations move. Stated, not waived.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the issuer's radius census is DESIRED-plane (comp-routes over
Terraform + committed source); V9-AC6 is the first LIVE read and a count other than five stops the cell; (2) the issuer has not
exercised build-nodejs-lambda.sh on this device since the reboot; (3) the issuer does not hold an authenticated session for the
five-path verify -- if the ui-smoke auth stub cannot reach the scoped behaviors, that is a row naming the credential gap, and the
verify is recorded PARTIAL as TO-7-AE's was, never faked.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~23/POSN_ASTTAX.TO-V9-1.the-edge-router-admits-the-two-new-leaves.proof_of_spec.json
</proof_of_spec>
