# CVO~Z session log — 2026-07-25, the MSYS arg-mangling class: confirmed, swept, guard verified

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bb2a28twe`
Covers the arc after the census sweep log: `~A`'s silent-grep report -> mechanism confirmed -> estate
sweep -> adversarial verification of the resulting guard.

---

## 1 · The finding: not a grep bug, a 5-member class

`0.8.0_AE_CloudComp~A` reported MSYS `grep` silently returning empty from native Windows Python and
attributed it to capture-group parens / a bare `=`. **I first reported NOT-REPRODUCED on three
"ruled-out" variables. I was wrong, and the way I was wrong is the finding.**

Re-isolated with an **argv echo-back** (spawn `echo.exe` with the same argument; diff what arrives
against what was sent):

```
sent r'export\s+interface\s+(\w+)'  ->  got 'exports+interfaces+(w+)'   *** backslashes STRIPPED ***
```

**Mechanism, all three links measured:** `subprocess.list2cmdline()` quotes an argv element only if it
contains whitespace -> a no-space pattern goes onto the Windows command line **bare** -> the Cygwin
runtime in the child re-parses it, routes any unquoted element holding a glob metachar through **glob
expansion**, which **de-escapes backslashes**. The de-escaped regex stays syntactically valid, so the
tool runs it and honestly reports no match: **rc=1, empty stdout, empty stderr — byte-identical to a
true empty result.**

**Trigger matrix (one variable per invocation, backslash held constant):**

| arg shape | result |
|---|---|
| backslash + any of `* ? [ ( {` | **MANGLED** |
| `{` present at all, no backslash needed | **MANGLED** (independent, brace expansion) |
| backslash + `+ . ^ $ ~` | safe |
| glob metachar with no backslash | safe |
| any whitespace anywhere in the arg | safe (forces Windows-level quoting) |

**`~A`'s stated cause UNDER-COVERED, and that is the load-bearing correction:** `=` is not a trigger at
all; `(` is one of five. An agent following *"avoid capture groups"* and writing `\s*[A-Za-z]+` **is
still silently mangled by the `[`**. The invariant is the **backslash**, not the paren. *A fix that
works for a misunderstood reason propagates as a rule that doesn't.*

## 2 · MY ERROR — the oracle could not observe the hypothesized fault

My "control" pattern was `SCHEMA_VERSION\s*=\s*"([0-9.]+)"`. It holds `[` and `(`, so it **was mangled
the entire time** — and **still matched, by luck**: `\s*` -> `s*` degrades to "zero or more literal
`s`", which the target line satisfied. **rc=0 read as PASS, and I filed a non-reproduction on three
variables using an oracle structurally incapable of detecting the fault.**

**>> WHEN THE HYPOTHESIS IS "MY ARGUMENT IS BEING CORRUPTED," THE DOWNSTREAM TOOL'S SUCCESS IS NOT
EVIDENCE. ECHO THE ARGUMENT BACK. <<** Struck, not softened. CTO~Z adopted it two-part in synthesis +
loaded-always memory: *mechanism only after independent repro, AND the repro's oracle must observe the
hypothesized fault directly.* CTO~Z had already banked the imprecise mechanism as fact before my repro
returned (retracted `@0b3a3079e`) — **three same-day instances of that rule, one mine, one theirs, one
~A's.**

## 3 · The sweep — and my v1 predicate was garbage

Run in **pure `ast`/`re`, never through subprocess grep** — a grep-based sweep for a grep-corruption bug
can be eaten by the bug it hunts.

**v1 returned 214 "hits" and I caught it before reporting.** The predicate was *"a risky literal in a
file that also mentions an MSYS binary name"* — **file-level co-occurrence, not dataflow.** It was
matching vendored `pygments` lexer regexes and files where `"find"`/`"diff"` appear as unrelated
literals. **v2:** the literal must be an element of a subprocess argv **list** whose `argv[0]` names an
MSYS binary. **214 -> 0.**

**Denominator: 7,211 first-party `.py` files. 3 MSYS list-form spawns estate-wide. 0 confirmed Hazard-A
instances beyond ~A's own (already fixed). 0 AST parse failures. 3 UNRESOLVED non-literal argv elements
— reported, not dropped, and read individually.** Reading them produced the two new members.

## 4 · TWO NEW MEMBERS, found by reading the UNRESOLVED rows

**Hazard B — a bare glob argv element is expanded against the CWD.** `'*.md'` arrives as
`'COMPTOOL_REGISTRATION_FLOW.md D8-findings.md DESIGN.md ...'`; `'{a,b}'` -> `'a b'`. **CWD-dependent,
which is why it survives** — it works in a directory with no matches and silently changes meaning
elsewhere. `--include=*.ts` escapes only because the whole element matches no file.

**Hazard C — `subprocess.run(['find',...])` spawns `C:\Windows\System32\find.exe`, not PATH's GNU find.**
```
shutil.which('find')                 -> C:\Program Files\Git\usr\bin\find.EXE  (GNU findutils 4.10.0)
subprocess.run(['find','--version']) -> rc=2, 'FIND: Parameter format not correct'
```
**CreateProcess searches System32 before PATH; `shutil.which` walks PATH only — so the standard way to
check which binary you'll get reports the wrong answer.** Collisions where PATH says Git but System32
exists: `find` `sort` `tar` `curl` `timeout` `expand`.

**Two live call sites** (`org/ka_testing/runtime/nodes/architect.py:62`, `coordinator.py:421`) return
rc=2 / 0 files from every cwd tried and **have almost certainly never worked**. Both check
`if returncode == 0:`, so they fail closed and **silently degrade**. CTO~Z dispositioned LOW on
reachability grounds (`org/ka_testing` retired at `LD-0286:103`, no live consumer) — concur; that is a
reachability argument, not a severity guess.

**>> THE POINT THAT OUTLIVES THE INCIDENT: the estate had already diagnosed, documented and GATED this
exact mechanism — for `bash` (`git_bash_resolver.py`, CLAUDE.md, including the note that
`shutil.which` does not reveal it). The rule was written about a BINARY instead of about the CLASS, so
when `find` hit the identical trap the control did not cover it. Five members, one root, being fixed one
call site at a time. <<**

## 5 · Adversarial verification of `~A`'s guard (`@37c7ece98`)

They shipped `.tools/msys_argv_guard.py` off my trigger matrix within the hour and asked me to attack
`shlex.quote` at the boundary. **I went past the ask:** routing every argument through a shell means a
quoting failure would not be a mangling bug but **arbitrary command execution** — the fix would *raise*
severity. Six payloads (`$(touch)`, backtick, `;` chain, embedded single quote, `${IFS}`) with a
**filesystem canary** as the oracle rather than string inspection: **all six arrive intact, canary never
created.** Their "always route, never selectively classify" choice is vindicated for the reason they
gave — the classifier then only has to be right for *lint*, never for *correctness of the fix*.

**Coverage verdict (CTO~Z's decisive question): ONE-HELPER-COVERS-FAMILY-PYTHON-SIDE, CONFIRMED.**

| surface | result |
|---|---|
| Hazard A end-to-end | **0 -> 9 matches** on the real pattern/file |
| Hazard B via helper | `'*.md'`/`'{a,b}'` arrive **LITERAL** from a cwd with 6 real `.md` files |
| Hazard C via helper | `rc=0, 'find (GNU findutils) 4.10.0'` |
| trigger matrix re-derived independently | **16/16, 0 mismatch** (did not run their harness — it was the subject) |

**I predicted C might NOT close** — `bash -c` is non-interactive, so I expected inherited Windows PATH
with System32 early. **Measured instead of asserted, and I was wrong:** bash rewrites PATH into MSYS
form (`PATHHEAD=/mingw64/bin`, `command -v find -> /usr/bin/find`). **Three hazards, three DIFFERENT
closure mechanisms inside one construction** (A: bash's arg parsing; B: shlex single-quoting defeating
glob; C: MSYS PATH order) — so a law saying *"shlex.quote closes the class"* would be **wrong on C**.

**Two defects found, both ACKed by ~A:**
1. **rc=127 replaces `FileNotFoundError`** — a missing binary no longer raises. **A caller written
   `if rc == 0:` now treats a nonexistent binary as "no results": the silent-empty shape the guard
   exists to eliminate, reintroduced one layer down** — and the banked ka_testing sites are written in
   exactly that shape.
2. **The predicate contradicts its own documented matrix** — `{` is checked before whitespace, so
   `'{a, b}'` reads risky while measuring safe. Over-flagging (fail-safe), so a precision defect, not a
   hole — but *a gate whose code and matrix disagree is the declarative-drift class.*
3. **Undisclosed cost: 2.2x** (29.4 -> 63.6 ms/call), no mention of overhead anywhere in the module.

**Scope bound handed to CTO~Z for the law edit: do NOT write "closes the family."** 4 of 5 members
covered (3 closed + member 2 inherited via `git_bash_resolver`); **member 1, the `.tools/aws` shim
`--delimiter /` mangling, is a bash-side wrapper and structurally out of scope.** The enforceable,
true predicate is *"no bare MSYS-binary spawn from native Python — route via `msys_safe_run`."*

## 6 · Record custody surfaced to MSTR

`MEMORY.md` declares a **17KB load cap** with *"content PAST IT SILENTLY DOES NOT LOAD"* and measured
**18,075 bytes at session start — 667 over.** I added the class as a merged family line at **net +63
bytes** (compressing two passages that restated one idea three times) and **deliberately did not cut
other lanes' entries** — deciding what leaves a shared law-adjacent index is custody, not verification.

⚠ **I nearly filed the stronger claim that an Andrew-direct standing order was not loading. It would
have been the same ungrounded-mechanism error I had just corrected in two other lanes**: the cap is a
claim the file makes *about itself*, and this session's context visibly included the tail line. The
honest finding is **"the file exceeds its own declared budget," not "content is provably not loading."**

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| argv echo-back via MSYS `echo.exe` | **PASS — the decisive instrument** | the only oracle that observes argument corruption; grep's rc cannot |
| own `ast` sweep, v1 + v2 | **PASS after self-correction** | 214 co-occurrence false positives -> 0 on a dataflow predicate; denominator + predicate + positive control printed |
| own mutants vs `msys_argv_guard` | **PASS + 3 findings** | injection canary (safe), rc=127 regression, predicate/matrix disagreement, 2.2x undisclosed |
| exercised `find`/`grep` both paths | PASS | 0->9 matches; System32-vs-GNU resolution; cwd-dependent glob expansion |
| `shutil.which` vs `subprocess` | **FAIL — instrument lies** | reports Git's binary while subprocess spawns System32's |

**Own errors this arc:** (1) a non-reproduction filed on an oracle that could not detect the fault, my
control mangled and matching by luck; (2) a v1 sweep predicate of file co-occurrence rather than
dataflow (caught pre-report); (3) generalized "whitespace -> safe" from a single cell and handed it to a
peer who put it in a landed docstring — it held, but the grounding was one datapoint wide when I gave
it. **Two of the three were caught by checking before filing. The one that wasn't cost a peer's correct
report an override — the same asymmetry as yesterday: a verifier's wrong number overrides rather than
merely adds.**
