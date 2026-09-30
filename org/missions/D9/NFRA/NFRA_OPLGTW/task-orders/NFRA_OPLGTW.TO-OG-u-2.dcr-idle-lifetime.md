# NFRA_OPLGTW task order -- `OG-u-2` -- ROUND 2 (E9, part 2): a Dynamic Client Registration expires after a 30-day idle lifetime (row W3-S5, PRD v1.1 C1, R-5), BUILD only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-u-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~12</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change; no cron, alarm, monitor or cadence. The table's existing TTL does the cleanup.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the runtime already writes its own RUNTIME# records.
comp-adversary: DECLARED-NOT-APPLICABLE -- the lifetime is the contract's (PRD v1.1 C1, L10 addendum R-5, ratified-text half SIGNED current).
EGRESS CLASS, declared: NONE. No AWS call, no deploy, no data write.
</preflight>

## 1. THE CELL -- `OG-u-2` (decomposition addendum R2-E, item E9, part 2)

**The defect (row W3-S5).** `/register` is public. `GW/app/oauth_as.py:541-574` `register_client` stores every client
record (`created_at` set, no expiry) so unauthenticated registrations accumulate without bound, limited only by the
per-IP auth rate limit. `GW` = `infra/aws/ec2/opal-gateway`.

**The contract, verbatim** (PRD `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v1.1, C1, :137; addendum R-5
@ac41d1fe1f, wording @c80b5c85b6; `python .tools/prd-signoff.py status NFRA_OPLGTW` reads ADMITTED, ratified-text half
SIGNED current by `3.0.0_SA_CVO~O`):
*"Persist client records so restarting a worker does not forget clients. A client registration expires after a 30-day
idle lifetime, counted from the later of its write to the durable table (a client migrated at cutover counts from that
migration write, never from a legacy registration time) and the last exchange that used it, unless it holds a live
refresh family, which keeps it until that family ends. Its record carries an explicit logical expiry, which every
exchange checks even if the table's TTL deletion is late; an expired client is refused with invalid_client and must
register again. (L10 addendum R-5, 2026-09-28, on row W3-S5.)"*

The idle lifetime is therefore 30 days = 2,592,000 seconds. Put it in ONE named constant.

**How the table already behaves** (read, do not change):
- `GW/app/access_state.py:17-19`: a record whose `expires_at` (epoch seconds) is at or before now reads as ABSENT, even
  while it is still in the table. DynamoDB TTL deletion is cleanup only, never authorization.
- The table's TTL attribute is `expires_at` (`infra/aws/terraform/opal-gateway/schwab_access_state.tf:44`, `:66-67`).
- The refresh family already carries `idle_expires_at` and `expires_at` (`oauth_as.py:814-816`, `:854`, `:877-898`).
- `get_client` is `oauth_as.py:535-538`.

**Build:**
1. `register_client` writes `access_state.EXPIRES_AT: now + 2592000` on the new client record.
2. Every successful exchange that uses a client (authorization-code redemption, refresh-family rotation) extends that
   client record's `expires_at` to `max(current, now + 2592000)`, by a conditional update that never shortens the
   expiry and never recreates a deleted record.
3. A client that holds a LIVE refresh family is kept until that family ends: its record's expiry is never earlier than
   the family's own `expires_at`.
4. Every exchange checks the client's logical expiry and refuses an expired client with `invalid_client`, even when the
   record is still in the table.
5. **A pre-existing client record WITHOUT `expires_at` is never rewritten, backfilled or deleted by this cell.** Its
   logical expiry is computed at read from its `created_at` (its write to the durable table, per the clause) and item
   2's extension on its next use. The operator's upload grant is bound to one live client id
   (`GW/identity_tool_allowlist.txt:19`); a backfill is a production data write this cell does not own.
6. **Tests.** New `GW/tests/test_dcr_idle_lifetime.py` (moto is not needed: use the `AccessState(client=stub)` seam).
   Exactly these 5 tests:
   - `test_new_client_carries_idle_expiry`
   - `test_token_exchange_extends_client_expiry`
   - `test_idle_client_refused_invalid_client` (the record is still present; the refusal is logical)
   - `test_legacy_client_expiry_counts_from_created_at`
   - `test_live_refresh_family_keeps_client`

## 2. BOUNDS

1. Code and tests only. No AWS call, no deploy, no data write, no backfill. Do not edit the contract JSON, the PRD or
   the Terraform.
2. Every test run sets `AUDIT_PATH` to a temp file. If the tracked `GW/audit.jsonl` is dirtied (W3-S2), restore it to HEAD
   bytes.
3. You work in the worktree named in your identity line (the same one as `OG-t-1`). Standing: no push, no vendor call,
   never `git stash`. REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/oauth_as.py
infra/aws/ec2/opal-gateway/tests/test_dcr_idle_lifetime.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~12/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W12-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-u-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/hl.AC1.sh; echo "exit=$?"</invocation><expect>named tests passed 5 of 5; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-u-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/hd.AC2.sh; echo "exit=$?"</invocation><expect>RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

- `AC1` -- the C1 clause, by the 5 named tests.
- `AC2` -- regression control, the same one `OG-u-1` uses (14 or more passed, none failed).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~12/NFRA_OPLGTW.TO-OG-u-2.dcr-idle-lifetime.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once: the diff stat, the 5 test names, the
literal AC1-AC2 output, the commits and the rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~12, queue position 3 (after `OG-u-1`). Rides `OG-t-2`'s release. R-5 is signed (PRD v1.1, CVO half current at
  the cut), so LIMB 6 admits this order in the one issuance.
- HAZARD for `OG-t-2`'s halves: a legacy client idle past 30 days with no live refresh family reads EXPIRED at release.
  `OG-t-2`'s PHASE A counts the `oauth_client` records that would, and names whether the operator's upload client
  (`identity_tool_allowlist.txt:19`) is among them.
- `<risk>` WORLD is GATE (xii)'s floor (an `infra/` path); the cell deploys nothing.

<status>complete</status>
<round>3</round>
<slot>~12</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
