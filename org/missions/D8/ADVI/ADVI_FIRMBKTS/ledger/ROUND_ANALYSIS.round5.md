# ADVI_FIRMBKTS -- ROUND 5, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~07:4xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4691, `surprise-channel/remediations/REMEDIATION_v6.md` @02e2a330df.
- 7 orders are complete with valid proofs. FB-h-5 is parked under round-4 ADDENDUM 1 item 2, outside the round.
- L9 re-ran 14 of 14 criteria and they match. S32 was re-computed with the CVO's own code: equal.
- D1-C-S33, D1-S28 and D1-S40 are REMEDIATED.

## 1. Graded

| FWD | Verdict | Read |
|---|---|---|
| FWD-1 | **PARTIAL** | The 11 of 11 reproduce. But 150 of 150 holds only as a COMPOSITE of two reads under two faces, independent by construction. It closes on ONE blind read of all 150 under the stated face (round 6). |
| FWD-4 | **PARTIAL** | As of 07:25Z there are 0 non-admin validator lines. The 17 organic lines on `/platinum/accounts/` and `/books/relationship/` are all `tier=internal`, the admin bypass (D1-S41). FB-h-5 is parked with this seat as owner (round-4 ADDENDUM 1). The offline replay reads 0 mismatches of 2,127 (FB-h-3). |
| FWD-2, 3, 5, 6, 7, 8 | as graded in ADJUDICATION_v5/v6 | This analysis moves none of them. |

## 2. This seat's rows

- **D1-S41 (INERT): PARKED**, owner `1.0.0_SA_CTO~DELL1`. It un-parks on the first organic non-admin validator line on the accounts or relationship paths, or on a non-admin
  session a seat comes to hold. FWD-4 cannot read REALIZED before then, and that is stated now.
- **D1-W65-S1 (ARMED): the exec-summary trigger.**
  - CloudTrail holds no `PutEvents` call in any of 17 enabled regions over 90 days. The chain-complete WARN never reached the events API, so the failure is UPSTREAM of
    EventBridge: in the runner's emit path (client construction, credentials, region, or a caught exception). FB-h-6's verdict is INDETERMINATE.
  - **Ruling, in order:**
    1. **A runner-side READ:** the WARN line's full exception text from the dispatcher's own log, plus the emit code path at that line (client, region, credential
       source).
    2. **Only if that is still indeterminate:** ONE non-matching test event, a `PutEvents` from the dispatcher's own identity with a `detail-type` that no rule matches. It
       is a write to the events API with no consumer, so it moves nothing served. **This seat's word authorizes exactly that one event.**
    3. **The fix** is its own cell under a never-widen pair (round-3 ADDENDUM 12: the up-to-158 summary keys, a sample read first, prior VersionIds as rollback).
  - **Why it stays ARMED:** client summaries stay stale while the trigger fails, and no interim disarm exists without a served change, so the hazard's disarm IS the fix
    cell. Disarm owner: `2.0.0_SA_COO~B1`.
- **The pricing evidence (FB-h-7, D1-S32 to S34): BRIEF TO THE CRO, agreed.**
  - **S32:** **830 of 5,366 asset-days** (450 assets, 20 weekday partitions) change their T-1 median when de-duplicated by `transaction_id`. The maximum delta is 753.5.
    The CVO re-computed it and it is EQUAL. That is material.
  - **S33:** 0 differ in the current file set, because every tie loses to a later-dated row. 3,906 of 11,108 differ AS OF the 10-09 run, which is INFERRED and not in the
    record. It is a latent defect, and the stable-sort fix rides the same brief.
  - **S34:** 2 of 12 served 2026-08-20..23 objects change under the instant reading, 0 under the strict day-after reading. Which reading the producer intends is the brief's
    first question.
  - None of these is FIRMBKTS's: it moved this pipeline and did not define its rules. `4.0.0_SA_CRO~DELL1` writes the brief for a Black Diamond pricing-rules project. Each
    corrected rule that moves served prices goes under its own pair there. Andrew confirms that project's DONE WHEN, as for any new project.

## 3. ENRICHMENT LIST (round 6, ONE issuance by `2.0.0_SA_COO~B1`)

1. **FWD-1:** ONE blind read of all 150 under the stated face, by a worker that did not author either earlier read.
2. **W65-S1:** the runner-side read, then the one non-matching test event only if it is still indeterminate. The fix is cut on the cause, under its pair.
3. **Carried:** D1-S41 / FB-h-5 (parked, owner this seat); D1-S43 (NFRA_CTLPLN's re-baseline, on the laptop).

## 4. ACTS ONLY ANDREW CAN DO (cited)

None for the round. **Information:** the CRO's pricing brief comes to Andrew for its DONE WHEN, and the exec-summary regeneration sample stays his to read if he chooses
(round-3 ADDENDUM 12).

-- 1.0.0_SA_CTO~DELL1
