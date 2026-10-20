# NFRA_OPLGTW task order -- `OG-rt-1` -- a MASTER-WIDE Schwab scope resolved at read time: a grant names `accounts[master] = ["*"]` and the gateway reads the master's own data, with no stored account list (round 47; round-46 analysis item 6; Andrew-direct 2026-10-19, "there shouldnt be a persisted list")

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rt-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rt-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~170</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code and test change; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the gateway reads the same master prefixes it reads today.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429), rank 6: "the master-wide Schwab scope resolved at read time, with no stored list (Andrew-direct ~17:2xZ 10-19)". Granting it to anyone is a LATER applier order under its own never-widen; this order changes code only and the code is inert until a grant names `["*"]`.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-rt-1` (decomposition addendum R3-T.124, round 47, workstream ENRICH-R47-A)

WHY. A Schwab grant stores a FROZEN account list per master (`scope.accounts = {master: [raw ids]}`, `app/data_entitlement.py`). Andrew's word is that a grant covers a master's FULL current accounts and "there shouldn't be a persisted list": new accounts must be covered without a grant write. Round 46 only re-activated grants at today's account sets (interim). This order adds the code: a grant may name a master as master-wide, and the gateway then reads the master's own data and resolves account references against the master's CURRENT accounts.

THE DESIGN (the issuer's; read it as the contract). The stored form is `"accounts": {"<master>": ["*"]}`: the one-element list holding the literal `*`. It parses to `Scope.accounts[master] == frozenset({"*"})` (the sentinel; because it is a frozenset every existing reader that sorts or counts it keeps working). Everything below treats the sentinel as "every account of that master that exists in the data at read time". A master that is NOT master-wide behaves exactly as today.

READ FIRST (under `infra/aws/ec2/opal-gateway/`): `app/data_entitlement.py` (the module docstring, `parse_scope` about line 376, `check_scope` about line 936, `Scope` about line 259); `app/account_ref.py` (the docstring, `_resolve` about line 210, `resolve_refs` about line 265); `app/integrations/schwab/integration.py` (`scope_summary` line 139, `_asset_holdings` about line 318, `query` about line 596, the download redemption about lines 905-960); `app/integrations/schwab/query.py` (`build_plan`, its `account_filter` argument, `ACCOUNT_SOURCE`); `ops/schwab_entitlement_admin.py` (`_scope_to_raw`, `scope_diff`: both already work with a frozenset and are NOT edited); `tests/test_account_ref.py`, `tests/test_data_entitlement_guard.py`, `tests/test_schwab_query.py` (the fixtures).

DO:

1. **`app/data_entitlement.py`.** (a) `parse_scope`: for each granted master, `accounts[master]` is either the list `["*"]` (exactly that one-element list) giving `frozenset({"*"})`, or an explicit list of ids as today. `["*", "<id>"]`, `[]`, the bare string `"*"`, and `"*"` mixed into an explicit list are `Malformed`; a `*` entry for a master that is not in `masters` stays `Malformed` through the existing key rule. (b) New function `is_master_wide(scope, master) -> bool`: true exactly when `scope.accounts.get(master) == frozenset({"*"})`. (c) `check_scope`: when the requested master is master-wide, any `account_ids` list that is non-empty is in scope (the `accounts` dimension adds no failure); an EMPTY list still fails as before; an explicit master is unchanged. Update the module docstring's scope description in two lines.
2. **`app/account_ref.py`.** New `class AccountsUnavailable(Exception)` and `candidate_accounts(scope, master, accounts_of=None) -> list`: for an explicit master the sorted explicit ids (`accounts_of` is NOT called); for a master-wide master `sorted(set(accounts_of(master)))`; with `accounts_of` None, or one that raises, `AccountsUnavailable`. `_resolve` builds its candidate list with `candidate_accounts` (replacing the line that reads `scope.accounts.get(master, frozenset())`), and maps `AccountsUnavailable` to its existing UNAVAILABLE denial (`_deny(..., "entitlement_unavailable", UNAVAILABLE, ...)` style, reason without ids). `resolve_refs` and `resolve_ref` gain the keyword `accounts_of=None` and pass it to `_resolve`.
3. **`app/integrations/schwab/integration.py`.** (a) New module function `account_filter_for(scope, master)`: `None` for a master-wide master, else `tuple(sorted(scope.accounts.get(master, ())))`. Replace the three former uses (the `pos_accounts` of `_asset_holdings`, and the two `account_filter` lines in `query` and the download redemption) with it; where a `PolicyFilter(qry.ACCOUNT_SOURCE, accounts)` is built from it, build NO policy filter when it is `None`. (b) `scope_summary`: `account_count[master]` is the string `"all"` for a master-wide master and the integer count otherwise. (c) The account-reference resolution in `query` and in the download redemption passes `accounts_of=` a closure over the master's current accounts: add an async method `_master_accounts(principal, master, date, operation, cache)` that returns the DISTINCT `account_id` values of the master's newest complete `dim_position` snapshot (reuse `_entries`, `_fetch` and the engine exactly as `_asset_holdings` reads the position snapshot: one rows query on the account column), cached on the integration for the life of that snapshot's digest, called ONLY when refs are present and the master is master-wide, and the ids it returns are never logged or returned to a caller. The census of `scope.accounts.get(` in this file must end at TWO (the helper and the explicit count in `scope_summary`).
4. **The new test file `tests/test_og_rt1.py`** with at least these tests (names fixed): `test_ogrt1_parse_and_malformed`, `test_ogrt1_check_scope`, `test_ogrt1_candidate_accounts`, `test_ogrt1_account_filter_for`, `test_ogrt1_scope_summary_all`, `test_ogrt1_master_accounts_distinct_and_cached` (with the fake engine and catalog the Schwab tests use: distinct ids, one engine read for two calls on the same snapshot, a new read when the digest changes), `test_ogrt1_explicit_scope_unchanged` (an explicit-list grant behaves exactly as before: filter tuple, resolution, check_scope), `test_ogrt1_admin_roundtrip` (`ops.schwab_entitlement_admin._scope_to_raw` of a master-wide scope gives `["*"]`, and `scope_diff` reads added `["*"]`, removed the old ids). Fakes only; fake ids (eight digits) built at run time; no real account id.

## 2. BOUNDS

- Write only `app/data_entitlement.py`, `app/account_ref.py`, `app/integrations/schwab/integration.py`, `tests/test_og_rt1.py`, `W/` and, if a row is needed, the channel. NO other product file (the admin script, `admin_grants.py`, the contract and the `client_*` tools are not edited), no release, no deploy, no Terraform, no grant write, no AWS call.
- The sentinel grants NOTHING by itself: no stored grant carries it until an applier order writes one. Do not edit any stored policy record.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number, email address or client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/account_ref.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/tests/test_og_rt1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~170/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W170-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rt-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/rt1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)accepted: one master explicit, one master-wide: ok.*is_master_wide: true for the wildcard master, false for the explicit one: ok.*the sentinel is frozenset.*: ok.*check_scope: any well-formed account ids are in scope for the master-wide master: ok.*check_scope: an id outside an explicit list is still refused: ok.*_scope_to_raw round-trips the sentinel: ok.*scope_diff: from a list to '\*' reads added \['\*'\] and the old ids removed: ok.*refused: '\*' mixed with an id: ok.*refused: an empty list: ok.*refused: a '\*' key for a master that is not granted: ok.*refused: the bare string '\*' \(not a one-element list\): ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rt-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/rt1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)account_filter_for exists: ok.*account_filter_for: None for the master-wide master: ok.*account_filter_for: the sorted tuple for the explicit master: ok.*scope_summary account_count: 'all' for the master-wide master, 2 for the explicit one: ok.*raw scope.accounts.get\( uses left in the schwab integration: at most 2: ok.*account_ref.candidate_accounts and AccountsUnavailable exist: ok.*explicit master: the explicit set, provider not called: ok.*master-wide master: the provider's ids, sorted and de-duplicated: ok.*a provider that raises: AccountsUnavailable: ok.*resolve_refs takes accounts_of=None: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-rt-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/rt1.AC3.sh; echo "exit=$?"</invocation><expect>(?s)new file tests/test_og_rt1.py: [1-9]\d* passed, 0 failed.*neighbours \(\d+\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the entitlement layer (parse, `is_master_wide`, `check_scope`, the admin round trip). `AC2`: the Schwab tool layer's filter and summary and the account-reference candidate rule. `AC3`: your test file (which covers `_master_accounts` and the explicit-scope no-change case) and the seven existing neighbour files.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rt-1.round-47-a-master-wide-schwab-scope-resolved-at-read-time-with-no-stored-account-list.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). Flip the ONE `<status>` tag to `complete` only if all three PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-A, `<risk>WORLD</risk>` is the gateway-path floor. Source: the CTO's round-46 analysis (msg 36165) rank 6; Andrew-direct ~17:2xZ 2026-10-19 (record `ANDREW_DIRECT_20261019_172xZ_ALYSSA_3PM_SCHWAB_TEST_SENDS_YES_ROSTER_AS_OPEN_CALLS_SCHWAB_FULL_ACCOUNTS.md` @65a05f6658). The grants that USE the sentinel (Andrew's own, Menachem's) are later applier orders; Andrew's grant moving to it retires `OG-mg-2`'s held half and the `email_deny` follow-on, and the CTO rules the `email_deny` handling in that grant's ask, not here.
- READINGS DISCLOSED TO THE CTO: (1) the stored sentinel is `["*"]` under the existing `accounts` key, not a new scope key, so an old gateway reading a new grant would call it Malformed (denying the principal): the release ORDER matters (this code live before any grant names `*`), and the grant order's Phase A must say so. (2) For a master-wide master the account-reference resolver enumerates the master's accounts from the newest complete `dim_position` snapshot, so a reference to an account with no position row in that snapshot does not resolve; that is the issuer's choice of "current accounts" and is stated in the code comment. (3) The dim_asset restriction (the CUSIPs a grant's accounts hold) uses the whole master's positions for a master-wide master, which is what "the master's full accounts" means. (4) Nothing here changes who may be granted a master: `scope.masters` is unchanged.
- Pre-cut: `AC1` base FAIL as expected (the master-wide scope is Malformed; the four refusal controls pass trivially), `AC2` base FAIL as expected (early exit: the scope does not parse), `AC3` base FAIL as expected (no test file). `AC1` and `AC2` were both fed a reference implementation in a scratch copy (about 40 changed lines in `data_entitlement.py`, `account_ref.py` and the integration's helper) and read PASS on every line, then it was discarded. The seven neighbour files pass at the base except the carried red `test_ogz1_ac08` (72 passed).

<status>pending</status>
<round>47</round>
<workstream>ENRICH-R47-A</workstream>
<slot>~170</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
