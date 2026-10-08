# NFRA_CTLPLN decomposition -- WORKSTREAM INBOUND, round 3: two closing items of the thread before its deploy (issuer 2.0.0_SA_COO~R; cut 2026-10-08 ~03:0xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

Rounds 1 and 2 are drained: every order `complete` with a VALID instance, merged at CLOUD dec595e935 and 2660df145d, the route
hookup at 58c1173e77. Two things the drain showed are cut here as ONE small direct-act cell, LOCAL, before the deploy order:

1. **The mail filter does not read the second domain record.** `1.0.0_SA_CTO` ruling msg 106655 had `4.0.0_SA_CRO` record the
   mail domains of the two parties that are not tenant firms; they landed in `infra/logic/registry/mail_parties.json`
   (@f5accebd7c, msg 106662: Opal measured; Alongside absent, `considered` false). `mail_requests.firm_domains()` reads
   `scopes.json` only, so Opal's own mail is not considered today.
2. **The box half and the cloud half were never run against each other.** Each was tested against the seam's text. The
   issuer's seam run of round 1 (the real box tool's envelopes fed to the real cloud handlers) is made a test file so it runs
   at every later merge.

**Cut on:** PRD v0.20 @ce40c9292d, ADMITTED. Carrier: FWD-20; C-SEATS clauses 8 and 9; the round-1 decomposition's seam.

**Rule 24.** Domain: what stands between the drained code and its deploy. Two items, one cell; the gateway's mail route
(row W31-S6) and the missing Alongside domain are owned elsewhere (NFRA_OPLGTW; Andrew) and are in the drain-end message.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CT-i-5` | the mail filter takes the union of the firm records and the mail-parties record, considering only a party the record marks considered; and one test that feeds the real box tool's dry-run envelopes to the real cloud handlers | FWD-20 | LOCAL | A, `~33` |

No edge. `fanout: 1 of 1 chains, cap 8`. Write set: `data/transcripts/scripts/teams_chat/mail_requests.py`,
`data/transcripts/scripts/tests/test_inbound_mail.py`, a new `data/transcripts/scripts/tests/test_inbound_seam.py`.
Battery: `comp-schedule`, `comp-iam` DECLARED-NOT-APPLICABLE; `comp-adversary` RUN on the order's record face.
