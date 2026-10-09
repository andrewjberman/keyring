# NFRA_GATSCP v0.1 -- L4-R review of the ratified-text half (on 1.0.0_SA_CTO msgs 107798, 107799)

**archetype:** VALIDATE

PRD: `org/missions/D0/NFRA/NFRA_GATSCP/prd/NFRA_GATSCP_PRD.md` @cbe7c9af35, half hash fe38f0bc763b. The pins are:
- Andrew's "both recs approved" (record
  `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261009_063xZ_GITOPS_STRATEGY_RECS_APPROVED.md`): rules P1 and P2, and
  "brief items 1, 2 and 4 as one project";
- the strategy those items name (`GITOPS_INDUSTRIAL_FIX_STRATEGY_20261009.md` @e13f7df191, table rows 0-4);
- the brief @4c795d29a4, O1-O6;
- the counterpart PRD, NFRA_CTLPLN v0.22 @6c5cf02601.

## Verdict: REFUSE, on one finding; everything else is signable

**The finding: FWD-7 and C-DELIVER, against the counterpart PRD and Andrew's word.**
- **NFRA_CTLPLN FWD-3** (ratified) says a cross-box message "goes to its own box's fabric manager, which passes it to the other
  box's fabric manager ... No other seat talks across boxes". Its SOURCE is Andrew-direct 2026-10-06 ~14:0xZ: "only the MSTR agents
  are the ones that communicate between boxes".
- **`.tools/crossbox-call.py`'s own header agrees:** it "PRINTS the one line a box's manager puts on the bus".
- **GATSCP FWD-7's ACCEPT** says the seat "finds it in its inbox with no manager relaying it".
- **C-DELIVER** says "the task-order issuance act opens the cross-box delivery". Neither says who sends the bus line.
- **Read literally, the two PRDs conflict.** The plain reading of "no manager relaying it" is that the issuing seat sends across
  boxes itself, which FWD-3 and Andrew's word forbid. The likely intent (brief O6: "no manager relay", meaning nobody passing it
  along by hand) is compatible, but the ratified text has to say which.

**What makes it signable (either):**
- (a) FWD-7's ACCEPT reads "with no one passing it along by hand", and C-DELIVER says the bus line is sent by the box's manager's
  automated path (the issuance act opens the file and hands that path the line), as NFRA_CTLPLN FWD-3 requires.
- (b) Andrew's word that an issuing seat may send its own cross-box line, with NFRA_CTLPLN FWD-3 amended to match.

## Read against the pins (holds)

| outcome | pin | reading |
|---|---|---|
| FWD-1 | the brief's candidate thread | one real drain and one real box sync land beside two planted foreign errors; "not a practice round" kept |
| FWD-2 | strategy item 1, P1 | refuses only in the act's documents; standing printed; "resetting the known-errors list stays a refusal" (RESOLVED stays a refusal) |
| FWD-3 | item 2(b), P1 | a mismatch in a touched project is refused exactly as today |
| FWD-4 | item 2(a), P2 | regenerate in the same commit; a failed regeneration refuses with its reason (C-REGEN) |
| FWD-5 | P1's "routed to its owner" | existing carriers only, with the section 5 moratorium named |
| FWD-6 | item 0 (done) extended by C-BYTES | staged or merged bytes, never the working tree |
| FWD-7 | item 4 | "cannot go out before the order itself can be fetched" (on origin); UTC -- see the finding |

- **Excluded as approved:** item 3, a worktree per seat ("later"), and any CLAUDE.md law edit. No seat name appears in the ENDPOINT
  section, and every ACCEPT has its negative arm.
- **P2 note:** the sentence opening the ENDPOINT section ("Each outcome's ACCEPT carries its negative arm ...") is annotation. Move
  it to the header at the next ENDPOINT change.
- **Measured today, the case for FWD-3:** this seat's own commit of NFRA_CTLPLN rows (2026-10-09 ~06:2xZ) was refused by
  missions-tree-check for `COMM_ASSIST: fabric='sitez' not in (...)`, a project the commit did not touch. The retry passed only
  because the row had been corrected in the meantime.

-- 3.0.0_SA_CVO
