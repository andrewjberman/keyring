# The registry scope-disclosure fix, and a citation-hygiene chain in which I was twice the defect

**archetype:** MIXED (VALIDATE + IMPLEMENT)
**Seat:** `4.0.0_SA_CRO` (base). **Window:** 2026-09-19 ~03:08-07:30Z. **Prior log:** `41a127dc12`.

## Current State

One commit this window. The spawn task closed and was accepted in the prior log's window; everything
here is event-driven work off the inbox.

`9dfa9a4c0f` -- `lib/opal_naming.py`, 35/8, **ON ORIGIN**. Every UNSCOPED `registry@` printer now
discloses its scope. Zero crons, watcher live, `IDLE: available`, inbox empty both probes.

⚠ **A RANGE NOTE THAT IS ITSELF THE WINDOW'S THEME:** `git log 41a127dc12..CLOUD --author=4.0.0_SA_CRO`
returns NINE commits, and eight are `~Y`/`~Z` lane work that entered CLOUD by merge from site Z. The
range answers *what arrived* , not *what this session did*. Same shape as everything below: a sound
instrument answering a question adjacent to the one asked.

## The one build

`1.0.0_SA_CTO` (98149) measured a two-hash trap: one `generate` run prints `registry@<a>` in its summary
while a file it wrote in the same run carries `registry@<b>`. The summary hashes ALL registry files; a
per-target mark hashes only the files that target reads. The mark printed its scope as `over <files>`;
the summary printed none, so the whole asymmetry fell on the reader -- and that seat was one `diff` from
reporting a stale input on a SIGNED never-widen sign-off.

⛔ **IT WAS THREE CARRIERS, NOT THE ONE REPORTED.** The report named GENERATE. A census of the notation
returned four sites: the docstring (describes the SCOPED mark, correct) and THREE unscoped printers --
VALIDATE, GENERATE, and the census report's prose *and* its fenced json. Patching only the reported line
would have left the same ambiguity in two places. Also folded `registry_hash`'s inline listdir into one
`registry_file_names()`, so a scope LABEL and the HASH it labels read the same function -- two copies is
precisely how they would drift.

Exercised, not asserted: the trap reproduced and read back in one screen, summary `over all 6 registry
file(s)` beside marks `over scopes.json`. ⭐ **The count is 6, not the 5 I assumed before computing it**,
which is the argument for deriving the label rather than typing it. Tests 2F/91P before and after, same
two; VALIDATE rc=0, hash unchanged -- no registry byte moved.

Declined in the same message, as the registry owner's call: no regen sweep of the eight stale provenance
marks. Bodies are all current, and those files sit in the AE and DS lanes where this seat cannot land
them at all. Told the CTO to say so if the cross-lane point changes the calculus rather than treat my
own first answer as settled.

## Where I was the defect -- twice, on the same axis

**1. "Has never existed on this box."** I falsified the NEW addresses in the CTO's law edit `34f73569ed`
(the instrument it had not run) and found one of two unresolvable -- a good catch, and the CTO landed
`6f79b07dda` on it. But my sentence overstated its own evidence: a filesystem `find` measures the
PRESENT, and "never" is a claim about HISTORY. The CTO then repeated the phrase in a law-edit broadcast
and commit message. ⭐ **Found by running the CTO's own S98 tell -- NEVER/ALWAYS/EVERY/NOTHING/ANY in a
sentence whose evidence names one object -- over my own output**, which is what that tell is for.
Chasing it turned up an instrument I had not known existed: **the box memory tree is itself a git repo.**
It agrees (never added in any commit, positive control passes) but cannot support a "never" either --
4 commits, 1014 of 1448 files tracked. The bounded form the CTO adopted verbatim:

> ABSENT NOW (0 of 1447 by filesystem census) and NEVER ADDED in any of the 4 commits of the memory
> tree's own git history (positive control passes), which tracks 1014 of 1448 files, so a file that
> lived and died between snapshots would be invisible to both instruments.

**2. And in the message correcting that, I did it again, worse.** I wrote "the phrase lives in a
broadcast, not in the file" -- a claim about where it lives across BOTH seats' artifacts -- **having
censused neither.** Not a narrow census; none. The CTO measured its own carriers and found the phrase in
the law edit's COMMIT MESSAGE, which is the artifact a future reader opens to learn why a law changed.
My half held: 1 of my 1446 commits matches "never existed", and it is `ff1b76243b` from 2026-08-10 on an
unrelated subject. **It held WITHOUT EVIDENCE, which at the time is indistinguishable from not holding.**
⚠ That 08-10 hit is not noise -- the same grammatical shape, in a commit subject, six weeks earlier, in
a second seat. That is what makes the tell worth a rule rather than a row.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-read --enumerate` | `opal_naming.py` / `registry_hash` | 7 hits / 2588 lines, 142 sections | found the scoped-vs-unscoped call sites |
| `comp-read --enumerate` | `opal_naming.py` / `registry@` | 4 hits, banded | **the census that turned one carrier into three** |
| `comp-read --enumerate` | `opal_naming.py` / `over ` | 11 hits | gave the mark's `over <files>` idiom to match |
| `comp-find` | `feedback_no_shadow_channels...` `--files --all` | 70 hits / 168,539 files | 2 live law carriers, ~39 historical; nothing outside org//docs//infra/logic/ |
| `python -m pytest` | `lib/tests/test_opal_naming.py` | 2F/91P before AND after | regression bound on my own instrument, not the CTO's report |
| `python lib/opal_naming.py generate` | `--out <scratch>` | 10 written | the positive control that proved the fix readable |
| `git log --grep -i` + count | my 1446 commits | 1 match, 2026-08-10 | denominator, no head -- a date-ordered head would have hidden it |

**GAPS:** (1) The rail aborted a compound call whose LAST segment was a gated `comp-read` pipe, so the
python edit in the FIRST segment never ran -- caught by reading the numstat, not the exit status.
(2) `# rail-checked:` used twice, correctly: `~/.claude` box memory and a scratchpad run-output dir are
both OUTSIDE the repo corpus, where `comp-find` returns 0-of-0 (out-of-corpus, not absence).
(3) A boolean substring probe on my own repaired file returned TRUE and I read it as a REVERT -- it was
my own explanatory text naming the dead file to declare it dead. Banked as its own memory trap.

## Blockers

None. Step 4 (Andrew removing the buckets' access policy at a console) is parked on his presence per his
~06:3xZ word, owned by `2.0.0_SA_COO~B`, not this seat.

## Next Steps

1. [`1.0.0_SA_CTO`] S95's two red tests -- whether `name()` or the worked cases are wrong. I reproduced
   and deliberately did not adjudicate; it needs the NAMING_SCHEMA intent for the system slot.
2. [Andrew] Remove the bucket's access policy on `opal-data-inflection` / `opal-data-cottonwood`; and the
   harvest tenancy fork MSTR re-asked in words.
3. [`4.0.0_SA_CRO`] Event-driven; re-arm the watcher each expiry.
