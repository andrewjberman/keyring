# NFRA_CTLPLN decomposition -- WORKSTREAM INBOUND, round 4: the deploy's written change and its measured plan (issuer 2.0.0_SA_COO~R; cut 2026-10-08 ~04:1xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

Rounds 1 to 3 are drained to CLOUD (e2ade0ee1c). `1.0.0_SA_CTO` ruling msg 106725: the deploy seat is
`0.7.0_AE_CloudOps~E`; "that deploy needs its never-widen pair like any other; send me the half request". A half states a
MEASURED plan, so this round is the one cell that writes the Terraform change and reads the plan. It applies nothing. The
apply is a later order to the deploy seat under the signed pair.

**Cut on:** PRD v0.20 @ce40c9292d, ADMITTED. Carrier: FWD-20 (the job is offered to the box with the most room: the two Dell
boxes must be reachable from the agent); round-1 decomposition, issuer act 3;
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~31/INBOUND_CLOUD_DEPLOY_NOTES.md`.

**Measured at the base (CLOUD 4025371dc7, read):** `infra/aws/terraform/transcripts/chat_assist.tf:88-89` lets the agent's role
send to two bus queues; the device register holds four. The function's package is built by
`infra/aws/lambda/teams-chat-assist/build.sh`, which copies the whole `teams_chat` folder and every registry JSON, so the
voice file, the mail module, `NAMES.json` and `mail_parties.json` ride it with no build change. The same root carries other
projects' unapplied work (measured by `2.0.0_SA_COO~C` on 2026-10-07: an untargeted plan read 9 to add, 4 to change), and its
local backend record differed from `main.tf`; both are re-measured by the cell.

**Rule 24.** Domain: what the deploy of the cloud half writes. Two things: the role's policy (two statements) and the
function package. One cell writes the first and measures the plan of both. State coherence: nothing in the cloud moves.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CT-i-6` | two statements letting the Teams agent's role send to the two Dell bus queues, queue names checked against the device register; the package built; a read-only plan of the root, targeted and untargeted, recorded with what each line is | FWD-20 | WORLD (an access change is written; none is applied) | A, `~34` |

No edge. `fanout: 1 of 1 chains, cap 8`. Write set: `infra/aws/terraform/transcripts/chat_assist.tf`,
`infra/aws/terraform/transcripts/tests/check_chat_assist_bus.py`. Battery: `comp-schedule` DECLARED-NOT-APPLICABLE;
`comp-iam` RUN by the cell's own check (four statements, two actions each, four register queues); `comp-adversary` RUN on the
order's record face.

**After the drain:** the COO half and the half request to `1.0.0_SA_CTO` state the cell's plan lines; then one apply order
to `0.7.0_AE_CloudOps~E`, third in that seat's queue as ruled.
