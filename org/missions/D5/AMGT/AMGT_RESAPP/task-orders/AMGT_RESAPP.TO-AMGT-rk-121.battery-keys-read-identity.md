# AMGT_RESAPP task order -- `AMGT-rk-121` -- L-FIL PRECURSOR: `keys_from_crosswalk` READS the landed `identity` block (cik, lei, website, legal name) instead of hard-coding every one of them ABSENT; CODE ONLY, no call, no write -- without it Lenovo's battery crawls with ZERO seeds

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-121</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~121</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one library function and its tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; no AWS write. AC0's crosswalk read
  is READ-ONLY under the seat's existing credentials.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification; the declaration applies to the worker's
  deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~121`.** Work ONLY in the worktree named in your spawn prompt. First act: print
`git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that `org/`, `.tools/` and
`lib/research/filings/battery.py` exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~121;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL -- `AMGT-rk-121` (round 30, the precursor to L-FIL)

**THE DEFECT, measured by the issuer at SITEZ `1fd5d2ba3f` (re-measure in AC0):**
`lib/research/filings/battery.py`'s `keys_from_crosswalk` returns, for EVERY security:
```
"cik": None, "cik_reason": "crosswalk/v1 record %r carries no cik field today (C-INSTANTIATION-ENTRY, chain I's own cell, has not landed yet -- 1.1)"
"lei": None, "lei_reason": ...same shape...
"web_address": None, "web_address_reason": ...same shape...
"legal_name": None, "legal_name_reason": ...same shape...
```
Those reasons are now **STALE**: `AMGT-rk-113` (round 29, drained @`74128f4c8b`) landed an `identity` block on the
crosswalk record. Measured live for `992_HK_Equity`:
- `crosswalk.record_for("992_HK_Equity")["identity"]` carries `cik` **932477**, `lei`
  **254900VUZRGD5U73RE46**, `website` **www.lenovo.com**, `name` **LENOVO GROUP LTD**;
- `battery.keys_from_crosswalk("992_HK_Equity")` nevertheless returns `cik None`, `lei None`, `web_address None`,
  `legal_name None`, with `ticker_root "992"` and `exchange "HK"`.

**WHY IT BLOCKS L-FIL.** In `_step4_company_site` the FIRST seed is `keys["web_address"]`
(source `bloomberg-web-address`). Lenovo's other two seed sources are empty too: there are no prior EDGAR seeds, and
`_exchange_listing_seed` returns `(None, "no exchange listing template for exchange 'HK'")` because
`EXCHANGE_LISTING_PAGES` has no HK entry. **So the crawl starts with ZERO seeds and refuses** -- and the trial would
record Lenovo's filings stage UNRESOLVED for a reason that is our own staleness, not the issuer's site. The legal
name also feeds the acceptance test, so a None there degrades the match even if a document is found.

**RULED, what you build (code only, no call, no write):**
1. `keys_from_crosswalk` reads the record's `identity` block when it is present:
   - `cik` <- `identity["cik"]`, `lei` <- `identity["lei"]`, `web_address` <- `identity["website"]`,
     `legal_name` <- `identity["name"]`;
   - each value that IS found carries its reason as `None` (the field is no longer absent);
   - each value still MISSING keeps a NAMED reason, and that reason must say what was looked for and where -- never
     the stale "carries no cik field today" blanket. State the identity source in the reason (the crosswalk record's
     `identity`), so a later reader can tell "absent from a present identity" from "no identity at all".
   - `ticker_root`, `exchange`, `domicile`, `source` and `raw_record` keep exactly today's behaviour.
2. A record with **no** `identity` block behaves EXACTLY as today, reason text included. That is the
   byte-compatibility limb: 89 of the 96 records have no identity, and the 60 keyless coverage records must not move.
3. New tests in a NEW file `lib/research/filings/tests/test_keys_from_identity.py`:
   - `test_identity_present_fills_cik_lei_website_name` -- a stub record with an identity yields all four, each with
     reason None;
   - `test_identity_absent_is_unchanged` -- a stub record with no identity yields today's four Nones AND today's
     reason strings, byte-equal (pin the expected strings from the pre-edit module via `git show`);
   - `test_partial_identity_names_what_is_missing` -- an identity carrying only `website` fills web_address and leaves
     cik/lei with a NAMED reason that mentions the identity block;
   - `test_ticker_root_and_exchange_unchanged` -- both still derive from `bloomberg`/`exchange` as today;
   - `test_live_lenovo_record_yields_seed` -- READ-ONLY against the served crosswalk: `992_HK_Equity` now yields
     `web_address` `www.lenovo.com` and `cik` 932477. (Skip with a NAMED skip reason if S3 is unreachable; never
     silently pass.)

**What this cell does NOT change:** `_step4_company_site`, `_step1_edgar_ticker`, `_step2_edgar_bloomberg_cik`,
`run_battery`, `fetch.py`, `filings.py`, the crosswalk, and every S3 object. No live call of any kind.

## 2. WHERE THIS CAME FROM

ROUND 30, decomposition s.38 (cut by `2.0.0_SA_COO~Z`). It exists because drafting L-FIL measured the battery blind to
rk-113's landed identity. Same class as `AMGT-rk-114`, which had to precede rk-113 for the same reason: a producer
that cannot see what the previous stage landed.

## 3. SURFACES

<paths>
lib/research/filings/battery.py
lib/research/filings/tests/test_keys_from_identity.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~121/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-121.battery-keys-read-identity.md
</paths>

- A surface not named here is a WALL. Scratch is `<worktree>/.scratch/r121/`.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~121 <0.9.0_WK_AMGT_RESAPP~121@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **CODE ONLY.** No Bloomberg, SEC, issuer-site, vendor or model call. No S3 write. AC0's and the live test's
  crosswalk reads are READ-ONLY.
- **One pytest call per test directory.** **Bars are AC0-measured + N**, never typed zeros.
- **THE REFUSAL CLAUSE** applies. **SURPRISE ROWS:** `AMGT_RESAPP-Z-W121-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (literal; timeout 600)

`.scratch/r121/ac0.py`:
```
import json, sys
sys.path.insert(0, ".")
from lib.research.filings import battery
from lib.research.identity import crosswalk as cw
k = battery.keys_from_crosswalk("992_HK_Equity")
print("keys_before", json.dumps({x: k.get(x) for x in ("ticker_root", "exchange", "cik", "lei", "web_address", "legal_name")}, default=str))
rec = cw.record_for("992_HK_Equity") or {}
ident = rec.get("identity") or {}
print("identity_on_record", json.dumps({x: ident.get(x) for x in ("cik", "lei", "website", "name")}, default=str))
print("seed_would_be", k.get("web_address"))
print("exchange_listing_seed", battery._exchange_listing_seed(k))
doc = cw._read_pool_latest() if hasattr(cw, "_read_pool_latest") else None
recs = (doc or {}).get("records") or []
print("crosswalk records", len(recs), "with_identity", sum(1 for r in recs if r.get("identity")), "without", sum(1 for r in recs if not r.get("identity")))
```

`.scratch/r121/ac3.py`:
```
import json, sys
sys.path.insert(0, ".")
from lib.research.filings import battery
k = battery.keys_from_crosswalk("992_HK_Equity")
print("keys_after", json.dumps({x: k.get(x) for x in ("ticker_root", "exchange", "cik", "lei", "web_address", "legal_name")}, default=str))
print("reasons_after", json.dumps({x: k.get(x) for x in ("cik_reason", "lei_reason", "web_address_reason", "legal_name_reason")}, default=str)[:600])
print("seed_now", k.get("web_address"))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-121"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r121/ac0.py &amp;&amp; python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -1</invocation><expect>BEFORE any edit, the defect measured on the live record: "keys_before" shows cik null, lei null, web_address null, legal_name null with ticker_root "992" and exchange "HK"; "identity_on_record" shows cik 932477, lei 254900VUZRGD5U73RE46, website www.lenovo.com, name LENOVO GROUP LTD; "seed_would_be None"; "exchange_listing_seed (None, ...no exchange listing template for exchange 'HK'...)" -- together, ZERO seeds; the crosswalk record split printed with its denominator (measured 96 records, 1 with identity, 95 without). Then the filings suite baseline F0 (measured 106 at the cut). Record every value</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-121"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest lib/research/filings/tests/test_keys_from_identity.py -v -p no:cacheprovider 2&gt;&amp;1 | tail -10</invocation><expect>"5 passed" and 0 failed, with the five named arms PASSED -- including test_identity_absent_is_unchanged, whose expected reason strings are pinned from the PRE-EDIT module, and test_live_lenovo_record_yields_seed (or a NAMED skip if S3 is unreachable, never a silent pass)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-121"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -1</invocation><expect>"N passed" with N = F0 + 5 and 0 failed</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-121"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r121/ac3.py</invocation><expect>AFTER the edit, on the SAME live record: "keys_after" shows cik 932477, lei 254900VUZRGD5U73RE46, web_address www.lenovo.com and legal_name LENOVO GROUP LTD, with ticker_root and exchange unchanged from AC0; the four reasons read null for the filled fields; "seed_now www.lenovo.com" -- the crawl now has its issuer seed</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-121"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; git diff --name-only HEAD~1 HEAD -- lib integrations infra .tools portal</invocation><expect>EXACTLY lib/research/filings/battery.py and lib/research/filings/tests/test_keys_from_identity.py -- no other code file</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~121/AMGT_RESAPP.TO-AMGT-rk-121.battery-keys-read-identity.proof_of_spec.json`,
grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4` (rc 0), flip the record face's
status to complete only if every criterion passes, commit, and report once, naming the before/after keys for Lenovo.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
1. **This precursor was not in the CTO's round-29 analysis.** Drafting L-FIL measured it: the battery cannot see the
   identity rk-113 landed, and Lenovo's crawl would start with zero seeds. It is the same class as rk-114 before
   rk-113, and it is why the four wave-2 cells are not all concurrent -- rk-118 chains behind this one.
2. **The stale reason string is itself the tell:** "C-INSTANTIATION-ENTRY, chain I's own cell, has not landed yet"
   was true when it was written and is false now. A reason that names a future event ages silently.
3. No `identity` reader exists elsewhere in `lib/` today, so this is the first consumer of rk-113's landing.

<status>complete</status>
<round>30</round>
<slot>~121</slot>
<fabric>site-z</fabric>
