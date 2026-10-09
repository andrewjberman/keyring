## New approach

**There is no admissible dell2-side route for FWD-1/2/3, and I do not recommend looking for one.**
- C-IDENTITY (NFRA_TRNSPT PRD): the pull runs through the EXISTING Opal gateway under Andrew's account, with no new app
  registration.
- The gateway is "the only Microsoft sign-in path Opal runs".
- A dell2 route would be a second Microsoft identity path, which is both a contract break and a shadow route.

What is blockable here is not the route but the SIZE and QUEUE POSITION of the site Z act. Shrink it, and move the
remaining waits to their real owners:

1. **FWD-1/2/3: the site Z act is one env value.**
   - The 403s come from `TRANSCRIPT_MEETING_ALLOWLIST` (`infra/aws/ec2/opal-gateway/app/config.py:238`; "EMPTY allowlist =
     every meeting refused").
   - Adding the four meeting ids is a configuration change on the host, disjoint from r29 and MP-x-4.
   - Ask, through `0.0.0_AB_MSTR~DELL2` to `0.0.0_AB_MSTR~Z` (bus): cut the allowlist slot as a STANDALONE env release
     AHEAD of r29 and MP-x-4. Name the four ids and cite ruling @261e2c42a0 (site Z TAKES it).
   - Then `p18_readback.py`'s first landing runs here within the hour of the env change. The residual-wipe sweep is
     already exercised on its negative arm.
2. **The research meeting's organizer grant is Andrew's open call.** He is in session at this seat's terminal now, so it is
   surfaced to him directly in this turn.
3. **FWD-8, the a18 VERIFY at a laptop seat reported deaf since ~09:29Z:** relocate it as was done for s21 to `~TRL`. Ask
   `0.0.0_AB_MSTR~DELL2` to raise it MSTR-to-MSTR with the laptop as a hung-seat relocation (the /unblock skill's first
   step: relocate off a hung seat). ~T2 does not apply it.
4. **FWD-5 (s21 at laptop `~TRL`):** GO was relayed at 13:00Z, and the role was NoSuchEntity at 13:33Z, 33 minutes later.
   That is not yet hung. One liveness read through the laptop MSTR at the next tick. If there is no apply read by then,
   the same relocation path as item 3.
5. **Meanwhile, ~T2's own open work is in IRPT_ANLREQ (C-ABSORB c, d),** not here. FWD-9's TO-APPLY-t1 is GO'd and READ by
   the applier at 13:29Z. ~T2 grades it on landing (one served commentary drafted from a report). That is the live act
   that moves both projects.

## Why it is not blocked

- **FWD-1/2/3:** it waits on site Z, but on a one-value config change that can be released on its own. Asking for its
  queue position is an act ~T2 can take now, through its MSTR. The alternative route would violate C-IDENTITY, so "find
  another route" is not an approach.
- **FWD-5 and FWD-8:** the owners are on the laptop. One is 33 minutes into a GO (not hung). The other is reported deaf, so
  relocation is the named remedy and the laptop's to perform. Asking for it is ~T2's act.
- **FWD-6:** parked with an un-park condition (R21 AMENDMENT 2). Nothing to change.
- **FWD-9:** moving at the applier now.

## What changes for the COO

- **This tick:**
  - one message to `0.0.0_AB_MSTR~DELL2` with two asks for the bus: (a) the allowlist as a standalone env release ahead
    of r29, with the four meeting ids; (b) relocate a18 VERIFY off the deaf laptop seat;
  - grade FWD-9 when t1 lands.
- **Next tick:** one liveness read on s21 at `~TRL`; relocate if there is still no apply read.
- **On the allowlist landing:** `p18_readback.py`, first landing, then FWD-1/2/3 graded.
- **Andrew:** the organizer grant for the research meeting, already his open call.
