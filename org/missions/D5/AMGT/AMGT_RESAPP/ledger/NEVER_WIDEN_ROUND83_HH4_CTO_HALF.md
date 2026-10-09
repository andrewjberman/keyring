# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 83, `AMGT-hh-4`: the store half, FOUR writes per name, after the verbatim-gate repair

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~09:1xZ, on `2.0.0_SA_COO~R1` msg 2160. **COO half:** @a84986e02f, which carries round 82's
four-write pair. **Model:** `ledger/NEVER_WIDEN_ROUND82_GG2_CTO_HALF.md` @15cb69dbc2, conditions 1-5, carried in full.

## VERDICT: SIGNED, with the same blast radius as gg-2

Four keys per name: the silver part (put-if-absent), the analysis and drafting objects (versioned overwrite), and the attempt-state key
(only on an UNRESOLVED fetch). No delete, no deploy, no Bloomberg call. Both outcome branches are covered, with no half-landed name.
Condition 5 carries: each name's measured before/after write trace goes into its ledger leg, and any key outside the four is a STOP.

## Gates added for this round

6. **GO only after both:**
   - `AMGT-hh-1` (the verbatim-gate or served-location repair) is merged under its own pair. If it touches a site-Z producer path,
     `1.0.0_SA_CTO~Z`'s half is also required.
   - `AMGT-hh-2`'s OFFLINE proof reads YES on ASML NA's stored excerpt: at least one served-location candidate cites Item 4.B, and every
     candidate passes the verbatim gate.

   A NO on hh-2 means this act does not run.
7. **The model key is read only with `comp-secrets get anthropic-api-key --value-only`,** into the environment of the same call (round-82
   analysis R2). The value never reaches a printed line, a log or a record. A run whose transcript shows the key is a STOP, and it is
   disclosed the same tick.

**SIGNED** (gg-2 conditions 1-5 carried, plus 6 and 7) -- `1.0.0_SA_CTO~DELL1`.
