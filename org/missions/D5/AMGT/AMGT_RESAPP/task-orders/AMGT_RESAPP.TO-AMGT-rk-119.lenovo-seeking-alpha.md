# AMGT_RESAPP task order -- `AMGT-rk-119` -- L-SA: the Seeking Alpha pull for Lenovo's ADR line, at most 10 calls, on the PARKED session through the Bright Data proxy -- AC0 REFUSES the run unless the ADR symbol and the session are BOTH measured, never guessed; bronze plus SA silver, no served reader, NO pair

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-119</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~119</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one manual run; no cron, alarm, monitor or cadence is armed or read.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant moves. The session bundle and proxy credentials are READ
  from Secrets Manager by the producer itself, under the seat's existing credentials.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification; the declaration applies to the worker's
  deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~119`.** Work ONLY in the worktree named in your spawn prompt. First act: print
`git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that `org/`, `.tools/` and
`integrations/seekingalpha/rest_fetch.py` exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~119;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`. **NEVER run `sa_harvest_session.py`** -- a re-harvest is an attended
act, not yours. **Never print a credential or a cookie value.**

## 1. THE CELL -- `AMGT-rk-119` (round 30, the Lenovo trial's wave 2, stages 7 and 9's SA half)

**The governing text, verbatim:**
- PRD v0.23 s.12: stage 7 *"peers | the SA peer set via the ADR line, where `C-PEER-SET-SA` can be met; otherwise the
  ranker, recorded as the fallback"*; stage 9 *"chatter and news | ... SA news on the ADR line"*.
- Caps: *"Seeking Alpha | at most 10 calls"*, and the two words Andrew's trial record names (Seeking Alpha AND Bright
  Data, because the client egresses through the residential proxy).
- CTO msg 24261 Q4 (the pair rule): a pair binds at a SERVED read. SA silver has no served reader today, so this cell
  carries NO pair.

**THE TWO THINGS THAT MUST BE MEASURED BEFORE ANY CALL -- this is the whole point of AC0:**
1. **The ADR symbol.** `run_ticker` fetches `/api/v3/symbols/<ticker>`; there is NO search endpoint in the producer,
   so the symbol is an INPUT. The issuer measured: **0 of 96 crosswalk records carry an `sa_symbol`**, and
   `model_block_pull._crosswalk_sa_symbol` would return None for Lenovo. Every prior SA fetch in the estate was a US
   primary listing (BABA, BA, COST; 38 bronze objects, **0 for 992**). **Lenovo's ADR symbol is NOT measured
   anywhere in this estate.** You do not guess it -- not from a ticker convention, not from memory, not from a
   plausible OTC form.
2. **The parked session's age.** The issuer measured `seeking-alpha/session` (Secrets Manager) `LastChangedDate`
   **2026-09-10T22:13:40-04:00**, i.e. **~11.7 days** old at the cut. The producer rides that bundle and never signs
   in; a stale bundle ends the run at the FIRST GET with `REHARVEST_NEEDED`.

**RULED, the refusal:** if AC0 cannot name the ADR symbol from a MEASURED source inside this repo or Opal's own
storage, **REFUSE the run**: file the row, record stage 7's SA half and stage 9's SA half as UNRESOLVED with that
reason, and STOP. That is a trial finding (the crosswalk has no `sa_symbol` field at all), and it costs nothing.
**Spending a word on a guessed symbol is the failure this cell exists to avoid** -- a wrong symbol enriches the wrong
company and burns both words.

**MEASURED SOURCES you MAY read for the symbol (read-only, no egress):** the crosswalk record's `identity` and
`association_keys`; `lib/research/identity/registrations.json`; the SA bronze already landed
(`seeking-alpha/harvest/bronze/`, 38 objects) and the SA silver `symbol_profile`; `integrations/seekingalpha/config.json`;
the model block's `forecast_fallback` block (which records `sa_symbol` when the fallback ran). If one of these names
Lenovo's SA symbol, USE IT and cite the source in your report.

**THE SIZED RUN, printed by AC0 before any call, and only if the refusal above does not fire:**
`run_ticker` walks: symbol -> report -> analysis listing -> news listing -> at most 2 articles. **At most 6 GETs for
one ticker, against the cap of 10.** Print the planned sequence and the cap BEFORE the run.

**THE ACT (one command):**
`python integrations/seekingalpha/rest_fetch.py run-ticker <MEASURED_SA_SYMBOL> --security-key 992_HK_Equity --state-dir .scratch/r119/state`

It writes:
- (W1) bronze under `seeking-alpha/harvest/bronze/{symbol,report,analysis,news,article}/security_key=992_HK_Equity/...`
  (immutable, through rk-92's `land_harvest`);
- (W2) **SILVER** `seeking-alpha/harvest/silver/symbol_profile/` and `.../news_item/` rows (`store.silver_append`).
  **The cell is NOT bronze-only** -- the producer writes these rows itself. Neither table has a served reader today,
  which is why there is no pair; if your AC1 finds one, STOP with a BLOCKING row;
- (W3) `packs/992_HK_Equity/input_ledger.json` -- **READ-MODIFY-WRITE, +1 entry** (`ledger.record_run`);
- (W4) the local state dir under your scratch (never committed).

## 2. WHERE THIS CAME FROM

ROUND 30, decomposition s.38 (cut by `2.0.0_SA_COO~Z`), on the CTO's round-29 analysis msg 24328 and PRD v0.23 s.12.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~119/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-119.lenovo-seeking-alpha.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- **Every code file is a WALL**, including `rest_fetch.py`, `sa_harvest_session.py` and
  `integrations/seekingalpha/config.json`. Scratch is `<worktree>/.scratch/r119/`.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~119 <0.9.0_WK_AMGT_RESAPP~119@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **NO PAIR**, because no served reader exists for SA bronze or SA silver (CTO msg 24261 Q4). AC1 re-measures that; a
  served reader is a STOP.
- **TWO WORDS ARE REQUIRED** (Seeking Alpha AND Bright Data, per Andrew's trial record). AC0 reads the recorded word
  and REFUSES if either is absent or narrower than this run. **Availability is not authorization.**
- **THE CAP IS 10 GETs, and the planned sequence is at most 6.** Count them from the producer's own state file and
  print the count. Exceeding the cap is a STOP.
- **ONE run, never retried.** `REHARVEST_NEEDED` or `AUTH_FAIL` ends the run: record it, file the row, and STOP. **Do
  not re-run and do not sign in.** A stale session is a trial finding and an attended re-harvest for the issuer.
- **CONCURRENCY:** (W3) `packs/992_HK_Equity/input_ledger.json` is a READ-MODIFY-WRITE append shared with
  `AMGT-rk-116` (L-MB). **This cell is spawned only after rk-116's pull has landed**; the issuer enforces the order.
  If you see a ledger entry you did not write appear mid-run, record it in a row.
- **Deploy ledger:** open it AFTER AC1 and BEFORE AC2:
  `python .tools/deploy_ledger.py open --slug amgt-rk119-lenovo-sa --title "<title>" --author "0.9.0_WK_AMGT_RESAPP~119" --leg "w1|s3-prefix|opal-data-harvest/seeking-alpha/harvest/bronze/|AC3" --leg "w2|s3-prefix|opal-data-harvest/seeking-alpha/harvest/silver/|AC3" --leg "w3|s3-key|opal-data-harvest/packs/992_HK_Equity/input_ledger.json|AC3"`
  Close each leg on its read, then the entry. If AC0 refuses the run, the ledger is NEVER opened.
- **ROLLBACK (any one trigger):** AC3 finds bronze or silver written under any `security_key` other than
  `992_HK_Equity`; or the entity check shows the fetched symbol is a DIFFERENT company (rk-111's `companyName` check
  is the instrument).
  **NEVER A DELETE:** bronze is immutable and silver is append-only, so a wrong-company row is LEFT, recorded in a row
  with the measured evidence, and superseded only by an issuer-authorised correction. A wrong-company fetch is also a
  WORD incident: report it plainly.
- **No other write:** no Bloomberg call, no Lusha, no filings, no crosswalk, no model block, no portal, no IAM.
- **THE REFUSAL CLAUSE** applies. **SURPRISE ROWS:** `AMGT_RESAPP-Z-W119-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (literal; timeout 900)

**Grading order:** AC0 (which may REFUSE and end the cell), AC1, (open the ledger), AC2, AC3, (close the ledger).

`.scratch/r119/ac0.py`:
```
import boto3, datetime, json, os, sys
sys.path.insert(0, ".")
from lib.research.identity import crosswalk as cw
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
cfg = json.load(open("integrations/seekingalpha/config.json", encoding="utf-8"))
sm = boto3.client("secretsmanager", region_name=cfg["region"])
d = sm.describe_secret(SecretId=cfg["secrets"]["session_secret_name"])
lc = d["LastChangedDate"]
age = (datetime.datetime.now(lc.tzinfo) - lc).total_seconds() / 86400.0
print("session_secret", cfg["secrets"]["session_secret_name"], "last_changed", lc.isoformat(), "age_days %.2f" % age)
rec = cw.record_for("992_HK_Equity") or {}
ident = rec.get("identity") or {}
print("crosswalk_sa_symbol_field_present", "sa_symbol" in rec, "identity_keys", sorted(ident))
doc = cw._read_pool_latest() if hasattr(cw, "_read_pool_latest") else {}
recs = (doc or {}).get("records") or []
print("records", len(recs), "with_sa_symbol", sum(1 for r in recs if r.get("sa_symbol")))
def ls(p): return sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
sa = ls("seeking-alpha/harvest/bronze/")
print("sa_bronze_total", len(sa), "for_992", len([k for k in sa if "992_HK_Equity" in k]))
print("sa_bronze_securities", sorted({k.split("security_key=")[1].split("/")[0] for k in sa if "security_key=" in k}))
der = ls("derived/model_block/992_HK_Equity/")
sym = None
if der:
    mb = json.loads(s3.get_object(Bucket=B, Key=der[-1])["Body"].read())
    ff = mb.get("forecast_fallback") or {}
    sym = (ff.get("provenance") or {}).get("sa_symbol") if isinstance(ff, dict) else None
    print("model_block_forecast_fallback_sa_symbol", sym)
print("MEASURED_SA_SYMBOL", sym if sym else "NONE -- REFUSE THE RUN")
print("PLAN (only if a symbol was measured): symbol -> report -> analysis -> news -> <=2 articles = at most 6 GETs, cap 10")
```

`.scratch/r119/ac1.py`:
```
import boto3, json, os
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
def ls(p): return sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
pre = {"bronze": ls("seeking-alpha/harvest/bronze/"), "silver": ls("seeking-alpha/harvest/silver/")}
led = json.loads(s3.get_object(Bucket=B, Key="packs/992_HK_Equity/input_ledger.json")["Body"].read())
pre["ledger_entries"] = len(led["entries"])
json.dump(pre, open(".scratch/r119/pre.json", "w"), indent=1)
print("pre bronze", len(pre["bronze"]), "silver", len(pre["silver"]), "ledger_entries", pre["ledger_entries"])
hits = []
for root, dirs, files in os.walk("lib"):
    dirs[:] = [d for d in dirs if d not in ("tests", "__pycache__")]
    for f in files:
        if f.endswith(".py"):
            s = open(os.path.join(root, f), encoding="utf-8", errors="replace").read()
            if "seeking-alpha/harvest/silver" in s or "symbol_profile" in s:
                hits.append(os.path.join(root, f))
print("served_readers_of_sa_silver_under_lib", len(hits), hits)
```

`.scratch/r119/ac3.py`:
```
import boto3, json
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
pre = json.load(open(".scratch/r119/pre.json"))
def ls(p): return sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=p) for o in pg.get("Contents", []))
for name, prefix in (("bronze", "seeking-alpha/harvest/bronze/"), ("silver", "seeking-alpha/harvest/silver/")):
    post = ls(prefix)
    added = [k for k in post if k not in pre[name]]
    foreign = [k for k in added if "992_HK_Equity" not in k]
    print(name, "pre", len(pre[name]), "post", len(post), "added", len(added), "foreign", len(foreign), added[:4])
led = json.loads(s3.get_object(Bucket=B, Key="packs/992_HK_Equity/input_ledger.json")["Body"].read())
print("ledger pre", pre["ledger_entries"], "post", len(led["entries"]), "last", json.dumps(led["entries"][-1], default=str)[:200])
st = json.load(open(".scratch/r119/state/request_log.json")) if __import__("os").path.exists(".scratch/r119/state/request_log.json") else {}
reqs = st.get("requests") or []
print("GETs_made", len(reqs), "cap 10", "status", st.get("status"))
for r in reqs:
    print("   ", r.get("endpoint") or r.get("path"), r.get("status") or r.get("class"))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-119"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r119/ac0.py</invocation><expect>BEFORE any GET and before the ledger is opened: the session's last_changed and age_days (measured ~11.7 days at the cut -- RECORD it, and record that a stale bundle ends the run at the first GET); "records 96 with_sa_symbol 0"; "sa_bronze_total 38 for_992 0" with the securities list showing only US primary listings; and the decisive line "MEASURED_SA_SYMBOL ...". If it reads "NONE -- REFUSE THE RUN", the cell REFUSES: file the row, record stage 7's and stage 9's SA halves UNRESOLVED with that reason, open NO ledger, make NO call, and STOP -- that is a PASS of this criterion and the correct outcome, not a failure. Also record whether BOTH words (Seeking Alpha and Bright Data) are on file for this run; either absent is the same refusal</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-119"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r119/ac1.py</invocation><expect>Only reached if AC0 did not refuse. READ-ONLY baselines: bronze and silver counts (38 and its own count at the cut) and the input ledger's entry count, each recorded as the bar AC3 is written against; and "served_readers_of_sa_silver_under_lib 0" -- a non-zero is a STOP, because the no-pair premise would be false</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-119"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python integrations/seekingalpha/rest_fetch.py run-ticker "$SA_SYMBOL" --security-key 992_HK_Equity --state-dir .scratch/r119/state 2&gt;&amp;1 | tee .scratch/r119/ac2_out.txt</invocation><expect>LIVE, ledger OPEN before it, ONE run, where $SA_SYMBOL is the symbol AC0 MEASURED (never a guess). Either "OK: parked session captured_at=... egress=residential-proxy" followed by the landing lines, or a REHARVEST_NEEDED / AUTH_FAIL stop -- which is RECORDED with its row and never retried. The entity check (rk-111's companyName preference) decides whether the symbol is Lenovo: a different company is a ROLLBACK trigger and a word incident</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-119"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r119/ac3.py</invocation><expect>"foreign 0" for BOTH bronze and silver -- nothing landed under another security_key (a foreign key is a ROLLBACK trigger); the added counts against AC1's; the input ledger reads pre + 1; and "GETs_made N cap 10" with N at most 6, each endpoint listed. Close the three legs and the entry on this read</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~119/AMGT_RESAPP.TO-AMGT-rk-119.lenovo-seeking-alpha.proof_of_spec.json`,
grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3` (rc 0), flip the record face's status
to complete only if every criterion passes, commit, and report once. **If AC0 refused, say so on the first line**, name
the missing input, and report the session age -- the cell is complete on a refusal, with 0 GETs and 0 words spent.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
1. **The likely outcome is the REFUSAL**, and that is the correct result. 0 of 96 crosswalk records carry an
   `sa_symbol`; the field does not exist in the schema. Unless the model block's `forecast_fallback` recorded one for
   Lenovo, the symbol is unmeasured and no word should be spent. The trial report then carries "stage 7 / stage 9 SA
   half UNRESOLVED: no measured ADR symbol" as a finding, and the CTO decides whether resolving a symbol is worth its
   own carded act.
2. **The CTO's analysis called this cell "bronze only".** The measurement says `run_ticker` ALSO writes SA silver
   (`symbol_profile`, `news_item`) through `store.silver_append`. Neither has a served reader, so the no-pair ruling
   still holds -- but the order names the silver writes rather than claiming bronze-only.
3. **The session was ~11.7 days old at the cut** and its last successful landing was 2026-09-11, about 2 hours after
   capture. A REHARVEST_NEEDED stop is a likely second outcome, and it is an attended re-harvest for the issuer, never
   the worker.
4. **The input ledger is shared with rk-116**, so this cell is chained behind it.

<status>pending</status>
<round>30</round>
<slot>~119</slot>
<fabric>site-z</fabric>
