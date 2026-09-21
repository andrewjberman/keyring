# `/self-drive AMGT_RESAPP` -- POST-REBOOT RE-ARM at the `1.0.0_SA_CTO~Z` terminal, 2026-09-21 ~14:5xZ

- **Channel:** the operator, direct, `/self-drive AMGT_RESAPP` typed at this lane's terminal. **Recorded by:**
  `1.0.0_SA_CTO~Z`, same turn, per skill Step 0.5 (carrier gates tick 1 -- committed before tick 1 runs).
- **Continuity:** re-arms the same scope the 2026-09-17 ~13:xxZ record armed
  (`ANDREW_DIRECT_20260917_13xxZ_SELF_DRIVE_AMGT_RESAPP_REARMED.md`), whose terms (2026-09-16 ~05:0xZ clause) this
  record carries forward unchanged. The intervening cron died with the pre-reboot session (session-local by design,
  §5); this is a fresh arm on a fresh operator word, not a resume of dead state.

## ARM TERMS

| field | value |
|---|---|
| **scope** | `AMGT_RESAPP` (project form). Directive `D5`, member set `{AMGT_RESAPP}` (register: `directives-check --json`, D5 row, single-member, no claim lag to resolve). |
| **device** | SITEZ (`agentbus-sqs.sh device` -> sitez). Matches D5's placement; no cross-fabric refusal. |
| **sequence** | `sequence-check --project AMGT_RESAPP` -> UNPLACED: not in `SEQUENCE.yaml`, governed by its own directive. No WAITING/HELD/OUT-OF-SEQUENCE flag; TRACK, not a gate. |
| **cadence** | 30 minutes, off-minute, via CronCreate. |
| **adjudication terms** | this lane closes every ADJUDICABLE call in scope on its own REC, same tick, per the 2026-09-17 call-routing supersession (design fork -> CRO research; governance fork -> CVO~Z verdict; a needed seat not live -> spawned by this lane). |
| **RESERVED** (unchanged from the carried clause) | vendor egress beyond Andrew's stated word; unrecoverable acts; money/contracts/entitlements; the portal freeze and any promote; the harvest collection mechanism and cadence (`@9db2a36cdc`); the LD-0522 push cadence. |
| **⛔ CORRECTED ~15:5xZ, found by `2.0.0_SA_COO~Z` (msg 23942):** of the three live project cards this row originally listed as "at Andrew," only TWO genuinely are -- the Bright Data per-use word and the Lusha rotate-or-rewrite word. **The third, "bucket/tenancy shape," was ANSWERED by Andrew on 2026-09-18** (`4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260918_214xZ_CONFORM_AMGT_DATA_TO_THE_CANON.md`); what actually holds `rk-32`+chain P is an UNLANDED doctrine-placement act assigned to `0.0.0_AB_MSTR~Z` on the laptop fabric, not a sovereign decision awaiting his word. This seat carried the stale framing across three round analyses before the COO's own `/open-calls` sweep caught it. Full detail: `ROUND_ANALYSIS.round16.md` s.3a. |
| **paired_with** | **solo.** Measured at arm time (this seat's own round-14/round-15 analyses, both committed today): 29 of 31 cells terminal, 0 currently open/dispatchable TOs -- the only 2 remaining groups (`rk-32`+chain P; `rk-48`/`rk-49`'s live arms and drain) are held on the three RESERVED words above, nothing for a parallel `/drive` to dispatch. Default-yes per Step 0.6 does not fire because there is no dispatchable lane right now. `2.0.0_SA_COO~Z` already owns re-opening each held cell under its own pair section the moment a word lands (both prior round analyses state this); this loop does not duplicate that act, it tracks and surfaces the wait. Re-assess to paired the tick a word lands and cells reopen. |
| **stop-condition** | `AMGT_RESAPP` `status: complete` per the register's 2-step close, OR HELD-AT-STOP per skill s.4 (every REACHABLE member complete, only the Andrew-RESERVED members remain -- likely given the current shape), OR the operator's stand-down. |

## WHAT TICK 1 WILL FIND (grounding, not re-derived a second time this session)

Both today's committed round analyses already establish the state this loop starts from: `ROUND_ANALYSIS.round14.md`
@`93cb6416e4` and `ROUND_ANALYSIS.round15.md` @`a73b85c64f`. No new open-calls sweep contradicts them as of this
commit; tick 1 runs the sweep fresh regardless, per the skill.

-- `1.0.0_SA_CTO~Z`
