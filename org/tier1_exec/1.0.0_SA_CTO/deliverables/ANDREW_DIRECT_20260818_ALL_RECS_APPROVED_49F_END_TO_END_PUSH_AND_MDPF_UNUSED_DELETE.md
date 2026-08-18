# ANDREW-DIRECT 2026-08-18 ~1500Z (CTO terminal, in response to /open-calls) -- ALL RECS APPROVED · unused MDPF artifacts DELETE · the 49F END-TO-END PUSH is NOW, whole fabric

**Channel:** Andrew at the `1.0.0_SA_CTO` terminal, immediately after `/open-calls` (7 cards, 14:58Z).
**Recorded by:** 1.0.0_SA_CTO, same turn. **Broadcast:** MSTR + COO + CRO + CVO, same turn.

## VERBATIM

> "All recs approved, any unused mdpf artifacts should be deleted especially if no active producer. I reallly want to make a major push on 49 as the test case for the end to end push and I think we really need a dedicated session to do so, which will be now, so let's decide who we need on it, and put the whole fabric on the case with the adequate handoffs"

## WHAT "ALL RECS APPROVED" RULES (the seven cards, as put; the phrasing is his, the cards were mine)

| # | call | RULED |
|---|---|---|
| 1 | Re-open OPAL_ADVIPOINTERS now with 49 Financial END-TO-END as the spine, ahead of finishing INF/COT P1 | **YES** |
| 2 | INF morning floor | **(a) ONE unified morning floor with a LABELED carry** -- P2 TIMING may open |
| 3 | Cottonwood four-row bundle at the cot cutover | **(a) CANONICAL basis on all four** (recomputed AUA over cert-override; custody mix over FIFO-cube; tax-deferred mapping definition; one-client identity) -- activates at the cot cutover; packet detail rides the cutover TO |
| 4 | ADVI_PERFORMANCE §15 served-performance defaults P-1 / P-4 / P-6 / P-7 | **CONFIRMED as written** (net-of-advisory-fee TWR served, gross+net stored; market_growth = measured net return dollars, name/shape kept; advisor headline membership = current contract; v1 = MWR nullable, benchmarks + asset-level contribution deferred). P-2/P-3/P-5 were consumed by the 08-11 GOs. |
| 5 | `carried` provenance class pixels | **ORDINARY** (same as `reconstructed`, LD-0417 logic; type stays honest) |
| 6 | Pull the authorized deployed-vs-built-from byte census forward to NOW (one bounded read, classify-don't-fix) | **YES** |
| 7 | GRAPHFEED | **PARK** (with record) |

## THE MDPF DELETE RULING (new, his words)

*"any unused mdpf artifacts should be deleted especially if no active producer."* -- Scope as stated: MDPF artifacts that are UNUSED, with "no active producer" named as the sharpest case. This is the sovereign word OPAL_MDPFCLEANUP TO-4's reserved rows were waiting for (json/mdpf legacy keys, cache/, the reserved EC2/S3 rows), and it supersedes the "delete comes back later" framing on COO's card.
**Surfaced, not adjudicated (my finding, on the record @fc74f8f6b4 §3):** ONE json/mdpf key is UNUSED-BY-ANY-ROUTE but NOT UNCONSUMED -- `s3://opal-data-portal-v2/json/mdpf/49financial/aggregate-aua-timeseries.json` is read daily by the canonical `mdpf-gold-lambda` (FLAG-2 count carry, fail-loud). Deleting it before the FLAG-2 re-point (MDPF_PROVENANCE T-B, DS, 08-19) breaks the 13:30Z gold. His word authorizes the deletes; the re-point is the ONE ordering constraint and it is an engineering fact, not a scope reading. COO (issuer) applies the word to TO-4's rows in that order.

## THE 49F END-TO-END PUSH -- "the test case for the end to end push", "a dedicated session ... which will be now", "the whole fabric on the case with the adequate handoffs"

Direction: OPAL_ADVIPOINTERS re-opens with 49 Financial (08335338, ADVI product) run through ALL FIVE PHASES as the proving instance; the whole fabric is on it; the session is now. Staffing + handoffs: `ADVI_49F_END_TO_END_PUSH_PLAN_20260818.md` (CTO, same folder) -> COO decomposes into dated TOs with proof-of-spec contracts; MSTR spawns/seats; CTO attests each phase close.

## SECOND INSTRUCTION, same terminal, ~1503Z -- THE RESET-AND-RELAUNCH ORDER (verbatim)

> "What I'd like you to do is organize the fabric, essentially get everyone who needs to be involved who is currently online to write a handoff doc and log, save the handoff, and then when they have confirmed they have done that, you kill the fabric, reinstantiate everyone with custom launch tagging the handoffs or just necessary instructions in the launch dialogue, and we do a concerted effort from fresh contxt"

**Reading (addressed to CTO; scope as stated):** (1) every seat currently online (MSTR, COO, AE 0.7.0, DS 0.4.0 base -- and CTO) writes a handoff doc (`/handoff save`, committed) + a session log (`/log`), then CONFIRMS to CTO; (2) on all confirmations CTO KILLS the fabric (`.tools/kill-agent.ps1`, MSTR last after its integrate/push); (3) CTO REINSTANTIATES every seat the push needs (`.tools/spawn-agent.ps1 <serial> <first-message>`) with a first message that tags the seat's handoff path + the push plan + its role line; (4) the concerted effort runs from fresh context. CTO's own successor is relaunched by Andrew (a live serial cannot spawn itself under the identity guard) with the CTO handoff path in the launch dialogue. Executed 2026-08-18 ~1505Z->; the spawn/kill scripts are the sanctioned mechanism (MSTR's `/mstr-spawn`/`/mstr-kill` wrap them; MSTR itself is in the reset set, so CTO drives the scripts directly on Andrew's word).
