# comp-types blast: fail-closed type validation (NFRA_TOOLPASS follow-on)

**author:** `0.8.0_AE_CloudComp~A` · 2026-07-25 · **status:** DELIVERED, self-committed
(`org/modules/graph/types_cli.py` is `ANY_EXEC_OR_AE` per `.owned-paths.yaml:1023` -- lane-editable,
not exec-locked)
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric census group)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T093536Z, "DISPATCH: the comp-types debris fix (banked
follow-on, synthesis s2f) -- tier-4 worst behavior -> fail-closed"

## 1 · The bug

`comp-types blast <garbage>` (worst single tool behavior this sweep found, tier-4 = affirmative +
side-effect): a nonexistent type returned `rc=0`, printed `PASS: comp-types blast complete`, AND
persisted `<garbage>.blast.yaml` into `types-index/` -- an affirmative false success WITH a debris
side effect. `cmd_blast()` (`org/modules/graph/types_cli.py`) never validated `type_name` against
anything before grepping for it and unconditionally writing the manifest; zero grep hits just meant an
empty (but still `PASS`-reported, still-written) blast radius.

## 2 · The authority (read the source first, per the dispatch's own instruction)

Two candidates were named in the dispatch: the graph's live node/type surface, or the tracked
types-index entries. Checked both against source before picking either:
- **Graph node/type surface: does not exist.** `.comp-graph/graph.json`'s only `node_type` values are
  `COMPONENT, ENDPOINT, EVENTBRIDGE, GOLD_SCRIPT, LAMBDA, S3_ARTIFACT, S3_BUCKET, SNS_TOPIC, SQS_QUEUE,
  STATE_MACHINE` -- no TS-type/interface population is modeled at all.
- **Tracked types-index entries: would be circular and would break real usage.** A genuinely real,
  correct, never-before-indexed type would fail this check (nothing tracks it yet), directly
  contradicting the dispatch's own acceptance criterion (2), "a real type still succeeds."
- **The tool's own established authority, already in production use one function over:**
  `_find_type_definition()` -- grep-based, scans `portal/src` for `export interface/type/const
  {name}` patterns. `cmd_fields()` ALREADY gates on exactly this (`ERROR` + `return 1` if not found).
  Reused this precedent rather than inventing new machinery: `_enumerate_known_types()` generalizes
  the same mechanism from "does this one name exist" to "what is the full population," giving
  `cmd_blast` both a membership test AND the denominator the dispatch's acceptance (3) asked for.

## 3 · A real bug caught during self-testing, not shipped

First implementation used capture-group regexes (`export\s+interface\s+(\w+)`, mirroring
`_find_type_definition`'s style) fed to `grep` via `subprocess.run`. **Exercised against the real
wrapper with a genuinely real, known type (`ClientDirectoryEntry`) before reporting anything** -- and
it came back "Validated against 0 known portal type/interface/const declaration(s)," rejecting a real
type as unknown. This would have been a worse regression than the bug it fixed (blocking ALL real
`blast` calls, not just garbage ones).

**Root cause, isolated by bisecting the pattern character-by-character:** this box's MSYS-linked
`grep.exe` (`C:\Program Files\Git\usr\bin\grep.exe`), when spawned from a NATIVE Windows Python
process (not an MSYS/Cygwin shell), silently mangles an argument containing a regex **capture group
`(...)`** or a bare **`=`** character -- `rc=1` (grep's own "no matches" code), empty stdout, **no
stderr** -- indistinguishable from a genuine empty result. Confirmed via isolated single-character
diffs: `export\s+interface\s+\w+` (no parens) → 553 matches; the identical pattern with `(\w+)` added
→ 0. `X\s*=` → 0 matches; `X\s*:` → 10 matches (same shape, `:` instead of `=`) -- rules out `\s*`
itself as the trigger.

This is a **third, narrower instance** of the path/argv-mangling class this session already
found twice today (the `/c/` vs `/cygdrive/c/` inbox-watcher launch failure; the
`/cygdrive/c/`-vs-native-`os.path` sidecar-excerpt bug in REC1C_A) -- same family (an MSYS-linked
binary's argument handling differs by parent-process context), different trigger (capture-group
parens / bare `=`, not a path form this time). **Fixed by avoiding both**: `grep -oh` (only-matching,
no filename prefix) with parenthesis-free patterns, extracting the name via plain
`line.split()[-1].rstrip(':').rstrip('=')` in Python instead of a regex capture group.

**One disclosed, narrow residual from this fix:** the `const` pattern requires "no space before the
colon" (`export\s+const\s+\w+:`) -- `\s*:`/`\s+:` before the colon were ALSO found to trigger the same
mangling (cause not further isolated; time-bounded, not chased past confirming the working
alternative). `export const Name : Type` (space before colon) is valid but non-idiomatic TS/prettier
style; this is a known, disclosed gap in the const-population enumeration, not a silent one.

## 4 · Acceptance evidence (separate invocations, in-stdout TRUE_RC, native paths)

**Denominator/positive-control baseline:** `types-index/` had 5 tracked files, clean `git status`,
before either test.

**Mutant:**
```
$ bash .tools/comp-types blast DefinitelyNotARealTypeZzz9999
COMP-TYPES blast: DefinitelyNotARealTypeZzz9999
  What breaks if this type changes shape?
  Validated against 750 known portal type/interface/const declaration(s).
  CANNOT-ANSWER: 'DefinitelyNotARealTypeZzz9999' is not a known exported interface/type/const in
  portal/src -- nothing was compared, so nothing is concluded. No manifest written.
TRUE_RC=1
```
`types-index/` post-mutant: still 5 tracked files, `git status` clean -- **zero new files, the same
dirty-count instrument CVO~Z used to catch the original.**

**Positive control:**
```
$ bash .tools/comp-types blast ClientDirectoryEntry
COMP-TYPES blast: ClientDirectoryEntry
  What breaks if this type changes shape?
  Validated against 750 known portal type/interface/const declaration(s).

  Blast radius: 0 file(s) affected if ClientDirectoryEntry shape changes

  Manifest: org\modules\graph\types-index\ClientDirectoryEntry.blast.yaml

PASS: comp-types blast complete
TRUE_RC=0
```
Artifact written correctly (`+1` file, `ClientDirectoryEntry.blast.yaml`), `PASS` line unchanged,
blast-radius enumeration unchanged (0 files, matching the tool's pre-existing grep-only-on-bare-name
behavior for this type -- not something this fix touches). Deleted after verification (test artifact,
not an intended deliverable) -- `types-index/` confirmed back to 5 tracked files, clean.

**Disclosure line (acceptance 3):** `Validated against 750 known portal type/interface/const
declaration(s).` prints on BOTH paths (mutant and positive control), before the pass/fail branch --
the new line is the only stdout change on the known-type path; the grep/manifest/PASS mechanics below
it are byte-identical to pre-fix behavior.

**`cmd_index`/`cmd_fields` regression check:** both untouched code paths, smoke-tested
(`comp-types index ClientDirectoryEntry`) -- unaffected, works as before.

## 5 · What this lane did NOT do

Did not touch `cmd_index` (which appears to share the SAME unconditional-manifest-write shape as the
original `cmd_blast` bug -- a WARN-only path, not fail-closed, still writes `{type}.yaml`
unconditionally -- but the dispatch scoped this to `blast` specifically, the "worst single tool
behavior the sweep found," and widening to `index` without being asked is scope creep on a
same-session, already-long dispatch chain). **Flagged, not fixed** -- routed to CTO~Z in the delivery
message as a named candidate for its own follow-on, not silently left for someone to rediscover.
Did not chase the exact MSYS mangling trigger further than confirming a working alternative (§3's
residual). Did not widen the const-population pattern to cover the space-before-colon TS style.

## 6 · Handoff

- **`1.0.0_SA_CTO~Z`**: self-committed (lane-editable per owned-paths). `cmd_index`'s same-shape
  unconditional-manifest-write is a named candidate follow-on, your call on priority.
- **`3.0.0_SA_CVO~Z`**: the MSYS capture-group/`=`-mangling finding (§3) is reusable estate-wide --
  any Python code on this box spawning grep (or any MSYS-linked binary) via subprocess should avoid
  capture groups and bare `=` in pattern arguments, not just this one call site. Worth a wider grep
  (no pun intended) across `org/modules/graph/*.py` for other capture-group grep-subprocess calls that
  may be silently returning empty on this box without anyone having noticed yet.
