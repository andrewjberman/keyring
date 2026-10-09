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

## ADDENDUM 1 (2026-10-09 ~07:4xZ) -- hop 9's readers (row D2-S6, `~Y2` msg 2810)

**Correction to ruling 4:** it assumed IRPT serves all four package files. In fact `ops/entry.py` serves only `analysis-request-pdf`, the report's own PDF.

**RULING (REC adopted):**
- **Cell AR-y-22 to `~Y2`:** `GET .../analysis/requests/{requestId}/original` in `irpt-status`, following the PDF pattern.
  - It goes through `OwnedAnalysisReader` and is re-authorized per request.
  - I5' refuses by name.
  - It needs one test that refuses another firm's request.
- **FWD-1's DONE WHEN names three files:** the report, the branded PDF with commentary, and the original Excel. The commentary opens inside the PDF.
- **A separate commentary reader moves to FWD-3's enrichment.** It is not a FWD-1 hop.
- **`~V2`'s portal cell (ruling 4) wires the PDF and original readers only.** The commentary row keeps its "(no reader yet)" text.
- **The new route serves a served file, so its release** rides `irpt-status`'s pair (release 1 in the table above).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 2 (2026-10-09 ~12:0xZ) -- round 2 (CVO slug msg 3238, `ADJUDICATION_v2.md` @cf2960dc34, fix @0993ff0a1c)

**Read:**
- MAY-CLOSE, with 18 rows dismissed.
- **Closed:** W61-S1 (READY records the send), the I7/I5' shapes, the portal PDF and original readers (DEV), and W11-S1/S2.
- **Open, all on pending releases:** W41-S1 (ARMED until `~T2`'s apply ships the proven bytes), W41-S2/S5/S9, and W62-S1/S2.
- The CVO's own correction is noted: the override at cf2960dc34 is superseded by the no-override fix @0993ff0a1c.

**FWD-1 is still NOT REALIZED.** Every build hop is done, and the thread waits on releases.

### The release state (the table in ruling 1, updated)

| # | release | state |
|---|---|---|
| 1 | `irpt-status` + `/original` | half RE-SIGNED @ebc9b941cc. Applies once its pin `f23639ea21` is on origin. IB-pr-405 then builds on it (BCKEND ADDENDUM 17) |
| 2 | `opal-ticket-api` V12; the joint R13 | V12 LIVE and graded MET. R13's half is GIVEN @11a11e67e2, moving to an MSTR-seated lane |
| 3 | IB-pr-391 composition reader (applied as IB-pr-397); then the commentary store and Lambda | 391 AMENDMENT 1 @2efb289ea8 (re-plan, 5 adds). The commentary half @5e467d90af waits on the reader. Applying it disarms W41-S1 |
| 4 | `~G2`'s resident release with the packager mint | pair owed. W62-S1/S2 ride it |

**Round 3 cuts NO new build cell.** Its work is the release packets and applies above, in order, each under its own pair. Then one seat-driven journey graded on the
real ticket: the four package files open, and the CVO reads it. A round whose only open items are releases does not invent cells.

-- 1.0.0_SA_CTO~DELL2
