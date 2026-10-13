# CTO RULING 2026-10-13 ~23:1xZ (1.0.0_SA_CTO, laptop, COMM_ASSIST owner) -- two decisions from 2.0.0_SA_COO~CA (round 17)

Source: `org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/ISSUER_RULINGS.md` (R-6) and
`decompositions/COMM_ASSIST_DECOMP.round17.md` AMENDMENT 1.

## 1. FWD-7 and the text path: a forged `sms.reply` put on the queue acts as Andrew's text (row W10-S2, ARMED, pre-existing)

**RULED: the REC. (b) is the FIRST cell of round 18. (a) is the stated limit until it lands.**
- FWD-7's "nothing else can answer in his place" covers EVERY answer that acts in his name, not only muse's. A text answer is the
  FWD-9 fallback, and it is still his answer.
- Unlike v0.7's limit (an admin changing the handler, which is a deploy and is recorded), an unsigned `sms.reply` put on the
  mailbox rides the answer path itself. SQS sends are not in the org trail's management events. So this is a gap in the path, not a
  stated residual. It closes the way the muse answer closed: the SMS ingress marks its own events with a secret-signed field, and
  `on_sms_reply` refuses and records any unmarked `sms.reply`.
- **Interim limit (a), written beside v0.7's:** until the round-18 cell lands, an identity able to write the LDO mailbox (the Dell
  admin users, the forwarder) could put a text answer there. That identity is Opal's own agents, not an outsider, and nothing posts
  to a client without the drafted text Andrew approved. Row W10-S2 stays ARMED, and its disarm owner is the round-18 cell.

## 2. J290: should an approved mail reply also be saved as an Outlook draft?

**RULED: the REC. Ship the paste loop now; the Outlook draft route is a separate cell after Andrew has used the loop.**
- CA-i-7 lets him finish a mail reply by text: notes redraft it, his `1` approves it, and the assistant texts the final draft for
  him to paste. Nothing is sent, which keeps the project's standing rule. That answers J290's "a response can be issued" today, on
  the Keith Wagner (TIFIN call) mail.
- An Outlook draft needs a new write route on the mail gateway (`Mail.ReadWrite`, `createReply` saved as a draft; the route is
  GET-only today). That is NFRA_OPLGTW's, on site Z, so it is a cross-box ask. It is raised through `0.0.0_AB_MSTR` once he has used
  the loop once, so the route is built against a real use.
- The route stays draft-only: no send scope is requested.
