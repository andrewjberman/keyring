# CTO ROUND ANALYSIS -- IRPT_ANLREQ round 1 (FWD-1, the thread)

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~07:1xZ | **Input:** the CVO's L10 slug msg 2759,
`org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/adjudications/ADJUDICATION_v1.md` and `remediations/REMEDIATION_v1.md` @6b63763b89.
Round 1: 9 of 9 orders complete, MAY-CLOSE, 13 OPEN, 2 ARMED. **PRD:** `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` v0.3.

## Grade

**FWD-1 is NOT REALIZED. The thread is code-complete and not live.** No other FWD is graded this round. Round 1 built the thread; round 2 makes it live
and enriches it.

## The releases, in order (each under its own never-widen pair; none is a cell)

| # | release | lane | pair state |
|---|---|---|---|
| 1 | `irpt-status`, with the packaged `AnalysisSubmissionRequest` schema re-pinned (W1-S2) | `~Y2` | owed |
| 2 | `opal-ticket-api` (AR-v-12) | `~V2` | CTO half GIVEN @7319f84a6e |
| 3 | IB-pr-391 composition reader, then the commentary store and Lambda (I3, I4) | `~P2`, then `~T2` | GIVEN @a946f8b829; @5e467d90af, AMENDMENT 1 @f4203149ad |
| 4 | `~G2`'s resident release, with the packager mint (W62-S1, W62-S2) | `~G2` | owed |

**Two ARMED rows must be disarmed before their releases:**
- **W41-S1 (`~T2`):** the commentary zip packages `keys.py` and the firm registry. The import is proven from the built bytes with a negative control
  BEFORE apply. This is now a condition of this seat's commentary half.
- **W11-S1 (`~V2`):** a disposition row names the portal reader fix, which landed on DEV as 9988b426. A `ticket_id` body passes the closed reader on the DEV
  build.

## Rulings on the open rows

1. **W61-S1, the READY-to-I3 crash gap (FWD-4): redelivery re-sends when no send is recorded.**
   - The READY write records `i3_sent_at` only after the send succeeds.
   - A redelivery that finds READY with no `i3_sent_at` sends again.
   - The consumer is already idempotent (`draft_exists` stops a second draft), so a duplicate send is harmless and a lost send is impossible.
   - Chosen over an outbox table because it adds no new store.
2. **W62-S4, one shape for `commentary_ref` and `pdf_ref`:** the structured form `{artifact_id, sha256, version_id}` on both sides (AR-g-12 and AR-t-12),
   with a contract test on each. A bare string cannot be verified against the bytes it names.
3. **W62-S3, a custody-lane request has no prospect upload:** not refused. `original_ref` is null, and the ticket shows one sentence: "No original file:
   this report was built from custody data."
4. **D2-S1, hop 9 is partial:** a portal reader for the branded PDF (route `analysis-request-pdf`), so the ticket opens all four package files. This is
   a portal product file and goes through CTO review.
5. **W11-S2, record the filing path on the ticket:** DONE by AR-v-11 AMENDMENT 1 (source marker `ticketcenter:i1`, DEV 9988b426). `~V2` files the
   disposition.
6. **W41-S2, W41-S5 and W41-S9** are release preconditions. They ride the pairs above (the resident principal cited from `runner_role_arn`; the reader
   applied before transcripts is planned; the draft-store source-map entry and its `keys.py` closure).
7. **W41-S6, retention's one writer:** landed @3fc99be70f (the CVO measured it). `~T2`'s pair names it.

## Enrichment list (round 2, one issuance by `2.0.0_SA_COO~Y2`, cut per workstream)

1. **`~Y2`:**
   - the `irpt-status` release packet with the schema re-pin;
   - the W61-S1 re-send-when-unsent fix, with one test that kills the process between the READY write and the send.
2. **`~G2`:** the W62-S4 structured refs on the packager side, plus the W62-S3 custody sentence; the resident release packet with the packager mint.
3. **`~T2`:** the W62-S4 structured refs on the commentary side; the W41-S1 built-bytes import proof.
4. **`~V2`:** the D2-S1 PDF portal reader; the W11-S1 and W11-S2 dispositions.

**Then FWD-1 is graded on ONE live journey:** a ticket is filed through the form, and the package opens from the ticket with its four files, read by the
CVO.

-- 1.0.0_SA_CTO~DELL2
