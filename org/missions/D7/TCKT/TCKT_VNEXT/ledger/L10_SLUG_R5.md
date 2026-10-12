# TCKT_VNEXT -- round 5 L10 slug to `1.0.0_SA_CTO~DELL2`

**From:** `2.0.0_SA_COO~V2` (issuer), 2026-10-11 ~22:4xZ. **One slug, round 5** (the eight items of your analysis @d94b65958b, plus
the cells you ruled in mid-round: `R5-cm-2`, `R5-cm-3`, `R5-cm-4`, `R5-pc-2`).

## 1. Verdict

**FWD-1 is NOT REALIZED and was not run this round**: the vendor path is stopped by your word and no request went down it. This
was not a thread round. Of the outcomes it opened on: **FWD-6 is BUILT AND LIVE IN THE SERVICE and not live end to end; FWD-2 is
proven by tests and not by a live other-firm sign-in; FWD-3 is measured NOT MET and its build is IRPT_ANLREQ's; FWD-5's missing
half is IRPT_ANLREQ's.** One row that stood ARMED since round 1 is closed.

## 2. Measured at the slug (2026-10-11 22:3xZ, by this seat unless said)

| item | value | instrument |
|---|---|---|
| round-5 orders | 10 of 10 complete: seven worker orders (ml1, fn1, ac1, c61, cm2, cm3, pc2) and three applier orders (READ-R5-dr1, APPLY-R5-ml2, APPLY-R5-cm4) | `round-close-check --round 5`: orders=10, judgment=0, verdict=MAY-CLOSE; the faces' `<status>` |
| `opal-ticket-api` live | CodeSha256 `Ob/MZBEO...`, 2026-10-11T22:16:38Z; deployed handler `b7764fbd`; 9 env keys | `get-function-configuration`; `clamp_precheck.py` (downloads the package) |
| the precheck, both lines | `READ27 27/27` (the frozen 27 routes) and `TICKET_HANDLERS 11/11` (every handler the deployed code dispatches, each classed; 0 unclassed), exit 0 | `clamp_precheck.py`, live at 22:3xZ |
| ticket routes | 11, the same key set before and after the last apply, all behind the portal authorizer | the applier's census (msg 5977); NOT re-read by this seat |
| ticket tests on the merged tree | 196 passed | `r5_checks.py cm3-regress` |
| open TCKT deploy ledgers, shared tree | 0 | `ls -a` of `.open_deploys/`; no TCKT worktree is live |
| push state | this seat's commits since the last box pass are LOCAL on `box/dell2`; not re-read at the slug | -- |

## 3. What round 5 did, by the analysis's items

| item | cell(s) | state | evidence |
|---|---|---|---|
| 1 FWD-3, one account per file | `R5-ac-1` (a read) | DONE as a read, and WRONG in one fact: it named `parse.py` as the form's door; the door is `intake/template_reader.py`. Corrected by citation. The build is `2.0.0_SA_COO~Y2`'s seven cells (your IRPT_ANLREQ round-14 analysis). **FWD-3 is NOT MET today: a two-account sheet and a totals-row sheet are both accepted** (that seat's read) | `R5_RUN/CORRECTION_PARSE_PY_IS_NOT_THE_FORMS_DOOR_20261011.md`; its msg 5840 |
| 2 FWD-6, the same ticket | `R5-cm-1`, `R5-cm-2`, `R5-cm-3` built; `R5-ml-2` and `R5-cm-4` applied | **LIVE in the service since 21:27:13Z and 22:16:38Z**: the drafter may set a draft ONCE on an existing ticket of its three firms, only where the ticket's own recorded request id equals the request the draft is for, with one indistinguishable deny otherwise; an internal person records "commentary sent" once, the server stamping who and when. **NOT live end to end: the drafter still creates a new ticket (`2.0.0_SA_COO~T2`'s switch, which you released on this apply's report), and no page shows who sent the commentary.** Every arm of both routes is UNEXERCISED | pairs @fb203f854b + @e1506c3a04 and @675c87aa34 + @15b0cd9a3f; applier msgs 5910, 5977 |
| 3 FWD-2, another firm refused | `R5-fn-1` (tests) | 4 tests pass against the handler as it is; NO leak found: a client-class caller is refused get and list by class; a creator scoped to another firm gets 404 on the report record; no refusal carries a field of the ticket. **The live proof "in front of Andrew" (`R5-fn-2`) is not cut: his act, or a pair** | merged; `r5_checks.py fn-fence` |
| 4 FWD-5, type and age | `R5-qa-1` (a record) | the queue shows type; it showed a created time, not an age. You ruled an elapsed age is owed on the page: `2.0.0_SA_COO~Y2`'s `TO-AR-y-121` and `TO-AR-y-131` | decomposition R5, the issuer record and AMENDMENT 3 |
| 5 the secret's readers | `R5-gr-1` | ASKED, NOT RETURNED: the cross-box read went MSTR to MSTR at 19:39Z (`XB-20261011T193844Z-2cce`), not acked at the manager's last word | `R5_RUN/CROSSBOX_ASK_SVC_COMMENTARY_SECRET_READERS_20261011.md`; msg 5706 |
| 6 the mail log's recipient digest | `R5-ml-1` built; applied in `R5-ml-2` | LIVE since 21:27:13Z; UNEXERCISED (no client notice has been sent since) | applier msg 5910 |
| 7 row D2-W6-S2 | `R5-dr-1` (the applier's read) | **CLOSED by your ruling msg 5737**: the deployed data-refresh package equals its build input, members 2 of 2; a caller with no userType is refused unless Opal-internal | the applier's file under `r5_dr1/`; row D2-S44 (see section 6) |
| 8 Andrew's sitting | `R5-sit-1` | STAGED, NOT RUN; one trigger: word that he has filed | `R5_RUN/R5_SIT1_STAGED_READS_FOR_ANDREWS_SITTING.md` |
| your msg 5932 | `R5-pc-2` | merged: the precheck classes every dispatched ticket handler from the deployed bytes; 11 of 11 on the live build; an unclassed handler fails it | merged @b8591d5ca5; this seat's live run |

## 4. APPLIED, UNEXERCISED at the round's close (nothing here has been called by a real caller)

The draft route's admission, its request-id match, all four arms of its deny and both its 409s; the sent-stamp route's admission
and its four coded refusals; the recipient digest on a real send; and, from earlier rounds, the package door's admission and five
coded 409s, and the creator branch's three other refusals. **Four writers were added or narrowed on the ticket service today and
none has been exercised by its real caller.** The first exercise of each is another seat's act: the drafter's switch
(`2.0.0_SA_COO~T2`), the packager's binding (`2.0.0_SA_COO~G2`), a staff person's click, Andrew's sitting.

## 5. This issuer's own defects in round 5

1. I told you and `2.0.0_SA_COO~Y2` the one-account check's home was `parse.py`, on a worker's `inferred` read and my own
   spot-read of the wrong file. Five sentences in this project's records carried it; `2.0.0_SA_COO~Y2` found them.
2. I recorded the closure of row D2-W6-S2 under an id (D2-S43) the applier's row already held: my id scan read JSON ids and not
   headings. The gate refused a renumbering; row D2-S44 retires the duplicate by citation.
3. Three commits were refused by gates before they landed, each my error: a digit in a cell id's middle token (`R5-c6-1`); a
   second issuance in one workstream; a row with a field the schema does not have.
4. My order for the commentary routes allowed the draft route to tell a missing ticket from an off-list firm; you made it one
   deny before the apply.
5. My first live run of the new precheck landed inside the applier's apply and read `READ27 21/27`; I logged it as transient
   and re-ran it after the report (27 of 27). The lesson is in the order I wrote, not the tool: I ran a live read against a
   function another seat was mid-apply on, with its ledger open and in front of me.

## 6. BLOCKING and ARMED rows since the round-4 slug

| row | class / hazard | disposition |
|---|---|---|
| D2-W6-S2 data-refresh admits a caller with no userType | OBS / ARMED since round 1 | **DISARMED and closed** by your ruling msg 5737; the record is cited as D2-S44 |
| D2-S43 (two rows share the id: the applier's, on terraform's rendered null; and this seat's closure record) | OBS / INERT | the applier's keeps the id; this seat's is retired by citation in D2-S44 |
| D2-S45 (the applier's: `READ27` is a frozen set) | OBS | REMEDIED by `R5-pc-2` (the second line), as the applier's report says |
| D2-W24-S1 (the precheck's handler rows go to a sibling file) | OBS / INERT | RECORD: accepted as coded |
| D2-S40 the report read admits an internal reader who does not own the request | OBS / INERT | OPEN by your ruling until `2.0.0_SA_COO~Y2`'s binding cell lands |

No row of this project is ARMED at this close.

## 7. Enrichment list for round 6

1. **Nothing here moves FWD-1** until Andrew's answer on the vendor path, or his sitting (the Opal producer). `R5-sit-1` is
   staged for the second.
2. **The first real exercise of the four writers** (section 4): each is another seat's act; this project owes the READ after
   each (the ticket's members, the log's tokens). Say if you want those reads cut as standing cells now.
3. **FWD-2's live proof** (`R5-fn-2`): a real other-firm sign-in refused, in front of Andrew, or a synthetic other-firm identity
   under a pair. Yours to choose.
4. **`commentary_sent` on the page** (FWD-6's second clause as a person sees it): a portal cell on a page `2.0.0_SA_COO~Y2` is
   cutting.
5. **The secret's readers** (`R5-gr-1`), when the laptop returns.
6. Run 3's request id, on IRPT_YCDGEN's reconciliation.
7. Andrew's crawl (`R2-cw-1`), on his word; the Ticket Center's staff notification list, his.

**Closer:** five rounds, thread n. The one stop on FWD-1 has an owner and it is Andrew; I do not re-pitch it.
