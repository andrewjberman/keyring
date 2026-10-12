# TCKT_VNEXT -- round 7 L10 slug to `1.0.0_SA_CTO~DELL2`

**From:** `2.0.0_SA_COO~V2` (issuer), 2026-10-12 ~00:4xZ. **One slug, round 7** (your analysis and PRD v0.4 ADDENDUM 3 @8bb81f8d6c).

## 1. Verdict

**The no-row refusal is LIVE and shown live.** An internal caller the users table does not know was served by the ticket service
before the release and is refused after it, on the ticket and on the list; a caller whose address has a row is still served.
No rollback ran. **FWD-1 is NOT REALIZED and was not run**: the vendor path stays stopped. FWD-2 stands where round 6 left it:
MET for the ticket, NOT READ for the file (arm F2, `2.0.0_SA_COO~Y2`).

## 2. Measured at the slug (2026-10-12 00:4xZ, by this seat unless said)

| item | value | instrument |
|---|---|---|
| round-7 orders | 4 of 4 complete (TO-R7-nr1, TO-R7-el1, TO-READ-R7-ct1, TO-APPLY-R7-nr2) | `round-close-check --round 7`: orders=4, judgment=0, proof_ok=4, verdict=MAY-CLOSE |
| `opal-ticket-api` live | CodeSha256 `lAt/vc4X...`, LastModified 2026-10-12T00:22:08Z, Active, Successful | `get-function-configuration` |
| the deployed handler | `f99a314b...` | the applier's package download (msg 6211); NOT re-downloaded by this seat |
| the four arms | N1 200 (before), N2 403, N3 200, N4 403 (after); refusal body one field, `error: firm scope lookup failed`, naming no ticket | `r7_nr2/RESULT.json` read by this seat; the order's check re-run, `NR3-ARMS-OK` |
| the routes | `READ27 27/27`, `TICKET_HANDLERS 11/11` on the new build | `clamp_precheck.py`, this seat |
| the log | 2 `FIRM-SCOPE-NO-ROW` lines, none with an address | the applier's count; NOT re-read by this seat |
| what the act wrote | the function's code; ItemCount 27 and 27; the control ticket unchanged; env and 11 routes unchanged | the applier's before and after reads; NOT re-read by this seat |
| the ledger | the entry `tckt-vnext-r7-nr2-no-row-refusal-20261012` is closed | no file of that name in the shared tree's `.open_deploys/` |
| tests | 201 passed, 0 failed, on the merged tree @09488abbb1 | `r7_checks.py nr-regress` at the drain |

## 3. What round 7 did, by the analysis's items

| item | cell | state |
|---|---|---|
| 1 the no-row refusal | `R7-nr-1` build, `R7-ct-1` count, `R7-nr-2` apply, `R7-nr-3` proof | DONE. Count: 30 internal addresses, 23 with one row, 0 with more, 7 with none, no person among the seven; the six old test identities read as you ruled (no code, last ticket event 2026-08-20 each) and need nothing. Pair: `deliverables/2.0.0_SA_COO~V2/R7_RUN/R7_NR2_DEPLOY_AND_PROOF_PACKET_20261011.md` @513f06c31b and your half @bec8e7a197 |
| 2 the empty firm list, a read | `R7-el-1` | DONE @1a47d695fb, claim INFERRED: `deliverables/0.9.0_WK_TCKT_VNEXT~26/EMPTY_FIRM_LIST_READ.json`. No row, no attribute and an empty list: the ticket service (before this release) and the investor-reporting INTERNAL reader read every firm; the investor-reporting SERVICE reader reads none. The literal `ALL`: refused by the investor-reporting internal reader, unrestricted for its service reader, an id matching nothing inside a ticket list. **The portal authorizer is not in this checkout: its three cells are NOT_READ** |
| 3 carried | -- | the four staged reads: none triggered; arm F2 and `commentary_sent` on the page: `2.0.0_SA_COO~Y2`; the secret's readers and the census for row D2-S46: the laptop, not returned; run 3's request id: not held; the crawl and the staff list: Andrew's |

## 4. What the round showed that is not a pass

- **Row TCKT_VNEXT-D2-S50 (ARMED, owner you):** the rule reads a row's EXISTENCE, not its status. Two disabled rows exist and
  both still admit by direct invoke; the twin arm N3 used one of them deliberately. Whether the portal sign-in already refuses a
  disabled user was not read.
- **Row TCKT_VNEXT-D2-S48 (INERT; you gave it to `2.0.0_SA_COO~Y2`):** the investor-reporting internal reader leaves a no-row
  caller unrestricted, by its own docstring. The two services now answer the same caller differently.
- **Row D2-S49 (the applier's):** one service-named address, classed INTERNAL by its firm, carries a firm list that is a STRING
  and is refused by the ticket service today, before and after this release. Not read in full by this seat.
- **An empty or absent firm list still reads every firm**, and 20 of the 23 rows are that shape. Stated in the addendum as not
  changed; item 2's read is the ground for ruling on it.
- **Not shown by the act:** the fence between two internal callers with rows; a real staff sign-in after the release (the organic
  case; N3 is its constructed arm).

## 5. Defects in round 7, this issuer's and the instrument's

1. I asked you which of the seven were live before reading where the workspace uses them; your answer was the read I should
   have made first. It cost one exchange.
2. The applier nearly rolled back a correct release: a shell capture took the whole invoke output where it wanted the status,
   compared unequal to 200, and its guard read N3 as refused. It caught this before acting and re-read the value. Its lesson, in
   its log: a rollback trigger is computed from a parsed value. My order named the trigger and not how to read it.
3. Row D2-S51 (the applier's): an unquoted hyphenated CloudWatch filter pattern returns zero silently; two false zeros preceded
   the log count.
4. `prd-signoff.py status` read the reviewer's half current on v0.4 before it was signed (the unfixed library; fixed on this box
   @df4b821efd during the round). The issuance rested on the reviewer's commit, by your rule.

## 6. BLOCKING and ARMED rows since the round-6 slug

| row | class / hazard | disposition |
|---|---|---|
| D2-S46 any holder of the invoke permission can be any caller | OBS / **ARMED** | OPEN, owner you; carried to the laptop's CTO by the manager; cited in this round's pair |
| D2-S50 a disabled row still admits | OBS / **ARMED** | OPEN, owner you, by your word (msg 6180) |
| D2-S48 the investor-reporting internal reader, no row | OBS / INERT | OPEN, `2.0.0_SA_COO~Y2`'s by your word |
| D2-S40 the report read admits an internal reader who does not own the request | OBS / INERT | OPEN until `2.0.0_SA_COO~Y2`'s binding cell lands |
| D2-S49, D2-S51 (the applier's) | OBS | RECORD; D2-S49's string firm list is a data fix on one users row, whose owner is not this project |

No BLOCKING row. No judgment criterion in the round, so no L9 grade is owed; the reviewer has no packet from this round.

## 7. Enrichment list for round 8

1. **Nothing here moves FWD-1** until Andrew's answer on the vendor path or his sitting.
2. **Row D2-S50:** whether the ticket service should also read the row's status is a CONTRACT question on C-FENCE, yours; the
   build would be one line and one test here, with the same pair shape. First the one read this box could not make: what the
   portal authorizer does with a disabled user.
3. **The empty firm list:** whether absent or empty should keep meaning every firm, on item 2's table; yours to rule.
4. The four staged reads on their triggers; FWD-2's arm F2, `commentary_sent` on the page and FWD-3 (`2.0.0_SA_COO~Y2`).
5. The secret's readers and row D2-S46's census when the laptop returns; run 3's request id; the crawl and the staff list on
   Andrew's word.

**Closer:** seven rounds, thread n. The one stop on FWD-1 has an owner and it is Andrew; I do not re-pitch it.
