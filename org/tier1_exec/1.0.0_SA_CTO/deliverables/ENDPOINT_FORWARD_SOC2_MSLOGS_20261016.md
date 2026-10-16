# ENDPOINT (step 2, /endpoint --forward) -- SOC2_MSLOGS: if an Opal account is taken over, know what was seen, what left, and for how long

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-16 ~16:1xZ.
**Brief:** `docs/briefs/soc2-mslogs-compromise-exposure-brief-20261016.md` @0113e9f438 (242 lines, 18,018 bytes), by `4.0.0_SA_CRO~DELL1`.
**Andrew's word:** `org/tier1_exec/2.0.0_SA_COO~S1/ANDREW_DIRECT_20261016_1559Z_REFRAME_M365_LOGS_AS_SOC2_COMPROMISE_EXPOSURE_MACRO_SOC2_MSLOGS.md`.
**State:** NOT YET LANDED in a PRD; it waits on Andrew's "yes" on the DONE WHEN lines. It lands as the ENDPOINT section of the new PRD.

## Placement and register (L3, ruled here)

- **A new project, SOC2_MSLOGS, under a new macro, SOC2.** It inherits every built TCKT_MTADTA resource: the collector, the door and its two
  aliases, the group, the app, the KMS key and `opal-data-trino/m365-metadata/trino/`. TCKT_MTADTA closes as superseded, the way
  NFRA_WFSPINE closed into it.
  - **Why new rather than renamed:** outcome ids are permanent. Four of TCKT_MTADTA's ten outcomes (hand-offs, recurring workflows,
    timing, Ticket Center candidates) retire under "scrub all ticket center frameworks". A new project starts clean ids instead of
    carrying vacant ones.
- **Naming:** Andrew said "a new macro called SOC2_MSLOGS". The estate grammar is a four-letter macro plus a project suffix, so this reads
  as macro `SOC2` and project `SOC2_MSLOGS`. His "yes" confirms the split.
- **Box:** dell1, by his messages 4-5. The plan returns to `2.0.0_SA_COO~S1` to drive.

## Outcomes

  FWD-1  The responder names one Opal account and a time window, and reads everything it did in that window, in order
         DONE WHEN  EXERCISED -- one live read of a real account's real window through the one door
         ACCEPT     Andrew picks an account and a day and reads its sign-ins, mail and file activity in time order, and
                    recognises it as that person's real day. Nothing in it was prepared by hand, and it came from collection
                    that is running
         SOURCE     brief Part I thread, O1

  FWD-2  For a window, the responder knows the exposure: what was opened, and everything that left
         DONE WHEN  EXERCISED -- one window's exposure list read and checked
         ACCEPT     for a window he chooses, Andrew gets one list he could act on: the mail and documents the account
                    opened, downloaded or synced, and every outside person who got a mail, forward, share link or file from
                    it. Where Microsoft does not record mail being opened for Opal's licence, the list says so rather than
                    leaving it out
         SOURCE     brief O2, F6

  FWD-3  The responder can tell when a takeover began and when it stopped
         DONE WHEN  EXERCISED -- a deliberate drill sign-in, read back
         ACCEPT     Andrew signs in to his own account from somewhere unusual, on purpose, and later reads back the first
                    and last moment of that session correctly. An ordinary day of his reads with no such session
         SOURCE     brief O3, F4

  FWD-4  The responder sees what an attacker left behind, so it can be removed
         DONE WHEN  EXERCISED -- a planted forwarding rule found
         ACCEPT     a mail forwarding rule set on purpose on an account appears in the list of lasting changes, with when
                    it was made and from where, and its removal appears too
         SOURCE     brief O4

  FWD-5  For any Opal user, the responder can read what normal looks like for that person
         DONE WHEN  EXERCISED -- a person reads their own pattern and agrees
         ACCEPT     Andrew reads his own usual pattern (where and when he signs in, from which devices, how much he reads,
                    sends and shares) and agrees it describes him
         SOURCE     brief O5

  FWD-6  On asking, the responder sees which accounts are acting outside their own normal pattern
         DONE WHEN  EXERCISED -- the drill shows up, and the rest is not noise
         ACCEPT     after the FWD-3 drill, asking shows his account with the reason. Andrew agrees the other accounts listed,
                    if any, are worth a look rather than someone's ordinary travel or busy day. Nobody is told unprompted; he
                    asks
         SOURCE     brief O6, F5

  FWD-7  A quiet record can be trusted: "nothing happened" is never confused with "collection missed it"
         DONE WHEN  EXERCISED -- a deliberate pause reads as a gap
         ACCEPT     after collection is paused on purpose for an hour, that hour reads as a gap for every account, not as a
                    quiet hour. A gap too old to recover reads as lost
         SOURCE     brief O7

  FWD-8  Only the door reads the store, Andrew knows what a stolen login could still reach, and the record survives an attacker
         DONE WHEN  EXERCISED -- a refused direct read, and a stored copy that outlives turning auditing off
         ACCEPT     an administrator's direct read of the stored data is refused. Andrew holds a plain statement of what his
                    own, an admin's or any user's stolen login could still reach here. Records already copied stay readable
                    even if auditing is switched off inside Microsoft 365
         SOURCE     brief O8, F7

  FWD-9  An auditor can be shown that Opal monitors user activity and keeps the record safe and complete
         DONE WHEN  EXERCISED -- one auditor-style question answered from the system
         ACCEPT     Andrew can show an assessor, from the system itself, that collection is running for every account, that
                    its gaps are known, that only the door reads it, and that it answered a compromise question
         SOURCE     brief O9

## Rulings carried into the PRD (not outcomes)

- **Population: every account in the Opal tenant, with addresses as Microsoft records them.** Bronze is raw, as Microsoft sends it, and
  silver is the same events in parquet. This retires LGIC X18 departure (1) and the old population and field limits. Andrew's reframe
  words ("any opal user", "silver is just formatted bronze") are that word; his "yes" here confirms it on the conformance ledger.
- **The sign-in feed is added.** Whether it needs a permission beyond the current one is read at L4.
- **No alerting.** The moratorium stands, and FWD-6 is read on asking.
- **Retention:** no expiry until Andrew sets one. Storage is small, and deleting records would defeat FWD-8.

**NOT READ:** the project's task orders, decompositions, `project.json` phase and blocking, and its surprise channel.

-- 1.0.0_SA_CTO~DELL1
