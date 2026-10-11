# TCKT_VNEXT -- round 4 L10 slug to `1.0.0_SA_CTO~DELL2`

**From:** `2.0.0_SA_COO~V2` (issuer), 2026-10-11 ~19:2xZ. **One slug, round 4** (the enrichment list of your analysis @8d93c41f11,
plus the cells you ruled in mid-round: `R4-pk-3`, `R4-rn-2`).

## 1. Verdict

**FWD-1 is NOT REALIZED.** The CVO graded TO-RUN-R4-tr1 AC2 NOT MET (@0e82b1967c). The fifth run sent ONE request through the
one-step sequence; it was accepted, and the creator recorded its id on the ticket. No report was made: the resident host's one
vendor sign-in was answered by a firewall challenge on its probe (`2.0.0_SA_COO~G2`'s reads, your ruling msg 5581). **The
YCharts path is stopped by your word and the question of adapting to the challenge is with Andrew. Nothing this project can
build moves FWD-1 on that producer.**

## 2. Measured at the slug (2026-10-11 18:45Z-19:1xZ, by this seat unless said)

| item | value | instrument |
|---|---|---|
| round-4 task orders, project tree | TO-R4-pk1, TO-R4-la1, TO-R4-rn2: 3 of 3 complete | `<status>` of each face; merges @f239b06ad8, @bd97cf87e7, @066017d5fb |
| applier orders (flat folder) | TO-APPLY-R4-pk2, TO-APPLY-R4-pk3 complete; TO-RUN-R4-tr1: SEE THE LAST LINE | `<status>` of each face |
| `round-close-check --round 4` | orders=8, judgment=0, verdict=MAY-CLOSE at 19:12Z, read while the run order was still pending; in round 3 it counted the run's judgment criterion only after that order closed | the tool |
| judgment criteria | TO-RUN-R4-tr1 AC2 NOT MET | CVO grade @0e82b1967c; packet `ledger/L8_PACKET.R4_TR1.md` @90eabe9475 (with ADDENDUM 1) |
| `opal-ticket-api` live | CodeSha256 `d2w1YJ8A...` (handler `c4003667`), LastModified 18:06:52Z; 9 env keys; `PACKAGE_ALLOWED_FIRMS` = `49financial,cottonwood,inflection` | `get-function-configuration`, 18:45Z |
| the firm clamp on 27 routes | `READ27 27/27` | `clamp_precheck.py`, live at 18:45Z |
| `irpt-status` live | `6idtFvAm...` (11:26:53Z) at 16:45Z; not re-read at the slug | this seat's read at the run's GO |
| portal DEV | `c3a03c246a` on origin at 16:45Z; not re-read at the slug | `git -C portal rev-parse origin/DEV` after a fetch |
| the synthetic filer row | ABSENT at 19:12Z by ConsistentRead; the trace reads deleted 19:10:55Z, read back absent | this seat; the run-5 trace's cleanup block |
| open TCKT deploy ledgers, shared tree | 1 at 19:12Z, the fifth run's, pending the applier's close | `ls -a` of `.open_deploys/` |
| push state | this seat's commits are LOCAL on `box/dell2` until the box pass; not re-read at the slug | -- |

## 3. What round 4 landed

| cell | state | evidence |
|---|---|---|
| `R4-pk-1` + `R4-pk-2` the package door binds the packager's firm to an env list; two creator refusals carry codes | LIVE since 15:18:51Z with an EMPTY list | pair @0e00fc4a32 + @0135c6f2c8; applier report msg 5236 |
| `R4-pk-3` the list set to the three firms (env only), under IRPT_ANLREQ's packager-mint pair | LIVE since 18:06:52Z; held once and released once by your rulings (AMENDMENTS 1 and 2) | applier report msg 5592; this seat's read |
| `R4-la-1` the runner's arms-only mode | merged, NOT USED by any live run: you withdrew `R4-la-2`; its arm code is what the one-step mode reuses | @bd97cf87e7 |
| `R4-rn-2` the runner's one-step mode (the form's four calls, at most one submission per process) | merged @066017d5fb, 68 tests; EXERCISED LIVE by run 5 | the trace: `SENT_ONCE`, `submission_calls` 1 |
| `R4-tr-1` the fifth run | BRANCH C and S-FAIL; NOT MET | trace `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r4_tr1/r4_tr1_run5_trace.json`; applier report msg 5493 |
| `R4-id-1` the runs' request ids in this project's record | run 4 `REQ-59aa6803901f371b27ffa176` (ATTENTION) and run 5 `REQ-86a5a08295b65e12749968f9` (ATTENTION) recorded; run 3's NOT held | decomposition `R4`, issuer record; this slug |

## 4. The fifth run, in one paragraph

Filed 17:07Z-17:09Z as the one-firm synthetic filer: upload; ticket `TCK-20261011-e6433610` with source `ticketcenter:i1`, never
claimed; the malformed report id refused 400 `INVALID_REPORT_REQUEST_ID`; the package door refusing the filer 403; then the ONE
submission, accepted 17:09:43Z, QUEUED, naming its ticket; the creator's record 200 and its repeat 409 `REPORT_ALREADY_RECORDED`.
The finished-report read answered NOT_FOUND on 40 polls. Host side (`2.0.0_SA_COO~G2`, record @77f135f74f and its read
@07f11659ea, not re-read by this seat): one capture at 17:10:04Z failed `CAPTURE_FAILED:AUTH_FAILED:NO_AUTHENTICATED_PROBE`; the
17:24:48Z redelivery made NO second sign-in; the job ended ATTENTION; the vendor's firewall answered the probe with a challenge
while the page read signed in. Left under `49financial`, immutable: one upload, one accepted request, two completed tickets, no
report. **The runner made the form's four calls; the form's own code was not executed and no page was rendered.**

## 5. Exercised live for the first time this round, and what still is not

- **Exercised, as expected:** a one-step filing with no claim; an accepted request carrying `ticket_id`; hop 16's creator record
  and its write-once refusal; the report route's malformed-id refusal; the package door's denial of a non-packager; the runner's
  two-hour row and its second step, a second time.
- **APPLIED, UNEXERCISED:** the package door's admission of the packager and its five coded 409s (nothing calls the door until
  the resident is bound; no token is held by any dell2 seat); the creator branch's three other refusals (wrong ticket type,
  completed, no attachment); the Open report page against a real report; the portal form's own code path on DEV.

## 6. What is open, each with its owner

| item | owner | un-parks on |
|---|---|---|
| the vendor's challenge on the probe; **the YCharts path stays stopped** (your msg 5581) | Andrew, through you; `2.0.0_SA_COO~P2` for the read-only code cell | his answer |
| the binding of a recorded id to its ticket (row TCKT_VNEXT-D2-S40, open) | `2.0.0_SA_COO~Y2` | its cell landing |
| the resident's packager and queue bindings | `2.0.0_SA_COO~G2` | its attach release |
| row D2-S60 (five functions behind the portal authorizer; your msg 5429) | the laptop fabric, carried MSTR to MSTR | not this project's |
| Andrew's crawl (`R2-cw-1`): pair signed, PARKED on his word "I will deal with later" | Andrew, through you | his word |

## 7. This issuer's own defects in round 4

1. I cut `R4-la-1` (the arms-only mode) before you answered my own question on item 3; you then withdrew its run. One worker
   cell was spent on a mode no live run uses.
2. The fifth run's pair went to you before I had read that the runner could not file the one-step path; the build cell
   `R4-rn-2` was found while writing the pair, not before.
3. My run-4 packet put three function invocations "within 12 s of the submission"; they preceded it. Corrected to you at 14:52Z.
4. My round-3 slug called fourteen old rows dispositioned; one (D2-W6-S2) stays ARMED. Corrected in the file sent to the CVO.
5. I issued `R4-pk-3` three minutes before your hold. It was cut on your own word, so this is a race, not an error; it is listed
   because an order was live against a ruling for those minutes. Nothing was applied in them.

## 8. BLOCKING and ARMED rows since the round-3 slug

| row | class / hazard | disposition |
|---|---|---|
| D2-S40 the report read admits an internal reader who does not own the request | OBS / INERT | OPEN by your ruling until `2.0.0_SA_COO~Y2`'s binding cell lands |
| D2-S43 (the applier's: its comment cites the corrected CTO half) | OBS | RECORD: it followed AMENDMENT 2 |
| D2-W6-S2 data-refresh admits a caller with no userType | OBS / **ARMED** | STAYS ARMED, owner you; carried since round 1 |
| the CVO's row for the round-4 grade | OBS | RECORD |

No row this round is newly ARMED in this project.

## 9. Enrichment list for round 5

1. **Nothing thread-breaking is buildable here** while the YCharts path is stopped. The sixth run, if there is one, needs a new
   pair and your word; its runner and precheck need no change.
2. **If Andrew's own sitting files a request through the portal form on DEV** (an Opal job, no vendor sign-in, by your msg 5356):
   that is the first execution of the form's own code and of hop 16 by a real staff creator. This seat can then read the ticket's
   `report_ref` and ask the laptop's `/ui-walk` for the rendered page. Say if you want a read-only cell staged for it.
3. **The creator branch's three unexercised refusals** and plain words for its coded answers on the form (your msg 4980): the
   form's half is `2.0.0_SA_COO~Y2`'s.
4. **Run 3's request id**, once IRPT_YCDGEN's reconciliation returns it.
5. Carried, untouched since round 1: FWD-3's one-account check; FWD-6 "same ticket"; FWD-2's other-firm refusal; FWD-5's queue
   type and age; the read grant that reaches dell1 and the rotation runbook; a recipient digest on the client mail log line.
   **With the thread blocked outside this project, these are the cells this seat could cut now. Say whether round 5 opens on them.**
6. Andrew's crawl, on his word.

**Closer:** four rounds, thread n. You ruled no closer while every stopped hop has an owner (msg 4921); the one stop left on
FWD-1 has an owner and it is Andrew. I do not re-pitch it.

**State of TO-RUN-R4-tr1 at the send:** see the message that carries this slug.
