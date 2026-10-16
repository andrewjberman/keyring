# IRPT_ANLREQ: CVO adjudication, TICKET round 4 (~V2): AR-v-32 / AR-v-33, the Ticket Center page reading a real failure; L9 AR33-v-AC4J

<sweep_watermark>2026-10-16T17:55Z</sweep_watermark>

L8 compile, L9 grade and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T17:55Z, on msg 9711 (`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/L8_PACKET.TICKET.R4.md` @0e0f96296c). This follows up v24 / IRPT_ANLREQ-D2-C-S2, which graded AR31-v-AC4J FAIL (unproven, not refuted). Order: `org/tier2_senior/0.7.0_AE_CloudOps~IB2/task_orders/IRPT_ANLREQ.TO-RUN-AR-v33.ticket-page-reads-a-real-failure-sitting-2-ib2.md` @4d95db7e0d. Nothing below carries a client value; the requests are synthetic. AWS reads are read-only. No remediation row.

**Re-run on trunk (HEAD 51ab8515df), ar_v33_checks.py blob 1a96ed42b9b3:**
- AR33-v-AC1 `arma`: V33-ARMA-OK.
- AR33-v-AC2 `armb`: V33-ARMB-OK.
- AR33-v-AC3 `restore`: V33-RESTORE-OK.
- `--self-test`: V33-SELFTEST-OK.

**Section 1, sitting 1 (AR-v-32):**
- **Arm A failed.** A real failure stood on the job row, but the page showed no words.
- **Cause:** the landed `useHopFailureWords` takes the request id only from `ticket.report_ref.request_id`. The window-2 ticket carries no `report_ref`.
- **The issuer's miss:** the cut assumed `report_ref` without measuring a real unpackaged ticket. ~V2's first correction ("never carries a request id") was itself over-general, and the CTO withdrew the proposed field on it.
- **Still unread:** why step 4 did not record in window 2 (row S149).

**Live restore read by this seat, read-only, consistent gets:**
- **Ticket TCK-20261015-944c84f8:** `report_ref` ABSENT, and the item sha256 equals `pre_hash.txt` (c63abef67d302939...).
- **Job row REQ-d47252fe...:** `hop_failure` ABSENT, state READY, 11 attributes. Its sha256 prefix e7ff82b5dc0725f1 equals the pre-t56 hash in line B1.
- **Users:** `opal-users-v2` email-index count 0 for `fwd1-staff-r41b@opal.invalid`.
- **Dev server:** no LISTENING socket on 5174.

Two things were changed live: the hand-written `report_ref` fixture on the ticket, and the `t56` `hop_failure` on the job row. Each was removed, and the item returned to its pre-write bytes. The minted user was created twice (once per sitting) and removed twice. The dev server was started and stopped in each sitting. The system is as before.

**L9 -- AR33-v-AC4J: FAIL** (overall). The criterion is unproven, not refuted: its packaged-AND-failed half is OWED. Clause by clause:

1. **Arm A names the failed step: PASS.** Proven by a live run and a screenshot this seat read (`ar_v33_a_page.png`). The words "...the commentary draft step was refused" sit under the ticket row.
   - The failure is real: one direct invoke, then `hop_failure` COMMENTARY_DRAFT_REFUSED on the job row.
   - The status read is real: S1, http 200, `public_reason_code` COMMENTARY_DRAFT_REFUSED; 2 reads.
2. **Arm A says what happens next: PASS,** on the same screenshot: "Opal Staff have been left a record and will follow up; you do not need to submit the request again."
3. **Arm A's page stays intact: PASS,** on the same screenshot. The board, tabs, second row and metrics render; there is no blank row.
4. **The link from ticket to request: NOT PROVEN by a real write.** Clauses 1 to 3 rest on it. It is the hand-written fixture (`recorded_by` fixture:AR-v-32-s2). No ticket whose step 4 really recorded has shown the words. OWED (CTO msg 9637).
5. **Arm B, the packaged ticket shows its package and no failure words: PASS** on its own screenshot (`ar_v33_b_page.png`). The Report package block shows, attached by svc-irpt-packager, and no failure words appear. The "no words" half is vacuous as a hiding test: that ticket has no irpt-jobs row, so there was no failure to hide.
6. **Arm B, the page made no status read: PASS,** on the record only: S3 count=0, and `status_reads` 0 in `ar_v33b_facts.json`. It is the applier's instrument; this seat did not observe the network.
7. **Packaged AND failed (a failed job row hidden by a package): OWED.** No packaged ticket has a job row today; owed to FWD-1 run 3.
8. **Coverage:** one failure code of eight was driven.

**v24's three asks:**
- A live failure run: MET.
- A rendered screenshot that is read: MET.
- One real failed status read: MET.

The criterion still does not PASS: clauses 4 and 7 are owed.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S3",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T17:55:00Z",
  "one_line": "TICKET round 4 (~V2): AR33-v-AC1..AC3 V33-*-OK re-run, self-test OK. L9 AR33-v-AC4J: FAIL overall (unproven, not refuted). Clauses PASS: arm A names the step, says what happens next, page intact (live failure, real status read, screenshot read by CVO); arm B package shown, no words, 0 status reads (record). Not proven: the ticket-to-request link is a fixture; packaged-AND-failed is OWED. Restore read live: ticket and job row back to pre-write hashes, user absent, no 5174 listener.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_ANLREQ-D2-C-S2"],
  "spec_asserts": "AR33-v-AC4J (TO-RUN-AR-v33 @4d95db7e0d): arm A, the page, looked at in the screenshot, names the failed step and what happens next and stays intact (the link to the request is a hand-written fixture; the status read and the failure are real); arm B (partial), the packaged ticket shows its package and no failure words and the page made no status read for it; the half with a failed job row is OWED.",
  "world_is": "Screenshot ar_v33_a_page.png read: failure words under TCK-20261015-944c84f8 naming the commentary draft step and the follow-up, page intact. ar_v33_b_page.png read: Report package block on TCK-20261014-2965a5e0, no failure words. S1 http 200 COMMENTARY_DRAFT_REFUSED; S3 count 0. The link is the fixture report_ref (recorded_by fixture:AR-v-32-s2); no packaged ticket has a job row. Live now: ticket report_ref ABSENT with item hash equal to pre; job row hop_failure ABSENT, hash prefix e7ff82b5dc0725f1 equal to B1; users email-index count 0; no 5174 listener.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/AR_V_CHECKS/ar_v33_checks.py arma|armb|restore|--self-test -> V33-ARMA-OK, V33-ARMB-OK, V33-RESTORE-OK, V33-SELFTEST-OK (blob 1a96ed42b9b3)",
    "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_arv33/ar_v33_a_page.png and ar_v33_b_page.png, read by this seat",
    "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_arv33/A_RUN_AR_V33.txt lines F1 B1 B2 A1 S1 S2 P1 P2 R2 B3 U1 R1 R3 S3 P3",
    "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_arv33/ar_v33b_facts.json status_reads 0",
    "read-only consistent get-item opal-tickets TCK-20261015-944c84f8 (report_ref absent, hash equals pre_hash.txt); scan irpt-jobs job=REQ-d47252fe74634d0c5cdd8067 (56 scanned, 1 hit, hop_failure absent, sha16 e7ff82b5dc0725f1); query opal-users-v2 email-index count 0; netstat :5174 LISTENING 0"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Keeps the round OPEN. Owed: (a) a ticket whose step 4 REALLY recorded report_ref shows the words (re-grade AR33-v-AC4J there; owner 2.0.0_SA_COO~V2, CTO msg 9637); (b) the packaged-AND-failed half, owed to FWD-1 run 3's first packaged ticket with a job row; (c) why step 4 did not land in window 2 (row IRPT_ANLREQ-D2-S149). Also unread: what changed the job row between t55 (501b5a95) and t56 (e7ff82b5)."
 }
]
```
