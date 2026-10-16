# AMGT_RESAPP task order -- `AMGT-bo-2` -- THE WITHHELD-REASONS FEATURE IS PROMOTED TO PROD FROM THE APPROVED LIST, WITH ITS RECEIPT AND THE CI CONCLUSION -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bo-2</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform~H1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bo-2.withheld-reasons-feature-promoted-to-prod</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one promote; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of PROD in the portal repository under the DT's standing /prod-deploy grant; no AWS call.
comp-adversary: RUN at the cut (2026-10-16 ~02:2xZ) -- `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-withheld-reasons` reads `state=OPEN valid=- row=dell1-20261016T013205Z-9365 head_sha=01e06415f17f5e2ea79b28548647142879cce340 commits=1 class=opal-internal`, so this order is STAGED and is not given until it reads `state=APPROVED valid=yes`; the candidate's diff against PROD `e0e69da7` reads ten paths, all under `src/pages/SecurityAnalysis/`; AC1 at the base reads `DIFFERS` on all ten (origin/PROD `e0e69da7`), AC2 reads the PROD head `e0e69da7` (success, completed), which the criterion refuses, and AC3 reads a missing receipt: each FAILS at the base as expected. EGRESS CLASS, declared: git fetch and push of PROD in Opal-Capital/portal, and the CI read; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-bo-2` (round 108, decomposition s.117)

STAGED. The issuer gives this order (status `staged` to `pending`, a go line in your inbox) only after the box CTO closes the approval row `dell1-20261016T013205Z-9365` APPROVED at head `01e06415f17f5e2ea79b28548647142879cce340` (class Opal-internal: `/security-analysis` is staff-only, no word from Andrew is needed). The feature (candidate `cand/dell1/amgt-sa-withheld-reasons`, base PROD `e0e69da7`): every Key Figures P/E cell the page fills from the research team's sheet prints `research team estimate`; What Changed never lists a withheld forward vendor P/E; a Key Figures table with no P/E row states the served withhold reason once. Do, in order:
1. **Wait for the merge-forward.** It is the box manager's act (`0.0.0_AB_MSTR~DELL1`), never yours. Run `git -C C:/dev/ajb_workspace/portal fetch origin DEV -q && git -C C:/dev/ajb_workspace/portal merge-base --is-ancestor 01e06415f17f5e2ea79b28548647142879cce340 origin/DEV && echo IN-DEV`. If it does not print `IN-DEV`, wait 120 seconds and run it again, for up to 20 minutes in all; do not freeze DEV pushes while you wait (the merge-forward IS a DEV push, and it is what you are waiting for). If it still does not print `IN-DEV` after 20 minutes, STOP and report that the merge-forward is not done: do not build, do not promote.
2. In the portal repository (`C:/dev/ajb_workspace/portal`), run `bash .tools/portal-release-build.sh --features cand/dell1/amgt-sa-withheld-reasons` from the workspace root. It refuses the whole release on any of its pinned tokens (not-approved, stale-head, commits-differ, unapproved-commits, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote.
3. Promote the release with `/prod-deploy`. The release carries ONE feature, ten files under `src/pages/SecurityAnalysis/` (three product files, one new helper, the new harness, the changed harness, five fixtures); no other candidate is in it. Your receipt names `/security-analysis` as Opal-internal. The PROD head may have moved since the cut (other seats promote too): build on the PROD head you read, and name any deviation from this order's numbers in the receipt.
4. Read the CI conclusion on the PROD head (`gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
5. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/PROMOTE_RECEIPT_BO2.md` with the sections `## Release` (the release branch, the PROD head before and after, the push state as an `ls-remote` read), `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## CI` (the conclusion and the run it came from, as read).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. One feature only, exactly the approved list; never `--features` anything else, never live DEV whole, never a client-facing page.
2. The push is PROD in `Opal-Capital/portal` by `/prod-deploy`; never DEV, never a force push, never a rebase. Portal DEV is written only by `.tools/portal-merge-forward.sh cand/<box>/<slug>` on an approved row (CLAUDE.md Portal section): the merge-forward in step 1 is that script's run by the box manager.
3. Edit no product file. The receipt and the deploy ledger entry the skill opens are the only things you write.

## 3. SURFACES

<paths>
org/devices/state/dell1/
org/critical_paths/.open_deploys/
org/critical_paths/change_management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bo-2"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for f in $(git diff --name-only e0e69da7 01e06415f17f5e2ea79b28548647142879cce340); do a=$(git rev-parse origin/PROD:$f); b=$(git rev-parse 01e06415f17f5e2ea79b28548647142879cce340:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done</invocation><expect>ten lines `EQUAL <path>` (one per path of the candidate's diff against `e0e69da7`, none `DIFFERS`)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bo-2"><invocation>gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `e0e69da7` (the pre-promote head at the cut: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bo-2"><invocation>grep -c -E "security-analysis|Opal-internal|completed|success" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/PROMOTE_RECEIPT_BO2.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit the receipt and the ledger entry under your own lane. Then write the proof-of-spec instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/AMGT_RESAPP.TO-AMGT-bo-2.withheld-reasons-feature-promoted-to-prod.proof_of_spec.json` (this order's name is short on purpose, so the canonical path opens on this box; `to_id` equal to the `<to_id>` line character for character, `decomp_ref` from the order's block, AC1 to AC3 with your own outputs; only this folder admits you), commit it, run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line, THEN stand down.

Report once:
- the release branch, the PROD head before and after, and the `ls-remote` read of PROD;
- AC1's, AC2's and AC3's output lines;
- the CI conclusion as read;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED SHELL cut 2026-10-16 ~02:2xZ (2.0.0_SA_COO~R1), the `bn-3` pattern (round 107) so the GO is one line the minute the approval row closes. Cell `AMGT-bo-2` of decomposition s.117. THE GO: given when `approval-status` reads `state=APPROVED valid=yes` for the branch at head `01e06415f17f5e2ea79b28548647142879cce340`; the issuer then flips `staged` to `pending`, records the approval in the GO commit, and sends the DT a go line (a Tier-2 seat hears an act only as a task order). The merge-forward is asked of `0.0.0_AB_MSTR~DELL1` by the issuer at the GO (the DT does not ask for it). The DT is a Tier-2 SEAT, not a worker: it holds this order in its own home and reports to `2.0.0_SA_COO~R1` and `1.0.0_SA_CTO~DELL1`. `bo-3` (the walk) waits on THIS promote. If the CTO instead approves the row at another head (a re-push), the GO re-reads the head and amends the three places that name it.

<status>pending</status>
<round>108</round>
<workstream>PROMOTE</workstream>
<slot>0.4.0_DT_ClientPlatform~H1</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
