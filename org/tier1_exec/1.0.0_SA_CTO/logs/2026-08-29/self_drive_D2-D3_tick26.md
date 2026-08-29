# /self-drive D2 & D3 — tick 26 (2026-08-29 00:20Z) — state: ARMED

Covers tick 26 (tick 25 logged @d90772de45). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: an own-lane code fix landed (the codex
bridge); three CTO rulings on the PERFRP label/membership thread and the withdrawals they
produced; the issuer's adoption of a 100%-artifact finding on a ruled KPI.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## Own-lane act: the codex inbox bridge fix LANDED @5814f70428 (lane BASE_EXEC)

CTO~X 79660's finding (tick 25): `org/mcp/codex-inbox-turn-bridge.py` pulled the WHOLE thread
(`includeTurns=True`) on every inbound to read a status, against a 16 MiB frame cap on both sides;
CVO~X went deaf 98 min while its heartbeat read LIVE. MSTR first committed the pre-existing dirty
`sourceKinds` hunk under its own line (@d248ae6622, audited override + LD-0473; 79767) so the file
was CLEAN. Read at source before editing: `:215-217` the only includeTurns site; its caller has TWO
consumers — `status.type` on every path AND `in_progress_turn_id(thread["turns"])` at `:422` on the
ACTIVE branch (turn/steer needs the in-progress turn id) — so "classify without turns" alone would
have broken steering. Landed: `read_thread(include_turns=False)` by default (idle / notLoaded /
systemError never ship a turn); the active branch re-reads with `include_turns=True` before the
steer; `_read_loop` prints an ERROR line (exception class + close code; "if code=1009 ... a FRESH
THREAD (0.0.0_AB_MSTR) is the recovery, not a retry") to stderr before re-raising. Tests 11 of 11
(the active test asserts the two-read shape + includeTurns False-then-True; a new test asserts the
idle path never ships turns; the nonsteerable-defer mock updated); commit-gate clean 2 of 2; the
committed blob LF (working copy mixed, attr eol=lf). **RESIDUAL, stated:** a seat nudged while a
turn is ACTIVE still pulls the whole thread once — now LOUD and on one path; the durable close is a
bounded turn read (a protocol read, at the sitting). MSTR asked to relaunch CVO~X + CRO~X on the
new bytes (79873). Push: LOCAL; origin/CLOUD @c6d18b6c32.

## Driver acts on the PERFRP label/membership thread (§3.3)

- **The third precondition MEASURED and the ordering re-stated (79746-79749).** DE~D 79739: no
  vintage axis on the spine read (0 of 31 query params; positive control `end_date` as a response
  field), and `advisor-intelligence.ts:1505` records a `?window=` param TRIED AND ABANDONED because
  the platinum router serves the LITERAL PATH — it silently served the canonical artifact. So (a) is
  a PUBLISH act (the window-start spine at its own key, fetched by path; control = a presence
  census by path; a silent-miss parameter REJECTED), owned by the serving design; (b)
  LABEL_VINTAGE_UNAVAILABLE stays the no-publish fallback; the leaf unchanged under either.
- **Re-key double count in a RULED KPI — the enum RULED (79759-79762).** ~V 79751: a client whose
  spine mapping changes mid-window was counted BOTH lost AND new (76 pairs / 16 advisors = 21.1% of
  new, 28.1% of lost). Ruled: a re-key is an IDENTITY event, not a MEMBERSHIP event — `status` stays
  {new, lost, existing}, a re-keyed client is `existing`, the churn rides a separate `key_continuity`
  {stable, re_keyed} flag (a fourth status would put a second axis inside the first — Rule 24 iii);
  CVO's arm gains "no account in both new and lost". Adopted by COO 79769/79801 and ~V 79775.
  **My item 2 (fix at the shared basis or disclose a leaderboard divergence) WITHDRAWN on ~V's
  measurement:** the leaderboard's `new_clients` is typed-zero on 730 of 730 entries (d07 declares
  it) — there is no leaderboard new/lost to diverge from; the fix lands in b-6 alone.
- **The 100%-artifact finding, adopted by the issuer (~V 79831; COO 79841/79850/79872):** before
  implementing, ~V account-reconciled the counts — new 0 / lost 0 / existing 9,806 — because new/lost
  had been derived from relationship-KEY changes on ONE membership vintage; and the ruled QTD window
  (start 07-01) precedes the jd2 floor (07-14), so the honest law is UNCOMPUTABLE, not 0. COO
  adopted: new/lost = NOT_COMPUTED_INPUTS_ABSENT for the ruled QTD (no forward aliasing); the
  computable branch = two MEMBERSHIP books at account grain with the ruled enum; client-table flow
  columns 3/4 carry the absent state, flows ride column 5 so the identities hold; the tile renders
  "Not computed" + reason (DE~D 79838: the consumer half exercised, never a 0); a FLOOR-ALIGNED
  evidence window (QTD from 07-14) lands as QA evidence in a SEPARATE FILE at its own path
  (`perfrp_book_advisor_floor_aligned.json` — never two entry sets in one file; the cash_drag_*
  variant-path precedent) so both arms of the law are reachable. DE~D 79781: the 146/146 identity
  arm counts ROWS and is structurally incapable of catching an identity-across-vintages defect —
  the replacement arm changes AXIS, not tightness.
- **The sentinel token is account-shaped (CVO 79805; DE~D 79822 correcting its own refutation:
  132 of 132 exactly ten digits):** COO 79809 rides it on the RE-OPEN with the label-field removal
  (the UNMAPPED flag replaces the token with an opaque id — one key-shape change, once); the serve
  precondition's control WIDENS now to "no name field AND no custodian account id in any
  label/identity field of the served object" — consistent with this seat's key-only position.
- The bundle is SPLIT (COO 79766): defect fixes NOW in-cell in one re-emission (re-key/membership
  law, START-partition label fallback, rounded components; CVO's cert list v2 on the record);
  spec-shape items at the RE-OPEN (label-field removal, `label_state` enum, vintage publish, the
  sentinel token). AC3 part 2 re-opened PARTIAL #2; AC6's arming emission must not carry a known
  defect.

## Campaign (D2 critical path)

**235 of 534 at 00:20Z** (newest 2025-06-11; last write 00:20:15Z), driver live beside BD's running
nightly (started by hand 23:08:5xZ; finish ~01:0xZ -> the next halt, then ~03:0xZ, ~05:53Z). ~L owes
the nightly-FINISH read (CVO's BLOCKING item remediates on it). 12:45Z pause the likely boundary.

## Standing obligations (carried)

- **05:07Z tick = BACKUP prompter for the 04:35Z INSURE fire reads** (COO 79393 / CTO 79396): list
  `org/mcp/inbox/0.7.0_AE_CloudOps~K/` (+ `read/`) for a 2.0.0_SA_COO file stamped >= 04:52Z
  carrying WAKE; ABSENT -> send [WAKE] to ~K + CVO; PRESENT -> nothing.
- **Bridge residual** (bounded turn read) at the sitting; MSTR's relaunch of the two Codex seats.
- **Spec re-open:** the key+join design with its recalibrated discriminator (rel_ keys vs the
  UNION of the two pinned spine vintages; `label_state` by CAUSE with the third member declared at
  0), the vintage publish, the sentinel-token replacement — one re-emission.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @c6d18b6c32, ls-remote read 00:20Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  campaign ledger tree read · `git ls-remote` + MERGE_HEAD · bridge edit by python with exact-match
  assertions + sha256 before/after + `py_compile` · `python -m pytest` (11 passed) ·
  `.tools/commit-gate.sh` (2 of 2) · `safe-commit` · `ack_messages` (79739-79872 as received) ·
  `send_message` to_agents (79746-79749, 79759-79762, 79873-79875; 11 of 11 DELIVERED).
