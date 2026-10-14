# NFRA_OPLGTW task order -- `OG-gt-2` -- `harvest_get_chatter`, `harvest_search_articles`, `harvest_get_article`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~73</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gt-2` (decomposition addendum R3-T.50, workstream G1-TYPED, FWD-22)

`harvest_get_chatter`, `harvest_search_articles`, `harvest_get_article` (gold chatter and mentions joined to publisher silver); the newest-part and `data_status` corrections.

### The base you build on (cell OG-gt-0, ALREADY ON YOUR HEAD): `app/harvest_typed.py`, exactly this surface

- `admit_typed(tool, ref, *extra) -> Optional[dict]`: the refusal dict, else `None`. It wraps `harvest_read.admit` (principal
  present, Opal user, served prefix; one audited refusal). Call it FIRST, before any S3 call.
- `audit_ok(tool, ref, nbytes) -> None`: the one audit row of a served call.
- `refusal(message, code) -> dict`: `{"error", "code", "guard_denied": True}`.
- `envelope(body, *, as_of, source_keys, denominator, absent_reason=None) -> dict`: returns
  `{"as_of", "source_keys", "denominator", "absent_reason", **body}`, projected to 50 KB.
- `project(out, limit=51200) -> dict`: when the JSON size exceeds `limit`, pops items off the end of the largest list
  field until it fits, sets `"truncated": True` and `"projected_to_bytes"`.
- `list_keys(prefix) -> list[{"key", "size", "last_modified"}]`: every page, no Delimiter, auto-paginated.
- `newest_part(prefix) -> Optional[str]`: for a prefix laid out `<prefix>date=YYYY-MM-DD/part-<stamp>.parquet`, the key
  with the greatest `(date partition, part file name)`; `None` when there is no `.parquet`.
- `read_parquet(key, columns=None, filters=None) -> (rows, total_rows, nbytes)`: columns projected at read; `filters` is
  a list of `(column, op, value)` with op in `=`, `<`, `>`, `in` (a string value is coerced to the column's date type).
- `read_json(key) -> (obj, nbytes)`: `.json` and `.json.gz`, capped.
- `TYPED_MAX_BYTES` (64 MiB): the cap on one object read; over it, `harvest_over_cap`.

**Rules of the seam.** A tool module NEVER imports `get_current_principal` or boto3: it reaches S3 and the principal only
through `harvest_typed`, so one probe patch point (`app.harvest_read.get_current_principal`) governs every tool. Each tool
is a TOP-LEVEL function in your module with exactly the tool's name and the inputs below, returns a dict, and every success
carries `as_of`, `source_keys`, `denominator` and `absent_reason` through `envelope(...)`. A key you were asked about that is
absent returns an empty body with `absent_reason` set (a string naming WHY), never an error and never silence.

### Two corrections from the CRO's L4-R review (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/L4R_REVIEW_NFRA_OPLGTW_v3.0_BRIEF_20261014.md` section "Corrections"), binding on this cell

1. `chatter_daily`, `article_security_mention` and `chatter_window` are read from the NEWEST part file of the newest date
   partition ONLY (`newest_part`). Every part is a full snapshot: the newest chatter_daily part holds 68,002 rows against
   1,338,296 across all parts; the newest mention part 52,424 against 459,334. Reading the prefix multiplies counts about 9x
   and 20x with no error. This is the one guard whose absence returns a plausible wrong number.
2. `harvest_get_chatter` returns `data_status` for every day and never presents 0 articles as "no chatter" (on the newest
   day 174 of 242 names read DENIED and 68 PARTIAL). `harvest_resolve_security` answers a CUSIP query `not_held`, never
   `none` (CUSIP is held in 0 of 18 Parquet tables; ISIN only for 65 names).

### The three tools (G1 section 3, lines 87-129 of `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md`)

Module `infra/aws/ec2/opal-gateway/app/harvest_press.py`.

- **`harvest_get_chatter(security_key: str, from_day: str, to_day: str)`**. Returns `daily` rows (day, articles_total, tier_a,
  tier_b, tier_c, tier_d, mention_score, trailing_7d_sum, trailing_30d_sum, `data_status`, publishers_found_codes);
  `windows` for 30, 90 and 365 days (articles_total, scored, voters, tone); `events` (first_day, last_day, articles_total,
  tier_a, publishers_distinct, lead_article_key). Reads: gold `chatter_daily` and `chatter_window` from the NEWEST part of the
  newest date partition only (correction 1); `chatter_event` deduplicated on `event_id`. `source_keys` names the exact
  part keys read. Rows are filtered to `from_day..to_day` inclusive and to the one `security_key`. `data_status` is copied
  from the part for EVERY day row; a day with `articles_total == 0` carries its `data_status` and never reads as "no chatter".
  The denominator is `{"rows_in_part": N, "rows_for_key": M, "days_returned": K}`.
- **`harvest_search_articles(security_key, publisher=None, from=None, to=None, min_tier=None, in_title=False, limit=25)`**
  (the date parameters are named `from_day` and `to_day` in Python because `from` is reserved; the tool schema names them
  `from` and `to`). Publisher in `sa|bbg|wsj|ft|barrons`; `limit` 25 default, 100 max (a larger value is clamped and
  `limit_applied` says so). Returns `articles`: article_key, publisher, published_utc, signal_tier, mention_in_title,
  co_mentioned_securities, sentiment label and score, then title, url, words from silver. Reads: gold
  `article_security_mention` (newest part, correction 1) and `article_sentiment`, joined on `article_key` to
  `<publisher>/harvest/silver/article/`. Newest first by `published_utc`.
- **`harvest_get_article(article_key: str, publisher: str, include_text: bool = False)`**. Returns title, url, published_utc,
  words, content_status, mentioned security_keys; the text or `body_blocks` ONLY when `include_text` is true. Reads the
  newest record per `article_key` under `<publisher>/harvest/silver/article/`, the partition located from the mention row's
  published date. `publisher` outside the five is refused `harvest_bad_argument`.

### Where the contracts are (read each section you need; they are the truth of columns and layout)

In `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md`: chatter_daily 1022-1280; chatter_event 1281-1465; chatter_window 1466-1659; article_security_mention
364-640; article_sentiment 641-830; silver article per publisher: barrons 4661-5014, bloomberg 5246-5605, ft 5827-6147,
seeking-alpha 6975-7328, wsj 7560-7865.

### Tests, `infra/aws/ec2/opal-gateway/tests/test_og_gt2.py` (fake client with TWO date partitions and TWO parts in the newest)

- `test_oggt2_ac01`: chatter reads the newest part of the newest partition ONLY: the fake holds an older part with a
  different `articles_total` for the same key and day, and the result equals the newest part's numbers; `source_keys` holds the
  newest part's key and not the older one.
- `test_oggt2_ac02`: every `daily` row carries `data_status`; a day with `articles_total == 0` and `data_status == "DENIED"`
  is returned with both, and `windows` and `events` are present.
- `test_oggt2_ac03`: `harvest_search_articles` clamps `limit=500` to 100 with `limit_applied`, orders newest first, honours
  `min_tier` and `in_title`, and joins sentiment and title from silver.
- `test_oggt2_ac04`: `harvest_get_article` omits text unless `include_text`, and returns it with it; an unknown publisher is
  refused `harvest_bad_argument`; a missing article returns an empty body with `absent_reason`.
- `test_oggt2_ac05`: a non-Opal principal is refused all three tools with zero S3 calls.

The live probe is the issuer's AC2: chatter for ASML over the last 30 days must match an independent read of the same newest
part (sum of `articles_total`), search returns one to five articles each with an `article_key`, and a fetched article has no
text unless asked. Run the three calls yourself first, with `INTERNAL_READER_ROLE_ARN` unset.

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer
  registers every tool and re-pins the counts at the merge, in one commit. Do not edit them; name the registration you
  expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address, or an object's
  text body into a report, a row or a log; write the catalog file (`app/refs/DATA_CATALOG.yaml` is NFRA_MCPINDEX's alone);
  override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/harvest_press.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/tests/test_og_gt2.py
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/L4R_REVIEW_NFRA_OPLGTW_v3.0_BRIEF_20261014.md
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~73/`. Rows: id `NFRA_OPLGTW-Z-W73-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 5 of 5; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)chatter: days \d+, data_status on every day True; source chatter_daily keys 1, equal to the independent newest part True; sum articles_total tool (\d+) vs independent \1; search [1-5] article\(s\) \(want 1-5\); article text withheld by default True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three tools read the newest part only and carry `data_status` on every day.
- `AC2`: against the real bucket: ASML's 30-day chatter equals an independent read of the SAME newest part (the 9x control), and search and article work.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-2.press-tools.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (decomposition addendum R3-T.50 @d9371ffe81; PRD v3.0 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- The release this cell rides: `NFRA_OPLGTW.TO-OG-ap-18`; its grant is `NFRA_OPLGTW.TO-OG-hv-2` (A5).
- The issuer registers the tools and re-pins counts at the merge (CUT BY WRITE SET: hookups belong to no cell).
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe absent).
- Queue: staged until OG-gt-0 merges; the spawn is the GO.

<status>complete</status>
<round>37</round>
<workstream>G1-TYPED</workstream>
<slot>~73</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
