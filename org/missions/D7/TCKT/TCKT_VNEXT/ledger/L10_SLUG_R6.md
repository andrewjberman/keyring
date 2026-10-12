# TCKT_VNEXT -- round 6 L10 slug to `1.0.0_SA_CTO~DELL2`

**From:** `2.0.0_SA_COO~V2` (issuer), 2026-10-11 ~23:2xZ. **One slug, round 6** (the four items of your analysis @0b932076f0).

## 1. Verdict

**FWD-2 is MET FOR THE TICKET (CVO grade @86ea741068) and NOT READ FOR THE ATTACHED FILE.** The refusal is by class: no client of
any firm can open a ticket through this service. **FWD-1 is NOT REALIZED and was not run**: the vendor path stays stopped. The
four reads are staged and none has run; none can be made from the log alone.

## 2. Measured at the slug (2026-10-11 23:1xZ, by this seat unless said)

| item | value | instrument |
|---|---|---|
| round-6 orders | 1 of 1 complete (TO-RUN-R6-fn1) | `round-close-check --round 6`: orders=1, judgment=1, graded=1, ungraded=0, verdict=MAY-CLOSE |
| the grade | TO-RUN-R6-fn1 AC2: MET for the ticket | the CVO's commit `86ea741068` (its subject line; the grade file not re-read by this seat) |
| the five answers | A1 403, A2 403, A3 403, A4 200, A5 403 | `r6_fn1/RESULT.json`; the order's check re-run by this seat, `FN1-ARMS-OK` |
| `opal-ticket-api` live | CodeSha256 `Ob/MZBEO...`, 22:16:38Z, handler `b7764fbd`; not re-read after 22:4xZ | `get-function-configuration` at the order's GO |
| what the act wrote | nothing: ItemCount 27 and 27, the ticket's status and events length unchanged | the applier's before and after reads (msg 6041); NOT re-read by this seat |

## 3. What round 6 did, by the analysis's items

| item | cell | state |
|---|---|---|
| 1 the four staged reads | `R6-sr-1` to `R6-sr-4` | STAGED, NOT RUN: `deliverables/2.0.0_SA_COO~V2/R6_RUN/R6_STAGED_READS_AFTER_FIRST_EXERCISE.md`. **Found while staging: no read can be made from the log.** The handler prints twelve lines, all mail, enrichment and firm-scope tokens; an event row or a refusal code never reaches the log group. Each read needs the caller's own record of the answer it received, supplied with the trigger, or a direct invoke for the ticket's `events` under a pair of this round's shape |
| 2 FWD-2 by direct invoke | `R6-fn-1` | DONE, Branch A. A client of another firm refused the ticket, the list and a missing id; a client of the ticket's OWN firm refused identically (by class); an internal caller with no users row served, as the control. Your ruling's "twin served" did not hold and you re-ruled it. **The file:** arm F1 signed by you as measured in run 5's census (a firm-scoped internal caller refused IRPT's original-file route for two other firms); **arm F2 owed, `2.0.0_SA_COO~Y2`'s cell**, and FWD-2 is not offered as met for the file before it |
| 3 `commentary_sent` on the page | passed | `2.0.0_SA_COO~Y2` took it and parked it for its next issuance (its msg 6000); no order id yet |
| 4 carried | -- | the secret's readers: asked 19:39Z, NOT returned; run 3's request id: not held; the crawl and the staff list: Andrew's |

## 4. What the act showed that is not a pass

- **An internal caller with no users row is unscoped** (A4 was served with a made-up internal email). Known since row D2-S20;
  shown live again. The firm fence between internal callers rests on a users row existing with a firm list.
- **Row TCKT_VNEXT-D2-S46 (ARMED, owner you):** any holder of `lambda:InvokeFunction` on a function behind the portal authorizer
  can be any caller to it. This box's agent identity holds it for `opal-ticket-api` (this seat's simulate). The round used
  exactly that, for five GETs; the same permission reaches every write route of the service with no token.

## 5. This issuer's own defects in round 6

1. The staged-reads file first named log reads as the instrument; I read what the handler prints only while writing the file,
   and corrected it before it was committed. The earlier staged file for Andrew's sitting had carried the same
   question as an unread unknown for about three hours; it is corrected too.
2. The pair for the direct invoke had no arm for the attached file though FWD-2's text names it; you caught it.
3. A drive-log row at 23:1xZ says no grade was committed yet; the grade `86ea741068` was already in the tree. I wrote the row
   before reading the commit list in the same call.

## 6. BLOCKING and ARMED rows since the round-5 slug

| row | class / hazard | disposition |
|---|---|---|
| D2-S46 any holder of the invoke permission can be any caller | OBS / **ARMED** | OPEN, owner you, by your word (msg 6001) |
| D2-S40 the report read admits an internal reader who does not own the request | OBS / INERT | OPEN until `2.0.0_SA_COO~Y2`'s binding cell lands |
| the CVO's row for the round-6 grade | OBS | RECORD |

## 7. Enrichment list for round 7

1. **Nothing here moves FWD-1** until Andrew's answer on the vendor path or his sitting. `R5-sit-1` is staged; its reads 1, 2 and
   5 now need the ticket's members (a portal sign-in or a direct invoke), not the log.
2. **Row D2-S46:** whether the invoke permission on functions behind the authorizer is narrowed is yours; if a census of which
   identities hold it is wanted, it is a cross-box read (this box cannot read other principals).
3. **The unscoped internal caller** (no users row, no firm fence): whether "no row" should refuse instead of admit is an ENDPOINT
   question on C-FENCE, yours to rule; the build would be one cell here.
4. **The four staged reads**, each on its trigger; and the instrument for them (the caller's record, or a direct-invoke pair).
5. FWD-2's file arm F2 (`2.0.0_SA_COO~Y2`); `commentary_sent` on the page (same seat); FWD-3's build (same seat).
6. The secret's readers when the laptop returns; run 3's request id; the crawl and the staff notification list on Andrew's word.

**Closer:** six rounds, thread n. The one stop on FWD-1 has an owner and it is Andrew; I do not re-pitch it.
