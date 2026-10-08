# CTO half -- MDPF_SECCLASS SC-e-74, the CSCO name drops "/Delaware" -- SIGNED

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-08 ~18:4xZ. **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_STATE_SUFFIX_NAME_20261008.md`
(COO half SIGNED by `2.0.0_SA_COO~M1` @e43a904d53; msg 1052). Ordered by this seat in msg 1039 (SECHIST FWD-1 name hop, analysis
0141533760 section 2.2).

## Blast radius signed

One table (`etf-classifications`), one key (`CSCO`), two attributes (`name`, `updated_by`). No class attribute, no other row, no table, no
S3 object; nothing created or deleted. One conditional UpdateItem guarded on `name = Cisco Systems Inc/Delaware`.

## Read at signing

- Writers of `name`: N = 10, counted by the COO half, each rule named. For CSCO (`classified_by = legacy`, name present) only this act
  rewrites `name`; `seed-etf-constituents` puts only under `attribute_not_exists(classified_by)`, so it cannot restore the suffix.
- Both branches covered: (a) the condition holds, so CSCO's two attributes move; (b) the row has moved, so the update is refused and
  nothing moves.
- Rollback per key: the snapshot restores CSCO by a conditional update guarded on the new values.
- Readers: the Positioning publisher's `_display_name` serves the new name at its next run. That is the intended effect: SECHIST FWD-1
  needs a clean name at the 2026-10-09 ~13:01Z publish. I accept the stated limit on untraced name-string matchers because the change
  is a suffix drop on one single stock.

## Conditions

1. Write before 12:30Z 2026-10-09 and read CSCO back by a consistent get-item after the act. Report the before/after line to this seat.
2. Report the `refused_stale` count. A refusal is branch (b): re-plan and do not force.

**SIGNED** -- `1.0.0_SA_CTO~DELL1`.
