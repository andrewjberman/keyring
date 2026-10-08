# NFRA_TRNSPT decomposition -- ROUND 12 (2026-10-08, issuer 2.0.0_SA_COO~T2, dell2, box/dell2) -- the FWD-10 THREAD

Re-cut on Andrew-direct ~22:2xZ (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_222xZ_TRNSPT_FOCUS_AI_COMMENTARY_PARK_ANALYST_ACCESS.md`
@a4fdb78bbe; CTO msgs 1763, 1780): "Cut FWD-10's thread as ONE live journey: an analysis report goes READY, then the slicer picks similar
past commentary from gold, then a Kimi K3 draft in Opal's voice (C-WIPE-GATE first), then a review ticket, as a draft only and never
delaying the report. Decompose over those hops." The round-11 analysis's E1 (the Apple exception list) is deprioritised behind this; FWD-5
access is parked. PRD contracts: C-SLICE, C-KIMI, C-WIPE-GATE, C-TICKET, C-TRIGGER, C-GOLD-FIELDS (`prd/NFRA_TRNSPT_PRD.md:113-121`).

**The thread's hops and owners.**

| hop | what | owner | this round |
|---|---|---|---|
| H1 | READY hook: DynamoDB stream on `irpt-requests` REPORT# items -> our entry, async, DLQ, never blocks the report (C-TRIGGER) | IRPT_BCKEND `2.0.0_SA_COO~P2` (routed, msg 1780) | STUB; the event shape is the contract file e12 drafts |
| H2 | READY event -> one ABSTRACT request (variant, comparison keys, account type, themes, holdings as category weights; no client identity) AND a separate ticket context for H6 only | this project | `TR-e-12` |
| H3 | the slicer over commentary gold (C-SLICE; `outlook/slicer.py`, built and tested) | this project | inside `TR-d-12` (adapter: gold rows in, candidates out) |
| H4 | the Kimi K3 draft in Opal's voice from the abstract request + precedent texts (C-KIMI), refused until C-WIPE-GATE passes | this project | `TR-d-12` |
| H5 | the `analysis_request` ticket type + requester-claim (C-TICKET) | TCKT_VNEXT `2.0.0_SA_COO~V2` (routed, msg 1780) | STUB; the write call is ~V2's contract v0.1 @a8410fcca3 (accepted by the issuer, msg 1785 reply) |
| H6 | the ticket-write client: the draft into an `analysis_request` ticket; a failure never reaches the report path | this project | `TR-t-12` |

**Chains.** A = TR-e-12 (slot ~1). B = TR-d-12 (slot ~2). C = TR-t-12 (slot ~3). No edge: each builds against a contract or a fake. Fan-out 3
of 3, cap 8. The live journey trace at the close strings H2 -> H3 -> H4 -> H6 with H1 and H5 stubbed.

**Write sets (disjoint).** New package `data/transcripts/scripts/commentary/`: e12 `entry.py`, d12 `drafter.py`, t12 `ticket_client.py`
(each cell creates `__init__.py` only if absent at its base -- e12 owns it); tests `test_commentary_entry.py`, `test_commentary_drafter.py`,
`test_commentary_ticket_client.py`; the contract file `org/standards/NFRA_TRNSPT_READY_EVENT_CONTRACT.json` (e12). t12 codes to ~V2's
ticket-write contract v0.1 @a8410fcca3 (no contract file of ours).

**Issuer rulings.**
1. **Measured state at the cut:** `s3://opal-data-transcripts/outlook/transcripts/gold/` holds 0 objects; silver holds 5 (round 4: all 3 rows
   held out). So the first live drafts take C-SLICE's no-precedent path ("with none at all a draft is still produced and says it has no
   precedent"). A gold build from silver is not in this round.
2. **No model call in any worker cell.** The drafter takes an injected model adapter (the estate pattern: `resolution_kimi.py` "the installer
   supplies a deadline-enforcing HTTP/secret adapter ... There is no default network client or credential read"); tests use a fake. The
   first REAL Kimi call is an issuer act at close, and only if C-WIPE-GATE is recorded passed (Andrew's 2026-09-30 word covers the first
   call after the gate, C-KIMI); otherwise the close trace runs the fake and says so.
3. **The READY-event contract is a DRAFT by the consumer** (this project) for `~P2` to agree; the ticket-write contract is `~V2`'s v0.1, ACCEPTED by the issuer with ruling O3: draft for every READY report, `add_commentary` sent true (FWD-10's DONE WHEN carries no condition). A field the producer cannot
   supply is a change to the file, not a workaround.
4. **No client identity crosses into H4** (C-KIMI: abstract fields only; FWD-10 ACCEPT "nothing in the draft identifies another client or
   firm"): e12 and d12 each test it with planted identity fields.

## Rule 24 record

Domain: the six hops of the Andrew-direct. H1 and H5 = other lanes (routed, stubbed); H2 = TR-e-12; H3 + H4 = TR-d-12; H6 = TR-t-12; the
journey = the issuer's close trace. Remainder: none. FWD-11 (attachment) and the gold build are not in this round.

## Battery

Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R12_CHECKS/r12_checks.py`, dry-run at base box/dell2 846cbbe61e: e12 FAIL
(absent), d12 FAIL (absent), t12 FAIL (absent).
