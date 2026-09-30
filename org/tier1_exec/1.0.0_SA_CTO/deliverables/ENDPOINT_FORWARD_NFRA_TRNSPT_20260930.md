# ENDPOINT (step 2, /endpoint --forward) -- NFRA_TRNSPT (D9), the Opal transcript database

**NOT YET LANDED IN A PRD.** The PRD does not exist; this block belongs under the section titled `ENDPOINT (step 2, /endpoint --forward)` in
`org/missions/D9/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` (L4). Until then this file is the carrier. Author 1.0.0_SA_CTO, 2026-09-30.
Owner fabric: this laptop fabric (Andrew-direct 2026-09-30, record `ANDREW_DIRECT_20260930_001xZ_TRNSPT_THIS_FABRIC_EDICT_STAYS_IN_COO_STARTUP.md`).
**AWAITING ANDREW'S CONFIRMATION of every DONE WHEN line (L2 gate).**

Brief: `docs/briefs/nfra-trnspt-opal-transcript-database-brief-20260929.md` @4206994dd3 (205 lines, incl. the 2026-09-29 addendum).
Kind: backend/infrastructure product with a data pipeline -- FWD-1 is the thread (spine v3.18): one real consumer, one real use, one trace.

FWD-1  Andrew opens the database on a Monday afternoon and finds that morning's meeting, with who said what, and nobody touched anything
       DONE WHEN  EXERCISED -- one real Monday meeting followed from its end to the readable transcript, no person running a step
       ACCEPT     Andrew reads the Monday meeting in the database the same day; it fails if anyone had to sit at a keyboard or run a command
       SOURCE     brief O1, Part III

FWD-2  Every regular investment meeting arrives on its own, the Research Meeting included
       DONE WHEN  EXERCISED -- one occurrence of each of the four meeting types has arrived unaided
       ACCEPT     for each of the four meeting types, the latest meeting is in the database without anyone fetching it
       SOURCE     brief O2, Part IV findings 6-7

FWD-3  Someone who needs last quarter's meetings gets them, and new meetings no longer expire unread
       DONE WHEN  EXERCISED -- a named past meeting still held by Microsoft has been checked in the database, and a new one landed before expiry
       ACCEPT     Andrew names a past meeting that Microsoft still holds and finds it; no meeting that could be fetched on 29 September is later found missing
       SOURCE     brief O3, finding 5

FWD-4  A person can tell what the database holds and what it is missing, and why
       DONE WHEN  EXERCISED -- asked about one missing meeting, a person gets its reason
       ACCEPT     for any meeting and date, the answer is "here" or a cause (never recorded, expired, refused); never a shrug
       SOURCE     brief O4

FWD-5  An analyst reads a transcript as structured speech, not a raw file
       DONE WHEN  EXERCISED -- one analyst has read one meeting this way, including one of the 29 existing Research Meeting transcripts
       ACCEPT     an analyst who now opens a file to find what was said about one company gets it without opening the file
       SOURCE     brief O5, finding 11

FWD-6  A market update (a PowerPoint) is put in the database and kept exactly as received
       DONE WHEN  EXERCISED -- one real market update placed and later compared with the original
       ACCEPT     someone places a market update and later gets back the identical deck; a re-saved copy is recognisable as the same deck
       SOURCE     brief O6, addendum A1, A3

FWD-7  Analysis commentary (email supplied by Alyssa) is put in the database and kept exactly as received
       DONE WHEN  APPLIED -- the landing place and the source's access route are in place; the first real supply is an enrichment
       ACCEPT     a piece of commentary sent by Alyssa is later retrievable word for word, and Alyssa (not Andrew) is the one whose access is used
       SOURCE     brief O7, addendum A2 -- how it arrives is OPEN with Andrew/Alyssa

FWD-8  Andrew can show who may read the database, and it is only the people he named
       DONE WHEN  EXERCISED -- a third person is tried and refused, in front of Andrew
       ACCEPT     Andrew and the terminal seat's account can read; a third person cannot by any route, and Andrew sees that shown, not asserted
       SOURCE     brief O8

FWD-9  A builder asks one question across meetings, updates and commentary
       DONE WHEN  APPLIED -- the shared layer that makes it possible is in place; a live question is a later round
       ACCEPT     an analyst asks which securities were discussed this quarter and gets one answer covering all three, not three searches
       SOURCE     brief O9 -- later round, not a round-1 promise

UNCOVERED / OPEN (owned, not silently dropped):
  - Who may sign in to Microsoft with nobody present (stored sign-in vs application permission): SECURITY DECISION, Andrew's. Gates FWD-1.
  - Research Meeting refusal cause (organizer Lauren Harmon): unknown. Gates FWD-2.
  - Whether Microsoft's transcript-finished notification can be subscribed to: UNVERIFIED (finding 8); a schedule is the fallback.
  - Owner of the commentary pull (Alyssa's agents or this project): open (A3).
  - Gateway tools: NFRA_OPLGTW, 1.0.0_SA_CTO~O, site Z: dependency, not owned here.
  - Whether Microsoft's retention can be extended by policy: tenant-owned; not a build.

GROUNDED ON: the brief in full (lines 1-239). NOT READ: the register, task orders, project JSONs, the prior-art files under REFS TO CARRY.
