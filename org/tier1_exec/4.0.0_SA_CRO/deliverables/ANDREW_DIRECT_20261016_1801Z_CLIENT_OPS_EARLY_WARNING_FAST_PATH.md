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
