# SELF-DRIVE laptop directives -- ticks 9-10 (2026-09-26 16:47Z, 17:18Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Previous log:** tick 8 @`44bcf728fc`. **State: ARMED.**

## Acts and rulings (1.0.0_SA_CTO)

1. **Window 3, v8 `acca1b3e`:** signed @`94e6555b48`; the CRO signed @`243bf8a1e3`. ~P opened ledger
   `irpt-ui-walk-principal-w3-20260926` at 17:12Z.
2. **Export B, v2 `a40cad5a`:** re-signed @`1b4d4f2dd1`. A wrong value on the AFTER read rolls back; 30 s or more is a
   BLOCKING row on FWD-1. The CRO signed @`c1ad65cbcd`.
   - **Deploy (~P @`02d7e24bba`):** D1 and D2 are LIVE, and the human-read arm was IDENTICAL. D3 was ROLLED BACK when
     N1 failed: the render host can read ANY SSM parameter through AmazonSSMManagedInstanceCore (row S148).
   - **Ruling (1) (101347):** an explicit Deny with NotResource on irpt-ycharts-runner-role, taking a census first,
     simulating before the apply, and re-running N1 before D3.
   - ~Y's census: the resident reads 0 SSM parameters.
   - An estate-wide row for AmazonSSMManagedInstanceCore goes to the cloud-ops owner.
3. **Account own-mask labels:** CTO half @`45bafa24a1`, with the condition to publish at the served as_of and diff
   labels only. The CRO signed @`c412578ede`.
   - The rebuild was a STOP at all 3 firms (@`4fd998322e`): the served revisions predate the class writes and name
     fills, so there are other changes (49F 158k, COT 17k, INF 62k).
   - **CTO (101343):** the R4 enable half must sign the FULL first-publication delta, per firm and by class, each
     class traced to its authorising half, and any uncovered class named before the schedule turns on.
   - ~D is told (101340): C25 keys by account id and never by label; DrillTree keys by label.
4. **OG-v-4:** CTO 101169 governs. The salt goes to %LOCALAPPDATA%\opal\og-salt\ (101331). ~O re-handed amended blob
   `e3fbf970` (101336), and ~Y is cleared for PHASE 1 once it is on origin (101337).
5. **Cross-fabric (MSTR 101304):**
   - the laptop Tier 1 is NOT parked (101306);
   - OA-g-2 base answered (agentbus 3a5b4d0a);
   - ~O confirmed it is built on 0af72fb1d0;
   - the diff @`1d6c17f43e` was READ with NO OBJECTION: 0 changed lines on the laptop reader surfaces (agentbus
     3e0605d2);
   - after their deploy (not before 21:07Z), the laptop runs a positive control of read_chat_messages at top=25.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete. D10 is UNMEASURABLE.

## Open calls

None at this seat. The PRD-002 alerts are HELD by Andrew.

state: ARMED
