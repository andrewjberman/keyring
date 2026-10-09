# IRPT_ANLREQ PRD v0.1 @5dd6c2422b -- ratified-text half review (L4-R)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~04:3xZ, on `1.0.0_SA_CTO~DELL2` msgs 2405 and 2407. Half hash 5fbe1b1603f4.

## Verdict: SIGN

1. **Verbatim against the pin.** The ENDPOINT block FWD-1..6 equals the L2 file
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_IRPT_ANLREQ_20261009.md` @670ded26ed: 3,378 characters each after whitespace
   normalisation, identical.
2. **Against Andrew's word** (@2b21a349d1). Every element he named has an outcome: the custom form with analysis type, Opal-model
   checkboxes, other-ETF field and the Excel (FWD-1, FWD-2); the typo check and swap (FWD-2); the ticket sitting open (FWD-1); the backend
   finishing by itself to the report, the commentary from the report's key surfaces, the branded PDF and the original Excel on the same
   ticket (FWD-1, FWD-3); the no-stop defect he named (FWD-4); the Analysis tab as the later manual path for unusual cases (FWD-6). Nothing
   is widened beyond his word except FWD-3's DRAFT state and FWD-5's firm wall, each sourced to an already-ratified contract (NFRA_TRNSPT
   C-KIMI; TCKT_VNEXT FWD-2 and C-PACKAGE).
3. **No wait.** Every DONE WHEN is a seat act on demand. Alyssa's first real filing is the organic arm and C-ONE-JOURNEY states it is
   never the gate.
4. **No annotation or seat name** inside ENDPOINT or CONTRACTS beyond contract and order ids.
5. **CONTRACTS agree with the counterpart.** C-PACKAGER's one `package_principal` named in the type definition is TCKT_VNEXT's C-PACKAGE
   (TCKT_VNEXT_PRD.md :110), whose four refs (report, pdf, original, commentary) are FWD-1's package. IB-pr-387 exists as an order.

## Note, not a ground

C-FIRM reads "svc-commentary by tenant-bound get()". The token's create reach is the three-firm clamp `COMMENTARY_ALLOWED_FIRMS`
(measured at TCKT_VNEXT F10, row D2-S11); per request its reads are tenant-bound. "Exactly the request's firm" holds per request, not
per token.

## Re-review on v0.2 @97ef783e9a (~04:4xZ, msgs 2423 and 2427): SIGN

Two changes reach this half (CRO refusal msg 2416):
1. **FWD-2 ACCEPT** now states the security swap: an unknown or unpriceable holding is replaced by a confirmed candidate before filing,
   never by an unverified guess. The v0.1 clause "a person who wants a model swapped" is gone. That matches the estate's meaning of
   "swap" in Andrew's word: the CRO trace @9076346655 (hop 2, lines 94-102) reads swap as the security swap that today refuses
   `KIMI_WEB_SEARCH_UNVERIFIED`. FWD-6's "a swap the form cannot express" still covers the manual remainder he named.
2. **C-ABSORB** names what moves in and what stays. It is Andrew's "compress ... into one project" (@2b21a349d1) made operative, with
   one driver (`~Y2`) and disjoint workstream scopes under rule 27. It conflicts with no counterpart contract: in-flight orders and
   signed pairs complete where they are.

The rest of ENDPOINT and CONTRACTS is unchanged from v0.1. Signed on these bytes.

## Re-review on v0.3 @1251f44685 (~05:0xZ, msgs 2496, 2499, 2509): SIGN

Against Andrew's verbatim words (~04:4xZ, recorded in `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261009_SECURITY_SWAP_AND_NO_YCHARTS.md`
@9ae5d353d1, final section):
1. **FWD-2 and C-SWAP** follow his method in order: check that the security exists; yfinance as "the checker"; if yfinance has nothing,
   classify with the SECCLASS taxonomy using a search; pick a proxy "that is in the registry". The proxy is deterministic from the registry,
   not proposed by the model, which is his "select an ETF ... in the registry". The clause "the advisor sees and can change it" is not in
   these words; it carries the brief's "swap ability ... featured in that process" (@2b21a349d1) and narrows nothing.
2. **FWD-7** is his "I do not think we actually need YCHARTS for anything", as an exercised trace with zero calls.
3. **C-PRICES:** SECHIST first, yfinance next, Bloomberg "only ... if truly absolutely necessary" (through its queue); the overlays use the
   ported performance engine, as he suggested.
4. FWD-1, FWD-3..6 and the other contracts are unchanged. No wait; no seat name inside the sections.
