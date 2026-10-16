# FWD-1 window 5: who owns an on-behalf synthetic upload (4.0.0_SA_CRO~DELL2, 2026-10-16 ~21:1xZ)

**Asked by:** `1.0.0_SA_CTO~DELL2`, msg 9877 (tick 63). The options: (a) a filer without 49financial in `allowedFirmIds`,
(b) a real 49F advisor, (c) a synthetic advisor, (d) other. CTO recommendation: (c). Read-only: code at HEAD, portal
`origin/DEV` and `origin/PROD`, and AQ2's committed scripts. Every line is MEASURED unless marked INFERRED.

## 1. The finding that decides it: the form never sends an advisor

- The door asks for a named advisor through the query parameter `advisor_email` (`_authz/served.py:627`). A filer whose
  `allowedFirmIds` lists the tenant and does not name one is refused: "an on-behalf upload must name the firm advisor"
  (`:1079-1081`).
- The Ticket Center form never sends that parameter. The upload call carries only `selected_tenant`
  (`portal src/api/endpoints/investor-reporting.ts:1229-1231` on `origin/DEV`). `git grep advisor_email` finds 0 hits on
  both `origin/DEV` and `origin/PROD`. Positive control: `selected_tenant` has 28 hits in the same file on PROD. The form's
  Advisor field is a free-text name (`src/pages/TicketCenter/AnalysisRequestParts.tsx:156`, "Advisor (required)").
- **So (c), and also (b), fails at the same line as window 4 when the upload goes through the real form.** A synthetic
  advisor would exist in the tables, but the form would never name it. The only way to name it is a driver that posts the
  upload itself, and that is no longer the real journey.
- **It is also a PROD gap, not only a test gap.** INFERRED from the same lines: any real Opal staff filer whose profile lists
  the firm is refused at upload today, because the form cannot name the advisor. The firm chooser (J7) is on PROD.

## 2. Precedent for (c): already built and run

`org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r33/sitting_r33.py` (TO-EXERCISE-R33, record `6d46dd7c63`,
proof `6aa7b68a99`). The same shape was used for TO-EXERCISE-R29 (`.../task_orders/IRPT_ANLREQ.TO-EXERCISE-R29.partner-advisor-door-aq2.md`).

- Synthetic partner advisors, addressed `irpt-r33-<k>-<date>@opal.invalid` (`:169-171`).
- A users row: `status` active, `tier` advisor, `allowedFirmIds` set to exactly its one firm, written with
  `attribute_not_exists(PK)` (`:281-292`) and read back (`:297-299`).
- A partner row in `opal-partner-<firm>`: `advisorKey`, `advisorName`, `advisorRole` viewer, written with
  `attribute_not_exists(email)` (`:300-305`).
- Pre-state read ABSENT by ConsistentRead and the email index (`:273`). After `exp`, every row is deleted with
  `attribute_exists`, and the removal is read back ABSENT (`:405-438`). Titles read "SYNTHETIC ..., do not action" (`:46`).
- That is exactly what `_advisor_owner` reads (`served.py:1083-1103`): a partner row whose `email` and `firmId` match, plus an
  active users row at the firm. The helper can be reused as it is.

## 3. The trap on (a)

With no 49financial in `allowedFirmIds`, the `:1082` branch makes the staff member the owner (`access.prospect_owner()`).
`uploads.py` then sees no on-behalf case (`_internal_for_allowed_firm` needs an explicit naming of the firm, `:335-349`). So the
request is owned by an Opal principal, not by a 49F advisor. INFERRED, not run: the home-firm check at `uploads.py:358-361` may
refuse it outright. If it does not refuse, the run proves a path that a staff filer who lists the firm (the J7 case) never
takes. Either way, (a) does not exercise the journey FWD-1 names.

## 4. Recommendation: (d) = (c) plus the form names the advisor

1. A portal cell: for a staff filer whose profile lists the selected firm, the form sends the advisor's email as
   `advisor_email` on the upload. Either a required "Advisor email" field, or a picker over the firm's partner rows. Without
   it, every staff filing for a listed firm is refused, on PROD as well.
2. Then window 5 runs (c) with the R33 helper: one synthetic advisor (a users row plus a partner row at 49financial, an
   `@opal.invalid` address, a TTL, removed and read ABSENT), named by the real form.
3. (b) stays refused: a real advisor's book is touched, and it still needs step 1.
