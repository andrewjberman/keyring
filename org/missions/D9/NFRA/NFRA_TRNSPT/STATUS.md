# NFRA_TRNSPT -- status (FAST: /closer-drive under lease `NFRA_TRNSPT`, the one remaining round)

Seat `2.0.0_SA_COO~D` (CLAUDE), holding this round in place of the project's own lane `2.0.0_SA_COO~T` (dark). Authority:
1.0.0_SA_CTO RULINGS batch 82 @dcdd1989d5 (msg 103707, 2026-10-01T11:18Z):
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`; the round's content is
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_2_20261001.md` section 2. Contract: PRD
`org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` v0.1 (ENDPOINT unchanged). Reviewer `3.0.0_SA_CVO` (grades each
landed pin after the fact). **As of 2026-10-01T11:4xZ.** An Investor Reporting item that becomes ready INTERRUPTS this round
(batch 82 item 3); DSGN_REBRND's round 3 stays behind both (item 6).

## Pins

| What | Value |
|---|---|
| Lease | FAST `NFRA_TRNSPT` until 2026-10-01T15:40:09Z, seat 2.0.0_SA_COO~D, surface `data/transcripts`, `org/missions/D9/NFRA/NFRA_TRNSPT`; armed by this seat 11:40Z (`org/mcp/drive-mode.log`) |
| FULL -> FAST boundary | 17 of 17 task orders read `complete` at 11:25Z (rounds 1 and 2); no worker is running, nothing is superseded, nothing new is cut |
| Round's rows | S9, W4-S8 (`surprise-channel/remediations/REMEDIATION_v1.md`, OPEN, owner 2.0.0_SA_COO~T) and S14 (`REMEDIATION_v2.md`, OPEN); S13 is site Z's and is reported met |
| Mail bearer | Secrets Manager `gateway/mail/bearer`: `describe-secret` answers under the laptop caller (IAM user Andrew_Berman), metadata only, 11:40Z. The value is read in-process at call time, never printed or committed |
| The gateway route | `/hx/mail`, REPORTED live by site Z since 10:43:56Z (0.0.0_AB_MSTR 103704, 103706); NOT exercised on the laptop. Its code and record are site-Z LOCAL (daa56d81ac, 2c8248a87e): the laptop tree has no `mail_route.py`, no route-names `mail` entry and no caller (`outlook/pull.py` `GatewayMailSource` is a stub that raises) |

## Live thread

State: NOT LIVE for the communications workstream (FWD-7 has run on no admitted real message). The transcripts
workstream's hops 3-6 were exercised in rounds 1 and 2; hops 1-2 wait on the same route family.

## Write claims

- `2.0.0_SA_COO~D`: `data/transcripts/scripts/tests/test_wipe_planted.py` and the wipe-gate record's writer (item 1, row S14).

## Next (in order)

1. **Row S14** -- the planted-wipe test writes its gate record to a temp path; the committed record is produced by one
   explicit command. Needs nothing from site Z.
2. **Row W4-S8 / review Q2** -- the wipe's stated limit (`lowercase_standalone_name` is not removed; ordinary-word
   surnames rely on a small stopword list) is written where a reader meets the data: the silver table's own contract or
   column note. Needs nothing from site Z.
3. **The laptop caller** -- `GatewayMailSource` against the route's request contract, the bearer read by name in-process;
   it writes the recorded directory `pull.py --replay` already reads (`<graph_id>.message.json`,
   `<graph_id>.attachments.json`) plus the PDF's bytes with the route's hash. BLOCKED on the contract (below).
4. **The control on the sample** (batch 82 item 4) -- is site Z's 582,728-byte PDF the message this project's row names
   at 585,757 bytes (Manav, 2026-08-11)? Stated before the sample is called landed.
5. **The real run** -- `precision.py` over the recorded directory (every message's booleans, no text),
   `pull.py --replay <dir> --apply` (bronze), `silver.py --apply`, `held_out=<h>` read off the real silver run, and the
   silver READ by the named reader this seat runs as. Rows S9 and W4-S8 are graded here.
6. The thread trace re-run and the silver census (FWD-1, FWD-2).

## Parked (one line each, owner + the condition that un-parks it)

- `/hx/mail`'s REQUEST CONTRACT (base URL, prefix, the two path templates, what the ids are, the bearer header, the
  PDF response shape): owner site Z's gateway owner; asked through 0.0.0_AB_MSTR at 11:41Z. Un-parks items 3 to 5.
- The fourth meeting type (row S11): a person act, one calendar invite of that type (batch 82 item 5). Does not hold
  this round.
- The second named reader (`opalbloomberg@opalinvest.com`) has no AWS principal yet (FWD-8): the silver is read by the
  one named reader this seat runs as, and that is stated, not hidden.

## Limits

- No reader beyond the two named ones reads a real mail row before the wipe's limit is stated and the held-out rate is
  read (the CVO's condition, adopted by the CTO).
- No vendor model call, no ticket write, no alert, no schedule and no Terraform in this round. Bronze receives only
  bytes that came from the route, never a copy relayed through a model.
- No message body, sender address or client name is written into a committed file or a broker message.
