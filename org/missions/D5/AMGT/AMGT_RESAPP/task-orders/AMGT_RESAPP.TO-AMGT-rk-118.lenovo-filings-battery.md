# AMGT_RESAPP task order -- `AMGT-rk-118` -- L-FIL: the filings battery for Lenovo `992_HK_Equity`, ISSUER-SITE ONLY (no HKEX, no ESEF), crawl at most 40 pages, `--write-bronze --write-pool`; it writes the SERVED `filing_attempt` / `filing_source` and issuer-site bronze under a never-widen pair -- CHAINED after `AMGT-rk-121`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-118</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~118</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one manual battery run; no cron, alarm, monitor or cadence is armed or read.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant moves; the S3 writes run under the seat's existing
  credentials.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification; the declaration applies to the worker's
  deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~118`.** Work ONLY in the worktree named in your spawn prompt. First act: print
`git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that `org/`, `.tools/` and
`lib/research/filings/battery.py` exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~118;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL -- `AMGT-rk-118` (round 30, the Lenovo trial's wave 2, stage 3)

**The governing text, verbatim:**
- PRD v0.23 s.12, stage 3: *"filings | the battery's non-SEC routes: the issuer's own site and the HKEX filings the
  issuer publishes; ESEF does not apply (HK)"*. Lenovo's today-state: *"`filing_attempt` UNRESOLVED-SOURCE (not an SEC
  filer)"*.
- **CTO ruling msg 24257, which NARROWS that stage:** *"the trial's filings stage is CONFINED TO THE ISSUER'S OWN
  SITE. ... A document fetched from hkexnews.hk is the regulator route, and address() REFUSES it ('source hkex is not
  a systems.json key'). Under Rule 30, a builder refusal is a missing registry row, never a workaround. That row
  belongs to the registry lane on the other fabric. It is NOT routed from here; it is recorded as an OPEN ITEM for the
  trial report ... If Lenovo's own site does not carry the annual report, stage 3 ends UNRESOLVED with that reason,
  which is itself a trial finding."*
- Cap: *"issuer crawl | at most 40 pages."*

**PRECONDITION, checked by AC0: `AMGT-rk-121` is DRAINED into your base.** Without it
`keys_from_crosswalk("992_HK_Equity")` returns `web_address None`, Lenovo has no prior EDGAR seed and no exchange
listing template (`_exchange_listing_seed` -> `(None, "no exchange listing template for exchange 'HK'")`), so
**step 4 starts with ZERO seeds and refuses** -- an UNRESOLVED caused by our own staleness, not by the issuer's site.
AC0 proves the seed exists BEFORE anything is fetched.

**THE MEASURED STATE (issuer, read-only, 2026-09-22 ~18:5xZ; re-measure in AC1):**
- `amgt/harvest/state/filing_attempt/security_key=992_HK_Equity/`: **1** object, `UNRESOLVED-SOURCE.json`.
- `filings/v1/992_HK_Equity/`: **1** object, `UNRESOLVED-SOURCE.source.json`.
- `sec/harvest/bronze/filing/` and `issuer-site/harvest/bronze/document/`: **0** objects each (estate-wide).
- Lenovo's keys AFTER rk-121: `ticker_root "992"`, `exchange "HK"`, `cik 932477`, `web_address "www.lenovo.com"`,
  `legal_name "LENOVO GROUP LTD"`.

**THE ROUTES, and which may run.** `run_battery` walks steps 1-5 in order:
- **step 1 `edgar-ticker`** -- an EDGAR ticker-table lookup on `ticker_root "992"`. **PUBLIC SEC requests, no vendor
  word needed**, and it is the producer's own ordered path; it will almost certainly not match a HK ticker root and
  will record an attempt. It is NOT the regulator route the CTO excluded.
- **step 2 `edgar-bloomberg-cik`** -- runs only when `keys["cik"]` is set. After rk-121 Lenovo HAS a CIK (932477), so
  **this step WILL run** and fetch that CIK's EDGAR filing index. **RECORD what it finds.** If it RESOLVES, stage 3
  resolves on an EDGAR document rather than the issuer's site: that is a TRIAL FINDING, not a violation (EDGAR is
  public and is the producer's own route), and you record it plainly in your report and in a row.
- **step 3 `esef-lei`** -- does not apply (HK); record its attempt.
- **step 4 `company-site`** -- the issuer's own site, seeded from `www.lenovo.com`, **max_pages 40** (the code
  default; there is no CLI flag, so AC0 prints it from the source).
- **step 5** -- the national regulator. **It must NOT fetch hkexnews.** Record its attempt; if it would fetch a
  regulator document, STOP with a BLOCKING row naming the CTO's ruling.
- **`--no-site-crawl` is NEVER passed** (it would disable the very step this stage is about).

**THE SIZED ACT (public sources only -- no vendor word is spent by this cell):**
`python -m lib.research.filings.battery --security-key 992_HK_Equity --write-bronze --write-pool --cache-dir .scratch/r118/cache --out-dir .scratch/r118/out`
- Ceiling: 1 SEC ticker-table fetch + at most 1 EDGAR index + at most 1 EDGAR document + **at most 40** issuer-site
  pages + the documents the crawl accepts. Print the ceiling BEFORE the run.
- **ONE invocation. Never re-run it**, save the single transient-failure allowance in section 4.

It writes:
- (W1) `sec/harvest/bronze/company_tickers/<date partition>/company_tickers.json` (rk-98's sink, FIRST for the estate
  if step 1 runs);
- (W2) `sec/harvest/bronze/filing/...` if step 2 fetches a document;
- (W3) `issuer-site/harvest/bronze/document/...` for EVERY step-4 candidate document the crawl checks (rk-98's ruled
  behaviour, not only the winner);
- (W4) **SERVED:** `amgt/harvest/state/filing_attempt/security_key=992_HK_Equity/UNRESOLVED-SOURCE.json` -- only on an
  UNRESOLVED outcome, and subject to rk-105's SKIP-HELD / CHANGED-HELD rules against the existing object;
- (W5) **SERVED:** `filings/v1/992_HK_Equity/...` and the `filing_source` silver on a RESOLVED outcome.

## 2. WHERE THIS CAME FROM

ROUND 30, decomposition s.38 (cut by `2.0.0_SA_COO~Z`), on the CTO's round-29 analysis msg 24328, its stage-3 ruling
msg 24257, and PRD v0.23 s.12.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~118/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-118.lenovo-filings-battery.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- **Every code file is a WALL** -- this cell changes NO code (rk-121 already did). Scratch is
  `<worktree>/.scratch/r118/`, including the crawl cache and out-dir, and is never committed.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~118 <0.9.0_WK_AMGT_RESAPP~118@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **THE PAIR:** both halves `ledger/NEVER_WIDEN_ROUND30_RK118_{COO,CTO}_HALF.md` must be SIGNED before you spawn
  (AC0 checks).
- **ISSUER SITE ONLY, and the hkexnews line is hard:** if any step would fetch `hkexnews.hk` (or any host the
  `address()` builder has no systems.json source for), STOP with a BLOCKING row quoting msg 24257. Rule 30: a builder
  refusal is a missing registry row, never a workaround.
- **rk-105's semantics apply to (W4):** an UNCHANGED unresolved outcome prints SKIP-HELD and writes nothing; a CHANGED
  outcome prints CHANGED-HELD with the differing field, writes nothing for that key, and the run exits non-zero with a
  summary. **A CHANGED-HELD is NOT a failure of this cell** -- it is the recorded truth that Lenovo's outcome moved;
  grade it and report it.
- **ONE run.** One transient network failure (a timeout or a 5xx from SEC or the issuer's site) allows **ONE** re-run
  of the process; a second failure is RECORDED, never looped (the CTO's standing rule, msg 24213).
- **Deploy ledger:** open it AFTER AC1 and BEFORE AC2:
  `python .tools/deploy_ledger.py open --slug amgt-rk118-lenovo-filings --title "<title>" --author "0.9.0_WK_AMGT_RESAPP~118" --leg "w4|s3-key|opal-data-harvest/amgt/harvest/state/filing_attempt/security_key=992_HK_Equity/UNRESOLVED-SOURCE.json|AC3" --leg "w5|s3-prefix|opal-data-harvest/filings/v1/992_HK_Equity/|AC3" --leg "w3|s3-prefix|opal-data-harvest/issuer-site/harvest/bronze/document/|AC4" --leg "v|verify|served thesis route for 992|AC5"`
  Close each leg on its read, then the entry.
- **ROLLBACK (any one trigger):** AC3 finds a `filing_attempt` or `filings/v1` object written under ANY security_key
  other than `992_HK_Equity`; or AC4 finds bronze written under another security; or AC5 finds the served thesis route
  for a CONTROL name (CAT) no longer 200.
  **NEVER A DELETE.** Every key here is either immutable (bronze) or write-once-per-outcome (`filing_attempt`, which
  refuses an overwrite by contract). A wrong object is LEFT, recorded in a row, and superseded only by a corrected
  write the issuer authorises. The ledger entry stays OPEN until the row names the served state.
- **No other write:** no Bloomberg call, no Lusha, no SA, no crosswalk, no model block, no portal, no IAM.
- **THE REFUSAL CLAUSE** applies. **SURPRISE ROWS:** `AMGT_RESAPP-Z-W118-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (literal; timeout 900)

**Grading order:** AC0, AC1, (open the ledger), AC2, AC3, AC4, AC5, (close the ledger).

`.scratch/r118/ac0.py`:
```
import inspect, json, os, sys
sys.path.insert(0, ".")
from lib.research.filings import battery
L = "org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND30_RK118_%s_HALF.md"
print("pair_coo", os.path.exists(L % "COO"), "pair_cto", os.path.exists(L % "CTO"))
k = battery.keys_from_crosswalk("992_HK_Equity")
print("keys", json.dumps({x: k.get(x) for x in ("ticker_root", "exchange", "cik", "web_address", "legal_name")}, default=str))
print("precursor_rk121_applied", bool(k.get("web_address")))
sig = inspect.signature(battery._step4_company_site)
print("max_pages_default", sig.parameters["max_pages"].default, "max_depth", sig.parameters["max_depth"].default, "delay", sig.parameters["delay"].default)
print("exchange_listing_seed", battery._exchange_listing_seed(k))
print("CEILING: 1 SEC ticker table + <=1 EDGAR index + <=1 EDGAR document + <=%d issuer-site pages; 0 vendor-word calls" % sig.parameters["max_pages"].default)
```

`.scratch/r118/ac1.py`:
```
import boto3, json
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
def ls(p): return sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
pre = {
  "filing_attempt_992": ls("amgt/harvest/state/filing_attempt/security_key=992_HK_Equity/"),
  "filings_v1_992": ls("filings/v1/992_HK_Equity/"),
  "filing_attempt_all": ls("amgt/harvest/state/filing_attempt/"),
  "filings_v1_all": ls("filings/v1/"),
  "sec_filing_bronze": ls("sec/harvest/bronze/filing/"),
  "issuer_doc_bronze": ls("issuer-site/harvest/bronze/document/"),
  "company_tickers": ls("sec/harvest/bronze/company_tickers/"),
}
for k, v in pre.items():
    print("pre", k, len(v))
body = None
if pre["filing_attempt_992"]:
    body = json.loads(s3.get_object(Bucket=B, Key=pre["filing_attempt_992"][0])["Body"].read())
    print("pre 992 attempt status", body.get("status"), "reason", str(body.get("reason"))[:120])
pre["attempt_body"] = body
json.dump(pre, open(".scratch/r118/pre.json", "w"), indent=1, default=str)
```

`.scratch/r118/ac3.py`:
```
import boto3, json
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
pre = json.load(open(".scratch/r118/pre.json"))
def ls(p): return sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
for name, prefix in (("filing_attempt_all", "amgt/harvest/state/filing_attempt/"), ("filings_v1_all", "filings/v1/")):
    post = ls(prefix)
    added = [k for k in post if k not in pre[name]]
    foreign = [k for k in added if "992_HK_Equity" not in k]
    print(name, "pre", len(pre[name]), "post", len(post), "added", len(added), "foreign", len(foreign), foreign[:3])
a992 = ls("amgt/harvest/state/filing_attempt/security_key=992_HK_Equity/")
f992 = ls("filings/v1/992_HK_Equity/")
print("992 filing_attempt", len(a992), "filings_v1", len(f992), f992)
for k in f992:
    d = json.loads(s3.get_object(Bucket=B, Key=k)["Body"].read())
    print("  ", k, "status", d.get("status"), "url", str(d.get("url"))[:120], "form", d.get("form"))
if a992:
    d = json.loads(s3.get_object(Bucket=B, Key=a992[0])["Body"].read())
    b = (d.get("battery") or {})
    print("attempt status", d.get("status"), "winner", b.get("winner"))
    for at in (b.get("attempts") or []):
        print("   step", at.get("step"), at.get("route"), "http", at.get("http_status"), "reason", str(at.get("reason"))[:110])
```

`.scratch/r118/ac4.py`:
```
import boto3, json
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
pre = json.load(open(".scratch/r118/pre.json"))
def ls(p): return sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
for name, prefix in (("sec_filing_bronze", "sec/harvest/bronze/filing/"), ("issuer_doc_bronze", "issuer-site/harvest/bronze/document/"), ("company_tickers", "sec/harvest/bronze/company_tickers/")):
    post = ls(prefix)
    added = [k for k in post if k not in pre[name]]
    print(name, "pre", len(pre[name]), "post", len(post), "added", len(added), added[:4])
hosts = set()
for k in ls("issuer-site/harvest/bronze/document/"):
    hosts.add(k.split("/")[3] if len(k.split("/")) > 3 else k)
print("issuer_doc partitions", sorted(hosts)[:8])
```

`.scratch/r118/ac5.py`:
```
import base64, boto3, json
lam = boto3.client("lambda", region_name="us-east-1")
def call(key):
    ev = {"rawPath": "/api/scoped/amgt/security/%s/thesis" % key, "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
    r = lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode())
    b = json.loads(r["Payload"].read() or b"{}")
    body = json.loads(b.get("body") or "{}") if b.get("statusCode") == 200 else {}
    print("thesis", key, "->", b.get("statusCode"), "FE", r.get("FunctionError"), "drafting_status", body.get("drafting_status"), "drafting_reason", str(body.get("drafting_reason"))[:140])
for k in ("992_HK_Equity", "CAT_US_Equity"):
    call(k)
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-118"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r118/ac0.py</invocation><expect>BEFORE any fetch: "pair_coo True pair_cto True"; the keys line showing cik 932477, web_address www.lenovo.com and legal_name LENOVO GROUP LTD; "precursor_rk121_applied True" -- a False here is a STOP with a BLOCKING row, because the crawl would have zero seeds; "max_pages_default 40"; the exchange-listing seed reading (None, "no exchange listing template for exchange 'HK'"); and the CEILING line. Record every value</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-118"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r118/ac1.py</invocation><expect>READ-ONLY baselines, each recorded as the bar its AC3/AC4 counterpart is written against: at the cut filing_attempt_992 1, filings_v1_992 1, sec_filing_bronze 0, issuer_doc_bronze 0, company_tickers 0, with the estate-wide counts too; and the pre 992 attempt printed with its status UNRESOLVED-SOURCE and its reason. pre.json written</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-118"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m lib.research.filings.battery --security-key 992_HK_Equity --write-bronze --write-pool --cache-dir .scratch/r118/cache --out-dir .scratch/r118/out 2&gt;&amp;1 | tee .scratch/r118/ac2_out.txt</invocation><expect>LIVE, ledger OPEN before it, ONE invocation. Either a RESOLVED line naming the winning route and document, or an "UNRESOLVED-SOURCE: 992_HK_Equity -- &lt;reason&gt;" line; plus the pool line (OK: uploaded, or rk-105's "SKIP-HELD: ... (unchanged UNRESOLVED outcome; held object kept)", or "CHANGED-HELD: 992_HK_Equity &lt;differing field&gt;" with the run returning 2). EVERY outcome is a graded result, not a failure. If any line shows a fetch of hkexnews.hk, STOP with a BLOCKING row quoting msg 24257</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-118"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r118/ac3.py</invocation><expect>"foreign 0" for BOTH filing_attempt and filings/v1 -- nothing was written under any security_key but 992_HK_Equity (a foreign key is a ROLLBACK trigger); the 992 counts against AC1's; and the attempt's own step-by-step table printed: step 1 edgar-ticker, step 2 edgar-bloomberg-cik (which NOW runs, because rk-121 supplies cik 932477 -- record what it found), step 3 esef-lei not applicable, step 4 company-site with its reason, step 5 regulator. Close the w4 and w5 legs</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-118"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r118/ac4.py</invocation><expect>the three bronze prefixes with pre/post/added; every added key belongs to this run (company_tickers 0 -&gt; 1 if step 1 ran; issuer_doc_bronze 0 -&gt; N for the step-4 candidates the crawl checked, per rk-98's ruled behaviour). The issuer_doc partitions are printed so a foreign security's partition is visible. Close the w3 leg</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-118"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r118/ac5.py</invocation><expect>the served thesis route for 992_HK_Equity returns 200, and the CONTROL CAT_US_Equity also returns 200 (a control regression is a ROLLBACK trigger). Lenovo's drafting_status and drafting_reason are printed -- if the outcome is still UNRESOLVED, the reason is the trial finding; if it RESOLVED, note that the adapter still serves the OLD reason until the supersede reader cell lands (Z-S225's sibling, carried by the CTO at round 27). Close the verify leg and the entry</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~118/AMGT_RESAPP.TO-AMGT-rk-118.lenovo-filings-battery.proof_of_spec.json`,
grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5` (rc 0), flip the record face's
status to complete only if every criterion passes, commit, and report once. The report names: the CEILING line, the
battery's outcome line, the five step attempts with their reasons, the added bronze counts, the served thesis states
for Lenovo and the control, and the ledger entry with its open and close.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
1. **Step 2 will now run, and that is new.** rk-121 supplies Lenovo's CIK (932477), so the EDGAR-by-CIK route is live
   for a name the PRD calls "not an SEC filer". EDGAR is public and is the producer's own ordered route, so it is not
   a scope breach -- but if it RESOLVES, stage 3 resolves on EDGAR rather than the issuer's site, which is a finding
   the trial report must carry. The issuer flagged it to the CTO at the cut.
2. **hkexnews stays excluded** by msg 24257, and the measurement says nothing pulls it in by accident: HK has no
   `EXCHANGE_LISTING_PAGES` template, so no exchange seed is produced.
3. **rk-98's ruled bronze behaviour** stores EVERY step-4 candidate document, not only the winner, so
   `issuer_doc_bronze` may add several objects for one crawl. That is expected and is why AC4 prints the count rather
   than asserting 1.

<status>pending</status>
<round>30</round>
<slot>~118</slot>
<fabric>site-z</fabric>
