# NFRA_CTLPLN decomposition -- WORKSTREAM INBOUND, round 1: FWD-20's thread, a request for work in Teams or in mail taken the whole way (issuer 2.0.0_SA_COO~R; cut 2026-10-07 ~22:0xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Why a workstream, and whose paths are whose.** `1.0.0_SA_CTO` ruling msg 106585: "2.0.0_SA_COO~C issues workstream SEATS
(C-SEATS clauses 1 to 7, FWD-21 to FWD-25) beside its round 5. 2.0.0_SA_COO~R issues workstream INBOUND (FWD-20 and clause 8:
one real Teams request end to end, then mail under clause 9). ... Disjoint write surfaces, one issuer each; say at each cut
which paths are whose." THIS workstream's paths: `data/transcripts/scripts/teams_chat/`, `data/transcripts/scripts/tests/
test_inbound_*.py`, `.tools/remote-job.py`, `.tools/tests/test_remote_job_review.py`, `.claude/skills/remote-drive/SKILL.md`.
It writes NO launcher, NO seat or rule file, NO gate, NO `org/calls/`, NO `/open-calls`, `/mstr-spawn`, `/mstr-kill`, `/unstick`
or `/agentbus` skill: those are SEATS. Orders carry `<workstream>INBOUND</workstream>`; worker slots are `~31` and up.

**Cut on:** PRD v0.18 @55e2de3227, ADMITTED (`python .tools/prd-signoff.py status NFRA_CTLPLN` at the cut). Carrier: FWD-20;
contract C-SEATS clauses 8 and 9; the six calls ruled in ADDENDUM v0.17 (C: a job starts on Andrew's reply to the text, as
today; D: the inbound seat sits on a Dell, which Dell is the bid's answer); brief Parts I.0, IV F2. Andrew at this terminal
~21:4xZ: "Yeah i need it for both teams and outlook" (record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_214xZ_COO_R_INBOUND_FOR_BOTH_TEAMS_AND_OUTLOOK_AND_AN_ANDREW_VOICE_MD.md`
@4f53112d76): mail is cut in THIS round, not a later one. The `andrew_voice.md` of the same word is NOT cut here: it is no
outcome of PRD v0.18 and is with the CTO (this seat's ask, msg of 21:48Z).

## The thread, as hops (FWD-20), measured at the base (laptop, CLOUD 3d04ce9c7c, read and not run)

| hop | what happens | exists today | this round |
|---|---|---|---|
| 1 | a person asks for work in Teams, or in mail to Andrew | Teams: yes, the agent polls chats (`tenant.py` `poll_chats`). Mail: no read for requests; `data/transcripts/scripts/outlook/` reads mail for YCharts reports only, through the gateway route `/hx/mail`, whose listing is not released (`pull.py` header) | `CT-i-3` (mail) |
| 2 | the agent recognises a request for work; Andrew gets ONE text: what was asked and what is recommended | partly: every unanswered message is texted with a reply draft (`on_chat_messages`, `assist.py` `offer_text`); nothing says "work is being requested" and nothing recommends (0 matches for "recommend" in either file); a job opens only when he texts `#dev` on his own | `CT-i-1` |
| 3 | on his reply the job is offered to every box and goes to the one with the most room, measured at the offer | partly: `assist.py:680` names two boxes by hand, so dell1 and dell2 are never offered a job; each bid is a CPU and memory reading taken at the bid (`.tools/remote-job.py` `cmd_bid`), and the device side already reads the register | `CT-i-1` |
| 4 | a seat started fresh for the job, handed a written brief, does it | yes by the skill's text (`/remote-drive` Half 1: spawn, `--brief-file`); the tool accepts a job with no brief file | `CT-i-2` |
| 5 | a seat that did none of the work grades it | no: 0 matches for a reviewer in the skill or the tool; `cmd_complete` sends on the manager's word alone | `CT-i-2` (box) and `CT-i-1` (cloud refuses an ungraded completion) |
| 6 | the person who asked is told, where they asked, that it is done | Teams: yes (`on_job_complete` drafts, his 1 sends, the requester's confirmation closes). Mail: no | `CT-i-3` records what a reply by mail needs |

**Rule 24.** Domain: the hops between "a person asks" and "the person is told", over two channels. By subtraction from the six
hops: 1 (Teams) and 6 (Teams) exist and are no cell; every other hop and channel is in a cell or named as owned elsewhere (the
gateway's mail route is NFRA_OPLGTW's; the two bus-send grants for the Dell queues are an access change, an issuer act after
the drain through the laptop's access route). Same grain: each cell is one side of one seam. One intent each. State coherence:
this round changes no deployed function and sends nothing; the cloud half reaches the cloud by ONE deploy after the drain.

## Cells

| cell | what | serves | carrier | risk | chain, slot |
|---|---|---|---|---|---|
| `CT-i-1` | the cloud half for Teams: the agent says in its one text when work is being requested, what was asked and what it recommends; the job is offered to every box of the device register; a completion with no reviewer grade is refused and Andrew is told | FWD-20 | brief O1, O3; clause 8 | LOCAL | A, `~31` |
| `CT-i-3` | the mail half: the two tests of clause 9 as code that runs before any model sees a message, the five domains read from the estate's records, a mail request turned into the same one text, and the measured read of what the gateway's mail route allows | FWD-20 | clause 9; Andrew ~21:4xZ | LOCAL | A, `~31` |
| `CT-i-2` | the box half: a job is accepted only with its brief file, a box with no live reviewer bids unavailable, a reviewer seat records the grade, and the tool refuses to report a job complete without a passing grade from a seat that is not the one that did it | FWD-20 | clause 8; brief O8 | LOCAL | B, `~32` |

## Edges and fan-out

- `CT-i-1 -> CT-i-3`: the mail half calls the recognise-and-recommend function and the text shape `CT-i-1` writes.
- `CT-i-2` shares only the SEAM below with `CT-i-1`; neither imports the other.

Two chains. `fanout: 2 of 2 chains, cap 8`.

## The seam between the box and the cloud (verbatim on `CT-i-1` and `CT-i-2`)

Additions to `org/tier1_exec/4.0.0_SA_CRO/deliverables/REMOTE_JOBS_PROTOCOL_20261002.md`; nothing in it is removed.
- `job.bid` payload gains `reviewer` (the serial of a reviewer seat live on the box at the bid, or null) and, when
  `available` is false, `unavailable_reason` ("job_open" | "no_reviewer").
- `job.accepted` payload gains `brief_sha256` (the SHA-256 of the brief file the seat was handed).
- `job.complete` payload gains `coo` (the serial that did the work) and `grade`: {`by` (a reviewer serial, never equal to
  `coo`), `verdict` ("PASS"), `record` (the repo path of the reviewer's grade record), `at`}.
- The cloud treats a `job.complete` whose `grade` is absent, whose `verdict` is not "PASS", or whose `by` equals `coo` as NOT
  complete: the job stays `working`, nothing is drafted to the requester, and Andrew is texted one line under the job's tag.
- A reviewer serial is `3.0.0_SA_CVO` with or without a `~lane`.

## Write set (disjoint)

- `CT-i-1`: `data/transcripts/scripts/teams_chat/tenant.py`, `assist.py`, `NAMES.json`, a new `gen_bus_devices.py` beside
  them, `data/transcripts/scripts/tests/test_inbound_cloud.py`.
- `CT-i-3`: a new `data/transcripts/scripts/teams_chat/mail_requests.py`, `data/transcripts/scripts/tests/test_inbound_mail.py`.
- `CT-i-2`: `.tools/remote-job.py`, `.tools/tests/test_remote_job_review.py`, `.claude/skills/remote-drive/SKILL.md`.

Hookup owned by no cell (the issuer's, at the merge): the one entry in `tenant.py` `ROUTES` that names `CT-i-3`'s handler.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE this round; the mail poll's clock is set by the deploy order after the drain.
- `comp-iam`: RUN by reading `infra/aws/terraform/transcripts/chat_assist.tf:88-89`: the agent's role may send to two bus
  queues, the laptop's and site Z's. The two Dell queues need two more statements. That is an access change: not in any
  cell; an issuer act below.
- `comp-adversary`: RUN per cell on each record face. BLIND: the model's judgment on a real message (every test fakes the
  model); the real run is the outcome's proof.

## The issuer's acts after the drain

1. Merge per chain end through `.tools/safe-merge.sh`; add the `ROUTES` hookup; `py_compile` and `ruff` once; the agent's
   existing test files once.
2. THE SEAM RUN on the merged trunk, offline: a bid, an accept, a grade and a complete produced by the real box tool with
   `--dry-run`, fed to the real cloud handlers under the test harness; one ungraded completion refused.
3. ONE deploy order for the agent's function and the two bus-send statements (`infra/aws/terraform/transcripts`), `WORLD`:
   a targeted apply under a signed pair, with its change-management entry. Another seat's transcripts-key apply is open in
   that root today; the order names it.
4. FWD-20's proof is one REAL request, never a replay ("a request replayed from a saved example fails the outcome"). It is
   driven, not waited for: this seat asks `1.0.0_SA_CTO` in its drain-end message to place one real small ask from a person
   at Opal in Teams, and one by mail once the gateway's route allows the read.

## Verification diet

Two mechanical criteria per order: the built behaviour with its difference control in the same test (a message that asks for
no work gets no recommendation; a completion without a grade is refused where one with a grade passes; a mail failing either
test of clause 9 never reaches the model), and one probe against the real neighbour (the real device register; the real
firm records; the real tool on this box).
