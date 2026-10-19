# NFRA_MCPORTAL task order -- `MP-z-6` -- WORKSTREAM GW ROUND 1: the FWD-20 close run -- Andrew reads the gateway breakdown

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-z-6</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-z-6</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~16</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time close run.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only: the deployed code from the release record, the grant store through the existing operator read path, the gateway log through SSM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the two equality reads are made against sources other than the page.
EGRESS CLASS, declared: AWS reads (S3 artifact get, DynamoDB GetItem/Query, SSM send-command for journalctl); no write.
</preflight>

## 1. THE CELL -- `MP-z-6` (workstream GW round 1, decomposition sections GW.1 and GW.6, G-SEE3)

Your worktree is `C:/tmp/mp-gw-16` (branch `wk-NFRA_MCPORTAL-gw-16`). Work and commit only there.

FWD-20 is DONE WHEN Andrew reads the gateway breakdown page, one channel's tool list is checked against the deployed
gateway's code, and one person's entitlements against the grant store (PRD v0.7). The release (MP-z-5) is live. The
ISSUER LINE at the end of your spawn prompt names the window in which Andrew opened `https://mcp.opalinvest.dev/gateway`
and then `https://mcp.opalinvest.dev/control-plane` by direct load, and quotes his words on what he read.

1. **The window.** Take `t0` and `t1` (ISO Z) from the issuer line as given.
2. **One channel against the deployed code.** Pick the channel with the most tools that is NOT `m365`. Read its tool
   list off the page's data: the live response is not readable by you (owner-gated), so read it from the served module
   instead: over SSM, run the deployed `app.admin_gateway_breakdown._compute()` from the host's venv (the way
   `deliverables/2.0.0_SA_COO~MP/fwd20/checks/_z5_probe.py` does, INCLUDING its first line `import app.server`: the
   served app registers its enabled integrations at that import, and without it `_compute()` sees 1 channel, not the 8
   the live process serves -- row Z-S48) and print that channel's tool names -> `page_tools`.
   Then, independently, read the DEPLOYED CODE: download the served artifact the manifest's `deployed_commit` names
   (`s3://<artifact bucket>/opal-gateway-latest.tar.gz`, git-ref metadata equal to `deployed_commit`), extract it to a
   scratch directory, and list the tools that integration's module registers (its `IntegrationSpec.tools` and the names
   its `register()` passes) -> `code_tools`.
3. **One person against the grant store.** Take the one real principal with a `principal_profile` (the page lists it
   with `how` "data grant revision <n>"). Read its active grant from the store with the existing operator read
   (`infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`, its read/show subcommand, run under the operator role
   as its header describes), and from that grant's `operations` list the data-grant tools it admits, using the
operation each tool needs in `app/data_entitlement.py` `SCHWAB_TOOLS` -> `store_tools`.
   Read the same principal's tools off the served `_compute()` output (all channels) -> `page_holder_tools`, restricted
   to the data-grant family (`schwab_*`, `blackdiamond_list_fees`).
4. **Write the run file** `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~16/z6_run.json`:
   `{"t0","t1","channel","code_tools","page_tools","principal","store_tools","page_holder_tools"}`, where `principal` is
   the display email or `<tid>/<oid>` exactly as the page shows it. Commit it, then run AC1.
5. Put Andrew's words, as the issuer line quotes them, VERBATIM into `deliverables/0.9.0_WK_NFRA_MCPORTAL~16/z6_andrew_read.md`
   with the window. That file is what the judgment criterion is graded on. Do not paraphrase and do not add a verdict.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No gateway file, no store write, no deploy.
2. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~16/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/EC2_MANIFEST.json`, `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`,
`infra/aws/ec2/opal-gateway/app/integrations/`, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W16-S<k>` (the next free k for W16). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-z-6"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z6.AC1.sh; echo "exit=$?"</invocation><expect>breakdown 200s>=1; direct /control-plane 200s>=1; channel tools code==page: yes; principal tools store==page: yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-z-6" judgment="true"/>
</proof_of_spec>

AC2 (JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on `z6_andrew_read.md` and the run file, never by you): Andrew's own
reading of the page shows he got the full breakdown he asked for -- every vendor or channel, the tools and indexes on
each, and the current state of entitlements -- which is also his stated condition for closing NFRA_OPLGTW. In the
instance, record AC2 under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~Z`.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~16/NFRA_MCPORTAL.TO-MP-z-6.fwd20-close-run.proof_of_spec.json`.
Report once, with: the AC1 output; the channel picked and both tool lists; the principal and both tool lists; the commit
hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut STAGED at the GW issuance (decomposition v7) from PRD v0.7 FWD-20 DONE WHEN. Gate G-SEE3: MP-z-5
drained, then the issuer cards Andrew ONCE to open `/gateway` and `/control-plane` by direct load; his words and the
window go to the worker in the spawn prompt's issuer line. Check dry-run at base 8abe56f2cd: AC1 FAIL (no run file).

**AMENDMENT (issuer 2.0.0_SA_COO~MP, 2026-10-13 ~22:2xZ):** step 2 now names the `import app.server` line (row Z-S48, the same probe defect MP-z-5 A3 fixed). Before this, the order did not carry it. No criterion changes.

**SPAWNED (issuer 2.0.0_SA_COO~MP, 2026-10-19 ~17:3xZ):** G-SEE3 is met by Andrew's live look at his own terminal on 2026-10-16 ~18:40-18:55Z (record org/tier1_exec/2.0.0_SA_COO~MP/deliverables/ANDREW_DIRECT_20261016_185xZ_CLOSE_21C5_21D9_44EB_GATEWAY_READS_WELL.md). The exact minute was not recorded, so the window handed to the worker is the superset t0=2026-10-16T18:30:00Z, t1=2026-10-16T19:05:00Z; AC1 grades 200s inside it. The access log is 3 days old: a FAIL for log retention is a finding, not a defect of the criterion. Check dry-run at base 2fce7de6ef: AC1 FAIL (no run file), as expected. Spawned worker 0.9.0_WK_NFRA_MCPORTAL~16, haiku/high (MODEL_POLICY MP-20261010).

<status>pending</status>
<round>1</round>
<workstream>GW</workstream>
<slot>~16</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
