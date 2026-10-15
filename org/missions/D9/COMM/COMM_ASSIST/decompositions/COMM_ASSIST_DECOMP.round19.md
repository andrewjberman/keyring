# COMM_ASSIST decomposition -- round 19: the pending-drafts list, the mode-default gate, one batch repair (issuer 2.0.0_SA_COO~CA, laptop; cut 2026-10-14 ~22:5xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO`'s round-18 analysis `ledger/ROUND_ANALYSIS.round18.md` @5e4395ae5c (msg 109267) with its ADDENDUM 1 @16e5520ca8, over PRD v0.10 (ratified-text half SIGNED by `3.0.0_SA_CVO~L`, current; the brief half admitted). The CVO's L10 slug `REMEDIATION_v5.md` @e4b0f0d878 closed round 18: 14 of 14 orders complete, W10-S2 disarmed, W21-S1 graduated and then closed by design on Andrew's 2026-10-09 word (the CTO's addendum; not a cell).
The standing direction: the laptop drives COMM_ASSIST at normal pace (Andrew ~18:4xZ, CTO msg 109206).

**The analysis's four enrichment items and what the issuer does with each.**

1. The pending-drafts list (ruling 2) -> cell `CA-k-1`, then its deploy `CA-k-4` (named below, cut at the merge).
2. The mode-default gate (ruling 3) -> cell `CA-k-2`.
3. One batch repair cell: CA-j-18's stale mail test arms plus the INERT rows the issuer carries -> cell `CA-k-3`. The INERT rows taken are W19-S5 (a bare sibling import in `test_teams_chat_natural.py`) and W25-S3 (the reader's help text and scan log line); the others ruled INERT in `r18/ISSUER_RULINGS.md` stay INERT (W19-S1, S3, S4, S6, W20-S1, W23-S1, S2, W24-S3, W25-S2, W26-S1).
4. FWD-13's exercise: cut the moment muse reports its three pieces built -> cell `CA-k-5`, NAMED and not cut. No cell waits idle on it; the issuer keeps its Gmail thread with muse (the 5-minute read inside the 30-minute bound).

`W21-S1` is not a cell (closed by design, CTO addendum).

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-k-1` | the mail object keeps a LIST of open drafts keyed by seq (`state["pending_list"]`); a newer considered mail ADDS and never overwrites; `pending` stays the newest; replies, signed answers and the open-items list resolve the entry by tag; the reader emits one drafts row per open draft; tests | FWD-4 (the draft loop), FWD-13 (an alert for each mail) | LOCAL | chain 0, slot ~27 | none |
| `CA-k-2` | `.tools/ldo001-mode-default-check.py` and the one hook block in `.tools/safe-apply.sh`: a plan or apply covering `module.ldo_001` is REFUSED when the trunk's `chat_assist_ingress_mark_mode` default differs from the live `INGRESS_MARK_MODE` | FWD-7 (guards the mark's mode) | LOCAL (a read-only live read; no apply) | chain 1, slot ~28 | none |
| `CA-k-3` | ONE batch repair: the stale arms of `test_inbound_mail.py` and `test_inbound_mail_draft.py`, `test_teams_chat_natural.py` alone from the repo root, the reader's help text and scan log line; NO product change | none of its own (hygiene, CTO ruling 4) | LOCAL | chain 0 after CA-k-1, slot ~29 | CA-k-1 merged (it edits the same two mail tests and `refresh.py`) |
| `CA-k-4` | DEPLOY of CA-k-1 (a targeted apply of `module.ldo_001`, code only), its own never-widen set (COO, CTO, CVO halves on one pin) | FWD-4, FWD-13 | WORLD | the CloudOps seat | CA-k-1 merged; halves; amendment at the merge |
| `CA-k-5` | FWD-13's exercise: one real Teams item and one real C-MAIL mail each reach Andrew as a muse alert within 30 minutes of receipt, one not-for-him item none (restates CA-j-16) | FWD-13 | SERVED | needs muse's three pieces and Andrew's two acts (calls 44eb, e435) | muse built; Andrew's acts |

`fanout: 2 of 2 chains, cap 8, reason: chain 0 is CA-k-1 then CA-k-3 (both edit the two mail test scripts and refresh.py, so CA-k-3 waits on CA-k-1's merge); chain 1 is CA-k-2 alone (it writes .tools/ldo001-mode-default-check.py and .tools/safe-apply.sh and touches nothing chain 0 touches). CA-k-4 waits on CA-k-1's merge and on its halves; CA-k-5 waits on muse and on Andrew.`

**Why CA-k-1 is wider than the analysis's one line.** The mail object is the ONE object that receives every considered mail, and four places read its single `pending`: the mail reply path (`tenant.on_sms_reply` -> `mail_requests.on_mail_reply`), the signed-answer path (`tenant.on_muse_reply` checks an answer's seq against `pending`, so an answer for an older mail would be refused), the natural-language "what is waiting" list (`tenant.open_items`), and the dell2 reader (`refresh.py` drafts rows, whose identity for a mail is the object plus the seq). A list that only the writer knows about would keep older drafts the owner can no longer answer. The issuer's check (`r19/checks/check_l1_pending.py`, 15 arms) pins all four, the tag-collision case (a new mail's tag never repeats the tag of an entry still open) and the redraft ordering (a redraft re-texts its entry, so it becomes the newest and an untagged `1` still answers the text he just read).

**Rule 24.** Domain: the analysis's enrichment items 1 to 4 (denominator 4). Item 1 is CA-k-1 (and CA-k-4); item 2 is CA-k-2; item 3 is CA-k-3; item 4 is CA-k-5 (named). None uncovered.

**Issuer checks (written first, base FAIL, green on a scratch reference, then the scratch removed):**
`CA-k-1` -> `r19/checks/check_l1_pending.py`: base `L1-PENDING ok=False arms=1 of 15`, reference 15 of 15; negative controls (overwrite instead of append: 3 of 15; act on the newest whatever the tag: 8 of 15).
`CA-k-2` -> `r19/checks/check_l2_gate.py`: base `L2-GATE ok=False arms=2 of 13`, reference 13 of 13; negative controls (the hook runs the check on every apply: 11 of 13; an unreadable live value read as OK: 10 of 13; a no-verdict taken as OK: 12 of 13). The reference script also read the LIVE value read-only: `LDO001-MODE verdict=OK default=enforce live=enforce`.
`CA-k-3` -> `r19/checks/check_l3_batch.py`: base `L3-BATCH ok=False arms=2 of 8` (six arms FAIL; `refresh_same` and `no_product_change` pass trivially in the trunk checkout and bite in a worker's worktree), reference 8 of 8; negative control (repairing a mail test by editing `mail_requests.py`) fails `no_product_change`.
Each check finds the repository from the current directory's git toplevel, never from its own file location (the round-18 H1 defect), and is run by relative path from the worktree under test.

**The issuer's real runs at close:** `check_l2_gate` and the real script read against the live Lambda (a match prints `verdict=OK`; a forced mismatch through the JSON seam REFUSES); after CA-k-4, a served-code probe on a `probe:` object (as `check_k3_live` did for the records): two stand-in mails considered inside one minute both keep their drafts in the served code, read by object and seq and never by content, with no text sent. The dell2 reader's own pick-up of the per-draft rows rides the box pass (a read-only seat order like CA-j-15, cut at the CA-k-4 amendment). The batch repair needs no real run (tests only).

## AMENDMENT 1 (2.0.0_SA_COO~CA, 2026-10-15 ~01:1xZ): CA-k-1 merged, CA-k-3 released; the workers' API limit

CA-k-1 merged @2d0a8f5027 (worker ~27; the issuer re-ran the criteria on the merged trunk: `L1-PENDING ok=True arms=15 of 15`, `I2-REGRESSION passed=64`, `K2-READER arms=7 of 7`). The first sessions of workers ~27 and ~28 both ended at ~23:10Z on an API monthly spend limit (HTTP 429), ~27 after committing its code and ~28 before committing; close-out sessions continued each lane (~27 finished and merged; ~28 still running at this write). Row `COMM_ASSIST-W27-S1` (the `client_no_request` arm of `test_inbound_mail_draft.py` already failed at the base, 11 of 12) is INERT and the ISSUER's own order-text defect (the order said only `test_inbound_mail.py` fails at the base); cell CA-k-3 repairs the arm, and its check already pins it.
CA-k-3 is released: `<status>` staged -> pending, worker ~29, worktree cut from the trunk after the CA-k-1 merge. At the trunk the check reads `L3-BATCH ok=False arms=2 of 8`: `mail_draft_arms` now reads 16 of 17 (only `client_no_request`), `mail_cases` 11 of 15, the natural, help and scan-log arms still fail. The issuer amends its own orders without a CTO ruling; the gate limb that grades this paragraph: none (a decomposition note and a status flip).
