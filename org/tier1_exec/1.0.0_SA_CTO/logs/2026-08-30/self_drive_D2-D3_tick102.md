# /self-drive D2 & D3 — tick 102 (2026-08-30 18:0xZ) — state: ARMED

Covers ticks 101–102 and the acts since the tick-100 log (`1b730c8df6`) and its correction note
(`e5d0984b57`). Origin @`885e08055f` at the 17:35Z CLOSE (own `ls-remote` read 17:38Z); three of this
seat's commits LOCAL, riding the next window. Cron `1c261f82` :07/:37.
**Written on the condition tick 101 stated aloud — "held to tick 106 or 1b's landing". 1b landed.**

## Scope (register-read, §0)

`D2 & D3` → 2 of 12 live → **10 projects (10 members + 0 claims)**. Composition now printed every tick,
adopted from `3.0.0_SA_CVO` 88781 at 88787 — `10` and `9 members + 1 claim` were indistinguishable in a
single figure, and that indistinguishability is what let a real register defect read as my own error.
Open TOs 26. Ledger 19 / 0. Acked READ: 88745, 88746, 88753, 88761, 88778, 88781, 88790, 88794, 88807,
88811, 88825, 88829, 88838.

## Calls (§1)

**0 ADJUDICABLE · 1 RESERVED** — card (2), citation quoted: *"NEVER call an external vendor API without
Andrew's explicit per-use word."* His approval covered "W1 probe then W2 pull"; W1 is not executable, so
whether the word reaches W2 alone is a scope question only he closes. The all-reserved tell fired on a
queue of one; the citation test was re-run before printing.

## ANDREW'S CARDS — TWO CLOSED THIS STRETCH (§3)

**CARD (1) ANSWERED: HIS ANTECEDENT IS FALSE.** His condition was *"if you are able to match the subject
accounts to the Schwab 0833 book definitively, then I will need to have a discussion with leadership."*
Measured (`0.4.0_DS_ClientPlatform~N` 1a 88778 + 1b 88825; GRADED PASS and **independently reproduced on
the grader's own reads**, `3.0.0_SA_CVO` 88844):
- **0 of 13 nine-digit keys in the 0833 book; 0 of 13 in 0824.** Each read on that book's own
  authoritative record with its own custodian field (`custdian_id` SCHWAB 7,371/7,371,
  `mstracct_number` 0008335338, `master_account_name` 49 FINANCIAL).
- **POSITIVE CONTROL FIRES THROUGH THE SAME PADDING PATH THE KEYS TAKE** — 5,787 of 5,791 eight-digit map
  keys found; NEGATIVE control (fabricated 999999999) rejects; **residual 4 printed by exact account
  number**, not swept. The grader reproduced all of it including the residual four.
- **A FALSE NEGATIVE CAUGHT BEFORE REPORT:** raw nine-digit keys against a `zfill(10)` `account_id`
  returns 0 of 13 **BY FORM**, indistinguishable from absence. **And the grader walked into the sibling
  ten minutes after reading the warning** — its first run printed `POSITIVE CONTROL: 0 of 0`, a control
  that had selected nothing. Its own control caught it. Two false starts stand between this zero and a
  zero that would have read identically.
- **CANNOT BE MET, stated as such:** naming the custodian these 13 DO belong to is unanswerable
  in-estate — the only carrier is dead (46 of 47 partitions 0 rows; the one populated partition is
  2026-07-14, 91 rows, all eight-digit). *"Not Schwab" is MEASURED. "Is Fidelity/FMTC" is NOT.*
- Business fact the prior did not carry: the masters are **different legal entities** on the custodian's
  own field — 0824 = "49 WEALTH MANAGEMENT LLC", 0833 = "49 FINANCIAL".

**CARD (6) EXECUTED** (`0.4.0_DS_ClientPlatform~V` 88829): 8 objects across BOTH buckets, 17:48:34–54Z,
by EXACT KEY, rc=0 on all 8. **His gate honoured as written** — the consumer census re-run IN THE STRETCH
(17:43:15–17:45:30Z), not cited from the four-hour-old one; 4 planes, controls firing, 1 call-shaped line
opened and resolved to a string literal in a self-test fixture. NEVER#2 ledger opened 17:42:10Z BEFORE
the act, closed after. RECOVERABLE: 8 delete markers, 33 versions retained, **VersionIds printed WHOLE**
after this fabric spent an hour on a `[:22]` slice.

## Corrections this stretch (two, both this seat's, both on committed records)

1. **THE REGISTER FINDING WAS BACKWARDS — `e5d0984b57`.** My `1 of 9` read was TRUE (a peer's close had
   removed the member 20 minutes earlier); I diagnosed my own correct reading as an instrument artifact
   and wrote "no register change occurred", **absorbing a live defect into a self-blame**. Then claimed
   "never a member" from `org/DIRECTIVES.yaml` — **a path that does not exist** (the register is
   `org/missions/DIRECTIVES.yaml`); grep and `git log` both returned empty against the same wrong path,
   which is repetition, not corroboration, and out-of-corpus read as absence. The membership I denied was
   added on this seat's own request six days earlier. §0.3 exception ask WITHDRAWN entirely.
2. **THE RECORD ANDREW READ CARRIED A FALSE SPATIAL PREMISE — `<this commit>`.** *"the 49F SmartX feed
   this fabric reads lands under `schwab/08335338/`"* is false: `smartx/` is its own top-level prefix
   (476,788 objects) and no SmartX feed is under either Schwab master. **Origin traced at the pin with a
   negative control** rather than claimed — `git show 1b730c8df6:<file>` matches `08335338` at lines
   25/30 and `smartx/platform` zero times. `3.0.0_SA_CVO` repeated it at 88640 and withdrew at 88811;
   the repetition is not the origin. Neither correction was amended away.

⛔ **THE PATTERN ACROSS BOTH, and it ran in OPPOSITE directions within one hour:** at 88690 I took blame
that was not mine (the truncated VersionId, origin another seat's `[:22]`); at 88774 I took blame that was
not mine AND the taking buried a live defect. **Reflexive self-blame is the cheapest available
explanation, it terminates inquiry, and nobody audits it** — the same mechanism that makes a false
self-attribution survive. Ordering rule adopted: when my own instrument disagrees with my prior number,
**test the WORLD first and myself second.**

## Fabric-wide, not mine

The foreign-row ACK class reached **7 self-reported instances** today across 5 seats, with at least two
distinct mechanisms (an id lifted from a notification SUBJECT; a read command that EXCLUDED the Msg-ID
line). The recipient guard refused every one, verified at the store rather than from the return. **The
guard's refusal log is the denominator for the POST-guard period only** — a pre-guard foreign ack would
be silent, and no one has censused that.

## Completion test (§4)

**NOT DONE — 2 of 10 (10 members + 0 claims).** REACHABLE 10 / UNREACHABLE 0. Cards (1) and (6) closed
CELLS, not projects; no member's `status` moved this stretch.

## Compiler Tools

`directives-check.py --json` + §0.3 claim scan (342 JSONs, both `prds[]` shapes); `git show <pin>:<file>`
with a negative control for the origin trace; `ls -la` on both register paths (the existence check that
should have preceded the absence claim); `grep -c` positive control on the real register; `git log --all`
on `org/missions/DIRECTIVES.yaml`; `safe-commit` ×3; Msg-IDs read per inbox file, never inferred.

state: ARMED · next log at a verdict or tick 108 (floor)
