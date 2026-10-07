# NFRA_OPLGTW task order -- `OG-rl-13` -- the r27 release on live r26 (feddb37244): the rivalfunds audit args (OG-au-2) and the status tool's date key (OG-sd-1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-13</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~28</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- both cells are the CTO's round-24 analysis (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round24.md @0e813364da, section 3).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM) and the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-rl-13` (decomposition addendum R3-T.22)

FOLLOW `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md` IN FULL: Phase A steps 1-8
(7a does not apply: no tool and no route is added or removed), Phase B 9-12, Phase D 13. Reuse the `r26_*` tooling in
`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/`; copy to `r27_` names. First bring your
branch level with CLOUD by a plain merge of the CLOUD commit the issuer names at the hand-off (no rebase).

- **Live:** `feddb372443adbcf139febab35b69f109e49b664` (r26). Re-read it by host md5 first. If the manifest names
  another sha, STOP and report.
- **Ledger:** `nfra-oplgtw-gateway-release-r27`.
- **Release branch** `rel-nfra-oplgtw-r27`, a NEW worktree `/c/tmp/og-rel22` at the live sha. **Rollback tree:** a NEW
  `/c/tmp/og-rb21` at the live sha, proven against the live S3 artifact.
- **The release set:** every gateway difference between live and CLOUD at the hand-off, except the CLOUD-only
  `runbooks/SCHWAB_PILOT_RUNBOOK.md`. Expected, 5 files:
  - `app/audit.py` (ships): ONE `_ARGS_ALLOWLIST` entry, `rivalfunds_view: day, route, fund` (OG-au-2);
  - `app/rivalfunds_view.py` (ships): every rivalfunds audit call passes a `route`; each 200 answer passes its size;
  - `app/integrations/opal_portal/integration.py` (ships): `_manifest_date` also reads `generated_at`, last (OG-sd-1);
  - `tests/test_audit_rivalfunds_args.py` and `tests/test_opal_portal_status_displayed_date.py` (source only).
  - If CLOUD carries any OTHER gateway difference, STOP before the release commit and report its files and commits.
- **Served output moves two ways, both ADDITIVE to a record or an answer.** The ANNOUNCE names them:
  - the gateway's own audit record for the four rivalfunds routes gains `day`, `route`, `fund` and `bytes`. No
    response, status code, header, key or cache behaviour of any rivalfunds route changes;
  - `opal_data_refresh_status` returns the served manifest's `generated_at` in `displayed_date`, where it returned
    null. Nothing else in the tool's answer changes.
  - Rollback per key: redeploying live `feddb37244` restores both.

**BEFORE and REHEARSAL (form step 5), host runs strictly one at a time, each in its own scratch directory.** Use a
scratch audit sink (`AUDIT_PATH` in the scratch directory), never the installed audit file.
- BEFORE, on the installed code: a signed-in GET of the newest rivalfunds day page writes a record whose args read
  `_omitted`; the status tool on the known 2026-10-07 ~01:26Z execution answers with `displayed_date` null.
- REHEARSAL, on the staged release bytes with the installed tree untouched: the same page GET writes a record whose
  kept args are exactly `day` and `route` and whose `bytes` equals the body served; a chart request on a day with no
  chart keeps `day`, `fund`, `route`; `verdict` and `days` are absent; the page's status, size and digest equal
  BEFORE; the status tool answers with `displayed_date` equal to the manifest's `generated_at`; tools 66; the scoped
  concierge's consent 9.
- **THE WRAPPER EXERCISE (row Z-W28-S13).** In the REHEARSAL and again post-deploy, call the status tool ONCE through
  the dispatch wrapper the MCP surface uses (allowlist check, tier gate, audit), with the scoped concierge as the
  principal, in-process on the host. No `/login`, no token acquired for that identity, no Graph call. Record whether
  the wrapper admitted it and what it returned. If the tier gate refuses the concierge, that is a FINDING: record it,
  file a row, and do not change the gate.
- Never print an email address: say "the scoped concierge". Never print an execution id.

**The post-deploy read, IMMEDIATELY after the verify script, through the INSTALLED code.** Write `W/RL13_READ.json` as
`{"body": {...}, "ssm_command_id", "instance_id"}`. The host prints `RL13_DIGEST <sha256>` of
`json.dumps(body, sort_keys=True)`. Body fields, exactly: `served_release`, `installed_code: true`, `tools`,
`scoped_scope_count`, `wrapper_status_tool` (`"OK"` or the refusal's name), `displayed_date`,
`manifest_generated_at`, `audit_keys_page` (sorted list), `audit_keys_chart_404` (sorted list), `audit_bytes_page`,
`page_bytes_served`, `audit_other_args_kept` (a count), `grants_written: 0`.
Also re-read the standing floor into `W/RL13_FLOOR.json`: the portal login OK, the real holder on both paths, the two
refused ids (`/` and `.`) making 0 requests, and the four route arms of r26 (`chart_404`, `chart_400`,
`day_page_unchanged`, `audit_page_unchanged`).
- **Rollback triggers:** any rivalfunds route changing status, size or digest; an arg other than `day`, `route`,
  `fund` kept in a rivalfunds record; the status tool failing on a well-formed id; a refused id making a request; the
  tool count off 66; the consent count off 9; a floor read off its bar.
- `displayed_date` still null after the deploy is NOT a rollback trigger (the answer is no worse than live); it fails
  `AC2` and is reported.

**THE MANIFEST'S `release_note` (row Z-W28-S19; AMENDED A1, the CTO's ruling in `ledger/ROUND_ANALYSIS.round26.md`
@c474e2d3f3).** When you record the manifest by hand, `release_note` holds THIS release's note ONLY. The chain of
earlier notes moves, whole and unedited, into the r27 ledger entry under a heading `RELEASE NOTE CHAIN (moved from
EC2_MANIFEST.json at r27)`, and the manifest's note ends with one sentence naming that entry file. Do not trim the
chain and do not touch `.tools/naming-gate.py`.

**AMENDED A2 (rows Z-W28-S21 and Z-W28-S20).**
- **The page reads are taken in the deploy window.** In Phase B, read each rivalfunds page's status, size, digest AND
  its S3 object's `LastModified` immediately BEFORE the deploy and again immediately AFTER it. A difference in size or
  digest is a rollback trigger ONLY if `LastModified` did not move between the two reads. If it moved, the page was
  republished: record both reads, say so, and re-take the pair once.
- **The principal for the wrapper exercise.** Phase A read the concierge's principal key from the gateway's encrypted
  sign-in cache on the host, decrypted in memory (row Z-W28-S20). Phase B repeats that read ONLY if the issuer's GO
  says the CTO half allows it. If the GO says it does not, skip the wrapper arm and report; the issuer amends `AC2`
  before the GO in that case. Never read, print, save or use a token from that cache.

**AMENDED A3 (the CTO half on r27, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_NFRA_OPLGTW_OG-rl-13_GATEWAY_R27_20261007.md`
@04fe936b66). It REPLACES A2's second bullet.**
- **The gateway's encrypted sign-in cache is NEVER opened again.** Do not read, decrypt or list it, for any purpose.
  Remove that method from the r27 host programs before any Phase B run.
- **The principal for the wrapper exercise comes from an OFF-REPO file the issuer wrote:**
  `%LOCALAPPDATA%/opal/og-salt/r27/concierge_principal.json`, two fields, `tid` and `oid`. Pass them only inside the
  SSM parameters, as the runner already does for `ga1/holder_pks.json`. Never print, save or commit them; the
  runner's redaction covers them. If the file is absent or the wrapper refuses that principal, STOP before the
  deploy and report.
- **One read added: the first audit-LAKE record after the deploy.** After the post-deploy read, list the gateway's raw
  audit lake prefix (the one runbook section 5 names) for objects written after the deploy time and read the first
  `rivalfunds_view` record, if one exists. Record in `W/RL13_FLOOR.json` as `lake_record`: its kept arg NAMES, whether
  `bytes` is present, and its object's write time; or the string `none yet`. Write nothing to the lake and make no
  request to produce one. `none yet` is not a rollback trigger; a lake record keeping an arg other than `day`, `route`,
  `fund` IS.

**THE TIMING RULE.** This release touches the send path's file. Its Phase B closes by 09:30Z, or it starts only after
that day's Bloomberg send is confirmed served. The issuer states which at the GO.

**ONE STOP for the halves.** Run Phase A, write `W/ANNOUNCE_OG-rl-13.md`, commit and report. Phase B starts on the
issuer's GO, with CTO + COO + CVO halves SIGNED on the release sha.

## 2. BOUNDS

- No grant or state-store write. No `.env`, secret, Terraform or IAM write. No S3 object written.
- Never run `opal_data_refresh_upload` with `confirm=True`, and never POST `/trigger`.
- No `/login` for the concierge in this order.
- Never print or commit a tid, oid, account id, credential, token or execution id; never print an email address to a
  log or a record. Redact a bucket name that embeds the account id (row Z-W28-S18).
- Host runs one at a time: never start a second SSM run before the first returns.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; call a vendor; run bun. R13 (a) applies on the release
  branch only.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r27.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/LINEAGE_R18.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`infra/aws/ec2/opal-gateway/` is written ONLY by the Phase D drain-back merge of the release branch, never edited.

Rows: id `NFRA_OPLGTW-Z-W28-S<k>` (next unused; S19 is the last used), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root, ONE AFTER THE OTHER, after the drain-back and ledger close are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-13"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r27/checks/rl13.AC1.sh; echo "exit=$?"</invocation><expect>(?s)descends from feddb37244=yes; host shipped files equal the release bytes: (\d+) of \1.*sentinel at HEAD=no; gateway files differing live\.\.CLOUD after drain-back \(CLOUD-only runbook excluded\) 0.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-13"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r27/checks/rl13.AC2.sh; echo "exit=$?"</invocation><expect>(?s)status date and audit args on the served release: fields=yes ssm=Success digest=yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the release is live, the ledger is closed, CLOUD equals live, and the floor holds.
- `AC2`: the served gateway returns the manifest's date and records which rivalfunds page was served.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rl-13.gateway-release-r27.proof_of_spec.json` and validate it with
`python .tools/proof-of-spec-check.py <instance>`. Flip the ONE `<status>` tag to `complete` only if both PASS. Report
once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 27 (R3-T.22), cut when `OG-rl-12` went terminal (r26 `feddb37244` live 2026-10-07T14:03:49Z). It ships the two
  round-26 cells, both complete and on CLOUD: OG-au-2 (content landed in `9f146f853a`, row Z-S66) and OG-sd-1
  (drained @757546aaab). Halves: CTO + COO + CVO.
- `rl13.AC1` is `rl12.AC1` with the slug and the live sha moved. `rl13.AC2` reads `RL13_READ.json` through
  `rl13_attest.py`, the r26 instrument with one new field rule.
- Rows this order answers: Z-S64 and Z-W28-S13 (shipped), Z-W28-S19 (the trim, in the worker face).
- OWED BY THE ISSUER, carried from the CTO half on r26 (C1): at the first real send after r26, one read of whether
  each of the two drive items carried a readable hash.
- AMENDMENT 1 (15:3xZ, issuer, during Phase A and before any GO): the manifest note holds the current release only and
  the chain moves to the ledger entry, as `ROUND_ANALYSIS.round26.md` @c474e2d3f3 rules for row Z-W28-S19. It replaces
  the trim. No criterion changed. Gate: LIMB 6 does not grade a modification; GATE (viii) reads placeholders NONE.
- AMENDMENT 2 (16:2xZ, issuer, after Phase A and before any GO): the page BEFORE and AFTER reads move into the deploy
  window with the object's `LastModified` as the discriminator (row Z-W28-S21, ARMED: disarmed by this for r27); the
  wrapper exercise's principal source is conditioned on the CTO half (row Z-W28-S20, never-widen ask section 4 (a)).
  No criterion changed. Gate: LIMB 6 does not grade a modification; GATE (viii) reads placeholders NONE.
- AMENDMENT 3 (16:4xZ, issuer, before any GO): the CTO half's ruling on never-widen ask section 4 (a). The sign-in
  cache is not opened again; the concierge's tid and oid come from `gateway-access-state-table`, read by the issuer
  with its own AWS identity (2 active refresh-family records name the identity, 1 distinct pair) and written to the
  off-repo file. The CTO half's branch (a) holds, so `rl13.AC2` stands unamended. One read added: the first audit-lake
  record. No criterion changed. Gate: LIMB 6 does not grade a modification; GATE (viii) reads placeholders NONE.
- Pre-cut 15:0xZ: see the issuance commit.

<status>pending</status>
<round>27</round>
<slot>~28</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
