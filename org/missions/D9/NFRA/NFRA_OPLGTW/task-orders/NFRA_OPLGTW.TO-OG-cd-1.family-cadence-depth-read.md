# NFRA_OPLGTW task order -- `OG-cd-1` -- the per-family poll cadence and backfill depth read for MC Portal (R3, PRD v2.6 FWD-20)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cd-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cd-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~65</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code, tests, a plan-free IAM file and ONE off-host live read; nothing is scheduled, deployed or applied. The code reaches the host only through the later release order NFRA_OPLGTW.TO-OG-ap-16 (cut after R1's ledger closes).
comp-iam: RUN-BY-ISSUER at the cut -- the gateway role holds ZERO opal-data-assets S3 and no events: read (infra/aws/terraform/opal-gateway/schwab_reader_iam.tf:37-42, taxsma_gateway_iam.tf:18,131). The cell WRITES the read grant the module needs as a Terraform file and names it in the ask; it plans and applies nothing.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-36 analysis R3 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round36.md @713305ee56) on PRD v2.6 FWD-20, direction XB-20261013T185926Z-4d72 Z3.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (read-only describes and S3 reads).
</preflight>

## 1. THE CELL -- `OG-cd-1` (decomposition addendum R3-T.49, R3)

**The outcome (PRD v2.6 FWD-20, verbatim).** "One read lists every vendor family the deployed gateway serves. For each
family it gives the sweep's schedule, its last sweep, and its history depth (earliest served date), each with the date
read. NFRA_MCPORTAL can display the read." ACCEPT: "The family list comes from the deployed definitions, never a
hand-kept list. The schedule is read live from the AWS schedule, never typed. The depth comes from `backfill-status` and
from the served data's earliest date. Every value carries a claim (measured / inferred / absent). The read is read-only:
no alert, alarm or monitor rides on it (standing moratorium)."

1. **The module.** Write `infra/aws/ec2/opal-gateway/app/family_depth.py` with one public function `read(clients=None)
   -> dict` (clients injectable for tests; boto3 by default). It returns:
   `{"read_at", "denominator", "denominator_source", "families": [{"channel", "family", "schedule", "last_sweep",
   "depth": {"backfill_status_keys", "backfill_frontier", "earliest_served_date"}}]}`, where every leaf value is
   `{"value", "claim", "read_at", "source"}` and `claim` is one of `measured`, `inferred`, `absent`. An `absent` value
   carries its reason in `source`.
   - **Channels** come from the deployed gateway's definitions: the integration registry's active set
     (`app/integrations/registry.py`, as `app/admin_gateway_breakdown.py` `_compute` reads it), plus the native
     Microsoft 365 channel.
   - **Families** come from `infra/aws/terraform/opal-assets/silver.tf` `local.silver_families`. Read it at build time
     into ONE generated file, `app/refs/silver_families.json` (never `DATA_CATALOG.yaml`: NFRA_MCPINDEX is its only
     writer), or read the live Lambda set `opal-assets-silver-*`. Choose one and
     state it in `denominator_source`.
   - **The channel-to-family link** is DERIVED. Use the catalog's dataset roots in `app/refs/DATA_CATALOG.yaml` (each
     read tool's dataset `s3://` root) against each family's bronze/silver source prefix. It is never a typed table. A
     channel with no family reads `family: null`, and its values are `absent`, with the reason "no silver sweep family
     serves this channel's datasets".
   - **Schedule:** `events.describe_rule(Name="opal-assets-silver-<family>-sweep-daily")` `ScheduleExpression`, live.
     The rule name is the one `silver.tf:884` builds.
   - **Last sweep and frontier:** each `s3://opal-data-assets/<family>/<scope>/meta/backfill-status.json` (schema:
     `data/assets/scripts/lib/backfill_status.py`), the `silver` layer's `updated_at` and `frontier_date`. Every key read
     is listed in `backfill_status_keys`.
   - **Earliest served date:** the earliest silver partition date. Use one bounded `list_objects_v2` with a delimiter,
     never a full walk. If it cannot be read within its bound, say so with claim `absent`.
   - **READ-ONLY.** No write, put, delete, invoke or tag call appears in the module.
2. **The mount** is NOT this cell's. Do not edit `app/admin_api.py` or `app/admin_gateway_breakdown.py`; both are
   NFRA_MCPORTAL's. State in your report the one-line route the release needs (for example
   `Route("/gateway/families", ...)` behind `owner_gate.owner_only`), and put it in the ask. The issuer adds it at the
   release.
3. **Tests,** in `infra/aws/ec2/opal-gateway/tests/test_og_cd1.py`, with AWS stubbed:
   - `test_ogcd1_ac01`: a planted extra integration and a planted extra silver family each appear with no code change.
     A channel with no family reads `absent` with its reason.
   - `test_ogcd1_ac02`: every leaf carries a claim from the enum. The schedule equals the stub rule's expression. Depth
     comes from the stub backfill-status and the stub earliest partition.
   - `test_ogcd1_ac03`: a client stub that raises on any write, put, delete or invoke API is never tripped. An unreadable
     source gives `absent` with its reason, never a default.
4. **The grant.** Write the read-only IAM the module needs on the gateway role in a new file
   `infra/aws/terraform/opal-gateway/family_depth_read_iam.tf`:
   - `events:DescribeRule` on the `opal-assets-silver-*-sweep-daily` rules;
   - `s3:GetObject` on `opal-data-assets/*/meta/backfill-status.json`;
   - `s3:ListBucket` on `opal-data-assets`, conditioned to the silver prefixes.

   Every name in the file is `lib/opal_naming.py` `name()` output. A builder REFUSAL is a row, never a hand-typed name.
   Run `terraform fmt -check` on the file only. Do not plan, apply or init.
5. **The one off-host live read.** Run `read()` once from this box, using the box's own AWS credentials through
   `.tools/aws`'s profile (boto3, default chain). Write `W/CD1_LIVE_READ.json`. This exercises the logic against live
   AWS before any release. The on-host read is the release order's.
6. **The ask,** `W/NEVER_WIDEN_ASK_OG-cd-1.md`, for the release order `NFRA_OPLGTW.TO-OG-ap-16`. Halves:
   `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~O`. It covers:
   - the code diff by file;
   - the ONE new read grant (actions, resources and conditions; its plan expectation: N add, 0 change, 0 destroy);
   - the one route line;
   - both branches of a read (every source readable; one unreadable, giving `absent`);
   - the rollback: redeploy the prior live ref, and destroy the one policy.

   That release follows R1 (the r30 release) in the one-at-a-time gateway queue.

## 2. BOUNDS

- Code, tests, one Terraform file (fmt only) and one off-host read. No deploy, release, plan or apply, and no write to
  any AWS store. No edit of NFRA_MCPORTAL's `admin_api.py` or `admin_gateway_breakdown.py`.
- No alert, alarm, monitor, schedule or notification of any kind (standing moratorium).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; type an AWS name by hand.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/family_depth.py
infra/aws/ec2/opal-gateway/app/refs/silver_families.json
infra/aws/ec2/opal-gateway/tests/test_og_cd1.py
infra/aws/terraform/opal-gateway/family_depth_read_iam.tf
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only, also inputs: `infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py`, `app/integrations/registry.py`,
`app/refs/DATA_CATALOG.yaml`, `infra/aws/terraform/opal-assets/silver.tf`, `data/assets/scripts/lib/backfill_status.py`,
`lib/opal_naming.py`, `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` (`ENABLED_INTEGRATIONS`).

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~65/`. Rows: id `NFRA_OPLGTW-Z-W65-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cd-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cd1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cd-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cd1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)families ([1-9]\d*); denominator \1 \([^)]+\); claim-less values 0.*schwab schedule record=.+? live=.+? equal=yes.*schwab backfill frontier record=.+? live=.+? equal=yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the read is derived, claimed and read-only.
- `AC2`: one family's cadence and one family's depth agree with live AWS (the FWD-20 PROOF, off-host).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cd-1.family-cadence-depth-read.proof_of_spec.json`. Validate it after
your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`. Flip the
ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, R3 (round-36 analysis @713305ee56). Cut only after `prd-signoff.py status NFRA_OPLGTW` reads ADMITTED
  (LIMB 6; analysis section 3).
- Rides release `NFRA_OPLGTW.TO-OG-ap-16` (cut-template rule adopted at the round-36 analysis: a deferred-release build
  cell names the release order it rides). That order is cut after R1's (r30) ledger closes, in the one-at-a-time queue.
- NFRA_MCPORTAL displays the read. Its display cell is the MCPORTAL issuer's (`2.0.0_SA_COO~MP`). This cell writes
  nothing of theirs.
- Measured at the cut (2026-10-13 ~20:4xZ):
  - live `opal-assets-silver-schwab-sweep-daily` reads `cron(15 12 * * ? *)`;
  - `s3://opal-data-assets/schwab/08335338/meta/backfill-status.json` has a `silver` layer, frontier 2026-10-12,
    updated 2026-10-13T12:18:13Z;
  - the schwab prefixes are 08242234, 08335338 and 08403355.
- Pre-cut:
  - cd1.AC1 base FAIL as expected (the test file is absent).
  - cd1.AC2 base FAIL as expected (the record is absent). Its GREEN arm PASSED on a planted record carrying the live
    values (schedule equal, frontier equal), and the fixture was removed.

- A1 (issuer, 2026-10-13 ~22:0xZ, row Z-W65-S4): AC2's `<expect>` used `record=\S+ live=\S+`, which can never match a
  live EventBridge expression (`cron(15 12 * * ? *)` holds spaces). This was the issuer's defect at the cut: the green arm
  was planted with a space-free value. Now `record=.+? live=.+? equal=yes` on both lines. Measured on worker ~65's real
  output: the old form does not match, the new one does, and a red `equal=no` output still fails. No code is re-run.
  Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<slot>~65</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
