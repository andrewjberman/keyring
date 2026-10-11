# CTO ROUND-74 ANALYSIS -- IRPT_DASHBD (workstream B) -- answering the L10 slug for rounds 71 to 73 (2026-10-11 ~18:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v30.md`
@dbf7c2e292 (3.0.0_SA_CVO msg 5591). **Prior:** the round-71 analysis @a15e967740. **No PRD addendum.**

## 1. Where the project stands

No order open (the reviewer's count). No served write in rounds 71 to 73. Three pairs of this project are signed and none is
applied: R45 REFRESH 4 (this seat's half @e969a090cc), the thresholds-file swap (unsigned by ruling, below), and nothing else
waits on a half. The live function still reads `oNgy4rnr` (this seat's read at 17:52Z).

## 2. The slug's four items

1. **The thresholds exposure is a ceiling: 569 manifest keys by listing, one body read. RULED at 17:14Z (msg 5436), recorded
   here: the served manifests are left as they are.** A rewrite leaves every prior version in a versioned bucket and so
   removes nothing; removing versions is a delete. The values sit in the firm's own store, and eleven of eleven known
   readers were read: none passes the object onward (one passes a manifest on, with a null in that member). The fix stops
   new ones, in REFRESH 4. Andrew has been told the count and that removal is his if he wants it. Row D2-W100-S3 closes
   on REFRESH 4's first manifest read with six keys, not before.
2. **The tie-out is not closed: 185 classed, 51 contested, 8 unclassed; on 18 of the 51 the custodian's flow rows do not
   reproduce the served flow day by day (row D2-W111-S1).** The same flow days appear and the segment's dollars tie, so this is
   a question of which day a flow is put on, and it is this project's method. One cell reads the 18 day by day against the
   custodian's rows until the difference has a cause, counts and cause only. Until it does, the tie-out is shown with three
   numbers beside it, 51 contested, 18 of them unreproduced, 8 unclassed, and is not called closed.
3. **R45 REFRESH 4 waits on this seat's half: it does not.** Signed @e969a090cc at ~17:5xZ, after the slug's input was
   compiled. It waits on Monday's scheduled fire and an applier the gates admit.
4. **The thresholds-file swap (round 73): both halves are signed AFTER REFRESH 4 is applied and its first fire is read**
   (msg 5589). One change at a time on that function, so a manifest that reads wrong has one release to answer for it.

## 3. ENRICHMENT LIST for round 74 (ONE issuance)

1. The 18 unreproduced segments read day by day (item 2).
2. Nothing else is cut: the project's next acts are two applies, in order, each under its signed pair, and the first waits
   for Monday.

## 4. Acts only Andrew can do

- Removing prior versions of served manifests, if he wants them gone (CLAUDE.md, Agent Autonomy: S3 deletes). This seat's
  ruling is that it is not needed, and does not ask it of him.

## 5. What this analysis did not measure

It rests on the slug as filed, which states that the reviewer made no read of its own in these rounds. This seat read no
manifest and no segment.

-- 1.0.0_SA_CTO~DELL2
