# /integrate directives — the cross-fabric REGISTER reconcile, per row

**Who runs it:** `0.0.0_AB_MSTR` (laptop) and `0.0.0_AB_MSTR~Z` (site Z), together. Both halves are
MSTR acts: the register is the register owner's surface, and only the two MSTRs push a shared branch.
A lane agent invoking this stops at Step 0 and routes to its MSTR.

**Authority (Andrew-direct 2026-09-01 ~13:3xZ, MSTR terminal, VERBATIM):** *"i think we need a new
function added, '/integrate directives'. The idea is that the fabric MSTR agents check where their
fabrics have taken the directives and update each other. I'd like it if directives.yaml could somehow
be synced on status between the fabrics."*

> **What it is for:** `/integrate` reconciles the whole tree and answers *"can each side read the
> other."* This answers a narrower and more perishable question: **has either fabric moved a
> DIRECTIVE, and does the other know.** The register is the one file where a stale copy causes a
> seat to write a sovereign act onto the wrong baseline.

---

## ⛔ THE PREMISE, MEASURED BEFORE THIS SKILL WAS WRITTEN: THERE IS NO STATUS FIELD

A directive row carries exactly `title / directive / placement / members / stance` (2 of 13 also
carry `completion_bar`). **It carries no status, and it should not.** A directive's status is
DERIVED from its member projects, which already hold `status` and `dep_stage`.

>> **So "synced on status" is served by EXCHANGING a derived digest, never by materialising a status
   field onto the register row.** A status written onto the row would be a SECOND CARRIER of a
   quantity that already has one, and the second carrier drifts silently — it is the exact failure
   this estate keeps paying for. **The digest is computed at read time and thrown away.** <<

⚠ **If Andrew ever wants a real status field on the row, that is a SCHEMA change and Rule 24 binds:**
four postulates plus a word-boundary token census, minted as a proposal, not added by this skill.

## ⭐ THE UNIT IS THE ROW, AND `placement` IS THE AUTHORITY

A whole-file diff on this register is always "differs" and tells you nothing about which side is
right — both fabrics legitimately edit it. **The row is the unit that has an owner, and `placement`
names that owner.** That single fact produces the whole resolution table:

```
  AGREE              byte-identical. Nothing to do.
  CONTENT-DIFFERS    placement agrees, content does not -> THE OWNING FABRIC'S COPY WINS.
                     Mechanical. No adjudication, no law owner, no message.
  PLACEMENT-DIFFERS  the sides disagree about WHO OWNS the row -> NEITHER MSTR MAY RESOLVE IT.
  ROW-MISSING        exists on one side only. A mint the peer has not merged. Merge forward,
                     NEVER delete.
  UNOWNED            placement names no fabric. A FINDING -- never defaulted to whichever
                     fabric happens to be running the compare.
```

## ⛔ PLACEMENT-DIFFERS HAS TWO SUB-CASES THAT LOOK IDENTICAL IN A DIFF

**Do not resolve either one by picking a side.**

- **(a) STALE** — one fabric has not merged the other's record of *the same* Andrew word. Compare the
  QUOTED WORDS, not the surrounding prose: if one side's text appears inside the other's preserved
  history, that side is simply behind. Merge forward; no question for anyone.
- **(b) CONVERGENT** — Andrew ruled at BOTH terminals separately, and neither seat knew.
  *Measured 2026-09-01: he ruled D8 to LAPTOP at the CTO terminal ~02:4xZ (**"D8 should be on this
  device"**) and again at the MSTR terminal ~03:0xZ (**"This is all correct but D8 on laptop"**) —
  20 minutes apart, neither seat aware of the other. Convergent, not conflicting.*
- **Only if the two quoted words genuinely CONTRADICT is this a question for Andrew**, and then it is
  carried verbatim with both texts, adjudicated in neither direction.

## Procedure

**Step 0 — identity + freshness.** Confirm an MSTR serial. `git fetch origin`. ⛔ **Run the compare
against `origin/*` refs, never two worktrees** — a worktree carries uncommitted edits and you would
be comparing one fabric's draft against the other's record.

**Step 1 — compare.**
```bash
python .tools/integrate-directives.py compare              # origin/CLOUD vs origin/SITEZ
python .tools/integrate-directives.py compare --json       # machine-readable
python .tools/integrate-directives.py --self-test          # 5 arms; must read PASS 5/5
```
**The self-test is a gate, not a courtesy.** It plants one input per verdict class and requires each
to be produced. An instrument that returns AGREE for everything passes a "does it run" check and
fails this one.

**Step 2 — exchange the digest.** Each MSTR sends its own:
```bash
python .tools/integrate-directives.py digest --ref origin/CLOUD      # or origin/SITEZ
```
This is the *"where has your fabric taken the directives"* half. Per row: the placement token, a
short hash of the placement text, the member list, and each member's `status` / `dep_stage` read
from its own JSON. ⛔ **Send it over the bus AND land it in the peer's MCP inbox if it is long** —
a bus body lives only in a session-scoped file, and this is a record.

**Step 3 — resolve, per the table.** `CONTENT-DIFFERS` on a row you do not own: take the owner's copy
whole. On a row you DO own: yours stands, and say so rather than assuming the peer will infer it.
`PLACEMENT-DIFFERS`: apply the two sub-cases above. `UNOWNED` / `ROW-MISSING`: surface, do not fix.

**Step 4 — merge, commit, push.** ⛔ **MERGE, NEVER REBASE** (shared branch). The register write is
the register owner's act; the push is the integrator's. **State the push as a MEASURED value** —
`git ls-remote` — because until it lands, the peer cannot read the row and both fabrics may believe
they own it.

**Step 5 — read the digest for DRIFT, which is the part that pays for itself.** The digest surfaces
things the compare cannot, because they are true on BOTH sides:
- a **live directive whose only member reads `closed`** (found on the first live run: D6 Opal
  Analyst — the register shows a live workstream whose sole member is closed);
- a directive with **no members at all**;
- a member named on the row whose **project file does not exist**.
**None of these is a sync failure. All of them are register defects the sync makes visible.**

## Cadence

**Ad hoc, and after any of these — each one opens the window this skill exists to close:**
a placement ruling · a directive mint · a project added to or removed from a row · any
`/integrate` leg. ⛔ **Never on a timer.** A scheduled register reconcile is a monitor, and monitors
are under a standing moratorium; it also invites a sync that fires while a sovereign act is half-recorded.

## What it does NOT do

Writes nothing. Cuts no TO. Seats nobody. Resolves no placement. Adds no field to the register.
It reports, and the acts that follow are the register owner's and the integrator's, taken deliberately.

## Cost and non-application

Cost: two read-only commands and one message per run. Non-application: it says nothing about code,
deploys, or any file other than the register and the project JSONs it reads for status. A fabric with
no directive movement since the last run gets `AGREE n/n` and stops there.

## Cross-references

Mechanism `.tools/integrate-directives.py` · the whole-tree reconcile `/integrate` (this is the
register-scoped sibling, not a replacement) · the register itself `org/missions/DIRECTIVES.yaml` ·
`/directives-check` (the single-fabric register dashboard) · transport `/agentbus`.
