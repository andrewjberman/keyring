# SPAWN BRIEF -- `3.0.0_SA_CVO~C`: `comp-read --enumerate` (file-internal enumeration with BANDS)

Author `3.0.0_SA_CVO` (base/MAIN). Andrew-direct at the CVO terminal 2026-09-01 ~00:4xZ. His framing,
VERBATIM:
> It should enumerate, how can we make it do that? It should have the same efficacy as comp-find just
> at the file-content level. I think that would make it very useful for reading whereas now its "most
> of the way" to what I believe it should be.
> ... The reason I made the comment about grep is because we "allow" grep for certain functions, the
> likes of which appeared to be read-style functions (check hooks to confirm), hence my confusion.

HOOKS CHECKED, HE IS RIGHT, AND IT IS WRITTEN IN THE HOOK. `.tools/hooks/comp-tool-hud.sh:177-178`:
> `#  (a) the search is scoped to a SINGLE FILE -> grepping a file's internals, NOT a`
> `#      relationship search (comp-pipescript io gives the I/O contract, not internals).`

Base CVO retains proof-of-spec management and does NOT build this. Andrew triggers the test; `~C`
reports READY and does not self-certify. Same contract as the stage-4 brief, which `~C` met 7/7.

---

## 1. THE ONE-SENTENCE MISSION

`comp-read` answers *"what is in this file and which parts bear on my question."* It cannot answer
*"where does this token occur, how many times, and in what kind of code."* **Build that second mode.**
comp-find's efficacy properties -- printed denominator, graded bands, no truncation -- at file grain.

---

## 2. WHY, WITH THE MEASUREMENT THAT MAKES IT WORTH DOING

`org/mcp/comp-which-rail.log` (45,119 rows), measured 2026-09-01T00:4xZ:
```
  ALLOW-SEARCH  shape=single-file      1,021      2026-08-28T19:57:41Z -> 2026-09-01T00:43:18Z
  ALLOW-SEARCH  shape=pipe-receiver    1,011
  DENY (recursive, routed to comp-find) 1,132
```
>> **1,021 single-file greps in ~3 days (~340/day), nearly matching the ENTIRE denied-recursive class.**
   That is the volume of file-internal reading currently done through raw grep -- no denominator, no
   bands, no false-zero protection. **The carve-out exists because NO comp-tool covers file internals.
   This build is exactly that gap.** <<
The `ALLOW-SEARCH shape=single-file` rows were instrumented specifically as *"the denominator the 08-28
audit found missing,"* with a revisit due ~2026-09-04 (CLAUDE.md Rule 21).
⛔ **NAMING, NOT PROPOSING:** whether the single-file carve-out then CLOSES is Andrew's call and
`1.0.0_SA_CTO`'s, not a consequence of this build and **not something `~C` may implement.** Do not touch
the hook. An agent-made gate is invisible to Andrew (CLAUDE.md s.2).

---

## 3. ALL RELEVANT PATHS (verified present 2026-09-01T00:4xZ)

### Build target
```
.tools/comp-read                     779 lines, python3, THE FILE YOU EDIT
~/bin/comp-read                      bootstrap shim, DO NOT hand-edit
                                     (regenerate: bash .tools/provision-path-shims.sh)
```

### Internal anchors (line numbers at read-vintage -- RE-DERIVE before editing)
```
:218   heading backend
:263   "via whole-file"      the no-structure fallback -- YOUR DEGRADE PATH, see s.4
:273   python-ast backend
:279   top-level-keys backend
:283   markdown backend
:479   the fired-panel text that already points users at `--for`
:506   " Full: comp-read %s --for \"<question>\"" -- the existing affordance string
:538   def main()
:541   argv = sys.argv[1:]   -- MANUAL argv parsing, NOT argparse. Match the existing style.
:543   the usage line: comp-read <file> [--for "<question>"] [--at LINE] [--top N] [--all-quals]
:557   the --for branch     |  :566  the --all-quals branch  -- imitate these
:635   "SALIENT: (no --for question given...)" -- the no-question path
:715   the QUALIFIERS counter + "--all-quals" affordance
```

### Precedent to imitate (the tool `~C` just shipped)
```
.tools/comp-adversary                             the stage-4 build; its selection rule is the
                                                  model for a Rule 24 taxonomy record in a header
.tools/tests/test_comp_adversary_stage4_packet.py YOUR TEST PATTERN -- ~C wrote it, reuse the shape
.tools/tests/test_comp_adversary_path_truncation.py  the older pattern
```

### The rail (context only -- DO NOT EDIT)
```
.tools/hooks/comp-tool-hud.sh        :97-105 the carve-out, :138/:141 shape detection,
                                     :177-178 the stated rationale quoted above
org/mcp/comp-which-rail.log          the ALLOW-SEARCH denominator
docs/architecture/NFRA_COMPRAIL_PRD.md   comp-find's trap list -- your bands must not repeat them
```

---

## 4. WHAT `--enumerate` MUST DO

### The shape (illustrative, not a spec of exact wording)
```
comp-read <file> --enumerate '<pattern>'
  31 hit(s) across 371 lines / 12 sections scanned        <- DENOMINATOR, always printed
  DEF        3   in a def/class signature
  CODE      18   in executable statements
  DOCSTRING  4   in prose describing the code
  COMMENT    6   in comments
  whole-value matches: 0   |   substring matches: 31      <- THE DISCRIMINATOR, s.4.2
  [then the hits, banded, never truncated]
```

### 4.1 THE BAND IS THE ENTIRE DIFFERENTIATOR FROM GREP
`comp-read` already parses structure (`:218/:273/:279/:283`). **Grep returns 31 undifferentiated lines;
this returns where each one lands, and that changes the conclusion** -- *"26 of 31 are in comments"* and
*"18 are in executable statements"* are different findings, and grep cannot distinguish them.
⛔ **THE BAND SET IS A SCHEMA. Rule 24 TAXONOMY LAW BINDS:** (i) MECE over a DECLARED domain -- every
hit lands in exactly one band and the bands sum to the total, asserted by the battery; (ii) SAME GRAIN;
(iii) INTENT COHERENCE -- one axis only, "what kind of region is this hit in", never mixed with
salience or recency; (iv) STATE COHERENCE -- name which bands one remedy does NOT move. **The
four-postulate record goes in the source header**, exactly as `~C` did for the S1-S4 selection rule.
⚠ Bands are backend-dependent. A python-ast file supports DEF/CODE/DOCSTRING/COMMENT; a `.env` at
`top-level-keys` does not. **Per-backend band sets are fine; a band set that pretends to a distinction
the backend cannot make is not.** At `:263` whole-file (no structure), **degrade honestly**: print the
enumeration with its denominator and state that banding is UNAVAILABLE for this file type. A band that
cannot fail is not a band.

### 4.2 THREE PROPERTIES INHERITED FROM comp-find -- each one earned by a MEASURED failure
1. **A ZERO CARRIES ITS DENOMINATOR.** `0 hit(s) across 371 lines / 12 sections scanned` is safe;
   grep's silent nothing is not. Measured 2026-08-31/09-01: `3.0.0_SA_CVO` produced TWO false zeros in
   one session (a backticked-hash probe, and a `fullmatch [0-9]{10}` against an embedded id), and
   `0.4.0_DE_ClientPlatform~D` produced a third (`--name '**/dir/file'` matching the BASENAME). **All
   three read as verdicts.**
2. ⭐ **WHOLE-VALUE vs SUBSTRING, BOTH PRINTED, ALWAYS.** This is the highest-value line in the build.
   `0.7.0_AE_CloudOps~G`'s serve-precondition control returned `UNMAPPED-RELATIONSHIP-*: 0` because
   `rel.startswith('UNMAPPED-RELATIONSHIP')` missed 132 rows whose values begin `UNLABELLED-`. **A line
   reading `0 whole-value | 132 substring` would have caught it in one read** instead of a [STOP], a
   fabric halt and a CTO ruling. Anchor-sensitivity is the file-grain equivalent of comp-find's
   case/substring trap.
3. **NEVER TRUNCATE; PAGINATE EXPLICITLY.** `--limit/--page`, and a page is not an answer. Never `head`
   a census (CLAUDE.md Rule 21).

### 4.3 A DISTINCT MODE, NOT A CHANGE TO THE DIGEST
⛔ **Do NOT fold enumeration into the default digest output.** Rule 24 (iii): enumeration and
summarisation are different intents on different axes. **And there is now a live consumer:**
`comp-adversary` stage 4 shells out to `comp-read` for its packet -- changing the default digest shape
would silently alter every `validation_context_declaration` the estate emits. `--enumerate` sits
ALONGSIDE `--for`/`--at`/`--top`/`--all-quals`, in the same manual-argv style at `:557`.

---

## 5. ACCEPTANCE -- criteria that CAN FAIL (write them before the feature; run the battery RED first)

1. **A NEW control that FAILS on the pre-build binary.** Run it red before building, and say so in the
   READY report -- `~C` did this correctly for stage 4 and it is the reason that build was creditable.
2. **BAND CONSERVATION:** on a python-ast file, the per-band counts SUM to the total hit count, asserted
   by the battery, over at least 3 files with different backends. An off-by-one in banding must fail.
3. **THE ANCHOR ARM (s.4.2 #2), with a REAL specimen, not a synthetic one:** enumerate
   `UNMAPPED-RELATIONSHIP` against
   `org/tier2_senior/0.4.0_DS_ClientPlatform~V/deliverables/emissions/perfrp_book_advisor.json`
   (14,947,901 bytes). It MUST report **whole-value 0 / substring > 0** and must NOT report a bare 0.
   ⛔ **This is the exact defect that halted the fabric on 2026-08-31. If the arm passes on the
   pre-build binary, it is the wrong arm.**
4. **ZERO WITH A DENOMINATOR:** a pattern absent from a file prints `0 hit(s) across N lines / M
   sections scanned`, never a bare zero and never silence.
5. **HONEST DEGRADE:** a file hitting the `:263` whole-file backend enumerates correctly and states
   banding UNAVAILABLE. It must NOT emit band rows of 0 that imply the distinction was tested.
6. **NO REGRESSION IN THE CONSUMER:** `comp-adversary --self-test` still returns **PASS 5/5** and a
   `comp-adversary compose` on
   `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_PERFRP.TO-R1-DS_PROOF_OF_SPEC.json`
   still yields `selected: 12 of 542` with a class census summing to 542. **Print both, before and
   after.** The digest path must be byte-comparable.
7. **RUNTIME:** report per-file enumerate time. comp-read digests measured 313-562 ms (n=4, `~C`).
   Enumeration on a 15 MB JSON will not be 500 ms -- **measure it and state it**; do not assume.
8. **PAGINATION:** a pattern with more hits than the page size shows the page, the total, and how to
   get the rest. No silent truncation at any limit.

---

## 6. SCOPE BOUNDARIES

- ⛔ **SINGLE FILE. NO corpus, NO pathspec, NO recursion, NO glob expansion.** The moment it takes a
  directory it becomes a worse `comp-find` and the two tools blur. If a caller wants a corpus, the
  answer is `comp-find` -- and that routing line belongs in the usage text at `:543`.
- ⛔ **Do NOT touch `.tools/hooks/comp-tool-hud.sh`.** Not the carve-out, not the shape detection, not
  the log. See s.2.
- ⛔ **Do NOT touch `comp-adversary`.** It is a consumer; criterion 6 protects it.
- Do NOT fix the `COMMIT_RE` backtick bound (`.tools/comp-adversary:57`) -- still owned by
  `0.8.0_AE_CloudComp`, finding 90279. `~C` correctly left it alone in stage 4; keep doing that.

---

## 7. CONSTRAINTS (non-negotiable)

- **Build ladder:** the section backends, the qualifier extractor and the argv parser ALL EXIST in
  `.tools/comp-read`. Extend them. New code is the LAST resort; a second file-parsing engine is a
  shadow path.
- **No shadow/build-alongside tool.** Edit in place. No `comp-read2`, no parallel enumerator.
- **No non-ASCII** in code or output. `OK:` / `WARN:` / `ERROR:` / `SKIP:` / `BLOCKED:`.
- **Commit:** `.tools/safe-commit.sh --author "3.0.0_SA_CVO~C <3.0.0_SA_CVO~C@opal.agent>" -F <msgfile>
  -- <paths>`. No pre-`git add`. `-F` not `-m`. Message file written by a NON-SHELL writer (Write tool
  / python).
- **Gate:** run `.tools/commit-gate.sh`. `.tools/comp-read` is python WITHOUT a `.py` extension -- the
  gate reads only `.py/.sh/.tf/org/projects/*.json` and will report **"checked 0 of 1 file(s)"**. That
  line is NOT evidence of a clean gate. Run `python -m py_compile` and `ruff` on it explicitly and say
  which instrument you used.
- **Never rebase on CLOUD.** Rejected push = pull-merge, re-push. Push may be REFUSED by the
  integrator-only gate -- that is expected; report push state as MEASURED (`git ls-remote`), never
  assumed, and do not override.
- **Zero crons.** `/watcher` once.

---

## 8. REPORTING

- Report READY to `3.0.0_SA_CVO` (base -- grades it), cc `1.0.0_SA_CTO` (rail owner) and
  `0.8.0_AE_CloudComp` (comp-tool build owner).
- Surprise channel: anything odd off-task = ONE line to `3.0.0_SA_CVO`, KEEP WORKING.
- In the READY report, state the s.5 battery result **per criterion**, and state which arms were run
  RED against the pre-build binary first.

---

## 9. WHAT `~C` MUST NOT DO

- Do not close, propose closing, or modify the single-file grep carve-out.
- Do not change the default `comp-read` digest output.
- Do not add a corpus/pathspec/recursive mode.
- Do not self-certify or ship. Andrew triggers the test.
- Do not adjudicate D2/D8 substance -- base CVO holds proof-of-spec management.

`3.0.0_SA_CVO`
