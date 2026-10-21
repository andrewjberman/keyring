# NFRA_OPLGTW task order -- `OG-gm-2` -- APPLY: Menachem's Schwab grant, MASTER-WIDE over the THREE masters, with Andrew's four datasets and rolling window, no download; one new grant (round 47; Andrew-direct 2026-10-21 ~13:xxZ, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261021_13xxZ_MENACHEM_ENTITLEMENTS_ALL_INDICES_ASSETS_AND_SCHWAB_CONFIRM_LIVENESS.md` @741e63614a, routed by the CTO's msgs 36276 and 36277: "cut both staged now inside round 47")

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gm-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gm-2</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a grant write only; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the write runs under the existing operator role `opal-gateway-access-admin` as `OG-mg-2` did.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew's recorded word (the record above: "make sure all indices are available, particularly the opal-data-assets and schwab categories", scoped by Andrew to `opal-data-assets`, `opal-data-etfs` and `opal-data-portal-v2`) applied by the CTO's msgs 36276 and 36277; the shape is `OG-gm-1`'s, already proven for Alyssa's grant revision 6.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gm-2` (decomposition addendum R3-T.124, amendment A19, round 47, workstream ENRICH-R47-P)

**METHOD = `OG-gm-1`'s, through it `OG-gv-1`'s** (`org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-gm-1.round-47-menachems-schwab-grant-master-wide.md` and `...TO-OG-gv-1.round-47-andrews-schwab-grant-moves-to-the-master-wide-scope.md`: prepare, pre-flight, the `email_deny` finding, the three-half ask, the ledger with entry AND sentinel first, no delete, the read-back against the DEPLOYED tree). Read both; this order states only what differs from `OG-gm-1`. `OG-gm-1` stays SUPERSEDED and untouched.

**What differs:** (1) the grant covers THREE masters, `08242234`, `08335338` and `08403355`, each `accounts[master]` `["*"]`; (2) the TEMPLATE is ANDREW's current grant scope, not Alyssa's: datasets, columns and dates (his four datasets and the rolling window) are copied from his LIVE scope (read it, do not retype it); (3) operations: the four read tools (`list`, `describe`, `query`, the access read), NO `download_filtered` (a reading disclosed to the CTO: Andrew's word names datasets and the window, not the download; the narrower reading is the safe one, one amendment widens it); (4) Menachem's principal comes from a profile that EXISTS (his first sign-in created it); his tid and oid are read from that profile, NEVER typed; if no profile exists when the GO arrives, STOP and report, do not create one.

**NOT in this order:** the `client_*` data grant for every served firm. It needs the per-firm client grant code (the CTO's msg 36202, row Z-S432: `decide()` denies `client_*` before any grant is read), a round-48 cell; its grant order comes right after that cell in the same issuance. This order writes only the Schwab grant.

⛔ **THE RELEASE-ORDER CONDITION:** as `OG-gm-1` and `OG-gv-1`: Phase B only after the `OG-rl-18` ledger is CLOSED and the live marker equals its release sha (an old gateway reads the stored sentinel as `Malformed`). The ask says so in a sentence naming `OG-rl-18` live before the activation. A batch17 rollback after the activation reverts this grant FIRST.

⛔ **TRIGGERS (the CTO's msg 36277): Phase A starts only on my GO, which is given when (a) batch17's ledger is CLOSED and (b) Menachem's principal profile exists.** Until both, nothing is read for him and nothing is written.

### PHASE A (only on the issuer's GO): as `OG-gm-1` Phase A, with these records
- `W/GM2_BEFORE.json` (`principal.role` `menachem`, `first_grant`, `pk_hash`, `scope_sans_accounts_sha256` = the hash of the CANDIDATE scope without accounts, `denominator.policy_items_scanned`); the template's source: Andrew's grant revision and scope hash (hashes only).
- `W/GM2_DIFF.json` = `{"menachem": {"changed_keys": ["accounts", "masters"], "masters_after": [...three...], "accounts_after": {master: ["*"]}, "rest_of_scope_matches_template": true, "rest_sha256_after_expected": "..."}}`, where `changed_keys` are the keys that DIFFER from the template (Andrew's current scope), `rest_of_scope_matches_template` is true only when every key other than `accounts` and `masters` equals his.
- `W/GM2_PREFLIGHT_DECIDE.json` = `{"menachem": {"admit": {...four read tools...}, "refuse": {"schwab_prepare_download": true}, "master_wide_parsed": true}}`.
- `W/GM2_DENY.json`: the `email_deny` finding for HIS email (present before? does `activate()` write it? the effect; options; no delete), as `OG-gv-1` step 4.
- The ask `W/NEVER_WIDEN_ASK_OG-gm-2.md`, three halves under headings containing CTO, COO, CVO, the widening stated plainly (a new principal gets four Schwab read tools over every current account of three masters and of accounts created later, with Andrew's datasets and window; no download), the release-order sentence, the `email_deny` handling for the CTO half to name, the rollback (`revoke` the grant revision, a tombstone; never a delete), the line `process-wide state this change touches: none (grant records; no process, logger, signal, environment or global config), read`. Commit, run AC1 (`.../r47/checks/gm2.AC1.sh`), REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed, the `OG-rl-18` ledger CLOSED and the live marker equal to its release)
As `OG-gm-1` Phase B with ledger `nfra-oplgtw-gm2-menachem-schwab`, `W/GM2_READBACK.json` (`served.as_principal` `menachem`: his own live gateway session; if no session of his exists to read as, report it and STOP before closing: do not mark a served read that was not his). Close the ledger; proof instance; commit; run AC2; report once; send me the ledger CLOSED time.

## 2. BOUNDS

- Menachem's records only (profile read; grant written). No other principal written; no delete of any kind; no IAM, Terraform, deploy or code change; no `client_*` grant; no `person_access` write (the sibling order `OG-pa-1` owns the narrowing, and it is written by the owner's confirm, not by you). Counts and hashes only: no account number, name, e-mail address or token in any record.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; activate in Phase A in ANY form.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gm2-menachem-schwab.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gm-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/gm2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)before-record: menachem with pk_hash, scope hash and a printed denominator.*: yes.*diff keys \['accounts', 'masters'\], masters after == the three masters, every master's accounts == \['\*'\], the rest of the scope equals its template: yes.*decide\(\) pre-flight on the candidate \(master-wide parser\) admits the 4 read tools and refuses schwab_prepare_download: yes.*email_deny finding: .*no delete proposed: yes.*ask: three halves yes; process-wide state line yes; states OG-rl-18 live before the activation yes; e-mail-shaped strings 0 \(want 0\); runs of 9\+ digits 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gm-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/gm2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)menachem: active yes; newer grant revision yes; masters equal the three masters yes; accounts == \['\*'\] for every master yes; rest of scope unchanged yes.*alyssa's grant revision as before: yes.*decide\(\) on the LIVE grant against the DEPLOYED tree at the batch17 release: admits 4 read tools and refuses prepare_download: yes.*served read as menachem through the gateway: schwab_get_access account_count 'all' for every master and one bounded schwab_query answered [1-9]\d* row\(s\): yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me before any GO to Phase B; `AC2` (Phase B) after the ledger closes, against the LIVE partitions.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gm-2.round-47-menachems-schwab-grant-over-the-three-masters.proof_of_spec.json` after Phase B and validate it with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-P, amendment A19 of R3-T.124. Source: Andrew-direct 2026-10-21 ~13:xxZ (the record above) routed by the CTO's msgs 36276 and 36277. STAGED: it runs when batch17's ledger is CLOSED and Menachem's principal profile exists (the CTO's triggers).
- READINGS DISCLOSED TO THE CTO: (1) "Andrew's four datasets and the rolling window" is read as the datasets, columns and dates of Andrew's LIVE scope, copied alias-for-alias; (2) operations are the four read tools with NO download (Andrew's word does not name the download); (3) the three masters are `08242234`, `08335338` and `08403355` as the CTO's msg 36276 lists them (`OG-gm-1` had two, Alyssa's template had the third for her alone); (4) the `client_*` data grant is NOT in this order: it waits on the per-firm client grant code and follows it in the same issuance in round 48.
- Pre-cut: `AC1` and `AC2` base FAIL as expected (no `GM2_*` records, no Menachem grant); `AC1` read OK on synthetic records built to the same fields (arm, not committed).

<status>staged</status>
<round>47</round>
<workstream>ENRICH-R47-P</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
