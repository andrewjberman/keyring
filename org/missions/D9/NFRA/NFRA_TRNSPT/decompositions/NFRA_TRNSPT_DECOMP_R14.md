# NFRA_TRNSPT decomposition -- ROUND 14 (2026-10-09, issuer 2.0.0_SA_COO~T2, dell2, box/dell2) -- keep-driving, empty tick

Cut under Andrew-direct ~01:5xZ "/keep-driving ON for all boxes, all COOs" (MSTR msg 2144; record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_000xZ_KEEP_WORK_DRIVING_OPEN_CALL_QUEUE_CROSS_ADJUDICATION_AND_NEXT_CALLS_ON_EMPTY_TICK.md`):
the round-13 enrichment was consumed and every remaining FWD-10 hop waits on another seat or a call, so `/next-calls NFRA_TRNSPT --drive` queued
the calls and this round takes the FREE options around the blocks. Calls queued on dell2's list (2026-10-09T01:5xZ): the Kimi standing word for
live operation (an Andrew act) and row D2-S7 (household; CTO + ~V2). PRD v0.2 FWD-10 and the round-12/13 decompositions are the frame.

| cell | item | outcome | placement | risk | worker_class | around which block |
|---|---|---|---|---|---|---|
| `TR-l-14` | the commentary Lambda: one handler wiring H2 -> H3 -> H4 -> H6 through injected ports, its `NAMES.json` (builder output), and its Terraform (function, DLQ, role, policy) -- DESIRED, plan only | FWD-10 | dell2 worker | WORLD (path floor; nothing applied) | worker | ~P2 cuts H1 only once `outlook-global-commentary-draft-lambda` exists |
| `TR-h-14` | H2 derives `holdings_categories` from the normalized input the composition names (~P2 msg 1849) | FWD-10 | dell2 worker | LOCAL | worker-light | D2-S7 (household) |
| `TR-x-14` | the curated exception list (round-11 analysis E1 / CTO msg 1745), Apple first, with its gate test | FWD-5 | dell2 worker | LOCAL | worker-light | the FWD-10 blocks (work around, on another outcome) |

**Chains.** A = TR-l-14 (slot ~1), B = TR-h-14 (slot ~2), C = TR-x-14 (slot ~3). No edge (l14 calls H2 through `entry.handler`; h14 changes
only the abstract request's one field). Fan-out 3 of 3, cap 8.

**Write sets (disjoint).** l14: `data/transcripts/scripts/commentary/lambda_handler.py` (new), `data/transcripts/scripts/commentary/NAMES.json`
(new), `infra/aws/terraform/transcripts/commentary.tf` (new), `data/transcripts/scripts/tests/test_commentary_lambda.py` (new). h14:
`data/transcripts/scripts/commentary/entry.py`, `data/transcripts/scripts/tests/test_commentary_entry.py`. x14:
`data/transcripts/scripts/teams/securities_exceptions.json` (new), `data/transcripts/scripts/teams/securities_allowlist.py`,
`data/transcripts/scripts/teams/securities_allowlist.json`, `data/transcripts/scripts/tests/test_securities_exceptions.py` (new).

**Issuer rulings.**
1. **The Lambda is DESIRED, never applied this round.** No apply until CALL 1 (Andrew's standing Kimi word) is answered AND the `irpt` key's
   decrypt leg is granted (a key another box uses: the before-rule, through MSTR to the laptop; ~P2's facts @6061d0e274). The model call in the
   handler requires a non-empty `KIMI_STANDING_WORD_REF` (the record path of Andrew's word); empty = the handler stops after H3, calls no model,
   writes no ticket, and returns `no_vendor_word`.
2. **Names are builder output** (rule 30, now REFUSED at commit): `name("outlook","global","commentary-draft", <kind>)` for the lambda, role,
   policy, queue (`outlook-global-commentary-draft-lambda` / `-queue` measured at the cut); the log group derives from the lambda name.
3. **The exception list's entries are reviewed by 3.0.0_SA_CVO** (msg 1745); Apple's holding evidence is the issuer's
   `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R12_HOLDING_EVIDENCE_AAPL.json` (PFDE holds AAPL, as of 2026-10-07). The re-fold and
   re-write of the 29 objects that would carry Apple is a later served act, not this round.

## Rule 24 record

Domain: the FREE options of the 2026-10-09 `/next-calls --drive` assessment (O1 Lambda, O2 holdings, O3 exception list). O4 (D2-S7 adaptation)
waits on its queued call. Remainder: none.

## Battery

Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R14_CHECKS/r14_checks.py`, dry-run at base box/dell2 1440a9d3d1: l14 FAIL
(absent), l14n FAIL (absent), h14 FAIL (missing test), x14 FAIL (absent).
