# NFRA_CTLPLN decomposition -- WORKSTREAM INBOUND, round 5: the representative voice set's tools, and a package that does not depend on line endings (issuer 2.0.0_SA_COO~R; cut 2026-10-08 ~09:3xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

Rounds 1 to 4 are drained; the Teams agent's deploy is APPLIED (order NFRA_CTLPLN.TO-APPLY-11, live 08:15Z 2026-10-08), not
EXERCISED. Two rulings of `1.0.0_SA_CTO` name this round's two cells:

- msg 106834, condition 2: "The representative set is the next cell: across kinds of act and across more than two days, with
  mail once the gateway serves it. FWD-26's exercise, Andrew reading one draft, waits for that set".
- msg 106855: "The package's dependence on line endings is a build defect: a cell, naming the two registry files" (row
  NFRA_CTLPLN-S27: a rebuild of the last deployed commit did not reproduce the deployed hash on this box).

**Cut on:** PRD v0.20 @ce40c9292d, ADMITTED. Carrier: FWD-26, C-SEATS clause 10; FWD-20 (the deploy's rollback).

**Measured at the base (CLOUD 2d7e46b76a):** the first cut of the examples object holds 12 Teams replies, the newest, two days
(`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_CTLPLN_VOICE_EXAMPLES_FIRST_CUT_UPLOAD_COO_R_20261008.md`); it was recorded by
a scratch script of this seat that is not in the repository. `voice.py harvest` keeps the newest N and has no other choice.
In this lane's worktree `git ls-files --eol infra/logic/registry` reads every one of 13 files `i/lf w/lf`; the applier's row
says two of them are CRLF in the SHARED tree. Which two, and why, is the cell's first read.

**Rule 24.** Domain: what stands between the first cut and a set Andrew can read a draft from, and between the deploy and a
rollback that can be rebuilt. Two cells, disjoint files. The gateway's mail read and Andrew's own choice of messages are
owned elsewhere (NFRA_OPLGTW; Andrew) and are not cells.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CT-i-7` | the recorder of his own Teams messages from the agent's archive as a tool in the repository, by kind of act, counts only; and a harvest that spreads its choice across days and conversations in place of the newest N | FWD-26 | LOCAL | A, `~35` |
| `CT-i-8` | the Teams agent's package is byte-identical whatever line endings its inputs have in the working tree; the two registry files named and the cause stated | FWD-20 | WORLD by its path under `infra/`; nothing is deployed | B, `~36` |

No edge. Two chains. `fanout: 2 of 2 chains, cap 8`.

Write set: `CT-i-7`: a new `data/transcripts/scripts/teams_chat/voice_record.py`, `voice.py`, a new
`data/transcripts/scripts/tests/test_inbound_voice_record.py`, and `data/transcripts/scripts/tests/test_inbound_voice.py` (the
test that pins `voice.py`, granted with the cell that changes it). `CT-i-8`: `infra/aws/lambda/teams-chat-assist/build.sh`, a
new `infra/aws/lambda/teams-chat-assist/tests/test_build_reproducible.py`.

Battery: `comp-schedule` DECLARED-NOT-APPLICABLE; `comp-iam` DECLARED-NOT-APPLICABLE (no policy; the recorder reads the
archive with the box's existing identity, and no worker runs it against the real archive); `comp-adversary` RUN per order.

**After the drain:** this seat runs the recorder and the spread harvest on the real archive, sends `1.0.0_SA_CTO` the counts
per kind and the firm-name count before any upload (ruling 106829), and replaces the first cut. The package change reaches
the cloud with the next deploy of the module, under its own pair; no deploy is cut for it alone.
