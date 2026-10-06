# ETFS_RIVALS task order -- `RIV-iam-1` -- ROUND 10 (ENRICHMENT): THE IAM GRANT FOR ROUND 9'S TWO TABLES: gold/security_names READ, gold/security_universe READ/WRITE (Z-S31)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-iam-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RV</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the issuer registers any stage at the merge)
comp-iam: RUN at L5 -- LIVE plane, `aws iam simulate-principal-policy` on etfs-rivalfunds-daily-role and rivalfunds-publish-page-role (round10/checks/iam-1.AC1.py at the cut): gold/security_names list+get and gold/security_universe put+get implicitDeny on both; gold/holding_contribution get allowed (positive control); APPLICABLE -- this cell widens exactly those two prefixes on those two policies
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 10** (the round-9 analysis): the G4 enrichment never lands an all-empty or all-error revision (S25, first), one key per security, a replay tool for the four code-defect classes of the G5 history (G3-pinned), and the IAM grant for round 9's two tables. Nothing in round 10 deploys, merges, flips a gate or calls Bloomberg from a worker (the AE seat's apply is under its own never-widen pair). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-iam-1` -- the IAM grant for round 9's two tables (row Z-S31; CTO~Z msg 29806)
- Measured 2026-10-05: the D12 Step B refresh republish failed holding_contribution with "etfs-rivalfunds-daily-role ... not
  authorized to perform: s3:ListBucket on opal-data-etfs" (the gold/security_names read); the sweep's security_universe write has no
  grant either; `gen_policies.py` names neither prefix.
- Interface: `gen_policies.py` grants the publish-page stage (so the daily union role) Get + List on `rivalfunds/etfs/gold/security_names/`
  and Put + Get + List on `rivalfunds/etfs/gold/security_universe/`, regenerated, planned (only the two role policies change) and
  applied under its own never-widen pair; nothing else widens.
- **Organic trigger:** the 07:00 ET marker publish and the 09:00 ET sweep (holding_contribution, build-security-universe).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 33d9077d5f (the package equals the deployed pin b8b47bb8e7))

- The patch is ready: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/Z-S31_IAM_GRANT_FOR_AE.patch`
  (gen_policies.py + the two regenerated policy files); apply it, regenerate with `python infra/aws/terraform/etfs-rivalfunds/gen_policies.py
  --out infra/aws/terraform/etfs-rivalfunds`, and confirm the regenerated files equal the patch's.
- The check simulates the LIVE roles (`aws iam simulate-principal-policy`, read-only): it FAILS until the apply lands. Before the apply,
  ask the never-widen pair -- 2.0.0_SA_COO~RV and 1.0.0_SA_CTO~Z -- with the plan text and the before/after policy documents.
- Apply with `safe-apply` from a saved plan; open and close a NEVER-2 ledger entry (`.tools/deploy_ledger.py`), committing its sentinel
  at open.
- (Issuer amendment, 2026-10-05 23:2xZ.) The plan changes the two role policies ONLY -- zero Lambda code changes. CLOUD now carries
  round-10 code (RIV-eg-1, RIV-ok-1) that must NOT deploy before the issuer's G5 replay, and `lambdas.tf` hashes the package staged
  under `<tree root>/.runtime/rivalfunds-build`. So stage that package at the deployed pin b8b47bb8e7 (`git worktree add <path>
  b8b47bb8e7`, apply the policy edit there, run `python infra/aws/lambda/etfs-pipeline/rivalfunds_package.py` there, plan there), or plan with
  `-target` on the two role-policy resources. Live code today: daily CGLr1BNO, fetch nhBoabXY, canonical wLYfa47Z, silver CTEET1+c,
  publish RBRmqCj9 -- a plan naming any `source_code_hash` change is wrong.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{8,9}/checks/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 10), the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round9.md`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.7.0_AE_CloudOps~RV/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-10 chain owns. Tests go beside the code as `tests/test_r10iam1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
infra/aws/terraform/etfs-rivalfunds/gen_policies.py
infra/aws/terraform/etfs-rivalfunds/policies/etfs-rivalfunds-daily-lambda.json
infra/aws/terraform/etfs-rivalfunds/policies/rivalfunds-publish-page-lambda.json
infra/aws/terraform/etfs-rivalfunds/generated.auto.tfvars.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/etfs-rivalfunds-iam-1.json
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.7.0_AE_CloudOps~RV/
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the live daily and publish-page roles may list/get gold/security_names and put/get gold/security_universe; put on security_names and a sibling prefix stay denied; an already-granted prefix reads allowed (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/iam-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-iam-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/iam-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.7.0_AE_CloudOps~RV/ETFS_RIVALS.TO-RIV-iam-1.round9-table-grants.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-iam-1.round9-table-grants`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round9.md @f68eb77491 section 4 (+ CTO~Z msg 29806: rp-2 option A; iam-1 to an AE seat with a simulate arm); decomposition round 10 v1.0. Chain `~RV`, slot `~RV`, position 1 of 1. Checks dry-run at base CLOUD 33d9077d5f (the package equals the deployed pin b8b47bb8e7): iam-1.AC1 FAIL (4; controls OK) as expected (simulated live, read-only). Bounds: no deploy before the issuer's never-widen pair; rp-2's served replay is an issuer act after the tool lands and BEFORE ok-1 deploys (ok-1 re-keys).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>10</round>
<slot>~RV</slot>
<fabric>site-z</fabric>
<status>complete</status>
