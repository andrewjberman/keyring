# TO IRPT_ANLREQ.TO-AR-y-223.driven-exercise-design -- the design of the driven status-rule exercise, predicted offline

<to_id>IRPT_ANLREQ.TO-AR-y-223</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~69</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-223` (`decompositions/IRPT_ANLREQ_DECOMP_R21_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~69`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-69` (branch `wk-IRPT_ANLREQ-69`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~69 <0.9.0_WK_IRPT_ANLREQ~69@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W69-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-223`, inlined) -- DESIGN THE DRIVEN STATUS-RULE EXERCISE. READ AND OFFLINE RUN ONLY. NOTHING IS MINTED.

*The status rule is in all eight packagers; no internal caller has met it yet (A4: 0 lines). NO FWD IS A WAIT: it is to be exercised by an act (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_21_20261013.md` section 2 item 4, section 3 item 3).* The act is a never-widen pair, cut and signed BEFORE any mint, executed by a Dell CloudOps lane, in the shape of the R2-cw-1 pair (`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_RUN/R2_CW1_CRAWL_PAIR.md`: a synthetic internal identity row in `opal-users-v2` and a short token, held in memory, the row removed after `exp` and read ABSENT). The act: two synthetic internal identities, one whose users row is `disabled` and one with NO row (token only), each selecting a firm other than its own on `irpt-directory-search`, expected REFUSED with one caller-class line each (`row_non_active`, `row_absent`); a positive control, an `active` synthetic row selecting the same firm, expected ADMITTED. This cell writes the DESIGN that pair rests on and predicts the outcomes OFFLINE. It mints nothing, calls nothing live, reads no key and no identity.

**Read first:** `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_RUN/R2_CW1_CRAWL_PAIR.md` (sections 2, 3 and 4: the row, the token claims, the one-firm proof, the removal) and the CTO half it cites; `infra/aws/lambda/investor-reporting/_authz/served.py` (`_internal_allowed_firms`, the caller-class line, how an internal principal is told from a service subject); `infra/aws/lambda/investor-reporting/_authz/tests/test_internal_status_active.py` and `test_caller_class_log.py` (the harness that already runs the rule offline); `infra/aws/lambda/investor-reporting/directory/` (the entry of `irpt-directory-search`: how a request names the selected firm, which member, which route, what the refusal looks like); and the live map entry for `irpt-directory-search` in `infra/aws/lambda/ci/lambda-source-map.json`.

1. **The route and the request.** Name the HTTP route (or event shape) a signed-in internal identity uses to reach `irpt-directory-search` and the member that selects a firm (read it from the entry; give file and line). Name a firm other than `opal-capital` that the function accepts as a selection WITHOUT touching any client's data (for example a registry firm the directory function lists without reading holdings; justify it from the code), and the minimal read-only request (a directory search or browse) that makes the rule decide.
2. **The identities.** For `disabled`, `norow` and `active`: the users-table row (or its absence; the R2-cw-1 row shape: `PK USER#<synthetic>@opal.invalid`, `SK PROFILE`, `firmId opal-capital`, `status`, `userType`, `allowedFirmIds` as the rule reads it), the token claims (`sub`, `iss`, `aud`, `firmId`, `tier`, `role`, `userType`, `exp` at most 20 minutes after `iat`), `home_firm`, `selected_firm`, and `expected` {`outcome` `refused` or `admitted`, `class` `row_non_active`, `row_absent` or `row_present`, the refusal code}. The `active` row must be `allowedFirmIds` naming the selected firm only.
3. **Predict offline.** Run the packaged `directory` entry and `_authz/served.py` (the release bytes at the trunk head) with fake principals and a fake users-table adapter that returns the three cases (the harness of `test_internal_status_active.py` is the model), capture each outcome and the exact `INTERNAL-CALLER-CLASS class=... outcome=...` line, and record `offline_run` {`method`, `results`: one object per identity with `name`, `outcome`, `class`, `line`}. The three results must equal the three `expected` values; if they do not, say so and stop (a BLOCKING row).
4. **The log and the counts.** `log` {`group` (the function's log group), `filter` (the pattern that finds the class line without any identity), `expected_lines` (what each identity must produce), `streams_denominator_rule`}.
5. **Removal and bounds.** `removal` {`method` (delete the row after `exp`, read it ABSENT with a consistent read; the token is never written to a file), `exp_rule`}. `bounds`: what the identities may do (one route, one read-only request), what they may not (any write, any client firm, any IRPT read of holdings), the keys touched (the users table rows, the signing key read), and the rollback per key.
6. **Write `r21/EXERCISE_DESIGN.json`:** `route`, `precedent` {`record`, `mint_steps` (the R2-cw-1 steps you reuse)}, `identities`, `offline_run`, `log`, `removal`, `bounds`, `claim`, `not_read`.
7. **In your report:** the route and the selected firm, the three offline outcomes with their class lines, and anything in the precedent that does not carry over.

### ACCEPTANCE

<criterion id="AR223-y-AC1" cell_refs="AR-y-223"><invocation>python C:/dev/wk-irpt-anlreq-69/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y223-design --root C:/dev/wk-irpt-anlreq-69</invocation><expect>Y223-DESIGN-OK</expect></criterion>
`AR223-y-AC1`: the design names three identities (`disabled`, `norow`, `active`), each selecting a firm other than its own, with expected outcomes `refused`/`row_non_active`, `refused`/`row_absent` and `admitted`/`row_present`; the offline run of each equals its expected outcome and class; the log group and the removal method are named.

<criterion id="AR223-y-AC2J" cell_refs="AR-y-223" judgment="true"/>
`AR223-y-AC2J` (judgment, graded at L9, never by you): the route and the selected firm are read from the code, the selected firm opens no client data, the offline run used the shipped bytes and the rule's own harness, and nothing was minted or called.

<expected_criteria>AR223-y-AC1 AR223-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~69/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R21_Y.md</decomp_doc>
<owned_cells>AR-y-223</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~69/IRPT_ANLREQ.TO-AR-y-223.driven-exercise-design.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-223`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reads and an offline run in a scratch folder outside the product tree; nothing is minted, called or written outside the worker's deliverables.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the R2-cw-1 pair against the cell; the lens: a design that selects a client firm whose data a read would touch, or an expected outcome copied from the rule's tests instead of run on the entry. The order names the offline run on the shipped entry and a selected firm justified from the code. NOT seen: the live token path and the users table.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-21 analysis items 3 as round 21 workstream `Y`. Base: `AR223-y-AC1` FAIL as expected (no record).
- The never-widen pair and the mint are not this order.
