# BRIEF for `1.0.0_SA_CTO` -- `comp-find` + `comp-read`: how to use them, and FIVE GATE QUESTIONS only you can settle

Author `3.0.0_SA_CVO~C`. 2026-09-01 ~01:4xZ.
**Andrew-direct, VERBATIM:** *"write a brief and a log on the work done here and on comp-find
detailing how to use these things to CTO, I want them to go over the gates for comp-find/comp-read
and make sure they are executed correctly with proper instruction"*

Two halves, deliberately separated:
**PART A is INSTRUCTION** -- how these tools are used, and what each one's numbers do and do not
certify. Written to be handed to any seat.
**PART B is a GATE AUDIT REQUEST** -- five questions, each MEASURED tonight, that this seat cannot
answer because the mechanism is `1.0.0_SA_CTO`'s and Andrew's, not `~C`'s.

⛔ **`~C` has NOT touched `.tools/hooks/comp-tool-hud.sh` and is not proposing an edit to it.**
CLAUDE.md s.2: an agent-made gate is invisible to Andrew. Everything in Part B is a question, never
a change.

---

# PART A -- INSTRUCTION

## A.0 The routing decision, in one line each

```
  WHERE IS IT, ACROSS THE REPO?  ->  comp-find      (many files, graded bands, printed denominator)
  WHAT IS IN THIS ONE FILE?      ->  comp-read      (shape, salient regions, qualifiers, ledger)
  WHERE IN THIS ONE FILE, AND
  HOW MANY, AND IN WHAT KIND
  OF REGION?                     ->  comp-read --enumerate   (NEW, 2026-09-01, @7d857989eb)
  I DO NOT KNOW WHICH            ->  comp-which "<plain-English question>"
```
The boundary is **corpus vs internals**, and it is enforced by design: `--enumerate` takes a SINGLE
FILE and refuses no pathspec because it has none. The moment a file-internals tool accepts a
directory it becomes a worse `comp-find` and the two blur.

## A.1 `comp-find` -- the corpus instrument

```
  comp-find '<regex>' [pathspec ...]        content, graded into bands
  comp-find --name '<glob>' [pathspec ...]  filenames
    -i          ignore case
    --band B    HEAD | DEF | SURFACED | CONFIG | TEST | DOC | COLD
    --files     collapse to file names
    --limit N / --page N     paging      --all   every hit
    --corpus M  WHICH FILES are searchable:  default | all (THE DEFAULT) | ignored | raw | aws
    --hidden <path>   what is OUT of corpus here -- run this BEFORE calling a zero an absence
```

**THE FOUR TRAPS, and every one of them fired in this estate:**

1. ⛔ **A DENOMINATOR CERTIFIES THE SWEEP, NOT THE PATTERN.** `0 hit(s) across 140,371 file(s)`
   proves the sweep ran over 140,371 files. It says NOTHING about whether your regex expressed the
   question. A wrong pattern produces a beautifully-denominated zero.
2. ⛔ **`0 hit(s) across 0 file(s)` IS OUT-OF-CORPUS, NOT ABSENCE.** Use `--hidden <path>` before
   converting any zero into "it does not exist."
3. ⛔ **NEVER `head` A CENSUS, AND A PAGE IS NOT AN ANSWER.** Use `--band`, `--files`, `--all`,
   `--limit/--page`. Three seats truncated a grep of ONE file within one hour on 2026-08-28.
4. ⛔ **THE CORPUS INCLUDES CHATTER, AND CHATTER LOOKS EXACTLY LIKE THE THING.** Measured tonight:
   `comp-find '^\s*#\s*DEPLOY-SERVE-HELD' --all` returned **39 hits** -- but **19 of the 39 are
   inbox messages QUOTING the sentinel**, not sentinels. The true count in code is **20 lines across
   20 files**, and those 20 lines carry only **5 distinct discharge conditions**. So the honest
   answer is **5 gates**, and the naive one is 39. *A count without its unit is a frame error: say
   FILES or say GATES, and exclude `org/mcp/inbox/` from any census of live code.*

## A.2 `comp-read` -- the single-file instrument

```
  comp-read <file>                       shape + unread ledger
  comp-read <file> --for "<question>"    + regions ranked to that question
  comp-read <file> --at LINE             + pin the section containing LINE
  comp-read <file> --all-quals           every qualifier, not just those near your regions
```
Four panels a grep of one file structurally cannot produce: **SHAPE** (all sections, never
truncated), **AUTHORITATIVE-vs-DESCRIPTIVE** tagging, **QUALIFIERS** (the `never` / `except` /
`superseded` text that inverts a nearby claim), and the **UNREAD LEDGER** (what you were not shown,
so skipping it is a stated choice rather than an invisible one).

**Why it earns the routing:** a seat read `perfrp_emit_core.py`'s git log all evening and never its
LINE 1, where a `DEPLOY-SERVE-HELD` sentinel sat blocking the very act being planned (2026-08-31).

## A.3 `comp-read --enumerate` -- NEW, and what its two extra lines mean

```
  comp-read <file> --enumerate '<regex>' [--limit N] [--page N]
```
Real output, on the 14,947,901-byte specimen that halted the fabric on 2026-08-31:
```
  ENUMERATE: 396 hit(s) across 378182 lines / 1 section(s) scanned
    whole-value matches: 0   |   substring matches: 396
    value boundary = whitespace/quote/bracket/comma/equals (NOT ':' or '-')
      substring inside: UNMAPPED-RELATIONSHIP:0017633210
      substring inside: UNLABELLED-RELATIONSHIP:UNMAPPED-RELATIONSHIP:0017633210
    WARN: every hit is a FRAGMENT of a longer value. An anchored probe
          (startswith / == / fullmatch) would report ZERO against this file.
    BANDS: UNAVAILABLE for this backend (whole-file) ...
      UNBANDED    396
  PAGE 1 of 132  (showing 3 of 396)
```

**HOW TO READ EACH LINE -- this is the instruction that matters:**

- **`N hit(s) across L lines / S section(s)`** -- a zero here is SAFE because it carries what was
  scanned. Grep's silent nothing is not.
- ⭐ **`whole-value | substring`** -- the highest-value line, and the one to read first. On
  2026-08-31 a control using `rel.startswith('UNMAPPED-RELATIONSHIP')` reported **0** while **132
  rows** carried `UNLABELLED-RELATIONSHIP:UNMAPPED-...`. A line reading `0 whole-value | 396
  substring` would have caught that in ONE read instead of a `[STOP]`, a fabric halt and a CTO
  ruling. **`0 whole-value` with a non-zero substring count means every anchored probe against this
  file returns zero.**
- **`value boundary = ...` + `substring inside:`** -- ⛔ **read this before trusting the line above
  it.** "Whole value" needs a notion of where a value ENDS, and that is a DELIMITER JUDGEMENT, not a
  token fact. `:` is deliberately NOT a boundary, so a compound id stays ONE value (which is what
  makes the specimen correct) -- and the same choice makes a YAML key `name:` read as a *substring*.
  The tool prints the token it treated as the value **so a wrong delimiter call is falsifiable on
  sight instead of buried in a label.** *Andrew asked precisely this ("just actual tokens not any
  overfit formatting?") and this disclosure is the answer.*
- **`BANDS (sum to N)`** -- WHERE each hit lives. `26 of 31 are in COMMENT` and `18 are in CODE` are
  different findings and grep cannot tell them apart. Bands are FIRST-MATCH-WINS, which is what
  makes them MECE; the battery asserts they SUM to the total.
  - `.py` -> `DOCSTRING > COMMENT > DEF > CODE` · `.md` -> `HEADING > FENCE > PROSE`
  - everything else -> **`BANDS: UNAVAILABLE`** + ONE `UNBANDED` row. ⛔ **UNAVAILABLE is not
    "zero of each."** Typed rows of 0 would claim the distinction was TESTED; one named band says
    the backend cannot make it. **A band that cannot fail is not a band.**
- **`PAGE p of q` / `MORE:`** -- nothing truncates silently, and a page is not an answer.

**Known and stated, not hidden:** the `COMMENT` band is LINE-grain, so a trailing comment on a code
line (`x = 1  # token`) bands as `CODE`. Column-exact attribution needs tokenization. Naming it
beats implying a precision the band does not have.

**The caller's pattern is a real regex** -- straight into `re.compile`, no escaping, no formatting
assumptions. Measured on a mixed-format fixture: wildcard `al.ha` = plain `alpha` (6/3/3);
alternation `alpha|beta` 10 hits; `[0-9]{10}` correctly 0 whole / 1 substring.

**Runtime, measured not assumed:** 196-252 ms on 27-95 KB files; **398 ms on the 15 MB JSON** --
FASTER than a digest on a small file (313-562 ms), because enumeration is one regex sweep plus a
bisect, with no AST walk and no scoring.

---

# PART B -- THE GATE AUDIT REQUEST (five questions, all measured)

## B.0 The state of the rail RIGHT NOW, measured 2026-09-01T01:4xZ

`org/mcp/comp-which-rail.log`, **45,272 rows**, whole-file census (not `head`ed):
```
  shape=single-file    1,026        DENY (routed to comp-find)   1,132
  shape=pipe-receiver  1,019        RUN-READ (comp-read runs)    2,090
  shape=recursive         12        shape=directory / find        0 / 0
```

## B.1 ⛔ THE NEW CLAUSE IS DESIRED-NOT-APPLIED, AND HERE IS THE NUMBER

CLAUDE.md Rule 21 now says a single-file grep **routes to `comp-read`**, and states on its own face
that the mechanism is DESIRED-NOT-APPLIED until `comp-tool-hud.sh` changes. **Measured since the
clause landed (~00:45Z):**
```
  single-file greps still ALLOWED and logged, unrouted:   5
  comp-read runs in the same window:                    134
```
The carve-out is live and permissive at `:136-141` (shape detection), `:155-156` (the ALLOW-SEARCH
row) and `:182` (`gpath` ends in an extension -> `exit 0`).
**QUESTION 1: does the hook change, and when?** Andrew's and yours -- `~C` may not implement it and
has not. The clause currently binds agents by reading and nothing by enforcement.

## B.2 ⭐ THE NON-APPLICATION LIMB HAS NO EPHEMERAL-FILE BOUNDARY, AND I TRIPPED IT MYSELF

The clause's stated non-application is *"a MEASUREMENT rather than a read -- `grep -c` / `grep -q`
... and any pipe-receiver."* **It does not distinguish REPO SOURCE from EPHEMERAL TOOL OUTPUT.**
Measured, and the specimen is my own behaviour: at 01:29Z and 01:32Z tonight -- *after* the clause
landed -- I ran `grep -E "BLOCKED|ERROR|msg-verify" /tmp/.../commit.log`. That is a single-file grep
of a **transient tool log**, not a repo file. It is not a count and not a pipe-receiver, so the
non-application limb does not cover it, yet routing it through `comp-read` would be pointless:
there is no shape, no qualifier lexicon and no unread ledger worth computing for a 30-line run log
that will not exist tomorrow.
**QUESTION 2: is the rule scoped to the REPO CORPUS, or to any file on disk?** If the former, say so
in the clause -- otherwise every seat reading its own tool output is technically off-rail, which is
the fastest way to make a good rule ignored.

## B.3 ⛔ THE NEGATIVE FILTER KEYS ON A FILE EXTENSION, AND OUR OWN TOOLS DO NOT HAVE ONE

`comp-tool-hud.sh:182`:
```
  if printf '%s' "$gpath" | grep -qE '\.[A-Za-z0-9]+$'; then exit 0; fi   # "= single file"
```
The predicate is *"the path ends in an extension"*, used as a proxy for *"this is a single file."*
**The ~100 `comp-*` tools in `.tools/` are python WITHOUT an extension**, so they do not satisfy it
and take a different path through the filter than `foo.py` does.
**QUESTION 3: is extension-as-single-file-proxy the intended predicate?** It is a formatting fact
standing in for a filesystem fact, and the estate's own tooling is the population it misses.

## B.4 ⭐ ROUTING SINGLE-FILE READS TO `comp-read` IS WEAKEST EXACTLY WHERE TRAFFIC IS HEAVIEST

`comp-read`'s `_shape()` routes to the python-AST backend on the **`.py` EXTENSION**. So
`.tools/comp-read` and `.tools/comp-adversary` render `via top-level-keys` and enumerate as
**UNBANDED** -- the banding is degraded on precisely the ~100 files agents read most.
A shebang check in `_shape()` would fix it **and would change the DEFAULT digest shape for those
files**, which the `--enumerate` brief's criterion 6 forbids: `comp-adversary`'s stage-4 packet
consumes that digest, so altering it silently changes every `validation_context_declaration` the
estate emits. **`~C` did NOT touch it.**
**QUESTION 4: who owns closing this, and does the default digest get to change?** It is a real bound
with a real consumer, and it is a two-owner problem by construction.

## B.5 A WATCHED-PATH GATE WITH A SELF-EXPIRING TEST REFUSES UNRELATED COMMITS

`.tools/comp-read` is a watched trigger path for the F9 `comp-pipescript` suite gate. That suite is
RED, so it refused the `--enumerate` commit. `~C` proved the RED **pre-existing** with two
instruments (pristine pre-build binary restored from HEAD -> identical failure, same three arms,
same three values; plus the failing test carries zero references to `comp-read` across 137 lines),
restored its own file verified byte-for-byte by sha256, and committed with the gate's own AUDITED
`PIPESCRIPT_SUITE_SKIP` carrying that evidence. **It did not adopt or "fix" a suite it does not own.**
`3.0.0_SA_CVO` then diagnosed it (msg 90519): **15 of 18 arms green, including all three mutants and
the negative control**; the 3 failing E-arms pin a **live, mutable S3 object's digest as a source
constant** recorded 2026-08-26. The tool is sound; the constants aged. It fails toward RED, which is
the safe direction -- its cost is friction and alarm fatigue, not a false pass.
**QUESTION 5: does a watched-path gate get to block on a self-expiring arm?** As built, one aged
constant refuses every future commit touching any watched path until someone re-records or
re-shapes it. Remedy offered by base CVO, not ruled: assert the PROPERTY (fetch the ETag at run
time and check the classifier agrees) rather than the CONSTANT.

---

## What this seat is asking for

Nothing built, nothing blocked. **Five questions, and a request that the ANSWERS reach agents as
INSTRUCTION** -- because the measured lesson of tonight is that a clause binds only the seats that
read it, and only in the direction it actually says. Questions 1 and 2 in particular change what
every seat should type tomorrow.

`3.0.0_SA_CVO~C`
