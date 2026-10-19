# NFRA_OPLGTW task order -- `OG-ms-2` -- APPLY: add Schwab master `08403355` (0840, the Tax SMA master) to ALYSSA'S grant at its full current account set, nothing else changed (round 46; Andrew-direct ~19:55Z 2026-10-19; Phase A now, Phase B only after the release carrying `OG-ms-1` is live)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ms-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ms-2</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one operator grant write and its reads; no cron, alarm, monitor or cadence.
comp-iam: RUN-BY-ISSUER at the cut, as `OG-mg-2` did: `sts:AssumeRole` into `opal-gateway-access-admin`, under it `dynamodb:PutItem` and `dynamodb:UpdateItem` with `dynamodb:LeadingKeys` `POLICY#*`; strong reads under the CALLING principal. You re-simulate them in Phase A; an implicitDeny is a STOP and a BLOCKING row.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew-direct ~19:55Z 2026-10-19 ("we need to add 0840 to her search ability for schwab. she has the 0824 and 0833 accounts at schwab, the smartx and black diamond masters. she needs the 0840 master too added to her entitlements"; record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261019_195xZ_ALYSSA_SCHWAB_MASTER_0840_ADD_TO_ENTITLEMENTS.md`) relayed by `1.0.0_SA_CTO~Z` msg 36102 and sequenced by its ruling (B) msg 36104.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (STS, DynamoDB, S3 reads).
</preflight>

## 1. THE CELL -- `OG-ms-2` (decomposition addendum R3-T.123 amendment A7, round 46, workstream ENRICH-R46-G)

**METHOD = `OG-mg-2`'s, read in `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-mg-2.round-46-schwab-grants-at-the-full-current-accounts.md` with its amendments A1 and A2 and followed step by step; this order states only what differs.** That includes the strongly consistent before-record, `prepare()` under `opal-gateway-access-admin`, the in-process `decide()` pre-flight, counts-only records, no account id, tid, oid or e-mail in any file, and the ask for three halves.

**What changes, and nothing else:** Alyssa's active grant (revision 6 at the cut, profile revision 6, written by `OG-mg-2`) gains the master `08403355`: (1) `scope.masters` gains `"08403355"`; (2) `scope.accounts` gains one key `"08403355"` whose value is that master's full CURRENT account set (the distinct `account_id` values of `dim_balance` at that master's latest complete date, the method `OG-mg-2` used and the CTO accepted; state the date and the S3 prefix `schwab/08403355/silver/dim_balance/date=<d>/`); the accounts of the two masters she already holds are NOT touched. Datasets, columns, dates (rolling complete window, the same `calendar_months`), and operations (her no-download rule) stay exactly as they are. **Andrew's grant is NOT touched** (held by `OG-mg-2` option (b)): this order names Alyssa only. `changed_keys` of the candidate against the grant in force MUST read `["accounts", "masters"]`.

**Confirm in Phase A (read, do not assume):** (a) that `08403355` is the ONLY `0840` prefix under `s3://opal-data-assets/schwab/` (the CTO's request); (b) that `schwab/08403355/silver/` holds the four datasets `dim_position`, `dim_balance`, `dim_asset`, `dim_transaction` with data at the latest complete date (print the date and the object counts per table, no values); (c) `prepare()` accepts the candidate. Phase A runs on trunk code, where `OG-ms-1` (drained as `9095ce68f39`) already lists `08403355` in `MASTERS`; the LIVE gateway does not know the master until the release `OG-rz-2` batch15 is deployed, so the grant, once written, names a master the running gateway will treat as unknown until then (state that plainly in the ask; the order of the acts below makes it harmless).

### PHASE A -- read, prepare, pre-flight, ask. NO write (start on the issuer's GO)

1. **Before-record** `W/MS2_BEFORE.json` (strongly consistent, fully paginated `POLICY#` scan, as `OG-mg-2`): `{"read_at", "denominator": {"policy_items_scanned", "principal_profiles"}, "principal": {"role": "alyssa", "pk_hash", "profile_revision", "grant_revision", "masters": [...], "accounts_before": {master: count}, "accounts_sha256": {master: <sha256 hex of the sorted account ids joined by "\n">}, "new_master": "08403355", "new_master_accounts_current": <count>, "new_master_latest_complete_date": "<YYYY-MM-DD>", "scope_sans_masters_accounts_sha256": "<sha256 hex of json.dumps(scope without the keys masters and accounts, sort_keys=True, separators=(',', ':'), default=num) with num = lambda o: int(o) if o == int(o) else float(o)>"}}`. COUNTS and HASHES only; the candidate lives in `X` = `%LOCALAPPDATA%/opal/og-salt/ms2/`.
2. **Operator identity and comp-iam**, record `W/MS2_PREFLIGHT.md`.
3. **Candidate and diff.** `X/alyssa_candidate.json` = the grant in force with `masters` and `accounts` changed as above. Call `prepare(store, raw, load_contract(None), out=...)` in process; it writes nothing. Write `W/MS2_DIFF.json`: `{"alyssa": {"changed_keys": [...], "masters_added": ["08403355"], "added": {"08403355": <n>}, "other_masters_accounts_unchanged": true}}`. `changed_keys` MUST read `["accounts", "masters"]`; anything else: STOP, BLOCKING row.
4. **decide() pre-flight on the CANDIDATE** (the gateway's own function, in process, no network, no write): for a request naming master `08403355`, the four tools `schwab_get_access`, `schwab_list_files`, `schwab_describe_dataset`, `schwab_query` are ADMITTED and `schwab_prepare_download` is REFUSED; and the same five answers for one of her existing masters are unchanged. Write `W/MS2_PREFLIGHT_DECIDE.json`: `{"alyssa": {"admit": {tool: true|false, ...four}, "refuse": {"schwab_prepare_download": true|false}, "master_in_scope": true}}`. All must read true. A false is a STOP and a BLOCKING row naming the tool.
5. **The ask** `W/NEVER_WIDEN_ASK_OG-ms-2.md` for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word. It carries: what she gains (the master, the count of accounts, the four datasets, the same operations and window), the method and date of the account set, the ONE-MASTER-ONLY statement, the rollback (`revoke` of the new revision, a tombstone, never a delete; revision 6 is the value to restore), the `email_deny` fact (her record already exists, so the activation's idempotent put changes nothing; Andrew's record is not touched because his grant is not), and the line `process-wide state this change touches: <list>, or none, read`.

Run AC1, commit, REPORT, STOP.

### PHASE B -- only on the issuer's GO naming all three halves signed AND the batch15 ledger `nfra-oplgtw-gateway-resize-t4g-large` CLOSED

6. Ledger `nfra-oplgtw-ms2-alyssa-master-0840`, entry AND sentinel first. Re-read step 1; nothing may have moved (a changed grant revision re-cuts Phase A once). The release must be LIVE: read `tools/list` count and the marker (the batch15 sha), and confirm the live service knows `08403355` by one in-process read of the deployed tree's `MASTERS` (counts only).
7. `activate` Alyssa's candidate under the operator role with `--approver "Andrew Berman"`; record the `ACTIVATED ...` or `REFUSED:` line in `W/MS2_WRITE.md`. No other record is written; no delete.
8. **Read-back:** `decide()` on her LIVE grant, in process, into `W/MS2_READBACK_DECIDE.json` (same shape as step 4); run AC2. On a FAIL, `revoke` the new revision, re-read, close the ledger ROLLED BACK and report. Otherwise close the ledger and report the CLOSED time to `2.0.0_SA_COO~O` at once.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`.

## 2. BOUNDS

- ONE record (Alyssa's grant), ONE added master, through `activate` under `opal-gateway-access-admin`. No IAM, code, Terraform, gateway or allowlist change. Never add an operation, dataset, column, date window or any other master; never touch Andrew's grant or any other profile.
- No tid, oid, e-mail, account id or grant value in any repo file, row or report: hashes, roles, keys and counts only.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; a delete action; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-ms2-alyssa-master-0840.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after Phase A, AC2 after Phase B's ledger is closed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ms-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/ms2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)before-record: Alyssa with pk_hash, per-master counts and hashes, the new master's current count and date, scope hash, denominator: yes.*diff keys == \[accounts, masters\]: yes; other masters' accounts unchanged: yes; decide\(\) pre-flight admits 4 and refuses prepare_download on the new master: yes.*ask: three halves yes; process-wide state line yes; e-mail-shaped strings 0 \(want 0\); runs of 9\+ digits 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ms-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/ms2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)status CLOSED=yes; sentinel at HEAD=no.*alyssa: active yes; newer grant revision yes; masters 3 yes; new master count == current yes; other masters' accounts unchanged yes; rest of scope unchanged yes.*andrew: grant revision unchanged yes.*decide\(\) on Alyssa's live grant admits 4 read tools and refuses prepare_download on the new master: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the candidate adds only the master and its accounts, the two existing masters' account lists are untouched, decide() reads 4 admitted and the download refused on the new master, and the ask has three halves.
- `AC2`: the grant is live and read back strongly consistent: a newer revision, three masters, the new master's account count equal to the current set, nothing else changed, Andrew's grant revision unchanged, decide() as in Phase A.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ms-2.round-46-add-master-08403355-to-alyssas-schwab-grant.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (the instance's `expect` copies the order's literal; a pattern amended later must be re-copied), and flip NOTHING (the `<status>` flip is mine). Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 46, a mid-round cell (CTO ruling (B) msg 36104), amendment A7 of R3-T.123. The pair of cells: `OG-ms-1` (the code, complete) and this grant write; the release between them is `OG-rz-2`'s batch15.
- Phase A runs now, on trunk code, so the three halves can be signed before tonight's window; Phase B waits for the batch15 ledger to close (the grant names a master the live gateway does not know until the release is live).
- Pre-cut: `ms2.AC1` and `ms2.AC2` base FAIL as expected.

<status>staged</status>
<status>pending</status>
<round>46</round>
<workstream>ENRICH-R46-G</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
