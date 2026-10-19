# NFRA_OPLGTW task order -- `OG-mg-2` -- APPLY: re-activate Andrew's and Alyssa's Schwab grants at each granted master's CURRENT account set, nothing else changed; in-process decide() pre-flight (round 46, URGENT: before 2026-10-19T18:45Z; Andrew-direct ~17:2xZ)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-mg-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-mg-2</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two operator grant writes and reads; no cron, alarm, monitor or cadence.
comp-iam: RUN-BY-ISSUER at the cut, the way `OG-mg-1` ran it (amended A1 there): `sts:AssumeRole` into `opal-gateway-access-admin`; under it `dynamodb:PutItem` and `dynamodb:UpdateItem` with the `dynamodb:LeadingKeys` context `POLICY#*` (the writes `activate()` makes); strong reads of the store run under the CALLING principal. You re-simulate each in Phase A and record allowed/implicitDeny; an implicitDeny is a STOP and a BLOCKING row.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew-direct ~17:2xZ 2026-10-19 (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_172xZ_ALYSSA_3PM_SCHWAB_TEST_SENDS_YES_ROSTER_AS_OPEN_CALLS_SCHWAB_FULL_ACCOUNTS.md` @65a05f6658: "Schwab should automatically cover the full accounts ... there shouldnt be a persisted list") relayed by `1.0.0_SA_CTO~Z` msg 36025 (a), (b).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (STS, DynamoDB, S3 reads).
</preflight>

## 1. THE CELL -- `OG-mg-2` (decomposition addendum R3-T.123 amendment A3, round 46, workstream ENRICH-R46-C)

**DEADLINE: both grants live and read back before 2026-10-19T18:45:00Z.** Alyssa tests at 19:00Z with Andrew. Move fast; do not widen anything.

Today a Schwab grant stores a frozen account list (`scope.accounts = {master: [ids]}`; `app/data_entitlement.py`). Andrew's word is that a grant covers a master's FULL current accounts. The code that resolves them at read time is a round-47 cell; THIS order is the interim: write a NEW grant revision for each of two principals whose `accounts` lists are each granted master's account set as it stands in S3 today, and change NOTHING else in the scope.

**The two principals** (resolved in-process by the profile's e-mail prefix, as `OG-mg-1` did; no e-mail, tid or oid in any repo file): Andrew's master-admin profile (`role` `andrew`) and Alyssa's profile (`role` `alyssa`). The Bloomberg principal and every other profile are NOT touched.

**The account set of a master "as it stands in S3 today"** is what the gateway's own Schwab tools enumerate for that master: use the same enumeration the deployed code and `ops/schwab_entitlement_admin.py` use (read them; do not invent a second method), over the latest complete date. State the method, the date and the S3 prefix in the ask (not the ids). The CTO's measure for one master is 7,559 now against 7,690 in S3 (master `08335338`); your count per master is the one that counts.

### PHASE A -- read, prepare, pre-flight, ask. NO write

1. **Before-record** `W/MG2_BEFORE.json` (strongly consistent, fully paginated `POLICY#` scan): `{"read_at", "denominator": {"policy_items_scanned", "principal_profiles"}, "principals": [{"role": "andrew"|"alyssa", "pk_hash", "profile_revision", "grant_revision", "masters": [...], "accounts_before": {master: count}, "accounts_current": {master: count}, "scope_sans_accounts_sha256"}]}`. `pk_hash` = first 10 hex of sha256 of the pk. `scope_sans_accounts_sha256` = sha256 hex of `json.dumps(scope_without_accounts, sort_keys=True, separators=(",", ":"), default=num)` with `num = lambda o: int(o) if o == int(o) else float(o)` (DynamoDB Decimals), computed on the grant in force. COUNTS ONLY: no account id, tid, oid or e-mail is written to the repo; the candidates live in `X` = `%LOCALAPPDATA%/opal/og-salt/mg2/`.
2. **Operator identity and comp-iam** as in the preflight; record `W/MG2_PREFLIGHT.md`.
3. **Candidates and diffs.** For each role write `X/<role>_candidate.json` = the grant in force with ONLY `accounts` replaced by the current set per master (same masters). Call `prepare(store, raw, load_contract(None), out=...)` in-process under the operator role; it validates and writes nothing. Write `W/MG2_DIFF.json`: `{"andrew": {"changed_keys": [...], "added": {master: n}, "removed": {master: n}}, "alyssa": {...}}`. **`changed_keys` MUST read `["accounts"]` for both.** Any other changed key, or any removed account that is no longer in S3 and was in the grant, is reported in `removed`; a non-empty `removed` is NOT a stop but goes in the ask. Anything else: STOP, BLOCKING row.
4. **decide() pre-flight on Alyssa's CANDIDATE, in process, no network, no write:** build the grant from the candidate and call the gateway's own `decide()` (the entitlement decision function in `app/data_entitlement.py` / the Schwab tools' gate; read how a tool call is decided) for the four tools `schwab_get_access`, `schwab_list_files`, `schwab_describe_dataset`, `schwab_query` and for `schwab_prepare_download`. Write `W/MG2_PREFLIGHT_DECIDE.json`: `{"alyssa": {"admit": {tool: true|false, ...four}, "refuse": {"schwab_prepare_download": true|false}}}` where `admit[tool]` is true when decide() ADMITS it and `refuse[...]` is true when decide() REFUSES it. All five must read true. A false is a STOP and a BLOCKING row naming the tool.
5. **The ask** `W/NEVER_WIDEN_ASK_OG-mg-2.md` for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word (CTO, COO, CVO). It carries: what each record grants and who gains what (the counts added per master per role, from the diff), the method and date of the current set, the rollback (`revoke` of the new revision, a tombstone, never a delete; the previous revision's scope is the value to restore), the line `process-wide state this change touches: <list>, or none, read` (CVO verdict 35844), and the approver: Andrew's word as quoted in the preflight record.

Run AC1, commit, REPORT to `2.0.0_SA_COO~O`, STOP. Be quick: the COO signs within minutes and relays to the CTO.

### PHASE B -- only on the issuer's GO naming all three halves signed

6. Ledger `nfra-oplgtw-mg2-schwab-full-accounts`, entry AND sentinel committed first (legs `andrew-write`, `alyssa-write`, `read-back`).
7. Re-read step 1; nothing may have moved (a changed grant revision re-cuts Phase A once). Then `activate` each candidate under the operator role with `--approver "Andrew Berman"` and the preflight's source record; record each `ACTIVATED profile_revision=... grant_revision=...` or `REFUSED:` line in `W/MG2_WRITE.md`.
8. **Read-back:** re-run the decide() check on Alyssa's LIVE grant (strongly consistent read, in process) into `W/MG2_READBACK_DECIDE.json` (same shape as step 4); run AC2. On a FAIL, `revoke` the new revisions, re-read, close the ledger ROLLED BACK and report. Otherwise close the ledger, commit, and report once to `2.0.0_SA_COO~O` with the CLOSED time.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`.

## 2. BOUNDS

- The two records only, through the module's `activate` under `opal-gateway-access-admin`. No IAM, policy, Lambda, gateway, allowlist or code change. Never add `download_filtered` or any operation, master, dataset, column or date window: ONLY `accounts` changes.
- No tid, oid, e-mail, account id or grant value in any repo file, row or report: hashes, roles, keys and counts only.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; a delete action; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-mg2-schwab-full-accounts.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after Phase A, AC2 after Phase B's ledger is closed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-mg-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/mg2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)before-record: both roles with pk_hash, counts before and current, scope hash, denominator: yes; current >= before on every master: yes.*diff keys for each role == \[accounts\]: yes; decide\(\) pre-flight on Alyssa admits 4 and refuses prepare_download: yes.*ask: three halves yes; process-wide state line yes; e-mail-shaped strings 0 \(want 0\); runs of 9\+ digits 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-mg-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/mg2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)status CLOSED=yes; sentinel at HEAD=no.*andrew: active yes; newer grant revision yes; per-master counts == current yes; rest of scope unchanged yes.*alyssa: active yes; newer grant revision yes; per-master counts == current yes; rest of scope unchanged yes.*decide\(\) on Alyssa's live grant admits 4 read tools and refuses prepare_download: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: both grants are prepared at the current account sets with only `accounts` changed; the decide() pre-flight reads 4 admitted and `schwab_prepare_download` refused; the ask has three halves.
- `AC2`: both grants are re-activated and read back live, the rest of each scope hashes unchanged, and decide() on the live grant still admits four and refuses the download.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-mg-2.round-46-schwab-grants-at-the-full-current-accounts.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip the ONE `<status>` tag to `complete` only if AC1 and AC2 PASS. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 46, a mid-round cell cut on the CTO's relay of an Andrew-direct (msg 36025, record @65a05f6658), amendment A3 of R3-T.123. It is the INTERIM half of Andrew's "no persisted list" word; the read-time scope is the round-47 cell the CTO named.
- Measured at the cut (2026-10-19 ~18:0xZ, read-only): both principals hold an ACTIVE profile with a grant in force (the mg2.AC2 dry-run at the base reads `active yes` for both and `newer grant revision no`); the check scripts FAIL at the base as expected (AC1: records absent; AC2: ledger absent, no newer revision).
- Pre-cut: `mg2.AC1` base FAIL as expected; `mg2.AC2` base FAIL as expected.
- Open for the halves, not this seat: whether Andrew's word reaches Alyssa's grant. The CTO relays it for both (msg 36025 (a)); the ask records that quotation and the halves sign or refuse it.

- A1 (issuer, 2026-10-19 ~18:3xZ): the applier's finding that `activate()` re-creates Andrew's `email_deny` record (row W3-S22; his record does not exist today, Alyssa's does) is ruled by the COO half: option (b), Alyssa's grant NOW, Andrew's HELD for a follow-on order with the deny handling. Phase B writes ONE record (Alyssa's) and writes `W/MG2_ANDREW_HELD.md`; `mg2.AC2` (amended the same turn) reads Andrew's grant revision as UNCHANGED when that file exists. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>46</round>
<workstream>ENRICH-R46-C</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
