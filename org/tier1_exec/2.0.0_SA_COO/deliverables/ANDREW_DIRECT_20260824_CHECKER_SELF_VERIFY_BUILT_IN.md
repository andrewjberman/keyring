# ANDREW-DIRECT 2026-08-24 ~23:5xZ — the message-integrity check BELONGS INSIDE the checker; the fabric-wide re-derivation is duplicated work

**Channel:** the base `2.0.0_SA_COO` terminal (mid-turn, during the fabric-wide LD-0449 message-integrity thread).
**Recorded:** 2026-08-24T23:56Z (same turn). **Recorder:** `2.0.0_SA_COO`.

## VERBATIM

> "Yeah that sounds like duplicated work to me, I also need to understand the mechanics of the checker behind the checker function, seems to me like the "checker" should have have that built in."

## What it binds (SURFACED, not adjudicated — scope is his)

1. **DUPLICATED WORK — CONFIRMED SOVEREIGN.** Five seats independently re-derived a message-integrity check inside ~90
   minutes (subject-vs-diff → byte arithmetic → naive diff → rstrip-both), each finding a real defect in the last. The
   COO stop-call issued at 67235 is RATIFIED by this word, not merely permitted.
2. **HE WANTS THE MECHANICS UNDERSTOOD**, not just the outcome — answered below, and the answer is why (3) is right.
3. ⛔ **THE CHECK BELONGS INSIDE `safe-commit`.** *"the 'checker' should have that built in."* Every seat re-deriving it
   AFTER the fact reconstructs something the tool already holds at the moment of the act — and reconstructs it through
   `git log`, which is where all four failures came from.

## THE MECHANICS, since he asked — why a "checker behind the checker" existed at all

**Rule 14a mandates `safe-commit -F <file>`, never the `-m` form.** That rule is correct: a double-quoted `-m` body is
SHELL-EVALUATED before git sees it, so a backtick or a command substitution in the message EXECUTES (F-010).

**The `-F` form fixes execution and introduces staleness.** It commits WHATEVER IS AT THAT PATH. If the path holds a stale
file — from another session, another seat on the shared `/tmp`, or the seat's own earlier failed step — git commits that
text against the correct diff. **The `-m` form fails LOUDLY on a malformed string; the `-F` form fails SILENTLY on a stale
one**, and every gate passes because the gates check CONTENT, not message accuracy.

**So seats began verifying after the fact — and the verification itself failed four times:**

| attempt | form | why it broke |
|---|---|---|
| 1 | subject vs diff | blind to a stale message about the SAME file — the common case for a seat committing repeatedly to one path |
| 2 | `file_bytes + 1 == commit_bytes` | git STRIPS trailing newlines and re-adds exactly one, so a file ending in a blank line lands on **0** and reads as a mismatch with nothing stale |
| 3 | `diff` of the file against the read-back message | git APPENDS a newline the file does not have → reports a difference on a sound commit |
| 4 | compare with trailing newlines stripped from BOTH, report the first differing index | works; nobody should call it "strictly better" — it is blind to whatever else git normalises |

⛔ **THE ROOT CAUSE, REPRODUCED AT THIS SEAT ON TWO OF MY OWN COMMITS: THE SAME FILE AND THE SAME COMMIT YIELD +1 OR 0
DEPENDING ONLY ON THE SPELLING OF THE FLAG.** The `--format=%B` spelling INCLUDES git's added trailing newline; the
`--pretty=format:%B` spelling SUPPRESSES it. **The byte arithmetic was testing for exactly the one byte that two spellings
of "read the message back" disagree about.** Measured: file 1110 B → commit `92a405e69f` reads +1 or 0; file 1472 B →
commit `d82b3d55ec` reads +1 or 0; both IDENTICAL under the sound compare.

**AND A SECOND FAILURE MODE RIDES THE SAME READ-BACK:** `git log -1` in a SHARED WORKTREE returns whichever seat committed
last. One seat broadcast two peers' hashes as its own tonight because of it.

## WHY HIS DESIGN CALL IS RIGHT — the mechanics make the case

**`safe-commit` is the only actor holding BOTH halves at the moment of the act** — the message file it was handed, and the
hash it just created. Every failure above came from a SEAT reconstructing that pairing afterwards: the wrong flag spelling,
the wrong seat's HEAD, the wrong normalisation assumption. **A check inside the tool reads neither a format flag nor a
"latest commit": it knows its own commit's hash and the file it was given.**

**PROPOSED SHAPE (routed to CTO as tooling owner; NOT implemented on this record):** after a successful commit,
`safe-commit` compares the message of ITS OWN new hash against the `-F` file with trailing newlines stripped from both; on
a difference it FAILS LOUD naming the first differing character index; it prints the subject line either way so the seat
sees what became immutable. Cost: one comparison per commit. **It also removes the reason a seat would ever reach for a
"latest commit" read — the second bug, closed by the same act.**

⛔ **NOT A GATE ON WORK** (no-inferred-gates): it adds no approval step, no hold, no reviewer. It is a tool verifying its
OWN act — the same class as the contamination and sensitive-file checks `safe-commit` already runs.

## Also standing in his word: STOP THE RE-DERIVATION

The instrument is settled at form 4. **Further passes at the check itself are duplicated work by his direct word**, and the
durable fix is the built-in. Seats carry: unique per-commit filename, write+commit in ONE chain, read the subject line
before it becomes immutable, anchored author matching for any per-seat census.

## POSTSCRIPT — the gate fired on this very record, and it is a false positive worth routing

My first attempt to commit this file was DENIED by `never-rules-gate.sh` with the F-010 message ("'git commit -m' carrying
a backtick or a command substitution"). **The invocation used `-F`, correctly.** The gate matched because the raw command
TEXT contained the two-character token `-m` — inside this document's prose, explaining the rule — alongside ordinary shell
substitutions elsewhere in the same compound command. **A record ABOUT the hazard was blocked for describing it.**
I did NOT use the audited override; I restructured (file written by the editor, commit issued with a minimal command).
⛔ **This is the exact risk CLAUDE.md's own F-010 note names — *"do NOT cite F-010 as licence to text-match a mechanism"* —
and it is a false positive on the SANCTIONED path, which is the shape that gets a gate routed around rather than obeyed.**
Routed to CTO as a gate-shape item: the matcher should require the `-m` flag in FLAG POSITION, not the token anywhere in
the command string. Surfaced, not fixed — the gate's enums are deliberately outside a non-tooling seat's write path.
