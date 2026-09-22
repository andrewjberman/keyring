# AMGT_RESAPP task order -- `AMGT-rk-92` -- MOVE M3: the 18 Seeking Alpha objects under `raw/seekingalpha/` are COPIED byte-for-byte, with their vintage, to the builder's `seeking-alpha/harvest/bronze/` addresses; every reader of `raw/seekingalpha/` (and the empty `raw/serp/` column) switches in the SAME window; the two old writers stop; the `raw/` read grant is removed only after the new grants are re-read present; no S3 delete

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-92</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~92</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- arms no cron, alarm, monitor or cadence; the Seeking Alpha REST run
  and the Bloomberg forecast fallback are hand-run, and neither is scheduled (0 schedule references to either
  entry point). The one deploy is TARGETED to module.scoped_amgt_api.aws_lambda_function.this plus the two
  scoped-role policy resources; the deploy-ledger entry is opened before the first live write and closed on the
  post-act read.
comp-iam: RUN -- 2 roles read; scoped role opal-amgt-scoped-api-role inline policy 4 statements, the
  scoped_amgt_pool_prefixes list 21 entries (13 old-grammar incl. "raw/", 8 new-grammar from AMGT-rk-82);
  chatter role 4 statements, 8 entries, holds NO "raw/" entry and is NOT touched. BLIND: the attached AWS-managed
  logs policy is not read (it grants no S3).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~92`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. Your
first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~92;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL, inlined in full -- `AMGT-rk-92` (M3; C-FORMAT-SEQUENCE)

**The rulings, verbatim.**
- CTO round-21 analysis, `ledger/ROUND_ANALYSIS.round21.md` @739eb5f288 `:44` (msg 24119 items 4-7): *"M1-M4 | the
  moves: COPY existing objects into the new grammar with their vintage, switch readers and retire the old path in ONE
  window (v0.17 "retire": no S3 delete). Each move carries its own never-widen pair. Each re-reads that its new read
  grant is present before removing the old one (the rk-82 condition). They run as a SEQUENTIAL chain, because M1-M3
  each redeploy the API Lambda."*
- PRD v0.17 @1f7459456a, C-FORMAT-SEQUENCE `prd/AMGT_RESAPP_PRD.md:895-905`: *"Existing objects move by COPY with
  their vintage, never by re-fetch or re-derivation ... Each move of served objects carries its own never-widen pair,
  and the source path's readers switch and the source path retires in the SAME window -- a copy that leaves the old
  path serving beside the new one is a standing duplicate output path, which the shadow-pipeline veto forbids."*
  and `:903-905`: *""Retire" means that in the move's window the old path's readers are switched, its writers are
  stopped, and its read grant is removed. It does NOT mean deletion. No move performs an S3 delete."*
- C-BRONZE-AS-RECEIVED `:866-870` (form (a): `{vendor}/harvest/bronze/{request}/{entity}={id}/{YYYYMMDDTHHMMSSZ}.{ext}`),
  C-DEDUPE-BY-KEY `:885-891` (one writer per fetch key), C-SLASH-SAFE-KEY `:893-894`, C-HARVEST-HOME `:856-864`.
- CTO msg 24112: *"a move that REMOVES an old grant re-reads that its matching new grant is present first, so no
  reader is ever left with neither."*
- **AMENDMENT OF RECORD -- CTO msg 24137 (2026-09-22T04:11Z), verbatim, binding this order before spawn:**
  *"THE CALL: RULED (c).
  - The adapter's BUILD STEP (build-and-upload-scoped-amgt.sh, or a python step it runs box-side) calls
  lib.opal_naming address() for each new-grammar prefix the adapter reads, and writes a GENERATED module into the
  artifact, e.g. lib/research/api/_harvest_prefixes.py, with a "generated, do not edit" header carrying the registry
  hash.
  - scoped_amgt.py imports its new-grammar constants from that module: FILING_ATTEMPT_STATE_PREFIX now, and M3's
  seeking-alpha/bronze prefix.
  - A box-side test asserts the committed/generated module equals fresh address() output (drift = FAIL).
  - Legacy v1 prefixes stay as they are until chain G retires them."*
  and *"BINDING ON M3 AND EVERY LATER ADAPTER-TOUCHING ORDER (the M1 W90-S3 and M2 incident class, twice now):
  BEFORE any live deploy, the worker builds the zip and imports the handler FROM THE ZIP in a clean interpreter
  (sys.path = the unzipped artifact only, no repo), then exercises each changed reader once. Any ImportError is a
  STOP before deploy. It becomes a criterion on rk-92."* (Why not a runtime `lib.opal_naming` in the Lambda: it
  resolves REPO from its own location and loads `infra/logic/registry/` AND `org/standards/NAMING_SCHEMA.json`, and it
  would put the whole naming machinery on the served path -- the class behind W90-S3 and W91-S3.)

**THE MEASURED STATE at HEAD `739eb5f288` (re-read every line at your branch HEAD; M1 `AMGT-rk-90` and M2
`AMGT-rk-91` land BEFORE you and edit some of the same files).**
- **The source: 18 objects, 209,361 bytes, newest LastModified 2026-09-11T19:18:57Z** (re-measured at `96045cc865`), all written 2026-09-11 (boto3 `list_objects_v2`, `opal-data-harvest`,
  prefix `raw/seekingalpha/`). Three old keys x six endpoints: `raw/seekingalpha/{BABA_US,BA_US,COST_US}/<stamp>/`
  `{symbol,report,analysis,news}.json` plus two `article_<id>.json` each. They are the REST response bodies as
  received (compact JSON, `{"data":...,"included":...,"meta":...}`), so they ARE bronze form (a) and copy byte-for-byte.
- **The old security keys are NOT canonical.** `crosswalk.resolve()` maps `BA_US -> BA_US_Equity`,
  `BABA_US -> BABA_US_Equity`, `COST_US -> COST_US_Equity`, all `resolution MEASURED`, 3 of 3.
- **The target is empty.** `seeking-alpha/` holds 0 objects and `bright-data/` 0 (read-only listing).
- **Builder output** (live `lib/opal_naming.py`, 0 validate refusals): symbol bronze
  `s3://opal-data-harvest/seeking-alpha/harvest/bronze/symbol/security_key=BA_US_Equity`; the same shape for
  `report`, `analysis`, `news`, `metrics`; an article body goes through
  `lib.opal_data_harvest.harvest_grammar.put_article_bronze("sa", <id>, body, "json", fetched_at)` to
  `seeking-alpha/harvest/bronze/article/article_hash=<sha256("sa:<id>")>/<stamp>.json`
  (e.g. `article_hash=4bdd69a3...4211` for `sa:4943496`).
- **Readers of the old path, census by SUBTRACTION.** Native Grep, pattern
  `raw/seekingalpha|publications/v1|publication-links/v1|...` over the whole repo: 340 occurrences / 98 files; the
  `seekingalpha|raw/` pattern over `{lib,integrations,infra}/**/*.{py,tf,json,sh}`: 201 lines, 18 in the AMGT roots,
  10 non-test. Subtracting prose, config and vendor URLs leaves these READERS of `raw/seekingalpha/`:
  1. `lib/research/api/scoped_amgt.py:3085` `RAW_PREFIX = "raw/"`, used by `read_coverage_freshness` `:3231-3235`
     (lists `raw/` once and takes landing stamps per vendor from KEY NAMES only; 0 GetObject);
  2. `lib/research/freshness/build_view.py:64` `VENDOR_INPUTS = ("bloomberg", "seekingalpha", "serp")` and `:188`
     `latest_stamp_under(client, f"raw/{vendor}/{security_key}/")`;
  3. `lib/research/coverage/run_reader.py:86` `prefix = "raw/%s/%s/" % (vendor, security_key)` (box-side runner).
  Prose-only mentions, NOT readers: `crosswalk.py:139` (a measured-on string), `sa_forecast_fallback.py:14`
  (docstring).
- **Writers of the old path: 2.** `integrations/seekingalpha/rest_fetch.py:211-216` `land_raw` (the default mode of
  `run_ticker`, `harvest_grammar_mode=False`), and `integrations/bloomberg/research/sa_forecast_fallback.py:233,276`
  (`rf.land_raw` for `symbol` and `metrics`).
- **Served effect today, measured live** (direct invoke of `GET /api/scoped/amgt/freshness`, 250 rows): the
  `seekingalpha` column reads NEVER on 250 of 250, because the old keys `BA_US` etc. never match the universe's
  `*_US_Equity` keys; `serp` reads NEVER on 250 of 250 (`raw/serp/` holds 0 objects; `raw/` holds exactly
  `bloomberg` 119 + `seekingalpha` 18 = 137).
- **The adapter Lambda** `opal-amgt-scoped-api`, AS M2 LEFT IT (re-measured at `96045cc865`, read-only, amendment of
  record): CodeSha256 `vsWWFL9jRKHbQb9WP7x2Ob1Qv02nQpAOJkPcQk8/nkA=`, LastModified 2026-09-22T03:40:06Z, artifact
  `research/opal-amgt-scoped-api.zip` VersionId `uiegBMbpQeruyGtakA88KEZTXMQ2mFtT` -- these are the ROLLBACK TARGETS
  unless your own AC3 read differs (then yours). Its build-input list, re-derived from `build-and-upload-scoped-amgt.sh`
  at `96045cc865`, is 57 members and includes `scoped_amgt.py` and `build_view.py`. The NON-MERGE commits on those 57
  since the rk-77 source `3a7afd3316` are EXACTLY five: `e61604dffa`, `b9d2d7b4f1` (AMGT-rk-90, M1) and
  `20f175e4e4`, `5b6f111c55`, `ce16181ffb` (AMGT-rk-91, M2) -- all already in the served artifact. NOTE: `b9d2d7b4f1`'s
  subject does not contain the string `AMGT-rk-90`, so the carry-along check admits by this HASH LIST, never by subject
  text. `run_reader.py`, `rest_fetch.py` and `sa_forecast_fallback.py` are in NEITHER Lambda's list (chatter: 18).
- **The scoped inline policy** `opal-amgt-scoped-api-grants`, as M2 left it: 4 statements; sha256 over
  `json.dumps(doc, sort_keys=True, separators=(",", ":"))` = `39372755f1ad65ce...` (COMPACT separators -- the default
  separators give a different digest on the same document; that is the W90-S6 trap); contains `raw/` (True),
  `filings/v1` (False), `filing_attempt` (True), `seeking-alpha/harvest/bronze/` (True), `bright-data/harvest/bronze/`
  (False).
- **The adapter's NEW-GRAMMAR constants today are HAND-TYPED** (the class ruling (c) removes):
  `scoped_amgt.py:192` `FILING_ATTEMPT_STATE_PREFIX = "amgt/harvest/state/filing_attempt/"` (rk-91),
  `scoped_amgt.py:3101` `BLOOMBERG_BRONZE_PREFIX = "bloomberg/harvest/bronze/"` (rk-90), and
  `build_view.py:75` `_BLOOMBERG_BRONZE_ROOT = "bloomberg/harvest/bronze"` (rk-90). The builder prints, at
  `96045cc865` (registry_hash `3ea1e46b06a8aa14...`, 0 validate refusals), via `key(src, "harvest", tier, table,
  "date=1970-01-01")` with the trailing segment(s) cut: `amgt/harvest/state/filing_attempt/`,
  `bloomberg/harvest/bronze/`, `seeking-alpha/harvest/bronze/` (tables `symbol/ report/ analysis/ news/` beneath it),
  `bright-data/harvest/bronze/serp/` (and the tier root `bright-data/harvest/bronze/`). Legacy v1 prefixes
  (`peers/v1/`, `management/v1/`, `derived/model_block/`, `raw/` ...) stay hand-typed (chain G).
- **Test baselines:** `lib/research/api/tests` 191 passed; `integrations/seekingalpha/tests` 9;
  `integrations/bloomberg/research/tests/test_forecast_fallback.py` 13; `lib/research/coverage/tests` 30.
- **Tests that PIN a phrase this cell retires** (census rule, CTO msgs 24100/24133 -- WHOLE REPO, not just `<paths>`;
  Native Grep over `**/test*.py` for `raw/seekingalpha|raw/serp|land_raw|RAW_PREFIX` = 9 hits in 3 files, plus a
  second sweep for `"raw/` keys): `test_forecast_fallback.py:120,176,177` pin `raw/seekingalpha/...` keys from
  `land_raw`; `integrations/seekingalpha/tests/test_rest_harvest.py` pins that the DEFAULT mode reproduces `land_raw`
  byte for byte (rk-85 ruling 4); and **`lib/research/harvest/tests/test_m1_move.py:217,223`** (M1's own arm asserting
  the seekingalpha stamp is still read from `raw/seekingalpha/`). All three are in `<paths>` (the third added by this
  amendment); you change ONLY the assertions this cell's switch makes false. Re-run the census at your HEAD before
  the live acts: a pinning test OUTSIDE `<paths>` is a STOP (BLOCKING row, the issuer widens).

**RULED, what you do, in this order:**
0. **Generated new-grammar prefixes (ruling (c), msg 24137; no live act).**
   - NEW generator `infra/aws/terraform/harvest/gen_harvest_prefixes.py` (box-side; imports `lib.opal_naming` only
     here, never in adapter code): computes, from `lib.opal_naming.key()` with the partition/table segment(s) cut
     (the same derivation `lib.research.harvest.store.table_prefix` uses), EXACTLY these constants and writes them to
     `lib/research/api/_harvest_prefixes.py`:
     `FILING_ATTEMPT_STATE_PREFIX = "amgt/harvest/state/filing_attempt/"`,
     `BLOOMBERG_BRONZE_PREFIX = "bloomberg/harvest/bronze/"`,
     `SEEKING_ALPHA_BRONZE_PREFIX = "seeking-alpha/harvest/bronze/"`,
     `BRIGHT_DATA_SERP_BRONZE_PREFIX = "bright-data/harvest/bronze/serp/"`,
     plus `REGISTRY_HASH` = `lib.opal_naming.registry_hash()` at generation time. The module starts with a header line
     `# GENERATED by infra/aws/terraform/harvest/gen_harvest_prefixes.py -- DO NOT EDIT` and a line naming the
     registry hash; it contains ONLY string constants (no imports). Modes: `--write` (regenerate) and `--check`
     (regenerate in memory, compare byte-for-byte to the committed file, exit 1 on any drift).
   - The module is COMMITTED (reviewable; the box-side test reads it) AND `build-and-upload-scoped-amgt.sh` runs
     `python infra/aws/terraform/harvest/gen_harvest_prefixes.py --check` BEFORE packaging and aborts the build on any
     drift. `lib/research/api/` is a seed package of the adapter's closure, so the module is packaged automatically;
     `lib/opal_naming.py` is NOT added to the closure.
   - `scoped_amgt.py` replaces its hand-typed `FILING_ATTEMPT_STATE_PREFIX` (`:192`) and `BLOOMBERG_BRONZE_PREFIX`
     (`:3101`) with `from lib.research.api._harvest_prefixes import ...` (same NAMES, same VALUES -- the served
     behaviour of M1/M2 does not move), and uses `SEEKING_ALPHA_BRONZE_PREFIX` / `BRIGHT_DATA_SERP_BRONZE_PREFIX` for
     M3. `build_view.py` does the same for `_BLOOMBERG_BRONZE_ROOT` (keep the name as an alias of the imported value if
     other code reads it) and its seekingalpha/serp inputs. This replaces the constants' SOURCE only; it is not a
     bloomberg behaviour change.
   - NEW box-side test `lib/research/api/tests/test_harvest_prefixes.py`: (i) every constant in the committed module
     equals fresh `lib.opal_naming` output (drift = FAIL); (ii) `REGISTRY_HASH` equals `lib.opal_naming.registry_hash()`;
     (iii) the header marks it generated; (iv) ONE identity arm (W85-S1): `lib.research.api.scoped_amgt.FILING_ATTEMPT_STATE_PREFIX
     is lib.research.api._harvest_prefixes.FILING_ATTEMPT_STATE_PREFIX` (qualified imports); (v) the module imports
     nothing (AST: 0 Import nodes).
1. **Code (no live act).**
   - `build_view.py`: the `seekingalpha` input reads the latest stamp across the builder's
     `seeking-alpha/harvest/bronze/{symbol,report,analysis,news}/security_key=<k>/` key names; the `serp` input reads
     the builder's `bright-data/harvest/bronze/serp/` (H5's home, 0 objects) -- keep NEVER semantics. `bloomberg` is
     M1's; do not touch its line.
   - `scoped_amgt.read_coverage_freshness`: the same, from one listing per prefix, KEY NAMES ONLY (no GetObject), via
     the GENERATED `lib.research.api._harvest_prefixes` constants (item 0) -- never a typed key, and NEVER a runtime
     import of `lib.opal_naming` or `lib.research.harvest.store` in adapter code (both sit outside the adapter's
     closure or import pyarrow at module scope: rows W90-S3, W91-S3). `RAW_PREFIX` is retired only if
     no caller remains after M1's change (read it at HEAD; if M1 left a `raw/bloomberg` read, STOP -- the grant
     removal below would break it).
   - `run_reader.py:86`: the same new prefixes for `sa`.
   - `rest_fetch.run_ticker`: `harvest_grammar_mode` becomes the only landing path; `land_raw` raises a named error
     if called. `sa_forecast_fallback.py`: `rf.land_raw` -> `rf.land_harvest` for `symbol` and `metrics`.
   - Tests: a new `lib/research/api/tests/test_freshness_harvest_stamps.py` (the reader switch, both vendors, stubbed
     listings) and the pinned assertions above updated. Every cross-module patch imports the QUALIFIED name
     (`lib.research.api.scoped_amgt`, `lib.research.freshness.build_view`) and ONE arm asserts with `is` that the
     patched object is the one `read_coverage_freshness` reaches (W85-S1 rule). The discriminating arm pins commit
     `739eb5f288`.
2. **COPY (live, under the pair).** For each of the 18 source keys: read the bytes; canonical key =
   `crosswalk.resolve(<old key>)["security_key"]` (STOP unless all 3 resolve); `fetched_at` = the old key's stamp
   segment; endpoints `symbol|report|analysis|news` -> `store.bronze_put("seeking-alpha", <endpoint>,
   store.entity_partition("security_key", <canonical>), store.form_a_object(<fetched_at>, "json"), <bytes>)`;
   `article_<id>` -> `harvest_grammar.put_article_bronze("sa", <id>, <bytes>, "json", <fetched_at>)`. Then read every
   new object back and compare sha256 to its source: **18 of 18 equal, 0 missing**.
3. **Deploy the adapter (under the pair):** FIRST build with `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh
   --build-only .scratch/r92/m3_build.zip` (it runs the drift check and its own ISOLATED runtime check, and uploads
   NOTHING) and pass the CLOSURE CHECK criterion AC7 on that exact zip -- any ImportError there is a STOP before deploy
   (msg 24137). THEN build-and-upload (the artifact key may take ONE OR MORE builds; record every VersionId; rollback
   is to your AC3 pre-act VersionId -- row Z-S212 wording), plan with `terraform -chdir=infra/aws/terraform/harvest
   plan -target=...` (`.tools/safe-apply.sh` refuses every subcommand but apply), then ONE targeted
   `HALT_ACK=1 bash .tools/safe-apply.sh infra/aws/terraform/harvest apply -target=...` over
   `module.scoped_amgt_api.aws_lambda_function.this` AND the scoped role's policy resource, in which `scoped_amgt_pool_prefixes` LOSES `"raw/"` and GAINS the builder key
   `bright-data/harvest/bronze/` -- **but only after AC5 re-reads the live policy and prints
   `seeking-alpha/harvest/bronze/` present in both limbs** (CTO msg 24112). Plan must read `0 to add, 2 to change,
   0 to destroy`.
4. **Read back:** live freshness route: `seekingalpha` landed on EXACTLY the 3 names BABA_US_Equity, BA_US_Equity,
   COST_US_Equity (was 0 of 250) with stamps equal to their newest copied stamp; `bloomberg` column unchanged from
   your pre-act read; `serp` NEVER 250 of 250; all 13 GET routes' status codes unchanged.

**What this cell does NOT do:** delete anything (the 18 old objects stay, unread by any served role, until Andrew's
one batched delete word); build Seeking Alpha SILVER (`symbol_profile`/`news_item` are filled by the backfill run's
writer, not re-derived here -- C-FORMAT-SEQUENCE "never ... re-derivation"); touch `raw/bloomberg/` (M1) or
`filings/v1/` (M2) or the chatter Lambda; call any vendor.

## 2. WHERE THIS CAME FROM

ROUND 22, decomposition s.30 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s round-21 analysis
`ledger/ROUND_ANALYSIS.round21.md` @739eb5f288 (msg 24119). Third link of the sequential move chain
M1 (`AMGT-rk-90`) -> M2 (`AMGT-rk-91`) -> M3 (this) -> M4 (`AMGT-rk-93`). Writers it rides: `AMGT-rk-81` (store),
`AMGT-rk-85` (`harvest_grammar.py`, `rest_fetch.py` harvest mode). Grants it relies on: `AMGT-rk-82`.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
lib/research/freshness/build_view.py
lib/research/coverage/run_reader.py
integrations/seekingalpha/rest_fetch.py
integrations/bloomberg/research/sa_forecast_fallback.py
lib/research/api/tests/test_freshness_harvest_stamps.py
lib/research/api/_harvest_prefixes.py
lib/research/api/tests/test_harvest_prefixes.py
lib/research/harvest/tests/test_m1_move.py
infra/aws/terraform/harvest/gen_harvest_prefixes.py
infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh
integrations/seekingalpha/tests/test_rest_harvest.py
integrations/bloomberg/research/tests/test_forecast_fallback.py
infra/aws/terraform/harvest/scoped-amgt-api.tf
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~92/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-92.sa-raw-move.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- A surface NOT in `<paths>` is a WALL (read freely). `lib/research/harvest/store.py`, `harvest_grammar.py`,
  `crosswalk.py`, `chatter-axis-schedule.tf` are walls.
- **Commit** with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~92 <0.9.0_WK_AMGT_RESAPP~92@opal.agent>"
  -F <msgfile> -- <paths>` (message file written by the Write tool). Commit the CODE before any live act.

## 4. BOUNDS

- **Live acts, exactly:** 18 conditional puts (`IfNoneMatch "*"`) under `seeking-alpha/harvest/bronze/`; ONE OR MORE
  builds/uploads of the one artifact key (each VersionId recorded) + one targeted apply (function + scoped policy). NOTHING ELSE writes S3, IAM or Lambda. **No S3 delete, no
  vendor call, no Bloomberg call, no secret.** Collection stays OFF; nothing is scheduled.
- **The pair** `ledger/NEVER_WIDEN_ROUND22_RK92_{COO,CTO}_HALF.md` must be on file with BOTH halves signed before
  AC4. Read both.
- **Carry-along STOP:** the adapter artifact may carry, since served source `3a7afd3316`, ONLY the five non-merge
  commits `e61604dffa b9d2d7b4f1 20f175e4e4 5b6f111c55 ce16181ffb` (M1, M2 -- admitted by HASH, not subject text) and
  your own; anything else on the (re-derived) build inputs -> STOP, deploy nothing.
- **Tool interfaces (issuer-text defects in rk-90/rk-91, carried here):** `.tools/deploy_ledger.py open --slug <s>
  --title <t> --author <serial> [--leg ...]` (no `--legs`), opened BEFORE the first live write and closed on the
  post-act read; `.tools/safe-apply.sh` accepts only `apply`. Where a criterion's literal text disagrees with a real
  CLI, run the real one, record both, file a row naming the issuer defect.
- **Policy hash formula:** always `hashlib.sha256(json.dumps(doc, sort_keys=True, separators=(",", ":")).encode())`;
  a criterion comparing to another criterion's digest uses the SAME formula.
- **Window condition (CTO):** record in your report the final `raw/seekingalpha/` count and newest LastModified; the
  issuer re-reads after the drain (one new object = copied under the pair; a second = BLOCKING row).
- **Tests:** each test directory in its OWN pytest call (a multi-directory call trips the W85-S1 module-identity
  clash).
- **REFUSAL CLAUSE:** a criterion you cannot satisfy as written is REFUSED with its measurement and a row; never
  repaired, widened, or satisfied by a route not named here.
- **Rows** `AMGT_RESAPP-Z-W92-S<k>`; a pure disarm sets `DISMISSED_WITH_REASON`.
- **Rollback (any AC6 failure):** artifact `copy_object` from your AC3 VersionId, re-apply the function; policy list
  restored to its AC3 contents and re-applied; the 18 new objects are left (additive, unread once readers roll back);
  read back AC3's hashes. No delete.

## 5. PROOF OF SPEC -- one clause per criterion

**Each criterion runs a FILE you write verbatim from the block beside it into `.scratch/r92/` (W84-S1 rule: no
escape-bearing inline code).** Record each criterion's ACTUAL OUTPUT and DENOMINATOR.

`.scratch/r92/ac0.py`:
```
import re, subprocess, sys
sys.path.insert(0, ".")
import lib.opal_naming as n
from lib.research.harvest import store
import glob
f91 = glob.glob("org/missions/D5/AMGT/AMGT_RESAPP/task-orders/*TO-AMGT-rk-91.*")
t = open(f91[0], encoding="utf-8").read() if f91 else ""
print("rk91_order", bool(f91), "rk91_complete", bool(re.search("^<" + "status>complete</" + "status>$", t, re.M)))
print("refusals", len(n.validate()[0]))
print("sa_symbol", n.address("seeking-alpha", "harvest", "bronze", "symbol", "security_key=BA_US_Equity"))
tf = open("infra/aws/terraform/harvest/scoped-amgt-api.tf", encoding="utf-8").read()
print("raw_entry_present", '"raw/",' in tf, "sa_bronze_entry_present", '"seeking-alpha/harvest/bronze/",' in tf)
```

`.scratch/r92/ac3.py` (pre-act baseline and source census):
```
import boto3, hashlib, json, sys
sys.path.insert(0, ".")
from lib.research.identity import crosswalk
s3 = boto3.client("s3", region_name="us-east-1"); lam = boto3.client("lambda", region_name="us-east-1"); iam = boto3.client("iam")
src = [o for p in s3.get_paginator("list_objects_v2").paginate(Bucket="opal-data-harvest", Prefix="raw/seekingalpha/") for o in p.get("Contents", [])]
print("source_objects", len(src), "bytes", sum(o["Size"] for o in src))
old = sorted({o["Key"].split("/")[2] for o in src})
print("resolve", [(k, crosswalk.resolve(k).get("security_key"), crosswalk.resolve(k).get("resolution")) for k in old])
tgt = sum(len(p.get("Contents", [])) for p in s3.get_paginator("list_objects_v2").paginate(Bucket="opal-data-harvest", Prefix="seeking-alpha/"))
print("target_objects", tgt)
c = lam.get_function_configuration(FunctionName="opal-amgt-scoped-api")
h = s3.head_object(Bucket="opal-313476888478-lambda-artifacts", Key="research/opal-amgt-scoped-api.zip")
print("CodeSha256", c["CodeSha256"], "ArtifactVersionId", h.get("VersionId"))
d = iam.get_role_policy(RoleName="opal-amgt-scoped-api-role", PolicyName="opal-amgt-scoped-api-grants")["PolicyDocument"]
print("policy_sha256", hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":")).encode()).hexdigest(), "statements", len(d["Statement"]))
ev = {"rawPath": "/api/scoped/amgt/freshness", "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
b = json.loads(json.loads(lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode())["Payload"].read())["body"])
rows = b["rows"]
for v in ("bloomberg", "seekingalpha", "serp"):
    print(v, "landed", sum(1 for r in rows if (r.get("per_input") or {}).get(v, "NEVER") != "NEVER"), "of", len(rows))
json.dump({"rows": rows}, open(".scratch/r92/pre_fresh.json", "w"))
```

`.scratch/r92/ac7.py` (CLOSURE CHECK, msg 24137 -- run on the `--build-only` zip BEFORE any upload or apply):
```
import os, shutil, subprocess, sys, zipfile
zp = os.path.abspath(".scratch/r92/m3_build.zip")
root = os.path.abspath(".scratch/r92/zipcheck")
shutil.rmtree(root, ignore_errors=True)
with zipfile.ZipFile(zp) as zf:
    zf.extractall(root)
    print("unzipped", len(zf.namelist()), "entries from", os.path.basename(zp))
venv = os.path.abspath(".scratch/r92/venv")
if not os.path.isdir(venv):
    subprocess.run([sys.executable, "-m", "venv", "--without-pip", venv], check=True)
vpy = os.path.join(venv, "Scripts", "python.exe") if os.name == "nt" else os.path.join(venv, "bin", "python")
probe = subprocess.run([vpy, "-I", "-c", "import sys; sys.path.insert(0, sys.argv[1]); import rpds", root], capture_output=True)
if probe.returncode != 0:
    pin = [ln for ln in open("infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh", encoding="utf-8").read().splitlines() if ln.startswith("RPDS_PIN=")][0].split("=", 1)[1].strip().strip(chr(34))
    wd = os.path.abspath(".scratch/r92/local_wheels")
    subprocess.run([sys.executable, "-m", "pip", "download", "--quiet", "--disable-pip-version-check", "--no-deps", "--only-binary=:all:", "-d", wd, pin], check=True)
    placed = []
    for wn in sorted(os.listdir(wd)):
        with zipfile.ZipFile(os.path.join(wd, wn)) as wz:
            for n in wz.namelist():
                if n.startswith("rpds/") and n.endswith((".pyd", ".so")) and not os.path.exists(os.path.join(root, n)):
                    wz.extract(n, root)
                    placed.append(n)
    print("overlay (scratch root ONLY, not the zip):", placed)
rt = os.path.abspath(".scratch/r92/lambda_runtime_pkgs")
import shutil, importlib.util as _u
if os.path.isdir(rt):
    shutil.rmtree(rt)
os.makedirs(rt)
for pkg in ("boto3", "botocore", "s3transfer", "jmespath", "dateutil", "urllib3", "six"):
    spec = _u.find_spec(pkg)
    src = os.path.dirname(spec.origin) if spec.submodule_search_locations else spec.origin
    dst = os.path.join(rt, os.path.basename(src))
    (shutil.copytree if os.path.isdir(src) else shutil.copy2)(src, dst)
print("lambda runtime set (python3.11 provides these; the build never vendors them):", sorted(os.listdir(rt)))
env = dict(os.environ, LAMBDA_RUNTIME_PKGS=rt)
r = subprocess.run([vpy, "-I", os.path.abspath(".scratch/r92/ac7_inner.py"), root], env=env)
sys.exit(r.returncode)
```

`.scratch/r92/ac7_inner.py` (runs INSIDE the fresh venv, `-I`, sys.path = the unzipped artifact only):
```
import json, os, sys, importlib.util
root = sys.argv[1]
runtime = os.environ["LAMBDA_RUNTIME_PKGS"]
sys.path[:] = [root, runtime] + [p for p in sys.path if "site-packages" not in p and p != ""]
os.chdir(root)
import lib
if not os.path.abspath(lib.__path__[0]).startswith(os.path.abspath(root)):
    print("FAIL: lib resolves outside the artifact --", lib.__path__[0])
    sys.exit(2)
print("control: lib resolves inside the artifact")
for repo_only in ("lib.opal_naming", "lib.research.harvest.store", "pyarrow"):
    try:
        spec = importlib.util.find_spec(repo_only)
    except ImportError:
        spec = None
    if spec is not None:
        print("FAIL: repo-only module importable --", repo_only)
        sys.exit(2)
print("control: lib.opal_naming, lib.research.harvest.store, pyarrow NOT importable (isolated)")
import boto3
print("control: boto3 importable from the Lambda runtime set only --", os.path.abspath(boto3.__file__).startswith(os.path.abspath(runtime)))
pool = os.path.join(root, "_closure_pool")
os.environ["AMGT_POOL_ROOT"] = pool
def put(key, obj):
    p = os.path.join(pool, *key.split("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(json.dumps(obj))
results = []
def arm(name, fn):
    try:
        out = fn()
        print("ARM", name, "OK", str(out)[:160])
        results.append("OK")
    except ImportError as exc:
        print("ARM", name, "IMPORT-FAIL", type(exc).__name__, exc)
        results.append("IMPORT")
    except Exception as exc:
        print("ARM", name, "OTHER-FAIL", type(exc).__name__, str(exc)[:200])
        results.append("OTHER")
import lambda_function
from lib.research.api import _harvest_prefixes as hp
from lib.research.api import scoped_amgt as sa
from lib.research.freshness import build_view as bv
print("generated constants", sorted(n for n in dir(hp) if n.isupper()))
put(hp.SEEKING_ALPHA_BRONZE_PREFIX + "symbol/security_key=BA_US_Equity/20260911T191857Z.json", {"data": {}})
put(hp.BLOOMBERG_BRONZE_PREFIX + "refdata/security_key=BA_US_Equity/20260915T000000Z.json", {"x": 1})
put(hp.FILING_ATTEMPT_STATE_PREFIX + "security_key=BA_US_Equity/UNRESOLVED-SOURCE.json", {"status": "UNRESOLVED-SOURCE"})
put("universe/v1/2026-09-16.json", {"as_of": "2026-09-16", "names": [{"security_key": "BA_US_Equity"}]})
arm("read_coverage_freshness", sa.read_coverage_freshness)
arm("filing_attempt_reader", lambda: sa._read_filing_source_object("BA_US_Equity"))
arm("build_view_seekingalpha", lambda: bv.latest_stamp_under(sa._LocalPoolClient(pool), hp.SEEKING_ALPHA_BRONZE_PREFIX + "symbol/security_key=BA_US_Equity/"))
ev = {"rawPath": "/api/scoped/amgt/freshness", "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
arm("handler_freshness_route", lambda: lambda_function.lambda_handler(ev, None).get("statusCode"))
print("RESULT arms", len(results), "ok", results.count("OK"), "import_fail", results.count("IMPORT"), "other_fail", results.count("OTHER"))
sys.exit(0 if results.count("OK") == len(results) else 1)
```
If a reader M3 adds under a NEW function name also runs on the served path, add ONE arm for it to `ac7_inner.py` (same
pattern, recorded in the deliverable). An `OTHER-FAIL` caused only by fixture shape is fixed by adjusting the FIXTURE
(never the code) and re-run; an `IMPORT-FAIL` is a STOP before deploy with a BLOCKING row.

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r92/ac0.py</invocation><expect>"rk91_order True rk91_complete True" (M2 drained -- the chain is sequential; anything else STOPS the order before any edit); "refusals 0"; sa_symbol printing s3://opal-data-harvest/seeking-alpha/harvest/bronze/symbol/security_key=BA_US_Equity; "raw_entry_present True sa_bronze_entry_present True" (M1 did not remove "raw/"; AMGT-rk-82's grant is in the source)</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python infra/aws/terraform/harvest/gen_harvest_prefixes.py --check && python -m pytest lib/research/api/tests/test_freshness_harvest_stamps.py lib/research/api/tests/test_harvest_prefixes.py -v -p no:cacheprovider</invocation><expect>the generator's --check exits 0 (committed module equals fresh builder output); all new arms PASSED, 0 failed, including: test_harvest_prefixes.py's five arms (each constant equals fresh lib.opal_naming output; REGISTRY_HASH equals registry_hash(); the generated header; the `is` identity arm scoped_amgt.FILING_ATTEMPT_STATE_PREFIX is _harvest_prefixes.FILING_ATTEMPT_STATE_PREFIX; 0 Import nodes in the module); seekingalpha stamps read from the builder's seeking-alpha/harvest/bronze/{symbol,report,analysis,news}/ key names; serp read from bright-data/harvest/bronze/serp/ with NEVER on an empty listing; 0 GetObject calls on the stub; one `is` arm proving the patched lister is the object read_coverage_freshness reaches; the discriminating arm on the copy pinned at 739eb5f288 reading 0 new-grammar stamps</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests -q -p no:cacheprovider ; python -m pytest integrations/seekingalpha/tests -q -p no:cacheprovider ; python -m pytest integrations/bloomberg/research/tests/test_forecast_fallback.py -q -p no:cacheprovider ; python -m pytest lib/research/coverage/tests -q -p no:cacheprovider ; python -m pytest lib/research/harvest/tests -q -p no:cacheprovider</invocation><expect>one pytest call per directory (W85-S1 clash); each reads 0 failed; passed = the spawn-time baselines (api 191, seekingalpha 9, forecast_fallback 13, coverage 30, harvest 52, re-measured at spawn and printed) plus this cell's new arms; the only changed pre-existing assertions are the ones naming raw/seekingalpha or the land_raw default, each listed in the deliverable</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r92/ac3.py</invocation><expect>"source_objects 18 bytes 209361"; resolve 3 of 3 to BABA_US_Equity, BA_US_Equity, COST_US_Equity with resolution MEASURED; "target_objects 0"; CodeSha256 and ArtifactVersionId printed (the rollback targets; vsWWFL9j... and uiegBMbp... as M2 left them -- amendment of record); policy sha256 printed with COMPACT separators (39372755f1ad65ce... as M2 left it) and "statements 4"; freshness landed: bloomberg N (printed; 32 at the cut), seekingalpha 0 of 250, serp 0 of 250. Any source count other than 18, or a non-empty target, STOPS the order</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r92/ac4.py</invocation><expect>written from section 1 RULED item 2 as a file: after reading both signed halves, copies the 18 objects (12 endpoint objects via store.bronze_put + 6 article bodies via harvest_grammar.put_article_bronze) and reads each back: "copied 18 read_back_equal 18 missing 0", every new key printed and each one builder output; "raw_bloomberg_objects 119 unchanged; raw_seekingalpha_objects 18 unchanged" (nothing deleted)</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only .scratch/r92/m3_build.zip 2>&1 | tail -3 && python .scratch/r92/ac7.py</invocation><expect>RUN BEFORE AC5 (the closure check, CTO msg 24137): the build prints "BUILD-ONLY: copied to .scratch/r92/m3_build.zip -- NOT uploaded" after its own drift check and "ISOLATED: OK"; then ac7.py prints (AMENDED by 2.0.0_SA_COO~Z after row W92-S1: the isolated interpreter carries EXACTLY the packages the python3.11 Lambda runtime provides -- boto3, botocore, s3transfer, jmespath, dateutil, urllib3, six -- and proves isolation by lib resolving inside the artifact and repo-only modules being unimportable) "control: lib resolves inside the artifact", "control: lib.opal_naming, lib.research.harvest.store, pyarrow NOT importable (isolated)", "control: boto3 importable from the Lambda runtime set only -- True", the generated constants [BLOOMBERG_BRONZE_PREFIX, BRIGHT_DATA_SERP_BRONZE_PREFIX, FILING_ATTEMPT_STATE_PREFIX, REGISTRY_HASH, SEEKING_ALPHA_BRONZE_PREFIX], every ARM line "OK" (read_coverage_freshness, filing_attempt_reader, build_view_seekingalpha, handler_freshness_route 200, plus any arm added for a new served reader) and "RESULT ... import_fail 0 other_fail 0", exit 0. ANY IMPORT-FAIL = STOP before deploy with a BLOCKING row (disarm_owner 2.0.0_SA_COO~Z); nothing is uploaded or applied</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r92/ac5.py</invocation><expect>BEFORE the apply: the live scoped policy shows seeking-alpha/harvest/bronze/ in BOTH limbs (GetObject resource and ListBucket s3:prefix) -- "new_grant_present_both_limbs True" (CTO msg 24112); then the targeted plan (`terraform -chdir=infra/aws/terraform/harvest plan -target=...`; safe-apply accepts only apply) reads "Plan: 0 to add, 2 to change, 0 to destroy", AC7 has already passed on the zip being uploaded, and, after the apply, "raw_entry_live False bright_data_bronze_entry_live True statements 4"; post CodeSha256 equals the uploaded artifact's sha</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r92/ac6.py</invocation><expect>live freshness route: "seekingalpha landed 3 of 250" naming exactly BABA_US_Equity, BA_US_Equity, COST_US_Equity, each stamp equal to that name's newest copied stamp; bloomberg landed equal to AC3's count; serp 0 of 250; 13 of 13 GET routes' status codes equal to AC3's pre-act census; the deploy-ledger entry closed and its sentinel removed</expect></criterion>
</proof_of_spec>

`ac4.py`, `ac5.py` and `ac6.py` are written by you from section 1 RULED items 2-4 and this section's expectations;
record each file's bytes in the deliverable. No judgment criterion.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~92/AMGT_RESAPP.TO-AMGT-rk-92.sa-raw-move.proof_of_spec.json`,
grade it with YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC7,AC5,AC6`
(rc 0), flip the status to complete, commit, and report once: the 18 copied keys, the generated constants and their
registry hash, AC7's closure-check arms, the live policy before and after (compact-separator sha), CodeSha256 and every
artifact VersionId pre/post, the freshness counts pre/post, the final `raw/seekingalpha/` count and newest
LastModified, rollback fired or not, the ledger entry.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES.** (1) M3 is the ONLY move that may remove `"raw/"`: M1 moves `raw/bloomberg` while `raw/seekingalpha`
is still read, so M1 must NOT remove it -- the M1/M2 drafter must be told. (2) The `serp` freshness column is re-pointed
at the H5 home and its list grant ADDED (a widening, named in the pair) so that `"raw/"` can be removed at all.
(3) Served change: the Seeking Alpha freshness column goes 0 -> 3 of 250 (canonical keys); named in the pair.
(4) AMENDED BEFORE SPAWN by `2.0.0_SA_COO~Z` on CTO msg 24137 (ruling (c) + the binding closure check): RULED item 0
(generated `_harvest_prefixes` module, generator, build-time drift check, box-side drift test), criterion AC7 (the
closure check, run before AC5), `<paths>` widened by exactly the build script, the generator, the generated module,
its test, and `test_m1_move.py` (it pins `raw/seekingalpha` at :217/:223 -- found by the whole-repo pinning census);
baselines re-measured to the state M2 left; carry-along admitted by hash; rk-90/rk-91 issuer-text lessons carried
(policy-sha formula, deploy_ledger/safe-apply CLIs, one-or-more builds, one pytest per directory).

<status>complete</status>
<round>22</round>
<slot>~92</slot>
<fabric>site-z</fabric>
