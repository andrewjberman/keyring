# ETFS_RIVALS task order -- `RIV-d-5` -- ROUND 4 (ENRICHMENT): THE LIVE JOIN (WORLD) -- DEPLOY, GQGU IMPORT, PER-SOURCE FLOORS, REPLAY, READ

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-d-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~4</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~12:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/ or the etfs-rivalfunds stack; re-run by the worker before the apply (NEVER-2 reads every live worktree's .open_deploys/).
comp-iam: RUN at L5 -- the pair names any widening; the fetch-holdings Lambda's GQGU fetch is egress to the issuer's public site (the BASG route's twin), not an IAM change; any role change is a named key, simulated before the apply.
comp-adversary: RUN at L5 on the round-4 decomposition; the act is bounded by the never-widen pair.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: rival active ETFs in two peer groups, each fund's trade schedule,
and a served page (`/rivalfunds`) grouped by Opal fund. Round 4's five build cells (own-prior-date pairing, one revision contract,
BASG's issuer alias, GQGU's issuer route, per-source identity floors) are merged at CLOUD; **this cell puts them live and reads them
back.** Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 0. BEGIN ONLY WHEN THESE HOLD

1. RIV-t-5, RIV-v-2, RIV-i-2, RIV-q-1 and RIV-f-3 are complete and MERGED; your worktree is cut from that merged HEAD (print
   `git log --oneline -3`).
2. BOTH never-widen halves are COMMITTED: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/NEVER_WIDEN_HALF_COO_D5.md`
   and 1.0.0_SA_CTO~Z's half, named in your spawn line. Act only inside them, key by key; an action a generator adds that a half
   does not name is disclosed BEFORE the apply (CTO forward condition, addendum @5247bfbb2d).
3. NEVER-2: read EVERY live worktree's `org/critical_paths/.open_deploys/` (union, per-tree denominator); open the ledger entry
   `etfs-rivalfunds-round4` with `.tools/deploy_ledger.py open` and COMMIT entry + sentinel before any apply.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-d-5` -- the live join of round 4 (WORLD)

Under a NEVER-2 ledger entry `etfs-rivalfunds-round4` and a never-widen pair signed by `1.0.0_SA_CTO~Z` and this seat (written by the
issuer at d-5's cut, after cells 1-5 are merged, with the served delta MEASURED per fund by `round3/served_delta_r3.py` widened to
GQGU):
1. Update the five Lambdas in place.
2. Import the 305 archived GQGU days as issuer bronze (QA-class, provenance); silver and G1 by marker.
3. Set the per-source floors in `guardrails_config.json` from each source's measured newest reports (rounded down) and record them.
4. Replay G1, G5 and G6 over the window the served-delta names; publish the page.
5. Read it back and record `d5_live.json`.

The next trading day's 07:00 issuer fetch for both funds, 08:03 leg and 09:00 sweep are the acceptance, read at the close.

## 2. THE RECORD YOU WRITE (`deliverables/0.9.0_WK_ETFS_RIVALS~4/d5_live.json`) -- the checks read exactly these keys

- `page_day` (the page date you published), `publish_marker` (its s3 URI);
- `floors`: `{issuer, bloomberg, home_producer}` -- the values you committed in `guardrails_config.json` (each the minimum newest-date
  resolved fraction of that source's funds, rounded DOWN to 2 decimals; print the per-fund fractions beside them);
- `replay_window`: `{start, end}` of the G1/G5/G6 replay; `newest_report_date`;
- `gqgu_import`: `{files, first, last, bronze_objects, silver_objects}`;
- `apply`, `iam_simulation`, `lambda_request_ids`, `s3_prefixes` with object counts, `remaining` (empty when done).

## 3. SURFACES AND BOUNDS

You READ (never edit): every package module, `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct
no-modify order), `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/` (all seats), `.tools/deploy_ledger.py`, `.tools/safe-apply`,
`infra/aws/lambda/README.md`, the device-local GQGU archive `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\amgt-reconn-daily-census-20260929\gqgu\`.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~4/`). NEVER: `etfs-netassets-daily` or its homes; the
bucket's tier-first keys or `bbg/`; `opal-data-assets`; any OpenAI call; any Bloomberg request (GQGU's BQL stays withdrawn); any
alert, alarm, SNS or monitor; `aws lambda update-function-code`; bare `terraform apply`; an S3 delete.

<paths>
data/etfs/scripts/rivalfunds/guardrails_config.json
infra/aws/terraform/etfs-rivalfunds/
infra/aws/lambda/etfs-pipeline/etfs-rivalfunds-*
infra/aws/lambda/etfs-pipeline/rivalfunds-*
infra/aws/lambda/etfs-pipeline/rivalfunds_package.py
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/.open_deploys/etfs-rivalfunds-round4.json
org/critical_paths/.open_deploys/etfs-rivalfunds-round4-a1.json
org/critical_paths/change_management/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

**AMENDMENT 1 -- ADDENDUM ACT A1-A3 (issuer ruling on rows Z-W4-S12 / Z-W4-S13, 2026-10-01).** Both addendum halves are COMMITTED: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/NEVER_WIDEN_HALF_COO_D5_ADDENDUM1.md` (@ad07f847d2) and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/NEVER_WIDEN_ROUND4_D5_ADDENDUM1_CTO_HALF.md` (@1ef54f4ff8), pin CLOUD 25f4ac5418. Act only inside them: (A1) the five stage Lambdas in place to the package at your merged HEAD (it carries the RIV-q-1 G2 fix); (A2) replay G2 `holdings_coverage` over the window in windows well under 900 s; (A3) republish the page for 2026-10-01. Gates before A1: `python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/served_delta_g2.py --deployed 5a4b5b5391 --out deliverables/0.9.0_WK_ETFS_RIVALS~4/served_delta_g2_act.json` equals the addendum's table (GQGU +307, every other fund 0 changed, 0 cross-fund, control 4094/4094); the plan is EXACTLY five source_code_hash updates (any other action: disclose, STOP); the five live CodeSha256 values equal `evidence/lambda_after_apply_r4.txt`; NEVER-2 union read, then open and COMMIT ledger entry `etfs-rivalfunds-round4-a1` + sentinel. Deadline: A1-A3 complete before 10:00Z 2026-10-02, else do nothing (CTO fallback). Record A1-A3 in `d5_live.json` under `addendum1` (request ids, CodeSha256 before/after, G2 rows per fund, publish marker); re-run AC1-AC3; close the ledger entry.

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the served page shows GQGU with issuer data, the committed config carries the recorded per-source floors, and no fund
  is not-updated by identity_coverage (`.../round4/checks/d-5.AC1.py`)
- **AC2** -- TSEL's and WCMG's served windows in the replay window each start on that fund's own prior report date
  (`.../round4/checks/d-5.AC2.py`)
- **AC3** -- served G1 2026-09-29 takes GICS from the live G4 only, and BASG's newest report date resolves >= 0.90
  (`.../round4/checks/d-5.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-d-5"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/d-5.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-d-5"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/d-5.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC3" cell_refs="RIV-d-5"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/checks/d-5.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~4/ETFS_RIVALS.TO-RIV-d-5.live-join-round4.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-d-5.live-join-round4`; pin every artifact row to the commit that carried it. Report once: each verdict line with the output above it; files written; ledger key states; rows filed. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-3 analysis items 1-4 joined live. Checks dry-run at base 48ec92238a: d-5.AC1/AC2 FAIL
(no act record), d-5.AC3 FAIL (`revision` absent) -- each FAIL as expected. Staged until the five build cells merge; the COO half is
written then with the served delta measured per fund.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>4</round>
<slot>~4</slot>
<fabric>site-z</fabric>
