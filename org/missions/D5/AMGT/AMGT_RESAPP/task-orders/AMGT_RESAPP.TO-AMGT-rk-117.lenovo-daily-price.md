# AMGT_RESAPP task order -- `AMGT-rk-117` -- L-PX: generalise the dense daily-price puller off its hard-coded BABA constants (code, default unchanged), then ONE `HistoricalDataRequest` for Lenovo `992_HK_Equity` (PX_LAST, DAILY) landing `histdata_daily_px` BRONZE -- bronze only, NO served key, NO pair

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-117</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~117</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one manual pull; no cron, alarm, monitor or cadence is armed or read.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant moves; one S3 bronze write under the seat's existing
  credentials.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification; the declaration applies to the worker's
  deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~117`.** Work ONLY in the worktree named in your spawn prompt. First act: print
`git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that `org/`, `.tools/`,
`integrations/bloomberg/research/pull_baba_daily_px.py` and `integrations/bloomberg/READ_HERE.md` exist; if any is
absent, STOP with a BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~117;`.
**NEVER RUN AN INSTALL.** Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.
**Never print a credential value.**

## 1. THE CELL -- `AMGT-rk-117` (round 30, the Lenovo trial's wave 2, stage 11)

**The governing text, verbatim:**
- PRD v0.23 s.12, stage 11: *"price | the daily price pull | none"* -- Lenovo has NO daily price series today.
- Cap: *"Bloomberg | 1 unique security."*
- CTO msg 24261 Q4: the READ_HERE sign-in check is this cell's AC0.
- Andrew-direct @`6f1a72e4be`: each pull is sized and printed before it runs.

**WHY THIS CELL HAS TWO LIMBS, and why it writes NO served key -- the issuer's measurement, which you re-measure:**
- The ONLY dense daily PX_LAST producer in the estate is `integrations/bloomberg/research/pull_baba_daily_px.py`, and
  it is **hard-coded to BABA**: `SECURITY = "BABA US Equity"`, `SEC_KEY = "BABA_US_Equity"`, `HIST_START = "2016-01-01"`,
  `HIST_END = "2025-12-31"`, and `main()` takes **no arguments at all**. Run as it stands it would pull BABA again --
  a different security, outside this trial's word.
- The OTHER price producer, `integrations/bloomberg/research/price_axis_pull.py`, writes the SERVED Lead Panel rank
  rows into DynamoDB `opal-harvest-security-metrics`. It is **cohort-wide by construction**: it loads the universe
  (34 MEASURED tickers, Lenovo among them), chunks 20 securities per `HistoricalDataRequest`, and writes a whole
  ranked GENERATION with a `_CURRENT` pointer. Ranking a cohort of one is meaningless, and running it would re-rank
  and rewrite the served rows for **every** name. **It is OUT OF SCOPE for this cell and is NOT run.** The served
  Lead Panel price rows for Lenovo are an OPEN QUESTION carried to the CTO in the round-30 decomposition.
- So this cell lands Lenovo's dense price series in **BRONZE only**. Bronze has **no served reader**, so per the CTO's
  ruling (msg 24261 Q4: a pair binds at a served read) **this cell carries NO never-widen pair.**

**THE MEASURED STATE (issuer, read-only, 2026-09-22 ~18:5xZ; re-measure at your HEAD in AC1):**
- `bloomberg/harvest/bronze/histdata_daily_px/`: **1** object in total across the estate, **0** for `992_HK_Equity`.
- Lenovo's annual-periodicity PX_LAST already sits in its `histdata` bronze; this cell adds the DAILY series that
  rk-109's `fye_join` pairs to a 31 March period end.

**THE SIZED PULL, printed by AC0 before any call:**
- The READ_HERE login-state probe: 1 `ReferenceDataRequest` (`SPX Index` x `PX_LAST`).
- The price pull: **1** `HistoricalDataRequest` -- `992 HK Equity` x `PX_LAST` (1 field), `2016-01-01`..`2025-12-31`,
  `DAILY`.
- **Cell total: 2 requests, 2 security-field points, 1 unique security.**

**RULED, LIMB 1 (code, no call).** In `integrations/bloomberg/research/pull_baba_daily_px.py`:
- give `main` an argument parser with `--security` (default `"BABA US Equity"`) and `--sec-key`
  (default `security_key(--security)`, i.e. the existing derivation), plus `--start` / `--end` defaulting to today's
  `HIST_START` / `HIST_END` constants. **Every default preserves today's behaviour exactly**: a bare `main()` run
  still pulls BABA over the same window to the same key.
- the module's `SECURITY` / `SEC_KEY` / `HIST_START` / `HIST_END` constants stay as the DEFAULTS, never deleted.
- the pull-log entry records the security actually pulled, not the constant.
- add `lib`-free unit tests in a NEW file `integrations/bloomberg/research/tests/test_daily_px_args.py`:
  - `test_defaults_are_baba_unchanged` -- parsed defaults equal the module constants;
  - `test_security_and_sec_key_override` -- `--security "992 HK Equity"` yields sec_key `992_HK_Equity`;
  - `test_no_blp_import_at_parse` -- argument parsing performs NO Bloomberg call (the client loader is not invoked).

**RULED, LIMB 2 (the ONE live pull), after limb 1's tests pass:**
`python integrations/bloomberg/research/pull_baba_daily_px.py --security "992 HK Equity"`

It writes exactly ONE S3 object:
- (W1) `bloomberg/harvest/bronze/histdata_daily_px/security_key=992_HK_Equity/<stamp>.json` (conditional put,
  immutable).
and ONE local file:
- (W2) the script's own pull-log path (a scratch/deliverable JSON, not S3) -- record where it lands; if it resolves
  inside `org/missions/.../deliverables/0.9.0_WK_AMGT_RESAPP~*/`, it is yours only if it is under YOUR slot's
  directory; if it resolves to another slot's directory, DO NOT write it: file a row and pass `--state`-style
  redirection only if the script offers one, else record the refusal.

## 2. WHERE THIS CAME FROM

ROUND 30, decomposition s.38 (cut by `2.0.0_SA_COO~Z`), on the CTO's round-29 analysis msg 24328 and PRD v0.23 s.12
stage 11.

## 3. SURFACES

<paths>
integrations/bloomberg/research/pull_baba_daily_px.py
integrations/bloomberg/research/tests/test_daily_px_args.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~117/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-117.lenovo-daily-price.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- **A surface not named here is a WALL**, including `price_axis_pull.py`, `model_block_pull.py`, every DynamoDB table
  and the crosswalk. Scratch is `<worktree>/.scratch/r117/`.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~117 <0.9.0_WK_AMGT_RESAPP~117@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **ISSUER AMENDMENT 1 (2026-09-22, 2.0.0_SA_COO~Z, on your BLOCKING row W117-S2): THIS CELL NOW CARRIES A PAIR, AND
  YOUR REFUSAL WAS CORRECT.** The cell was cut "no served key is written". That premise was FALSE and it was mine: the
  served `/freshness` route reads `histdata_daily_px` as one of six Bloomberg bronze request tables
  (`lib/research/api/scoped_amgt.py:3108`, `_BLOOMBERG_BRONZE_REQUESTS`, consumed by `read_coverage_freshness`), which
  I re-measured myself. A first `histdata_daily_px` object for Lenovo CHANGES what `/freshness` serves for that name.
  So:
  - the pair is `ledger/NEVER_WIDEN_ROUND30_RK117_{COO,CTO}_HALF.md`. The COO half is SIGNED; **AC0 now also requires
    the CTO half to be present and signed, and STOPS with a BLOCKING row if it is not** -- exactly as rk-116's did;
  - AC1's served-reader finding is EXPECTED and is NO LONGER a STOP: record the count and the call site and continue;
  - the live leg proceeds under the pair, with its rollback read from the COO half: bronze is write-once and an S3
    delete is a destructive act reserved to a human word, so a bad object is superseded by a NEWER stamp, never deleted;
  - AC4 gains one arm: every name OTHER than 992 shows a freshness answer byte-equal to its pre-act value, with the
    denominator printed.
- **ISSUER AMENDMENT 2 (2026-09-22, on the CTO half @3c9c171dd4): THE FRESHNESS STAMP IS NOT REVERSIBLE BY ADDITION.**
  `_bloomberg_bronze_stamps` (`scoped_amgt.py:3189-3215`, the ONLY read of `_BLOOMBERG_BRONZE_REQUESTS`) takes the
  **MAXIMUM** stamp per security. So publishing a newer object to "roll back" moves the served answer FURTHER FORWARD,
  never back; only an S3 DELETE lowers it, and that is destructive, reserved to a human word, and NOT covered by this
  pair. **A bad object therefore makes the surface read FRESHER than its data warrants.**
  - **So the mitigation is a PRECONDITION, not a remedy: BEFORE you accept the run, verify the landed object's
    CONTENT -- its row count, its date range, its first and last observations -- not merely its presence.** Print them.
  - A wrong object is corrected by a NEWER stamp carrying right data (which fixes the data AND leaves freshness
    honest). A delete escalates to Andrew and is not yours.
  - **The CTO's precision, which supersedes my half's wording:** 992 is ALREADY in the freshness map at
    `20260922T201211Z` (rk-116 tonight), so this act MOVES its stamp forward rather than adding it; and **36 of the 37
    security partitions cannot move BY CONSTRUCTION**, since each name's stamp is computed from its own keys. AC4's
    control arm prints that denominator: 36 of 36 unchanged.
- **The old text, kept so the change is legible:** "NO PAIR, because NO served key is written. If your own AC1 finds a
  served reader of `bloomberg/harvest/bronze/histdata_daily_px/`, STOP with a BLOCKING row: the premise of "no pair"
  would be false and
  the issuer must cut a pair first.
- **DAPI DOWN = STOP**, exactly as rk-116: file a BLOCKING row naming the surface and STOP. You do NOT run the
  sign-in.
- **NEVER run `price_axis_pull.py`.** It is cohort-wide and writes served DynamoDB rows for every name.
- **ONE pull, never retried.**
- **Deploy ledger:** open it AFTER limb 1 and AC1 and BEFORE the pull:
  `python .tools/deploy_ledger.py open --slug amgt-rk117-lenovo-daily-px --title "<title>" --author "0.9.0_WK_AMGT_RESAPP~117" --leg "w1|s3-prefix|opal-data-harvest/bloomberg/harvest/bronze/histdata_daily_px/security_key=992_HK_Equity/|AC4"`
  Close the leg on AC4, then the entry. There is NO `--legs` flag.
- **ROLLBACK (any one trigger):** AC4 finds no new object under Lenovo's `histdata_daily_px` prefix; or finds an
  object written under ANY other `security_key`; or AC3's run named a security other than `992 HK Equity`.
  **The rollback is NEVER a delete:** the bronze key is immutable and has 0 production readers, so a wrong object is
  LEFT, recorded in a row, and superseded by a corrected stamp if one is authorised. A wrong-SECURITY pull is a
  quota incident: record it, do not re-run.
- **No other write:** no DynamoDB, no derived block, no crosswalk, no filings, no SA, no portal, no IAM.
- **THE REFUSAL CLAUSE** applies. **SURPRISE ROWS:** `AMGT_RESAPP-Z-W117-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (literal; timeout 600)

**Grading order:** AC0, AC1, AC2 (limb 1), (open the ledger), AC3 (limb 2, live), AC4, (close the ledger), AC5.

`.scratch/r117/ac0.py`:
```
import importlib.util, subprocess, sys
spec = importlib.util.spec_from_file_location("px", "integrations/bloomberg/research/pull_baba_daily_px.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
print("module_defaults SECURITY", m.SECURITY, "SEC_KEY", m.SEC_KEY, "start", m.HIST_START, "end", m.HIST_END)
print("SIZED: 1 HistoricalDataRequest (992 HK Equity x PX_LAST, %s..%s, DAILY) + 1 SPX login probe = 2 requests, 2 points, 1 unique security" % (m.HIST_START, m.HIST_END))
print(subprocess.run([sys.executable, "integrations/bloomberg/auth/bbg_credentials.py", "--check"], capture_output=True, text=True).stdout.strip()[:300])
```

`.scratch/r117/ac1.py`:
```
import boto3, json, os, re
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
def ls(p): return sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
allk = ls("bloomberg/harvest/bronze/histdata_daily_px/")
mine = [k for k in allk if "security_key=992_HK_Equity" in k]
print("histdata_daily_px total", len(allk), "for_992", len(mine))
json.dump({"all": allk, "mine": mine}, open(".scratch/r117/pre.json", "w"), indent=1)
hits = []
for root, dirs, files in os.walk("lib"):
    dirs[:] = [d for d in dirs if d not in ("tests", "__pycache__")]
    for f in files:
        if f.endswith(".py") and "histdata_daily_px" in open(os.path.join(root, f), encoding="utf-8", errors="replace").read():
            hits.append(os.path.join(root, f))
print("served_readers_of_histdata_daily_px_under_lib", len(hits), hits)
```

`.scratch/r117/ac4.py`:
```
import boto3, json
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
pre = json.load(open(".scratch/r117/pre.json"))
def ls(p): return sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
allk = ls("bloomberg/harvest/bronze/histdata_daily_px/")
added = [k for k in allk if k not in pre["all"]]
mine = [k for k in allk if "security_key=992_HK_Equity" in k]
print("total pre", len(pre["all"]), "post", len(allk), "added", len(added), added)
print("for_992 pre", len(pre["mine"]), "post", len(mine))
print("added_all_under_992", all("security_key=992_HK_Equity" in k for k in added))
if added:
    doc = json.loads(s3.get_object(Bucket=B, Key=added[-1])["Body"].read())
    sec = list(doc.keys())
    rows = doc.get("992 HK Equity") or []
    print("securities_in_object", sec, "rows", len(rows), "first", rows[:1], "last", rows[-1:])
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-117"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r117/ac0.py &amp;&amp; python integrations/bloomberg/auth/dapi_check.py</invocation><expect>BEFORE any call: the module defaults printed (SECURITY "BABA US Equity", SEC_KEY "BABA_US_Equity", start 2016-01-01, end 2025-12-31 at the cut); the SIZED line "2 requests, 2 points, 1 unique security"; the credential fingerprint line, never a value; then dapi_check prints an UP line and exits 0. A DOWN line is a STOP with a BLOCKING row naming the surface</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-117"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r117/ac1.py</invocation><expect>READ-ONLY baseline: "histdata_daily_px total 1 for_992 0" at the cut (a drifted count is RECORDED, not a fail); pre.json written; and "served_readers_of_histdata_daily_px_under_lib 0" -- if that count is NOT 0, STOP with a BLOCKING row, because the cell's no-pair premise would be false</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-117"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest integrations/bloomberg/research/tests/test_daily_px_args.py -v -p no:cacheprovider 2&gt;&amp;1 | tail -8</invocation><expect>LIMB 1, code only, NO Bloomberg call: "3 passed" and 0 failed, with test_defaults_are_baba_unchanged, test_security_and_sec_key_override and test_no_blp_import_at_parse PASSED</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-117"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python integrations/bloomberg/research/pull_baba_daily_px.py --security "992 HK Equity" 2&gt;&amp;1 | tee .scratch/r117/ac3_out.txt</invocation><expect>LIVE, ledger OPEN before it, the ONE pull: a "PULL DAILY PX: 992 HK Equity -&gt; N rows landed at s3://opal-data-harvest/bloomberg/harvest/bronze/histdata_daily_px/security_key=992_HK_Equity/&lt;stamp&gt;.json" line with N &gt; 0, then the RAW KEY and STAMP lines. The security named MUST be 992 HK Equity and never BABA. A BLOCKED line (health not ok) is a STOP with a row, never a retry</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-117"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r117/ac4.py</invocation><expect>"total pre 1 post 2 added 1" with the added key under security_key=992_HK_Equity; "for_992 pre 0 post 1"; "added_all_under_992 True"; and the object itself carrying exactly the one security "992 HK Equity" with its DAILY row count and first/last dates printed. An object under any other security_key is a ROLLBACK trigger. Close the w1 leg and the entry on this read</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-117"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; git diff --name-only HEAD~1 HEAD -- integrations lib infra .tools portal &amp;&amp; grep -c "992 HK Equity" .scratch/r117/ac3_out.txt</invocation><expect>the changed code files are EXACTLY integrations/bloomberg/research/pull_baba_daily_px.py and integrations/bloomberg/research/tests/test_daily_px_args.py (no price_axis_pull.py, no model_block_pull.py); and the run output names 992 HK Equity at least once. Record the spend: 1 pull + 1 probe = 2 of 2 sized</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~117/AMGT_RESAPP.TO-AMGT-rk-117.lenovo-daily-price.proof_of_spec.json`,
grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5` (rc 0), flip the record face's
status to complete only if every criterion passes, commit, and report once. The report names: the SIZED line, the
dapi_check line, the PULL DAILY PX line with its row count, the added key, the pre/post counts, and the ledger entry
with its open and close.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
1. **The CTO's analysis called L-PX "SERVED (the DynamoDB rank rows), PAIR".** The measurement says otherwise: the
   rank rows come from `price_axis_pull.py`, which is **cohort-wide** (universe of 34 MEASURED tickers, 20 per
   request, one ranked generation with a `_CURRENT` pointer). A Lenovo-only rank row does not exist as an act, and
   running the ranker would rewrite every name's served rows -- far outside Lenovo's blast radius and against
   Andrew's no-fleet-run word. So this cell is bronze-only and carries no pair, and **the served Lead Panel price
   surface for Lenovo is an OPEN QUESTION for the CTO** (decomposition s.38).
2. **Limb 1 is needed because the only dense-price producer is BABA-hardcoded** with no arguments at all. The
   generalisation keeps every default, so BABA's own behaviour is untouched.
3. **Stage 11's "price" is therefore partially served by this cell:** the dense series lands, and the Lead Panel row
   does not. The trial report must say so rather than reading stage 11 as SERVED.

<status>pending</status>
<round>30</round>
<slot>~117</slot>
<fabric>site-z</fabric>
