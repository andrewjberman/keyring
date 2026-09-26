# ANDREW-DIRECT 2026-09-26 ~02:2xZ -- 1.0.0_SA_CTO~O: the six open calls answered

- Channel: terminal, the 1.0.0_SA_CTO~O session, site Z, answering this seat's /open-calls (6 cards, ~02:1xZ).
- Recorded by: 1.0.0_SA_CTO~O, same turn.

## Verbatim

> recs approved for all 1-4. On call 5, lift fully. On call 6, it is currently a script that runs every day, not an ai agent. the agent is just there as a failsafe if the script fails.

## The calls, as put, and what each answer settles

1. **The laptop's CLOUD push** (the cherry-picks 678891171b..52809cd052 and the opal-gateway release_note entry for
   0af72fb1d0): **YES.** The laptop seat pushes; 0.0.0_AB_MSTR~Z verifies origin/CLOUD. Row NFRA_OPALAI-Z-S21 disarms
   when origin/CLOUD's EC2_MANIFEST names what the host serves.
2. **The test colleague:** **Alyssa Keith, scoped to portal figures only.** 2.0.0_SA_COO~O writes the permission
   through the existing operator path (runbook step 6); nothing new is built.
3. **The Analyst's Claude account:** **a dedicated account used only by the Analyst, not Andrew's.** Andrew signs it in
   at runbook step 4.
4. **G-PYPI:** **YES, one pinned, hash-checked package at one version** for the grant-writer apply (NFRA_MCPORTAL
   TO-MP-a-1). The apply still needs the owner key from runbook step 7.
5. **The NFRA_OPLGTW stop (2026-09-22, "do not go further with it"):** **LIFTED FULLY.** This releases:
   - gate G-MOVE (the gateway's move into opal_ai, NFRA_OPALAI FWD-5/FWD-11);
   - NFRA_MCPORTAL C6;
   - the 5 Schwab tools held in NFRA_MCPINDEX TO-MX-c-5;
   - NFRA_OPLGTW's own two open orders, OG-v-4 and OG-v-5. Each still waits on its own named gates (G-C/G-D and
     G-E/G-F), which this lift does not satisfy.
6. **The daily Bloomberg upload:** a scheduled script does it every day. An agent is only a failsafe for the day the
   script fails.

## Reading, narrow

- Answers 1-4 approve the recs as put and widen none of them.
- "lift fully" lifts the stop. It does not grant any gate the stop sat in front of: a gate with its own condition
  (an identity, a grant, a sign-off, a device act) still needs that condition.
- Answer 6 is a statement of fact, not a ruling on the rec. Measured beside it, this turn:
  - The daily script is `integrations/bloomberg/pipeline/publish_to_portal.py`. It publishes straight to the portal
    with no gateway, no OAuth and no agent in its path (its own header, lines 6-17). So the gateway's
    `opal_data_refresh_upload` serves only the failsafe.
  - OA-f-1 (drained @e8b9aaeebf) admits that tool for opalbloomberg@ on ONE OAuth client, measured as the single live
    refresh family: the operator's sign-in on this box. A failsafe run from an operator-side session keeps working.
  - After the switchover, the Analyst runtime signs in with its own client and has no AWS or workspace access (C4).
    So the Analyst is NOT the failsafe, and the round-2 fence change (drop the upload from the Analyst's tool list)
    stands as the rec put it. If Andrew wants the Analyst itself to be the failsafe, that is a new call.
