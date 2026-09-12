# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 32

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-12T21:4xZ**
(stamp MEASURED: `date -u` 21:41:04Z, and this log's own commit author time is the check.)
Tick 31's log is `@7fcdd1cf65`, amended `@042149180e`. **Short by intent: Andrew's 02:22Z priority
ruling landed this window and the remedy is subordinate to the work.**

---

## 1. THE PRODUCING PLANE CAME BACK, AND MY INSTRUMENT COULD NOT SEE IT

⛔ **I TOLD ANDREW "the producing plane has produced nothing in 37 minutes." IT WAS FALSE WHEN I SAID
IT.** `0.9.0_WK_AMGT_RESAPP~12` committed **`d771f204d8` at 21:33:22Z** -- 33 min after the rate-limit
reset, 8 min after `2.0.0_SA_COO~ZZZ` measured both branches at the issuance, and **4 min before my
claim**. Subject: *"rf-6 complete, 4 criteria re-verified, portal gitlink moved as directed"*; 4 files
-- proof instance, investigation rows, the order's status flip, and `portal`.

⛔ **THE CAUSE IS THE INSTRUMENT'S DOMAIN, NOT THE READING.** I ran
`git log --since=... --author="0.9.0_WK_"`. **Without `--all`, `git log` walks HEAD's ancestry ONLY --
and under spine v3 a worker's output lives on an UNMERGED branch by construction, until the drain.**
So the census was structurally incapable of seeing the population it was claiming about, and it
returned a clean, confident, controlled ZERO.
⚠ **AND MY CONTROLS PASSED.** Positive control 12, negative control 0 -- both TRUE, both irrelevant:
they proved the author filter works, never that the WALK reached the branches. **A control inside the
wrong domain certifies the instrument and tells you nothing about the coverage.**
⭐ The discriminator that caught it was cheap and I only ran it because two instruments disagreed:
`git for-each-ref refs/heads/` showed `wk-amgt_resapp-7-2` at `d771f204d8`, not at `c9b1fc5ed0`.
**FOURTH wrong-domain census against this seat tonight** (the L10 band filter, the "carriers I
authored" enumeration, the HEAD-only walk here, and the 20-hour-stale liveness quote).
**THE STANDING FIX: any worker-plane question uses `git log --all` or `for-each-ref`, never a bare
`git log`.**

⚠ `wk-amgt_resapp-7-1` (`~11`) is **still AT `c9b1fc5ed0`** -- no movement. One of two workers is
producing.

## 2. A DRAIN-TIME FLAG FOR `2.0.0_SA_COO~ZZZ`, RAISED NOT RESOLVED

`d771f204d8` moves the **`portal` gitlink** (1 path, measured). On an UNMERGED worker branch that is
inside bounds -- `3.0.0_SA_CVO~Z` released local edits and commits this window, and AMGT rd-8's own
precedent is *commit-yes, promote-no*. ⛔ **BUT MERGING THAT BRANCH MOVES THE GITLINK ON `SITEZ`**, and
portal is FROZEN both fabrics. The drain is the COO's act and this seat neither merges nor blocks it;
flagged so the decision is taken deliberately rather than discovered. Banked sibling: a superproject
merge carries a BARE OBJECT ID and never moves what it points at, so a clean merge is not evidence
the submodule resolves.

## 3. THE QUEUE DROPPED FROM FIVE TO THREE, AND TWO WERE STRUCK BY MEASUREMENT

| card | tick 31 | now | why |
|---|---|---|---|
| generator deploy | BLOCKING | **STRUCK from Andrew's queue** | CVO withdrew this seat's scope citation; NEVER#1's closers are CTO+COO |
| POSN round-3 carry-forward | BLOCKING | **NOT MINE** | `2.0.0_SA_COO~Z` re-asked it correctly `@ee14709b4e`: FOUR orders of 15, not two of seven |
| portal freeze | BLOCKING | **BLOCKING, NARROWED** | EDIT half released by the CVO; only "may a DEV PUSH happen" is his |
| LIMB 6 widening | CARRIED | CARRIED | CVO confirmed the citation |
| Bright Data proxy | CARRIED | CARRIED | CVO confirmed the citation |

⛔ **NO PITCH THIS TICK, AND THAT IS A DECISION.** All three survivors were reviewed by
`3.0.0_SA_CVO~Z` ~25 minutes ago and CONFIRMED RESERVED with their citations read. Re-pitching them
is repetition, not corroboration, and Andrew's priority ruling names exactly this kind of traffic.
The skill's zero-branch applies: no empty pitch.

## 4. WHAT PEERS DID, recorded because it changes this seat's state

- `2.0.0_SA_COO~Z` **REFUSED to cut round 4** `@ee14709b4e` and was right: the L10 refuser counts
  **per PROJECT**, so cutting now would deadlock round 3's slug until round 4 fully drained -- the
  AMGT round-6 inversion **this seat itself banked into Rule 27**. I routed authority correctly and
  timing not at all; that seat supplied the half I dropped and parked both inputs against the cut.
  It also measured `_posn_round2_terminal_exception` at `:827` requires `total == 8` while POSN is now
  **15**, so the round-2 carve-out **can never match again**.
- `4.0.0_SA_CRO~Z` took the priority ruling by ACTING: `Z-S18` disarmed `@7a7815eec0` (a perishable
  gate state that never blocked), `Z-S12` disarmed `@50018bedd0` -- the rename's own row, 522 hits
  over 57,312 files, all five `DEF` band hits FROZEN worker proof artifacts, **zero live code
  definitions**. Keeper: *a rename's census never returns to zero in an estate that preserves its own
  history.*
- `0.0.0_AB_MSTR~Z` measured its own flagged summary: `d0efe81ca8` is an **ANCESTOR of origin/SITEZ**,
  not a foreign remote's tip -- a 20h-stale cursor, same axis as this seat's 20h-early stamps,
  opposite sign.

## 5. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 3 RESERVED (all CVO-confirmed this cycle; no pitch, see s.3)
  BLOCKING  portal freeze -- may a DEV PUSH happen (EDIT half released)
  CARRIED   LIMB 6 widening · Bright Data proxy
  NOT-MINE  POSN round-3 L10 exception, re-asked by 2.0.0_SA_COO~Z via 0.0.0_AB_MSTR~Z
  NOT-MINE  the mechanical-change carve-out on the half-hash, carded by 0.0.0_AB_MSTR~Z
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 projects, 2 of 14 live directives)
  AMGT_RESAPP  active/EXECUTING  REACHABLE  round 7, 6 ACTIVE; ~12 PRODUCING (d771f204d8), ~11 static
  POSN_ASTTAX  active/EXECUTING  REACHABLE  round 3, 4 of 15 ACTIVE; round 4 correctly NOT cut
  UNREACHABLE: 0     HELD-AT-STOP: not reached
```
⚠ D4 `open_tos=6` vs measured 4 -- still UNDETERMINED (lag vs grain), unchanged from tick 31, still
not reported as a defect on an undetermined cause.

**Push state:** LOCAL at write time; `042149180e` and earlier are ON ORIGIN (`0.0.0_AB_MSTR~Z` pushed
and read `ls-remote` in the same breath).

## Compiler Tools

`git for-each-ref refs/heads/` and `git log --all` (**the worker-plane instruments; a bare `git log`
is HEAD-only and cannot see an unmerged branch**) · `git merge-base --is-ancestor` with a positive
control · `date -u` for the stamp, never carried forward · `directives-check.py --json` ·
`to-check.py --all` · author-filter positive AND negative controls (which passed and still did not
save me) · `safe-commit.sh -F`.
