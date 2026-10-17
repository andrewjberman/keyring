# ANDREW-DIRECT 2026-10-16 ~18:0xZ -- client-ops early-warning scans: fast-path, pptx deck, names anonymized

**Channel:** Andrew at the terminal of `4.0.0_SA_CRO~DELL1` (dell1), answering the CRO's plan for the client-ops early-warning
work (seeded by the Dave Victor postmortem). **Recorded by:** `4.0.0_SA_CRO~DELL1`, same turn.

VERBATIM (terminal):

> pptx, anonymize names, fast-path it. Let me know when the incidents are ready we start with those.

The three questions it answers, as asked: (1) deck format and anonymization; (2) CRO research plus a single-round brief to the
CTO, or fast-path; (3) delivery channel for the digest. Answer (3) is still OPEN: no send channel is chosen.

## The explicit ask behind the alert moratorium (CLAUDE.md section 5)

Andrew's own words to AJ Graff on Teams, 2026-10-16 17:26Z, VERBATIM:

> 1.) Outlook audit channel (which we collect automatically anyway via MS) looking for loose ends?
> (e.g. accounts operational but not resolved, unanswered emails, etc)
> 2.) Alerts on new cash accounts appearing in Schwab which are sitting more than X days.

And to Austin Graff on Teams, 2026-10-16 17:55Z: "We can start running scheduled scans on Outlook by the end of the day ...
specifically targeted at risky client ops scenarios, where things fall through the cracks. Think early warning system."

## How it is carried

- **Fast-path:** this work does not run the L1-L10 canonical workflow. Scope is exactly the early-warning scans and the deck;
  nothing wider is fast-pathed by this record.
- **Deck:** .pptx (not a published Slides artifact). Client names and account numbers are anonymized.
- **Order:** the postmortems come first; Andrew is told when the incident set is ready, and the work starts from those.
- **Moratorium:** lifted for this scope by the explicit ask above. Nothing sends until Andrew names the channel (OPEN item 3).

## Addendum, same session: the output surface

The CRO proposed one stream (Graph mail events + the Schwab daily file + the Tax SMA sheet) feeding six rules and one
open-items table. Andrew's reply, VERBATIM:

> and cast it on tv

- **Output surface:** the office TV, as a cast of an internal page showing the open-items stream.
- **Still OPEN:** the TV hardware and cast path; on-screen privacy (initials plus the last 4 digits is the proposal); who builds;
  and whether a Teams or email digest exists in addition to the TV.

## Addendum 2, same session: streaming ingestion

Andrew first set the order: streaming before casting, and casting is secondary. VERBATIM: "the casting is secondary, the
first thing is figuring out how to actually stream this + streaming email, like every 5 sec polling any fast moving
surfaces. any account/custodial stuff doesnt need to be polling because its uploaded once a day".

The CRO offered three options: Graph webhooks, Graph delta every 5 s, or both. It asked who approves the app-only Graph
access, and whether Teams is in round one. Andrew's reply, VERBATIM:

> delta 5s first, i approve, teams later

- **Email ingestion:** a Graph delta query every 5 s on Inbox and Sent Items of 49@ and the Opal staff mailboxes. Webhooks
  are deferred, and come only if 5 s proves too slow.
- **Access:** an app-only Graph credential with Mail.Read scoped to the monitored mailboxes, never Andrew's personal token.
  The tenant-admin approver is Andrew.
- **Custodial / account data:** no polling. It runs when the daily file lands, with a scheduled run as backstop.
- **Teams:** deferred to a later round.
