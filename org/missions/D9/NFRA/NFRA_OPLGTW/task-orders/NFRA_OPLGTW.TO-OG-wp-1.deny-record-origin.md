# NFRA_OPLGTW task order -- `OG-wp-1` -- walkthrough prep: the ACTIVE email_deny record's origin and the synthetic partitions, read-only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-wp-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~20</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot read; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- reads the access-state table with existing access; nothing written.
comp-adversary: DECLARED-NOT-APPLICABLE -- the remedy is the CTO's (analysis round 12 s.3b, row Z-W12-S8).
EGRESS CLASS, declared: NONE beyond Opal's own AWS, read-only.
</preflight>

## 1. THE CELL -- `OG-wp-1` (decomposition addendum R3-T.7, item 4)

Row Z-W12-S8: the access-state table's only real POLICY partition (write-capable person #1) holds an ACTIVE `email_deny`
record, a live refusal on a roster principal's GUI sign-in path (`/login`, `/sprint*`); plus 3 synthetic `probe-og-i1`
partitions from 2026-09-16. Table `gateway-access-state-table`; the only designed writer is
`infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py deny-backfill` (design
`deliverables/2.0.0_SA_COO~O/R2-k_EMAIL_DENY_CELL_DESIGN_20260927.md`; rulings
`deliverables/1.0.0_SA_CTO~O/RULING_R2-k_FIVE_CALLS_20260927.md`).

1. A STRONG (consistent) read census of the table: total items, real partitions, synthetic partitions, active
   `email_deny` records. Counts only.
2. The deny record's ORIGIN from that partition's `operator_audit` items and the record itself: writer (command or
   path), approver, written time (UTC), source authorization. Any field the data does not hold: `"ABSENT: <why>"`.
3. A disposition PROPOSAL for the deny record: `REVOKE_PROPOSED` (its own never-widen halves would follow, not here) or
   `KEEP_WITH_REASON`, with the reason read from the origin and the rulings.
4. The 3 synthetic partitions: recorded as FIXTURES (keys' shape and date only). Delete nothing.
5. Write `deliverables/0.9.0_WK_NFRA_OPLGTW~20/DENY_RECORD_ORIGIN.json`: `{"census": {"strong_read": true,
   "items_total", "partitions_real", "partitions_synthetic", "email_deny_active"}, "deny_record": {"writer", "approver",
   "written_utc", "source_authorization"}, "deny_disposition", "deny_reason", "synthetic_partitions":
   "FIXTURE_RECORDED", "synthetic_note"}` -- no email address and no GUID anywhere (refer to people by role).

## 2. BOUNDS

Read only: no POLICY write, no delete, no revoke, no deploy. Never print an email, oid or hash key. Never push, merge,
rebase, stash, `checkout --` or `clean`; never override a gate.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~20/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W20-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-wp-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/wp.AC1.sh; echo "exit=$?"</invocation><expect>(?s)missing/invalid 0 \[\]; email/GUID strings 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the record holds a strong-read census, the deny record's origin, a disposition proposal and the fixtures, with
  no personal identifier.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~20/NFRA_OPLGTW.TO-OG-wp-1.deny-record-origin.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`; if it PASSES, append a `complete` status tag after the
order's last status line in the same commit. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 14 (addendum R3-T.7, item 4). S63 (the seal of record) is dispositioned by the issuer's row in this
  issuance: OG-v-4's amendment already names the 18:06Z working seal as phase 1's record and marks `OGV4-AC8` MUTATING;
  OG-v-7 retired that probe. A revoke, if proposed, is a separate act with its own halves.

<status>pending</status>
<round>14</round>
<slot>~20</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
