# NFRA_OPLGTW task order -- `OG-gv-1` -- APPLY: Andrew's own Schwab grant moves from its HELD stored account lists to the MASTER-WIDE scope (`accounts[master] = ["*"]` for each of his masters), nothing else changed; one grant revision; the `email_deny` handling is ruled in the ask (round 47; round-46 analysis item 6, "then Andrew's own grant moves to it")

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gv-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gv-1</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a grant write only; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the write runs under the existing operator role `opal-gateway-access-admin` as `OG-mg-2` and `OG-ms-2` did.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429) rank 6: "then Andrew's own grant moves to it. That retires `OG-mg-2`'s held half and the `email_deny` follow-on together. The `email_deny` handling is ruled in that cell's ask, not ahead of it." Andrew-direct 2026-10-19 ~17:2xZ (record `ANDREW_DIRECT_20261019_172xZ_ALYSSA_3PM_SCHWAB_TEST_SENDS_YES_ROSTER_AS_OPEN_CALLS_SCHWAB_FULL_ACCOUNTS.md` @65a05f6658): "Schwab should automatically cover the full accounts ... there shouldn't be a persisted list".
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gv-1` (decomposition addendum R3-T.124, amendment A5, round 47, workstream ENRICH-R47-F)

**METHOD = `OG-ms-2`'s and `OG-mg-2`'s** (`org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-ms-2.round-46-add-master-08403355-to-alyssas-schwab-grant.md` and `...TO-OG-mg-2.round-46-schwab-grants-at-the-full-current-accounts.md`, with their amendments), read at HEAD and followed step by step: `ops/schwab_entitlement_admin.py` `prepare` then `activate`, the in-process `decide()` pre-flight, the three-half ask, the ledger with entry AND sentinel first, no delete of any kind, counts and hashes only. This order states only what differs.

**The change:** Andrew's principal (read his tid and oid from his profile record, never typed) has a HELD grant at revision 1 whose `scope.accounts` is a stored list per master (`OG-mg-2` option (b): his activation was held because `activate()` re-creates his `email_deny` record and removing it is a delete). The NEW revision keeps his `masters`, `datasets`, `columns`, `dates` and `operations` byte-equal and replaces ONLY `accounts`: for each of his masters, `["*"]`. Nothing is added: no master, no dataset, no operation. The grant is then "every current account of each master he already holds", resolved at read time by `OG-rt-1`'s code.

⛔ **THE RELEASE-ORDER CONDITION:** Phase B starts only after the `OG-rl-18` ledger (`nfra-oplgtw-gateway-release-batch17`) is CLOSED and the live marker on the host equals its release sha: an OLD gateway reads a stored sentinel as `Malformed` and would deny the principal's WHOLE Schwab access. Phase A may run now, on trunk code (the parser is on trunk); the ask states this ("`OG-rl-18` ... live ... before the activation") and a batch17 rollback after the activation reverts this grant FIRST.

### PHASE A (only on the issuer's GO): prepare, pre-flight, the `email_deny` finding, the ask. NO activation IN ANY FORM

1. **Read the state first** (strong reads of the `POLICY#` partitions): Andrew's profile, his grant revision and its scope; write `W/GV1_BEFORE.json` = `{"principal": {"role": "andrew", "pk_hash": "<sha256 of the pk, 16 hex>", "grant_revision": n, "accounts_before_counts": {master: n}, "scope_sans_accounts_sha256": "<sha256 of the scope without accounts, sorted keys, compact>"}, "denominator": {"policy_items_scanned": n}}` (counts and hashes only).
2. **Prepare** the candidate with `prepare` on trunk's `ops/schwab_entitlement_admin.py` (the master-wide parser): write `W/GV1_DIFF.json` = `{"andrew": {"changed_keys": ["accounts"], "masters_after": [...], "accounts_after": {master: ["*"]}, "rest_of_scope_matches_template": true, "rest_sha256_after_expected": "<sha256 of the scope without accounts and masters, sorted keys, compact>"}}`. `rest_of_scope_matches_template` is true only when every key other than `accounts` equals his current scope.
3. **The `decide()` pre-flight** in ONE fresh process, in-process, no store write: on the candidate, the tools `schwab_get_access`, `schwab_list_files`, `schwab_describe_dataset`, `schwab_query` are admitted and `schwab_prepare_download` is refused: `W/GV1_PREFLIGHT_DECIDE.json` = `{"andrew": {"admit": {tool: true}, "refuse": {"schwab_prepare_download": true}, "master_wide_parsed": true}}`.
4. **THE `email_deny` FINDING (the CTO rules it in his half; you write the facts):** `W/GV1_DENY.json` = `{"deny_record_present_before": <bool: does his email_deny record exist now>, "activate_writes_deny": <bool: would `activate()` write or re-write it>, "effect": "<two or three sentences: what the email_deny record does to his OTHER (non-Schwab) gateway access, read from `app/` code and the activate path, not guessed>", "options": ["<at least two, each one sentence, none a delete>"], "delete_proposed": false}`. Read `ops/schwab_entitlement_admin.py` (`activate`, `_deny_put_op`), the legacy-path gate that reads the record, and `OG-mg-2`'s record of the same finding (`W/MG2_*`).
5. **The ask**, `W/NEVER_WIDEN_ASK_OG-gv-1.md`, for THREE halves (headings with CTO, COO, CVO). It carries: the `diff` (accounts only, per master, stored list to `["*"]`; counts before); the `widening`: the principal's reach grows from the stored account list to every current account of each master he already holds, and to accounts created later, with no grant write; no new master, dataset or operation; the release-order sentence naming `OG-rl-18` live before the activation and the rollback order; the `email_deny` finding (step 4) with the options and a request that the CTO half name the handling; the `rollback` (`revoke` of the new revision, a tombstone, then the held revision-1 scope re-activated as a new revision; never a delete); the `triggers`; the line `process-wide state this change touches: none (one grant record; no process, logger, signal, environment or global config), read`. Commit, run AC1 (`.../r47/checks/gv1.AC1.sh`), REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed, the `OG-rl-18` ledger CLOSED and the live marker equal to its release)

6. Ledger `nfra-oplgtw-gv1-andrew-masterwide`, entry AND sentinel first. Re-read the live marker (print it; it must equal `W/rl18_release.json`'s `release_sha`) and Andrew's grant revision (a different revision than `W/GV1_BEFORE.json` re-cuts Phase A once). Run `activate` for the one record under `opal-gateway-access-admin`, `--approver "Andrew Berman"`, handling the `email_deny` exactly as the CTO half names.
7. **Read back, against the DEPLOYED tree** (`W/GV1_READBACK.json`, `"tree": "deployed"`, `"code_sha"` = the live marker): `decide()` on his LIVE grant in a guarded fresh process importing the deployed `app/`: admits the four read tools and refuses `schwab_prepare_download`; `served` = `{"as_principal": "andrew", "account_count_all_masters": "all", "query_rows": n}`: as Andrew through the served gateway, `schwab_get_access` reports `account_count` `"all"` for each master, and ONE bounded `schwab_query` (any dataset he holds, a small page, no account value printed) answers at least one row. A failed read-back is an incident: revoke the new revision and re-activate the held revision-1 scope at once, close the ledger ROLLED BACK, tell me the same turn.
8. Close the ledger; write `W/NFRA_OPLGTW.TO-OG-gv-1....proof_of_spec.json`; commit; run AC2; report once; send me the ledger CLOSED time.

## 2. BOUNDS

- Andrew's grant record only. No other profile or grant written; no delete of any kind; no IAM, Terraform, deploy or code change. Counts and hashes only in every record: no account number, name, e-mail address or token.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; activate in Phase A in ANY form.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gv1-andrew-masterwide.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gv-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/gv1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)before-record: andrew with pk_hash, scope hash and a printed denominator, per-master counts: yes.*diff keys \['accounts'\], masters after == the two original masters, every master's accounts == \['\*'\], the rest of the scope equals its template: yes.*decide\(\) pre-flight on the candidate \(master-wide parser\) admits the 4 read tools and refuses schwab_prepare_download: yes.*email_deny finding: .*no delete proposed: yes.*ask: three halves yes; process-wide state line yes; states OG-rl-18 live before the activation yes; e-mail-shaped strings 0 \(want 0\); runs of 9\+ digits 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gv-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/gv1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)andrew: active yes; newer grant revision yes; masters equal the two originals yes; accounts == \['\*'\] for every master yes; rest of scope unchanged yes.*alyssa's grant revision as before: yes.*decide\(\) on the LIVE grant against the DEPLOYED tree at the batch17 release: admits 4 read tools and refuses prepare_download: yes.*served read as andrew through the gateway: schwab_get_access account_count 'all' for every master and one bounded schwab_query answered [1-9]\d* row\(s\): yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me on my run before any GO to Phase B; `AC2` (Phase B) after the ledger closes, against the LIVE partitions.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gv-1.round-47-andrews-schwab-grant-moves-to-the-master-wide-scope.proof_of_spec.json` after Phase B and validate it with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-F, amendment A5 of R3-T.124. Source: the CTO's round-46 analysis (msg 36165) rank 6. Staged: Phase A may run now; Phase B waits on `OG-rl-18` CLOSED.
- READINGS DISCLOSED TO THE CTO: (1) Andrew's masters stay as they are (the two originals); `08403355` was Andrew's word for Alyssa only. (2) The `email_deny` handling is the one open ruling: the order asks the applier for facts and options, not a choice; removing the record would be a delete, which this order never does. (3) `AC2`'s `rest of scope unchanged` compares the live scope without `accounts` and `masters` with the hash the applier recorded in Phase A.
- Pre-cut: `AC1` and `AC2` base FAIL as expected (records absent; `AC2` read the live partitions and found no master-wide grant). The check is `grantcheck.py` (phaseA / phaseB); `AC2` reads Alyssa's and Andrew's revisions against `W/MG2_BEFORE.json`.

<status>staged</status>
<status>pending</status>
<round>47</round>
<workstream>ENRICH-R47-F</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
