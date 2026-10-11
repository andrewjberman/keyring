# TCKT_VNEXT -- round 2 L10 slug to `1.0.0_SA_CTO~DELL2`

**From:** `2.0.0_SA_COO~V2` (issuer), 2026-10-11 ~10:1xZ. **One slug, round 2** (the thread rectangle of your analysis @bbba700c22,
plus the cells you ruled in mid-round: `R2-pg-1`, `R2-pk-1`, `R2-pk-2`).

## 1. Verdict

**FWD-1 is NOT REALIZED.** The CVO graded TO-RUN-R2-tr1 AC2 NOT MET (row TCKT_VNEXT-D2-S33). Three GOs were spent under the pair:
the first wrote nothing; the second was refused at the submission because the runner re-sent round 1's idempotency token; the third
was, on a code read, ACCEPTED at the submission and misread by the runner as a refusal, and no generation was seen after it. No run
read a finished report. Round 2 did repair and land the three breaks your analysis named, and it found four more on the way, three
of them in this issuer's own runner.

## 2. Measured at the slug (2026-10-11 ~10:0xZ)

| item | value | instrument |
|---|---|---|
| round-2 task orders, project tree | 7 of 7 complete | `round-close-check --round 2`: orders=7, proof_ok=7, verdict=MAY-CLOSE (it counts no judgment criterion: judgment=0) |
| applier orders (flat folder) | TO-APPLY-R2-rr2, TO-RUN-R2-tr1, TO-APPLY-R2-pk2: 3 of 3 complete | `<status>` of each face |
| judgment criteria | TO-APPLY-R2-rr2 AC2 MET (S26); TO-RUN-R2-tr1 AC2 NOT MET (S33); TO-APPLY-R2-pk2 AC2 at the CVO, ungraded | CVO rows; packet `ledger/L8_PACKET.R2_PK2.md` |
| `opal-ticket-api` live | CodeSha256 `t1EoiJRZ...`, 2026-10-11T09:47:09Z; deployed file `cf10e19e` | `get-function-configuration`; `reread_27.py` (downloads the package) |
| the firm clamp on 27 routes | `READ27 27/27` | `reread_27.py`, live |
| `irpt-status` live | `6idtFvAm...` at the last read (08:1xZ, run 3's precheck); not re-read at the slug | run 3's trace |
| portal DEV | `7bb81fa897` on origin at 05:0xZ; CI run 38113443256 success; not re-read at the slug | `ls-remote`, `gh run list` |
| the synthetic filer row | ABSENT after each run, by two reads each | the applier's reports |
| surprise channel | 59 investigation rows by the tool's count (44 parsed by this seat's own regex; the difference is not reconciled) | `round-close-check`; this seat's parse |
| open TCKT deploy ledgers, shared tree | not re-read after the last apply closed; the applier reports its ledger closed 5 of 5 | msg 4642 |

## 3. What round 2 landed

| cell | state | evidence |
|---|---|---|
| `R2-rr-1` + `R2-rr-2` the report route refuses a malformed request id | LIVE since 04:19Z; AC2 MET | S26; live arms never exercised (no run reached hop (f)) |
| `R2-pg-1` the ticket's Open report opens the finished report | on portal DEV `7bb81fa897`, CI green | CTO approval msg 4118; looked at with fixtures; never rendered against a live report |
| `R2-ts-1` no ticket test can reach real SES or the users table | merged | 161 tests pass on the merged tree |
| `R2-pk-1` + `R2-pk-2` the package route's 409s carry codes; no answer hands the packager the ticket | LIVE since 09:47Z; AC2 at the CVO | packet R2_PK2; live arms not exercised; no deployed caller exists |
| `R2-rn-1` the runner | merged @8838ec4313 after SIX amendments; 11 checks, 50 tests | see section 4 |
| `R2-tr-1` the thread re-run | NOT MET | `R2_RUN/R2_TR1_RUN2_RESULT.md`, `R2_RUN/R2_TR1_RUN3_RESULT.md` |
| `R2-cw-1` Andrew's crawl | NOT RUN: pair signed (@532566cb3f, @4542edc8b5), PARKED by this seat on Andrew's later word "I will deal with later"; the question is at your terminal | open call `-fbb1` stays open |

## 4. This issuer's own defects in round 2 (so the analysis can weigh the process, not only the product)

1. The runner order told the worker to keep round 1's token, cleanup and trace code. Four amendments undid that: a 2-hour token and
   a row deleted before expiry; a trace written into round 1's files; a zero-call read on a dead API field.
2. The runner re-sent round 1's idempotency token (run 2's refusal).
3. The order's rule "a non-empty reason means refused" is wrong for the submission answer (run 3's misreading). The trace kept no
   body, so even that is a code read.
4. The portal candidate was cut from a stale local `DEV` ref; the push was refused by the fabric manager, correctly.
5. The precheck's allow-list of ticket builds was not updated for the build this round deployed (run 1's stop).
6. The package apply order named a Lambda as the packager's host (its first stop).
Each was caught by a gate, a reviewer or an applier's STOP before it reached a wrong live state. None was caught by this seat first.

## 5. BLOCKING and ARMED rows since the round-1 slug, dispositioned

| row | class / hazard | disposition |
|---|---|---|
| D2-W8-S3 the worker could not write the refusal table | BLOCKING / INERT | CLOSED: transcribed to `R2_RUN/REPORT_READ_REFUSALS.md`, PROPOSED |
| D2-W8-S6 the runner wrote into round 1's trace files | OBS / **ARMED** | DISARMED: `--trace-out` is required (TO-R2-rn1 AMENDMENT 3, merged @daad38c5e2); runs 2 and 3 wrote their own files |
| D2-S28 the precheck's hand-kept build list | BLOCKING / INERT | CLOSED for round 2 (both deployed builds admitted on measured reads); its remedy is list item 5 |
| D2-S34 the package route's caller could not be read | BLOCKING / INERT | CLOSED by CTO ruling msg 4587 and the read of the resident (msg 4594); the applier corrected its own denominator |
| the rest (S22-S27, S29-S33, W8-S1/S2/S4/S5/S7-S10, W11-S1-S3) | OBS / INERT | RECORD, or carried below (S24 landed as R2-pg-1; S27 with Andrew via you; S29-S31 closed by your half's amendments; W11-S3 and S3/S4 with 2.0.0_SA_COO~Y2) |

No ARMED row of this project is open. `2.0.0_SA_COO~G2` holds the ARMED row on the generation dead-letter queue (IRPT_YCDGEN).

## 6. Enrichment list for round 3 (thread-breaking first)

1. **The fourth run**, under a new pair, after (i) the resident release carrying the `ticket_id` schema is live and (ii) one dead
   letter has been read (your ruling @c7a257c031 and its CORRECTION). The runner at `8838ec4313` (blob `3199fd8a`) now reads an
   accepted submission by state and identity and keeps the answer's keys.
2. **Run 3's accepted request.** One request was accepted under `49financial` whose `REQ-` id this project does not hold (CTO
   condition 5 unmet). `2.0.0_SA_COO~G2`'s next batch reads it; the id and its job state belong in this project's record.
3. **The live arms nobody has exercised:** the report route's id check (both arms), the package route's codes and its ticket-free
   answers, and the Open report page against a real report, including its waiting state.
4. **Andrew's crawl** (`R2-cw-1`), on his word.
5. **The precheck reads the source map's recorded hash** instead of a typed list (rows D2-S28, D2-S25).
6. `round-close-check` counts no judgment criterion on orders held in an applier's flat folder (row D2-S23; it read judgment=0 for a
   round with three).
7. Carried from round 1, untouched in round 2: FWD-3's one-account check; FWD-6 "same ticket"; FWD-2's other-firm refusal; FWD-5's
   queue type and age; the read grant that reaches dell1 and the rotation runbook; a recipient digest on the client mail log line.
8. Inputs only Andrew or Alyssa give, none gating: the default advisory fee; who is on the ticket distribution list (row D2-S27);
   Alyssa's one filing on DEV.

## 7. Asked of the CTO

The round-3 analysis. This seat cuts round 3 in one issuance the tick it arrives; item 1 waits on its two conditions and is cut
then.
