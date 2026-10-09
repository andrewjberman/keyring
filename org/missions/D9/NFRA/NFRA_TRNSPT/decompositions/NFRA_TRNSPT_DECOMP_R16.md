# NFRA_TRNSPT decomposition -- ROUND 16 (2026-10-09, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on 1.0.0_SA_CTO~DELL2 msg 2205: "(1) D2-S7 is ruled and shipped: household is optional for svc-commentary only, deployed in F10-d-1 v2 ...
(2) The CVO APPROVED Apple (msg 2200, ADJUDICATION_v9). (3) Backfill: YES, one bounded backfill of 365 days ... under its own never-widen pair."

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-h-16` | H6 to ~V2's shipped behavior: household optional for svc-commentary (row D2-S7) | FWD-10 | dell2 worker | LOCAL | worker-light | -- |
| `TR-a-16` | the Apple re-write: re-fold + re-write the 29 Research silver objects (laptop, as TO-RUN-b11), read back Apple > 0 | FWD-5 | ISSUER (served; laptop writes) | SERVED | -- | -- (routed to MSTR 2026-10-09T02:35Z) |
| `TR-b-16` | the ONE 365-day backfill under its pair (laptop) | FWD-10 (precedent) | ISSUER (served; laptop writes) | SERVED | -- | the CTO half of the pair |

**Chains.** A = TR-h-16 (slot ~1). TR-a-16 and TR-b-16 are the issuer's served acts. Fan-out 1 of 1 worker chain, cap 8.

**Issuer rulings.** (1) Until ~V2 records contract v0.2, H6 codes to the SHIPPED behavior (msg 2198): `answers.household` omitted when the
ticket context has none; the title then reads "Draft commentary -- <report_type> (<report_request_id>)". (2) The backfill's COO half is
`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/NEVER_WIDEN_NFRA_TRNSPT_COO_HALF_365D_BACKFILL_20261009.md` @0e839e0e49; the run is routed
only after the CTO half lands.

## Rule 24 record

Domain: msg 2205's three items. (1) = TR-h-16 (our side; ~V2 shipped theirs); (2) = TR-a-16; (3) = TR-b-16. Remainder: none.

## Battery

Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R16_CHECKS/r16_checks.py` at base box/dell2 20784c5462: h16 FAIL (missing test).
