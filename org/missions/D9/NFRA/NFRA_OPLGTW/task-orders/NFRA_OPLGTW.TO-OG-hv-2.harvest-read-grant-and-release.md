# NFRA_OPLGTW task order -- `OG-hv-2` -- APPLY: the harvest read grant on gateway-global-internal-reader-role and the gateway release of OG-hv-1's two tools (R4, FWD-21)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-hv-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-hv-2</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- gateway queue: NFRA_MCPORTAL MP-z-5 (in flight, applier 0.7.0_AE_CloudOps~MQ), then round 37's R1, NFRA_OPLGTW.TO-OG-ap-14 (the r30 release: OG-pf-1 + OG-tg-1 + OG-bd-2 + OG-sh-1), then THIS release; gateway releases go one at a time (round-36 analysis section 3). PHASE A starts only when OG-ap-14's NEVER-2 ledger nfra-oplgtw-gateway-release-r30 reads CLOSED at HEAD. B window 11:00Z-23:00Z. No cron, alarm or monitor is created.
comp-iam: RUN-BY-ISSUER at the cut, for every API call OG-hv-1's code makes: s3:GetObject and s3:ListBucket (list_objects_v2) on opal-data-harvest by opal-gateway-role. simulate-principal-policy opal-gateway-role s3:GetObject opal-data-harvest/packs/1299_HK_Equity/input_ledger.json -> implicitDeny; wsj/harvest/x -> implicitDeny; control opal-data-portal-v2/json/x.json -> allowed (2026-10-13 ~20:4xZ). get-bucket-policy opal-data-harvest -> NoSuchBucketPolicy (no bucket-side deny or grant to add); get-bucket-encryption -> AES256 (no kms:Decrypt needed). The new policy is an aws_iam_role_policy (inline) on aws_iam_role.gw: no ForceNew field is changed on the role; the policy's `name` and `role` are ForceNew on the new resource only (plan bar: 1 to add, 0 to change, 0 to destroy). Name from the builder: `python -c "import sys; sys.path.insert(0,'lib'); import opal_naming as n; print(n.name(system='gateway', scope='global', function='harvest-read', kind='policy'))"` -> gateway-global-harvest-read-policy.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-36 analysis R4 (ledger/ROUND_ANALYSIS.round36.md @713305ee56) on PRD v2.7 FWD-21 (@27ba6b6191: V1 admits by identity, the grant writer writes nothing; CTO msg 33764) and Andrew-direct ~20:0xZ call 8; the build is OG-hv-1.
Lane check of <paths>: EC2_MANIFEST.json is lane SHARED_CLOUD_OPS and infra/aws/terraform/** falls under infra/aws/**; 0.7.0_AE_CloudOps~Z committed both under an OPLGTW order grant before (d8f0b20b8a OG-ap-10 B2; f17393675e OG-ap-7 B2). The runbook, change_management/ and the sentinel are named below.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-hv-2` (decomposition addendum R3-T.49, R4)

Ship OG-hv-1's `harvest_list` and `harvest_read` (built on box/sitez, drained by the issuer) and the IAM read grant they
need. Andrew (2026-10-13 ~20:0xZ, call 8): all 24 prefixes of `opal-data-harvest` SERVE to Opal principals, raw included;
a non-Opal principal is refused on every prefix. Today `opal-gateway-role` AND `gateway-global-internal-reader-role` are
implicitDeny on the bucket; `harvest_read.py` reads through the second (`internal_role.s3_client()`, the assumed
`INTERNAL_READER_ROLE_ARN`, no fallback), so the grant goes on THAT role (A5).

### PHASE A (when OG-ap-14's ledger `nfra-oplgtw-gateway-release-r30` is CLOSED): re-cut, grant file, ask. NO apply, NO deploy

1. **Live ref.** Read `services.opal-gateway.deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json` at HEAD, then one SSM md5
   read of the host against it, walking `app/`, `deploy/` and `dashboard/`. A mismatch is a STOP and a BLOCKING row.
2. **Re-cut** in a worktree `C:/tmp/og-rel-hv`, new branch `rel-nfra-oplgtw-hv`, at that live ref. Take OG-hv-1's own hunks
   only (`git diff <hv-1 build commit>~1 <hv-1 build commit> -- infra/aws/ec2/opal-gateway`; the issuer's drain message names
   the commit): `app/harvest_read.py` and `tests/test_og_hv1.py` whole; `app/tools.py`, `app/data_entitlement.py`,
   `app/destructive_ops.py`, `tests/test_entitlement_admin.py` and `tests/test_data_entitlement_family.py` by hunk, 3-way
   where the base differs. Never take a whole file from trunk for those five. Commit with the audited
   `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the release commit only. Write `W/hv2_release.json` = `{"base_sha",
   "release_sha"}`. Run the release tree's `tests/test_og_hv1.py`, `tests/test_entitlement_admin.py` and
   `tests/test_data_entitlement_family.py`.
3. **The grant file**, on box/sitez (not the release branch): `infra/aws/terraform/opal-gateway/harvest_read_iam.tf`, ONE
   `aws_iam_role_policy` on `aws_iam_role.int_reader` (defined in `mcpmsp_internal_reader.tf`; NEVER `aws_iam_role.gw`), named by the builder (`gateway-global-harvest-read-policy`):
   - `s3:GetObject` on `arn:aws:s3:::opal-data-harvest/<prefix>*` for EXACTLY the 24 prefixes of `app/harvest_read.py`
     `SERVED_PREFIXES` (read from that file; never typed);
   - `s3:ListBucket` on `arn:aws:s3:::opal-data-harvest` with `Condition StringLike s3:prefix` = those 24 prefixes, each with
     and without a trailing `*`;
   - nothing else: no Put, no Delete, no bucket-wide object read.
   Run a targeted `terraform plan -target=...` directly (`safe-apply` gates `apply` only; a plan is non-destructive: A6)
   and record it: 1 to add, 0 to change, 0 to destroy. The APPLY in step 5 is `safe-apply`, targeted at the one resource.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-hv-2.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`; it
   WIDENS the gateway's reach). It carries: the release diff by file; **two widenings, each named as one** (PRD v2.8): the
   gateway's reach to the 24 prefixes for Opal principals, AND `gateway-global-internal-reader-role`'s own S3 read on `opal-data-harvest` (the role `harvest_read` assumes);
   the research-only boundary (an asset manager stays refused every Schwab and Black Diamond tool unless Andrew admits it
   to v2.2's connected set); the two tools and their refusals; the grant (24
   prefix ARNs, the ListBucket condition, the plan line); tools 63 -> 65 on the live census, no `.env` key change, no
   `ENABLED_INTEGRATIONS` change; writers N printed; the order of acts (the grant under ledger
   `nfra-oplgtw-harvest-read-grant`, THEN the deploy under `nfra-oplgtw-gateway-release-hv`, so no request runs the new code
   without the grant); the rollback per act (redeploy the base; destroy the one policy); the triggers (`/health`, tools
   +2 only, `.env` names unchanged, md5 = release). Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

5. Ledger `nfra-oplgtw-harvest-read-grant`, entry AND sentinel first; `safe-apply` the targeted policy; read it back
   (`get-role-policy` on `gateway-global-internal-reader-role`); simulate THAT role (`arn:aws:iam::313476888478:role/gateway-global-internal-reader-role`,
   never `opal-gateway-role`) `s3:GetObject` on one `packs/` key -> allowed, one `wsj/harvest/` key ->
   allowed, and the control `opal-data-harvest/zzz-not-served/x` -> implicitDeny (ONE `--resource-arns` per call). Write
   `W/HV2_IAM_SIM.json` = `{"role": "gateway-global-internal-reader-role", "packs": "...", "wsj_harvest": "...",
   "control_unlisted": "..."}`. Close the ledger.
6. Ledger `nfra-oplgtw-gateway-release-hv`, entry AND sentinel first. Deploy from `C:/tmp/og-rel-hv` through
   `infra/aws/ec2/safe-ec2-deploy.sh` with `DEPLOY_BASE_REF=<base_sha>`. The release cone carries `lib/`, `.tools/`,
   `org/modules/graph/`, `data/transcripts/scripts/teams/` AND your agent home `org/tier2_senior/0.7.0_AE_CloudOps~Z/`. No
   `HALT_OVERRIDE`. Read back immediately against the triggers; on any trigger redeploy the base and file an ARMED row
   naming `2.0.0_SA_COO~O`.
7. **The served read**: one SSM read through the INSTALLED code, calling each tool's function under a synthetic principal
   context, writing `W/HV2_SERVED.json` = `{"body": {...}}` with: `tools_listed` (both names present), `opal_packs_read`
   (an Opal principal's `harvest_read` of one real `packs/<name>/input_ledger.json` returns parsed JSON; print only True/False
   and the byte count), `non_opal_refused_packs`, `non_opal_refused_wsj` (code `harvest_opal_only` on `packs/` and on
   `wsj/harvest/`), `off_prefix_refused` (`zzz-not-served/x.json` -> `harvest_prefix_not_served`),
   `s3_calls_on_refusal: 0`, and (PRD v2.8, the research-only arm) `research_only_schwab_refused` and
   `research_only_bd_refused`: the SAME unprofiled standard-tier Opal principal that read `packs/` is refused one `schwab_*`
   tool and `blackdiamond_list_fees` by `data_entitlement.decide()`. No object content is printed.
8. **Standing release clauses:** runbook 7.2 names the new live release; EC2_MANIFEST `deployed_commit` and
   `file_checksums` come from the release blobs. Close the ledger, commit, run AC2, and report once to `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- OG-hv-1's hunks and the one policy only. No other gateway change, no catalog edit, no grant-store record written, no
  object written to any bucket.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform`;
  print an `.env` value, a person's name or email, or harvest object content; override a gate other than the one audited
  lane escape in step 2.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/harvest_read_iam.tf
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-harvest-read-grant.json
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-hv.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` =
`date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after PHASE A, AC2 after PHASE B's second ledger is closed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-hv-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/hv2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)base [0-9a-f]+ is the live ref before this release: yes.*outside OG-hv-1's files 0 \(want 0\); harvest_read\.py byte-equal to HEAD: yes.*grant object prefixes equal SERVED_PREFIXES: 24 of 24, extra 0; list condition prefixes 24 of 24; non-read actions 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-hv-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/hv2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledgers CLOSED 2 of 2; sentinels at HEAD 0.*equal=yes; rb\.AC2 PASS.*simulate packs=allowed wsj_harvest=allowed control_unlisted=implicitDeny.*served fields: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-hv-2" judgment="true"/>
</proof_of_spec>

- `AC1`: the re-cut carries exactly OG-hv-1 on the live ref, and the grant names exactly the 24 prefixes.
- `AC2`: both acts landed and closed; the role reads the listed prefixes and nothing else; the installed tools admit an
  Opal principal and refuse a non-Opal one on `packs/` and `wsj/harvest/`.
- `AC3` (judgment, `3.0.0_SA_CVO~Z`): FWD-21's driven call -- a REAL Opal asset manager, signed in to their own work
  Claude, asks for one covered name and gets its pack and chatter through the gateway. That is the user's (or Andrew's) act,
  owed, never simulated here; record it UNVERIFIABLE-BY-INSTRUMENT naming the CVO and the act owed. An asset manager with
  no work Claude account goes on the site Z open-calls list as Andrew's act.
  **A1 (CTO ruling msg 33823, call `sitez-20261013T215753Z-232a`):** no asset manager is named on record yet.
  - FWD-21's FIRST live read runs on Andrew's own work Claude as a STAND-IN Opal principal. It proves the harvest read
    path: one covered name's pack and chatter.
  - It cannot grade the research-only arm, because Andrew is master_admin and Schwab and Black Diamond are allowed to
    him.
  - The CVO grades AC3 PARTIAL with that arm named, never PASS, until a named asset manager runs the same proof.
  - The negative arms (a non-Opal principal refused; an off-list prefix refused) are AC2's and do not wait.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-hv-2.harvest-read-grant-and-release.proof_of_spec.json`. Validate it after
your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip
the ONE `<status>` tag to `complete` only if AC1 and AC2 PASS. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, R4 (FWD-21, PRD v2.7 @27ba6b6191). Cut only after `prd-signoff.py status NFRA_OPLGTW` reads ADMITTED. Rides behind R1 in
  the gateway queue; OG-hv-1 must be drained before PHASE A (edge hv-1 -> hv-2; edge ap-14 -> hv-2). Its order against OG-cd-1's release is the decomposition's.
- Pre-cut: hv2.AC1 and hv2.AC2 base FAIL as expected (records absent).

- A1 (issuer, 2026-10-13 ~23:0xZ): AC3's text carries the CTO's stand-in ruling (msg 33823). The Andrew-as-stand-in read
  is owed by Andrew; the named asset manager stays open on call 232a. No mechanical criterion moves.
  Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A2 (issuer, 2026-10-14 ~05:0xZ, from row Z-S105 on OG-ap-14): **deploy-source guard.** Before the first deploy
  command, the deploy tree's `git rev-parse HEAD` must equal the signed `release_sha` in full, and its parent must equal
  live `deployed_commit` at the act. Any mismatch is a STOP; print both. If the live base moved since the cut, re-cut,
  and both halves re-sign. Never deploy from a worktree named for an earlier cut.
  Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A3 (issuer, 2026-10-14 ~11:5xZ, relay msg 34020): **call `sitez-20261013T215753Z-232a` is ANSWERED.**
  - Andrew named the asset manager for FWD-21's driven call. The name is in
    `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md`; no address is
    copied here.
  - The call runs later this week, as Andrew's own act.
  - AC3: the stand-in read (A1) comes first. The named asset manager's own driven call is the arm that can lift AC3
    from PARTIAL, including the research-only refusal arm (that person is not master_admin).
  - Still never simulated here. If the census (OG-hv-1) did not see that principal in the identity store, their first
    sign-in creates it; that is not a blocker.
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A4 (issuer, 2026-10-14 ~12:1xZ, Andrew-direct "we need to accelerate this use case and the associated task orders";
  record `deliverables/2.0.0_SA_COO~O/ANDREW_DIRECT_20261014_121xZ_ACCELERATE_FWD21_HARVEST.md`): **FIRST in the gateway
  queue.**
  - PHASE A starts now. Its precondition is met: OG-ap-14's ledger is CLOSED, the live ref is 90967e39ba, and OG-hv-1
    drained @e4096a971f.
  - OG-ap-17 and MX-r-13 follow this release.
  - The three halves were told in advance, so the ask is signed as it lands.
  - Steps, criteria and bounds are unchanged.
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A5 (issuer, 2026-10-14 ~12:3xZ, CTO relay msg 34054 from CVO msg 34051; verified at `harvest_read.py` `_client()` ->
  `internal_role.s3_client()` and `deploy-to-ec2.sh` `INTERNAL_READER_ROLE_ARN=...:role/gateway-global-internal-reader-role`):
  **the grant names the wrong role.** Cut as written, Phase B would pass while every served read is AccessDenied.
  - The policy attaches to `aws_iam_role.int_reader`; step 5 reads and simulates `gateway-global-internal-reader-role`;
    `HV2_IAM_SIM.json` gains `role`.
  - hv2.AC1 now also requires the grant on `int_reader` and not on `gw`; hv2.AC2 requires `role` to equal the internal
    reader. The `<expect>` regexes are unchanged (both appended text sits after the matched fields).
  - The widening to name is the internal reader's S3 read on `opal-data-harvest` (that role is assumed only by the gateway).
  - Gate limb: GATE (viii) on the modified order (placeholders NONE); no other limb fires on a modification.

- A6 (issuer, 2026-10-14 ~13:4xZ, row Z-S108 from `0.7.0_AE_CloudOps~Z`; OBSERVATION / INERT, disarm_owner this seat):
  step 3 named an instrument that does not exist. `.tools/safe-apply.sh:16-17,63` gates `apply` only and refuses other
  subcommands, so a targeted plan runs through `terraform` directly. The step now says so; the apply stays `safe-apply`.
  No criterion moves. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
