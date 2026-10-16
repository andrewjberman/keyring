# NFRA_OPLGTW task order -- `OG-ap-27` -- APPLY (grant): the internal reader role gets the read of the four prefixes the OG-ap-23 served read found denied (row Z-S164; CTO ruling msg 34853)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-27</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-27</to_id>
<issued_to>0.7.0_AE_CloudOps~ZS</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; the applier still runs `comp-schedule --drift` at the act and records what it scanned.
comp-iam: RUN-BY-ISSUER at the cut (`comp-iam stats` 2026-10-16 ~06:3xZ: 222 IAM roles parsed, 197 services, 1175 operations, 345 permission gaps estate-wide; a DESIRED-plane lens over Terraform that cannot see a live-only policy, so the applier reads the live role in Phase A step 1): TWO new inline policies on `gateway-global-internal-reader-role`, read-only (`s3:GetObject`, prefix-confined `s3:ListBucket`) on four prefixes of two buckets. Nothing is removed and no other role moves.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (msg 34853: "grant the internal reader read-only GetObject plus prefix-conditioned ListBucket on exactly the prefixes those 4 tools read ... Addresses come from registry rows. I sign on receipt"), on the applier's measured evidence (`W` of `0.7.0_AE_CloudOps~Z`: `CODE_SERVED.json`, row Z-S164: four `AccessDenied` as `assumed-role/gateway-global-internal-reader-role`).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-27` (decomposition addendum R3-T.88, workstream RELEASE-GAP-GRANTS, FWD-22)

The release `3d5c9c8bf1` (code, signed by all three halves) was deployed and rolled back under its condition C5 because four of its 27 tools read S3 prefixes that no internal-reader statement covers: `etfs_get_new_securities`, `etfs_get_fund_bloomberg_characteristics`, `etfs_get_fund_snapshot` (bucket `opal-data-etfs`) and `mdpf_get_model_composition` (bucket `opal-data-mdpf`). This cell grants exactly those reads, so the SAME release can be re-deployed.

THE FOUR PREFIXES, as the committed catalog states them (`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`; read it with `git show HEAD:<path>` and derive, never type from this face; if HEAD disagrees with a line below, the HEAD rows win and you say so on the ask):
- `opal-data-etfs` prefix `bbg/` (the Bloomberg silver tables: `bbg/{as_of}/fund_daily.parquet`, `bbg/{as_of}/constituents/derived_*.parquet`; entities `opal_data_etfs_silver_bbg_*`);
- `opal-data-etfs` prefix `snapshots/` (`snapshots/snapshot_{date}.json`; entity `opal_data_etfs_silver_snapshots`);
- `opal-data-etfs` prefix `mdpf/etfs/gold/new_securities/` (`date={D}/new_securities.json`; entity `opal_data_etfs_gold_mdpf_new_securities`);
- `opal-data-mdpf` prefix `mdpf/feeds/model_composition/` (`<firm>/...`; entity `opal_data_mdpf_feeds_model_composition`, firm-scoped).
The CTO's message names "opal-data-etfs/silver/*" for the three etfs tools. That is the table family's label, not the key prefix: the keys sit under `bbg/`, `snapshots/` and `mdpf/etfs/gold/new_securities/`. Do NOT grant `silver/*` (it would cover tables no tool of this release reads); the ask says so in one line.

### PHASE A (files, plan, ask; NO apply IN ANY FORM)

1. **Read the live state first.** `list-role-policies` and `get-role-policy` for every policy on `gateway-global-internal-reader-role` (names and document hashes, so the rollback is exact; the two new names must be absent). Write `W/GAP_BEFORE.json`.
2. **Write the Terraform** `infra/aws/terraform/opal-gateway/gateway_release_gap_read_iam.tf`: TWO `aws_iam_role_policy` resources on `aws_iam_role.int_reader`, one per bucket (`opal-data-etfs`, `opal-data-mdpf`), each with exactly two statements in the shape of `etfs_read_iam.tf` (copy its form): `s3:GetObject` on the prefix object ARNs (`arn:aws:s3:::<bucket>/<prefix>*`), and `s3:ListBucket` on the bucket ARN with an `s3:prefix` `StringLike` condition naming the same prefixes (`<prefix>*`). Policy names are `lib/opal_naming.py name()` output read through `../modules/opal_name` as `etfs_read_iam.tf` does (the commit-time naming gate refuses a typed name; a builder refusal is a missing registry row to add under `infra/logic/registry/`, never a hand-typed workaround). No `*` resource, no bucket-root object ARN, no `s3:Put*`/`s3:Delete*`, no unconditioned `ListBucket`, no firm token in any prefix. Header comment: why (row Z-S164), the four catalog rows each prefix derives from, and what it does NOT do.
3. **The plan**, targeted at those two resources, `-lock=false`, no `-out`, no apply: it must read `2 to add, 0 to change, 0 to destroy`. Save it as `W/GAP_PLAN.txt`. Any other change is a STOP.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-27.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word (CTO, COO, CVO): (1) the `diff` (the one file); (2) the `widening`, stated plainly, per bucket and prefix: the internal reader gains read-only object read and a prefix-confined list; Opal-internal market data for the three etfs prefixes; for `mdpf/feeds/model_composition/` the catalog row reads `firm_scope_rule: firm-scoped` (model holdings forked by firm), the IAM prefix is NOT firm-confined (no firm token may be typed), and the gateway tool `mdpf_get_model_composition` is in `NATIVE_TOOLS` (any Opal principal, one firm per call) in `app/data_entitlement.py`: state that the halves sign knowing both facts; (3) the four `tools` and what each reads; (4) the `order` of acts (one targeted apply; both ends read back from IAM and the simulator; BEFORE the re-deploy of `3d5c9c8bf1`); (5) `both branches` (an in-prefix read serves; an out-of-prefix read stays denied; a non-Opal call is still refused by the gateway before any S3 call); (6) the `rollback` (a targeted destroy of the two policies; the prior state is in `GAP_BEFORE.json`; the release re-deploy has not happened yet at this step); (7) the `triggers`. Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at the `.tf` hash)

5. Ledger `nfra-oplgtw-grants-ap27`, entry AND sentinel first. Apply through `safe-apply`, targeted at the two resources. Read back from IAM: both policies are on `gateway-global-internal-reader-role` and match the file; absent elsewhere; `simulate-principal-policy`, ONE resource per call: `s3:GetObject` allowed on a probe key under each of the four prefixes, `s3:ListBucket` allowed with each prefix as the `s3:prefix` context value, and NOT allowed on an out-of-scope key and prefix of each bucket (negative control, `ap27-negative-control/`); a `*`-principal positive control beside any deny read. Re-plan the target: `No changes`. On a trigger failing, destroy the two policies and file an ARMED row naming `2.0.0_SA_COO~O`. Close the ledger, write `W/GAP_APPLIED.json` = `{"policy_names": ["<name1>", "<name2>"], "prefixes": ["<bucket>/<prefix>", ...], "applied_at": "<iso>"}`, commit, run AC2, report once.

## 2. BOUNDS

- IAM and Terraform of the two named policies only (and a registry row if the naming builder refuses a name). No object read or written; no deploy; no other role or policy touched.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply` (use `safe-apply`); apply in Phase A in ANY form; print an account number or an object's content.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/gateway_release_gap_read_iam.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
infra/logic/registry/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-grants-ap27.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZS/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZS/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free; a correction is a NEW row citing the old id), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-27"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap27.AC1.sh; echo "exit=$?"</invocation><expect>(?s)terraform: policies 2 \(want 2\); both on the internal reader True; actions \['s3:GetObject', 's3:ListBucket'\]; wildcard False \(want False\); bucket-root object arn False \(want False\).*prefixes: four stems in GetObject resources True; in ListBucket s3:prefix values True; list confined True.*plan: 2 to add, 0 to change, 0 to destroy True; ask has the three halves True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-27"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap27.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; policies named 2, held on the internal reader 2; simulate GetObject allowed 4 of 4, ListBucket allowed 4 of 4; negative control GetObject not allowed 2 of 2, ListBucket not allowed 2 of 2.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the one `.tf` file puts two policies on the internal reader role, read-only and prefix-confined on the four prefixes, and the plan is two additions only. `AC2`: both policies are live on the internal reader role, the simulator allows the four prefixes and refuses an out-of-scope key and prefix of each bucket, and the ledger is closed.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-27.release-gap-grants-to-internal-reader.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream RELEASE-GAP-GRANTS (decomposition addendum R3-T.88). The gap is mine: the OG-ap-23 preflight declared `comp-iam` not applicable ("no IAM change") and my condition C5 assumed the four G2-remainder tools read prefixes the internal reader already held; the applier's served read measured otherwise. C5 did its job (rollback, nothing served wrongly).
- The CTO's ruling (msg 34853): ONE ask, applier `~ZS`, redeploy `3d5c9c8bf1` unchanged after the apply, the code halves stand; fallback at 18:00Z is a 23-tool re-cut.
- The open classification question (raised to the CTO in a separate message, not blocking Phase A): `mdpf_get_model_composition` sits in `NATIVE_TOOLS` while its catalog row is firm-scoped; precedent is OG-ap-20's partner-folder tools (Opal-principal-only, one firm per call). A change of class would change the release bytes and re-open the code halves.
- Phase A GO is the issuer's message. OG-ap-23's re-GO waits on `ap27.AC2` PASS.
- Pre-cut: ap27.AC1 and ap27.AC2 base FAIL as expected (tf, plan, ask and GAP_APPLIED.json absent).

<status>complete</status>
<round>37</round>
<workstream>RELEASE-GAP-GRANTS</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
</output>
