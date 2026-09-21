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

**THE MEASURED STATE at HEAD `739eb5f288` (re-read every line at your branch HEAD; M1 `AMGT-rk-90` and M2
`AMGT-rk-91` land BEFORE you and edit some of the same files).**
- **The source: 18 objects, 209,361 bytes**, all written 2026-09-11 (boto3 `list_objects_v2`, `opal-data-harvest`,
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
- **The adapter Lambda** `opal-amgt-scoped-api`: CodeSha256 `hP+6OO5PIBiaFL9IVCvFJ5ijaaVcme2q1tinW/oKa/U=`,
  LastModified 2026-09-21T19:20:04Z, artifact `research/opal-amgt-scoped-api.zip` VersionId
  `.BKJHDt8u.NTMdFQHOGf6pgAVdXpE52f`; served source `3a7afd3316` (AMGT-rk-77). Its build-input list, derived from
  `build-and-upload-scoped-amgt.sh` itself, is 57 members and includes `scoped_amgt.py` and `build_view.py`;
  commits on those 57 since `3a7afd3316`: 0 at the cut. `run_reader.py`, `rest_fetch.py` and
  `sa_forecast_fallback.py` are in NEITHER Lambda's list (chatter: 18 members).
- **Test baselines:** `lib/research/api/tests` 191 passed; `integrations/seekingalpha/tests` 9;
  `integrations/bloomberg/research/tests/test_forecast_fallback.py` 13; `lib/research/coverage/tests` 30.
- **Tests that PIN a phrase this cell retires** (census rule, CTO msg 24100): `test_forecast_fallback.py:120,176,177`
  pin `raw/seekingalpha/...` keys from `land_raw`; `integrations/seekingalpha/tests/test_rest_harvest.py` pins that
  the DEFAULT mode reproduces `land_raw` byte for byte (rk-85 ruling 4). Both are in `<paths>`; you change ONLY the
  assertions this cell's switch makes false.

**RULED, what you do, in this order:**
1. **Code (no live act).**
   - `build_view.py`: the `seekingalpha` input reads the latest stamp across the builder's
     `seeking-alpha/harvest/bronze/{symbol,report,analysis,news}/security_key=<k>/` key names; the `serp` input reads
     the builder's `bright-data/harvest/bronze/serp/` (H5's home, 0 objects) -- keep NEVER semantics. `bloomberg` is
     M1's; do not touch its line.
   - `scoped_amgt.read_coverage_freshness`: the same, from one listing per prefix, KEY NAMES ONLY (no GetObject), via
     `lib.research.harvest.store` / `lib.opal_naming` output -- never a typed key. `RAW_PREFIX` is retired only if
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
3. **Deploy the adapter (under the pair):** build via `build-and-upload-scoped-amgt.sh`, then ONE targeted
   `HALT_ACK=1 .tools/safe-apply.sh` over `module.scoped_amgt_api.aws_lambda_function.this` AND the scoped role's
   policy resource, in which `scoped_amgt_pool_prefixes` LOSES `"raw/"` and GAINS the builder key
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

- **Live acts, exactly:** 18 conditional puts (`IfNoneMatch "*"`) under `seeking-alpha/harvest/bronze/`; one artifact
  upload + one targeted apply (function + scoped policy). NOTHING ELSE writes S3, IAM or Lambda. **No S3 delete, no
  vendor call, no Bloomberg call, no secret.** Collection stays OFF; nothing is scheduled.
- **The pair** `ledger/NEVER_WIDEN_ROUND22_RK92_{COO,CTO}_HALF.md` must be on file with BOTH halves signed before
  AC4. Read both.
- **Carry-along STOP:** the adapter artifact may carry, since served source `3a7afd3316`, ONLY non-merge commits whose
  subject names `AMGT-rk-90` or `AMGT-rk-91` (M1, M2) and your own; anything else on the 57 build inputs -> STOP,
  deploy nothing.
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
print("policy_sha256", hashlib.sha256(json.dumps(d, sort_keys=True).encode()).hexdigest(), "statements", len(d["Statement"]))
ev = {"rawPath": "/api/scoped/amgt/freshness", "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
b = json.loads(json.loads(lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode())["Payload"].read())["body"])
rows = b["rows"]
for v in ("bloomberg", "seekingalpha", "serp"):
    print(v, "landed", sum(1 for r in rows if (r.get("per_input") or {}).get(v, "NEVER") != "NEVER"), "of", len(rows))
json.dump({"rows": rows}, open(".scratch/r92/pre_fresh.json", "w"))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r92/ac0.py</invocation><expect>"rk91_order True rk91_complete True" (M2 drained -- the chain is sequential; anything else STOPS the order before any edit); "refusals 0"; sa_symbol printing s3://opal-data-harvest/seeking-alpha/harvest/bronze/symbol/security_key=BA_US_Equity; "raw_entry_present True sa_bronze_entry_present True" (M1 did not remove "raw/"; AMGT-rk-82's grant is in the source)</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests/test_freshness_harvest_stamps.py -v -p no:cacheprovider</invocation><expect>all new arms PASSED, 0 failed, including: seekingalpha stamps read from the builder's seeking-alpha/harvest/bronze/{symbol,report,analysis,news}/ key names; serp read from bright-data/harvest/bronze/serp/ with NEVER on an empty listing; 0 GetObject calls on the stub; one `is` arm proving the patched lister is the object read_coverage_freshness reaches; the discriminating arm on the copy pinned at 739eb5f288 reading 0 new-grammar stamps</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests integrations/seekingalpha/tests integrations/bloomberg/research/tests/test_forecast_fallback.py lib/research/coverage/tests -q -p no:cacheprovider</invocation><expect>0 failed; passed = the spawn-time baselines (api 191, seekingalpha 9, forecast_fallback 13, coverage 30, re-measured at spawn and printed) plus this cell's new arms; the only changed pre-existing assertions are the ones naming raw/seekingalpha or the land_raw default, each listed in the deliverable</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r92/ac3.py</invocation><expect>"source_objects 18 bytes 209361"; resolve 3 of 3 to BABA_US_Equity, BA_US_Equity, COST_US_Equity with resolution MEASURED; "target_objects 0"; CodeSha256 and ArtifactVersionId printed (the rollback targets; hP+6OO5P... and .BKJHDt8u... at the cut unless M1/M2 redeployed -- then theirs); policy sha256 and "statements 4" printed; freshness landed: bloomberg N (printed; 32 at the cut), seekingalpha 0 of 250, serp 0 of 250. Any source count other than 18, or a non-empty target, STOPS the order</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r92/ac4.py</invocation><expect>written from section 1 RULED item 2 as a file: after reading both signed halves, copies the 18 objects (12 endpoint objects via store.bronze_put + 6 article bodies via harvest_grammar.put_article_bronze) and reads each back: "copied 18 read_back_equal 18 missing 0", every new key printed and each one builder output; "raw_bloomberg_objects 119 unchanged; raw_seekingalpha_objects 18 unchanged" (nothing deleted)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r92/ac5.py</invocation><expect>BEFORE the apply: the live scoped policy shows seeking-alpha/harvest/bronze/ in BOTH limbs (GetObject resource and ListBucket s3:prefix) -- "new_grant_present_both_limbs True" (CTO msg 24112); then the targeted plan reads "Plan: 0 to add, 2 to change, 0 to destroy" and, after the apply, "raw_entry_live False bright_data_bronze_entry_live True statements 4"; post CodeSha256 equals the uploaded artifact's sha</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-92"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r92/ac6.py</invocation><expect>live freshness route: "seekingalpha landed 3 of 250" naming exactly BABA_US_Equity, BA_US_Equity, COST_US_Equity, each stamp equal to that name's newest copied stamp; bloomberg landed equal to AC3's count; serp 0 of 250; 13 of 13 GET routes' status codes equal to AC3's pre-act census; the deploy-ledger entry closed and its sentinel removed</expect></criterion>
</proof_of_spec>

`ac4.py`, `ac5.py` and `ac6.py` are written by you from section 1 RULED items 2-4 and this section's expectations;
record each file's bytes in the deliverable. No judgment criterion.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~92/AMGT_RESAPP.TO-AMGT-rk-92.sa-raw-move.proof_of_spec.json`,
grade it with YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6`
(rc 0), flip the status to complete, commit, and report once: the 18 copied keys, the live policy before and after,
CodeSha256 pre/post, the freshness counts pre/post, rollback fired or not, the ledger entry.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES.** (1) M3 is the ONLY move that may remove `"raw/"`: M1 moves `raw/bloomberg` while `raw/seekingalpha`
is still read, so M1 must NOT remove it -- the M1/M2 drafter must be told. (2) The `serp` freshness column is re-pointed
at the H5 home and its list grant ADDED (a widening, named in the pair) so that `"raw/"` can be removed at all.
(3) Served change: the Seeking Alpha freshness column goes 0 -> 3 of 250 (canonical keys); named in the pair.

<status>pending</status>
<round>22</round>
<slot>~92</slot>
<fabric>site-z</fabric>
