# COMM_ASSIST decomposition -- round 17: muse reads and answers (issuer 2.0.0_SA_COO~CA, laptop; cut 2026-10-13 ~22:5xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO`'s round-16 analysis `ledger/ROUND_ANALYSIS.round16.md` @6e9e2fc1ff, over PRD v0.7 (the ratified-text half reads
SIGNED by `3.0.0_SA_CVO~L`, current by ENDPOINT hash; the CTO's v0.7 addendum changes no ENDPOINT byte). Enrichment items 1 to 3 are the
cells below; item 4 (FWD-12) is cut the round after FWD-6 is exercised; item 5 is Andrew's two carried acts.

**Direction (binding):** muse replaces the Kimi text agent as Andrew's interface; the text path stays working as the fallback (FWD-9) and the
drafter (decision 2). No cell below changes the text path's behaviour. Whether Kimi stops drafting is HELD at Andrew (`87a2`).

**How the analysis's cells are split (the issuer's call, inside its own decomposition).**

- Item 1 (FWD-6's exercise) is two things: a BUILD so that every item in the folder carries its age (CA-i-1) and a human act (one question asked
  in muse). The act is Andrew's and is carded on the laptop list once CA-i-1 is merged; it is not a cell. muse's key goes on record now
  (`deliverables/2.0.0_SA_COO~CA/r17/MUSE_KEY_RECORD.md`, written by the issuer with this cut; closes W8-S7).
- Item 2 (FWD-7 receiver-verified) is CA-i-2, with W8-S6. W8-S8 (`object_id` on the draft rows) is cut into CA-i-1 instead, because
  `refresh.py` is that cell's file (cut by write set, `/dispatch` Step 1).
- Item 3 (the answers folder) is two cells and a host act: CA-i-3 builds the forwarder and the folder layout (a laptop worker); CA-i-5 installs
  it on dell2 (a crossbox order to `0.7.0_AE_CloudOps~CA2`); CA-i-4 deploys the receiver (Terraform only).

**The one contract the three build cells share (fixed here so they run in parallel; each cell's check pins its half).**

- The ANSWER FILE muse writes is one JSON object `{"payload": "<json text>", "signature": "<armored SSHSIG>"}`. `payload` is the exact text that
  was signed: `{"tag","action" (send|drop|edit),"notes","version","signed_at"}`. Signature namespace `muse-answer@opal`; key `ssh-ed25519`.
- The ASSISTANT EVENT is kind `muse.reply` (a distinct kind, so the text path's `sms.reply` is untouched), payload `{"answer": {"payload", "signature"}}`,
  object id = the draft's `object_id`, event id `muse-` + sha256 hex of the answer file's bytes.
- The RECEIVER (`tenant.py`) verifies the signature against the key pinned in `MUSE_ANSWER_PUBKEY` and refuses everything else.
  The FORWARDER does not verify signatures; it checks the shape and the tag only, and forwards.
- `drafts.json` rows carry `object_id`. The `answers/` folder (with `done/` and `rejected/`) sits beside the four source files; the refresh never touches it.

**Measured at the base (laptop, ~22:4xZ):** `check_i1_ages` base FAIL, `check_i1_live` base FAIL (`items=23 aged=0`), `check_i2_receiver` base FAIL
(0 of 7; a scratch reference receiver using `ssh-keygen -Y verify` scored 7 of 7, so the check has a green arm), `check_i3_forward` and
`check_i3_cli` base FAIL (no `forwarder.py`; a scratch reference scored 6 of 6 and 1 call, then was deleted). `check_i2_regression` (19 passed) and
`check_h1_census` (files=6 hits=0) PASS at the base as controls.

**Rule 24.** Domain: the analysis's enrichment items 1 to 3. Uncovered member by subtraction from the printed denominator (3 items): item 1 is
CA-i-1 plus the carded act; item 2 is CA-i-2; item 3 is CA-i-3, CA-i-5. None uncovered. Item 4 and the deploy (CA-i-4) are named, not cut.

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-i-1` | `refresh.py`: every item carries `age_minutes` and `age_from`; draft rows carry `object_id` (W8-S8); README names `answers/` and says the refresh never touches it | FWD-6, FWD-10 | LOCAL | chain 0, slot ~9 | none |
| `CA-i-2` | `tenant.py`: kind `muse.reply`, the receiver verifies the SSHSIG against the pinned key, refuses and records every other answer, the stale check covers edit (W8-S6); tests | FWD-7 | LOCAL | chain 1, slot ~10 | none |
| `CA-i-3` | `forwarder.py`: reads `answers/*.json`, forwards each once to the mailbox as `muse.reply`, rejects a malformed or unknown-tag file locally, idempotent by sha256 | FWD-7, FWD-8 | LOCAL | chain 2, slot ~11 | none |
| `CA-i-4` | DEPLOY of the receiver: Terraform pins `MUSE_ANSWER_PUBKEY`, applies the handler; never-widen pair, ledger entry | FWD-7 | WORLD | a CloudOps seat | CA-i-2 merged; a seat; the pair |
| `CA-i-5` | HOST ACT on dell2: install the forwarder and the `answers/` folder, a task, the mailbox URL from the Terraform output | FWD-7, FWD-8 | SERVED | `0.7.0_AE_CloudOps~CA2` (crossbox order) | CA-i-3 merged; CA-i-4's mailbox read |

`fanout: 3 of 3 chains, cap 8, reason: CA-i-1, CA-i-2 and CA-i-3 write disjoint files (refresh.py; tenant.py and its tests; forwarder.py) and share only the contract above, so each is its own worker.`

**Coverage note for the gate.** CA-i-4 and CA-i-5 have unmet dependencies, so under obligation 2 they are not cut at this issuance; they are listed
with their dependency so the round does not close without them, and the tick that reads their dependency met cuts them. FWD-12 is the next round.

**The issuer's real runs at close:** the live refresh with ages (CA-i-1's AC2, re-run by the issuer) and the folder read over SSH from the laptop. A live
signed answer needs muse's private key, which only Andrew's muse holds, so it is a carded act of his, not a run of the issuer's; the issuer's
evidence for FWD-7 is the receiver check's seven arms (real `ssh-keygen -Y sign` keys), the forwarder checks, and the deploy's read-back.
