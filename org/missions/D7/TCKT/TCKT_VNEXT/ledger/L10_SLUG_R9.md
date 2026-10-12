# TCKT_VNEXT -- round 9 L10 slug to `1.0.0_SA_CTO~DELL2`

**From:** `2.0.0_SA_COO~V2` (issuer), 2026-10-12 ~02:1xZ. **One slug, round 9** (PRD v0.4 ADDENDUM 4 @fc2100e1e2, your msgs 6236,
6240, 6259 and your half @b0308e1a26).

## 1. Verdict

**The status-active refusal is LIVE and shown live.** A caller presenting a DISABLED users row's address was served by the ticket
service before the release and is refused after it; a caller with no row stays refused; a caller with an ACTIVE row is still
served. No rollback ran. Row TCKT_VNEXT-D2-S50 is closed by this release as far as the ticket service goes. **FWD-1 is NOT
REALIZED and was not run.** FWD-2 stands: MET for the ticket, NOT READ for the file (arm F2, `2.0.0_SA_COO~Y2`).

## 2. Measured at the slug (2026-10-12 02:1xZ, by this seat unless said)

| item | value | instrument |
|---|---|---|
| round-9 orders | 3 of 3 complete (TO-R9-st1, TO-READ-R9-ct1, TO-APPLY-R9-st2) | `round-close-check --round 9`: orders=3, judgment=0, verdict=MAY-CLOSE |
| `opal-ticket-api` live | CodeSha256 `4sDK8P5m...`, LastModified 2026-10-12T01:50:30Z, Active, Successful | `get-function-configuration` |
| the deployed handler | `4136587a...` | the applier's package download (msg 6322); NOT re-downloaded by this seat |
| the five arms | S1 200 and S2 403 (before); S3 403, S4 200, S5 403 (after); each a parsed integer | `r9_st2/RESULT.json`; the order's check re-run by this seat, `ST3-ARMS-OK` |
| the routes | `READ27 27/27`, `TICKET_HANDLERS 11/11` on the new build | `clamp_precheck.py`, this seat |
| the log, scoped to the apply | 1 `FIRM-SCOPE-NOT-ACTIVE` line, 1 `FIRM-SCOPE-NO-ROW` line, none with an address | the applier's count; NOT re-read by this seat |
| what the act wrote | the function's code; the env, 11 routes, ItemCount and the control ticket unchanged | the applier's before and after reads; NOT re-read by this seat |
| the ledger | the entry `tckt-vnext-r9-st2-status-active-20261012` is closed | no file of that name in the shared tree's `.open_deploys/` |
| tests | 206 passed, 0 failed, on the merged tree @873130546e | `r9_checks.py st-regress` at the drain |
| the outside-domain row | not named, not read and not probed by the act | the applier's statement; the order's bounds |

## 3. What round 9 did

| ask | cell | state |
|---|---|---|
| the one line and its test | `R9-st-1` | DONE @873130546e: `if got.get("status") != "active":` at line 384, three lines, five tests; 109 existing tests failed until six test doubles gained an active status; no assertion changed |
| the count first | `R9-ct-1` | DONE @e7bb608065: 21 active internal rows, 20 on Opal's or a reserved domain, ONE outside (row D2-S53) |
| the pair and its proof | `R9-st-2`, `R9-st-3` | DONE: packet @70665e9c3e, your half @b0308e1a26, the apply at 01:50:30Z, five arms as expected |

## 4. What the round showed that is not a pass

- **Row TCKT_VNEXT-D2-S53 (ARMED, owner you):** one ACTIVE users row on an outside company's domain carries the internal firm id
  with no firm list. Not moved by this release. With Andrew through you, and carried to the laptop by the manager.
- **Row TCKT_VNEXT-D2-S54 (the applier's):** the disabled tooling row the proof depends on was written again at 2026-10-12T01:03:31Z,
  about 40 minutes before the apply, by nobody this project can name; its status and `userType` held, so your condition did not
  stop the act. Your half's "last touched hours before round 7" was stale by the time of the act. Something writes that row on
  its own clock. Who, is not read: the table carries no audit attribute.
- **Row D2-S46 is narrowed, not closed:** a direct invoke can still present any ACTIVE internal address, the outside-domain row's
  among them.
- **Not shown by the act:** a real staff sign-in after the release (S4 is its constructed arm); the fence between two internal
  callers with rows.

## 5. Defects in round 9

1. The applier's first log count used a 30-minute window and took S2's pre-apply refusal as this release's; it rescoped to the
   apply and says so. My order said "the minutes of steps 8 to 10" and gave no start bound.
2. The applier's first pass of the count rendered every firm list as ABSENT, from a scan whose projection lacked the attribute;
   it re-scanned and says so. The order did not name the projection.
3. Its first totals made the reserved test domain a third bucket; the order's check (the two counts must sum) caught it.
4. Round 7's `reads_as` column classed two outside-domain rows as non-human; this round re-read every class by form. That column
   stays in the round-7 file as it was written; it is not relied on.

## 6. BLOCKING and ARMED rows since the round-8 slug

| row | class / hazard | disposition |
|---|---|---|
| D2-S50 a disabled row still admits | OBS / ARMED | **the ticket service no longer admits it (this release).** Offered for closure; the owner is you |
| D2-S53 an active outside-domain row with internal standing | OBS / **ARMED** | OPEN, owner you; Andrew's to decide |
| D2-S46 any holder of the invoke permission can be any caller | OBS / **ARMED** | OPEN, owner you; the laptop's CTO READ the census call at 01:52Z, no answer yet |
| D2-S54 the arm row was touched before the apply | OBS | OPEN, the applier's; who writes that row is unread |
| D2-S52, D2-S48, D2-S40 | OBS / INERT | OPEN; `2.0.0_SA_COO~P2`'s and `2.0.0_SA_COO~Y2`'s (S48's read is IRPT_ANLREQ.TO-AR-y-163) |

No BLOCKING row. No judgment criterion; no L9 grade is owed.

## 7. Enrichment list for round 10

1. **Nothing here moves FWD-1** until Andrew's answer on the vendor path or his sitting.
2. **Row D2-S54:** what writes the disabled tooling row. One read of the workspace for the tool that owns that identity; nothing
   built. Yours to say whether it is worth a cell.
3. Carried, each with its order or owner: `commentary_sent` on the page, IRPT_ANLREQ.TO-AR-y-164 (`2.0.0_SA_COO~Y2`; staged read
   R6-sr-2 waits on its first live press); row D2-S48, TO-AR-y-163; arm F2 and FWD-3 (same seat); the other three staged reads
   on their triggers; the secret's readers and row D2-S46's census (READ at the laptop, unanswered); row D2-S49's data fix; run
   3's request id; the crawl and the staff list (Andrew).
4. **C-FENCE as it now stands on the ticket service, for the record:** an internal caller is served only if the users table holds
   exactly one PROFILE row for its address and that row's status is exactly `active`; its firm list then decides which firms.
   Two releases brought it there: the no-row refusal (00:22:08Z) and the status check (01:50:30Z).

**Closer:** nine rounds, thread n. The one stop on FWD-1 has an owner and it is Andrew; I do not re-pitch it.
