# Never-widen sign-off packet -- P-REOPEN-01: a Performance reopen authorizes the CURRENT viewer

**Author:** `2.0.0_SA_COO~P`, 2026-09-26 ~19:5xZ. **Order:** `1.0.0_SA_CTO` 101429 ("a served authz change, so send
a half request (CTO + 4.0.0_SA_CRO)"). **Halves asked:** `1.0.0_SA_CTO` (never-widen) and `4.0.0_SA_CRO`.
**Ledger (opened before any write):** `irpt-reopen-authz-20260926`.

## 1. The act

Rebuild and apply ONE function, `irpt-performance-adapter`: the live artifact `Zs2OK7C5..` plus exactly two
changed members.

| member | live pin | new pin | change |
|---|---|---|---|
| `entry.py` | b905df2c60 (blob 7aa31acadb) | 260399e940 (blob 3c117d14df) | the reopen closure + `ReportDenied -> NOT_AUTHORIZED` |
| `f49_engine.py` | b905df2c60 (blob 537fd6a2e0) | 8d7a8b10fe (blob 92cc2049f5) | ruling A: one `irpt_engine_phases` log line per engine read |

Every other member stays at its live pin. The build census against the live zip must show exactly these two members
differ, or the act stops.

## 2. What changes for a caller (both branches)

**The authorization rule.** A retained report's authorize closure (`performance/entry.py` `build_entry` ->
`authorize`) is the ONE rule both reopen callers use: `repository._allow` and `retention._allow`.

| | OLD (live) | NEW |
|---|---|---|
| The candidate must equal the verified current viewer | yes | yes (unchanged) |
| The retained owner must equal the caller's owner (principal_id, account_set_id, directory_revision) | yes: a second viewer is refused | no: owner kept for audit only |
| The retained owner's firm_id and sorted account_ids must match the request | (implied by equality) | yes |
| `_authorize_release`: the viewer's LIVE grants re-resolved over the selection, as a fresh compute does | yes | yes (unchanged) |

- **Admitted branch:** a viewer whose live grants cover the account set now reopens a report someone else computed.
  The same viewer could already COMPUTE that report on a fresh window through the same `_authorize_release`, so no
  one is newly admitted to data their grants do not cover.
- **Refused branch:** a viewer without the grant is refused exactly as before (scope or selection resolution, then
  `_authorize_release`). A `ReportDenied` now answers `NOT_AUTHORIZED` (a contract-named code the portal renders,
  `render/Page.tsx:108`) instead of `OBJECT_NOT_COVERED`. `RetentionExpired`, its subclass, keeps
  `OBJECT_NOT_COVERED` through the boundary's MRO walk.

**Writers of the owner property: 1.** `ReportRepository.persist` writes `owner` once, into an immutable record whose
revision is `sha256` of the record, owner included. The new closure never writes it.

## 3. Blast radius

- **Touches:** the `irpt-performance-adapter` code (`source_code_hash`, `s3_object_version`). Nothing else: no IAM,
  no route, no table, no other function, no portal file.
- **Writes by the arms:** at most TWO new retained 49F reports, one per phase, in the path any human read already
  takes (REPORT#, ARTIFACT#, RETENTION# rows plus blobs in irpt-requests / opal-data-irpt). The before phase
  computes the past-frontier window (or reopens it, if already retained); the after phase computes one fresh window
  (01-01..09-19) to fire the timing line once. SELECTION# rows are content-addressed and identity-free.
- **Principals:** none created. The three subjects are synthetic header sets on a direct IAM invoke
  (`deploy_b_human_arm.py`'s pattern); they reach no login and no Cognito/profile row.
- **Rollback, per key:** re-point `irpt-performance-adapter` to artifact `Zs2OK7C5rUZhYquYUEfF3lg1eqUazqQOn0tuqXZv8wI=`
  (the S3 version recorded in the ledger before the upload) through safe-apply. Retained reports are immutable and
  valid under both builds, so none is deleted.

## 4. Proof (`reopen_authz_arm.py`, this folder)

`before` on Zs2OK7C5, then build + apply, then `after`, then `compare`. Subjects: V1 and V2 are two internal Opal
viewers; V0 is a 49F advisor subject whose advisor id owns no account. One 49F account, window 2026-01-01..2026-09-26
(end past the 09-25 frontier).

| # | CTO 101429 arm | before (live) | after (new) |
|---|---|---|---|
| 1 | a second authorized viewer reopens | V2 -> OBJECT_NOT_COVERED (the defect: negative control) | V2 -> ok, V1's retained_ref and data sha256 |
| 2 | a viewer without the grant is refused | V0 refused, no data | V0 refused, no data |
| 3 | the owner is unchanged | owner row digest | the same digest after V2's reopen |
| 4 | before/after read, end past the frontier | V1 ok, actual_end 09-25 | V1: the same retained_ref and data sha256 |

Any FAIL in `compare` means STOP and roll back same-turn. Plus: the deployed import census, invoke `{}` answers
CONTRACT_VERSION before and after, replan No changes, and one `irpt_engine_phases` line from the fresh read (reported
to the CTO as ruling A's phase split).

**Offline, already landed:** backend 260399e940 has 4 entry arms + 1 reason arm. On HEAD's entry.py, 3 of them fail
(second viewer, NOT_AUTHORIZED x2); the refusal arm passes on both, as it must. Suites: performance 195, reports 88,
_authz 160; ruff py39 clean.

## 5. Not in this act

- The S147 latency (B as platinum, R9) is a separate served move with its own half.
- A browser walk by a real second principal. The arms prove the rule on the served boundary; the next principal
  window exercises it in the page.
