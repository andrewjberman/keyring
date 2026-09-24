# AMGT_RESAPP task order -- `AMGT-rk-65` -- ONE accession-ranking rule, in ONE place, read by BOTH readers: `roster.py` ranks an EDGAR digit accession over a `doc-<16 hex>` document id over any placeholder by explicit rule (never by ASCII sort order), and `management_posture_batch.filed_status` imports that rule instead of bare-sorting -- closing a live wrong answer (the posture batch drops a filed name roster resolves)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-65</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~65</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one library module, one batch module and their tests; it
  arms no cron, alarm, monitor or cadence, reads no schedule and writes none.
comp-iam: DECLARED-NOT-APPLICABLE -- NO live AWS act: every criterion runs against an in-memory stub S3 client the
  tests build themselves; nothing reads or writes opal-data-harvest.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~65`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~65;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-65` (R16-C1; rows `AMGT_RESAPP-Z-S179` residual and `-W46-S2` item 2)

**The ruling, verbatim (`ledger/ROUND16_CTO_RULINGS_20260921.md` @dcd88f0acc s.1, `:25-27`):** *"C1, C2 ratified as
written. Disjoint write surfaces, no served output, offline-provable, zero collision with the held `wk-amgt-14-50`
branch. C1 covers both readers in one cell (roster.py + management_posture_batch.py), correctly avoiding the chain the
split would create."* The CTO's own spot-check (`:13-16`): *"`roster.py:831-838` `_is_accession_key` returns
`stem.isdigit()` -- a `doc-<sha16>` key and `UNRESOLVED-SOURCE` both fail it and fall to a bare `sorted(keys)[-1]`
(:869-870), which is genuinely case-fragile ... (`doc-` beats `UNRESOLVED-SOURCE` only because lowercase `d` > `U`;
a `Doc-` variant would not)."*

**The census this cell was cut from (`ledger/ROUND16_CANDIDATE_CENSUS_20260921.md` @a0d593560c, item C1 and s.5):**
two drafters measured two readers of ONE rule and found them disagreeing. Measured offline with a stub S3 client,
one name holding both `000000000000000001.source.json` (RESOLVED) and `UNRESOLVED-SOURCE.source.json`:
`roster.load_source_object -> 000000000000000001.source.json` / `posture batch filed_status -> UNRESOLVED-SOURCE` /
`posture batch filed_names -> []`. **The posture batch drops a filed name that roster resolves.**

**THE MEASURED STATE, at HEAD (cite these lines; RE-READ them at your branch HEAD before editing):**
- `lib/research/management/roster.py:831-838`, `_is_accession_key(key)`: strips `.source.json`, returns
  `stem.isdigit()`. Docstring: *"A real accession is digits-only; UNRESOLVED-SOURCE (or any other placeholder) is
  not, and must never win over a real one just because it sorts after every digit (AMGT-rk-46 item 7)."*
- `roster.py:841-872`, `load_source_object(security_key, source_path=None, client=None)`: lists `.source.json` keys
  under `filings/v1/<key>/` (`:863-866`), then `:869-870` `accession_keys = sorted(k for k in keys if
  _is_accession_key(k)); key = accession_keys[-1] if accession_keys else sorted(keys)[-1]`. Returns `(object,
  label)`; the label ends with the chosen key.
- **The `doc-` id's exact shape, read at its GENERATORS (not from a row):** `lib/research/filings/document.py:880`
  `"accession": "doc-%s" % document_sha256[:16]` and `lib/research/filings/battery.py:1050`
  `"document_id": "doc-%s" % winner["sha256"][:16]` -- `doc-` followed by the first 16 characters of a sha256
  hexdigest, i.e. 16 LOWERCASE hex characters. `roster.pool_source_key` (`:827-828`) turns the accession into the
  key name `filings/v1/<key>/<accession>.source.json`. (Test fixtures such as `doc-fixture` in
  `lib/research/filings/tests/test_translation.py` are NOT this shape and are not pool keys.)
- **So today a resolved non-EDGAR winner `doc-<16hex>.source.json` is NOT an accession by `_is_accession_key`, is
  grouped with the placeholder, and wins only because `'d'` (100) sorts after `'U'` (85).** A placeholder named with
  a letter after `d` (e.g. `unresolved-probe.source.json`) beats it.
- `integrations/bloomberg/research/management_posture_batch.py:96-107`, `filed_status(client, security_key)`: lists
  the same prefix and takes `key = sorted(keys)[-1]` (`:105`) -- no accession rule at all. Its docstring (`:97-98`)
  claims it reads *"the LATEST accession the same way roster.py's own load_source_object does"* -- FALSE at HEAD.
  `filed_names` (`:110-113`) keeps the names whose `filed_status == "RESOLVED"`. The module already puts the repo
  root on `sys.path` (`:38-41`) and imports `from lib.research.management import enrich` (`:43`), so importing
  `roster` from the same package is available.
- `lib/research/management/tests/test_management.py:856-878`, `AccessionPlaceholderTest`: TWO arms at this cut (a real
  accession beats the placeholder; the placeholder is picked only when alone), using `_StubS3` (`:283`).
- Baseline suite: `python -m pytest lib/research/management/tests -q` -> 73 passed (census, re-measure at spawn).

**RULED, what you build (one rule, one place, two readers):**
1. **`roster.py`** -- add ONE pure, importable function (name it `pick_source_key(keys)`; no I/O) that returns the
   winning key from a list of `.source.json` keys by EXPLICIT CLASS, then within the class the sorted-last key:
   class 2 = an EDGAR accession (stem all digits, today's `_is_accession_key` meaning -- KEEP that function and its
   meaning, callers may depend on it); class 1 = a document id matching `^doc-[0-9a-f]{16}$` exactly (the generator
   shape above -- a `Doc-` capital or a `doc-fixture` is NOT class 1); class 0 = anything else, placeholders included.
   **EDGAR before `doc-` is the ruled order** (it preserves today's result when both exist); the within-class
   sorted-last keeps today's "latest accession" semantics. `load_source_object` calls `pick_source_key` in place of
   `:869-870`; its signature and `(object, label)` return are UNCHANGED. Update its docstring to name the three
   classes.
2. **`management_posture_batch.py`** -- `filed_status` calls `roster.pick_source_key(keys)` (import the function;
   NEVER copy the rule) in place of `sorted(keys)[-1]`, and its docstring's parity claim becomes true. Nothing else in
   the module moves.
3. **Tests.** In `AccessionPlaceholderTest` add arms (keep the two existing ones byte-identical): (a) a
   `doc-1defdb68a7ffd3b7.source.json` beside `unresolved-probe.source.json` (a placeholder that sorts AFTER `d`) ->
   the `doc-` key wins (today the placeholder wins -- the discriminating arm); (b) a digit accession beside a `doc-`
   key -> the digit accession wins (the ruled EDGAR-before-doc- order); (c) a `Doc-1defdb68a7ffd3b7.source.json`
   (capital, not the generator shape) beside `UNRESOLVED-SOURCE.source.json` -> both class 0, sorted-last decides,
   and the test ASSERTS that documented outcome so the capital case is pinned, not left to accident; (d)
   `pick_source_key` directly over a mixed list of all three classes. New file
   `integrations/bloomberg/research/tests/test_management_posture_batch.py` with its own minimal stub S3 client (do
   not import a private test helper from another test module): (e) digit + `UNRESOLVED-SOURCE` for one name ->
   `filed_status` returns `"RESOLVED"` and `filed_names([name])` returns `[name]` (today `[]`); (f) `doc-<16hex>` +
   `unresolved-probe` -> `"RESOLVED"` read from the `doc-` object.

**What this cell does NOT change:** `_is_accession_key`'s meaning; `load_source_object`'s signature or return shape;
`lib/research/management/enrich.py`, `management.schema.json`, `domains.json`, `tests/test_lusha_domain.py` (the held
`wk-amgt-14-50` branch changes exactly those -- they are WALLS); `lib/research/filings/analyze.py:1410`
(`source_from_pool`, the same bare-sort pattern, measured to cause a fallback rather than a wrong answer -- NAMED, not
this cell's; if you judge otherwise, file a row, do not edit it). No pool object is read or written.

**THE VALIDATION BAR:** a pure-function and batch-reader fix with no security population, proven offline on stub
clients. No live call, no fleet run.

## 2. WHERE THIS CAME FROM

**ROUND 16**, decomposition s.24 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s round-16 rulings
`ledger/ROUND16_CTO_RULINGS_20260921.md` @dcd88f0acc s.1, answering the COO's census
`ledger/ROUND16_CANDIDATE_CENSUS_20260921.md` @a0d593560c (item C1 and s.5). Rows: `AMGT_RESAPP-Z-S177` / `Z-S179`
(the `doc-` residual carried), `AMGT_RESAPP-Z-W46-S2` item 2 (the shared-census unification "not owned by any open
cell"). Andrew-direct ~14:58Z (record @9bf58c4b95) and ~15:12Z (record @1e2a54bf0f) govern this round's width and
its one-slug issuance. PRD v0.13 @1699960261: no FWD or `C-` contract changes (a defect fix inside ratified
behaviour; no PRD addendum per the rulings).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/management/roster.py
lib/research/management/tests/test_management.py
integrations/bloomberg/research/management_posture_batch.py
integrations/bloomberg/research/tests/test_management_posture_batch.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~65/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-65.accession-ranking-rule-both-readers.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant (`document.py`, `battery.py`, `enrich.py`,
  `analyze.py`, `lib/research/management/batch.py` freely). Scratch is `<your worktree>/.scratch/` only.
- **NEVER read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`** -- it holds a leaked
  credential.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~65 <0.9.0_WK_AMGT_RESAPP~65@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.py`
  you commit passes `.tools/commit-gate.sh` inside safe-commit.

## 4. BOUNDS

**NO LIVE AWS ACT, NO DEPLOY, NO VENDOR CALL.** PORTAL FROZEN. **COLLECTION STAYS OFF.** **NO alarm, monitor,
SNS/SES-send, notification or freshness checker.** No non-ASCII in anything you write. **PUSH: never** (LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by copying the rule into
the batch module, and never by editing a WALL.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- the 73-test baseline and the two-arm class are
re-measured before you edit (a sibling round-16 cell touches no file here, but measure anyway).
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W65-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-65"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/management/tests -q 2>&1 | tail -5</invocation><expect>a final line "N passed" with 0 failed and N equal to the spawn-time baseline (73 at the cut, re-measured) plus the count of arms you added to AccessionPlaceholderTest (at least 4: arms a-d of section 1 item 3); the two pre-existing AccessionPlaceholderTest arms still pass unchanged</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-65"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest integrations/bloomberg/research/tests/test_management_posture_batch.py -v 2>&1 | tail -12</invocation><expect>every test PASSED, 0 failed, including arm e (a digit accession beside UNRESOLVED-SOURCE -> filed_status "RESOLVED" and filed_names returns the name, where HEAD returns []) and arm f (a doc-<16hex> beside unresolved-probe -> "RESOLVED" read from the doc- object)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-65"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import sys
sys.path.insert(0, '.')
from lib.research.management import roster
keys = ['p/X/unresolved-probe.source.json', 'p/X/doc-1defdb68a7ffd3b7.source.json', 'p/X/Doc-1defdb68a7ffd3b7.source.json', 'p/X/UNRESOLVED-SOURCE.source.json']
print('doc_vs_late_placeholder', roster.pick_source_key(keys).rsplit('/', 1)[-1])
print('digit_vs_doc', roster.pick_source_key(keys + ['p/X/000000000000000001.source.json']).rsplit('/', 1)[-1])
b = open('integrations/bloomberg/research/management_posture_batch.py', encoding='utf-8').read()
body = b.split('def filed_status', 1)[1].split('\ndef ', 1)[0]
print('batch_bare_sort_in_filed_status', body.count('sorted(keys)[-1]'), 'imports_pick_source_key', b.count('pick_source_key') >= 1)
"</invocation><expect>doc_vs_late_placeholder doc-1defdb68a7ffd3b7.source.json (the explicit class beats a placeholder that sorts after it -- at HEAD pick_source_key does not exist and load_source_object would pick unresolved-probe); digit_vs_doc 000000000000000001.source.json (EDGAR before doc-, the ruled order); batch_bare_sort_in_filed_status 0 and imports_pick_source_key True (one rule, imported, never copied)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-65"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import io, subprocess
for f in ('lib/research/management/roster.py', 'lib/research/management/tests/test_management.py', 'integrations/bloomberg/research/management_posture_batch.py', 'integrations/bloomberg/research/tests/test_management_posture_batch.py'):
    b = io.open(f, 'rb').read()
    compile(b.decode('utf-8'), f, 'exec')
    base = subprocess.run(['git', 'show', 'SITEZ:' + f], capture_output=True)
    hb = base.stdout if base.returncode == 0 else b''
    print(f, 'compiles True', 'crlf', b.count(b'\r\n'), 'non_ascii_bytes', len(b) - len(b.decode('utf-8')), 'at_SITEZ', (len(hb) - len(hb.decode('utf-8'))) if hb else 'NEW-FILE')
"</invocation><expect>all four print compiles True and crlf 0; each file's non_ascii_bytes equals its at_SITEZ figure (this cell adds no non-ASCII) and the new test file prints at_SITEZ NEW-FILE with non_ascii_bytes 0 -- the bar is the delta against SITEZ, never an assumed literal zero for a pre-existing file</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~65/AMGT_RESAPP.TO-AMGT-rk-65.accession-ranking-rule-both-readers.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, naming the suite's final count and the name you gave the
pick function.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>16</round>
<slot>~65</slot>
<fabric>site-z</fabric>
