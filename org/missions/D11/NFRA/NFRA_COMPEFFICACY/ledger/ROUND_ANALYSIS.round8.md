# ROUND 8 ANALYSIS -- NFRA_COMPEFFICACY

**Seat:** `1.0.0_SA_CTO` (L10, the CTO's one send) · **Stamp:** 2026-09-10 ~06:1xZ
**On the slug:** `surprise-channel/adjudications/ADJUDICATION_v1.md` @`98554ed525` (`3.0.0_SA_CVO`, msg 95035;
rows C-S10, C-S11; 14 rows) · **Packet:** `ledger/L8_PACKET.round8.md` @`6b0e8258c9`, sha256
`f2b152b9eaf4f9e6314ab65dad19687f6657f927a20e6a331a0fa0461bf26f5c` over 10,414 bytes, hashed by the issuer
after its own commit and re-computed independently at the CVO · **Graded against:** PRD **v0.11**

---

## 1. Coverage

**2 of 2 orders terminal and drained**, both instances re-validated at the issuer's seat with criterion ids
taken from the ORDER AT HEAD. **0 of 51 investigation items undispositioned**, 0 malformed. The one duplicate
id the census reports is the pre-existing S34 collision recorded at C-S2 and is not this round's. No PRD
addendum for coverage — but the endpoint changed for a different reason (§4).

**Grades: 8 REALIZED, 2 NOT_EVALUATED**, unchanged in count from round 7 and changed entirely in what the two
mean.

## 2. What round 8 actually fixed, and why it existed

This round exists because of the CVO's own S40, and it answers that row's question better than the row asked.

**E1-AC3 — the hash-pinned asset.** The fix shape was chosen against an alternative **measured to be blocking
rather than merely costlier**: the verifier hashes RAW bytes, so a normalised manifest would have stopped the
alarm while the bytes still differed, and would have **moved the false alarm from the worker slots to the main
tree** — and making it work needs the verifier, which the order forbids touching. The reading cites this
repository's own prior refusal of that shape: normalising inside a comparator blinds a tamper detector to a
real whole-file rewrite in order to silence a checkout artifact.

**The stronger attribute was chosen over the narrower one on a hazard the CVO's row never named:** stopping the
conversion alone leaves the default text merge armed on a hash-pinned file, and **a clean auto-merge of such a
file yields bytes matching neither parent and breaks the pin WITH NO CONFLICT.** A second, quieter instance of
the same disease, found while fixing the first.

**And the answer to what S40 actually asked is the round's sharpest single fact.** The directory's other member
was never converted — and **not by any rule.** Git's own binary heuristic classified it on a NUL at byte offset
one, against no NUL in the first 8,000 bytes of the member that WAS converted. **Two members of one directory,
one protected and one not, with ZERO declared difference between them: the sibling's safety was INCIDENTAL to
its file format.** A check scoped to the member the row named would have certified the directory on a property
one member holds by accident. That is the shape this seat has been ruling on all night, **arriving inside the
fix for it.**

**E2-AC3 — a worker can now verify its own tool edit**, and it is measured rather than asserted: a marker
planted in a fresh worktree's tool was executed **by the bare name from that worktree and not from the main
tree**, with the file restored byte-identically on both sides. Before this cell the same invocation returned
rc 0 with a byte-identical answer **from the wrong file.** The fallback's loudness is graded in BOTH directions
— enough to tell a reader, not enough to tell a program, because it is on stderr with no machine-readable field
and a caller capturing only stdout sees nothing — with the sufficient instrument named and its per-invocation
cost stated. The new bound is stated FROM measurement with its denominator: four completions spanning 651.6 to
826 seconds, a 27% spread, **bound set above the maximum rather than at it**, with the reason given.

## 3. Seven of nine dispositions are defects in the cut or in the estate's own controls — every one surfaced by the assignee

The two blocking ones are the round's best record and they are properties of **my gates**, not of the work:

- **A granted path was uncommittable by the lane it was granted to.** A commit touching those tools is refused
  while a generated state file is stale, and **the staleness pre-dated the order** — proven at the source, not
  asserted.
- **The clearing act could never have cleared it.** The fingerprint reads the WORKTREE, so a regeneration on
  any tree the pending edit is not in re-drifts the instant the edit exists, and staging does not help.

The worker **proved the issuer's regeneration had LANDED rather than assuming it failed**, by watching the
refusal fingerprints move. **The override was never spent across all three refusals**, on the reasoning that it
exists for a case where regeneration is impossible and here it was impossible only FROM OUTSIDE THE TREE.
*That is the distinction between a blocked act and a blocked location*, and it is worth more than the fix.

**Carried with its wording:** the staleness predicate means to stop a seat laundering a peer's unlanded work,
and **it cannot tell a peer's unlanded work from the file THIS VERY COMMIT IS LANDING.** A gate gap, not a
misuse — and the **third gate found blind to its own question tonight.**

Two accept-side defects, both mine in class: one arm required byte-equality against **a baseline itself
captured under the broken fallback** — a criterion that could not have passed on a correct world. And one bound
is **smaller than the thing its own arm measures**, the exact defect the cell exists to fix, one level up,
inside the accept that grades the fix. **It is a real weakening and it is DISCLOSED**, and the CVO graded it as
such because *the disclosure is what makes it gradeable: a substitution printed beside a verdict can be
weighed, a substitution made silently cannot.*

## 4. THE ENDPOINT CHANGED, and the defect is the same one I ruled on an hour ago in another project

**FWD-4's `DONE WHEN` read "EXERCISED — the last tool's state has been READ BY ANDREW."** That grades the
outcome on a PERSON'S ACT. No seat can take it — not a driven run, not a history read — so it was **unprovable
by the fabric rather than merely slow**, and no amount of work could ever have closed it.

**This is the IDENTICAL defect ruled on `NFRA_OUTSET` FWD-4 at ~04:1xZ. Same id number, same shape, different
project.** Two projects carried it at the same coordinate, and the second was found **only because this round's
slug sent me back to the endpoint** — by no control, no gate, and no census. PRD v0.11 re-points it, id KEPT:
it grades on the list's own artifact carrying all three states with a printed denominator and no tool carrying
none, readable by anyone on demand. **Andrew's reading is the CONSEQUENCE of the property holding, never its
criterion.** Round 9 grades it against the new line; this round records it NOT_EVALUATED rather than grading a
line minted in the same tick.

## 5. FWD-9 — the mechanism is PROVEN and the outcome still cannot grade, on its own words

Both surfaces landed. The pin now holds in a fresh worktree **by construction rather than by luck** (binary
set, text/diff/merge unset; the attribute reads on BOTH directory members where the converted one showed none;
683,666 bytes, zero CRLF pairs, hashing to the manifest's own value). And a tool edited in a fresh worktree is
**executed from that worktree by bare name**, where it previously answered from the wrong file with rc 0.

**And FWD-9's own text reads "the fix is on the SHARED BRANCH, never only on one machine." Local is 388 commits
ahead of `origin/CLOUD`. The fix is on ONE MACHINE right now**, so the outcome refuses itself — measurably, not
cautiously.

**This is not a wait in the forbidden sense.** It is gated on ONE NAMED HUMAN ACT — Andrew's push, which he
said he would ask for before signing off — and this paragraph is the express qualification the L2 law requires.
The Codex allocation carried at this seat tests a **different axis** (another RUNTIME, not another clone) and
does not gate this outcome.

## 6. Product, not residue

The assignee **caught a defect in its OWN control before the run**: arm (c) first probed with a flag that
**prints the target and exits before the exec**, so a marker planted inside the tool could never have appeared
and **the arm would have been a CONSTANT.** A detector that cannot return non-zero on a positive, caught by the
seat holding it. Four further defects came from **exercising the GENERATED ARTIFACT in a scratch environment
rather than reading the generator** — the worst would have baked a fallback pointing at the very checkout that
ran it, giving a not-found from every one of these tools on the box for any caller outside a repository.

`dep_stage` stays **EXECUTING**.

## Push state
LOCAL. `origin/CLOUD` @`c6bcb7b12b`; local **388 ahead**, measured this tick. Nothing in this round is readable
at site Z until Andrew's push word — **which is also exactly what FWD-9 is waiting on.**
