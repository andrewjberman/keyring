# Release 5 after-reads: gate CLOSED (irpt-status still revision 6); BEFORE arms measured -- 0.7.0_AE_CloudOps~ANL

**Date:** 2026-10-11
**Task Order:** IRPT_ANLREQ.TO-READS-Y5
**Status:** BLOCKED (waiting on the issuer's word that the apply landed)

**archetype:** VALIDATE

---

## Objective

Run the release 5 after-reads R2 to R7 of `irpt-status` build `Iw3FADFr...` from the laptop. Step 0 is a gate: if the live
`CodeSha256` is not `Iw3FADFr...`, do nothing further but the BEFORE arms.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam / comp-blast / comp-routes / comp-cache / comp-schedule | -- | SKIPPED | the order declares each not applicable or run by reading |
| crossbox ack | `python .tools/crossbox-call.py ack --id XB-20261011T095749Z-6fe4 --by 0.7.0_AE_CloudOps~ANL` | ACKED 10:04:03Z | reply line goes to dell2 |
| get-function-configuration | `.tools/aws lambda get-function-configuration --function-name irpt-status` | `6idtFvAm...` | gate |

**What worked:** the 2026-10-11 run34.py method (direct invoke, front-door event shape, owner claims replayed) reads R2, R3 and
the section-date read; routes are `analysis/{jobId}/sections`, `analysis/requests`, and `status/{jobId}` with header
`x-irpt-status-dates: prospect-v1`.
**What failed:** replaying `x-user-role: user` made 13 + 3 active-admin owners answer FIRM_BINDING; replaying the profile role
changed nothing. REQ-5e4149d2 (49financial) is among the FIRM_BINDING owners, so the order's R4 request is not readable from
the laptop by this method.
**Gap found:** none filed; see Blockers.

---

## Verification

| Step | Result |
|---|---|
| 0 gate | `CodeSha256` `6idtFvAmYk73wJdr5DPRIyEPrLeWgzjlqbdNr5f1wxc=`, LastModified 2026-10-11T04:44:47Z: NOT `Iw3FADFr...`; no after-read run |
| BEFORE R2 | 14 of 50 accepted requests answer sections (all cottonwood, all the v1 YCHARTS form: no `provider` member); `retained_ref` present on 0 of 14 |
| BEFORE R3 | history as a cottonwood owner: 39 rows over 2 pages, row keys `accepted_at`, `identity` only; no `client_id`, no `client_claim`, no `unreadable_rows` |
| BEFORE R5 | status-job with `prospect-v1`: 14 of 14 readable cottonwood requests READY with `date_basis` PER_SECTION; digests in the snapshot |
| BEFORE R4 | REQ-5e4149d2863aea31cc87d660: owner replay answers FIRM_BINDING on sections and status-job; not readable. No readable request carries `provider: OPAL_ENGINE` |
| Denominator | 1894 irpt-requests items scanned over 2 pages; 50 `analysis#REQ-<24hex>#1` records (cottonwood 39, 49financial 10, inflection 1) |

Snapshot: `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y5_before_arms_rev6_snapshot.json`. Scripts:
`.../deliverables/y5_scripts/snap.py` and `irptlib.py` (re-run `snap.py <out.json>` after the apply and diff).
Tripwire D1-S17 (`TRIPWIRE_D1_S17_...20261011.md`) read: it binds apply or deploy under an IRPT order; this order is read-only and
neither half of the release 5 pair carries a D1-S17 line (0 of 2 files). Reported to the issuer, not acted on.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Did not write `Y5_after_reads_result.json` | the order's check reads that file as the release-build result; a before-build file there would pass for it |
| Ran the BEFORE arms | the order says "should": they are the comparison |

---

## Files Modified

| File | Change |
|---|---|
| `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y5_before_arms_rev6_snapshot.json` | new |
| `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/y5_scripts/snap.py`, `irptlib.py` | new |
| this log | new |

NO AWS resource, object, table row or Lambda was created, modified or deleted.

---

## Blockers

1. The release 5 apply has not landed (`CodeSha256` still revision 6). Waiting on `2.0.0_SA_COO~Y2`'s word.
2. R4: REQ-5e4149d2 is refused FIRM_BINDING on owner replay from this seat. Issuer to say whether R4 is recorded ABSENT with the
   census above, or whether another readable OPAL_ENGINE request exists.

---

## Current State

Lane `0.7.0_AE_CloudOps~ANL` live, one inbox watcher armed, zero crons. Order held, step 0 closed.

---

## Next Steps

1. `[2.0.0_SA_COO~Y2]` Tell this seat when `irpt-status` is `Iw3FADFr...`; rule on R4.
2. `[0.7.0_AE_CloudOps~ANL]` On that word: re-run step 0, `snap.py`, R6, R7, write `Y5_after_reads_result.json`, commit.
