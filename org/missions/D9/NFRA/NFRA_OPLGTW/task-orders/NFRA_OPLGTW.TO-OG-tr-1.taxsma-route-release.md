# NFRA_OPLGTW task order -- `OG-tr-1` -- the NARROW gateway release of the Tax SMA workbook route, capability ON (half 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-tr-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the host role's read of gateway/global/taxsma-workbook-token exists (laptop TX-i-3, gateway-taxsma-workbook-bearer-read-policy).
comp-adversary: DECLARED-NOT-APPLICABLE -- the release shape is Andrew's (~17:2xZ, ~17:3xZ) and the CTO's (msgs 27986, 27992).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM, Secrets Manager reads) and the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-tr-1` (decomposition addendum R3-T.4)

Andrew-direct ~17:2xZ: site Z runs the Tax SMA gateway release (the MDPF_TAXSMA exclusion is lifted for this ONE
release); ~17:3xZ: "ON at this deploy". The spec is
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAY_20261001_1733Z_LAPTOP_CRO_103933_TAXSMA_GATEWAY_RELEASE_SPEC.md` -- read
it whole. Your OG-rl-1 / OG-rl-2 records (`ANNOUNCE_OG-rl-1.md`, `ANNOUNCE_OG-rl-2.md`) are the pattern for every step.
STANDING RULE (row Z-S32): nobody sources `/opt/opal-gateway/.env` in a shell; key names only, or
`/proc/<service pid>/environ` for one named key, never echoed.

### PHASE A (pre-GO): no upload, no secret written, read-only SSM only

1. **Live commit** from the manifest at HEAD (expect `0a1d9079c682c640e619612f804257681c5db357`), confirmed by host md5 of
   every file the release ships. A mismatch STOPS.
2. **The identity, confirmed BEFORE anything else (Andrew ~17:3xZ, CTO 27992 (b)).** A read-only SSM read of the host
   token broker's account records (`app/token_broker.py` names the store) printing ONLY each record's oid and whether its
   username is `opalbloomberg@opalinvest.com` (true/false). Exactly ONE record must match; neither or both STOPS with a
   BLOCKING row. Cross-check that oid against the site-Z Part D record
   (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/PART_D_RECORD_20260930.md` maps opalbloomberg@ to
   `WRITE_CAPABLE_PRINCIPALS` 2 of 2; the values file is `%LOCALAPPDATA%/opal/og-principals/part_d_20260930.json`) and
   record MATCH/DIFFER. The identity value is `6810043e-d171-4adc-9975-068b35e179da/<that oid>`.
3. **Release tree** `/c/tmp/og-rel6`, branch `rel-nfra-oplgtw-taxsma-route`, at the live commit: add
   `app/taxsma_workbook.py` and `tests/test_taxsma_workbook.py` from CLOUD HEAD (sha256 `6acc3e8c...` and `810148fe...`),
   and merge ONLY the Tax lines onto the LIVE `app/server.py` (the import and the `Route`) and `app/config.py` (the two
   `TAXSMA_WORKBOOK_*` fields and their comment block). Census against live: exactly these four files plus
   `deploy-to-ec2.sh`. Audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPLGTW~15` for release-branch commits only.
4. **Tests** on the release tree, `AUDIT_PATH` isolated: `tests/test_taxsma_workbook.py` (it needs `moto`; install into a
   local venv if absent and record the version), `tests/test_mail_route.py`, `tests/test_mail_listing.py`,
   `tests/test_entitlement_admin.py::test_ogz2_ac08` (LIVE + OWN = LIVE + 0: the route is not an MCP tool).
5. **The template edit** hand-merged onto the LIVE `deploy-to-ec2.sh`, following the `MS_INGEST_BEARER` block:
   - on the host: `TAXSMA_WORKBOOK_BEARER` from `aws secretsmanager get-secret-value --secret-id
     gateway/global/taxsma-workbook-token`; REFUSE (non-zero, before any `.env` write or restart) when the read fails or
     is empty (capability ON requires it);
   - from the deploying shell: `OG_TAXSMA_WORKBOOK_IDENTITY`, validated as ONE `<tid>/<oid>` pair (the template's
     existing pair regex), REFUSED with no upload when missing or malformed; never committed;
   - two new `.env` lines `TAXSMA_WORKBOOK_BEARER=` and `TAXSMA_WORKBOOK_IDENTITY=`; `%s` and argument counts equal;
     46 -> 48 keys, every existing key and `ENABLED_INTEGRATIONS` unchanged.
6. **Rollback** `/c/tmp/og-rb6` at the live commit, built WITHOUT uploading, equal file by file to the live S3 artifact;
   the re-deploy command with `DEPLOY_BASE_REF` (that template needs nothing from the shell: it reads the rosters and the
   sender table host-side).
7. Write `ANNOUNCE_OG-tr-1.md` (steps 1-6 numbers; the identity step as oid-match booleans and MATCH/DIFFER only; no
   secret, no full oid) with the standing-rule line; commit and report. Do NOT upload.

### PHASE B (GO): only after the issuer says GO (both halves SIGNED; OG-tt-1 complete; the gateway queue told)

8. Re-read the live ref; if it moved, re-cut and re-run 1-7 before any act. BEFORE reads (tool list,
   `ENABLED_INTEGRATIONS`, key names). NEVER-2 ledger `nfra-oplgtw-taxsma-route-release` (legs: upload, install + verify,
   manifest, rollback-proven), entry AND sentinel committed BEFORE the act.
9. Act from `/c/tmp/og-rel6` with `OG_TAXSMA_WORKBOOK_IDENTITY=<the confirmed value, exported via a python eval, never
   printed> DEPLOY_BASE_REF=<live full sha> HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~15` through
   `infra/aws/ec2/safe-ec2-deploy.sh`. Capture the deploy's own result lines literally.
10. VERIFY with a script written at PHASE A, run immediately after the deploy returns (row W15-S18): host `/health` 200;
    shipped md5 = release bytes; tool list unchanged; `.env` keys 46 -> 48 (the other 46 unchanged); `/ms/*`, `/hx/*`
    as before; then `tr.AC1.sh`. Any failure: roll back, re-verify, close ROLLED BACK.
11. Record `EC2_MANIFEST.json` `services.opal-gateway` by hand on the CLOUD base; close every leg with proof; commit.

## 2. BOUNDS

Terraform, IAM, the ALB, the instance and the identity allowlist untouched; `safe-ec2-deploy.sh` READ only; no secret
written; no workbook read (the controlled read is the laptop's TX-r-3). Never push, `git stash`, rebase, `checkout --` or
`clean`; never override a gate; no vendor call. REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-taxsma-route-release.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Release-branch only, never merged to CLOUD by this cell: `deploy-to-ec2.sh` and the release tree's merged `server.py` /
`config.py`. Rows: id `NFRA_OPLGTW-Z-W15-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-tr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/tr.AC1.sh; echo "exit=$?"</invocation><expect>(?s)TAX ARMS 4 of 4.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-tr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/tr.AC2.sh; echo "exit=$?"</invocation><expect>(?s)sentinel at HEAD=no;.*outside the Tax set 0; ms_ingest.py shipped 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the spec's section-4 acceptance on the SERVED gateway, capability ON.
- `AC2`: NEVER-2 closed; the release ships only the Tax files and the template.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-tr-1.taxsma-route-release.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 12 (addendum R3-T.4) with `OG-tt-1`. The never-widen ask names the live content route (capability ON)
  and the identity binding; CTO half at PHASE A (msg 27986), CVO second half as for OG-rl-1/rl-2.
- Pre-cut control: `tr.AC1.sh` reads `TAX ARMS 1 of 4` (module ABSENT, Tax path 302, `.env` 46 keys, no TAXSMA keys).

<status>pending</status>
<status>complete</status>
<round>12</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
