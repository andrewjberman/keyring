# AMGT_RESAPP task order -- `AMGT-rk-70` -- `model_block_pull._latest_stamp` returns only a stamp that actually carries BOTH `refdata.json` and `histdata.json` (the rule `build_unit_map` already applies), and raises a NAMED, catchable error naming the prefix and the rejected-stamp count when none qualifies -- never a bare NoSuchKey crash in `stage_derive`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-70</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~70</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one box-side producer module and its tests; it arms no
  cron, alarm, monitor or cadence, reads no schedule and writes none.
comp-iam: DECLARED-NOT-APPLICABLE -- NO live AWS act: every criterion runs against an in-memory stub S3 client the
  test builds itself; no role, policy or grant is read or changed, and opal-data-harvest is never touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~70`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~70;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-70` (R17 W38-S5-guard; row `AMGT_RESAPP-Z-W38-S5`; EXPOSURE)

**The ruling, verbatim (msg 23943, `1.0.0_SA_CTO~Z`, 2026-09-21T15:57:53Z):** *"You're right, that was an oversight
on my end, not a ruling -- I should have said so explicitly in msg 23935 rather than leaving it ambiguous. Verified
independently before ruling: model_block_pull.py:344-352 _latest_stamp is a bare sorted(stamps)[-1] with no content
check, and its one caller (:904-906) reads refdata.json/histdata.json from that stamp immediately -- confirms the
exposure. RULED: W38-S5 rides round 17 alongside S176-anchor. Disjoint write surface (model_block_pull.py + tests vs
surprise-row-gate.py + test), independent of all three held words, no chain. ... round 17 is two cells now, not one
-- S176-anchor and W38-S5-guard (require refdata+histdata on the resolved stamp, same rule build_unit_map already
applies; raise a named error rather than a bare NoSuchKey crash if none qualifies). One wave, no chain. Cut both
together."*

**The analysis section, verbatim (`ledger/ROUND_ANALYSIS.round16.md` @1764686f10 s.3, `:88-92`):** *"`W38-S5-guard`
-- `_latest_stamp` requires the resolved stamp to carry both `refdata.json` and `histdata.json` (the same rule
`build_unit_map` already applies elsewhere), raising a named, catchable error instead of letting `_read_json_from_s3`
fail on a generic NoSuchKey when it does not; proof: a stub with a non-raw newest stamp beside a raw one resolves to
the raw stamp (or raises the new named error if none qualifies, never a bare crash), plus the existing test suite
green."* (`:77-80`: *"A non-raw newest stamp (two writers can produce one) crashes `stage_derive` on the first
fallback roster run after a pull -- a real, currently-unfired EXPOSURE."*)

**The row this cell closes, `AMGT_RESAPP-Z-W38-S5`** (`INVESTIGATION_v1.md:9828-9849`, OBSERVATION, INERT, filed
2026-09-19T06:30Z by `0.9.0_WK_AMGT_RESAPP~38`), `one_line` verbatim: *"raw/bloomberg/<key>/<stamp>/ can carry a stamp
folder holding ONLY an identity.json (no refdata.json/histdata.json) for a key whose Bloomberg raw has never landed --
measured on all three validation names -- so a stamp folder existing is not evidence raw landed, and
model_block_pull.py's own _latest_stamp (used unmodified by its stage_derive) would crash NoSuchKey rather than report
absence if pointed at one of these keys."* (Line numbers inside the row cite an older file version; use the HEAD
citations below.)

**THE MEASURED STATE, at HEAD `1764686f10` (cite these lines; RE-READ them at your branch HEAD before editing):**
- `integrations/bloomberg/research/model_block_pull.py` (1121 lines, non-ASCII byte delta 0, crlf 0 at the cut):
  `_latest_stamp(s3, prefix)` at `:344-352` -- `s3.list_objects_v2(Bucket=BUCKET, Prefix=prefix, Delimiter="/")`,
  stamps from `CommonPrefixes`, `raise RuntimeError(f"no stamp found under s3://{BUCKET}/{prefix}")` if none, else
  `return sorted(stamps)[-1]` -- NO content check. `_read_json_from_s3` at `:339-341` (a bare `get_object`).
- **Callers of `_latest_stamp`, measured (Grep over the whole repo, `*.py`): exactly ONE -- `stage_derive` at
  `:903-904` (`if raw_stamp is None: raw_stamp = _latest_stamp(s3, f"raw/{VENDOR}/{sec_key}/")`), which then reads
  `refdata.json` and `histdata.json` from that stamp at `:905-906`.** `stage_derive` itself is reached with
  `raw_stamp=None` (the fallback) from `main()`'s derive loop at `:1095` (`r = stage_derive(s3, sec, raw_stamp=None)`).
- **The consumer path does NOT hit the fallback:** `integrations/bloomberg/research/pull_consumer.py:99` calls
  `mbp.stage_derive(s3, ticker, raw_stamp=pull_result["raw_stamp"])` -- the stamp the pull just landed, never `None`
  (cell `AMGT-rk-64` fixed that file's call site this morning; it is NOT this cell's surface).
- **The rule to reuse, `integrations/bloomberg/research/build_unit_map.py:232-248`, `_stamps_with_refdata(s3, prefix)`:**
  lists stamps with `Delimiter="/"`, sorts NEWEST FIRST (`:241`), and for each stamp lists
  `f"{prefix}{st}/"` and keeps it only if `"refdata.json" in names and "histdata.json" in names` (`:246`); returns the
  qualifying stamps newest first. Its docstring (`:233-239`) records the same measured hazard.
- **IMPORT DIRECTION, measured -- why this cell MIRRORS the rule rather than importing it:** `build_unit_map.py:46` does
  `import model_block_pull as _mbp`, so `model_block_pull` importing `build_unit_map` would be a CIRCULAR import. The
  shared rule therefore belongs in the LOWER module, `model_block_pull.py`. `build_unit_map.py` is NOT in this cell's
  `<paths>` (a WALL): it keeps its own copy this round. If you judge it should import the new helper, FILE A ROW
  (disarm_owner `2.0.0_SA_COO~Z`); do not edit it.
- **Served output:** none. `model_block_pull` is box-side (runs under the PY_AWS interpreter with blpapi); a Grep for
  `model_block_pull` over `infra/` returns 0 files -- no Lambda or Terraform deploys it. The next real pull/derive run
  on the box picks the change up.
- **Test baseline at the cut, measured:** `integrations/bloomberg/research/tests/` holds 9 test modules. TWO fail to
  COLLECT at HEAD (`test_consumer_wiring.py`, `test_unresolved_overlay_renders_marked.py`: `ImportError: cannot import
  name 'load_model_block' from 'lib.research.print.render_pack'` -- pre-existing, last render_pack change @e2d89be7da,
  not this cell's). Excluding those two: `3 failed, 30 passed`, the 3 failures all in `test_fye_join.py`
  (`test_calendar_year_grouping_fails_same_period_alignment`,
  `test_fiscal_period_grouping_passes_same_period_alignment`,
  `test_fiscal_period_join_direction_assertion_all_landed_securities`) -- live-S3-coupled (`NoSuchBucket`),
  pre-existing, disjoint from this diff. There is NO existing test file for `_latest_stamp`.

**RULED, what you build:**
1. **`model_block_pull.py`** -- add ONE named error class, `class NoRawStampError(RuntimeError)` (a RuntimeError
   subclass, so every existing `except RuntimeError` still catches it), and ONE helper
   `_stamps_with_raw_pair(s3, prefix) -> list[str]` implementing EXACTLY `build_unit_map._stamps_with_refdata`'s rule
   (newest first; a stamp qualifies iff its own listing holds both `refdata.json` and `histdata.json` as exact
   basenames). Change `_latest_stamp(s3, prefix)` to return the first (newest) qualifying stamp; if no stamp folder
   exists at all, keep today's message text; if stamp folders exist but none qualifies, raise `NoRawStampError` whose
   message names `s3://{BUCKET}/{prefix}` and `"<k> stamp(s) rejected (no refdata.json+histdata.json pair)"`. Keep
   `_latest_stamp`'s signature and `str` return. `stage_derive` (`:899-906`) is UNCHANGED.
2. **Tests, a NEW file `integrations/bloomberg/research/tests/test_latest_stamp_raw_pair.py`**, pytest, offline by
   construction: a minimal stub S3 whose `list_objects_v2(Bucket, Prefix, Delimiter=None)` answers `CommonPrefixes`
   when `Delimiter="/"` and `Contents` otherwise, from an in-memory key set. Arms (names must match the `-k` filters
   below):
   - `test_incomplete_newest_is_skipped` -- stamps `20260919T011821Z/` holding only `identity.json` (the row's
     measured shape) and an OLDER `20260915T000000Z/` holding both files -> returns `20260915T000000Z`.
   - `test_head_copy_returns_the_incomplete_stamp` -- the DISCRIMINATING arm: load HEAD's module bytes via
     `subprocess.run(["git", "show", "HEAD:integrations/bloomberg/research/model_block_pull.py"])` (merge-base with
     SITEZ if HEAD has moved -- record which) into a temp file, import it under another module name, run its
     `_latest_stamp` on the same stub -> returns `20260919T011821Z` (the bug), proving arm 1 discriminates.
   - `test_all_incomplete_raises_named` -- every stamp identity-only -> `pytest.raises(NoRawStampError)`, message
     contains the prefix and `2 stamp(s) rejected` (use two stamps).
   - `test_single_complete_unchanged` -- one complete stamp -> returned as today.
   - `test_named_error_is_runtimeerror` -- `issubclass(NoRawStampError, RuntimeError)`.
   - `test_mirror_agrees_with_build_unit_map` -- ISSUER ADDITION AT THE CUT (`2.0.0_SA_COO~Z`): the rule is MIRRORED, not
     imported (the import would be circular), and two copies of one rule drift silently -- round 16's `AMGT-rk-65` exists
     because exactly that happened to the accession rule. So: over at least four stub layouts (all complete; newest
     incomplete; all incomplete; a stamp holding refdata.json only), assert `model_block_pull._stamps_with_raw_pair(s3,
     prefix) == build_unit_map._stamps_with_refdata(s3, prefix)` element for element. Importing BOTH modules in the TEST
     is fine (the circularity is only a module-level import inside `model_block_pull.py`). If they disagree on any layout,
     that is a REFUSAL with a row naming the layout -- never an edit to `build_unit_map.py` (a WALL).
   Importing `model_block_pull` needs no blpapi at import time (the existing `test_pull_consumer_arity.py` already
   imports it offline -- follow its `sys.path` pattern). No arm calls `blp`, `boto3.client`, or the real bucket.

**What this cell does NOT change:** `stage_derive`, `stage_pull`, `_read_json_from_s3`, `main()`; `build_unit_map.py`
(WALL -- see above); `pull_consumer.py` (WALL -- rk-64's); the two uncollectable test modules and the three live-coupled
`test_fye_join.py` failures (pre-existing; named, not fixed here -- file a row only if you find one is caused by this
diff).

**THE VALIDATION BAR:** a box-side producer guard with no security population, proven offline on a stub client. No
live AWS act, no Bloomberg call, no pull, no fleet run.

## 2. WHERE THIS CAME FROM

**ROUND 17**, decomposition s.25 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s ruling msg 23943 and
`ledger/ROUND_ANALYSIS.round16.md` @1764686f10 s.3 (`:68-92`); the row `AMGT_RESAPP-Z-W38-S5` (surfaced by
`0.9.0_WK_AMGT_RESAPP~38`, surfaced to the round by `3.0.0_SA_CVO~Z` msg 23940 when the analysis had dropped it without
comment). Sibling cell this round: `AMGT-rk-69` (S176-anchor), writing only `.tools/surprise-row-gate.py` and
`.tools/tests/test_acceptance_sweep.py` -- disjoint. Andrew-direct ~14:58Z (record @9bf58c4b95) and ~15:12Z (record
@1e2a54bf0f) govern this round's width and its one-slug issuance. PRD v0.13 @1699960261: no FWD or `C-` contract
changes (a defect guard inside ratified behaviour; no PRD addendum per the analysis).

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_latest_stamp_raw_pair.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~70/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-70.latest-stamp-requires-raw-pair.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant (`build_unit_map.py`, `pull_consumer.py`, the
  existing tests, the ruling and the analysis freely). Scratch is `<your worktree>/.scratch/` only.
- **Collision check, done at the cut:** the sibling `AMGT-rk-69` writes `.tools/surprise-row-gate.py` and
  `.tools/tests/test_acceptance_sweep.py` only; the held branch `wk-amgt-14-50` changes only
  `lib/research/management/{domains.json,enrich.py,management.schema.json,tests/test_lusha_domain.py}` plus AMGT org
  files (names only). Zero overlap with this cell's code paths.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~70 <0.9.0_WK_AMGT_RESAPP~70@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every `.py`
  you commit passes `.tools/commit-gate.sh` inside safe-commit.

## 4. BOUNDS

**NO LIVE AWS ACT, NO BLOOMBERG CALL, NO PULL, NO DEPLOY, NO VENDOR CALL.** PORTAL FROZEN. **COLLECTION STAYS OFF.**
**NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No non-ASCII in anything you write. **PUSH:
never** (LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by editing a WALL, never by
changing `_latest_stamp`'s signature or return type, and never by "fixing" a pre-existing test failure.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- the suite baseline (30 passed / 3 failed / 2
collection errors) is re-measured before you edit.
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W70-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-70"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest integrations/bloomberg/research/tests/test_latest_stamp_raw_pair.py -v -p no:cacheprovider 2>&1 | tail -12</invocation><expect>a final line "6 passed" (or N passed with N at least 6 if you added helper-free arms -- name them) and 0 failed, the PASSED lines naming test_incomplete_newest_is_skipped, test_head_copy_returns_the_incomplete_stamp, test_all_incomplete_raises_named, test_single_complete_unchanged, test_named_error_is_runtimeerror and test_mirror_agrees_with_build_unit_map -- the second of which proves the first discriminates (HEAD's copy returns the identity-only stamp 20260919T011821Z on the same stub), and the last of which proves the mirrored rule agrees with build_unit_map's on every layout</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-70"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest integrations/bloomberg/research/tests -q -p no:cacheprovider --ignore=integrations/bloomberg/research/tests/test_consumer_wiring.py --ignore=integrations/bloomberg/research/tests/test_unresolved_overlay_renders_marked.py 2>&1 | tail -6</invocation><expect>"3 failed, 36 passed" -- the spawn-time baseline (3 failed, 30 passed at the cut, the two uncollectable modules ignored because they fail to COLLECT at HEAD on a pre-existing render_pack ImportError) plus exactly this cell's 6 new arms passed; the 3 failures are EXACTLY the three pre-existing live-S3-coupled test_fye_join.py tests named in section 1 and no other -- print the FAILED lines. Re-measure the baseline before you edit; the bar is "baseline plus your new arms, failures unchanged in identity and count"</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-70"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io, re; s = io.open("integrations/bloomberg/research/model_block_pull.py", encoding="utf-8").read(); body = s.split("def _latest_stamp(", 1)[1].split("\ndef ", 1)[0]; print("bare_sorted_last_in_latest_stamp", body.count("sorted(stamps)[-1]")); print("named_error_class", bool(re.search(r"class NoRawStampError\(RuntimeError\)", s))); print("helper_defined", "def _stamps_with_raw_pair(" in s); print("stage_derive_fallback_unchanged", "raw_stamp = _latest_stamp(s3, f\"raw/{VENDOR}/{sec_key}/\")" in s); print("imports_build_unit_map", bool(re.search(r"^\s*(import build_unit_map|from build_unit_map|import .*build_unit_map)", s, re.M)))'</invocation><expect>bare_sorted_last_in_latest_stamp 0; named_error_class True; helper_defined True; stage_derive_fallback_unchanged True; imports_build_unit_map False (the rule is mirrored in the lower module, never imported upward -- a circular import at HEAD). This invocation is single-quoted: no regex here contains a dollar sign exposed to the shell</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-70"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io, subprocess; base = subprocess.run(["git", "merge-base", "HEAD", "SITEZ"], capture_output=True, text=True).stdout.strip(); [print(f, "compiles", bool(compile(io.open(f, "rb").read().decode("utf-8"), f, "exec")), "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8")), "| base", (lambda b: len(b) - len(b.decode("utf-8")))(subprocess.run(["git", "show", base + ":" + f], capture_output=True).stdout) if f.endswith("model_block_pull.py") else "NEW-FILE") for f in ("integrations/bloomberg/research/model_block_pull.py", "integrations/bloomberg/research/tests/test_latest_stamp_raw_pair.py")]'</invocation><expect>both files print compiles True and crlf 0; model_block_pull.py's non_ascii_bytes EQUALS its base figure printed beside it (0 at the cut -- read from the merge-base, never assumed), and the new test file prints NEW-FILE with non_ascii_bytes 0</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~70/AMGT_RESAPP.TO-AMGT-rk-70.latest-stamp-requires-raw-pair.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, naming the suite counts before/after and the three
`test_fye_join.py` failures verbatim (unchanged in identity).

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>17</round>
<slot>~70</slot>
<fabric>site-z</fabric>
