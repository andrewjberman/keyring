# /self-drive D2 & D3 — tick 25 (2026-08-28 23:49Z) — state: ARMED

Covers tick 25 (tick 24 logged @ccdfed449b, ON origin @baae9a766a). Cron bde882a4 (:07/:37; ran on
idle). Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: three driver acts on
the PERFRP PII item (a design position, its amendment, and a recalibration of the pre-registered
test before first use) and an own-lane remedy taken on a fabric-infra finding.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## Driver acts (§3.3)

- **PII on the b-6 client table — the serve precondition CONCURRED and a design POSITION recorded
  (79565-79568).** DE~D 79550: the client table's first column (the display label this seat named
  in 79446) is REAL client names — 3,362 distinct over the leaf — correct at the producer, new PII on
  a served-shaped surface; DE~D pseudonymised the committed portal fixture by INDEX (not hash: a
  stable hash is a re-identification handle), 0 of 3,362 with a positive control. COO 79556 RULED it
  a PRECONDITION of any serve/flip at arm-(a) (owner the serving design / publisher lane / 0.7.0,
  CTO as PRD author; on ADVI_PERFRP.json `blocking` so Andrew's arm-(a) card carries it) and left
  the design fork to this seat. POSITION for the spec re-open: **the leaf carries the KEY, the
  portal resolves the label from the spine it already holds scoped** through the existing
  summary.json path — not "scope at serve" (that is a second pseudonymising Lambda path beside the
  one summary.json has = a shadow serve channel; the label is already served scoped on
  d04/d05/d10/d12/d13; a leaf with no name field cannot leak one through any future path). My 79446
  conflated what the user SEES with what the leaf CARRIES; corrected at the design grain. ~V 79575
  concurred and added a second surface it clears: the git-tracked emission carries 3,216 real
  names (not novel — two census CSVs under `docs/briefs/derisk2_census/` carry the same). COO 79592
  BUNDLED the label-field removal with ~V's rounding change into ONE re-emission at the re-open.
- **The position AMENDED on DE~D's catch (79578-79581).** DE~D 79572 read the consumer half at
  source (`AdvisorBookView.tsx:711-718` builds {client_key, client_name}; `:779-781` resolves by
  key) — so "the portal has it" is measured — and found the load-bearing assumption: the leaf's
  `relationship_id` and the portal's `client_key` must be ONE key space, unverifiable under the cap
  (the fixture rebinds keys, so a working render is the fixture agreeing with itself), and a
  mismatch FAILS QUIETLY (every row renders UNLABELLED, a designed state). Amended: the design is
  CONDITIONAL on the key-space identity; discriminator pre-registered for the first served read;
  the fallback if the spaces differ is COO's serve-side scoping, not a client-side mapping.
- **The discriminator RECALIBRATED before first use (79646-79649).** DE~D 79637's cross-tab over
  all 10,076 rows: 132 sentinel-key (`UNMAPPED-RELATIONSHIP:<id>`, no relationship record — never
  in the spine by construction) x UNLABELLED; 270 rel_-key x UNLABELLED (a real key the producer
  found no label for); 9,674 rel_-key x real label; the fourth cell (sentinel x labelled) = 0 of
  10,076 BY CONSTRUCTION, measured by ~V (79650) — which makes the tab MECE. The test as written in
  79578 would have read a PERFECTLY HEALTHY join as 132 short. Now: match denominator = the
  rel_-shaped subset (9,944), sentinels reported beside; `label_state` in {LABELLED, NO_SPINE_LABEL
  (270), UNMAPPED (132)} as a PRODUCER field with its four-postulate record (only the producer can
  say which absence a rel_-keyed unlabelled row is — the consumer cannot tell producer-absence from
  join-failure); the served counts checked per state; the join-failure signature = a rel_ key the
  spine holds rendered unlabelled. Rides the same single re-emission. COO 79672 recorded both
  calibrations on the face; ~V 79633 confirmed the testability claim on the served leaderboard (it
  carries COUNTS, no key set — so a-5's acceptance as WORDED has no served counterpart; graded
  tonight as same-basis evidence: 146/146 by name, 140/146 exact counts across a 7-day gap; the set
  equality = AC11's read = the discriminator). DE~D recorded a hypothesis of its own as REFUTED (no
  custodian account number in the label field, 0 of 402) rather than dropping it.
- **Own-lane (not D2/D3): the codex inbox bridge remedy OWNED (79669-79671).** CTO~X 79660: `org/
  mcp/codex-inbox-turn-bridge.py:404` calls `read_thread(includeTurns=True)` on every inbound to
  read `status.type`, so the WHOLE thread crosses the app-server socket each time against a 16 MiB
  cap both sides (:71); CVO~X crossed at ~21.5h of thread age (first 1009 21:40Z), deaf 98 min while
  the heartbeat read LIVE; MSTR re-seated it 23:30Z; CRO~X on the same clock. Read at source: :215-
  217 is the ONLY includeTurns site and :404 its ONLY caller, using `status.type` alone — the fix is
  `includeTurns: False` (status is metadata) plus a LOUD log at the 1009 site in `_read_loop`. The
  file is DIRTY in the shared tree (+5/-1 `sourceKinds: ["cli","vscode"]` for `--remote` discovery
  + the test +22; author unknown; dirty since before this session; CRLF working copy vs LF index),
  and the re-seated seat RUNS those bytes — so MSTR (last committer @1ab6bea1e7, the fabric-infra
  owner) was asked to commit-or-name the hunk FIRST; the edit lands the moment the file is clean.
  Lane BASE_EXEC. Still dirty at 23:49Z; MSTR's word pending.

## Campaign (D2 critical path)

**217 of 534 at 23:49Z** (newest 2025-05-15; last write 23:49:07Z), driver live beside BD's running
nightly (started by hand 23:08:5xZ per tick 24's ruling (A); finish ~01:0xZ -> the next halt). Per-100
#2 at date 200 ACCEPTED at three seats on three instruments (~L 79570 at pin @c19c20039a; COO 79583;
CVO 79623): zero unexplained on both planes, the three form corrections all fire. ~L still owes the
nightly-FINISH read (CVO's BLOCKING item remediates on it). Predicted halts ~01:0xZ / ~03:0xZ /
~05:53Z; 12:45Z pause the likely operative boundary.

## PERFRP round 2 (issuer plane)

TO-R1-DE CERTIFIED 11 PASS / 2 UNCOMPUTABLE / 0 FAIL (CVO 79618): the frontend read of the rewrite
is closed at the certifier; AC11 (serving gate) and AC8 (producer enum) remain by design. TO-R2-DS:
every computable row certified at three seats; AC6 (534/534) and AC7 (round close) remain.

## Standing obligations (carried)

- **05:07Z 2026-08-29 tick = BACKUP prompter for the 04:35Z INSURE fire reads** (COO 79393 / CTO
  79396): list `org/mcp/inbox/0.7.0_AE_CloudOps~K/` (+ `read/`) for a 2.0.0_SA_COO file stamped
  >= 04:52Z carrying WAKE; ABSENT -> send [WAKE] to ~K + CVO; PRESENT -> nothing.
- **Codex bridge fix** on MSTR's word (above).
- **Spec re-open (COO's cut):** the key+join PII design with its recalibrated discriminator and the
  producer `label_state` flag, bundled with ~V's rounding change — one re-emission of b-4 + b-6.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope (the PII serve precondition rides his arm-(a) card as a precondition, not a call).

state: ARMED · push state of this log: LOCAL (origin/CLOUD @baae9a766a, ls-remote read 23:49Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  campaign ledger tree read (outcome-filtered) · `git ls-remote` + MERGE_HEAD · `git diff` +
  single-file grep on the bridge (includeTurns sites) · `ack_messages` (79550-79672 as received) ·
  `send_message` to_agents (79565-79568, 79578-79581, 79646-79649, 79669-79671; 15 of 15
  DELIVERED).
