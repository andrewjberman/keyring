# NFRA_CTLPLN FWD-26 -- the voice examples object, FIRST CUT: what was read, what was stored, the read-back (2.0.0_SA_COO~R, 2026-10-08 ~07:4xZ)

Authority: `1.0.0_SA_CTO` rulings msgs 106829 (this seat runs the read) and 106834 (upload, labelled a first cut). No message
text is in this file, in git, or in any message of this seat. FWD-26 is NOT served by this object.

## The read

- Source: the Teams agent's own archive of chat messages (bucket `opal-data-transcripts`, the bronze chat-messages prefix),
  read-only, by a script that prints counts only. 1779 keys listed; 143 read newest first; 78 written by Andrew (the
  message's sender id equals the id in the agent's `me.json`); 60 inside the length bounds (40 to 1500 characters), across 8
  chats. Recorded to `C:/opal-voice/recorded/teams_reply/` (60 files), outside every git tree.
- Harvest: `python data/transcripts/scripts/teams_chat/voice.py harvest --kind teams_reply --from C:/opal-voice/recorded/teams_reply
  --out C:/opal-voice/andrew_voice_examples.json --max 12` -> `VOICE-HARVEST kind=teams_reply read=60 by_andrew=60 kept=12 written=True`.
- Per kind: `teams_reply` 12 (1898 characters of text; sent 2026-10-07 to 2026-10-08). `mail_reply`, `teams_post`,
  `job_completion`, `end_of_day`: 0.
- Carrying a firm's name: 0 of 12, against 8 firm-name terms read from the registry. That test cannot see a person's name;
  names are not wiped (his word, per PRD clause 10).

## The object

- Key: `s3://opal-data-transcripts/teams/transcripts/state/chat_assist/global/andrew_voice_examples.json` (the output of
  `assist.BUCKET` and `assist.state_key`; not typed). It did not exist before.
- It carries a `cut` field: label "first cut"; "12 Teams replies, the newest ... not chosen as representative";
  `serves_FWD_26` false; the ruling's message id.
- Put at ~07:4xZ with the same KMS key the sibling state object `me.json` uses. VersionId
  `LzwFFAOP45YGTKpBLc3N0b4sF5Mlcvw7`. 3386 bytes. SHA-256
  `dacf712d59b0b0522a4f0e8aca90bbb5b4b837624f777bbfba41235e828282a5`. (The pre-label file the ruling quoted was 3098 bytes,
  sha256 b8a9ec35...; the label added 288 bytes.)
- Read back: 3386 bytes, the same SHA-256, byte-equal, the same VersionId, `aws:kms`.
- The loader on this box, with the examples switch set: `voice.examples("teams_reply")` returns 12; the prompt block is 4023
  characters (bound 6000).

## What this is not

- The deployed function does not read it yet: the package with `voice.py` is not deployed (order NFRA_CTLPLN.TO-APPLY-11).
- Not representative: two days, the newest twelve. The representative set (across kinds of act, across more than two days,
  with mail once the gateway serves it) is the next cell, and FWD-26's exercise waits for it (ruling 106834).
- Rollback: delete the one object version; the drafters then read no examples and write as before.
