# IRPT_CUSTDY, ADVI_BILLING, NFRA_OPSWKF v0.1 @aa3d5efaa5 -- ratified-text half review: SIGN all three

**Reviewer:** 3.0.0_SA_CVO, 2026-10-06 ~21:3xZ. **Asked by:** 1.0.0_SA_CTO msgs 105768-105771.
**Andrew's word:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_210xZ_SEVEN_CALLS_RDP_LOCK_Q1_Q2_Q3_CONFIRMED_NO_BD_SHAPE.md`.
**Pins read against:** the three confirmed proposals, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_{Q1_CUSTODIAL_INVESTOR_REPORTING,Q2_BILLING_BUY_OR_BUILD,Q3_TRADE_SUBMISSION_OPS_WORKFLOW}_20261006.md`.

## ENDPOINT -- each PRD block diffed line by line against its confirmed proposal (whitespace-normalised)

| Project | Proposal lines | PRD lines | Differences |
|---|---|---|---|
| ADVI_BILLING (Q-2) | 43 | 43 | 0 |
| NFRA_OPSWKF (Q-3) | 44 | 44 | 0 |
| IRPT_CUSTDY (Q-1) | 60 | 69 | FWD-9 added, nothing else |

- **IRPT_CUSTDY FWD-9** carries call 6 as he said it: for every figure a Black Diamond report shows, the Black Diamond
  source that served it and the custodian or Opal source that replaces it ("do black diamonds job for them"). His
  suspicion that Commonwealth's history holds more is shown where true, never assumed.
- **Form:** no seat serial and no version history inside any of the three blocks.

## CONTRACTS -- PASS

- **IRPT_CUSTDY**
  - C-SHAPE is call 6: the custodian's shape, Black Diamond as a field map only.
  - C-COMPARE is two dated, one-time comparisons, with no rerun. That respects the no-standing-comparator law.
  - C-TEMPLATE leaves template approval OPEN with Andrew, which is right: his answer to call 6 did not decide it.
- **ADVI_BILLING**
  - C-SHAPE cites IRPT_CUSTDY's C-SHAPE, so the two agree.
  - C-TRIAL-FIRST makes one check against an actual debit, never a standing comparator.
  - Two holds keep vendors and uploads out until Andrew says so: C-NO-VENDOR-YET (no seat contacts a vendor) and
    C-NO-UPLOAD (only today's person uploads, on his word).
- **NFRA_OPSWKF**
  - C-ANALYST-DEFERRED is the one wait in the three projects. It is stated on the outcome (FWD-2), with its reason
    and his word ("I need to review this later"). That is how rule 27's essential-wait clause wants a wait carried.
  - C-NO-SEND: Opal never transmits a trade.

**Notes, not blocking:**
1. **The call numbers in CONTRACTS** (IRPT_CUSTDY C-COMPARE "call 3"; NFRA_OPSWKF C-WORKFLOW-LEADS "call 4") map to the
   CTO's seven-card deck, which is not in the repo. This seat checked the mapping by elimination against his
   answers, not against the cards.
2. **IRPT_CUSTDY C-PROGRAMME closes ADVI_STITCH, ADVI_COTKEY and ADVI_BDPARITY as MERGED.** Their register rows and
   PRDs must say the same at L3. That is the CTO's carrier to write.
3. **The register differs from the proposal for Q-3:** the proposal named `TRSB_OPSWKF` under the trade-submission
   macro, and the register reads `NFRA_OPSWKF` (D9/NFRA). L3 is the CTO's, and the code sits outside this half.

## Row NFRA_CTLPLN-S1: disarm VERIFIED (graded in its adjudication document)

Read here ~21:3xZ. The three enabled Remote Desktop inbound rules (User Mode TCP, User Mode UDP, Shadow TCP) each read
RemoteAddress `100.64.0.0/255.192.0.0`, which is the tailnet range. The wider census of other inbound rules on 3389
was PARTIAL: `Get-NetFirewallPortFilter` returned Access denied without admin rights. "No other rule opens 3389" is
therefore the CTO's read, not re-measured here.

-- 3.0.0_SA_CVO
