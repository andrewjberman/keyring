# IRPT_BCKEND round 77, workstream ~Y -- L8 COMPILE (release 6b: the custody factory live)

**By** `2.0.0_SA_COO~Y2` **for** `3.0.0_SA_CVO`, 2026-10-09 ~15:0xZ. Risk WORLD. `round-close-check.py --round 77 --workstream ~Y`: MAY-CLOSE.

## TO-APPLY-Y77 (cell `IB-ya-771`): COMPLETE @6a8e64ed12, proof VALID

**Re-cut from release 6 to release 6b** (AMENDMENT 2, CTO msg 2833): IB-pr-390 went live via IB-pr-395 at 07:49Z as `ZA0QJ5Wt`. Release 6's
signed `V6EiBNcJ` would have reverted 390's served.py.

**6b:**
- pin `66207bce7d`, built `tdpterTM`;
- rollback `ZA0QJ5Wt`;
- census against live: 3 members, all IRPT_ANLREQ `AR-y-11`;
- the custody-factory policy added (11 ARNs);
- the pandas layer already live through 390.

**LIVE** `tdpterTM` at 09:32Z; both layers intact; policy 11 ARNs; re-plan 0; census `failed {}`; ledger CLOSED 5/5.

**Reads:**
- 3: the custody path reached the factory, and a typed `ACCEPTED_CUSTODY_SELECTION_REQUIRED` came from its own validation, with no AccessDenied and no
  ImportError; 0 custody_reports written.
- 4: the prospect path holds.
- 5b: a malformed `ticket_id` refuses `TICKET_REFERENCE`.
- 5a: the `ticket_id` on the STORED record, measured by the laptop (`4_record` TRUE, IRPT_ANLREQ Y1 laptop result sha256 13aa6be20e54).

**Grades** (`checks/r77/y77_cells.py`, AMENDMENTS 1-4: release-6b values, an adapter to the applier's read file, read 5a through the laptop, branch B only on a
FAILED read): Y77-1-AC1, AC2 and AC3 PASS.

## Surfaced and ruled this round

- **Row `D2-S35`:** disposes `D2-S31`.
- **Row `D2-S51`:** the Y75 cleanup list deleted a CONTENT-ADDRESSED retention row shared by Y77's three synthetic requests. Test-only; no restore. Future
  lists walk the retention dependency tree first.
- **Row `D2-S52`** (the applier's): the proof schema's prose type blocked every flip fleet-wide; the CTO fixed it @023be3c879.
- **Cell ids:** `APPLY-Y75`/`APPLY-Y77` became `IB-ya-751`/`IB-ya-771` @7d4318cd3e (row `D2-S21` fired at the flip).

## Open, carried

- The S3 deletes of Y77 reads 4-5's synthetic objects (and the three broken requests): a list built after a dependency walk, for Andrew's word.
- IRPT_ANLREQ release 1 rev 4 (the reader registers the research revision, so the Opal 49F report is served) is in flight under IRPT_ANLREQ.
