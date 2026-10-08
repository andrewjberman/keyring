# NFRA_TRNSPT decomposition -- ROUND 13 (2026-10-08, issuer 2.0.0_SA_COO~T2, dell2, box/dell2) -- FWD-10 thread, first real draft

Cut on 1.0.0_SA_CTO~DELL2's round-12 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_12_20261008.md`
@a090c5ea23 (msg 1840): "C-WIPE-GATE is PASSED at current code" (TR-w1 complete; `test_wipe_planted.py` re-run at HEAD 49c04cd4b2: 13 passed)
-- "What this unlocks: the first real Kimi K3 call, under Andrew's 2026-09-30 word ... the abstract fields only. Any second use of the vendor
needs his word for that use."

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-g-13` | E1: row D2-S6 -- the drafter emits `generated_at`; a seam test writes the drafter's real output through the ticket client against ~V2's stub | FWD-10 | dell2 worker | LOCAL | worker-light | -- |
| `TR-k-13` | E2 + E3: the journey trace H2 -> H6 with the gate REAL, making the ONE real Kimi call (a no-precedent draft from abstract fields) | FWD-10 | ISSUER (a vendor call under Andrew's 09-30 word) | WORLD | -- | TR-g-13 drained |

**Chains.** A = TR-g-13 -> TR-k-13. Fan-out 1 of 1 worker chain, cap 8.

**Issuer rulings.**
1. **E2 and E3 share ONE vendor call.** Andrew's word covers the first call only; the E3 trace makes that call at H4 and it IS E2's draft. A
   second call (a retry included) needs his word and is not made.
2. **The call:** `drafter.KimiAdapter` with `http_post` = a stdlib POST to `https://api.moonshot.ai/v1/chat/completions` (the estate endpoint,
   `infra/aws/lambda/investor-reporting/ycharts/generate/kimi_port.py:18`) and `api_key_reader` = Secrets Manager `astn/kimi/api-key`
   (C-KIMI), key held in memory only. Logged by request id with no prompt body (the analysis's E2 criterion). The draft text is recorded only
   in the close record's hash and length; the text itself goes nowhere but the ticket stub's response check.
3. **Where the draft lands:** H5 (the ticket service route and the `svc-commentary` token, ~V2's contract O1) is not live, so the draft lands on
   the section-5 STUB, not a real ticket. "Only Opal can see" is therefore met by construction (nothing leaves the issuer's process except the
   vendor call); the real landing waits on H5. Stated, not hidden.
4. **Credential:** this is dell2's first read of `astn/kimi/api-key`; it is reported to the laptop through `0.0.0_AB_MSTR~DELL2` (msg 1232 rule 2).

## Rule 24 record

Domain: analysis E1-E3. E1 = TR-g-13; E2 + E3 = TR-k-13 (one call). Remainder: none. H1 and H5 stay stubbed (their owners).

## Battery

Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R13_CHECKS/r13_checks.py`, dry-run at base box/dell2 b75b0669f1:
g13 FAIL (absent).
