# AMGT_RESAPP task order -- `AMGT-rk-48` -- DIRECT ACT: live CEO search validation names

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-48</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~71</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a ONE-TIME direct act (Andrew-direct ~16:1xZ: one-time use on the three validation names, not recurring, not scheduled); it arms no cron, alarm, monitor or cadence and reads no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant changes; the act uses this box's existing S3 put/get on management/v1/ and Secrets Manager read, the same permissions AMGT-rk-47 used on these same three keys (each key's single version written 2026-09-19T07:46Z, measured by the issuer at the cut).
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the validator-context declaration applies to the worker's deliverable at drain.
</preflight>

## 1. THE SIGNED SECTION -- inlined verbatim from both halves of the never-widen pair

### COO HALF
## `AMGT-rk-48` -- the CEO search: organizing agent over SERP records, validation names (R14-E6; FWD-17)

**THE ACT.** AC1-AC3 OFFLINE (the primitive fix in `serp.py`, the mutant pair, the namesake anchor, the verbatim
control) -- no live act, no pair needed. AC4-AC6 LIVE, ONLY IF the spawn prompt states the Bright Data per-use word is
on file (PRD v0.13 :751 -- Bright Data runs *"only under Andrew's per-use word"*; the ~17:2xZ record :44-45 does not
answer it for the running validation; the issuer will name the record in the spawn prompt or the worker refuses with a
row): at most 9 SERP requests (`serp_opal`) and an Anthropic call capped at US$2.00 on the 3 validation CEOs, then a
REWRITE of the 3 dated management keys `rk-47` wrote (`ceo_profile` block added; `ceo_public_profile` kept as its
projection so `read_management` and E1's reading do not break mid-round).

**BLAST RADIUS.** The 3 management keys `rk-47` wrote -- the ONE in-place rewrite of a dated key in this chain (the
worker prints pre-act sha and VersionId per key). Served: NO until `rk-31` lands; then yes. `_pool/` untouched
(`--skip-pool`). NO Lambda.

**WRITER CENSUS of those 3 keys: N = 1 active writer this round** (`crosswalk.write_pool` via `enrich`), two cells in
sequence (`rk-47` then `rk-48`, same slot, `rk-48` reading `rk-47`'s object as its pre-act state). No schedule.

**EXPECTED OUTCOME, both branches (CTO msg 23833: the domain comes from `rk-38`'s `verified_site`, never a hand list;
`domains.json` is not a source for a validation name).** A name with no `verified_site`: `NOT_ATTEMPTED` /
`NO_VERIFIED_SITE`, nothing searched, nothing rewritten for it. A CEO whose SERP records anchor to the namesake control: `ceo_profile` with the
anchored fields and the record ids. A CEO with no anchoring record, or the vendor word ABSENT from the spawn prompt:
`ceo_profile` ABSENT with the reason (offline branch -- AC4-AC6 REFUSED with the reason, nothing rewritten), and
`ceo_public_profile` unchanged. The `_pool/` ETag EQUAL before and after in every branch.

**PER-KEY ROLLBACK.** Pre-act: `get_object` bytes of each of the 3 keys saved to `.scratch/` with sha256 + VersionId
in the entry (the bucket is versioned -- `list-object-versions` confirms the pre-act VersionId). Rollback = re-put the
saved bytes (or `copy_object` from the pre-act VersionId), read back sha256.

**NOT COVERED:** any SERP request beyond the cap; any spend beyond US$2.00; any name outside the three; a `_pool/`
write; a run without the per-use word on file.

Signed `2.0.0_SA_COO~Z`, 2026-09-18, at the round-14 cut.


### CTO HALF
## `AMGT-rk-48` -- the CEO search: organizing agent over SERP records, validation names (R14-E6)

### 1. THE ACT
AC1-AC3 offline (a primitive fix in `data/find/dualbiz/scripts/serp.py`, a mutant pair, a namesake anchor, a
verbatim control) -- no live act. AC4-AC6 live ONLY under Andrew's Bright Data per-use word: at most 9 SERP
requests and an Anthropic call capped at US$2.00 on the three validation CEOs, then an in-place rewrite of the
three dated management keys rk-47 wrote. **This agrees with the COO half.** On the authorization: Andrew's
2026-09-18 ~19:4xZ word covers **Lusha** inside the three-name validation with no credit ceiling, and his
~20:4xZ answers cover the CEO-step shape (labelled links for found-but-not-read, LinkedIn link-only and never
fetched, an unlocker for 403/429 **for the CEO step alone**, a residence line permitted, contact data still
forbidden). **Neither of those is a Bright Data per-use word**, and the COO half is right to gate on the
spawn prompt naming the record. I concur with the gate as written and add nothing to it.

### 2. THE SOURCE DIFF
The existing CEO step is `enrich.ceo_public_profile()` (`enrich.py:404-453`), consuming
`data/find/dualbiz/scripts/serp.py` through `_serp_module()` (`:370-381`), which side-loads the estate module
and injects `BRIGHT_DATA_API_KEY` / `BD_SERP_ZONE` from the environment (`:373-379`) so the module makes no
secret-store call of its own. The primitive's limitation is stated in the producer's own basis string at
`:449-451`: *"title and snippet are null: that primitive returns urls only."*

That limitation is exactly what the ratified clause forbids -- `AMGT_RESAPP_PRD.md:747`: *"Each organic result
keeps its title and snippet, not the url alone."* **So AC1's "primitive fix in `serp.py`" is the change the
contract requires, and I confirm the defect at source.** The consequential edits: `ceo_public_profile` must
stop hard-coding `title`/`snippet` null (`:414`), and `management.schema.json`'s `definitions.ceo_profile`
already carries `title` and `snippet` as properties, so the SCHEMA does not block it (unlike `roster_source`
in rk-47). Verified: `ceo_profile` properties are `['absence_class', 'basis', 'ceo_name', 'ir_domain',
'query', 'snippet', 'status', 'title', 'url']`, `additionalProperties: False`. **A `ceo_profile` BLOCK with
new fields (the half's word) WILL hit `additionalProperties: False` and take `main`'s branch 1 -- nothing
written, `rc=1` -- unless the schema is extended.** Same shape as rk-47's finding, same remedy.

### 3. THE PRODUCER'S RULE, BRANCH BY BRANCH
`ceo_public_profile()` at HEAD, complete (this is the rule the rewrite must preserve or deliberately replace):

| # | branch | source | `status` | `absence_class` | vendor call |
|---|---|---|---|---|---|
| 1 | no CEO on the roster | `:418-421` | ABSENT | **NOTHING_FOUND (the `:416` default -- WRONG, nothing was searched)** | none |
| 2 | no declared IR domain | `:423-425` | ABSENT | **NOTHING_FOUND (same defect)** | **none** |
| 3 | the SERP primitive raised | `:429-433` | ABSENT | **NOTHING_FOUND (same defect)** | attempted |
| 4 | urls returned, none on the IR host | `:440-444` | ABSENT | CANNOT_SAY | yes |
| 5 | zero urls returned | `:436-439` | ABSENT | NOTHING_FOUND (correct here) | yes |
| 6 | a url on the IR host | `:446-452` | RESOLVED | null | yes |
| 7 | empty roster (built elsewhere) | `:532-536` | ABSENT | NOTHING_FOUND | none |

Branch 3 is the PRD's *"A FAILED search (a request error or an unparseable body) is recorded as FAILED, with
its cause -- never as an EMPTY search"* (`:745-746`) -- **and HEAD records it as NOTHING_FOUND, i.e. exactly
as an empty search.** Branches 1, 2, 3 and 7 all collapse into NOTHING_FOUND. **That is four of the five
ratified states missing and the wrong one asserted**, and it is the producer-side twin of the rk-43 adapter
finding. rk-48 is the cell that touches this function; if the rewrite does not fix `:416`'s default, the new
`ceo_profile` block inherits a field that lies on four branches.

**Which branch the COO half's outcomes rest on, and the gap.** The half's positive outcome (a CEO whose SERP
records anchor to the namesake control) rests on branch 6; its negative (no anchoring record, or the vendor
word absent -> `ceo_profile` ABSENT with the reason, `ceo_public_profile` unchanged, nothing rewritten) rests
on branches 4/5 and on the offline refusal. **Both are covered.** But **branch 2 fires FIRST on all three
names and neither half names it**: as measured in rk-47 section 3, CAT / CSL / 6861 are absent from
`domains.json` (5 declared), so `ir_domain` is `None` and `ceo_public_profile` returns at `:425`
**before reaching `serp_brightdata` at `:430`**. **So on the code and data at HEAD, rk-48's AC4-AC6 cannot
issue a single SERP request for the three validation CEOs.** The cell is blocked on a declared IR domain, and
the contract says where that domain may come from -- `AMGT_RESAPP_PRD.md:741-743`: *"The company domain comes
ONLY from the site the filings battery VERIFIED as the right entity -- never a hand list, never Bloomberg's
raw web address."* **Hand-adding three rows to `domains.json` is the forbidden hand list.** So rk-48's live
arm has an unstated upstream dependency on the filings battery having verified a domain for each of the three,
and neither half names it. **This is the finding I would put in front of the issuer before the spawn.**
I have NOT verified whether any other chain's cell supplies those domains -- **UNVERIFIED (the round-14
issuance is not committed; only chains I, M, F, E, P COO halves exist at `9a6aa12da2`).**

**The rewrite's own write rule.** The rewrite goes through `crosswalk.write_pool` (via `write_document`), so
every branch in the rk-45 table applies here too. Two consequences for this cell specifically: (a) if the
rewritten document is byte-identical to rk-47's, **no put happens** (`crosswalk.py:627`) and `put_performed`
is `False` -- a correct outcome that a naive "the key was rewritten" criterion grades as failure; (b) the
overwrite is `IfMatch`-conditional on the ETag read moments earlier (`:628`), so a concurrent writer yields an
uncaught 412 and **nothing is written** -- consistent with the half's radius, and the half's rollback
(saved bytes + VersionId, `copy_object` from the pre-act version) covers every branch. I confirm the rollback
is sound.

### 4. WRITER CENSUS CROSS-CHECK
The COO half prints **N = 1 active writer this round** of the three dated keys (`crosswalk.write_pool` via
`enrich`), two cells in sequence. **I measure the same N = 1** and I confirm the sequencing claim at source:
`write_document` (`enrich.py:619-622`) is the only caller of `management_key` (`:553`), and `enrich.main` is
its only caller (`:685`). Instrument: `comp-find 'management_key' lib/` plus line-numbered reads -- different
from the COO's live-key/VersionId instrument. **One addition the half does not make:** the same three keys are
also READ by `compute_pool` (`enrich.py:594-605`) whenever ANY name is enriched with `--write-pool` on the
same date, so rk-48's rewrite CHANGES A POOL INPUT even though it writes no pool object. Under `--skip-pool`
that is inert this round; it stops being inert the moment any cell runs `enrich` without the flag.

### 5. WHAT THIS HALF DOES NOT COVER
Any SERP request beyond 9; any spend beyond US$2.00; any name outside the three; any `_pool/` write; a run
without the Bright Data per-use word on file; **any edit to `domains.json`** (required for the live arm to
fire, and forbidden by `:741-743` unless the domain comes from the verified filings battery); the
`management.schema.json` extension the new `ceo_profile` block needs; the `absence_class` producer fix at
`enrich.py:416`; the five-state enum the PRD ratifies at `:750-752`; and any fetch of a LinkedIn page (Andrew:
link-only, never fetched) or any unlocker use outside the CEO step.

---


## 2. WHERE THIS CAME FROM

Minted by `python .tools/direct-act-order.py mint` from the signed never-widen pair bounding this DIRECT act; round 14.

## 3. SURFACES -- what you may read and write

<paths>
.scratch/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~71/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-48.live-ceo-search-validation-names.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

## 4. BOUNDS

Bounded to the paths the signed pair names -- the pair bounds, the order grants. No path outside the <paths> block above is a write surface.

## 5. PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-48"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import boto3, hashlib, os
print("word_record_at_HEAD", os.path.exists("org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_161xZ_AMGT_RESAPP_BRIGHT_DATA_AND_ZHKO_SPEND_YES.md"))
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
os.makedirs(".scratch/rk48_pre", exist_ok=True)
for k in ("CAT_US_Equity", "CSL_AU_Equity", "6861_JP_Equity"):
    objs = [o["Key"] for p in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="management/v1/%s/" % k) for o in p.get("Contents", [])]
    r = s3.get_object(Bucket=B, Key="management/v1/%s/2026-09-19.json" % k); body = r["Body"].read()
    open(".scratch/rk48_pre/%s.json" % k, "wb").write(body)
    print("PRE-ACT", k, "objects_under_prefix", len(objs), "version", r.get("VersionId"), "bytes_sha256", hashlib.sha256(body).hexdigest())
pool = [o for p in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="management/v1/_pool/") for o in p.get("Contents", [])]
print("POOL_BASELINE objects", len(pool), "newest", sorted(pool, key=lambda o: o["Key"])[-1]["Key"] if pool else None, "etag", sorted(pool, key=lambda o: o["Key"])[-1]["ETag"] if pool else None)
'</invocation><expect>word_record_at_HEAD True (Andrew's Bright Data per-use word, 2026-09-21 ~16:1xZ, one-time, the three validation names only -- the COO half's gate). For each of CAT_US_Equity, CSL_AU_Equity, 6861_JP_Equity: objects_under_prefix 1 and version EQUAL to the issuer's measurement at the cut (CAT PO0KN5ZWaAmK28_drCI9dXxmmYC5Qx1T, CSL pNV1.QMgs9tdvbuVCa4ifuzP4K.UKKIX, 6861 ntH46iAfkv1Je.AMZA0LIXbDeyJCNm80 -- the keys AMGT-rk-47 wrote 2026-09-19T07:46Z, untouched since), with the pre-act bytes saved to .scratch/rk48_pre/ and their sha256 printed (the rollback baseline). POOL_BASELINE printed. ISSUER RULE: the act is the IN-PLACE REWRITE OF THESE DATED 2026-09-19 KEYS that both halves signed -- never a run dated today, which would CREATE new management/v1/*/2026-09-21.json keys no half covers. Any version differing from the issuer's, or any objects_under_prefix other than 1: STOP, BLOCKING row (disarm_owner 2.0.0_SA_COO~Z) -- a writer moved the key since the cut and the signed pre-act state no longer holds; no live act</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-48"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/deploy_ledger.py open --slug amgt-rk48-live-ceo-search --title "AMGT-rk-48 live CEO search, direct act under the round-14 chain E pair: in-place rewrite of management/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/2026-09-19.json" --author 0.9.0_WK_AMGT_RESAPP~71 --leg "L1|verify|management/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/2026-09-19.json|3 keys schema-valid, 0 contact fields, no new dated key, _pool untouched, SERP attempts at most 9, model_usd at most 2.00"</invocation><expect>the ledger entry is OPENED and its sentinel lands in org/critical_paths/.open_deploys/ BEFORE any live write (CLAUDE.md NEVER-2: a deploy is never left half-landed); the command prints the entry path; run AFTER AC1 passes and BEFORE AC3</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-48"><invocation>cd "$(git rev-parse --show-toplevel)" && export BRIGHT_DATA_API_KEY="$(comp-secrets get find-insure/bright-data/api-key --reveal --value-only)" && export BD_SERP_ZONE=serp_opal && export ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal --value-only)" && [ -n "$BRIGHT_DATA_API_KEY" ] && [ -n "$ANTHROPIC_API_KEY" ] && python -c '
import boto3, json
from lib.research.management import enrich
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"; AS_OF = "2026-09-19"
serp = 0; usd = 0.0
for k in ("CAT_US_Equity", "CSL_AU_Equity", "6861_JP_Equity"):
    if serp >= 9 or usd >= 2.00:
        print("CAP REACHED before", k, "-- not run"); continue
    rc = enrich.main(["--security-key", k, "--as-of", AS_OF, "--write-pool", "--skip-pool"])
    doc = json.loads(s3.get_object(Bucket=B, Key="management/v1/%s/%s.json" % (k, AS_OF))["Body"].read()); cp = doc.get("ceo_profile") or {}
    a = len((cp.get("search") or {}).get("attempts") or []); m = float((cp.get("cost") or {}).get("model_usd") or 0); serp += a; usd += m
    print("POST-ACT", k, "RC", rc, "status", cp.get("status"), "reason_code", cp.get("reason_code"), "name_source", cp.get("name_source"), "ceo", cp.get("ceo_name"), "attempts", a, "model_usd", m, "items", len(cp.get("items") or []), "counts", json.dumps(cp.get("counts")))
print("TOTALS serp_attempts", serp, "of cap 9 | model_usd", round(usd, 4), "of cap 2.00")
'</invocation><expect>the key-presence guard passes (both exports non-empty -- the --value-only flag AMGT-rk-67 landed returns the BARE value; the pre-round-16 idiom "$(comp-secrets get X --reveal)" captured a four-line descriptor block, not a key, and is the idiom behind row W50-S4 -- do not use it); per name RC 0 and status one of the five ratified states with a reason_code; a name whose filings source object carries no verified_site reads NOT_ATTEMPTED / NO_VERIFIED_SITE with nothing searched for it (the CTO half's re-signature condition @541d395e0d: the domain comes ONLY from the filings battery's verified site, never domains.json); Keyence may honestly read NOT_SEARCHED / NO_CEO_ON_ROSTER; TOTALS serp_attempts at most 9 and model_usd at most 2.00 (the pair's caps; the loop refuses to START a name once either is reached). NO secret value appears anywhere in the output, the proof instance, a row or a log -- only the command text. A cap breach, or any name outside the three, is outside the pair: STOP, BLOCKING row, AC4's rollback branch</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-48"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import boto3, hashlib, json
from lib.research.management import enrich
s3 = boto3.client("s3", region_name="us-east-1"); B = "opal-data-harvest"
total = relocated = contact = 0
for k in ("CAT_US_Equity", "CSL_AU_Equity", "6861_JP_Equity"):
    objs = sorted(o["Key"].rsplit("/", 1)[-1] for p in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="management/v1/%s/" % k) for o in p.get("Contents", []))
    r = s3.get_object(Bucket=B, Key="management/v1/%s/2026-09-19.json" % k); body = r["Body"].read(); doc = json.loads(body)
    ok, errors = enrich.validate(doc); contact += len(enrich.contact_fields_present(doc)); cp = doc.get("ceo_profile") or {}
    pre = hashlib.sha256(open(".scratch/rk48_pre/%s.json" % k, "rb").read()).hexdigest()
    for item in cp.get("items") or []:
        for fact in item.get("facts") or []:
            total += 1; relocated += 1 if fact.get("char_range") and fact.get("quote") else 0
    print(k, "dated_objects", objs, "version_now", r.get("VersionId"), "rewritten", hashlib.sha256(body).hexdigest() != pre, "schema_valid", ok, "errors", errors[:2], "status", cp.get("status"))
pool = [o for p in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="management/v1/_pool/") for o in p.get("Contents", [])]
print("POOL objects", len(pool), "newest", sorted(pool, key=lambda o: o["Key"])[-1]["Key"] if pool else None, "etag", sorted(pool, key=lambda o: o["Key"])[-1]["ETag"] if pool else None)
print("DENOMINATOR: 3 objects read back; facts with quote and char_range %d of %d; contact fields stored %d" % (relocated, total, contact))
' 2>&1 | tee .scratch/rk48_ac4.txt</invocation><expect>each name's dated_objects is EXACTLY ["2026-09-19.json"] (no 2026-09-21 key was created -- the pinned as_of held); schema_valid True with no errors on all 3; rewritten True for a searched name, and False is CORRECT for a NOT_ATTEMPTED name or a byte-identical rewrite (crosswalk.write_pool performs no put on identical bytes -- the CTO half's gap 3); POOL objects, newest and etag EQUAL to AC1's POOL_BASELINE (_pool untouched, --skip-pool held); every fact carries a quote and a char_range (relocated equals total; if total is 0 the report says so explicitly rather than reading it as a pass); contact fields stored 0 -- a read-back through get_object and validate(), a different instrument from the writer's own print. ROLLBACK BRANCH (any schema_valid False, any contact field, any new dated key, the pool moved, or a cap breached): re-put each rewritten key's saved bytes from .scratch/rk48_pre/ (or copy_object from its AC1 pre-act VersionId), read back its sha256 equal to AC1's, file a BLOCKING row naming the branch; DELETE NOTHING -- a stray new dated key is reported for the issuer, because an S3 delete needs Andrew's word</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-48"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/deploy_ledger.py close-leg --slug amgt-rk48-live-ceo-search --leg-id L1 --proof "$(cat .scratch/rk48_ac4.txt)" && python .tools/deploy_ledger.py close --slug amgt-rk48-live-ceo-search && python .tools/deploy_ledger.py check</invocation><expect>leg L1 closed with AC4's read-back as its proof, the entry CLOSED, and the check lists no open entry for amgt-rk48-live-ceo-search (its sentinel removed from org/critical_paths/.open_deploys/); the closed entry is COMMITTED with the instance, never left staged. On the rollback branch the leg closes with the rollback proof instead</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the proof_of_spec instance, flip <status> to complete, commit under the granted <paths> only.

<!-- ===================== RECORD FACE -- never travels to a worker ===================== -->

<status>complete</status>
<direct_act>true</direct_act>
<slot>~71</slot>
<fabric>site-z</fabric>

