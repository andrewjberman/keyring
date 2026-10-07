# NFRA_CTLPLN decomposition -- WORKSTREAM INBOUND, round 2: the voice file, FWD-26 (issuer 2.0.0_SA_COO~R; cut 2026-10-07 ~22:4xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Why round 2 and not a fourth order of round 1.** `1.0.0_SA_CTO` ruling msg 106606: "FWD-26 is 2.0.0_SA_COO~R's, in the same
round as the Teams thread and mail." Round 1 of this workstream was issued at 544c5c0cd6 before FWD-26 existed, and the
task-order gate admits one issuance per workstream and round. So the cell is cut as round 2, issued the same evening, on the
same chain and the same worker slot as round 1's cloud half, and the two rounds drain and deploy together.

**Cut on:** PRD v0.19 @6a24dd7db4, ADMITTED (`python .tools/prd-signoff.py status NFRA_CTLPLN` at the cut: ratified-text SIGNED,
current). Carrier: FWD-26; ADDENDUM v0.19; contract C-SEATS clause 10; Andrew's word
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_214xZ_COO_R_INBOUND_FOR_BOTH_TEAMS_AND_OUTLOOK_AND_AN_ANDREW_VOICE_MD.md`.

## Measured at the base (laptop, CLOUD 03eaa2342d, read and not run)

1. `daily_reports/eod/VOICE.md` (114 lines) is the End of Day writer's whole brief. Two readers: `data/transcripts/scripts/
   teams_chat/assist.py` `voice_md()` and `daily_reports/eod/eod_update.py` (`VOICE`). The function's package gets it by one
   line of `infra/aws/lambda/teams-chat-assist/build.sh`.
2. A Teams reply is drafted by `assist.draft_chat_reply` from the constant `CHAT_SYSTEM`; a job's completion message by
   `tenant._completion_draft` from `COMPLETION_SYSTEM`. Neither reads a voice file, and neither is shown a message he wrote
   except what is in that chat's own recent turns.
3. Messages Andrew himself wrote are reachable two ways: the Teams agent's own archive of chat messages in the transcripts
   bucket, and the gateway (his Teams and his mailbox), which a seat can read and a worker cannot.

## What the cut decides (C-SEATS clause 10 leaves these to the cell)

- **Where the file lives:** `data/transcripts/scripts/teams_chat/andrew_voice.md`, beside the agent that drafts in his name.
- **`daily_reports/eod/VOICE.md` this round:** its content is carried into the new file's End of Day section word for word,
  and a test fails if the two ever differ. Its two readers STAY on the old file this round ("or stays where it is"): moving
  them changes a post that goes out daily, and belongs in the round that also moves the package line. One enrichment item.
- **Who gathers his real messages:** the worker builds the file's shape, its loader, its use in every draft, and a harvest
  tool that fills a section from a RECORDED folder of messages. The read of his real Teams messages and sent mail through
  the gateway is the ISSUER's act after the drain, at this seat, read only; the recorded folder is outside every git tree.

**Rule 24.** Domain: the kinds of thing an agent writes in his name today, by subtraction from the agent's draft calls: a
Teams reply, a job's completion message to a requester, the End of Day post; and from clause 10: a reply to a client's mail, a
Teams post. Five kinds; "others as they arise" is an empty section added by name later, never a default bucket. One cell.

## The cell

| cell | what | serves | carrier | risk | chain, slot |
|---|---|---|---|---|---|
| `CT-i-4` | the one file of how Andrew writes, a section per kind of act with messages he wrote; a loader; every draft the agent writes in his name shown the section for its kind; a harvest tool that fills a section from a recorded folder of his own messages; the End of Day brief carried in word for word | FWD-26 | C-SEATS 10 | LOCAL | A (after `CT-i-3`), `~31` |

Edge: `CT-i-3 -> CT-i-4` (the mail kind's draft path and `assist.py` as `CT-i-1` and `CT-i-3` leave them). One chain.
`fanout: 1 of 1 chains, cap 8`.

## Write set

`data/transcripts/scripts/teams_chat/andrew_voice.md`, `voice.py` beside it, `assist.py` and `tenant.py` (the draft calls
only), `data/transcripts/scripts/tests/test_inbound_voice.py`. Round 1's `CT-i-1` and `CT-i-3` are drained from the same slot
before this order starts, so no two open orders write `assist.py` or `tenant.py` at once. `daily_reports/eod/VOICE.md`,
`eod_update.py` and `build.sh` are NOT in the set.

## Battery

- `comp-schedule`, `comp-iam`: DECLARED-NOT-APPLICABLE.
- `comp-adversary`: RUN on the order's record face. Stated here because it outlives the cell: his real messages carry client
  names (not wiped, his word of ~18:3xZ per clause 10), and once harvested they sit in a tracked file and are shown to the
  drafting model as examples. The harvest is the issuer's act and its result is put to `1.0.0_SA_CTO` before it is committed.

## The issuer's acts after the drain

1. Merge with round 1's chain A; hygiene once; the agent's existing tests once, the End of Day ones first.
2. THE HARVEST: his own recent Teams messages and sent mail read through the gateway at this seat, read only, into a recorded
   folder outside git; the harvest tool run on it; the filled file's path and counts to `1.0.0_SA_CTO` before any commit of it.
3. The deploy order of round 1 carries this file's package line.
4. FWD-26's proof is his own read: one real draft written from the file, texted to him as every draft is, and his word on it.
