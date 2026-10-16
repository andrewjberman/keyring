# NFRA_OPLGTW task order -- `OG-mg-1` -- APPLY: the r30 grant writes -- Andrew's v2.2-width profile with 13 months, and the Bloomberg principal as its exact mirror

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-mg-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-mg-1</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two operator grant writes and reads; no cron, alarm, monitor or cadence. Phase B runs only after OG-ap-14's ledger nfra-oplgtw-gateway-release-r30 is CLOSED (the writes are inert before pf-1 is served, and the positive arm reads after both).
comp-iam: RUN-BY-ISSUER at the cut, on every API call the act makes -- sts:AssumeRole into opal-gateway-access-admin (the role OG-ga-1 used, @ the R22 round); under it dynamodb:GetItem/Query/Scan (strong reads) and dynamodb:TransactWriteItems (access_state.operator_transact, the one transaction that writes the profile, the grant revision and the operator_audit row); secretsmanager:GetSecretValue on gateway/principals/rosters for the two principals' tid/oid (read host-side or under the operator role; values held off-repo only). Phase A RUNS each of these as a dry call (simulate-principal-policy on the role) and records allowed/implicitDeny per action before any write; an implicitDeny is a STOP and a BLOCKING row, never a widening by this seat.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~O's ruling msg 32383 ("Andrew gets a v2.2-width profile with 13 months, and the Bloomberg concierge mirrors it in r30"), decomposition R3-T.31 ("r30 carries OG-pf-1 and OG-tg-1 plus the two grant writes"), PRD v2.3 item 1 (Andrew-direct 2026-10-09 ~03:2xZ, "opal-gateway-bbg should be an exact copy of opal-gateway for now"), and 1.0.0_SA_CTO~Z's ruling msg 33850 (the positive arm).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (STS, DynamoDB, Secrets Manager).
</preflight>

## 1. THE CELL -- `OG-mg-1` (decomposition addendum R3-T.49 A1)

Two grant writes were planned to ride r30 and were never cut: Andrew's profile, and the Bloomberg mirror. Measured
2026-10-14 ~00:4xZ, read-only, strongly consistent full scan of `gateway-access-state-table` POLICY# partitions:

- **17 POLICY# items**: 4 `data_entitlement`, 4 `principal_profile`-class, 8 `operator_audit`, 1 `email_deny`.
- **ONE active `principal_profile`, and it is Alyssa's** (`profile_kind` restricted, revision 4, grant_revision 4). The
  three other profile-class records are probes (status pending/revoked, sk `PROFILE`).
- **Andrew's principal holds NO profile and NO grant. The Bloomberg principal holds NONE either** (no POLICY# partition
  carries it).

So both writes CREATE: a profile plus a grant revision for each principal. The mirror copies Andrew's NEW grant, not an
existing one.

**The writer -- one module, one entry point for this seat.** Every POLICY# write goes through the admin module
`infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py` (`prepare` -> `activate`, one `operator_transact`). The
MC Portal grant writer (`mcportal-grant-writer-lambda`) imports the same module but refuses without Andrew's verified
owner token, so this seat cannot drive it. This seat uses the module's CLI `activate` under the role
`opal-gateway-access-admin`, exactly as OG-ga-1 did, with `--approver "Andrew Berman"` and `--source-authorization`
naming the records in the preflight. No other path writes a grant.

### What the two records are

| record | principal | profile | grant scope |
|---|---|---|---|
| R1 | Andrew's (tid/oid from `gateway/principals/rosters`, master_admin) | `restricted` (the only kind; under OG-pf-1 it confines ONLY the data-grant family) | v2.2-width: every account in every source the gateway serves (PRD v2.2 item 2), the hidden classes unchanged (v2.2 item 4), `calendar_months: 13` |
| R2 | the Bloomberg principal (oid prefix `517aa5ee`, Part D 2026-09-30) | `restricted` | the SAME scope as R1, identity fields aside: the mirror (PRD v2.3 item 1) |

**The template is the store's own v2.2-width grant.** Alyssa's grant in force (revision 4) is the only v2.2-width scope
on record. Build R1's candidate as that scope with `calendar_months: 13` and identity replaced. **Print the diff of R1
against it.** Its `operations` field is the ONE open choice: Alyssa's carries her no-download rule (v2.2 item 4), and
Andrew's words do not reach his. Put the two branches in the ask (R1 with Alyssa's operations; R1 adding
`download_filtered`), and let the halves name one. Never pick it yourself.

### PHASE A -- read, prepare, ask. NO write

1. **Before-record.** Write `W/MG1_BEFORE.json` from the strongly consistent, fully paginated POLICY# scan:
   `{"read_at", "denominator": {"policy_items_scanned", "principal_profiles"}, "principals": [{"role": "andrew"|"bbg"|"alyssa",
   "pk_hash", "profile": null | {"status", "revision", "grant_revision", "kind"}, "profile_revision", "grant_scope_keys"}]}`.
   - Roles are resolved in-process by the profile's email prefix, or for a principal with no profile by its roster oid.
   - `pk_hash` is the first 10 hex of sha256 of the pk. No tid, oid or email is ever written to the repo; they live
     only in `X` = `%LOCALAPPDATA%/opal/og-salt/mg1/`.
2. **Operator identity and comp-iam.** Assume `opal-gateway-access-admin`; confirm `sts get-caller-identity` names it.
   Simulate each action in the preflight against the role, and record allowed/implicitDeny in `W/MG1_PREFLIGHT.md`.
3. **Candidates and diffs.** Write `X/r1_candidate.json`, `X/r2_candidate.json` and (per branch of `operations`)
   `X/r1b_candidate.json`. Call `prepare(store, raw, load_contract(None), out=...)` in-process under the operator role;
   it validates and prints the diff, and writes nothing.
   - R1's diff against Alyssa's revision-4 scope changes ONLY the window (`calendar_months: 13`) and identity, plus
     `operations` on branch b.
   - R2's scope equals R1's, identity aside.
   - Any other change: STOP, file a BLOCKING row. Save the diff line counts and changed-key lists in
     `W/MG1_PREFLIGHT.md` (keys only, no values).
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-mg-1.md`, for `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~O`, one section per record. It
   carries:
   - **what each record grants and who gains what.** Andrew's principal gains the Schwab data tools and every account
     in every served source for 13 months. The Bloomberg principal gains the same, the mirror. Its Teams surface stays
     under the Opal-users-only gate that OG-tg-1 ships in r30, which is the condition v2.3 item 4 sets ("it ships with
     item 1 or neither ships").
   - **its current value** (none, for both) and **the rollback per record**: `revoke` (a tombstone, never a delete),
     under the same role.
   - **the `operations` branch** to be named by the halves.
   - **the writers of the property**: N = 1 module, read.
   - **the positive arm** this enables (section 4, AC3).

   Run AC1, commit, REPORT, STOP.

### PHASE B -- only on the issuer's GO naming both halves signed (and only after OG-ap-14's ledger is CLOSED)

5. Ledger `nfra-oplgtw-r30-grant-writes`, legs `r1-write`, `r2-write`, `read-back`: entry AND sentinel committed first.
6. Re-read step 1 and confirm nothing moved since Phase A. Then `activate --candidate X/r1_candidate.json` (or the
   named branch), then `X/r2_candidate.json`, each under the operator role with `--approver "Andrew Berman"`, the
   preflight's source records, and a one-line `--summary`. Record each `ACTIVATED profile_revision=... grant_revision=...`
   or `REFUSED:` line in `W/MG1_WRITE.md`. A stale-revision refusal re-cuts Phase A once.
7. **Read-back:** run AC2. On a FAIL, revoke what was written, re-read, close the ledger ROLLED BACK and report. Then
   close the ledger, commit, and report once to `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- The two records only, through the module's `activate` under `opal-gateway-access-admin`. No IAM, policy, Lambda,
  gateway or allowlist change: the identity-scope side is r30's (OG-tg-1).
- No tid, oid, email, account id or grant value in any repo file, row or report: hashes, roles, keys and counts only.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; a delete action; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-r30-grant-writes.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after Phase A, AC2 after Phase B's ledger is closed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-mg-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/mg1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)before-record: roles andrew\+bbg with pk_hash and state: yes; denominator printed: yes.*ask items: 6 of 6; email addresses in the ask: 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-mg-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/mg1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)status CLOSED=yes; sentinel at HEAD=no.*andrew active\+13mo: yes; bbg active: yes; bbg scope == andrew scope: yes; alyssa unchanged: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-mg-1" judgment="true"/>
</proof_of_spec>

- `AC1`: both records are prepared and asked, with their current state and rollback.
- `AC2`: both are written, read back live, and mirrored; the one existing profile is untouched.
- `AC3` (judgment, `3.0.0_SA_CVO~Z`; CTO ruling msg 33850): after r30 AND these writes, `0.0.3_BG_BBGTerminal` re-runs
  its own capability exercise on the 8 gateway data tools it measured denied (opal_discover, mdpf_get_aum_metrics,
  mdpf_get_aggregate_aua, mdpf_get_account_distribution, mdpf_get_model_benchmarks, etfs_get_positioning,
  gateway_query_catalog, ycharts_freshness), the same way it read them, and reads 8 of 8 ALLOWED. That act is owed by
  `0.0.3_BG_BBGTerminal`; record it UNVERIFIABLE-BY-INSTRUMENT naming the CVO and the act. Denied after both is a
  BLOCKING row, not a pass.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-mg-1.r30-grant-writes.proof_of_spec.json`. Validate it after your last
commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip the ONE
`<status>` tag to `complete` only if AC1 and AC2 PASS. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, a mid-round cell inside the issuer's own decomposition (addendum R3-T.49 A1). It carries the two grant writes
  that R3-T.31 assigned to r30 and that were never cut, now load-bearing for 1.0.0_SA_CTO~Z's positive arm (msg 33850).
  The CTO's ruling @8f236865cc kept them as a separate act; this is that act.
- Measured at the cut (2026-10-14 ~00:4xZ): 17 POLICY# items; 1 active profile (Alyssa's, restricted, rev 4); Andrew
  and the Bloomberg principal hold none. The MC Portal grant writer needs Andrew's owner token; the module CLI under
  `opal-gateway-access-admin` is the OG-ga-1 precedent.
- Pre-cut:
  - mg1.AC1 base FAIL as expected (records absent).
  - mg1.AC2 base FAIL as expected: ledger absent; the live read works (policy items 17) and reads andrew no, bbg no.
- Open for the halves, not this seat: R1's `operations` (Alyssa's no-download carried, or `download_filtered` added).

- A1 (issuer, 2026-10-14 ~01:4xZ, row Z-S103): the comp-iam preflight named `dynamodb:TransactWriteItems`, which is
  not an IAM action (accessanalyzer INVALID_ACTION). Simulating it denies any non-admin principal, so it would have
  manufactured a STOP; this was the issuer's defect at the cut. Ruled:
  - **Writes:** Phase A simulates `dynamodb:PutItem` and `dynamodb:UpdateItem` on `opal-gateway-access-admin`, WITH the
    `dynamodb:LeadingKeys` context `POLICY#*`. `GetItem` is unconditioned. These, read allowed, settle the write path:
    `activate()` builds only Put ops and never deletes.
  - **Before-record reads** (strong `Scan`/`Query` of the store) run under the CALLING principal
    (`0.7.0_AE_CloudOps~Z`'s own read access), because the role holds no Query or Scan. Reads only; no write ever runs
    outside the role.
  - Carried to the cut template: an IAM preflight names only actions that exist (check with
    `accessanalyzer validate-policy`), and supplies the condition context the policy keys on.
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A2 (issuer, 2026-10-14 ~02:2xZ, msg 33919): both records are CREATES, so `prepare()` has no stored email to fall back
  on, and each candidate must carry its own. Ruled sources, never typed by hand into the repo:
  - **R1 (Andrew):** the single alias in the live host `.env` `MASTER_ADMIN_EMAILS` (exactly 1, on `opalinvest.com`, as
    measured). That alias is Andrew's master-admin principal.
  - **R2 (Bloomberg):** `opalbloomberg@opalinvest.com`, the identity pinned in code and named by `identity_scope`'s
    `OPAL_USERS_ONLY`.
  - Each value is held off-repo. W records only the source, `sha256(lower(email))[:10]`, and the domain. If either
    source does not resolve to exactly one value at the act, STOP with a BLOCKING row.
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A3 (issuer, 2026-10-14 ~02:3xZ, row Z-S104, msg 33932): **route (i) ruled.** Alyssa's revision-4 scope is already
  contract-MAXIMAL: `dates` `{mode: rolling_complete_window, calendar_months: 13}`, and operations = every operation the
  contract approves (`describe`, `download_filtered`, `list`, `query`). So:
  - R1 is that scope with identity replaced, and R2 is R1's mirror. Neither adds or removes a key.
  - Step 4's branch (a) vs (b) on operations is STRUCK. It was vacuous, which is the issuer's defect at the cut.
  - The ask instead carries ONE measurement for the halves: where Alyssa's no-download rule (PRD v2.2 item 4) actually
    lives (a profile-level field, the contract's `portal_only_schwab_tools`, the hidden classes, or nowhere in force),
    and whether R1 and R2 INHERIT it by being built from her record. Name either outcome; never change it.
  - Andrew's word is 13 months, and v2.2 says any account and any source. Route (iii) (narrower than the template) is
    not taken.
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>complete</status>
<round>37</round>
<workstream>R37-GRANTS</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
