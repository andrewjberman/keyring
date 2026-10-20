# NFRA_OPLGTW task order -- `OG-gm-1` -- APPLY: Menachem's Schwab grant, in the MASTER-WIDE shape, the same shape as Alyssa's (four read tools, no download), over the two original masters; one new grant (round 47; Andrew-direct 2026-10-19 ~17:5xZ, call `sitez-20261019T172907Z-fea3` APPROVED "(a) Menachem's Schwab grant, the same shape as Alyssa's, over the full current accounts, after her 3p session proves it"; the CTO's analysis: "in the master-wide shape once item 6 lands")

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gm-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gm-1</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a grant write only; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the write runs under the existing operator role `opal-gateway-access-admin` as `OG-mg-2` did.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew's recorded word (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_175xZ_ROSTER_OPEN_CALLS_YES_TO_RECS_SCRATCH_NO_REC_WIDENINGS.md`: "yes to all the recs that you had a position on") applied by the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429): "Grants after the code, each with its own never-widen: Menachem's Schwab grant, in the master-wide shape once item 6 lands". Alyssa's 19:00Z session on 2026-10-19 ran under grant revision 6 (the shape is proven).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gm-1` (decomposition addendum R3-T.124, amendment A6, round 47, workstream ENRICH-R47-G)

**METHOD = `OG-gv-1`'s** (`org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-gv-1.round-47-andrews-schwab-grant-moves-to-the-master-wide-scope.md`, steps 1 to 8: prepare, pre-flight, the `email_deny` finding, the three-half ask, the ledger with entry AND sentinel first, no delete, the read-back against the DEPLOYED tree), through it `OG-ms-2`'s and `OG-mg-2`'s. This order states only what differs.

**The grant:** Menachem's principal (his tid and oid read from the people/roster records the gateway's grant tools already use; NEVER typed; if he has no profile yet this is a FIRST grant: `prepare` creates the profile and grant records together, `first_grant` true in the before-record) gets a scope that is ALIAS-FOR-ALIAS Alyssa's CURRENT grant scope with two differences: (1) `masters` is the two ORIGINAL masters only (`08242234`, `08335338`): the third master (`08403355`) was Andrew's word for Alyssa alone; (2) `accounts[master]` is `["*"]` for each of the two. Datasets, columns, dates and operations are copied from her live scope (the template: read it, do not retype it; operations `list`, `describe`, `query`; no `download_filtered`; her rolling window), so the shape is hers by construction. Nothing else: no other principal, no download, no master beyond the two.

⛔ **THE RELEASE-ORDER CONDITION:** as `OG-gv-1`: Phase B only after the `OG-rl-18` ledger is CLOSED and the live marker equals its release sha (an old gateway reads the stored sentinel as `Malformed`). The ask says so in a sentence naming `OG-rl-18` live before the activation. A batch17 rollback after the activation reverts this grant FIRST.

### PHASE A (only on the issuer's GO): as `OG-gv-1` steps 1 to 5, with these records
- `W/GM1_BEFORE.json` (`principal.role` `menachem`, `first_grant`, `pk_hash`, `scope_sans_accounts_sha256` = the hash of the CANDIDATE scope without accounts, `denominator.policy_items_scanned`); the template's source: Alyssa's grant revision and scope hash (hashes only).
- `W/GM1_DIFF.json` = `{"menachem": {"changed_keys": ["accounts", "masters"], "masters_after": [...two...], "accounts_after": {master: ["*"]}, "rest_of_scope_matches_template": true, "rest_sha256_after_expected": "..."}}`, where `changed_keys` are the keys that DIFFER from the template (Alyssa's current scope), `rest_of_scope_matches_template` is true only when every key other than `accounts` and `masters` equals hers.
- `W/GM1_PREFLIGHT_DECIDE.json` = `{"menachem": {"admit": {...four read tools...}, "refuse": {"schwab_prepare_download": true}, "master_wide_parsed": true}}`.
- `W/GM1_DENY.json`: the `email_deny` finding for HIS email (present before? does `activate()` write it? the effect; options; no delete), as `OG-gv-1` step 4.
- The ask `W/NEVER_WIDEN_ASK_OG-gm-1.md`, three halves, the widening stated plainly (a new principal gets four Schwab read tools over every current account of two masters and of accounts created later; no download), the release-order sentence, the `email_deny` handling for the CTO half to name, the rollback (`revoke` the grant revision, a tombstone; never a delete), the line `process-wide state this change touches: none (grant records; no process, logger, signal, environment or global config), read`. Commit, run AC1 (`.../r47/checks/gm1.AC1.sh`), REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed, the `OG-rl-18` ledger CLOSED and the live marker equal to its release)
As `OG-gv-1` steps 6 to 8 with ledger `nfra-oplgtw-gm1-menachem-schwab`, `W/GM1_READBACK.json` (`served.as_principal` `menachem`: his live gateway session is his own; if no session of his exists to read as, the served read is run by the applier through the gateway as the OWNER with the principal's grant read from the store and `served.as_principal` still `menachem` only when his own session answered; otherwise report it and STOP before closing: do not mark a served read that was not his). Close the ledger; proof instance; commit; run AC2; report once; send me the ledger CLOSED time.

## 2. BOUNDS

- Menachem's records only (profile and grant, together if first). No other principal written; no delete of any kind; no IAM, Terraform, deploy or code change. Counts and hashes only: no account number, name, e-mail address or token in any record.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; activate in Phase A in ANY form.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gm1-menachem-schwab.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gm-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/gm1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)before-record: menachem with pk_hash, scope hash and a printed denominator.*: yes.*diff keys \['accounts', 'masters'\], masters after == the two original masters, every master's accounts == \['\*'\], the rest of the scope equals its template: yes.*decide\(\) pre-flight on the candidate \(master-wide parser\) admits the 4 read tools and refuses schwab_prepare_download: yes.*email_deny finding: .*no delete proposed: yes.*ask: three halves yes; process-wide state line yes; states OG-rl-18 live before the activation yes; e-mail-shaped strings 0 \(want 0\); runs of 9\+ digits 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gm-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/gm1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)menachem: active yes; newer grant revision yes; masters equal the two originals yes; accounts == \['\*'\] for every master yes; rest of scope unchanged yes.*alyssa's grant revision as before: yes.*decide\(\) on the LIVE grant against the DEPLOYED tree at the batch17 release: admits 4 read tools and refuses prepare_download: yes.*served read as menachem through the gateway: schwab_get_access account_count 'all' for every master and one bounded schwab_query answered [1-9]\d* row\(s\): yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me before any GO to Phase B; `AC2` (Phase B) after the ledger closes, against the LIVE partitions.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gm-1.round-47-menachems-schwab-grant-master-wide.proof_of_spec.json` after Phase B and validate it with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-G, amendment A6 of R3-T.124. Source: Andrew-direct @50bd4a33b4 (call `fea3` approved) and the CTO's round-46 analysis. Staged like `OG-gv-1`.
- READINGS DISCLOSED TO THE CTO: (1) "the same shape as Alyssa's" is read as her scope MINUS the third master: `08403355` was Andrew's word of 2026-10-19 ~19:55Z for Alyssa only. If the CTO reads it as her full three masters, that is one amendment before the ask. (2) The Phase B served read as Menachem needs a session of his own; the order refuses to mark a read that was not his. (3) `email_deny` for a new principal: the finding is the applier's facts, the handling the CTO's.
- Pre-cut: `AC1` and `AC2` base FAIL as expected; `AC2` read the live partitions (no Menachem grant).

<status>staged</status>
<status>pending</status>
<round>47</round>
<workstream>ENRICH-R47-G</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
