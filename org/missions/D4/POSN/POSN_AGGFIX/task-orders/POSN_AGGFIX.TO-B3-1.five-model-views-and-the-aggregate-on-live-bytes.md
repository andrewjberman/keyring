# TO POSN_AGGFIX.TO-B3-1 -- THE SERVED READ: the five model views unchanged for an advisor and a client across the producer deploy, and the aggregate on the live Opal-only file as Opal staff, through the live edge (AF1-s-16; FWD-8, FWD-7, FWD-1, FWD-3)

<to_id>POSN_AGGFIX.TO-B3-1</to_id>
<project>POSN_AGGFIX</project>
<issued_to>0.9.0_WK_POSN_AGGFIX~3</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-15</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md` **v0.2**
@`cbd85e5cff` (C-FIVE-BOOKS-UNCHANGED, C-OPAL-ONLY-DATA) - **Decomp cell:** `AF1-s-16` - **Issuance:** round 1, slot `~3`, THIRD in this
slot's queue. **Handed to you only after TO-B2-1, TO-A3-1 and TO-C1-1 have ALL drained onto SITEZ** (the three chains join here).
READ-ONLY toward the cloud: no deploy, no served write, no promote.

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_AGGFIX~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_AGGFIX~3;`. Workspace worktree
`/c/tmp/wk-aggfix-1-3` (branch `wk-posn_aggfix-1-3`); portal worktree `/c/tmp/wk-aggfix-1-3/portal` on YOUR branch `wk-aggfix-1-3-portal`
carrying TO-B1-1 and TO-B2-1 (verify `git -C /c/tmp/wk-aggfix-1-3/portal merge-base --is-ancestor edf85ce503 HEAD`). First act:
`git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, then bring SITEZ into the workspace branch
(`git merge-base --is-ancestor SITEZ HEAD || git merge --no-edit SITEZ`; never a rebase) so TO-A3-1's and TO-C1-1's proof instances and
scripts are in your tree. Workspace commits via `bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_AGGFIX~3
<0.9.0_WK_POSN_AGGFIX~3@opal.agent>" -F <msgfile> -- <paths>` (msgfile by the Write tool, PURE ASCII). Never push, rebase, `checkout --`,
`clean`. Scratch in `/c/tmp/wk-aggfix-1-3/.scratch/` only. **Secrets:** the live edge arm reuses TO-C1-1's token script, which reads
`opal/auth/jwt-private-key` ONLY through `comp-secrets get opal/auth/jwt-private-key --reveal` inside the signing process; the key and
every token are NEVER printed, written, placed in argv or committed; tokens live no more than 300 s.

## THE CELL (verbatim from the decomposition @`605c03f81f`)

**`AF1-s-16` -- the five model views unchanged, and the aggregate on live bytes (S16, C-FIVE-BOOKS-UNCHANGED).** On the drain ref carrying
AF1-s-12..s-15: the page rendered as an advisor and as a client, Models mode, each of the five books, once with the shared file's PRIOR
served version and once with the version AF1-s-10 wrote (VersionIds from AF1-s-10's proof), holdings and weights text identical per book (a
positive control: a one-weight mutation of the fixture differs); and as an Opal user with the LIVE `opal_aggregate.json` bytes, the aggregate
present with both panels and the five breakdown columns.

**Your inputs (at SITEZ after the merge, never re-derived):** `deliverables/0.9.0_WK_POSN_AGGFIX~1/POSN_AGGFIX.TO-A3-1.deploy-the-producer-and-read-the-served-result.proof_of_spec.json`
(the prior and new VersionIds of `json/positioning/positioning_data.json` that A3-AC8/AC9 recorded); TO-C1-1's proof instance
`deliverables/0.9.0_WK_POSN_AGGFIX~2/POSN_AGGFIX.TO-C1-1.edge-refuses-the-aggregate-outside-opal.proof_of_spec.json` (the path of the
script C1-AC13 ran); your own `B_DOM_BEFORE.json`, `<FIVE_BOOKS_DOM_B>` and `<AGG_DOM_B2>`. Your portal branch HEAD is the tree AF1-s-12..s-15
landed on; the COO drains it onto `refs/drains/aggfix-1-portal` at each of your drains, so your branch HEAD and that ref carry the same tree.

## YOUR ACT

1. `<LIVE_FIXTURES_B3>`: read the two VersionIds from TO-A3-1's instance; fetch both objects by VersionId and the live
   `json/positioning/opal_aggregate.json` (its VersionId printed), decompress, and write the three fixture sets to `.scratch/`.
2. Run the criteria. Commit the deliverables. Record every criterion.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, id `POSN_AGGFIX-Z-W3-S<k>` continuing your sequence, in
`org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working.

## CRITERIA -- structured, one clause each

<criterion id="B3-AC1" cell_refs="AF1-s-16"><invocation>timeout 300 python <LIVE_FIXTURES_B3></invocation><expect>the prior and new VersionIds of json/positioning/positioning_data.json read from TO-A3-1's proof instance and printed; both objects fetched by VersionId (LastModified printed, the prior one earlier); the prior carrying current_holdings UST ST INT LT ULT AGG and the new one UST ST INT LT ULT; the live json/positioning/opal_aggregate.json fetched with its VersionId, decompressed, status OK and a non-empty current_holdings.AGG.holdings; three fixture files written.</expect></criterion> `B3-AC1` -- THE LIVE BYTES, PINNED BY VERSION.

<criterion id="B3-AC2" cell_refs="AF1-s-16"><invocation>timeout 900 node <FIVE_BOOKS_DOM_B> --prior-vs-new .scratch/b3_fixtures</invocation><expect>at your portal branch HEAD, as an advisor and as a client, Models mode, UST ST INT LT ULT: the composition labels and the breakdown rows rendered on the PRIOR shared file and on the NEW shared file IDENTICAL per book (`IDENTICAL 10 of 10`); and the control -- the NEW fixture with one holding weight mutated -- reported as a difference.</expect></criterion> `B3-AC2` -- WHAT ADVISORS AND CLIENTS SEE, ACROSS THE DEPLOY.

<criterion id="B3-AC3" cell_refs="AF1-s-16"><invocation>timeout 900 node <AGG_DOM_B2> --viewer opal-staff --remembered none --fixtures .scratch/b3_fixtures</invocation><expect>on the NEW shared file and the LIVE aggregate bytes: the page lands on Aggregate; the Portfolio Composition entries and the Holdings Breakdown rows each count equal to the live current_holdings.AGG.holdings length; the five Model Breakdown columns present with three sampled cells equal to model_breakdown x 100 at one decimal; a screenshot saved.</expect></criterion> `B3-AC3` -- THE AGGREGATE ON LIVE BYTES, AS OPAL STAFF.

<criterion id="B3-AC4" cell_refs="AF1-s-16"><invocation>timeout 900 node <LIVE_TIER_ARMS_FROM_C1> --phase post</invocation><expect>the script is the one TO-C1-1's instance names for C1-AC13 (its path printed first); on the live distribution after TO-A3-1: Opal-staff and Dev tokens on /api/general/positioning/opal_aggregate.json return 200 with a body whose status is OK; advisor-class and client-class tokens on both aggregate URLs return 401; all four classes on /api/general/positioning/positioning_data.json return 200 and that body carries no current_holdings.AGG.</expect></criterion> `B3-AC4` -- THROUGH THE LIVE EDGE: OPAL GETS IT, NOBODY ELSE DOES.

<criterion id="B3-AC5" cell_refs="AF1-s-16" judgment="true"/> `B3-AC5` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9:** whether B3-AC2's identity across the deploy is the FWD-8 bar ("the same holdings and weights") on the page advisors and clients read, and whether anything an advisor or a client can reach in B3-AC4's responses reveals Opal's model mix or total. Record the readings and offer NO verdict.

<expected_criteria>B3-AC1, B3-AC2, B3-AC3, B3-AC4, B3-AC5</expected_criteria>

<placeholders>LIVE_FIXTURES_B3, FIVE_BOOKS_DOM_B, AGG_DOM_B2, LIVE_TIER_ARMS_FROM_C1</placeholders>

<paths>
org/missions/D4/POSN/POSN_AGGFIX/task-orders/POSN_AGGFIX.TO-B3-1.five-model-views-and-the-aggregate-on-live-bytes.md
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/
org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_AGGFIX/decompositions/POSN_AGGFIX_DECOMP.md</decomp_doc> round 1 @`605c03f81f`.
<owned_cells>AF1-s-16</owned_cells>
Read-dependencies, NOT claimed: `AF1-s-10` (TO-A3-1's VersionIds), `AF1-s-11` (TO-C1-1's live gate and token script), `AF1-s-14` (TO-B2-1's
rendered tree), `AF1-s-13`/`AF1-s-15` (TO-B1-1). The served page after Andrew's promote word is read at L10 by the grader, not here.
</decomp_ref>

<preflight>
comp-schedule: RUN at the cut (2026-09-15 ~18:3xZ) -- 7 armed gates, 0 POSN; no deploy, promote or push in this order.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only S3 GETs by VersionId and HTTPS requests with short-lived tokens; no grant changes.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) if the scheduled pipeline runs between TO-A3-1's driven run and this order, the shared file's LATEST version is not A3's -- this order reads by VersionId for exactly that reason; (2) CloudFront may serve a cached copy of the shared file for a short window after the invalidation; B3-AC4's control reads the served body; (3) the issuer has not run the edge token script; its correctness is TO-C1-1's proof.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/POSN_AGGFIX.TO-B3-1.five-model-views-and-the-aggregate-on-live-bytes.proof_of_spec.json
</proof_of_spec>
