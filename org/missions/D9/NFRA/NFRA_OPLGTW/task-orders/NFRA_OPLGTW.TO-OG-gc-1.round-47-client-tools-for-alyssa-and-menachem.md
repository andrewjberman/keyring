# NFRA_OPLGTW task order -- `OG-gc-1` -- APPLY: the `client_*` tools for Alyssa and Menachem; find the gates first, write a `person_access` record only if a gate needs one (round 47; Andrew-direct 2026-10-19 ~17:5xZ, call `sitez-20261019T172907Z-fea3` APPROVED the `client_*` grants for both after D1-D3 land)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gc-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gc-1</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read, and at most one grant write; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; any write runs under the existing operator role `opal-gateway-access-admin` as `OG-mg-2` did.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew's recorded word (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_175xZ_ROSTER_OPEN_CALLS_YES_TO_RECS_SCRATCH_NO_REC_WIDENINGS.md`: "yes to all the recs that you had a position on") applied by the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429): `client_*` for Alyssa and Menachem after the code.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gc-1` (decomposition addendum R3-T.124, amendment A7, round 47, workstream ENRICH-R47-H)

**What is asked:** Alyssa and Menachem each reach the five `client_*` tools (`client_resolve_account`, `client_get_holdings`, `client_get_transactions`, `client_get_allocation`, `client_get_fees`) and get an answer. **What is NOT known:** which gate, if any, denies them today. A tool can be refused by the tool-denial policy, the identity scope, the `person_access` record, the tier, the entitlements or the admit scope. So this order is FACTS FIRST: read each gate for each principal, and write only what a gate requires.

**Constraint on any write:** `person_access` records are written only by NFRA_MCPORTAL's grant writer. If the only path is a component this seat does not own, or an owner session, say so in `W/GC1_GATES.json` (`write_path.needs_owner_session` true) and STOP after Phase A: that becomes an Andrew open call, never a workaround. No hand-written item in the table.

### PHASE A (only on the issuer's GO)
1. Read, per principal (`alyssa`, `menachem`; roles, never e-mail or tid in a record): the profile (present?), the `person_access` record (present?), the tool-denial policy, tier and entitlements, and what the admit scope decides for each of the five tools on the TRUNK code (use the gateway's own `decide`/admit functions with the principal's stored records; do not re-implement them).
2. Write `W/GC1_GATES.json`: `{"principals": {"alyssa": P, "menachem": P}, "write_path": W}`, `P = {"role", "profile_present", "client_tools": {<each of the five>: "admitted" | "denied:<gate>"}, "gates_read": [...], "needs_write": bool, "reason": "..."}`, `W = {"mechanism", "needs_owner_session", "writer"}`.
3. For each denied principal also record `person_access_can_admit` (true only if a `person_access` record could change the denial; false when the gate is `entitlements`, i.e. `decide()` denies before `person_access` is read) and cite the lines read. If a denied principal has `person_access_can_admit` true, write the ask `W/NEVER_WIDEN_ASK_OG-gc-1.md`: three headed halves (CTO, COO, CVO); the EXACT `tools_allow` set, a subset of the five; the sentence `nothing else is widened` (no channel, no other tool, no other principal); the rollback (`revoke`, a tombstone, never a delete); the line `process-wide state this change touches: none (grant records; no process, logger, signal, environment or global config), read`. If nothing is denied for either, or no `person_access` record can admit what is denied, write NO ask and say so in `reason`.
4. Commit, run AC1 (`.../r47/checks/gc1.AC1.sh`), REPORT, STOP. Activate nothing in Phase A in ANY form.

### PHASE B -- REMOVED (issuer ruling on row Z-S432, 2026-10-20): Phase A showed that no `person_access` record can admit the five tools (the denial is `decide()`'s `entitlement_denied`; `person_access` only narrows after it). There is nothing for this order to apply. The order closes on its Phase A facts. The instrument is a code change to the entitlement model, asked of the CTO as an enrichment item.

## 2. BOUNDS

- Alyssa's and Menachem's records only, and only `person_access`; no other principal, no `tools_deny` edit, no delete of any kind, no IAM, Terraform, deploy or code change. Counts, roles and hashes only: no account number, name, e-mail address or token in any record.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; activate in Phase A in ANY form.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gc1-client-tools.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gc-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/gc1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)alyssa: five client tools classified yes.*menachem: five client tools classified yes.*write path named: mechanism and writer stated.*: ok.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A, amended: a denied principal whose gate is `entitlements` needs no ask, and none may be present) is graded by me; the order is complete on AC1. There is no Phase B and no `AC2`.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gc-1.round-47-client-tools-for-alyssa-and-menachem.proof_of_spec.json` after Phase A and validate it with `python3 -I .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-H, amendment A7 of R3-T.124. Source: Andrew-direct @50bd4a33b4 (call `fea3` approved) and the CTO's round-46 analysis. Staged: Phase A may run now on trunk code; Phase B waits for `OG-rl-17` (D1-D3 live) CLOSED.
- The shape is two-sided on purpose: the gate that denies the `client_*` tools is not established, so a write is conditional on Phase A's facts. If `person_access` is NFRA_MCPORTAL's alone, the order stops at an Andrew open call; I do not route around that owner.
- Pre-cut: `AC1` and `AC2` base FAIL as expected (no `GC1_GATES.json`, no `GC1_RESULT.json`). The `AC2` pass arm needs a served call from each principal's own session; the order refuses a read that was not theirs.
- AMENDED 2026-10-20 ~12:5xZ (2.0.0_SA_COO~O, row Z-S434): Phase A found that the gate is `entitlements` (`decide()`), which no `person_access` record moves. Phase B and `AC2` removed; `AC1` and Phase A step 3 amended; the order closes on its facts. Gate limb: none graded (an existing tree order that declares no placeholders). The client_* build is the CTO's to rule.

<status>staged</status>
<status>pending</status>
<round>47</round>
<workstream>ENRICH-R47-H</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
