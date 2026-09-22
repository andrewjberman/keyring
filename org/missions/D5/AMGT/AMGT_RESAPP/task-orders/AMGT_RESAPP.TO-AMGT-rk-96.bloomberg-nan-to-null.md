# AMGT_RESAPP task order -- `AMGT-rk-96` -- Bloomberg bronze maps every non-finite float (NaN, +Inf, -Inf) to JSON `null` BEFORE its one deterministic serialisation, and every harvest JSON writer that stores a document refuses a non-finite float (`allow_nan=False`) instead of emitting the bare token `NaN`; CODE ONLY, ahead of B1

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-96</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~96</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits two library modules and two test files; it arms no cron,
  alarm, monitor or cadence, reads no schedule and writes none, and runs no producer (B1 is a later cell).
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; the one live AWS act (AC3, GET of the
  110 bloomberg bronze, 122 model_block and 194 filings source objects in opal-data-harvest) is READ-ONLY under the
  seat's existing credentials, exactly as every prior harvest census; nothing is written to AWS by this order.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~96`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~96;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-96` (round 24, ahead of B1; the CVO's v0.18 exposure)

**The ruling of record, verbatim** (1.0.0_SA_CTO~Z msg 24165, 2026-09-22T07:53:15Z, file
`org/mcp/inbox/2.0.0_SA_COO/~Z/read/20260922T075315Z_1.0.0_SA_CTO_Z_v0.18_ADMITTED__both_halves__--_LIMB_6_c.md`,
lines 8-12):

> The CVO flagged one EXPOSURE, measured never fired (0 of 110 bronze objects carry NaN or Inf; 0 of 110 fail a strict
> parse): lib/research/harvest/bloomberg.py:47 calls json.dumps with allow_nan at its default True, so a NaN would be
> written as the bare token NaN and a strict reader would reject the object.
> RULED: this is not chain-G debt. B1 is the first run that will write NEW Bloomberg bronze at scale, and Terminal fields
> do return NaN. So round 24 carries, AHEAD of B1:
> - allow_nan=False;
> - a test arm showing that a NaN value raises and nothing is written;
> - the order's rule for a NaN field: map it to null BEFORE serialisation, or refuse the object. Pick one and state it.
> My REC is null, because a missing Bloomberg value is a null, not an error.

**ISSUER RULING (L5), the NaN rule: MAP TO NULL.** For Bloomberg BRONZE, every float that is not finite (NaN, +Inf,
-Inf), at any depth inside dicts and lists, becomes JSON `null` BEFORE serialisation -- a missing Bloomberg value is a
null, not an error. `allow_nan=False` then stands as a BACKSTOP: if any non-finite float ever slips past the mapping,
the serialiser RAISES and nothing reaches the store. State this rule in `client_json`'s docstring.

**THE MEASURED STATE, measured at `049b19e565` and re-pinned to `1229b10b83` (SITEZ; `lib/research/harvest` and `integrations/bloomberg/research` are byte-identical between the two, 0 files changed). RE-READ every line at your branch HEAD before editing:**

- `lib/research/harvest/bloomberg.py` (424 lines). `:45-47` `_canonical_json(obj)` =
  `json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)` -- `allow_nan` at its default True.
  `:50-56` `client_json(obj)` returns `_canonical_json(obj).encode("utf-8")` -- the bronze serialiser.
  `_canonical_json` has THREE more callers, all for model_block SILVER (a LOSSLESS copy): `:198` `doc_json`,
  `:224` `basis_json`, `:225` `figure_json`.
- `client_json` production callers (unchanged by this order; they inherit the rule): `integrations/bloomberg/research/
  model_block_pull.py:487-489` (refdata, histdata, bestdata) and `integrations/bloomberg/research/pull_baba_daily_px.py:87`,
  both importing `from lib.research.harvest import bloomberg as hbloom` (`:71` and `:31`).
- **THE SERIALISATION-SITE CENSUS, by subtraction.** Every `json.dumps` / `json.dump` call in
  `lib/research/harvest/*.py` (non-test): **7 sites**.
  - `bloomberg.py:47` -- stores a document (bronze via client_json; silver via doc/basis/figure json). **EXPOSED.**
  - `filings.py:183` -- `row["object_json"]`, the lossless `filing_source` silver copy of a `.source.json` document.
    **EXPOSED, same one-line class, inside AMGT's harvest lane -> INCLUDED.**
  - minus `filings.py:182` -- `object_keys`, a sorted list of key STRINGS: no float can occur. Not exposed.
  - minus `bright_data_serp.py:52` -- `query_sha256` hashes a dict of STRINGS (q, engine, gl, hl). Not exposed.
  - minus `store.py:290` -- `record_hash`, a sha256 INPUT, never stored or parsed as JSON (and `default=str`).
    A NaN there only changes a hash deterministically. Not the stored-document class; not changed.
  - minus `bloomberg.py:395` and `filings.py:470` -- `json.dump` of a local `--report` file in scratch, never in the
    bucket. Out of scope.
  => 2 sites change: `bloomberg.py:47` and `filings.py:183`. `lusha.py` has none.
- **Live population, measured read-only at HEAD:** `bloomberg/harvest/bronze/` **110** objects, **0** carry a
  non-finite float; `derived/model_block/*.json` **122**, **0** non-finite; `filings/v1/*.source.json` **194**, **0**
  non-finite. So neither silver refusal can fire on today's data.
- **Byte parity, measured:** re-serialising each of the 110 parsed bronze objects with the NEW `client_json` gives bytes
  **identical to the OLD `client_json` in 110 of 110**. (The STORED bronze bytes are M1's verbatim copies of the old
  raw files, pretty-printed, so they are NOT `client_json` output -- 0 of 110 equal it; the parity that matters is old
  formula vs new formula on the same parsed object.)
- **Tests at the cut:** `lib/research/harvest/tests` **58 passed**; `test_bloomberg.py` **9 passed**; `test_filings.py`
  **8 passed**. `integrations/bloomberg/research/tests` has **2 collection errors** pre-existing -- not a pass bar here.
  Whole-repo census of tests pinning NaN / `allow_nan` behaviour under `lib/` and `integrations/`: **0 files**.

**RULED, what you build:**

1. `bloomberg.py`: add a private `_nan_to_null(obj)` -- recursive over `dict` (values) and `list`/`tuple` (items; a
   tuple comes back a list, as `json.dumps` already renders it); a `float` that is not `math.isfinite` becomes `None`;
   every other value returns unchanged (ints, bools, strings, None untouched). `_canonical_json` gains
   `allow_nan=False` (the one line the CVO named). `client_json(obj)` returns
   `_canonical_json(_nan_to_null(obj)).encode("utf-8")`. The silver callers (`:198`, `:224`, `:225`) keep calling
   `_canonical_json` WITHOUT the mapping, so a non-finite float in a model_block silver copy RAISES instead of being
   silently changed (a lossless copy may not alter a value). The docstring of `client_json` states the rule.
2. `filings.py:183`: `object_json` gains `allow_nan=False` (refuse, same lossless reasoning). No mapping there.
3. Tests, in the two existing test files (new arm names must match AC1):
   - `test_bloomberg.py`:
     - `test_client_json_maps_nan_to_null` -- `{"a": nan}` serialises to `{"a":null}`.
     - `test_client_json_maps_infinities_to_null` -- `+inf` and `-inf` both become `null`.
     - `test_client_json_maps_nested_non_finite` -- NaN inside a list inside a dict inside a list becomes `null`;
       sibling finite floats and ints are byte-unchanged.
     - `test_backstop_raises_and_nothing_is_written` -- with `_nan_to_null` monkeypatched to identity, `client_json`
       on a NaN raises `ValueError`, and the stub store records 0 puts (the chain `bronze_write(client_json(...))`
       never reaches the store).
     - `test_patched_client_json_is_the_one_production_reaches` -- the W85-S1 identity arm: import
       `lib.research.harvest.bloomberg` by its QUALIFIED name and assert the module-level `client_json` `is` the one
       `integrations.bloomberg.research.model_block_pull`'s `hbloom` reaches (`hbloom.client_json is hb.client_json`),
       loading `model_block_pull` only if its import succeeds offline; if it cannot import offline, assert identity
       against `lib.research.harvest.bloomberg` imported a second time by qualified name and record why.
   - `test_filings.py`:
     - `test_filing_source_row_refuses_non_finite` -- an object carrying a NaN raises `ValueError` from
       `filing_source_row` and returns no row.

**What this cell does NOT change:** `store.py` (a WALL), `bright_data_serp.py`, `lusha.py`, the two `client_json`
callers in `integrations/`, the S3 objects, the bronze contract's other properties (sorted keys, fixed separators,
UTF-8, `received-form: bbg-client-json`). No live Bloomberg call. No S3 write.

## 2. WHERE THIS CAME FROM

**ROUND 24**, decomposition s.32 (cut by `2.0.0_SA_COO~Z`), on the CTO's msg 24165 (PRD v0.18 @`788846596a` ADMITTED;
the CVO's review @`22b0d497c2`). Ahead of the backfill run B1, which is the first run that writes new Bloomberg bronze
at scale. Andrew-direct ~15:12Z governs one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/harvest/bloomberg.py
lib/research/harvest/filings.py
lib/research/harvest/tests/test_bloomberg.py
lib/research/harvest/tests/test_filings.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~96/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-96.bloomberg-nan-to-null.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant. Scratch is `<your worktree>/.scratch/r96/`
  only (never committed). The only shared file is `INVESTIGATION_v1.md` (append-only; do not isolate it).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~96 <0.9.0_WK_AMGT_RESAPP~96@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**CODE ONLY.** No live Bloomberg call, no vendor call, no S3 write, no deploy. The one AWS act is AC3's READ-ONLY
census. **Imports in tests use the QUALIFIED `lib.<pkg>.<mod>` names** (W85-S1). **Run each test directory in its OWN
pytest call** (a multi-directory call trips the W85-S1 module-identity clash). **A script that carries a backslash is a
FILE you write from this order's text verbatim**, never an inline `python -c` (W84-S1); `ac0.py` carries backslashes
(its regex), which is why every script here is a file. **The discriminating comparison is pinned to commit `1229b10b83`** (Z-S193), never
HEAD or a merge-base.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name, and never by editing a WALL.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- re-measure 58 / 9 / 8 before you edit.
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W96-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row; a worker names the issuer
(`2.0.0_SA_COO~Z`) as `disarm_owner`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 300)

**Script files.** Write each block below to the named file under `<your worktree>/.scratch/r96/`, byte-for-byte, then
run it from the worktree root as the criterion states.

`.scratch/r96/ac0.py`:
```
import re, subprocess
src = open("lib/research/harvest/bloomberg.py", "rb").read().decode("utf-8")
lines = src.splitlines()
print("bloomberg_line47", lines[46].strip())
sites = []
for f in ("bloomberg.py", "bright_data_serp.py", "filings.py", "lusha.py", "store.py"):
    for i, l in enumerate(open("lib/research/harvest/" + f, "rb").read().decode("utf-8").splitlines(), 1):
        if re.search(r"json\.dumps?\(", l):
            sites.append("%s:%d" % (f, i))
print("serialisation_sites", len(sites), sites)
pin = subprocess.run(["git", "cat-file", "-t", "1229b10b83"], capture_output=True, text=True).stdout.strip()
print("pin_object", pin)
```

`.scratch/r96/ac3.py`:
```
import boto3, importlib.util, json, math, subprocess, sys, tempfile, os
sys.path.insert(0, ".")
import lib.research.harvest.bloomberg as new
src = subprocess.run(["git", "show", "1229b10b83:lib/research/harvest/bloomberg.py"], capture_output=True).stdout
tmp = os.path.join(tempfile.mkdtemp(), "bloomberg_pin.py")
open(tmp, "wb").write(src)
spec = importlib.util.spec_from_file_location("bloomberg_pin", tmp)
old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
def nonfinite(o):
    if isinstance(o, float): return not math.isfinite(o)
    if isinstance(o, dict): return any(nonfinite(v) for v in o.values())
    if isinstance(o, list): return any(nonfinite(v) for v in o)
    return False
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
def keys(p):
    return [o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", [])]
bk = keys("bloomberg/harvest/bronze/")
same = nf = 0
for k in bk:
    o = json.loads(s3.get_object(Bucket=B, Key=k)["Body"].read())
    nf += nonfinite(o)
    same += old.client_json(o) == new.client_json(o)
print("bronze_objects", len(bk), "old_equals_new", same, "nonfinite", nf)
mb = [k for k in keys("derived/model_block/") if k.endswith(".json")]
print("model_block_json", len(mb), "nonfinite", sum(nonfinite(json.loads(s3.get_object(Bucket=B, Key=k)["Body"].read())) for k in mb))
fs = [k for k in keys("filings/v1/") if k.endswith(".source.json")]
print("filings_source_json", len(fs), "nonfinite", sum(nonfinite(json.loads(s3.get_object(Bucket=B, Key=k)["Body"].read())) for k in fs))
probe = {"px": float("nan"), "hi": float("inf"), "v": [1.5, float("-inf")]}
print("old_on_probe", old.client_json(probe))
print("new_on_probe", new.client_json(probe))
```

`.scratch/r96/ac4.py`:
```
import subprocess
out = subprocess.run(["git", "diff", "--name-only", "1229b10b83", "HEAD", "--", "lib", "integrations", "infra", ".tools"], capture_output=True, text=True).stdout.split()
print("changed_code_files", sorted(out))
callers = subprocess.run(["git", "grep", "-n", "client_json(", "--", "integrations"], capture_output=True, text=True).stdout.splitlines()
print("integrations_client_json_calls", len(callers))
```

`.scratch/r96/ac5.py`:
```
for f in ("lib/research/harvest/bloomberg.py", "lib/research/harvest/filings.py", "lib/research/harvest/tests/test_bloomberg.py", "lib/research/harvest/tests/test_filings.py"):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_bytes", len(b) - len(b.decode("utf-8").encode("ascii", "ignore")))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-96"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r96/ac0.py</invocation><expect>BEFORE any edit: "bloomberg_line47" prints the json.dumps line of _canonical_json with NO allow_nan argument; "serialisation_sites 7" listing bloomberg.py:47, bloomberg.py:395, bright_data_serp.py:52, filings.py:182, filings.py:183, filings.py:470, store.py:290 (line numbers as measured at 1229b10b83 -- a drifted number is recorded, not a fail, if the SITE is the same); "pin_object commit". Record the output; this is the baseline the other criteria compare against</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-96"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_bloomberg.py -v -p no:cacheprovider 2>&1 | tail -18</invocation><expect>a final line "14 passed" and 0 failed (the 9 at the cut plus 5), the PASSED lines naming test_client_json_maps_nan_to_null, test_client_json_maps_infinities_to_null, test_client_json_maps_nested_non_finite, test_backstop_raises_and_nothing_is_written and test_patched_client_json_is_the_one_production_reaches -- the fourth proving allow_nan=False raises and 0 puts reach the store when the mapping is removed</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-96"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/harvest/tests/test_filings.py -v -p no:cacheprovider 2>&1 | tail -3</invocation><expect>first "64 passed" and 0 failed (58 at the cut plus this cell's 6: five in test_bloomberg.py, one in test_filings.py); then the test_filings.py run ends "9 passed" (8 plus 1) with test_filing_source_row_refuses_non_finite PASSED. The bar is "baseline plus 6, failures 0" against the baselines re-measured at spawn</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-96"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r96/ac3.py</invocation><expect>READ-ONLY. "bronze_objects 110 old_equals_new 110 nonfinite 0" -- the new client_json is byte-identical to the PINNED old one on every live bronze object (the deterministic contract is unchanged for NaN-free data); "model_block_json 122 nonfinite 0"; "filings_source_json 194 nonfinite 0" (so neither silver refusal fires on today's data); then the discriminating probe: "old_on_probe" contains the bare tokens NaN and Infinity, "new_on_probe" is b'{"hi":null,"px":null,"v":[1.5,null]}'. If any live count differs from the measured cut, record it with its denominator and file a row -- a changed population is not a failure of this cell</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-96"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r96/ac4.py</invocation><expect>"changed_code_files" lists EXACTLY lib/research/harvest/bloomberg.py, lib/research/harvest/filings.py, lib/research/harvest/tests/test_bloomberg.py and lib/research/harvest/tests/test_filings.py -- no other code file; "integrations_client_json_calls 5" (measured at 1229b10b83: model_block_pull.py:436 is a DOCSTRING mention, :487, :488, :489 are calls, pull_baba_daily_px.py:87 is a call -- 4 calls plus 1 mention) -- the callers are unchanged and inherit the rule</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-96"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r96/ac5.py</invocation><expect>all four files print "compiles True crlf 0 non_ascii_bytes 0"</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~96/AMGT_RESAPP.TO-AMGT-rk-96.bloomberg-nan-to-null.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict); flip the order's
status (on the record face) to `complete` only if every criterion PASSES; commit with `--only -- <paths>`. Report once,
naming the suite counts before and after, AC3's parity and probe lines, and AC4's file list.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/r96/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>24</round>
<slot>~96</slot>
<fabric>site-z</fabric>
