# NFRA_OPLGTW task order -- `OG-rl-15` -- gateway release r29: the mail domain route, the asker tool SAFE, the refresh send gate, the 13-month grant window, and the 13-month grants

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-15</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rl-15</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~43</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot release; no cron, alarm, monitor or cadence. The R55/R49 window binds: no deploy inside the 12 hours before the 07:00 America/New_York send (23:00Z to 11:00Z).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the grant-writer rebuild (if Phase A finds it is needed) is a Lambda code change, named in the ask as its own leg.
comp-adversary: DECLARED-NOT-APPLICABLE -- the cells are rulings R50, R54, R55 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round31.md @e43ee663be), PRD v1.9 C7 and v2.0 item 4, and the CTO ruling msg 32087 (r29 also carries OG-cm-1 and the 13-month grants).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM) and the public gateway URL. NO package, script or program is fetched from the internet by this box.
</preflight>

## 1. THE CELL -- `OG-rl-15` (decomposition addendum R3-T.30, item 6)

FOLLOW `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md` IN FULL, with ONE change of
actor: **site Z's deploys are applied by `0.7.0_AE_CloudOps~Z`** (Andrew-direct 2026-10-08 ~22:0xZ, relay msg 32057).
So Phase A and the post-deploy reads are yours; Phase B's deploy (form steps 9-11) is the applier's, under an apply
order the issuer cuts after the halves. Reuse the r28 tooling in
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/` (`r28_*`); copy to `r29_` names in `W`.
First bring your branch level with box/sitez by a plain merge of the commit the issuer names at the hand-off (no rebase).

- **Live:** `aa75078e1b72a28219e6148d3ec8e9bf705ea111` (r28). Re-read it by host md5 first. Another sha: STOP, report.
- **Ledger:** `nfra-oplgtw-gateway-release-r29` (opened and closed by the applier in Phase B).
- **Release branch** `rel-nfra-oplgtw-r29`, a NEW worktree `C:/tmp/og-rel29` at the live sha. **Rollback tree:** a NEW
  `C:/tmp/og-rb29` at the live sha, proven against the live S3 artifact.
- **The release set:** every gateway difference between live and box/sitez at the hand-off, except the CLOUD-only
  `runbooks/SCHWAB_PILOT_RUNBOOK.md`. Expected, by cell:
  - OG-md-1: `app/mail_route.py`, `app/config.py`, `deploy-to-ec2.sh`, `deploy/mail_sender_domain_table.txt` (ships
    EMPTY), `tests/test_mail_route_domain.py` and its edits to the two v1.4 mail test files;
  - OG-sf-1: `app/destructive_ops.py`, `tests/test_asker_safe_tool.py`;
  - OG-rf-1: `app/server.py`, `app/oauth_as.py`, `tests/test_oauth_send_budget.py`;
  - OG-cm-1: `app/integrations/schwab/catalog.py`, `app/integrations/schwab/integration.py`, `app/data_entitlement.py`,
    `app/admin_grants.py`, `ops/schwab_entitlement_admin.py`, `ops/schwab_status.py`, `deploy/NFRA_OPLGTW_CONTRACT.json`
    (contract 1.4), `tests/test_grant_calendar_months.py`.
  - State for each non-test file whether it reaches the host, from the host md5 list, not from its path.
  - Any OTHER gateway difference: STOP before the release commit, report its files and commits. One named exception
    may arrive by the issuer's continuation: five rows in `identity_tool_allowlist.txt` for the Bloomberg concierge, ONLY
    with Andrew's verbatim record named (overlay header, PRD 4.3). Without that record, no overlay row ships.
  - If the diff touches `requirements.txt` or `bun.lock`: STOP and report.
- **THE FLOOR TESTS MOVE WITH THE RELEASE (R55).** `tests/test_schwab_host_inputs.py` counts `.env` keys 51 -> 52 and
  host inputs 18 -> 19 for the one key OG-md-1 adds, `MAIL_SENDER_DOMAIN_TABLE`. Update ONLY those two constants in
  the release's own diff and name each line. Its third failure,
  `test_grant_writer_stages_the_contract_only_from_the_standard`, is row Z-W42-S1 (below), not a constant.
- **ROW Z-W42-S1 (ARMED, the grant writer).** `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/` ships its own
  copy of `data_entitlement.py` and the contract, pinned to the manifest's `deployed_commit`. Until it is rebuilt from
  r29's commit it refuses every `calendar_months` grant. In Phase A: determine whether the 13-month grant write (Phase C)
  goes through that Lambda or through `ops/schwab_entitlement_admin.py` against the state store, and whether the
  rebuild is needed for this release's grants. If needed, the rebuild is a separate leg in the ask, applied by
  `0.7.0_AE_CloudOps~Z` after the gateway deploy (the build input pinned to the new manifest commit, never HEAD).
- **THE DOMAIN TABLE (PRD v1.9 C7).** It ships EMPTY from OG-md-1. In the ANNOUNCE, propose its entries: the domains
  of the five parties Andrew named and no other row's, LOOKED UP in `infra/logic/registry/scopes.json`
  (`tenant.email_domain`) and `infra/logic/registry/mail_parties.json`, each entry beside its party; the demo tenant's
  domain is not admitted. The halves sign the entries; Phase B ships exactly those (the table is a deploy-side file).
- **AMENDMENT A1 (issuer, 2026-10-09 ~01:3xZ; `1.0.0_SA_CTO~O` msg 32212, relaying the laptop's COMM_ASSIST ask).**
  (a) The domain table: fill it per PRD v1.9 (PRD lines 685-691), the five parties of Andrew's 2026-10-07 ~18:3xZ
  record item 6; a party with no domain in `scopes.json` / `mail_parties.json` is LEFT OUT and named as left out (the
  laptop reads 4 of 5). (b) ONE new `MAIL_BEARER` value for the laptop Teams agent, issued into the gateway's secret
  store. In Phase A, read how the mail route's bearer(s) reach the host (the secret `gateway/mail/bearer`, the deploy
  script's host-side read, and whether more than one labelled value is supported, as `TEAMS_BEARER_LABELS` is) and
  design the issuance as its OWN LEG of the ask: the secret's name (by the builder's grammar), the label, how the host
  reads it at deploy, the rollback (the prior secret version), and the hand-over BY SECRET REFERENCE ONLY (the name
  and version id; never the value, in no file, message, log or commit). The secret write and the deploy that reads it
  are the applier's, never yours. If the route admits only one bearer value, say so: then the leg is a rotation, and the
  ask names every current holder that must receive the new reference.
- **AMENDMENT A2 (issuer, 2026-10-09 ~02:0xZ; `1.0.0_SA_CTO~O` msg 32258).** Andrew's word for the five Bloomberg-concierge
  allowlist rows, verbatim in `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261009_015xZ_OPAL_STAFF_MAY_READ_BLACK_DIAMOND_THROUGH_GATEWAY.md`
  @0035550443: "any account at ... any vendor any everything", "do not hold up progress". The release set GAINS five rows in
  `infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt` for `opalbloomberg@opalinvest.com`: `opal_discover`,
  `opal_describe`, `blackdiamond_list_fees`, `find_sharepoint_site`, `search_files`, unqualified, under one comment block
  citing that record by path@commit (the file's own rule: every row carries its authorization). Add them in your
  release commit; they are the ONE named exception to "any OTHER gateway difference: STOP". In Phase A's REHEARSAL and
  Phase C's read, `identity_scope.check` for that identity on each of the five reads allowed: AC2's body gains
  `bloomberg_tools_allowed` (the count of the five that read allowed through the INSTALLED code, 5 expected).
- **Row Z-S67 and R49.** Name the re-authentication this release causes per R49, and read 0 revoked refresh families
  for the concierge since the deploy (AC2's body). Z-S67 disarms on that read.
- **Timing (R55, R49).** No deploy between 23:00Z and 11:00Z. Phase A may run now.

### PHASE A (now) -- form steps 1-8, read-only on the host

Run the form's Phase A steps 1-8 (7a: no tool and no route is added or removed; the tool count stays 66). BEFORE and
REHEARSAL on the host, strictly one run at a time, in scratch directories, never writing a grant or a lake object:
- BEFORE (installed r28): `opal_asker_query` classifies non-SAFE; `oauth_as` has no `SendGate`; a `calendar_months`
  grant is refused; the contract reads 1.3; the domain table is absent.
- REHEARSAL (the staged release bytes): the asker tool SAFE with no write class and 0 registered tools unclassified;
  `SendGate` present; `calendar_months` 1-13 accepted and 14 refused; contract 1.4; the domain table loads with the
  proposed entries; tools 66; the scoped concierge's consent 9.
Write `W/ANNOUNCE_OG-rl-15.md` (the form's step 8) as the never-widen ask for THREE halves (CTO, COO, CVO) covering:
the deploy; the domain entries; the grant-writer leg if needed; and the Phase C grant write, whose blast radius is
EXACTLY the reach field of Andrew's and Alyssa's principals' grants set to 13 calendar months, no other field or
principal, rollback = the prior reach per key (CTO ruling msg 32087). Commit and REPORT. Then STOP.

### PHASE C (after the applier's deploy report, named by the issuer's continuation)

1. The post-deploy read through the INSTALLED code: `W/RL15_READ.json` as `{"body": {...}, "ssm_command_id",
   "instance_id"}`, the host printing `RL15_DIGEST <sha256>` of `json.dumps(body, sort_keys=True)`. Body fields,
   exactly: `served_release`, `installed_code: true`, `asker_query_class`, `asker_query_write_class`,
   `unclassified_registered_tools`, `send_gate_in_oauth_as`, `calendar_months_max`, `contract_version`,
   `mail_domain_entries`, `mail_domain_entries_signed`, `concierge_families_revoked_since_deploy`, `bloomberg_tools_allowed`,
   `grants_written: 0`.
   Re-read the standing floor into `W/RL15_FLOOR.json` per the form.
2. The grant write, under the signed halves only: Andrew's and Alyssa's principals' grants gain `calendar_months: 13`;
   record each key's prior reach first. Then `W/RL15_GRANTS.json`, the host printing `RL15G_DIGEST <sha256>`, body
   fields exactly: `served_release`, `principals_changed`, `fields_changed`, `calendar_months_after` (list),
   `other_principals_changed`, `prior_reach_recorded`, `thirteen_month_read_available_dates_min` (the smallest count of
   available dates a 13-month availability read returns for either principal on either master). Never print a tid, oid
   or email; principals are named by role (`andrew`, `alyssa`).
3. Phase D (form step 13): drain-back of the release branch's gateway files to box/sitez in your own worktree.
4. Run the criteria one after the other.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~43/`.

## 2. BOUNDS

- You deploy nothing, apply nothing, upload nothing: Phase B is the applier's.
- No grant written before Phase C and both its halves; only the two principals' reach field; no other state-store
  write. No `.env`, secret, Terraform or IAM write.
- Never run `opal_data_refresh_upload` with `confirm=True`, never POST `/trigger`, no `/login` for the concierge, never
  read the gateway's sign-in cache.
- Never print or commit a tid, oid, client account id, credential, token or execution id; never an email address.
- Host runs one at a time. Fetch nothing from the internet. Never: push, `git stash`, rebase, `checkout --`, `clean`,
  `FORCE_HEADMOVE`; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/
org/standards/NFRA_OPLGTW_CONTRACT.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~43/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W43-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root, ONE AFTER THE OTHER, after the drain-back and the applier's ledger close are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-15"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/rl15.AC1.sh; echo "exit=$?"</invocation><expect>(?s)descends from aa75078e1b=yes; host shipped files equal the release bytes: (\d+) of \1.*sentinel at HEAD=no; gateway files differing live\.\.CLOUD after drain-back \(CLOUD-only runbook excluded\) 0.*floor: rl4\.AC1 yes; ht\.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-15"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/rl15.AC2.sh; echo "exit=$?"</invocation><expect>(?s)r29 served content: fields=yes ssm=Success digest=yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-rl-15"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/rl15.AC3.sh; echo "exit=$?"</invocation><expect>(?s)13-month grants: fields=yes ssm=Success digest=yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the release is live, the ledger closed, the branch drained back, the floor holds at 52 keys.
- `AC2`: the served gateway carries all four cells' behaviour, and no concierge family was revoked by the deploy.
- `AC3`: exactly the two ruled grants reach 13 months, and a 13-month read answers.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rl-15.gateway-release-r29.proof_of_spec.json` and validate it with
`python .tools/proof-of-spec-check.py <instance>`. Flip the ONE `<status>` tag to `complete` only if all three PASS.
Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32 (R3-T.30), item 6, cut 2026-10-09 ~01:2xZ after its four build cells drained (md-1 @a2c6b9cc65, sf-1
  @773b8e56af, rf-1 @3637777b86, cm-1 @50172c7e1a). The CTO's msg 32184 records R55's sign-in precondition MET
  (Andrew ~00:4xZ, record @6938d82aad). Scope per CTO ruling msg 32087 (adds OG-cm-1 and the 13-month grants).
- The deploy actor changed since r28: Phase B goes to `0.7.0_AE_CloudOps~Z` (msg 32057). The issuer cuts its apply
  order after the three halves.
- Rows carried: Z-W42-S1 (grant writer, ARMED), Z-W42-S2 (13-month I/O cost, ARMED: the AC3 read is its first live
  measurement), Z-S67 (disarms on AC2's revoked-families read), NFRA_OPALAI-Z-S62 (disarms on AC2's asker class),
  Z-W35-S1 (disarms with R50 live).
- A1 (2026-10-09, CTO msg 32212): the domain table per v1.9 (a party with no domain left out) and one MAIL_BEARER
  value for the laptop Teams agent as its own leg (applier writes the secret; hand-over by reference). Graded by no gate
  limb as a modification (placeholders NONE).
- A2 (2026-10-09, CTO msg 32258, Andrew @0035550443): the five Bloomberg allowlist rows ride r29; AC2's attest rule gains
  `bloomberg_tools_allowed == 5` (rl15_attest.py, same commit). Graded by no gate limb as a modification.
- Pre-cut: rl15.AC1 base FAIL as expected (deployed = live r28, floor at 52 keys reads no); positive control: the same
  floor scripts against live values read arms 1, 2, 4 OK and arm 3 (host contract vs HEAD) differing only because HEAD
  carries OG-cm-1's contract 1.4; ht.AC2 at 51 PASS 4 of 4. rl15.AC2, rl15.AC3 base FAIL as expected (records absent).

<status>pending</status>
<round>32</round>
<workstream>RELEASE-R29</workstream>
<slot>~43</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
