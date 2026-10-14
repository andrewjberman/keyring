# TCKT_VNEXT PRD v0.5 -- L4-R review, ratified-text half

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~18:5xZ. **Delivery:** msg 7805. **PRD:**
`org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md` @1bf1db1b0f (half_hash 0f168dc10b13). **Compared against:** v0.4 @fc2100e1e2,
which this seat's base serial signed.

**Authority read:**
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_173xZ_DELIVERABLES_FOUR_PRIORITIES_AND_DATES.md`, lines 37-45: "very
  simple", "We simply need to upload a trade request form", "in the next week or so", "confirmation or rescheduling", "We do not need to
  use Calendly". This is a machine transcript; its own list of possibly misheard words includes the coordinator's name, and the PRD
  says the spelling is unconfirmed.
- `ANDREW_DIRECT_20261014_183xZ_FIVE_CALLS_ANSWERED_AND_BD_ASOF_CITATION.md`, line 8: "DELL2 has the capacity to manage it".

**Verdict: REFUSE. The ENDPOINT carries his word, but CONTRACTS is silent on the two new types and on the staff filer's firm choice.**

## The ENDPOINT against his word -- carried

- **FWD-10, the Trade Request:**
  - it is an upload of the form, with no trade sent anywhere (ACCEPT);
  - a placeholder form is named as such until the real one arrives;
  - it goes to DEV, then to PROD by 2026-10-24.
- **FWD-11, the Meeting Request:**
  - it goes to the coordinator's queue;
  - the coordinator confirms or reschedules on the ticket, and the filer reads the outcome there;
  - it is in-house, with no Calendly.
- **FWD-1 to FWD-9** are byte-equal to v0.4.

## Refusal -- what FWD-10 and FWD-11 operate on is not in CONTRACTS

The CONTRACTS table is unchanged from v0.4. C-TYPE says every type is a definition: label, questions, checks, route and output. The first
type has its own row, C-ANALYSIS-REQUEST. The two new types have none. Three operative rules live only in ADDENDUM 5:

1. **The staff filer's firm choice.**
   - FWD-10's filer "chooses the firm".
   - The table's only firm rule is C-FENCE, which exempts internal callers ("unless the caller is internal").
   - Nothing binds a staff filer's choice to its explicit `allowedFirmIds`, or makes every later hop follow the choice. ADDENDUM 5 item 4
     says "Firm choice follows IRPT_ANLREQ C-FIRM", but that is history, not a citation in the table.
   - This seat refused IRPT_ANLREQ v0.6 for the same gap.
2. **The Trade Request type.** Its question set, the attachment (the form), its route, and the boundary "no trade engine submission;
   the engine path and its 409 stay with NFRA_OPSWKF".
3. **The Meeting Request type.**
   - Its questions: who, purpose, proposed times.
   - Its route: the coordinator's queue, by the Ticket Center's own assignee and queue.
   - Its output: confirmed or rescheduled, on the ticket.
   - No new sender is built (C-MORATORIUM already covers this).

**Fix (three rows):**
- C-FIRM, cited to IRPT_ANLREQ in the C-SOURCES manner: one home, cited at its path, not restated;
- C-TRADE-REQUEST;
- C-MEETING-REQUEST, each in C-TYPE's terms.

## Point to fix in the same bump (not a reason to refuse)

FWD-10's DONE WHEN carries '(Andrew: "in the next week or so")'. That is an attribution inside DONE WHEN; it belongs in SOURCE. Keep
"until the real form arrives".

-- 3.0.0_SA_CVO~DELL2
