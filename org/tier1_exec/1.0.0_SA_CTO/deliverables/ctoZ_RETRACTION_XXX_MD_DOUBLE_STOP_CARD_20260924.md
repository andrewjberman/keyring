# RETRACTION -- the `org/XXX.md` "stale double-stop" card is WITHDRAWN

**Seat:** `1.0.0_SA_CTO~Z`. **Measured:** 2026-09-24 22:2xZ, against `origin/CLOUD` @`5b3756fa16`.

## What I told Andrew, and what is true

I carried a card asking Andrew for an `ANDREW_LAW_EDIT_ORDER` to repair a **stale double-stop in
`org/XXX.md` at `:86-87`**. I had already flagged that item 4 of that clarification was overstated
because it was measured against a locally-reverted copy, and that it owed a re-measure against origin.
The re-measure is below. **The defect does not exist.**

| read | instrument | result |
|---|---|---|
| positive control -- does `<ref>:<path>` resolve? | `git show origin/CLOUD:org/XXX.md \| wc -l` | **245 lines** (resolves; the mangle-returns-clean-empty trap did not fire) |
| local vs origin | `git diff --stat origin/CLOUD -- org/XXX.md` | **empty -- byte-identical** |
| worktree state | `git status --porcelain org/XXX.md` | **empty -- clean** |
| `:80-95` (the cited region) | `sed -n '80,95p'` on origin's bytes | sections **A.2 audit-archive** and **A.3 PATH check**. No stop of any kind |
| every stop/halt marker in the file | `grep -n -i "stop\|do not proceed\|halt"` on origin's bytes | **6 hits, exactly ONE stop heading**: `:9 "## STOP -- READ THESE FIRST"`. The others are prose referring to `[STOP]`/`[HALT]` message grammar (`:32`, `:43`, `:80`, `:165`, `:170`) |
| the one stop block | `sed -n '9,14p'` | one heading plus ONE directive (`BANNED: Explore agent`). **Not a double-stop** |

## The mechanism of my error, which is the keepable half

`org/XXX.md` is LOCKED, so the only act the card could ask for was Andrew's law-edit order. **I asked
him to unlock a law file to repair a defect that was an artifact of a transient working-tree state that
has since been reverted.** The file I was reading and the file on origin were never different in the way
I reported; by the time I owed the re-measure, the copy that produced the reading no longer existed.

Two lessons, both already banked in other forms and both re-earned here:

1. **A DEFECT CLAIM ABOUT A SHARED FILE IS MEASURED ON THE SHARED PLANE, NOT THE WORKING TREE.** A
   working-tree read answers "what does this device hold right now", which for a file peers are merging
   is a different question from "what does the law say". The cheap control is one `git diff --stat
   origin/<branch> -- <path>`, and an empty stat retires the whole class.
2. **A CARD AT ANDREW IS AN ASSERTION AND CARRIES THE EVIDENCE BURDEN OF ONE.** This one asked him to
   lift a lock -- the most expensive act the card could request -- on a citation (`:86-87`) that pointed
   at unrelated lines. A line-number citation is verified by PRINTING THE BYTES AT THE CITED LINE, which
   is exactly what CLAUDE.md already says about quotations and which I did not do before carrying it.

Against CLAUDE.md's DO NOT MANUFACTURE FRICTION line, this card was friction I generated: it proposed a
law-file edit nobody needed.

## Effect

- **The card is WITHDRAWN.** No law-edit order is owed, and `org/XXX.md` needs no change.
- **Cards at Andrew go from TWO to ONE:** only ft/barrons remains, whose publisher refusals (a 403 from
  the search endpoint and a post-auth rejection) authorization cannot reach, and which is why
  `AMGT_HARVST` round 6 is PARTIAL-shaped -- `data_status COMPLETE` needs all five publishers.
- Any prior record of mine citing an `org/XXX.md` double-stop is superseded by this file.

Push state: this commit LOCAL on landing; origin/CLOUD @`5b3756fa16` (`ls-remote`, 22:2xZ). This lane
does not push.
