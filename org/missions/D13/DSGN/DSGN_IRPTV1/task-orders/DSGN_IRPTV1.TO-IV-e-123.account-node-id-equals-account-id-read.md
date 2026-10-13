# TO DSGN_IRPTV1.TO-IV-e-123 -- one read of the holdings producer: is an ACCOUNT node's id equal to the account id on every served path; where it is not, the page maps the node ref to the account id before the Holdings focus post -- a read; a product change only if the ids differ

<to_id>DSGN_IRPTV1.TO-IV-e-123</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~72</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>32</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6671, round-32 analysis section 2 item 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_32_20261012.md`): "one read of the holdings producer for the ACCOUNT node id equal to the account id on served answers; if not equal on any, map node ref to account id before the focus post." | **Rows:** D2-W69-S2 | **Decomp cell:** `IV-e-123` (decomposition v32) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** none (portal DEV cf52fdbf00f2 is the base).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-72` (branch `wk-DSGN_IRPTV1-72`); run everything from its root unless a step says the portal. Your folder is
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~72/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-72/portal` is a PORTAL worktree (its own git repo, branch `wk-DSGN_IRPTV1-72-portal`) at portal DEV `cf52fdbf00f2`. Do not amend or revert anything
committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with
`.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` here is a LINK to the main portal checkout's real install:
no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only
with `git checkout -- <file>` on a file that has no uncommitted work of yours. If (and only if) you change the page, run ONE whole-scope run before any edit
(`bun test src/pages/InvestorReporting`, output to a file under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~72/`) as your base for
`new_failing_ids`; the issuer measured the base at the previous head as 1216 pass, 27 skip, 1 fail (F14-AC3, a diff check against DEV 1f3ce9f0, a known base failure).

**What is asked, and why.** On Holdings, the card's account tile opens the one-account view. The page names the account it opens by the card's account NODE ref
(`portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx` lines 749-763 map to `account.nodeRef`; `HoldingsTab.tsx` lines 171-190 `pickedAccountRef`, line 304
`focusedAccountId`, line 327 `resolveAccountFocus` posts an ACCOUNT scope with `scope_ids [that ref]`). That is correct only where the ACCOUNT node's id equals the
account's id. The reader's own row D2-W69-S2 (`org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md`, search the row id) says
the producer's `infra/aws/lambda/investor-reporting/holdings/snapshot.py` near line 441 builds the selected custody account ids from the ACCOUNT nodes' `node_id` and
refuses when the sets differ, and `portal/src/pages/InvestorReporting/contracts/adapt.ts` near line 1150 maps `nodeRef` from `node.node_id`. That read covers ONE
producer function; it was not checked against every path that can serve a holdings answer, and no live payload was read.

**The cell (`IV-e-123`).**
1. **The read.** Enumerate every producer path in this workspace that builds a holdings snapshot or answer the page can receive (start in
   `infra/aws/lambda/investor-reporting/holdings/`: `snapshot.py`, `publication.py`, `resolve.py`, `handler.py`, `entry.py`, `stage.py`, the contract fixtures under
   `contracts/` and the producer's own fixtures and tests; and any other provider path the page's adapter handles, which you find from `contracts/adapt.ts` and the
   `contracts/wire/` types). For each, read how an ACCOUNT node's `node_id` is built and whether it is the account id. Print the denominator: how many paths you
   enumerated and how many you read, and say how you enumerated them (`denominator` {paths_enumerated, paths_read, basis}). Each rule you rely on goes in
   `producer_reads` {file, line, rule}. Read only; no AWS call, no live request. `ids_equal_on_all` is true only if EVERY enumerated path builds the ACCOUNT node id
   as the account id; a path you could not read is not "equal", and is a row.
2. **If every path is equal:** record `product_change false`, `product_files_changed []`, and add nothing to the page. The only files you add are the record, rows and this
   order's flip.
3. **If any path is not equal:** map the node ref to the account id in the page BEFORE the focus post (in `tabs/holdings/`, where `pickedAccountRef` and the focus read
   are), without changing what the header hands on or any request shape for the equal case; add one test `__tests__/dsgn-irptv1/iv-e-123.account-node-map.test.tsx`
   (a node ref that differs from its account id posts the account id; one that equals it posts as before), one temporary mutant (post the node ref again) that the test
   catches, then reverted. Record `product_change true`, `page_maps_node_ref true`, `test`, `suite_base`, `suite_after` {pass, skip, fail, new_failing_ids},
   `lint_errors`, `typecheck_errors` (run `bun run lint` and `bun run typecheck` after your last portal commit), `product_files_changed`, `portal_commit` (40 hex).
   Record everything in `NODE_ID_READ.json` with the keys named in the criterion below.

<criterion id="IV123-AC1" cell_refs="IV-e-123"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r32/p32_round32.py" . IV123-AC1</invocation><expect>IV123-AC1 PASS</expect></criterion>
`IV123-AC1` -- every enumerated producer path was read with its denominator printed and the ACCOUNT node-id rule cited by file and line; the record says whether the ids are equal on all of them; the page maps the node ref only where they are not, with a test and a mutant. Base: FAIL (no record).

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-13 ~00:0xZ; gate limb: none graded it, this is a modification of an existing order).** Your first report found the ids differ
(the live 49 Financial builder mints ACCOUNT node ids from the Schwab balance key, the directory from gold dim_account) and that the wire carries no account id the page
could map to, so the step-3 map has no source inside this grant. That is a valid outcome of this cell, not a failure of it. The cell's answer is now the READ plus the named
blocker, with NO page change. Re-record `NODE_ID_READ.json` and keep every key you already wrote, except: `product_change` false; `page_maps_node_ref` false; keep
`page_map_blocker`; add `blocking_row` ("DSGN_IRPTV1-D2-W72-S1"); `product_files_changed` []. Add to `verdict_basis` one sentence that on a live served 49 Financial client the
one-account Holdings view loaded and showed that account's own value (the issuer's real run on portal DEV, no client named), and that the producer refuses or withholds an
unequal account (`holdings/snapshot.py:442-443`, `holdings/resolve.py:512`) rather than serving it under a wrong id. Re-run IV123-AC1 (the amended checker is on your branch),
validate the proof instance, and flip this order's `<status>` to complete only when the criterion PASSES. File no further blocking row for the same fact. Row W72-S2 (ARMED,
disarm owner the issuer) is the issuer's to rule; leave it.

<expected_criteria>IV123-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every producer file under `infra/` and every file under `contracts/wire/` (generated).
  `tabs/analysis/` is the other cell's file this round (IV-e-124): do not edit it.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no secret read, no `bun install`, no package change, no dev server on port 5174.
- **Synthetic data only** in any fixture or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
  Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W72-S<k>`, with the real current UTC time; append as BYTES, never re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~72/
portal/src/pages/InvestorReporting/tabs/holdings/
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-123.*
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-123.account-node-id-equals-account-id-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v32 (round 32), cell `IV-e-123`.
<owned_cells>IV-e-123</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV123-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~72/DSGN_IRPTV1.TO-IV-e-123.account-node-id-equals-account-id-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV123-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the denominator and each producer path with the rule that builds its ACCOUNT node id; whether the ids
are equal on all of them; whether the page changed and what; the test and its mutant if any; lint, typecheck and the suite before and after if the page changed; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a read of producer code, with a one-site page change only if the read finds a path where the ids differ. The candidate, if any, is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
