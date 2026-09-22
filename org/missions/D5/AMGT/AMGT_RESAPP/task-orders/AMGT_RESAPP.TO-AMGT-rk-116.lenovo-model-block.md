# AMGT_RESAPP task order -- `AMGT-rk-116` -- L-MB: the Bloomberg model-block PULL + DERIVE for Lenovo `992_HK_Equity` (5 requests on 1 security, sized and printed first), landing refdata/histdata/bestdata bronze and ONE new served `derived/model_block/992_HK_Equity/<stamp>/model_block.json` that carries rk-109's `fiscal_year_join` and rk-112's currency labels, under a never-widen pair

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-116</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~116</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two manual stages (pull, derive); no cron, alarm, monitor or cadence is
  armed or read.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant moves. Every write runs under the seat's existing S3
  credentials into `opal-data-harvest`.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification; the declaration applies to the worker's
  deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~116`.** Work ONLY in the worktree named in your spawn prompt. First act: print
`git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that `org/`, `.tools/`,
`integrations/bloomberg/research/model_block_pull.py` and `integrations/bloomberg/READ_HERE.md` exist; if any is absent,
STOP with a BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~116;`.
**NEVER RUN AN INSTALL.** Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.
**Never print a credential value.**

## 1. THE CELL -- `AMGT-rk-116` (round 30, the Lenovo trial's wave 2, stage 2)

**The governing text, verbatim:**
- PRD v0.23 s.12, stage 2: *"model block | Bloomberg refdata, histdata and bestdata; bronze then silver `model_block`;
  served block"*. Its measured today-state: *"refdata and histdata 09-16; 3 served blocks; no forecasts; silver not
  wired"*.
- PRD v0.23 s.12 precondition: *"Fiscal-year pairing. The model block for a 31 March year-end is graded only with the
  fiscal-year join wired (field map s.3 item 2, `fye_join.py`)."* And: *"Currency. The model block states Lenovo's
  reporting currency (USD) against its listing currency (HKD) on every per-share and valuation figure, and never mixes
  the two silently."*
- Cap: *"Bloomberg | 1 unique security."*
- CTO msg 24261 Q4: *"The READ_HERE two-phase sign-in check is each Bloomberg cell's AC0, and a refusal names the
  surface."*
- CTO msg 24300 / 24328, the blast radius this cell's pair must carry: *"L-MB's never-widen pair names Lenovo's served
  keys as its ENTIRE blast radius ... It states that 12 other names ... would change their block on any future derive ...
  It states that none is derived in this trial."*
- Andrew-direct @`6f1a72e4be`: *"The Bloomberg data quota binds every pull, and each pull is sized and printed before it
  runs."*

**PRECONDITIONS, checked by AC0:**
- rk-113 is drained: Lenovo's crosswalk record carries `identity` (composite FIGI `BBG000BG4QC6`). This cell does not
  read it, but the trial's stage order is identity first.
- rk-109 (`fye_join` wiring) and rk-112 (currency labels) are in your base. **Lenovo's FYE is 31 March, so the derive
  takes rk-109's NON-December path**, and the block must carry `fiscal_year_join` and per-figure currency labels.
- Both halves `ledger/NEVER_WIDEN_ROUND30_RK116_{COO,CTO}_HALF.md` are SIGNED.

**THE MEASURED STATE (issuer, read-only, 2026-09-22 ~18:5xZ; re-measure at your HEAD in AC0/AC1):**
- Bronze for `992_HK_Equity`: `refdata` **1** object, `histdata` **1**, `bestdata` **0**, `histdata_daily_px` **0**.
  The state `pull_log` for 992: **0** objects.
- `derived/model_block/992_HK_Equity/`: **3** stamps, newest `20260919T075318Z`.
- `packs/992_HK_Equity/input_ledger.json` exists with **1** entry (`market_data`, `bloomberg`, `OK`,
  stamp `20260916T201811Z`).
- `bestdata` 0 is why the served block carries **no forecasts**: `stage_derive`'s forecast figures come from the
  bestdata object this pull lands.

**THE SIZED PULL, printed by AC0 BEFORE any call. The real count is FIVE requests, not three:**
`stage_pull` (`model_block_pull.py:452-524`) sends, per security:
- 1 `ReferenceDataRequest` -- `992 HK Equity` x `HEADER_FIELDS` (**18** fields);
- 1 `HistoricalDataRequest` -- `992 HK Equity` x `HIST_FIELDS` (**23** fields), `2016-01-01`..rolling end, `YEARLY`;
- **3** `ReferenceDataRequest`s -- one per `FORECAST_OVERRIDES` member (`1FY`, `2FY`, `3FY`), each
  `FORECAST_FIELDS` + `BEST_PERIOD_END_DATE` (**6** fields). They land as ONE `bestdata.json`, which is why a
  "bestdata = 1 request" reading is wrong.
- **Cell total: 5 Bloomberg requests + 1 READ_HERE login probe = 6 requests, 60 security-field points, 1 unique
  security.** (59 points for the pull + 1 for the SPX probe.)
- **The pull's `--dry-run` makes NO Bloomberg call** (`cmd_pull` prints the plan and returns; `model_block_pull.py:1264-1292`),
  unlike `add_security`'s. So AC1 runs it and it is FREE.

**THE ACT, two commands in this order:**
1. `python -m integrations.bloomberg.research.model_block_pull pull --securities "992 HK Equity"`
2. `python -m integrations.bloomberg.research.model_block_pull derive --securities "992 HK Equity"`

It writes, in this order:
- (W1) `bloomberg/harvest/bronze/refdata/security_key=992_HK_Equity/<stamp>.json` (immutable);
- (W2) `bloomberg/harvest/bronze/histdata/security_key=992_HK_Equity/<stamp>.json` (immutable);
- (W3) `bloomberg/harvest/bronze/bestdata/security_key=992_HK_Equity/<stamp>.json` (immutable, FIRST ever for 992);
- (W4) `bloomberg/harvest/state/pull_log/security_key=992_HK_Equity/<stamp>.json` (immutable, FIRST ever for 992);
- (W5) `packs/992_HK_Equity/input_ledger.json` -- **READ-MODIFY-WRITE, +1 entry** (`ledger.record_run`);
- (W6) **SERVED:** `derived/model_block/992_HK_Equity/<derived stamp>/model_block.json` -- a NEW stamp; the three
  existing stamps are never touched.

## 2. WHERE THIS CAME FROM

ROUND 30, decomposition s.38 (cut by `2.0.0_SA_COO~Z`), on the CTO's round-29 analysis msg 24328 and PRD v0.23 s.12.
Wave 2, stage 2 of the Lenovo trial. rk-113 (identity) is its stage predecessor.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~116/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-116.lenovo-model-block.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- **Every code file is a WALL.** This cell changes NO code: it runs the producer as it stands. Scratch is
  `<worktree>/.scratch/r116/` (never committed).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~116 <0.9.0_WK_AMGT_RESAPP~116@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **THE PAIR:** both halves must be SIGNED before you spawn (AC0 checks). The pair's blast radius is Lenovo's keys
  only, and it STATES that 12 other non-December names (6861, 9433, CSL, COST, HD, NVDA, INTU, IMB, NG/, SSE, ST,
  ICICIBC) would move on their NEXT derive. **You derive NOTHING but 992.** Passing a second security to either
  command is a violation, and the producer itself refuses more than 3.
- **DAPI DOWN = STOP.** If AC0's probe reads DOWN, file a BLOCKING row naming the surface ("DAPI login state,
  READ_HERE s.2") and STOP. **You do NOT run the sign-in:** its submit phase spends one of a 2-attempt lockout budget
  and types a credential, so it is an attended act for the issuer.
- **CONCURRENCY, a real hazard this round:** (W5) `packs/992_HK_Equity/input_ledger.json` is a READ-MODIFY-WRITE
  append, and `AMGT-rk-119` (L-SA) writes the SAME key through the same `record_run`. **rk-119 is not spawned until
  this cell's AC2 has landed**, and the issuer enforces that; if you observe a ledger entry you did not write
  appearing between AC1 and AC3, file a row and record it.
- **ONE pull, never retried.** A Bloomberg error lands per the producer's own path; record it, do not re-run. A
  re-run spends the quota twice.
- **A field Bloomberg does not return** is recorded by the producer in the response it lands, NOT a failure of this
  cell.
- **Deploy ledger:** open it AFTER AC1 and BEFORE AC2:
  `python .tools/deploy_ledger.py open --slug amgt-rk116-lenovo-model-block --title "<title>" --author "0.9.0_WK_AMGT_RESAPP~116" --leg "w1|s3-prefix|opal-data-harvest/bloomberg/harvest/bronze/|AC3" --leg "w5|s3-key|opal-data-harvest/packs/992_HK_Equity/input_ledger.json|AC3" --leg "w6|s3-prefix|opal-data-harvest/derived/model_block/992_HK_Equity/|AC4" --leg "v|verify|served block reads fiscal_year_join + currency|AC5"`
  Close each leg on its read, then the entry. There is NO `--legs` flag.
- **ROLLBACK (any one trigger):** AC4 finds the new derived block absent, unreadable, or carrying a `security_key`
  other than `992_HK_Equity`; or AC4 finds any of the **3 pre-existing** derived stamps changed; or AC5 finds the
  block missing `fiscal_year_join` on a non-December FYE; or AC3 finds a bronze object written under any
  `security_key` other than `992_HK_Equity`.
- **WHICH ROLLBACK APPLIES -- NEVER A DELETE.** Every key here is immutable-by-construction except (W5):
  - (W1)-(W4), (W6): new stamped keys. A bad derive is superseded by a NEW derived stamp, never removed. The reader
    picks the latest stamp, so publishing a corrected stamp IS the rollback; if no corrected derive is possible, the
    entry stays OPEN and the row names the served state. **No S3 delete in any branch.**
  - (W5): re-append a correcting entry; the ledger only grows by contract, and an entry is never removed.
- **No other write:** no crosswalk, no filings, no Lusha, no SA, no portal, no IAM, no DynamoDB.
- **THE REFUSAL CLAUSE** applies: a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row,
  never repaired or widened.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W116-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (literal; timeout 900)

**Grading order:** AC0, AC1, (open the ledger), AC2, AC3, AC4, AC5, (close the ledger), AC6.

`.scratch/r116/ac0.py`:
```
import importlib.util, os, subprocess, sys
spec = importlib.util.spec_from_file_location("mbp", "integrations/bloomberg/research/model_block_pull.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
L = "org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND30_RK116_%s_HALF.md"
print("pair_coo", os.path.exists(L % "COO"), "pair_cto", os.path.exists(L % "CTO"))
print("fye_join_wired", hasattr(m, "_is_december_fye"), "currency_labels_wired", hasattr(m, "_figure_currency"))
reqs = 2 + len(m.FORECAST_OVERRIDES)
pts = len(m.HEADER_FIELDS) + len(m.HIST_FIELDS) + len(m.FORECAST_OVERRIDES) * (len(m.FORECAST_FIELDS) + 1)
print("SIZED: %d Bloomberg requests (1 refdata x %d fields, 1 histdata x %d fields, %d bestdata x %d fields) + 1 SPX login probe = %d total, %d points, 1 unique security"
      % (reqs, len(m.HEADER_FIELDS), len(m.HIST_FIELDS), len(m.FORECAST_OVERRIDES), len(m.FORECAST_FIELDS) + 1, reqs + 1, pts + 1))
print(subprocess.run([sys.executable, "integrations/bloomberg/auth/bbg_credentials.py", "--check"], capture_output=True, text=True).stdout.strip()[:300])
```

`.scratch/r116/ac1.py`:
```
import boto3, json, sys
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
def ls(p): return sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
pre = {}
for req in ("refdata", "histdata", "bestdata"):
    pre[req] = ls("bloomberg/harvest/bronze/%s/security_key=992_HK_Equity/" % req)
pre["pull_log"] = ls("bloomberg/harvest/state/pull_log/security_key=992_HK_Equity/")
pre["derived"] = ls("derived/model_block/992_HK_Equity/")
led = json.loads(s3.get_object(Bucket=B, Key="packs/992_HK_Equity/input_ledger.json")["Body"].read())
pre["ledger_entries"] = len(led["entries"])
json.dump(pre, open(".scratch/r116/pre.json", "w"), indent=1)
for k, v in pre.items():
    print("pre", k, len(v) if isinstance(v, list) else v)
```

`.scratch/r116/ac3.py`:
```
import boto3, json
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
pre = json.load(open(".scratch/r116/pre.json"))
def ls(p): return sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
for req in ("refdata", "histdata", "bestdata"):
    post = ls("bloomberg/harvest/bronze/%s/security_key=992_HK_Equity/" % req)
    added = [k for k in post if k not in pre[req]]
    print("bronze", req, "pre", len(pre[req]), "post", len(post), "added", len(added), added[-1:] )
pl = ls("bloomberg/harvest/state/pull_log/security_key=992_HK_Equity/")
print("pull_log pre", len(pre["pull_log"]), "post", len(pl), "added", len([k for k in pl if k not in pre["pull_log"]]))
allb = ls("bloomberg/harvest/bronze/")
foreign = [k for k in allb if "security_key=992_HK_Equity" not in k and k not in sum((pre[r] for r in ("refdata","histdata","bestdata")), [])]
print("bronze_keys_total", len(allb), "note: foreign-key count is informational, compared in AC6")
led = json.loads(s3.get_object(Bucket=B, Key="packs/992_HK_Equity/input_ledger.json")["Body"].read())
print("ledger_entries pre", pre["ledger_entries"], "post", len(led["entries"]), "last", json.dumps(led["entries"][-1], default=str)[:200])
```

`.scratch/r116/ac4.py`:
```
import boto3, json
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
pre = json.load(open(".scratch/r116/pre.json"))
def ls(p): return sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
post = ls("derived/model_block/992_HK_Equity/")
added = [k for k in post if k not in pre["derived"]]
print("derived pre", len(pre["derived"]), "post", len(post), "added", len(added), added)
import hashlib
for k in pre["derived"]:
    b = s3.get_object(Bucket=B, Key=k)["Body"].read()
    print("pre-existing stamp UNCHANGED?", k, "sha256", hashlib.sha256(b).hexdigest()[:16])
doc = json.loads(s3.get_object(Bucket=B, Key=added[-1])["Body"].read())
print("security_key", doc.get("security_key"), "figures", len(doc.get("figures") or []), "unresolved", len(doc.get("unresolved") or []))
json.dump({"key": added[-1]}, open(".scratch/r116/post.json", "w"))
```

`.scratch/r116/ac5.py`:
```
import boto3, json
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
key = json.load(open(".scratch/r116/post.json"))["key"]
doc = json.loads(s3.get_object(Bucket=B, Key=key)["Body"].read())
fyj = doc.get("fiscal_year_join")
print("fiscal_year_join", json.dumps(fyj, default=str) if fyj else "ABSENT")
print("currencies", json.dumps(doc.get("currencies"), default=str))
figs = doc.get("figures") or []
labelled = [f for f in figs if "currency_basis" in f]
bases = sorted({f.get("currency_basis") for f in labelled})
print("figures", len(figs), "with currency_basis", len(labelled), "bases", bases)
px = [f for f in figs if f.get("mnemonic") == "PX_LAST"]
print("PX_LAST figures", len(px), "sample", json.dumps(px[:1], default=str)[:300])
fy = sorted({f.get("fiscal_year") for f in figs if f.get("scope") == "fiscal_year_line_item"})
print("fiscal_years", fy)
fc = [f for f in figs if str(f.get("mnemonic","")).startswith("BEST_")]
print("forecast figures", len(fc), "periods", sorted({f.get("fiscal_year") for f in fc}))
```

`.scratch/r116/ac6.py`:
```
import re
text = open(".scratch/r116/ac2_pull.txt", encoding="utf-8", errors="replace").read()
hits = re.findall(r"PULL: .* -> raw stamp (\S+)", text)
print("pull_lines", len(hits), "stamps", hits)
print("securities_named", sorted(set(re.findall(r"PULL: (.+?) ->", text))))
print("requests_spent 5 probe 1 total 6 sized_total 6")
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-116"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r116/ac0.py &amp;&amp; python integrations/bloomberg/auth/dapi_check.py</invocation><expect>BEFORE any call: "pair_coo True pair_cto True"; "fye_join_wired True currency_labels_wired True"; the SIZED line reading "5 Bloomberg requests (1 refdata x 18 fields, 1 histdata x 23 fields, 3 bestdata x 6 fields) + 1 SPX login probe = 6 total, 60 points, 1 unique security" (re-measured from the module, not typed); the credential check's fingerprint line, never a value; then dapi_check prints an UP line and exits 0. A DOWN line is a STOP with a BLOCKING row naming the surface -- no sign-in is attempted</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-116"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r116/ac1.py &amp;&amp; python -m integrations.bloomberg.research.model_block_pull pull --securities "992 HK Equity" --dry-run</invocation><expect>READ-ONLY (the dry run makes NO Bloomberg call, model_block_pull.py:1264-1292). The pre-counts, each recorded as the baseline every later bar is written against: measured at the cut refdata 1, histdata 1, bestdata 0, pull_log 0, derived 3, ledger_entries 1 -- a drifted count is RECORDED, not a fail. Then five DRY-RUN PULL lines naming exactly one security, 992 HK Equity, and the four keys it would write. pre.json written</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-116"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m integrations.bloomberg.research.model_block_pull pull --securities "992 HK Equity" 2&gt;&amp;1 | tee .scratch/r116/ac2_pull.txt &amp;&amp; python -m integrations.bloomberg.research.model_block_pull derive --securities "992 HK Equity" 2&gt;&amp;1 | tee .scratch/r116/ac2_derive.txt</invocation><expect>LIVE, ledger OPEN before it. The pull prints "PULL: 992 HK Equity -> raw stamp &lt;stamp&gt; (...refdata..., ...histdata..., ...pull_log...)" then "PULL DONE: 1 of 1 securities landed raw". The derive prints "DERIVE: 992 HK Equity -> derived stamp &lt;stamp&gt; (N FY rows, M figures, K unresolved)" then "DERIVE DONE: 1 of 1". Exactly ONE security is named in both. A Bloomberg error is recorded and NEVER re-run</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-116"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r116/ac3.py</invocation><expect>Each bronze request reads post = pre + 1 with the added key under security_key=992_HK_Equity: refdata 1 -&gt; 2, histdata 1 -&gt; 2, and bestdata 0 -&gt; 1 (the FIRST bestdata object for Lenovo, which is what gives the block its forecasts). pull_log 0 -&gt; 1. The input ledger reads pre + 1 entry, whose last entry is this run's market_data record. Close the w1 and w5 legs on this read</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-116"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r116/ac4.py</invocation><expect>"derived pre 3 post 4 added 1" with the added key under derived/model_block/992_HK_Equity/; each of the 3 pre-existing stamps printed with its sha256 -- record them, they must be the SAME objects (a changed pre-existing stamp is a ROLLBACK trigger); the new document's "security_key 992_HK_Equity" with its figure and unresolved counts. Close the w6 leg</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-116"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r116/ac5.py</invocation><expect>THE PRECONDITION READ-BACK. "fiscal_year_join" is PRESENT (not ABSENT) and names the fiscal-period method with its max gap -- Lenovo's FYE is 31 March, so rk-109's non-December path must have run; an ABSENT here is a ROLLBACK trigger. "currencies" carries quote and reporting with "converted": false. Every figure carries currency_basis (with_currency_basis equals figures), and the bases are drawn from reporting/quote/invariant. The fiscal_years list and the forecast figures (from the new bestdata) are recorded with their counts. Close the verify leg and the ledger entry on this read</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-116"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r116/ac6.py</invocation><expect>"pull_lines 1" with one stamp, "securities_named ['992 HK Equity']" -- exactly one security was pulled -- and the spend line "requests_spent 5 probe 1 total 6 sized_total 6", equal to AC0's SIZED line</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~116/AMGT_RESAPP.TO-AMGT-rk-116.lenovo-model-block.proof_of_spec.json`,
grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5,AC6` (rc 0), flip the record
face's status to complete only if every criterion passes, commit, and report once. The report names: the SIZED line,
the dapi_check line, the pull and derive lines, the six write counts, the `fiscal_year_join` and `currencies` blocks,
the ledger entry path with its open and close, and the branch taken.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
1. **The request count is FIVE, not three.** The CTO's analysis said "3 requests"; `stage_pull` sends 1 refdata +
   1 histdata + 3 bestdata (one per `FORECAST_OVERRIDES` member), each an explicit `BEST_FPERIOD_OVERRIDE` per
   AMGT-rk-36's own rule. With the READ_HERE probe the cell spends 6. The plan's "7 Lenovo requests" budget is nearly
   consumed by this cell alone; the issuer flagged it to the CTO at the cut.
2. **`bestdata` is 0 for Lenovo today**, so this is the FIRST forecast pull for the name and the first served block
   that can carry forecast figures.
3. **The ledger key is shared with rk-119** (`packs/992_HK_Equity/input_ledger.json`, read-modify-write). The two
   cells are therefore NOT concurrency-safe together; the issuance chains rk-119 behind this cell.
4. **This cell changes no code.** rk-109 and rk-112 are already merged, so the non-December path and the currency
   labels are exercised LIVE for the first time here -- AC5 is the read-back that proves it.

<status>pending</status>
<round>30</round>
<slot>~116</slot>
<fabric>site-z</fabric>
