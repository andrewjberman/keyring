# AMGT_RESAPP task order -- `AMGT-rk-76` -- the crosswalk module mints ONE slash-safe security key form (`/` becomes `-SLASH-`, reversible, identity on every slash-free key), with a partition helper so an entity id reaches the naming builder only as a PARTITION, never as `object`; `BP/_LN_Equity` is the negative control; ADDITIVE ONLY -- no served `security_key` changes

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-76</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~76</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order adds functions to one library module and one new test file; it
  arms no cron, alarm, monitor or cadence, reads no schedule and writes none, and runs no producer.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; the one live AWS read (AC4, a GET of
  the served crosswalk object through crosswalk.load_crosswalk()) runs under the seat's existing credentials exactly as
  every prior crosswalk census did, and nothing is written to AWS by this order.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~76`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~76;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-76` (R19-B; contract `C-SLASH-SAFE-KEY`)

**The ruling, verbatim (`ledger/ROUND_ANALYSIS.round18.md` @ac58e01116, `1.0.0_SA_CTO~Z`), `:34-35`:** *"Independent
of the registry, cut now: `C-SLASH-SAFE-KEY`. It is pure code in the crosswalk module and a prerequisite of every
format writer."* **`:40`, the R19-B row:** *"`C-SLASH-SAFE-KEY`: mint ONE slash-safe security key in the crosswalk
module (no slash-safe function exists there today) and prove an entity id never reaches the builder's `object`
argument. `BP/_LN_Equity` is the standing negative control. | `lib/research/identity/crosswalk.py` + tests | **No**
served change until a format writer uses it. It must not change today's served `security_key` (a reader-visible
key); if it would, it STOPs and reports rather than migrate a key mid-round."* **`:42`:** *"Disjoint: R19-A is
management, R19-B is identity. There is no chain between them."*

**The contract, verbatim (PRD v0.15 `prd/AMGT_RESAPP_PRD.md:857-858`, ratified text, admitted -- CVO @a986a03423,
CRO @c894c62896):** *"C-SLASH-SAFE-KEY. One slash-safe security key is minted in the crosswalk module and used
everywhere downstream. An entity id sits in a partition, never in the builder's free-form `object` argument."*

**The design source (the adopted plan, `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/
PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md:141-145` @1a9f1c4469):** *"Measured: `security_key=BP/_LN_Equity` as
a partition is REFUSED by the builder (`partition must be ... no '/'`). That is the right result -- and it only
happens because the entity sits in the PARTITION. If it sat in the free-form `object` argument, the builder accepts
`/` there, and the 10-object phantom-`BP` defect would carry straight into the new grammar. Recommend: mint one
slash-safe form in `lib/research/identity/crosswalk.py` (e.g. `/` becomes `-SLASH-`), and never put an entity id in
`object`."*

**THE MEASURED STATE, at HEAD `ac58e01116` (SITEZ). RE-READ every line below at your branch HEAD before editing:**
- `lib/research/identity/crosswalk.py` -- 938 lines, non-ASCII byte delta 0, crlf 0, last changed @0164b134ac
  (`AMGT-rk-68`). 45 distinct top-level names (functions, classes, assignments). **No slash-safe helper exists:**
  `comp-find -i 'slash[_-]?safe|safe[_-]?key|-SLASH-|encode_key|key_safe' lib/ integrations/ infra/aws/lambda/` =
  12 hits over 5428 files, none a security-key encoder (a DynamoDB attribute-name mangle in a trade Lambda, a
  listing census in `management/batch.py:27`, vendored lexer tables).
- The root grammar admits a slash: `_ROOT_RE = ^[A-Z0-9./*-]{1,12}$` (`:103`), and a TRAILING `/` is Bloomberg's own
  root spelling (`'BP/ LN'`, `'NG/ LN'`, comment `:104-106`), preserved verbatim into `security_key`.
- **The served crosswalk** (`crosswalk.load_crosswalk()` with no env -> `loaded_from()` =
  `s3://opal-data-harvest/crosswalk/v1/2026-09-19.json`, VersionId `pwgdKMxY3pN3duv1KWzW47Xuo8TQzJ9W`, 202505 bytes,
  sha256 `6668326f...1c3cc7`): **96 records, 36 carry a `security_key`, 60 are UNRESOLVED (null), 36 distinct.
  Exactly 2 contain `/`: `BP/_LN_Equity`, `NG/_LN_Equity`.** 0 contain the text `SLASH`; 0 non-ASCII; the only other
  non-alphanumeric, non-underscore character is one `*` (`WALMEX*`).
- **The builder, measured** (`lib/opal_naming.py`; `key()` `:1537`, `address()` `:1558`, `_segment()` `:1522`):
  `key("amgt","harvest","bronze","exec_officers","security_key=BP/_LN_Equity")` -> REFUSED *"partition must be a
  non-empty ASCII string with no '/' and no outer space"*; the same with `security_key=BP-SLASH-_LN_Equity` -> OK;
  `security_key=WALMEX*_MM_Equity` -> OK. `address(..., object="BP/_LN_Equity/x.json")` -> ACCEPTED (the `object`
  check refuses only a LEADING `/`, `:1580-1582`) -- the exact hole the contract closes.
- **Every `address(` call in the estate** (AST walk over `git ls-files '*.py'`: 6551 files, 0 unparsable): **8
  calls.** The 2 production calls pass a CONSTANT file name as `object`: `lib/research/identity/build_universe.py:459`
  `object=object_name` (both callers pass `SEC_CACHE_OBJECT_NAME = "sec_ticker_cik_cache.json"`, `:453`, `:468`,
  `:527`) and `lib/research/peers/universe.py:101` `object=CACHE_NAME` (`= "candidate_universe.json"`, `:84`). The
  other 6 are in `lib/tests/test_opal_naming.py` (3) and two `org/missions/**/deliverables/` scripts (3). **0 pass an
  entity id as `object` today.**
- **Test baselines at the cut:** `lib/research/identity/tests` **49 passed** (`test_crosswalk.py` 24 of them); the
  `lib/research/api/tests` suite (the page route imports this module, `scoped_amgt.py:115`) **185 passed**; 0 failed
  in either.

**RULED, what you build (additive only -- no existing line of `crosswalk.py` changes behaviour):**
1. **In `crosswalk.py`, beside the other module constants:** `SLASH_SAFE_TOKEN = "-SLASH-"` and a named error
   `class SlashSafeKeyError(ValueError)`.
2. **`slash_safe_key(security_key) -> str`:** returns `security_key.replace("/", SLASH_SAFE_TOKEN)`. It RAISES
   `SlashSafeKeyError` naming the input for: a non-`str` or empty value; a non-ASCII value; a value with outer
   whitespace; a value that ALREADY contains `SLASH_SAFE_TOKEN` (the form would stop being reversible). It is the
   IDENTITY on every slash-free key -- `slash_safe_key("CAT_US_Equity") == "CAT_US_Equity"`.
3. **`security_key_from_slash_safe(safe_key) -> str`:** the exact inverse (`SLASH_SAFE_TOKEN` back to `/`); RAISES
   `SlashSafeKeyError` for a value containing `/` (it is not a slash-safe form) or failing the same shape checks.
4. **`security_key_partition(security_key) -> str`:** returns `"security_key=" + slash_safe_key(security_key)` --
   the ONE way a format writer puts an entity into a builder address, as a PARTITION. Its docstring states the
   contract sentence verbatim ("An entity id sits in a partition, never in the builder's free-form `object`
   argument") and cites `C-SLASH-SAFE-KEY`.
5. **Nothing calls these yet.** Do not wire them into `resolve()`, `_record_for()`, `build_crosswalk()`, any writer or
   any reader; do not add a field to the crosswalk document; do not touch `security_key` anywhere it is minted or
   served. The served key stays `BP/_LN_Equity`.
6. **Tests, a NEW file `lib/research/identity/tests/test_slash_safe_key.py`** (offline; `opal_naming.key()` reads
   only the committed registry). Arms, names must match AC1's list:
   - `test_slash_free_keys_are_unchanged` -- `CAT_US_Equity`, `6861_JP_Equity`, `WALMEX*_MM_Equity` map to
     themselves.
   - `test_slash_keys_are_encoded_and_round_trip` -- `BP/_LN_Equity` -> `BP-SLASH-_LN_Equity`, `NG/_LN_Equity` ->
     `NG-SLASH-_LN_Equity`; `security_key_from_slash_safe` returns each original.
   - `test_refusals_are_named` -- `SlashSafeKeyError` for `""`, `None`, a non-ASCII key, `" CAT_US_Equity"`, a key
     already containing `-SLASH-`, and (inverse) a value containing `/`.
   - `test_partition_is_admitted_by_the_builder` -- `opal_naming.key("amgt", "harvest", "bronze", "exec_officers",
     security_key_partition("BP/_LN_Equity"))` returns a key ending `security_key=BP-SLASH-_LN_Equity`.
   - `test_raw_slash_partition_is_refused_by_the_builder` -- THE NEGATIVE CONTROL: the same call with
     `"security_key=BP/_LN_Equity"` raises `ValueError` (proves the builder check the partition relies on is live).
   - `test_pinned_copy_has_no_slash_safe_key` -- THE DISCRIMINATING ARM. Load `crosswalk.py` from the PINNED commit
     `PRE_SLASH_SAFE_COMMIT = "ac58e01116c4c11beb54a6d98d30cb4652eae44b"` (a module constant in the test file) via
     `subprocess.run(["git", "show", PRE_SLASH_SAFE_COMMIT + ":lib/research/identity/crosswalk.py"])` into a temp
     file, import it under another name, and assert it has NO `slash_safe_key` attribute while the current module
     does. **PIN THE HASH. NEVER read the "before" copy from `HEAD` or a merge-base** -- that form reads the cell's OWN
     code once it merges and turns the suite red on the shared branch (row `AMGT_RESAPP-Z-S193`, round 18).

**What this cell does NOT change:** any existing function, class or constant in `crosswalk.py` (AC3 proves it by
AST); `lib/opal_naming.py` (a WALL); `scoped_amgt.py`, `enrich.py`, `ceo_search.py`, any writer or reader; the
crosswalk document or any S3 object. **No served change**, because nothing calls the new functions.

**THE STOP CLAUSE (the ruling's own):** if AC4 shows the new function would change ANY slash-free served
`security_key`, or two served keys would collide on one safe form, or a served key already contains `-SLASH-`, STOP:
file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`) with the offending keys and do not change the function to fit.

## 2. WHERE THIS CAME FROM

**ROUND 19**, decomposition s.27 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s round-18 analysis
`ledger/ROUND_ANALYSIS.round18.md` @ac58e01116 (s.2 `:34-42`), sent as msg 24011 (*"R19-B is C-SLASH-SAFE-KEY: mint
ONE slash-safe key in crosswalk.py (none exists today), with BP/_LN_Equity as the negative control. It must NOT change
today's served security_key. If it would, it STOPs and reports rather than migrate a key mid-round."*). Contract
`C-SLASH-SAFE-KEY`, PRD v0.15 s.11 (`:857-858`). Andrew-direct ~15:12Z (record @1e2a54bf0f) governs the one-slug
issuance. The memory lesson behind the control: a key containing a slash cannot be cut from an S3 path by splitting
on `/` -- `BP/_LN_Equity` became a phantom `BP` in a listing census, twice, with the count staying even.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/identity/crosswalk.py
lib/research/identity/tests/test_slash_safe_key.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~76/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-76.slash-safe-key.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant (`lib/opal_naming.py`, `scoped_amgt.py`,
  `test_crosswalk.py`, the analysis, the plan, the PRD). Scratch is `<your worktree>/.scratch/r76/` only (never
  committed).
- **Collision check, done at the cut:** round 19's other cell `AMGT-rk-75` (R19-A) writes
  `lib/research/management/enrich.py`, `lib/research/management/ceo_search.py` and their tests, and rewrites three
  `management/v1` objects. **Zero file overlap.** `enrich.py` imports this module (`:44`) and calls only
  `crosswalk.serialise` and `crosswalk.write_pool` (`:793-803`) -- neither changes here (AC3). The held branch
  `wk-amgt-14-50` changes only `lib/research/management/{domains.json,enrich.py,management.schema.json,
  tests/test_lusha_domain.py}` plus AMGT org files (names only). The only shared file is `INVESTIGATION_v1.md`
  (append-only; do not isolate it).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~76 <0.9.0_WK_AMGT_RESAPP~76@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.py`
  you commit passes `.tools/commit-gate.sh` inside safe-commit.

## 4. BOUNDS

**THIS CELL DEPLOYS NOTHING, WRITES NO S3 OBJECT AND NEEDS NO NEVER-WIDEN PAIR (it has no live act). BUT
`crosswalk.py` IS PACKAGED IN BOTH AMGT LAMBDAS -- `opal-amgt-scoped-api` (one of the 58 paths `AMGT-rk-74`'s AC3
swept; imported by the page route, `scoped_amgt.py:115`, `:1735`, `:1780-1790`, `:1853`) AND `amgt-resapp-chatter-axis`
(reached from `pool_reader.py`, `infra/aws/terraform/harvest/lambda_src/build_zip.py:16-17`) -- SO THE NEXT REDEPLOY
OF EITHER FUNCTION CARRIES THIS CHANGE AS A CARRY-ALONG, AND WHOEVER CUTS THAT REDEPLOY'S NEVER-WIDEN PAIR NAMES THIS
CELL'S COMMIT IN ITS CARRY-ALONG LIST.** The bound on that carry-along is what AC3 proves: every one of the 45
top-level names the served bytes use is unchanged, and the added names are called by nothing, so the redeployed
function's behaviour is unchanged.
**NO DEPLOY, NO VENDOR CALL, NO POOL WRITE, NO BLOOMBERG CALL.** PORTAL not your surface. **COLLECTION STAYS OFF.**
**NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No secrets are needed. No non-ASCII in anything
you write. **PUSH: never** (LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by editing
`lib/opal_naming.py`, never by changing an existing `crosswalk.py` symbol, and never by migrating a served key.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- re-measure the two suite baselines (49 / 185) before you
edit; the served crosswalk may have moved (AC4 re-reads it; its population figures are the cut's, and a moved
population is recorded, not a failure, so long as the STOP conditions in section 1 do not fire).
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W76-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row. A pure disarm sets
`DISMISSED_WITH_REASON` with a `dismissal_reason`, never `GRADUATED`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-76"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/identity/tests/test_slash_safe_key.py -v -p no:cacheprovider 2>&1 | tail -12</invocation><expect>a final line "6 passed" and 0 failed, the PASSED lines naming test_slash_free_keys_are_unchanged, test_slash_keys_are_encoded_and_round_trip, test_refusals_are_named, test_partition_is_admitted_by_the_builder, test_raw_slash_partition_is_refused_by_the_builder and test_pinned_copy_has_no_slash_safe_key -- the fifth the negative control on the builder, the sixth the discriminator against the PINNED pre-change commit ac58e01116</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-76"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/identity/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/api/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>two lines: first "55 passed" and 0 failed (the 49 identity tests at the cut plus this cell's 6), then "185 passed" and 0 failed (the api suite unchanged -- the page route imports this module); the bar is "identity baseline plus 6, api baseline unchanged, failures 0" against the baselines you re-measured at spawn</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-76"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import ast, subprocess
PIN = "ac58e01116c4c11beb54a6d98d30cb4652eae44b"
F = "lib/research/identity/crosswalk.py"
def tops(src):
    out = {}
    for n in ast.parse(src).body:
        names = []
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)): names = [n.name]
        elif isinstance(n, ast.Assign): names = [t.id for t in n.targets if isinstance(t, ast.Name)]
        elif isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name): names = [n.target.id]
        for x in names: out[x] = ast.dump(n)
    return out
old = tops(subprocess.run(["git", "show", PIN + ":" + F], capture_output=True).stdout.decode("utf-8"))
new = tops(open(F, "rb").read().decode("utf-8"))
same = [k for k in old if new.get(k) == old[k]]
added = sorted(k for k in new if k not in old)
print("pinned_top_level", len(old), "unchanged", len(same), "of", len(old), "removed", sorted(k for k in old if k not in new), "changed", sorted(k for k in old if k in new and new[k] != old[k]))
print("added_public", [k for k in added if not k.startswith("_")], "added_private", [k for k in added if k.startswith("_")])
'</invocation><expect>two lines: "pinned_top_level 45 unchanged 45 of 45 removed [] changed []", then "added_public ['SLASH_SAFE_TOKEN', 'SlashSafeKeyError', 'security_key_from_slash_safe', 'security_key_partition', 'slash_safe_key']" followed by added_private listing only underscore-prefixed helpers you wrote for these five (an empty list is fine) -- the change is ADDITIVE: every top-level name at the pinned pre-change commit is AST-identical, and exactly the five ruled PUBLIC names are new (measured so on a patched copy at the cut, with one private shape-check helper). Any removed or changed name, or any other public name, FAILS this criterion</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-76"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
from lib.research.identity import crosswalk as c
from lib import opal_naming as n
doc, _i, _a = c.load_crosswalk()
recs = doc["records"]
keys = sorted({r["security_key"] for r in recs if r.get("security_key")})
slash = [k for k in keys if "/" in k]
free = [k for k in keys if "/" not in k]
safe = {k: c.slash_safe_key(k) for k in keys}
changed_free = [k for k in free if safe[k] != k]
collide = len(keys) - len(set(safe.values()))
clash_existing = [k for k in slash if safe[k] in keys]
rt = sum(1 for k in keys if c.security_key_from_slash_safe(safe[k]) == k)
ok = 0
for k in keys:
    try:
        n.key("amgt", "harvest", "bronze", "exec_officers", c.security_key_partition(k)); ok += 1
    except ValueError as e:
        print("BUILDER REFUSED", k, e)
raw_refused = 0
for k in slash:
    try: n.key("amgt", "harvest", "bronze", "exec_officers", "security_key=" + k)
    except ValueError: raw_refused += 1
print("source", c.loaded_from(), "records", len(recs), "keyed", len(keys), "slash_keys", slash)
print("slash_free_unchanged", len(free) - len(changed_free), "of", len(free), "changed", changed_free, "| encoded", {k: safe[k] for k in slash})
print("distinct_safe", len(set(safe.values())), "of", len(keys), "collisions", collide, "clash_with_existing_key", clash_existing, "| round_trip", rt, "of", len(keys))
print("builder_accepts_partition", ok, "of", len(keys), "| raw_slash_partition_refused", raw_refused, "of", len(slash))
'</invocation><expect>four lines, measured at the cut on a copy carrying the ruled functions: "source s3://opal-data-harvest/crosswalk/v1/2026-09-19.json records 96 keyed 36 slash_keys ['BP/_LN_Equity', 'NG/_LN_Equity']"; "slash_free_unchanged 34 of 34 changed [] | encoded {'BP/_LN_Equity': 'BP-SLASH-_LN_Equity', 'NG/_LN_Equity': 'NG-SLASH-_LN_Equity'}"; "distinct_safe 36 of 36 collisions 0 clash_with_existing_key [] | round_trip 36 of 36"; "builder_accepts_partition 36 of 36 | raw_slash_partition_refused 2 of 2". THE STOP CLAUSE BINDS HERE: any slash-free key in changed, any collision or clash, or any BUILDER REFUSED line is a BLOCKING row and a STOP, never a function edit to fit. If the served object has moved since the cut, record the new source and counts; the pass condition is the four invariants (unchanged = all slash-free, 0 collisions, 0 clashes, round_trip = accepts = keyed, raw refused = slash count), not the cut's numbers</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-76"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import ast, subprocess
files = [f for f in subprocess.run(["git", "ls-files", "*.py"], capture_output=True, text=True).stdout.split("\n") if f]
calls, bad = [], 0
for f in files:
    try: tree = ast.parse(open(f, "rb").read().decode("utf-8"))
    except Exception: bad += 1; continue
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fn = node.func
            nm = fn.attr if isinstance(fn, ast.Attribute) else (fn.id if isinstance(fn, ast.Name) else None)
            if nm == "address":
                obj = [k for k in node.keywords if k.arg == "object"]
                val = ast.unparse(obj[0].value) if obj else ("POSITIONAL:" + ast.unparse(node.args[5]) if len(node.args) >= 6 else None)
                calls.append((f, node.lineno, val))
prod = [c for c in calls if c[0].split("/")[0] in ("lib", "integrations", "data", "infra") and "/tests/" not in c[0] and c[2] is not None]
print("py_files", len(files), "unparsed", bad, "address_calls", len(calls), "production_calls_with_object", len(prod))
for c in prod: print(" ", c)
print("new_module_address_calls", sum(1 for c in calls if c[0] == "lib/research/identity/crosswalk.py"))
'</invocation><expect>"unparsed 0", "address_calls 8" and "production_calls_with_object 2", listing exactly ('lib/research/identity/build_universe.py', 459, 'object_name') and ('lib/research/peers/universe.py', 101, 'CACHE_NAME') -- both constant file names ("sec_ticker_cik_cache.json" at build_universe.py:453, "candidate_universe.json" at peers/universe.py:84), so 0 production calls pass an entity id as object -- then "new_module_address_calls 0". py_files is the tracked count at your HEAD (6551 at the cut plus this cell's one new file); line numbers may shift only if those files moved since the cut -- record them</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-76"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import io, subprocess
PIN = "ac58e01116c4c11beb54a6d98d30cb4652eae44b"
for f in ("lib/research/identity/crosswalk.py", "lib/research/identity/tests/test_slash_safe_key.py"):
    b = io.open(f, "rb").read()
    base = subprocess.run(["git", "show", PIN + ":" + f], capture_output=True).stdout
    print(f, "compiles", bool(compile(b.decode("utf-8"), f, "exec")), "crlf", b.count(b"\r\n"), "non_ascii_bytes", len(b) - len(b.decode("utf-8")), "| base_bytes", len(base), "base_non_ascii", len(base) - len(base.decode("utf-8")))
'</invocation><expect>both files print compiles True, crlf 0 and non_ascii_bytes 0; crosswalk.py's base figures are base_bytes of its pinned copy (non-zero) and base_non_ascii 0; the test file is NEW, so its base_bytes is 0 (absent at the pin) and base_non_ascii 0</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~76/AMGT_RESAPP.TO-AMGT-rk-76.slash-safe-key.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, naming the two suite counts before and after, the AC3
added-names list, the AC4 slash-key population and encodings, and the AC5 call census.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/r76/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>19</round>
<slot>~76</slot>
<fabric>site-z</fabric>
