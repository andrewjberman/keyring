# ANDREW-DIRECT — OPAL_ANALYST project spin-up (0.0.3_BG "Opal Analyst")

**Channel:** MSTR~Z terminal (site Z), direct prompt
**Time:** 2026-08-10 ~13:30Z
**Received by:** 0.0.0_AB_MSTR~Z
**Recorded:** same turn, per the record+broadcast law (org/XXX.md)

## VERBATIM

> I want you to continue your work on the matter of the 0.0.3_BG "Opal Analyst" project. What I
> recommend is that you spawn 1.0.0_SA_CTO~Z and have them assess state of that agent and its
> purpose as I dictated last week which should be logged somewhere in terms of how it operates
> and its intention, and essentialy register a project called ANALYST, under the OPAL macro, for
> project code OPAL_ANALYST which facilitates the development of that product. What I'd recommend
> is that you first spawn 4.0.0_SA_CRO~Z to assess current state of that agent and find any
> relevant user input and logging about the intention for that product R&D and development, and
> then they write a brief on the state of everything they find whch they hand off to
> 1.0.0_SA_CTO~Z for PRD writing and project registry, and they hand it to COO~Z for
> decomposition and dispatch. Please spawn the requisite agents now, and your fabric should not
> be working on any other projects other than this one.

## Operative reading (MSTR~Z; surface-not-adjudicate — scope questions go back to Andrew)

1. **Sequence:** spawn `4.0.0_SA_CRO~Z` FIRST — assess current state of the 0.0.3_BG agent +
   gather all user input / logging on the product's intention, R&D and development → write a
   state-of-everything brief → hand off to `1.0.0_SA_CTO~Z`.
2. `1.0.0_SA_CTO~Z`: from the CRO brief + own assessment of the agent's operation/intention as
   Andrew dictated last week (logged — see pointers below), write the PRD and **register project
   ANALYST under the OPAL macro, project code `OPAL_ANALYST`**.
3. CTO~Z hands to `2.0.0_SA_COO~Z` for decomposition and dispatch.
4. **Site-Z fabric exclusivity:** no other projects worked on this fabric until further word.

## Known starting pointers (from the record, for the CRO)

- Build record: base MSTR log 2026-08-06 (`org/tier0_exec/0.0.0_AB_MSTR/logs/2026-08-06/`),
  items 7–9: 0.0.3_BG Teams-concierge redesign, LD-0382 @6e0e58552a, agent home
  `org/tier0_utility/0.0.3_BG_BBGTerminal/` (prompt + refs/ + tools/portal_lookup.py).
- Completion set commit: `65d80ab37` "build(0.0.3_BG): the Teams-concierge completion set
  (Andrew-direct 2026-08-07 at the MSTR~Z terminal)".
- ~~Launch was HELD on the identity blocker (gateway authenticates as Andrew; second-key
  `opal-bloomberg` auth mint was at Andrew). Current state of that blocker = CRO to assess.~~
  **CORRECTED 2026-08-10 ~1630Z (CRO~Z phase-1 brief @92e7020f4, live-verified):** the HELD line
  was the 08-06 end-of-day state and was stale by three days when this record was written.
  Launch + first live serve happened 2026-08-07 (reply DELIVERED 05:26:19Z as "Opal Bloomberg");
  identity blocker RESOLVED and HOLDING (both gateways whoami-verified 08-10). The agent is
  DORMANT since 08-07, and the live P0 relaunch gate is the `teams-watch.py:54` identity-blind
  token pick (durable fix owed by 0.5.0_AE). See the brief for the full open-items register.
- Skill: `/bbg-teams-assist` (ACK-FIRST serve loop, Andrew-direct 2026-08-07).

## Broadcast

- Bus frame to laptop `0.0.0_AB_MSTR` (same turn).
- Broker sends to `4.0.0_SA_CRO~Z`, `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z` on registration.
