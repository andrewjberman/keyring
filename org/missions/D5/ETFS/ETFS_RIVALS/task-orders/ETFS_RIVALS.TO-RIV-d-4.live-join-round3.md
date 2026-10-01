# ETFS_RIVALS task order -- `RIV-d-4` -- ROUND 3 (ENRICHMENT): THE LIVE JOIN (WORLD) -- DEPLOY, FLOOR, ISSUER RE-CAPTURE CONTROL, G4, REPLAY, READ

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-d-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~4</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~06:4xZ, --drift) -- 2 armed gates fabric-wide, none names rivalfunds/, bloomberg/etfs/, gold/security_market/ or the etfs-rivalfunds stack; re-run by the worker before the apply (NEVER-2 reads every live worktree's .open_deploys/).
comp-iam: RUN at L5 -- the canonical-shape Lambda gains READS of bbg/<D>/constituents/ (the home landing) and gold/security_market/ (G4); the terminal machine's identity gains the G4 WRITE. Each is named in the pair and simulated before the apply/landing; nothing else widens; no DeleteObject anywhere.
comp-adversary: RUN at L5 on the round-3 decomposition (3 of 3 cited commits verified); the act is bounded by the never-widen pair.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: rival active ETFs in two peer groups, each fund's trade schedule,
and a served page (`/rivalfunds`) grouped by Opal fund. Round 3's five build cells (repairs, the home-producer reader, identity, G4,
the GICS join) are merged at CLOUD; **this cell puts them live and reads them back.** Work ONLY in the worktree your spawn line
names; every path below is relative to that root.

## 0. BEGIN ONLY WHEN THESE HOLD

1. RIV-r-3, RIV-hp-1, RIV-i-1, RIV-s-4 and RIV-g-6 are complete and MERGED; your worktree is cut from that merged HEAD (print
   `git log --oneline -3`).
2. BOTH never-widen halves are COMMITTED: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/NEVER_WIDEN_HALF_COO_D4.md`
   and 1.0.0_SA_CTO~Z's half, named in your spawn line. Act only inside them.
3. NEVER-2: read EVERY live worktree's `org/critical_paths/.open_deploys/` (union, per-tree denominator); open the ledger entry
   `etfs-rivalfunds-round3` with `.tools/deploy_ledger.py open` and COMMIT entry + sentinel before any apply; close it or roll back
   per key and say so.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-d-4` -- the live join of round 3 (WORLD)

Under a NEVER-2 ledger entry opened and committed first, and a never-widen pair signed by `1.0.0_SA_CTO~Z` and this seat (written by
the issuer at d-4's cut, after cells 1-5 are merged):
1. Update the five Lambdas' code in place (`safe-apply`; the plan is `source_code_hash` updates only).
2. Set the publisher's `identity_coverage` floor from RIV-i-1's measured fraction (a one-constant hookup).
3. The issuer-retain positive control: one live re-capture of a LANDED BASG report date through the deployed fetch-holdings Lambda
   in `backfill` mode for that one date, then silver and G1 by marker.
4. G4 import from the newest Positioning `characteristics.parquet` (QA-class).
5. Replay G1, G2, G5/G6 for the window the home landings cover, then publish the page.
6. Read the page back; record `d4_live.json`.
7. If the Terminal reads signed in, also run the live `market` pull and one scripted GQGU holdings request (row Z-S6's measurement).

The next trading day's 08:03 leg + 09:00 sweep is the acceptance, read at the close; it is never waited on.

## 2. THE RECORD YOU WRITE (`deliverables/0.9.0_WK_ETFS_RIVALS~4/d4_live.json`) -- the checks read exactly these keys

- `page_day` (the page date you published), `publish_marker` (its s3 URI);
- `control`: `{report_date, recapture_capture_id, silver_marker}` (the `<ts>-<sha12>` id of the re-capture, the s3 URI of its
  build-silver marker);
- `newest_report_date` (the newest G1 report date you replayed), `identity_floor` (the number you set; from
  `deliverables/0.9.0_WK_ETFS_RIVALS~1/i1_identity.json`, the minimum per-fund fraction rounded DOWN to 2 decimals);
- `apply` (plan line counts and the five functions), `iam_simulation`, `lambda_request_ids`, `s3_prefixes` with object counts,
  `terminal` (health read and whether step 7 ran), `remaining` (empty when done).

## 3. SURFACES AND BOUNDS

You READ (never edit): every package module, `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify
order), `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/` (all seats), `.tools/deploy_ledger.py`, `.tools/safe-apply`,
`infra/aws/lambda/README.md`.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~4/`). NEVER: `etfs-netassets-daily` or its homes; the
bucket's tier-first keys (`bronze/`, `silver/`, `gold/`, `daily/`, `platinum/`) or `bbg/`; `opal-data-assets`; any OpenAI call; an
interactive Bloomberg call (step 7 is the scripted `enrichment_bloomberg` / `collector_bloomberg` only); any alert, alarm, SNS or
monitor; `aws lambda update-function-code`; bare `terraform apply`.

<paths>
data/etfs/scripts/rivalfunds/publish_page.py
infra/aws/terraform/etfs-rivalfunds/
infra/aws/lambda/etfs-pipeline/etfs-rivalfunds-*
infra/aws/lambda/etfs-pipeline/rivalfunds-*
infra/aws/lambda/etfs-pipeline/rivalfunds_package.py
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/.open_deploys/etfs-rivalfunds-round3.json
org/critical_paths/change_management/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the served page shows IDVZ and PFOE with data, freshness reasons count trading days, and the publish marker names every
  not-updated fund (`.../round3/checks/d-4.AC1.py`)
- **AC2** -- the live re-capture kept the earlier silver object, wrote an OK marker, and G1 reads the new capture
  (`.../round3/checks/d-4.AC2.py`)
- **AC3** -- served G1 resolves identity at or above the measured floor per fund, a served G4 exists, and G1 carries RESOLVED GICS
  (`.../round3/checks/d-4.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-d-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/d-4.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-d-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/d-4.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC3" cell_refs="RIV-d-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/d-4.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~4/ETFS_RIVALS.TO-RIV-d-4.live-join-round3.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-d-4.live-join-round3`. Report once: each verdict line with the output above it; files written; ledger key states; rows filed. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-2 analysis items 1-5 joined live; ruling 1's control (re-capture of a landed BASG
date) under this cell's pair. Checks dry-run at base 78167bb8fc: d-4.AC1/AC2/AC3 FAIL (no act record) -- each FAIL as expected.
Staged until cells r-3, hp-1, i-1, s-4, g-6 merge; the COO half is written then, with the expected outcomes read from the merged code.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>staged</status>
<round>3</round>
<slot>~4</slot>
<fabric>site-z</fabric>
