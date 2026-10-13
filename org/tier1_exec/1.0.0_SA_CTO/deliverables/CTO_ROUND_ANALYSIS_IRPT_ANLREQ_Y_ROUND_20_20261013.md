# CTO ROUND-20 ANALYSIS -- IRPT_ANLREQ (workstreams Y, YR) -- answering the round-19 L10 slug (2026-10-13 ~07:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/remediations/REMEDIATION_v12.md` and the L9
grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_19_L9_GRADE_20261013.md` @c219042317 (3.0.0_SA_CVO msg 6840): release 19 is
live; AR194-y-AC4J FAIL; 6 rows OPEN, 3 ARMED. **No PRD addendum.**

## 1. Where it stands

Release 19 (the reader that turns back two-account and total-row templates) is live on both the resident (06:09Z) and
`irpt-ycharts-generate` (06:27Z; this seat read `bNPCG2Oe...`). Row D2-W52-S36 is RELEASED, NOT SHOWN LIVE until Andrew's staff act
(`dell2-20261012T222152Z-2e30`) uploads the two synthetic files. The next reader release (r19.1, the widening and the value backstop)
is built, not released, and failed one judgment grade.

## 2. Rulings

| row | ruling |
|---|---|
| **D2-W59-S1** (L9 FAIL: the r19.1 backstop turns back a one-account file whose ABBREVIATED attribute header -- `Acct Market Value`, `Acct CUSIP`, `Acct Lot` -- holds distinct 8+-digit integers or letter-and-digit tokens) | **Repair before r19.1 is released, as the CVO's remedy says:** the attribute exclusions apply to the abbreviated root too (`acct`/`accnt` + `value`, `cusip`, `lot`, `status`, `opened` and the other ruled attribute words), so such a header never enters the backstop; and the backstop's identifier-like test is checked against the same negative controls the CVO named. The `No. of Accounts` reading as built (excluded unless its values are identifier-like) stands; the r18 test with name values under it passes. |
| **D2-W55-S25** (owner this seat: `irpt-status` carries 4 of the 24 correction words) | Named limit, as accepted; **carried by the status rule's all-eight pair**, which is the next release in this workstream after r19.1. |
| **D2-W58-S4** (owner this seat: PROD's ticket page shows the raw code `TEMPLATE_FINDINGS`; DEV shows words) | **No separate ask.** DEV already carries the words; the page is client-facing, so it goes to PROD with Andrew's held promote `dell1-e7f2`, and this line joins that breakdown ("ticket message: words instead of the raw reason code"). |
| **D2-W55-S5** (W328-S1's repair lives in the host capture library, which no release has moved) | Accepted: it rides IRPT_BCKEND's next resident library release (`2.0.0_SA_COO~P2`); the D2-S109 hold keeps any release that carries `ycharts_session.js` until it does. |
| **D2-W57-S5** (`SHEETS_NOT_READ` rides the stored answer and no portal reader shows it) | A portal cell shows the notice on the upload answer's face; through this seat's review lane, DEV first. |

## 3. ENRICHMENT LIST for round 20 (Y, ONE issuance; each build order at most three mechanical criteria)

1. The backstop repair (W59-S1) with the CVO's negative controls; then r19.1's two-leg release pair by the release-19 method.
2. The status rule's all-eight pair (W54-S5, W55-S1, W55-S25).
3. The portal notice for `SHEETS_NOT_READ` (W57-S5).

## 4. Acts only Andrew can do

Unchanged: the staff act `2e30` (the 49financial test request naming `TCK-20261012-c546fead`, plus the two synthetic uploads that show
release 19 live). The PROD ticket wording rides `e7f2`.

-- 1.0.0_SA_CTO~DELL2
