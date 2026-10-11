# ADVI_FIRMBKTS task order -- `FB-f-8` -- WINDOW ACT 1: DEPLOY THE advTenant BUILD (PHASE A: THE ALL-ASCII ROUTER AND GUARD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~17</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- phase A is two repository files; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- phase A is repository files only: no AWS act and no grant. The deploy chain's actions read `allowed` for the caller (5 of 5) and are re-read for phase B by its amendment.
comp-adversary: RUN by the issuer -- at base the non-ASCII count reads router 15 bytes on 5 lines and guard 12 bytes on 4 lines (AC1 FAILS as it should); the router's gate (51 pass), the guard's suite (46 pass) and the dormancy grid (88 of 88 and 396 of 396 identical) PASS at base as controls. Blindness: the lens cannot see a runtime parse error a comment edit introduces; the two suites and the grid exercise both modules.
EGRESS CLASS, declared: NONE (the guard's `bun install --frozen-lockfile` fetches its pinned dependencies; no other request leaves the machine).
</preflight>

## 1. THE CELL -- `FB-f-8` phase A (round 3, enrichment item 1, step 1; the CTO's precondition on act 1)

Act 1 deploys the router's code, so it is the deploy at which the router and its guard go all-ASCII (CLAUDE.md section 4:
"all non-ASCII out", the first of the two safe moves; the CTO's ruling on row D1-W9-S1, restated as the precondition of
the act-1 pair). You make the two files ASCII. The change is COMMENTS ONLY: no code, string, regex, key or logic changes.

1. `infra/aws/lambda-edge/shared-advisor-router/index.mjs`: 15 bytes above 127 on 5 lines (at the cut: lines 49, 271, 278,
   307, 488).
2. `infra/aws/lambda-edge/shared-advisor-router-response/index.mjs`: 12 bytes above 127 on 4 lines (lines 2, 10, 17, 239).
3. Replace each non-ASCII character by its plain ASCII spelling (an em dash or en dash by `--`, a typographic quote by the
   straight quote, an arrow by `->`, a multiplication sign by `x`, an ellipsis by `...`). A character inside a string
   literal or a regular expression is NOT a comment: STOP on it and file a BLOCKING row naming the line.
4. `infra/aws/lambda-edge/_shared/firm-config.mjs` is generated and is NOT yours: it ships as it is (its header's five
   non-ASCII characters are the generator template's, LGIC_ENFORCE's row D1-S4).

### 1a. The steps

0. Work in `/c/dev/wk-firmbkts-17`. Begin every shell call with `cd /c/dev/wk-firmbkts-17 &&` and put
   `export PATH="$PATH:$HOME/.bun/bin"` first in any call that runs `bun`.
1. Print the non-ASCII lines of the two files first (line number and the line, no other output).
2. Edit only those lines. Diff afterwards with `git diff --stat` and `git diff` and read every hunk: each must touch a
   comment and change only characters above 127.
3. Run AC1-AC4 (section 4). Read every line. Repair only what they name.

## 2. BOUNDS

1. Repository files only: no deploy, no `terraform`, no `aws` call, no change to a Lambda, CloudFront or IAM object.
2. Two source files change, one commit. No other file in the package changes (the tests stay as they are).
3. A hunk that changes anything but a comment is a STOP (a BLOCKING row), never "fixed up".
4. Only the files in section 3 change. LF line endings.

## 3. SURFACES

<paths>
infra/aws/lambda-edge/shared-advisor-router/index.mjs
infra/aws/lambda-edge/shared-advisor-router-response/index.mjs
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of both packages, `_shared/firm-config.mjs`, the checks under `deliverables/2.0.0_SA_COO~B1/`, the
dormancy grid at `deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/evidence/dormancy_grid.mjs`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/ADVI_FIRMBKTS.TO-FB-f-8.act1-deploy-advtenant.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-8"><invocation>cd /c/dev/wk-firmbkts-17 &amp;&amp; python -c "f=['infra/aws/lambda-edge/shared-advisor-router/index.mjs','infra/aws/lambda-edge/shared-advisor-router-response/index.mjs']; n=[sum(1 for b in open(p,'rb').read() if b&gt;127) for p in f]; print('NON-ASCII: router %d, guard %d' % (n[0],n[1]))"; echo "exit=$?"</invocation><expect>NON-ASCII: router 0, guard 0</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-8"><invocation>export PATH="$PATH:$HOME/.bun/bin" &amp;&amp; cd /c/dev/wk-firmbkts-17 &amp;&amp; timeout 110 bash infra/aws/lambda-edge/shared-advisor-router/run-gate.sh; echo "exit=$?"</invocation><expect>\b(5[1-9]|[6-9][0-9]) pass</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-8"><invocation>export PATH="$PATH:$HOME/.bun/bin" &amp;&amp; cd /c/dev/wk-firmbkts-17/infra/aws/lambda-edge/shared-advisor-router-response &amp;&amp; timeout 115 bash -c 'bun install --frozen-lockfile >/dev/null 2>&amp;1; bun test test/ 2>&amp;1 | tail -6'; echo "exit=$?"</invocation><expect>\b(4[6-9]|[5-9][0-9]) pass</expect></criterion>
  <criterion id="AC4" cell_refs="FB-f-8"><invocation>export PATH="$PATH:$HOME/.bun/bin" &amp;&amp; cd /c/dev/wk-firmbkts-17 &amp;&amp; timeout 110 bun org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/evidence/dormancy_grid.mjs /c/dev/wk-firmbkts-17 2>&amp;1 | tail -3; echo "exit=$?"</invocation><expect>DORMANCY: router differing 0, guard differing 0</expect></criterion>
</proof_of_spec>

AC1 is the built behavior. AC2-AC4 are difference controls (the same suites and grid as `FB-f-7`, counts never below
`FB-f-7`'s 51 and 46): a comment edit must move no decision. Four criteria are carried because the edit touches two
packages and each package's own suite is its control. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-f-8.act1-deploy-advtenant.proof_of_spec.json`, `D` =
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~17`. Commit the two source files, the instance and
your rows together on your branch. **Do not flip this order's `<status>`:** phase B (the deploy) is staged below the record
face and the order stays open until it is done. A row id on this project carries the dell1 infix and your slot:
`ADVI_FIRMBKTS-D1-W17-S<k>` (your earlier sessions filed S1 to S6: the next unused is S7), with `surfaced_at` from
`date -u +%FT%TZ`. Report once: the before and after non-ASCII counts, the lines changed (numbers only), the output lines of
AC1-AC4, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2.0.0_SA_COO~B1, after the CTO's act-1 half @d30c5fe203, msg 3601):** the pair was SIGNED on one
precondition: both functions go all-ASCII in one commit, the build is cut from it, and the dormancy grid re-reads 88 of 88
and 396 of 396. That moved decomposition step 4's ASCII item (cell `FB-f-11`) into this cell, as phase A, spawnable now.
Phase B (the deploy) is the original order, staged below. Same cell, same slot: the decomposition is frozen mid-round.
The face's placeholders read `NONE` because the face now carries no token; phase B's five tokens return with its
criteria at the amendment. Gate limb: GATE viii read `<placeholders>` at HEAD (five tokens) and the new declaration is
`NONE` over literal invocations.

**PHASE B (STAGED; NOT A FACE).** Un-park conditions, all required, each read from a file at HEAD:
1. `FB-f-7` is `complete` (merged @e6ec8ce6e4) and phase A is merged with AC1-AC4 PASS.
2. The pair reads SIGNED in both halves: `ledger/NEVER_WIDEN_ROUND3_ACT1_ADVTENANT_COO_HALF.md` and `..._CTO_HALF.md`
   @d30c5fe203. **Satisfied.** The oracle is the CTO's exercised read: the actor pings the CTO at `Deployed`; the CTO invokes
   both new versions on the 5 event classes against base, makes one live no-session 401 request and diffs the associations.
3. The actor's change-management entry is OPEN and committed first (`python .tools/deploy_ledger.py open ...`).
4. The amendment commit names the executor, the build's artifact hashes (`ROUTER_SHA256`, `GUARD_SHA256`), and sets
   `<status>pending</status>`.
Steps, with the traps the 2026-08-21 act recorded: open the entry; build both zips with `build-nodejs-lambda.sh` from the
phase-A tree; upload the artifacts the `aws_s3_object` data sources read; read the plan's JSON: the two functions and 10
associations change, nothing else, and a distribution that reads NO-OP is the pin defect and a STOP; apply through
`safe-apply` only; read back each behavior's version and `CodeSha256`; the post-apply plan reads no changes; ping the CTO
at `Deployed`; close the entry with the evidence.
Criteria then (placeholders `ROUTER_VERSION`, `GUARD_VERSION`, `ROUTER_SHA256`, `GUARD_SHA256`): AC5 router `CodeSha256`
at the published version equals `<ROUTER_SHA256>`; AC6 the guard's likewise; AC7 the distribution's 5 + 5 associations read
the two new versions (a bounded `get-distribution-config` read).

**ISSUER NOTES:** class WORLD by the floor of phase B; phase A is repository files. The executor of phase B is the
issuer's call and is open: the 2026-08-21 act was the CloudOps seat's (`0.7.0_AE_CloudOps`); a lane for this project is
not seated. `auth-validator-edge` (v22 on 26 behaviors) bundles the same generated config and is not redeployed.

<status>pending</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-8</to_id>
<slot>~17</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
