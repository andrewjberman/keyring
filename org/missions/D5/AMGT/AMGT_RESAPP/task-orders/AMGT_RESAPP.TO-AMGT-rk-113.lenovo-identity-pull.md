# AMGT_RESAPP task order -- `AMGT-rk-113` -- L-ID: the ONE Bloomberg identity pull for Lenovo `992_HK_Equity` (1 ReferenceDataRequest, 1 security, 9 fields, sized and printed first), which ENRICHES Lenovo's existing crosswalk record with its identity (composite FIGI, FIGI, ISIN, SEDOL, LEI, website) under a never-widen pair; the other 95 records byte-equal

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-113</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~113</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one manual pull; no cron, alarm, monitor or cadence is armed or read.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant moves. The writes run under the seat's existing S3
  credentials: one immutable identity bronze object and one crosswalk/v1/<today>.json pool object in opal-data-harvest.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification; the declaration applies to the worker's deliverable.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~113`.** Work ONLY in the worktree named in your spawn prompt. First act: print
`git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that `org/`, `.tools/`,
`lib/research/identity/add_security.py` and `integrations/bloomberg/READ_HERE.md` exist; if any is absent, STOP with a
BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~113;`. **NEVER RUN AN INSTALL.**
Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`. **Never print a credential.**

## 1. THE CELL -- `AMGT-rk-113` (round 29, the Lenovo trial's wave 1, stage 1)

**The governing text, verbatim:**
- PRD v0.23 s.12: *"Identity first. Stage 1 runs before every other stage. The working key (composite FIGI) is RECORDED
  on the crosswalk record as an attribute. `security_key` stays the partition and page key until the key design is
  ruled."* Stage 1: *"Bloomberg add-security, with the FIGI family, ISIN, SEDOL and LEI appended to its identity
  fields."* Cap: *"Bloomberg: 1 unique security."*
- CTO msg 24261 Q4: *"The READ_HERE two-phase sign-in check is each Bloomberg cell's AC0, and a refusal names the
  surface."* Q5: *"It is a SERVED act and takes a CTO/COO pair. The blast radius is Lenovo's record only. The other 95
  records must be byte-equal before and after. Rollback restores the prior crosswalk version."*
- Andrew-direct @`6f1a72e4be`: *"The Bloomberg data quota binds every pull, and each pull is sized and printed before it
  runs."*

**PRECONDITION: `AMGT-rk-114` is DRAINED into your base.** It makes `add_security` write an ENRICH registration for a
name that is already a coverage record, and makes `build_crosswalk` attach that identity to the existing record instead
of appending a colliding second one. Without it this pull half-lands. AC0 checks for it.

**THE MEASURED STATE at SITEZ `0972b8631c` (re-measured by AC0/AC1 at your HEAD):**
- The served crosswalk is `s3://opal-data-harvest/crosswalk/v1/2026-09-19.json`: 96 records (89 coverage, 7
  registered). Lenovo is a COVERAGE record (`source_row.folder = "Lenovo 992 HK"`) with no `identity`. A local
  `build_crosswalk("2026-09-19")` is byte-identical to it.
- `lib/research/identity/registrations.json`: 7 rows (CAT, CSL, 6861 and 4 UNRESOLVED); none for 992.
- `bloomberg/harvest/bronze/identity/`: 3 objects (CAT, CSL, 6861); none for 992.
- The box's default interpreter (Python 3.11) imports both `blpapi` 3.26.4.2 and `boto3`.

**THE SIZED PULL, printed by AC0 before any call:**
- The login-state probe `integrations/bloomberg/auth/dapi_check.py`: 1 ReferenceDataRequest, `SPX Index`/`PX_LAST` (1
  security x 1 field). READ_HERE: openService alone is not sufficient, so the probe is a real data request.
- The identity pull: 1 ReferenceDataRequest, `992 HK Equity` x 9 fields (`NAME, EXCH_CODE, LEGAL_ENTITY_IDENTIFIER,
  CENTRAL_INDEX_KEY_NUMBER, COMPOSITE_ID_BB_GLOBAL, ID_BB_GLOBAL, ID_ISIN, ID_SEDOL1, COMPANY_WEB_ADDRESS`).
- **Total for this cell: 2 requests, 10 security-field points, 1 Lenovo security.** No `--dry-run` pull: add_security's
  dry run makes the SAME Bloomberg call, so it would double the spend.

**THE ACT (one command, today's UTC date):**
`python -m lib.research.identity.add_security --folder "Lenovo 992 HK" --bloomberg "992 HK" --as-of <today UTC> --write-pool`

It writes, in this order:
- (W1) raw bronze `s3://opal-data-harvest/bloomberg/harvest/bronze/identity/security_key=992_HK_Equity/<stamp>.json`
  (conditional put, immutable);
- (W2) `lib/research/identity/registrations.json` +1 ENRICH row (a repo file; you COMMIT it);
- (W3) `s3://opal-data-harvest/crosswalk/v1/<today>.json`, a NEW key that becomes the served latest.

## 2. WHERE THIS CAME FROM

ROUND 29, decomposition s.37 (cut by `2.0.0_SA_COO~Z`), on PRD v0.23 s.12 and CTO msgs 24257, 24261 and 24300. Wave 1 of
the Lenovo trial.

## 3. SURFACES

<paths>
lib/research/identity/registrations.json
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~113/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-113.lenovo-identity-pull.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- Every code file is a WALL. Scratch is `<worktree>/.scratch/r113/` (never committed).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~113 <0.9.0_WK_AMGT_RESAPP~113@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **THE PAIR:** both halves `ledger/NEVER_WIDEN_ROUND29_RK113_{COO,CTO}_HALF.md` must be SIGNED before you spawn (AC0
  checks).
- **DAPI DOWN = STOP.** If AC0's probe reads DOWN, file a BLOCKING row naming the surface ("DAPI login state, READ_HERE
  s.2") and STOP. **You do NOT run the sign-in:** its submit phase spends one of a 2-attempt lockout budget and types a
  credential, so it is an attended act for the issuer.
- **Deploy ledger:** open it AFTER AC1 and BEFORE AC2:
  `python .tools/deploy_ledger.py open --slug amgt-rk113-lenovo-identity --title "<title>" --author "0.9.0_WK_AMGT_RESAPP~113" --leg "w1|s3-prefix|opal-data-harvest/bloomberg/harvest/bronze/identity/security_key=992_HK_Equity/|AC3" --leg "w3|s3-prefix|opal-data-harvest/crosswalk/v1/|AC3" --leg "w2|git|lib/research/identity/registrations.json|AC3" --leg "v|verify|crosswalk resolve 992|AC4"`
  Close each leg on its read, then the entry. There is NO `--legs` flag.
- **ONE pull, never retried.** A Bloomberg error on the call lands UNRESOLVED per add_security's own path; record it,
  do not re-run.
- **A field Bloomberg does not return** (an entitlement or bad-field error) is recorded in `identity.field_errors`, NOT
  a failure.
- **ROLLBACK (any one trigger):** AC3 finds any record other than 992 changed, the record count changed, or 992's
  `security_key` or any non-identity field changed.
- **WHICH ROLLBACK APPLIES, decided from the measured substrate (CTO msg 24307): RE-PUBLISH THE PRIOR CONTENT AS A
  NEWER VERSION -- never a delete, and NOT a VersionId restore.**
  - `opal-data-harvest` versioning is **Enabled**, measured at the draft: the 09-19 key holds 7 versions (corrected from 8 by the CTO's full listing, msg 24312, and re-read by the issuer on list_object_versions), with 0 delete
    markers.
  - But the reader picks the latest DATED KEY (`crosswalk._read_pool_latest`, `sorted(keys)[-1]`, `crosswalk.py:806-830`),
    never a version. This act writes a NEW key (`crosswalk/v1/<today>.json`) and never writes the 09-19 key.
  - So today's key has NO prior version to restore, and restoring the 09-19 key would change nothing the reader serves.
- **The rollback steps:**
  1. a NEW commit removing the ENRICH row from `registrations.json`;
  2. `python -m lib.research.identity.crosswalk --as-of <the UTC day the rollback runs> --write-pool`, which writes a
     document whose records equal AC1's:
     - on the SAME day it writes a NEWER VERSION of today's key (write_pool's IfMatch overwrite; the enriched version
       stays as a noncurrent version);
     - on a later day it writes that day's NEW key, which becomes the latest;
  3. re-run AC3's record comparison against AC1. **The SAME byte-equal criterion binds the ROLLBACK run as the forward
     run (CTO msg 24310):** every record, 992 included this time, byte-equal to AC1's snapshot, with the count printed.
     Anything short of that is a BLOCKING row, and the ledger stays OPEN.
  - The crosswalk-vintage stamp on every served page (`scoped_amgt.py:1725-1732`) moves to today on the forward run, and
    to the rollback's date on a rollback. That is the CTO half's named blast radius (msg 24310), and it is expected.
  - The identity bronze object is immutable and has 0 production readers, so it is LEFT and recorded.
  - **No S3 delete in any branch.**
- No other write: no model block, no battery, no Lusha, no portal, no IAM.
- **THE REFUSAL CLAUSE** applies. **SURPRISE ROWS:** `AMGT_RESAPP-Z-W113-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (literal; timeout 600)

**Grading order:** AC0, AC1, (open the ledger), AC2, AC3, AC4, (close the ledger), AC5.

`.scratch/r113/ac0.py`:
```
import os, subprocess, sys
sys.path.insert(0, ".")
from lib.research.identity import add_security as a, crosswalk as cw
print("pair_coo", os.path.exists("org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND29_RK113_COO_HALF.md"), "pair_cto", os.path.exists("org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND29_RK113_CTO_HALF.md"))
print("precursor_rk114", os.path.exists("lib/research/identity/tests/test_crosswalk_enrich_coverage.py"))
print("identity_fields", len(a.IDENTITY_FIELDS), a.IDENTITY_FIELDS)
print("SIZED: probe 1 request (SPX Index x PX_LAST); pull 1 request (992 HK Equity x %d fields); total 2 requests, %d points, 1 Lenovo security" % (len(a.IDENTITY_FIELDS), 1 + len(a.IDENTITY_FIELDS)))
print(subprocess.run([sys.executable, "integrations/bloomberg/auth/bbg_credentials.py", "--check"], capture_output=True, text=True).stdout.strip()[:300])
```

`.scratch/r113/ac1.py`:
```
import json, hashlib, boto3, sys
sys.path.insert(0, ".")
from lib.research.identity import crosswalk as cw
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
keys = sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="crosswalk/v1/") for o in pg.get("Contents", []))
served = json.loads(s3.get_object(Bucket=B, Key=keys[-1])["Body"].read())
def label(r): return r["security_key"] or json.dumps(r["source_row"], sort_keys=True)
shas = {label(r): hashlib.sha256(json.dumps(r, sort_keys=True).encode()).hexdigest() for r in served["records"]}
json.dump({"key": keys[-1], "records": len(served["records"]), "shas": shas, "r992": [r for r in served["records"] if r["security_key"] == "992_HK_Equity"][0]}, open(".scratch/r113/pre.json", "w"), indent=1)
open(".scratch/r113/pre_crosswalk.json", "wb").write(cw.serialise(served))
regs, _ = cw.load_registrations()
idb = [o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="bloomberg/harvest/bronze/identity/") for o in pg.get("Contents", [])]
print("served_key", keys[-1], "records", len(served["records"]), "distinct_labels", len(shas))
print("r992_has_identity", "identity" in [r for r in served["records"] if r["security_key"] == "992_HK_Equity"][0])
print("registrations", len(regs), "for_992", sum(1 for r in regs if r.get("security_key") == "992_HK_Equity"))
print("identity_bronze", len(idb), "for_992", sum(1 for k in idb if "992_HK_Equity" in k))
print("local_rebuild_byte_equal", cw.serialise(cw.build_crosswalk(served["as_of"])) == cw.serialise(served))
```

`.scratch/r113/ac3.py`:
```
import json, hashlib, boto3, datetime, sys
sys.path.insert(0, ".")
from lib.research.identity import crosswalk as cw
pre = json.load(open(".scratch/r113/pre.json"))
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
keys = sorted(o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="crosswalk/v1/") for o in pg.get("Contents", []))
today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
post = json.loads(s3.get_object(Bucket=B, Key=keys[-1])["Body"].read())
def label(r): return r["security_key"] or json.dumps(r["source_row"], sort_keys=True)
shas = {label(r): hashlib.sha256(json.dumps(r, sort_keys=True).encode()).hexdigest() for r in post["records"]}
others = [k for k in pre["shas"] if k != "992_HK_Equity"]
print("latest_key", keys[-1], "is_today", keys[-1] == "crosswalk/v1/%s.json" % today)
print("records", len(post["records"]), "pre", pre["records"])
print("others_byte_equal", sum(1 for k in others if shas.get(k) == pre["shas"][k]), "of", len(others))
r = [x for x in post["records"] if x["security_key"] == "992_HK_Equity"][0]
ident = r.get("identity") or {}
fe = ident.get("field_errors") or {}
for f in ("composite_figi", "figi", "isin", "sedol", "lei", "website"):
    print("992", f, "present" if ident.get(f) else ("field_error" if fe else "ABSENT"))
strip = {k: v for k, v in r.items() if k != "identity"}
strip["provenance"] = {k: v for k, v in r["provenance"].items() if k != "identity"}
print("992_non_identity_equal", strip == pre["r992"], "security_key", r["security_key"])
print("denominators", post["denominators"])
idb = [o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="bloomberg/harvest/bronze/identity/") for o in pg.get("Contents", [])]
print("identity_bronze", len(idb), "for_992", [k for k in idb if "992_HK_Equity" in k])
regs, _ = cw.load_registrations()
print("registrations", len(regs), "992_rows", [(x.get("mode"), x.get("resolution")) for x in regs if x.get("security_key") == "992_HK_Equity"])
```

`.scratch/r113/ac4.py`:
```
import json, os, subprocess, sys
code = "import json,sys; sys.path.insert(0,'.'); from lib.research.identity import crosswalk as cw; out={}; [out.__setitem__(q, cw.resolve(q)) for q in ('992 HK','992 HK Equity','CAT US','CSL AU','6861 JP')]; print(json.dumps({'from': cw.loaded_from(), 'r': out}, sort_keys=True, default=str))"
post = json.loads(subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, env={k: v for k, v in os.environ.items() if k != "AMGT_CROSSWALK_PATH"}).stdout)
pre = json.loads(subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, env=dict(os.environ, AMGT_CROSSWALK_PATH=".scratch/r113/pre_crosswalk.json")).stdout)
print("post_from", post["from"])
def strip_identity(rec):
    # ISSUER AMENDMENT 3: provenance gains an `identity` line for an enriched name. That line is
    # named in BOTH signed pair halves, so it is expected, and AC3 already strips it. AC4 asks a
    # DIFFERENT question -- does the adapter still RESOLVE the same way -- so it compares with the
    # same strip, and separately prints which top-level keys differ, so a second difference cannot hide.
    out = dict(rec)
    prov = dict(out.get("provenance") or {})
    prov.pop("identity", None)
    out["provenance"] = prov
    return out
for q in post["r"]:
    a, b = post["r"][q], pre["r"][q]
    differing = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
    print("resolve", repr(q), a.get("security_key"), a.get("resolution"),
          "equal_to_pre", strip_identity(a) == strip_identity(b),
          "raw_differing_keys", differing)
```

`.scratch/r113/ac5.py`:
```
import re, sys
text = open(".scratch/r113/ac2_out.txt", encoding="utf-8", errors="replace").read()
calls = [int(x) for x in re.findall(r"bloomberg_calls (\d+)", text)]
print("pull_calls", sum(calls), "probe_calls 1", "spent_total", sum(calls) + 1, "sized_total 2")
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-113"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r113/ac0.py && python integrations/bloomberg/auth/dapi_check.py</invocation><expect>BEFORE any write: "pair_coo True pair_cto True"; "precursor_rk114 True"; "identity_fields 9" with the nine names; the SIZED line "total 2 requests, 10 points, 1 Lenovo security"; the credential check's fingerprint line (never a value); then dapi_check prints an UP line and exits 0. A DOWN line is a STOP with a BLOCKING row naming the surface -- no sign-in is attempted by the worker</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-113"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r113/ac1.py</invocation><expect>READ-ONLY, the pre-act snapshot: "served_key" (measured crosswalk/v1/2026-09-19.json at the cut) with "records" R0 and "distinct_labels" equal to R0 (measured 96); "r992_has_identity False"; "registrations" G0 with "for_992 0"; "identity_bronze" D0 with "for_992 0"; "local_rebuild_byte_equal True". pre.json and pre_crosswalk.json written. A False rebuild-equality is a STOP and a row: the "other 95 byte-equal" bar would then be untestable</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-113"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.identity.add_security --folder "Lenovo 992 HK" --bloomberg "992 HK" --as-of "$(date -u +%Y-%m-%d)" --write-pool 2>&1 | tee .scratch/r113/ac2_out.txt</invocation><expect>LIVE, the ONE pull, ledger OPEN before it: "RAW LANDED: s3://opal-data-harvest/bloomberg/harvest/bronze/identity/security_key=992_HK_Equity/..."; a "MEASURED: security_key 992_HK_Equity ... composite_figi ..." line (field_errors printed if any); "bloomberg_calls 1"; then "OK: uploaded s3://opal-data-harvest/crosswalk/v1/<today>.json ... records=R0 ...". An UNRESOLVED line (a Bloomberg security error) is recorded with its reason and graded by AC3's rollback rule, never re-run</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-113"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r113/ac3.py</invocation><expect>"latest_key crosswalk/v1/<today>.json is_today True"; "records" equal to R0 and pre; "others_byte_equal" R0-1 "of" R0-1 (95 of 95 at the cut); for 992 each of composite_figi, figi, isin, sedol, lei and website reads "present" or "field_error" (never "ABSENT" with no field_errors); "992_non_identity_equal True security_key 992_HK_Equity"; denominators carry "enriched": 1 and "registered" unchanged from AC1; "identity_bronze" D0+1 with exactly one 992 key; "registrations" G0+1 with the 992 row ("ENRICH", "MEASURED"). ANY other record differing, or a changed record count, is a ROLLBACK per section 4. Close the w1/w2/w3 legs on this read</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-113"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r113/ac4.py</invocation><expect>"post_from s3://opal-data-harvest/crosswalk/v1/<today>.json"; AMENDMENT 3: "resolve '992 HK' 992_HK_Equity MEASURED equal_to_pre True raw_differing_keys ['provenance']" and the same for '992 HK Equity' -- the adapter's RESOLUTION for Lenovo is unchanged, and the only raw difference is the provenance identity line both signed halves name. raw_differing_keys listing anything besides 'provenance' for 992, or anything at all for a control, is a ROLLBACK trigger; the three controls CAT US, CSL AU and 6861 JP each "equal_to_pre True". Close the verify leg and the ledger entry on this read</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-113"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r113/ac5.py && git log --oneline -1 -- lib/research/identity/registrations.json</invocation><expect>"pull_calls 1 probe_calls 1 spent_total 2 sized_total 2"; then the commit carrying the registrations.json ENRICH row (committed by you after AC3)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~113/AMGT_RESAPP.TO-AMGT-rk-113.lenovo-identity-pull.proof_of_spec.json`,
grade it with your worktree's `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5` (rc 0), flip the
record face's status to `complete` only if every criterion passes, commit, and report once. The report names: the SIZED
line, the dapi_check line, the MEASURED line, the six identity field states, the others_byte_equal count, the ledger
entry path with its open and close, and the branch taken (kept or rolled back).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
1. **Why a precursor (rk-114):** `add_security` was built for NEW names. Lenovo is a coverage record, so the planned
   invocation would pass the folder pre-check, spend the call, land the bronze, dirty `registrations.json`, and then
   `build_crosswalk` would raise on the duplicate key. That is a half-landed act, and every later crosswalk build would
   raise until someone hand-edited the file.
2. **The served effect is wider than Lenovo's record, and the pair says so:** the new `crosswalk/v1/<today>.json`
   becomes the latest key for EVERY reader. Each served identity block's `crosswalk_vintage`/`crosswalk_source`
   (`scoped_amgt.py:1725-1732`) moves from 2026-09-19 to today for EVERY name, with no record content changing. Warm
   Lambda containers keep the cached 09-19 document until they recycle (`crosswalk._CACHE`).
3. **Budget:** 2 requests, of which 1 is the SPX login probe (READ_HERE requires a data read). The plan's "7 requests on
   1 security" counted Lenovo pulls only; this cell spends 1 of those 7.
4. **`identity` has 0 production readers today** (a `lib/` + `integrations/` census). The FIGI is RECORDED as the PRD
   asks; nothing keys on it yet.

<status>pending</status>
<round>29</round>
<slot>~113</slot>
<fabric>site-z</fabric>
