# AMGT_RESAPP task order -- `AMGT-rk-68` -- the crosswalk vintage read admits only `crosswalk/v1/<YYYY-MM-DD>.json` keys and fails loudly on any other key under the prefix, newest-wins stays the policy, and the resolved key is recorded BESIDE the loaded document so a reader can see which vintage answered

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-68</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~68</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one library module and its test file; it arms no cron,
  alarm, monitor or cadence, reads no schedule and writes none; the standing no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order changes no role, policy, grant or resource and deploys nothing. Its
  ONE live act is a READ-ONLY `list_objects_v2` over `s3://opal-data-harvest/crosswalk/v1/` (AC6) under the
  permissions this box already holds; it writes no object.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~68`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~68;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-68` (R1-filter; row `AMGT_RESAPP-Z-W54-S2`; identity)

**The ruling, verbatim (`ledger/ROUND16_CTO_RULINGS_20260921.md` @dcd88f0acc s.2, `:42-48`):** *"R1 (`W54-S2`,
unpinned crosswalk vintage read). RULED, adopting the COO's own rec. Newest-wins stays the policy
(`management/batch.py` depends on it by design) -- this is not a fork worth Andrew's or CVO's time, it is this
seat's ordinary business-semantics call under Rule 27. Cut now, as a fourth cell: the key-shape filter
(`^crosswalk/v1/\d{4}-\d{2}-\d{2}\.json$`, loud on anything else) in `crosswalk.py`, baseline the 19 existing tests
green; the resolved key recorded on the returned document (so a reader can see which vintage answered it, closing
the same class of ambiguity C1 closes for accessions). `run_scores.py`'s copy stays untouched -- chain P, HELD, not
this cell's to touch. Issue: + R1-filter, a fourth disjoint cell."*

**The row this cell closes, `AMGT_RESAPP-Z-W54-S2`** (ARMED, owner `1.0.0_SA_CTO~Z`): `crosswalk.load_crosswalk()`
resolves the pool's `crosswalk/v1/` prefix by `sorted(keys)[-1]` with NO pinning and NO key-shape filter, so any
non-dated key under the prefix (a `latest.json`, a scratch copy) would sort after every dated vintage and silently
become the identity every reader resolves against.

**THE MEASURED STATE, at HEAD `daed5dc57b` (cite these lines; RE-MEASURE at spawn, do not re-derive from memory):**
- `lib/research/identity/crosswalk.py` (901 lines, pure ASCII, LF-only): `CROSSWALK_PREFIX = "crosswalk/v1/"` at
  `:68`. `load_crosswalk(path=None, refresh=False)` at `:689-703` -- docstring `:690-695` states the invariant *"The
  index is held BESIDE the document, never inside it: a loaded document stays byte-faithful to what it was read
  from."*; it caches `(document, index, ambiguous)` in `_CACHE` under `source or "<pool>"` (`:697-703`).
  `_read_pool_latest()` at `:706-723` builds its OWN `boto3` client (`:709`, not injectable), lists every key under
  the prefix (`:710-715`), raises `LookupError` on an empty listing (`:716-721`), and reads `sorted(keys)[-1]`
  (`:722`) with no shape filter. `write_pool(key, payload, bucket=..., client=None)` at `:802-850` is the pattern to
  mirror for an injectable client.
- **Callers of the unpinned path:** `load_crosswalk()` is the ONLY caller of `_read_pool_latest()` (`:700`; the two
  mentions in `lib/research/identity/add_security.py:36`, `:308` are comments). `load_crosswalk()` is called at
  `crosswalk.py:734` (`resolve`), `:783` (`aliases`), `:791` (`record_for`), `lib/research/identity/build_universe.py:681`
  and `lib/research/api/scoped_amgt.py:1729` -- every one UNPACKS A 3-TUPLE, so the return shape of `load_crosswalk()`
  MUST NOT change.
- **THE WRITER CENSUS (this seat's measurement at the cut, for the ISSUER RULE in s.2):** exactly TWO paths write a
  crosswalk vintage -- `crosswalk.main()` (`:868-881`: `build_crosswalk(args.as_of)` -> `serialise` -> `write_pool`)
  and `add_security._persist_registration_and_pool` (`add_security.py:152-160`: `crosswalk.build_crosswalk(as_of)` ->
  `serialise` -> `write_pool`). BOTH build the document FROM SCRATCH out of `registrations.json`; `build_crosswalk`'s
  own body (70 lines) calls neither `load_crosswalk` nor `_read_pool_latest` (measured). **No writer reads the loaded
  document, mutates it and writes it back.** Census instrument: `comp-find 'CROSSWALK_PREFIX|crosswalk/v1/'` over the
  whole corpus (296 hits, 8 HEAD / 2 DEF / 24 SURFACED; every SURFACED/DEF hit in first-party code read) plus every
  `load_crosswalk(` / `_read_pool_latest` / `put_object` site under `lib/research/identity/`.
- **Other unpinned `crosswalk/v1/` readers exist and are NOT this cell's -- WALLS, named so you do not drift into
  them:** `lib/research/scores/run_scores.py:81-92` (chain P, HELD, the ruling names it);
  `integrations/bloomberg/research/management_posture_batch.py:87` (`_latest_key`; that file is cell `AMGT-rk-65`'s
  write surface this same round -- a hard collision); `integrations/bloomberg/research/build_unit_map.py:460`;
  `integrations/bloomberg/research/model_block_pull.py:606`. If you think one of them needs the same filter, file a
  ROW and keep working.
- **Baselines measured at the cut:** `python -m pytest lib/research/identity/tests/test_crosswalk.py -q` -> `19
  passed`; `python -m pytest lib/research/identity/tests -q` -> `44 passed`; `python -m pytest lib/research/api/tests -q`
  -> `179 passed` (fully green after round 15's rk-63); `python -m pytest lib/research/api/tests/test_route_boundary_identity.py -q`
  -> `13 passed`. The test file is `unittest`-style (classes `CrosswalkRecords` `:104`, `CrosswalkFixedPoint` `:192`,
  `ResolveApi` `:206`) and has NO boto3 stubbing today.

**RULED, what you build:**

1. **`crosswalk.py`** -- add, next to `CROSSWALK_PREFIX`:
   `CROSSWALK_KEY_RE = re.compile(r"^crosswalk/v1/\d{4}-\d{2}-\d{2}\.json$")` and a named error
   `class CrosswalkKeyShapeError(LookupError)`. Change `_read_pool_latest()` to `_read_pool_latest(client=None)`
   (default: the same `boto3.client("s3", region_name="us-east-1")`, mirroring `write_pool`'s `client=None`) returning
   `(document, key)`. After listing: if ANY key under the prefix fails `CROSSWALK_KEY_RE`, raise
   `CrosswalkKeyShapeError` naming every offending key and the bucket -- LOUD, never a silent skip, never a warning;
   otherwise read `sorted(keys)[-1]` exactly as today (newest-wins STAYS). Keep the empty-listing `LookupError`
   message unchanged.
2. **The resolved key, recorded BESIDE the document** -- see the ISSUER RULE in s.2 for why beside, not inside. A
   module-level dict `_RESOLVED_FROM`, keyed by the SAME `cache_key` `load_crosswalk` uses, set on every uncached
   load to `"s3://<POOL_BUCKET>/<key>"` (pool) or `"file:<path>"` (a local copy); and a public accessor
   `loaded_from(path=None) -> str` that returns it for the same source `load_crosswalk(path)` would read (loading if
   not yet cached). `load_crosswalk()`'s signature and its 3-tuple return are UNCHANGED; the returned `document` dict
   is exactly what was read (no key added). Update `load_crosswalk`'s docstring with one sentence naming `loaded_from`.
3. **`tests/test_crosswalk.py`** -- a new `unittest` class `PoolVintageRead` (append-only; no existing test edited),
   with a stub S3 client (`get_paginator("list_objects_v2").paginate(**kw)` yielding one page of `Contents`, and
   `get_object(Bucket, Key)` returning `{"Body": <object with .read()>}`) and these arms at minimum:
   (a) keys `[crosswalk/v1/2026-09-15.json, crosswalk/v1/latest.json]` -> `_read_pool_latest(client=stub)` RAISES
   `CrosswalkKeyShapeError` whose message names `crosswalk/v1/latest.json` (at HEAD `:722` would have read
   `latest.json` -- `sorted(...)[-1]`);
   (b) keys `[crosswalk/v1/2026-09-14.json, crosswalk/v1/2026-09-15.json]` -> returns the 2026-09-15 document and the
   key `crosswalk/v1/2026-09-15.json` (newest-wins held), and the stub's `get_object` was called for that key only;
   (c) `load_crosswalk(refresh=True)` with `_read_pool_latest` patched (`unittest.mock.patch.object`) to return
   `(doc, "crosswalk/v1/2026-09-15.json")` and `AMGT_CROSSWALK_PATH` removed from the environment
   (`unittest.mock.patch.dict(os.environ, ...)`) -> `loaded_from()` returns
   `"s3://opal-data-harvest/crosswalk/v1/2026-09-15.json"`, and the returned document `== doc` exactly (deep
   equality; no key injected);
   (d) THE NON-PERSISTENCE GUARD: the document from (c), passed through `serialise(...)` and then `write_pool(key,
   payload, client=<a recording stub>)`, puts a body in which neither `loaded_from`'s value nor the substring
   `resolved` appears -- the recorded key can never ride a later vintage even if a future writer starts from a
   loaded document;
   (e) a local-path load (`load_crosswalk(path=<fixture>, refresh=True)`) -> `loaded_from(path=<fixture>)` returns
   `"file:<fixture>"`.
   Every new test restores `_CACHE` / `_RESOLVED_FROM` for the keys it touched (other test classes use a local path
   and must not see stale pool entries).

**What this cell does NOT change:** the newest-wins policy; `load_crosswalk()`'s signature or 3-tuple return;
`build_crosswalk`, `serialise`, `write_pool`, `resolve`, `aliases`, `record_for`; `add_security.py`,
`build_universe.py`; any of the four WALL readers above; `scoped_amgt.py` (read only).

**THE VALIDATION BAR (`C-VALIDATION-NAMES`, PRD v0.13 @1699960261 `:1652-1658`):** proven OFFLINE on the module's own
battery with a stub client, plus ONE read-only live listing (AC6) that proves the filter would NOT fire on today's
real pool population -- no write, no fleet run, no re-run of anything.

## 2. WHERE THIS CAME FROM

**ROUND 16**, decomposition s.24 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s round-16 rulings
`ledger/ROUND16_CTO_RULINGS_20260921.md` @dcd88f0acc s.2 R1 (`:42-48`), answering the COO's census
`ledger/ROUND16_CANDIDATE_CENSUS_20260921.md` @a0d593560c item R1; the row `AMGT_RESAPP-Z-W54-S2` (owner
`1.0.0_SA_CTO~Z`). PRD v0.13 @1699960261: `C-ONE-IDENTITY`; the crosswalk population `:1617`.

**ISSUER RULE -- THE RESOLVED KEY IS NEVER PERSISTED INTO A LATER VINTAGE (`2.0.0_SA_COO~Z`, at the cut):** the
recorded resolved key must never reach a crosswalk object any writer lands. **Measured at the cut: no writer
re-persists a loaded document** (both writers build from scratch -- s.1's writer census), so the risk is
prospective, not present; arm (d) stays as a GUARD so a future writer that starts from `load_crosswalk()` cannot
carry it. **Held BESIDE the document, not inside it**, for a second, independent reason: `load_crosswalk`'s own
stated invariant (`:693-694`) that a loaded document stays byte-faithful to what it was read from, and five callers
that read the document dict directly. The ruling's words "recorded on the returned document" are met by
`loaded_from()` -- the record travels WITH the load, answerable for the same source, without mutating the dict.
If a reader genuinely needs it IN the dict, that is a ROW to the issuer, never an edit made here.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/identity/crosswalk.py
lib/research/identity/tests/test_crosswalk.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~68/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-68.crosswalk-key-shape-filter.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `scoped_amgt.py`, `add_security.py`,
  `build_universe.py`, the four WALL readers, the rulings and the census freely); this block governs WRITES. Scratch
  is `<your worktree>/.scratch/` only.
- **Collision check, done at the cut:** none of these paths is written by `AMGT-rk-65` (`roster.py`,
  `test_management.py`, `management_posture_batch.py`, `tests/test_management_posture_batch.py`), `AMGT-rk-66`
  (`.tools/wk-provision.sh`), `AMGT-rk-67` (`.tools/comp-secrets`, `.tools/tests/test_comp_secrets.py`), or changed
  on the held branch `wk-amgt-14-50` (`lib/research/management/{domains.json,enrich.py,management.schema.json,tests/test_lusha_domain.py}`,
  names only). Zero overlap.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~68 <0.9.0_WK_AMGT_RESAPP~68@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.py`
  you commit passes `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39) inside safe-commit.

## 4. BOUNDS

**THIS CELL DEPLOYS NOTHING. BUT `crosswalk.py` IS IMPORTED BY THE PAGE ROUTE (`lib/research/api/scoped_amgt.py:115`,
`:1729`, `:1773`), SO THE NEXT `opal-amgt-scoped-api` REDEPLOY CARRIES THIS CHANGE TO THE SERVED PLANE -- WHOEVER CUTS
THAT REDEPLOY'S NEVER-WIDEN PAIR NAMES THIS CELL IN ITS BLAST RADIUS.** What the route serves from the crosswalk,
measured at the cut: ONE field derived from the loaded document -- `crosswalk_vintage` (`:1714`), which is
`document.get("as_of")` (`_crosswalk_vintage`, `:1725-1730`); the resolved KEY is not served by this cell (only
`loaded_from()` holds it). The failure mode after that redeploy is bounded: `resolve_identity`'s own
`try/except Exception` (`:1772-1777`) turns a `CrosswalkKeyShapeError` into `record = None` with `reason "crosswalk
not read: CrosswalkKeyShapeError: ..."` -- an unresolved identity with its reason, not a 500. AC6 proves today's
live population would not trigger it. **Pre-measured by the issuer at the cut, AC6's exact invocation, 2026-09-21
~15:3xZ:** `live_crosswalk_keys 2 matching 2 non_matching 0 [] newest crosswalk/v1/2026-09-19.json` -- the cell was
issued BECAUSE this read came back clean; your AC6 re-reads it at spawn (it may have moved).
**NO DEPLOY, NO VENDOR CALL, NO POOL WRITE.** PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm,
monitor, SNS/SES-send, notification or freshness checker.** No non-ASCII in anything you write. **PUSH: never.** Your
work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never change newest-wins, never
change `load_crosswalk()`'s return shape, never touch a WALL reader. **If AC6 finds ANY non-matching key in the live
prefix, STOP before committing the filter with a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`) naming the key: the
filter would break the page route's next redeploy, and whether to exempt that key is the issuer's call, not yours.**
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the four pytest baselines (19,
44, 179, 13) are re-measured at spawn BEFORE you edit; they may have moved if a sibling cell landed first.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W68-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-68"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/identity/tests/test_crosswalk.py -q 2>&1 | tail -5</invocation><expect>a final line "N passed" with 0 failed and N at least 24 (the 19 pre-existing tests, re-measured at spawn, plus the at least 5 new PoolVintageRead arms (a)-(e): the latest.json key RAISES CrosswalkKeyShapeError naming it; two dated keys resolve the 2026-09-15 vintage and read only that key; loaded_from() returns the s3:// key for a pool load while the returned document equals the stub's document exactly; the serialised-and-written body of a loaded document carries neither loaded_from's value nor the substring "resolved"; a local-path load reports "file:<path>")</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-68"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests/test_route_boundary_identity.py -q 2>&1 | tail -5</invocation><expect>"13 passed" (the count re-measured at spawn) with 0 failed -- the page route's identity boundary, which calls load_crosswalk() and unpacks its 3-tuple, is unchanged by this cell</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-68"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/identity/tests -q 2>&1 | tail -3 && python -m pytest lib/research/api/tests -q 2>&1 | tail -3</invocation><expect>the identity suite reads "M passed" with 0 failed, M equal to its spawn-time baseline (44 at the cut) plus exactly the number of new arms AC1 counted; the api suite reads the SAME "K passed" as its spawn-time baseline (179 at the cut) with 0 failed -- print both baselines beside both results; no test outside PoolVintageRead changed state</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-68"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import io, subprocess
for f in ('lib/research/identity/crosswalk.py', 'lib/research/identity/tests/test_crosswalk.py'):
    b = io.open(f, 'rb').read()
    base = subprocess.run(['git', 'merge-base', 'HEAD', 'SITEZ'], capture_output=True, text=True).stdout.strip()
    h = subprocess.run(['git', 'show', base + ':' + f], capture_output=True).stdout
    try:
        compile(b.decode('utf-8'), f, 'exec'); ok = True
    except SyntaxError as exc:
        ok = False; print(f, 'SYNTAX ERROR', exc)
    print(f, 'compiles', ok, 'non_ascii_bytes', len(b) - len(b.decode('utf-8')), 'crlf', b.count(b'\r\n'), '| parent non_ascii_bytes', len(h) - len(h.decode('utf-8')), 'parent crlf', h.count(b'\r\n'))
"</invocation><expect>both files print compiles True, crlf 0, and a non_ascii_bytes figure EQUAL to its base figure printed beside it (the "parent" columns read the worktree's merge-base with SITEZ, i.e. the pre-cell bytes, whatever number of commits you make; both 0 at the cut -- the two files are pure ASCII at HEAD daed5dc57b)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-68"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import sys
sys.path.insert(0, '.')
from lib.research.identity import crosswalk as cw
class _Body:
    def __init__(self, data): self.data = data
    def read(self): return self.data
class _Pages:
    def __init__(self, keys): self.keys = keys
    def paginate(self, **kw): return [{'Contents': [{'Key': k} for k in self.keys]}]
class _Stub:
    def __init__(self, keys): self.keys = keys; self.read_keys = []
    def get_paginator(self, name): return _Pages(self.keys)
    def get_object(self, Bucket, Key):
        self.read_keys.append(Key)
        return {'Body': _Body(('{\"as_of\": \"' + Key.rsplit('/', 1)[-1][:-5] + '\", \"records\": []}').encode('utf-8'))}
bad = _Stub(['crosswalk/v1/2026-09-15.json', 'crosswalk/v1/latest.json'])
try:
    cw._read_pool_latest(client=bad)
    print('bad_listing NOT RAISED')
except cw.CrosswalkKeyShapeError as exc:
    print('bad_listing RAISED CrosswalkKeyShapeError names_latest', 'crosswalk/v1/latest.json' in str(exc), 'objects_read', len(bad.read_keys))
good = _Stub(['crosswalk/v1/2026-09-14.json', 'crosswalk/v1/2026-09-15.json'])
doc, key = cw._read_pool_latest(client=good)
print('good_listing key', key, 'as_of', doc.get('as_of'), 'objects_read', good.read_keys)
print('is_lookuperror_subclass', issubclass(cw.CrosswalkKeyShapeError, LookupError))
"</invocation><expect>bad_listing RAISED CrosswalkKeyShapeError names_latest True objects_read 0 (the refusal happens at the listing, before any object is read); good_listing key crosswalk/v1/2026-09-15.json as_of 2026-09-15 objects_read ['crosswalk/v1/2026-09-15.json'] (newest-wins held, one read); is_lookuperror_subclass True -- a direct offline probe on a different instrument from AC1's pytest arms. At HEAD this probe cannot run (no client parameter, no named error) and :722 would have read crosswalk/v1/latest.json</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-68"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import re, boto3
rx = re.compile(r'^crosswalk/v1/\d{4}-\d{2}-\d{2}\.json$')
keys = []
for page in boto3.client('s3', region_name='us-east-1').get_paginator('list_objects_v2').paginate(Bucket='opal-data-harvest', Prefix='crosswalk/v1/'):
    keys.extend(o['Key'] for o in page.get('Contents', []))
bad = [k for k in keys if not rx.match(k)]
print('live_crosswalk_keys', len(keys), 'matching', len(keys) - len(bad), 'non_matching', len(bad), bad, 'newest', sorted(keys)[-1] if keys else None)
"</invocation><expect>live_crosswalk_keys N (N at least 1) with matching N and non_matching 0 [] -- the ONE read-only live act of this order: the filter, once the next redeploy carries it, would not fire on today's real pool population, and the newest key printed is the vintage the route resolves today. ANY non_matching key is the STOP in section 4 (a BLOCKING row, no commit of the filter), never an exemption you add. A paginated listing, never a bare list_objects_v2 page</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. Run AC6 FIRST (before any edit): its answer decides whether you build at all.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~68/AMGT_RESAPP.TO-AMGT-rk-68.crosswalk-key-shape-filter.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, naming the error class and accessor names you landed, AC6's
live key count and newest key, and the four suite counts before/after.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>16</round>
<slot>~68</slot>
<fabric>site-z</fabric>
