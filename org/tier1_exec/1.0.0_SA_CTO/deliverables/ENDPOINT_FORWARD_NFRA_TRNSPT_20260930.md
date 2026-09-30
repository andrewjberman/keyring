# ENDPOINT (step 2, /endpoint --forward) -- NFRA_TRNSPT (D9), the Opal communications database and the commentary drafter

**NOT YET LANDED IN A PRD.** The PRD does not exist; this block belongs under the section titled `ENDPOINT (step 2, /endpoint --forward)` in
`org/missions/D9/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` (L4). Until then this file is the carrier. Author 1.0.0_SA_CTO. Revision 2, 2026-09-30 ~03:5xZ
(revision 1 was @19b4670). **AWAITING ANDREW'S CONFIRMATION of every DONE WHEN line (L2 gate).** Ids are permanent: FWD-7 is amended IN PLACE; FWD-10 and FWD-11 are new; no id is renumbered.
Owner fabric: this laptop fabric (Andrew-direct 2026-09-30, `ANDREW_DIRECT_20260930_001xZ_TRNSPT_THIS_FABRIC_EDICT_STAYS_IN_COO_STARTUP.md`). D9 is already placed LAPTOP (MSTR 103134);
NFRA_TRNSPT is not yet in D9's `members.projects`, which is the L3 carrier.

Briefs: `docs/briefs/nfra-trnspt-opal-transcript-database-brief-20260929.md` @4206994dd3 (L1) and
`docs/briefs/nfra-trnspt-commentary-ingestion-expansion-brief-v3-20260930.md` @7d7ff17def (consolidated; wins over v1 and v2).
Kind: backend/infrastructure product with a data pipeline and a drafting service. FWD-1 is the thread (spine v3.18).

FWD-1  Andrew opens the database on a Monday afternoon and finds that morning's meeting, with who said what, and nobody touched anything
       DONE WHEN  EXERCISED -- one real Monday meeting followed from its end to the readable transcript, no person running a step
       ACCEPT     Andrew reads the Monday meeting in the database the same day; it fails if anyone had to sit at a keyboard or run a command
       SOURCE     L1 brief O1, Part III

FWD-2  Every regular investment meeting arrives on its own, the Research Meeting included
       DONE WHEN  EXERCISED -- one occurrence of each of the four meeting types has arrived unaided
       ACCEPT     for each of the four meeting types, the latest meeting is in the database without anyone fetching it
       SOURCE     L1 brief O2, findings 6-7

FWD-3  Someone who needs last quarter's meetings gets them, and new meetings no longer expire unread
       DONE WHEN  EXERCISED -- a named past meeting still held by Microsoft has been checked in the database, and a new one landed before expiry
       ACCEPT     Andrew names a past meeting that Microsoft still holds and finds it; no meeting that could be fetched on 29 September is later found missing
       SOURCE     L1 brief O3, finding 5

FWD-4  A person can tell what the database holds and what it is missing, and why
       DONE WHEN  EXERCISED -- asked about one missing meeting, a person gets its reason
       ACCEPT     for any meeting and date, the answer is "here" or a cause (never recorded, expired, refused); never a shrug
       SOURCE     L1 brief O4

FWD-5  An analyst reads a transcript as structured speech, not a raw file
       DONE WHEN  EXERCISED -- one analyst has read one meeting this way, including one of the 29 existing Research Meeting transcripts
       ACCEPT     an analyst who now opens a file to find what was said about one company gets it without opening the file
       SOURCE     L1 brief O5, finding 11

FWD-6  A market update (a PowerPoint) is put in the database and kept exactly as received
       DONE WHEN  EXERCISED -- one real market update placed and later compared with the original
       ACCEPT     someone places a market update and later gets back the identical deck; a re-saved copy is recognisable as the same deck
       SOURCE     L1 brief O6, addendum A1, A3

FWD-7  (AMENDED IN PLACE) Investment feedback that Manav sends a client with a YCharts report attached is filed in the database on its own, every day, and never altered
       DONE WHEN  EXERCISED -- one real such email followed from its sending to its filed copy by the ordinary daily run, no person starting it
       ACCEPT     Andrew finds a real feedback email the next day in the database; the original is kept exactly as received and only two people can read it;
                  the searchable copy has client names and identifying numbers removed; an email that does not meet all three tests (Manav or another named
                  author, a client recipient, a YCharts report attached) is not treated as feedback
       SOURCE     v3 brief sections 2-5; Andrew-direct 2026-09-30 (own ingestion, criterion, daily pull from his mailbox)
       (previous wording, revision 1: "Analysis commentary (email supplied by Alyssa) is put in the database and kept exactly as received", APPLIED. Retired because the source is
       now Andrew's mailbox, not Alyssa's supply. This is a scope change to the same outcome, not a shrink: it now asks for EXERCISED.)

FWD-8  Andrew can show who may read the database, and it is only the people he named
       DONE WHEN  EXERCISED -- a third person is tried and refused, in front of Andrew
       ACCEPT     Andrew and the terminal seat's account can read the original; a third person cannot by any route, and Andrew sees that shown, not asserted.
                  A separate, narrower reader may see only the copy with names and numbers removed
       SOURCE     L1 brief O8; v3 brief section 4 (a scoped role reads the wiped copies only)

FWD-9  A builder asks one question across meetings, updates and commentary
       DONE WHEN  APPLIED -- the shared layer that makes it possible is in place; a live question is a later round
       ACCEPT     an analyst asks which securities were discussed this quarter and gets one answer covering all three, not three searches
       SOURCE     L1 brief O9 -- later round, not a round-1 promise

FWD-10 (NEW) When someone generates an analysis report in Investor Reporting, a draft commentary in Opal's voice appears for an Opal person to review, without slowing the report
       DONE WHEN  EXERCISED -- one real report generated, and its draft commentary opened by the person who asked for it
       ACCEPT     the person who generates a report (first Alyssa, later advisors) finds a ticket with a draft written from past commentary for a similar report;
                  the draft never reaches an advisor unless a person sends it; the person who asked can claim and finish their own ticket; the report itself is never
                  late or failed because of the draft; nothing in the draft identifies another client or firm
       SOURCE     v3 brief sections 1, 7, 8; Andrew-direct 2026-09-30 (Analysis tab tie-in, Ticket Center, draft only, Kimi K3, requester may claim own ticket, all tickets)

FWD-11 (NEW) The report itself is attached to the commentary ticket, not linked
       DONE WHEN  EXERCISED -- a person opens the report from the ticket, and a person at a different firm is tried and refused
       ACCEPT     the Opal person who opens the ticket opens the actual report from it; a person at another firm cannot open it
       SOURCE     v3 brief addendum 3; Andrew-direct 2026-09-30 ("the text is just included + attachment included on the ticket"). Depends on the ticket system's
                  attachment work (D7, now on the laptop); until it lands the ticket carries the text and a link, so FWD-10 does not wait on it.

DEPENDENCIES OWNED ELSEWHERE (named, not built here):
  - Unattended Microsoft sign-in and how long a stored one lasts: NFRA_OPLGTW / Andrew's security decision. Gates FWD-1 and FWD-7 in production.
  - The hook that fires when a report is READY: IRPT_BCKEND (proposed: a stream on the requests table). Gates FWD-10.
  - The ticket type, the service identity, dropping the "requester cannot claim" block on ALL tickets, and attachments: D7 (OPAL_TICKET_VNEXT). Gates FWD-10 and FWD-11.
  - The ticket system's deployed security state (the 2026-08-12 finding): read before client-derived text goes into tickets. Gates FWD-10.
  - The first hosted-model call: needs Andrew's per-use word, given for the first call after the wipe test passes (record `ANDREW_DIRECT_20260930_03xxZ_TRNSPT_OPEN_CALLS_ANSWERED_TICKET_CENTER_OWN_INGESTION.md`).

OPEN, owned:
  - Research Meeting refusal cause (organizer Lauren Harmon): unknown. Gates FWD-2.
  - How a YCharts report is recognised in an attachment (one look at a real one): gates FWD-7's third test.
  - Whether Yang's addresses join the author table and their addresses: data to supply (FWD-7).
  - Same-firm or cross-firm precedent for the drafter: Andrew answered "across all firms"; the wipe must then remove firm and advisor names (v3 addendum 2).

GROUNDED ON: the L1 brief and the v3 brief in full, plus the Andrew-direct records they cite. NOT READ: the register, task orders, project JSONs, Ticket Center code, IRPT code (read by the CRO's subagents; this seat did not re-open them).
