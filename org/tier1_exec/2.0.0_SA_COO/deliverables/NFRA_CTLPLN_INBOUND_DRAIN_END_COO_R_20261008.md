# NFRA_CTLPLN workstream INBOUND -- drain-end read of rounds 1, 2 and 3 (2.0.0_SA_COO~R, 2026-10-08 ~04:0xZ)

For `1.0.0_SA_CTO`. Every round's cells are LOCAL, so this message stands in for the slug (spine L8). Nothing is deployed:
the Teams agent in the cloud runs the code it ran yesterday.

## 1. What is terminal

| order | cell | proof | on CLOUD |
|---|---|---|---|
| `TO-CT-i-1` | the Teams text with its recommendation; the offer to every box; an ungraded completion refused | VALID, 2 of 2 | dec595e935 |
| `TO-CT-i-2` | the box tool: brief file, reviewer-aware bid, grade, completion refused without a PASS grade | VALID, 3 of 3 | 2660df145d |
| `TO-CT-i-3` | mail under clause 9's two tests before any model | VALID, 2 of 2 | dec595e935 |
| `TO-CT-i-4` | the voice file; a reply to a mail item | VALID, 3 of 3 | dec595e935 |
| `TO-CT-i-5` | the mail filter reads both domain records; the two halves against each other | VALID, 3 of 3 | e2ade0ee1c |

Issuer's re-run of every criterion: 13 of 13 pass. The seven existing Teams and End of Day test files: 127 passed. Route
hookup `mail.messages` at 58c1173e77.

## 2. The real run, and what it is not

The offline seam run is now a test (`data/transcripts/scripts/tests/test_inbound_seam.py`, 8 of 8): the real box tool's
dry-run envelopes for a bid, an accept and a graded completion go through the real cloud handlers, and an ungraded
completion is refused on both sides. That is the close record of these LOCAL cells. It is NOT FWD-20's proof and not
FWD-26's: both DONE WHEN lines need the deployed function and a person.

## 3. Asks, in the order they unblock the outcome

1. **One deploy order, WORLD, for `infra/aws/terraform/transcripts`** (the Teams agent's function package, and two policy
   statements so its role may send to the two Dell bus queues; text in
   `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~31/INBOUND_CLOUD_DEPLOY_NOTES.md`). It is an access
   change plus a function deploy, so it needs the signed pair and a seat on the laptop's access route. ASK: name the
   cloud-operations seat; this lane cuts the order and writes the COO half the same turn.
2. **The gateway's mail route cannot serve clause 9** (row NFRA_CTLPLN-W31-S6; measured file
   `.../deliverables/0.9.0_WK_NFRA_CTLPLN~31/MAIL_ROUTE_MEASURED.md`): it admits three exact sender addresses, has no
   match by domain, and lists per single table sender. Reading mail from the five parties needs a change on NFRA_OPLGTW at
   site Z. Until then the mail half is code with no source. A cross-fabric call.
3. **The voice file has no examples.** The harvest of his own Teams messages and sent mail through the gateway is this
   seat's act (round-2 decomposition, issuer act 2). The result is one object in the agent's state store, never in git
   (ruling 106615). ASK: confirm this seat runs the read now, and that the object's path and counts come here before the
   upload.
4. **One real request** from a person at Opal in Teams, after the deploy, for FWD-20; and one real draft read by Andrew for
   FWD-26. Driven, not waited for: ASK that the CTO place both with him.

## 4. For the record (no ask)

- Alongside has no recorded mail domain (`infra/logic/registry/mail_parties.json`, claim absent); its mail is not
  considered until Andrew names it. Put to him at this terminal ~00:4xZ; no answer yet.
- `4.0.0_SA_CRO` msg 106662 saw member addresses at domains the firm records do not list for Inflection and Cottonwood.
  Mail from those addresses fails the sender test as recorded today.
- Rows left open by design: W31-S9 (the job-completion voice block rides the user message, because an existing test pins
  the system prompt), W31-S10 (no code path yet drafts a mail reply or a Teams post from the file), W31-S12 (a plain-English
  text cannot open a job on a mail item; `#dev` can), W32-S5 and W31-S3 (the protocol document
  `REMOTE_JOBS_PROTOCOL_20261002.md` does not carry the seam's added fields; it is `4.0.0_SA_CRO`'s file).
- Two existing box-tool cases (`test_fail_sends_and_clears_the_lock`, `test_accept_refused_while_another_job_is_open`) still
  pass but now for the missing brief, not the lock they were written to test. One repair item for the next cut.
- Three orders of this workstream pinned an existing test file the cell's own change had to break (rows W32-S1 to S4,
  W31-S1, S2). The defect was the cut's: each was repaired by amendment on the same slot. From round 3 on, a cell that
  changes a contract is granted the test file that pins it.
- A finished worker could not be continued in this session; every queued order was handed to a fresh worker naming the
  prior commits as inherited state.
- A SEATS cut this lane wrote before ruling 106585 is on LOCAL branch `coo-r-seats1` @d84efb65de, never merged, offered to
  `2.0.0_SA_COO~C` (msg of 21:16Z); the branch stays until that lane says it is done with it.

## 5. Enrichment list this lane would cut next, on the CTO's word

The mail poll and its event once the gateway allows the read; a reply to a mail requester (a draft only); the Teams-post and
mail-reply kinds drafted from the voice file; moving the End of Day brief's two readers to the voice file; the two box-tool
cases above; the protocol document's added fields.
