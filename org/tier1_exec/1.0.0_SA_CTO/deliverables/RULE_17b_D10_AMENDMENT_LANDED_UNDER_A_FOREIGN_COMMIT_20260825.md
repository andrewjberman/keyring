# RULE 17b's D10 AMENDMENT IS LIVE UNDER A FOREIGN COMMIT -- the reasoning, recorded where it survives

**Seat:** `1.0.0_SA_CTO`. **When:** 2026-08-25 ~19:2xZ. **Filed against myself.**

## WHAT HAPPENED

| UTC | event |
|---|---|
| ~19:14Z | I edited `CLAUDE.md` Rule 17b with the D10 amendment. `safe-commit` returned **rc=128, `fatal: Unable to create .git/index.lock`** -- another seat held the lock. **I left the edit uncommitted in the shared working tree** and went to answer Andrew. |
| ~19:2xZ | `6df0f160c6`, author **`1.0.0_SA_CTO~X`**, subject *"NEVER#4 CLAIMED A GATE FOR THREE ACTS AND THE GATE COVERS ONE"*, committed `CLAUDE.md`. **It carried my amendment.** |

Verified: `git log -S "PER-PRODUCT OR PER-FIRM BUCKET" -- CLAUDE.md` -> `6df0f160c6`, author `~X`.
My own commit never landed; my message file never entered the record.

**`~X` did nothing wrong.** `safe-commit` stages the pathspec it is given; my dirt was inside it.
**I flagged this exact exposure to Andrew in the message immediately before it happened, and left the
edit sitting anyway.**

## NOT REVERTED -- DELIBERATELY

The content is correct and live, the branch is shared, and rewriting history to correct an author
line is worse than the defect. **CLAUDE.md's Git section already documents this exact class** from a
prior instance (*"CTO's probe landed it under the wrong author+subject… The rule is correct and
wanted; do NOT revert"*). Same file, same mechanism, same disposition.

## ⛔ WHAT IS ACTUALLY LOST: THE REASONING, NOT THE LAW

The rule text is intact. The commit message is not, and it carried the load-bearing framing. It is
reproduced here because `git log CLAUDE.md` now leads a reader to a commit about NEVER#4:

**1. THE AMENDMENT IS NARROW. Only gold's HOME and CODE-HOME move.** Unchanged and re-ratified:
bronze raw + silver parquet queryable stay in `opal-data-assets`; platinum is the serving tier under
`opal-data-portal-v2/platinum/`; serving is its own tier; **GOLD IS PARQUET** with JSON leaving the
gold tier; every platinum publisher reads parquet and is the estate's only JSON producer.
**A reader who sees "D10 amends 17b" without this will assume the whole medallion form is in play.
It is not -- most of D10 is this estate's existing law, unenforced.**

**2. THE SUPERSEDED CLAUSE**, named so nobody hunts for it: 17b's 2026-08-11 amendment set the
product-gold home at `opal-data-assets/portal/gold/{product}/{scope}/`. **That is the one clause D10
replaces.**

**3. THE MEASURED GAP** the migration guard now cites, censused across all 16 `opal-data-*` buckets
on 2026-08-25: **gold in SIX buckets · code in SEVEN · platinum in FIVE beyond `opal-data-portal-v2`.**

**4. WHICH SCOPES ARE PRODUCT- vs FIRM-SHAPED IS ANDREW'S PER-CASE CALL** -- reserved by him
explicitly (*"i will define which case"*). No seat infers it.

**5. ADDED FROM HIS WORDS:** silver->gold is pulled by **Lambda; EC2 only where genuinely heavy.**

**Spec of record: `docs/architecture/D10_GLOBAL_PIPELINE_STRUCTURE_PRD.md`** (@`afcac062ce`, A6
worked example @`53b86ebe67`) -- committed under my own author line, and the surviving home for all
of the above. The amended rule points at it by path.

## THE CLASS, STATED WITHOUT THE INCIDENT

**AN UNCOMMITTED EDIT IN A SHARED WORKING TREE IS NOT "PENDING" -- IT IS ADRIFT.** Any seat that
commits that path next adopts it, silently, under their author line and their subject. The window
is not a moment; it lasts until someone else touches the file, and on a 15-agent tree touching a
hot file that is minutes.

**The remedy is not "commit faster."** It is: **when a commit fails on a lock, the edit is not
finished work waiting -- it is exposure, and it either lands on the next attempt or gets stashed out
of the shared path.** A lock failure reads as a delay and behaves as a handoff.

⚠ **AND IT COMPOUNDS WITH `1.0.0_SA_CTO~X`'s SAME-HOUR NEVER#4 FINDING**, which measured that bare
`git commit` is an **imperative enforced by nobody** -- `never-rules-gate.sh` covers `terraform
apply` and not the commit path. **Their finding is that nothing stops the act; this record is what
the act costs.** Two sides of one hazard, found independently within the hour.
