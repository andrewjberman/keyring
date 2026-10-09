# COMM_ASSIST decomposition -- round 9: the laptop side of FWD-4 -- mail fetched from the gateway's domain route, and every admitted client mail texted with a draft reply (issuer 2.0.0_SA_COO~R; cut 2026-10-09 ~00:5xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO` msg 107513 ("drive ... the laptop side of FWD-4 ready for site Z's mail release"), on Andrew's word of
~00:0xZ that an empty tick runs `/next-calls` and proceeds. PRD v0.2 ADMITTED (`805fec22c5`). FWD-4 ACCEPT: "an email from one
of the five firms whose body mentions Andrew arrives as a text with a draft reply, the client is flagged as a client, and mail that
does not name him does not text him". C-MAIL: admitted only from the five firms' own domains and only when the body names Andrew;
drafted, never sent. Andrew-direct ~22:5xZ (`c0a11edcc8`): "it always has to say andrew in the body text somewhere".

**Measured at the base (`box/laptop` 416b9c1260):**

- `teams_chat/mail_requests.py` holds the two tests (`considered`: sender domain from the estate's firm records, never typed;
  "Andrew" as a whole word) and the handler `on_mail_messages` (route `mail.messages`, in `tenant.ROUTES`). The handler texts a
  considered mail ONLY when the model reads it as a work request, and with `draft: ""`: no draft reply, and a client mail that asks
  for nothing reaches him not at all. That falls short of FWD-4's ACCEPT.
- NOTHING produces a `mail.messages` event: no poller reads mail.
- Site Z's gateway (NFRA_OPLGTW OG-md-1, in this trunk at `15b08fdca1`, BUILT AND HELD, not deployed) serves
  `GET /hx/mail/messages?sender_domain=<d>` (exactly one of `sender` / `sender_domain`; a window of at most 31 days; minimal
  rows; its own page token) and `GET /hx/mail/messages/{message_id}` (one message with its body, allow-by-key), under its own bearer
  `MAIL_BEARER` (`infra/aws/ec2/opal-gateway/app/mail_route.py`). The domain table ships empty.

**Rule 24.** Domain: FWD-4's hops: fetch (no code) -> the two tests (built) -> text with a draft reply and the client flag (short)
-> his reply (the mail reply path exists, `on_mail_reply`). Two cells on disjoint files. Not cells: the deploy, and the agent's
access to the mail bearer (a secret grant under a pair), both after site Z's release.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CA-m-1` | a mail poller in the minute clock: per firm domain, list the window since its own cursor through the domain route, fetch each new message by id, and send ONE `mail.messages` event per message; bounded calls; first run sends nothing | FWD-4 | LOCAL | A, `~2` |
| `CA-m-2` | the handler texts EVERY considered mail with a draft reply in his voice (mail section of the voice file), the sender flagged `CLIENT <firm>` (or `Opal`); the work-request lines stay, added when the model reads a request; still never sent | FWD-4 | LOCAL | B, `~3` |

**The contract between them** (pinned so they build in parallel): the poller sends `ldo.send("mail:<message id>", "mail.messages",
{"messages": [<the by-id route's row, unchanged>]}, event_id="mail-<message id>")`. The handler reads that row with its existing
`_sender` / `_body_text` (`from.emailAddress.address`, the body).

`fanout: 2 of 2 chains, cap 8`.

Hookup at the merge (the issuer's): `tenant.ingress` gains `_safe("mail", ...)` calling the poller.

Battery: `comp-schedule` DECLARED-NOT-APPLICABLE (inside the existing minute clock, bounded); `comp-iam` DECLARED-NOT-APPLICABLE
for the cells (no policy, no AWS call; the bearer grant is a later pair); `comp-adversary` RUN on each order.
