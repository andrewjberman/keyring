# NFRA_OPLGTW task order -- `OG-nw-1` -- G6: news_search_articles, news_trending_topics, news_keyword_intelligence, news_market_mood, news_for_security (+ the DynamoDB read grant and its ask)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-nw-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-nw-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~82</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-nw-1` (decomposition addendum R3-T.52, workstream FWD22-W6, FWD-22 G6)

The five G6 news tools over the live news DynamoDB tables and the two portal singletons, their DynamoDB read grant file and their own never-widen ask (Phase A: no apply, no deploy).

Build the five G6 news tools, their DynamoDB read grant and their own never-widen ask. PHASE A ONLY: build, grant file, ask. NO apply, NO deploy.
Module `infra/aws/ec2/opal-gateway/app/news_typed.py`.

### The seam you build on (ALREADY ON YOUR HEAD)

`app/typed_scope.py` (OG-gt-6) over `app/harvest_typed.py` (OG-gt-0): `Scope(name, bucket, served_prefixes, client, max_bytes)`, `admit_scope(scope, tool, ref, *extra)` (principal present; Opal user,
else `typed_opal_only`; `ref` under a served prefix, no `..`; one audited refusal; call it FIRST, before any S3 or DynamoDB call), `list_keys`, `newest_part`, `read_parquet`, `read_json`, and the
re-exports `envelope(body, *, as_of, source_keys, denominator, absent_reason=None)` (the answer is projected to 50 KB; an empty body must carry an `absent_reason`), `project`, `refusal`,
`audit_ok`, `TypedOverCap`. `HARVEST` is the harvest bucket's scope. A tool module NEVER imports `get_current_principal` or holds a boto3 client at module scope.

For the two portal singletons (S3) build your OWN scope in this module: `Scope("portal", <the bucket opal-data-portal-v2>, ("json/sentiment/",), <app.internal_role.s3_client when it returns a client, else a lazily created boto3 S3 client inside a function>)`.
For the DynamoDB reads use ONE injectable function `_ddb()` (module scope, returns the boto3 `dynamodb` client created lazily INSIDE it, so a test replaces it and `comp-iam` resolves the calls). The three table names
come from the ENVIRONMENT at call time, never from a literal (the naming gate refuses live names that are not builder output, and has no override): `NEWS_ARTICLES_TABLE`, `NEWS_TRENDING_TABLE`, `NEWS_KEYWORD_TABLE`
(`os.environ.get`; a key that is unset returns the error dict `news_unavailable` with ZERO reads). Add the three lines writing those keys to the `.env` printf in `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`
(a shell file the gate does not grade; the values are the live table names in the census below). Allowed DynamoDB calls: `Query` and `GetItem` ONLY (never `Scan`, never a write).

### FIRST ACT (the naming limb stopped five G1 workers)

Before you build, stage your S3 key literals (the two singleton keys) as a scratch `.py` file and run `python .tools/naming-gate.py --diff <the staged diff> --enforce`. A refused literal: STOP, file ONE BLOCKING row,
report. Never split a string or override. The gate grades the bucket literal and `s3://` URIs, not bare keys.

### The five tools (G6 section (c), lines 142-154 of `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G6_news.md`; the store census is at lines 38-90)

All five are Opal-internal reads with no firm fork. Every answer carries `as_of`, `source_keys` (for DynamoDB: the table names read and the key condition, never item content), a `denominator` dict and `absent_reason`.
Each answer states its store's freshness in TRADING DAYS behind T-1 (`lib/trading_calendar.py`).
- **`news_search_articles(date_from: str, date_to: str, text: str = None, source: str = None, sentiment_label: str = None, limit: int = 25)`**: reads `opal-news-articles` (HASH `article_date` `YYYY-MM-DD`, RANGE `url_hash`; GSI
  `source_date_index` on `source` + `published_at`). The window `date_from..date_to` is CAPPED AT 14 DAYS (a longer window is refused `harvest_bad_argument` with ZERO reads). One `Query` per day (paginated with
  `LastEvaluatedKey`), capped per day at 2,000 items scanned (the denominator says when the cap bit). `text` is a case-folded match on title + summary; `source` filters on the source (use the GSI when `source` is given);
  `sentiment_label` on the FinBERT label. `limit` 25 default, 100 max (`limit_applied`). Returns per article: published, source, title, url, FinBERT label and score, entity_type; plus `per_day_counts` (a DICT `{"YYYY-MM-DD": count}`: the COUNT of items
  that day, from a `Select=COUNT` Query, independent of the text filter) and the denominator scanned. The articles are under the answer key `articles`. The table has NO ticker or security column: never present a text match as a security match.
- **`news_trending_topics(date: str = None, side: str = "all", days: int = 1, match: str = None)`**: reads `opal-news-trending-daily` (HASH `date`, RANGE `topic_rank` `bullish-1..10`, `bearish-1..10`). `date` default is the
  newest date present; `side` in `bullish|bearish|all`; `days` 1-30 (a theme history; clamped, `limit_applied`); `match` is a case-folded match on headline and raw_keyword. Returns `date` (the date served) and `topics`, the ranked topics (rank, headline, raw_keyword,
  trending_score, momentum, velocity, article_count, sources, citations, sentiment map, gpt_model, created_at). Do NOT read the frozen `semantic-news-trending-daily` (160 trading days behind).
- **`news_keyword_intelligence(keyword: str = None, date: str = None)`**: reads `opal-keyword-intelligence` (HASH `keyword`, RANGE `generated_date`; GSI `date-index`). With `keyword`, that keyword's newest brief; with `date`, the briefs of
  that date (GSI); neither is refused `harvest_bad_argument`. Returns headline_summary, sentiment label/score/pattern, key_drivers, counterarguments, confidence, the article list (titles + urls), generated_at.
- **`news_market_mood()`**: reads `json/sentiment/fear-greed-index.json` and `json/sentiment/keyword-sentiments.json` (the only two live keys under `json/sentiment/`; the 720 keyword-history keys are frozen since 2026-04-07 and are NOT served).
  Returns the current fear/greed with its history and the keyword FinBERT set, each with its own `generated_at` as the as-of.
- **`news_for_security(security_key: str = None, ticker: str = None, window_days: int = 14)`**: FIRST the harvest mention index: `amgt/harvest/gold/article_security_mention/` read from the NEWEST part of the newest date partition ONLY
  (`typed_scope.newest_part(HARVEST, ...)`; every part is a full snapshot, reading the prefix multiplies counts about 20x), filtered to the security and to `window_days` (max 30); THEN, as a stated fallback, `news_search_articles`
  with `text=<ticker>`. The answer carries `mentions` (the harvest rows) and `fallback` (the text-match rows, EACH with `match: "text"`) and the answer's `precision` saying a text match on titles is NOT a security-keyed index. Neither ticker nor security_key is refused `harvest_bad_argument`.
  The harvest read goes through the HARVEST scope's admission (`admit_scope(HARVEST, ...)`).
Not built: no semantic-trending tool, no Seeking Alpha URL tool, no tool on `opal-harvest-articles` (empty), no `market-updates` tool, no keyword-history family.

### The grant file and the ask

1. **Grant file** `infra/aws/terraform/opal-gateway/news_read_iam.tf`: ONE `aws_iam_role_policy`, named by the builder (run `lib/opal_naming.py name(...)` and cite the call in a comment; if the builder refuses, STOP and file a BLOCKING row),
   on the gateway instance role `aws_iam_role.gw`, with `dynamodb:Query` and `dynamodb:GetItem` ONLY, on exactly these resources: the three tables' ARNs and the two GSI ARNs (`.../table/<name>/index/source_date_index` and `.../index/date-index`) --
   no `Scan`, no wildcard action, no `*` resource. Run a targeted `terraform plan -target=...` directly (`safe-apply` gates `apply` only) and record it: 1 to add, 0 to change, 0 to destroy. If the root plan shows other changes, record them whole and STOP.
2. **The ask**, `W/NEVER_WIDEN_ASK_OG-nw-1.md`, for the three halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`). SEVEN items, each under a heading containing its word: (1) the `diff` by file; (2) the five `tools`, their refusals and the 14-day cap;
   (3) the `widening`: the gateway instance role gains `Query` and `GetItem` on three tables and two indexes (read only; the S3 singleton reads need no change) and the three new `.env` keys; (4) the `grant` (the one policy, its builder name, the actions, the resource ARNs, the plan line);
   (5) `both branches` of a call (refused: zero reads; admitted: bounded queries); (6) the `rollback` (redeploy the prior release; destroy the one policy); (7) the `triggers` (tools +5 on the live census, the three `.env` names present, a served read of each tool under an Opal stand-in principal).

### Tests, `infra/aws/ec2/opal-gateway/tests/test_og_nw1.py` (a fake DynamoDB client recording every call; a fake S3 scope; Opal stand-in principal patched at `harvest_read.get_current_principal`)

- `test_ognw1_ac01`: `news_search_articles` caps the window at 14 days (a 15-day window is refused with ZERO calls), issues `Query` only (the fake raises on `Scan`), applies `text` and `sentiment_label`, clamps `limit=500` to 100, and returns `per_day_counts`.
- `test_ognw1_ac02`: `news_trending_topics` defaults to the newest date, honours `side`, `days` (clamped to 30) and `match`; `news_keyword_intelligence` serves by keyword and by date through the GSI and refuses neither-given.
- `test_ognw1_ac03`: `news_market_mood` reads exactly the two singleton keys and reports each `generated_at`; `news_for_security` reads the NEWEST part only (a fake holds an older part with different mentions) and its fallback rows carry `match: "text"`.
- `test_ognw1_ac04`: a non-Opal and an absent principal are refused all five tools with ZERO reads of any kind; with a table env key unset the tool returns `news_unavailable` with zero reads.
- `test_ognw1_ac05`: no `Scan`, no write call and no table-name literal exists in `news_typed.py` (grep the source for the three live table names: zero hits).

The live probe is the issuer's AC2 (it sets the three env keys to the live names itself). Run the same calls yourself first, with `INTERNAL_READER_ROLE_ARN` unset, with the env keys set to the live names (`opal-news-articles`, `opal-news-trending-daily`, `opal-keyword-intelligence`).

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
infra/aws/ec2/opal-gateway/app/news_typed.py
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/tests/test_og_nw1.py
infra/aws/terraform/opal-gateway/news_read_iam.tf
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G6_news.md
lib/trading_calendar.py
lib/opal_naming.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~82/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~82/`. Rows: id `NFRA_OPLGTW-Z-W82-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-nw-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/nw1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 5 of 5; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-nw-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/nw1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)news: day \d{4}-\d{2}-\d{2} count tool (\d+) vs independent \1; articles [1-5] \(want 1-5\); 15\+ day window refused True; trending topics [1-9]\d* \(want >= 1\); mood reads 2 keys; neither-keyword refused True; for_security answered True with fallback rows labelled text True; envelope on all True; non-Opal refused True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-nw-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/nw1.AC3.sh; echo "exit=$?"</invocation><expect>(?s)grant: policies 1 \(want 1\); actions \['dynamodb:GetItem', 'dynamodb:Query'\] \(want only Query and GetItem\); dynamodb ARNs [3-9]\d* \(want >= 3\); bare \* resources 0 \(want 0\).*ask sections: 7 of 7.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the five tools are built, read only through Query and GetItem, cap the window, hold no table-name literal, and refuse non-Opal before any read.
- `AC3`: the grant file is one policy with `Query` and `GetItem` only on named table and index ARNs, and the ask names its seven items.
- `AC2`: against the live tables the per-day count equals an independent COUNT query, the 14-day cap and neither-given refusals fire, the singletons read two keys, the security tool labels its fallback, and a non-Opal principal is refused.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-nw-1.news-tools.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if AC1, AC2 and AC3 PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (decomposition addendum R3-T.52; PRD v3.5 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- Decomposition addendum R3-T.52 (G6). Rides release `OG-ap-19` with its own never-widen ask (the gateway instance role gains Query and GetItem on three tables and two indexes).
- The issuer registers the tools and re-pins counts at the merge (CUT BY WRITE SET: hookups belong to no cell).
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe absent).

- A1 (issuer, 2026-10-14 ~19:2xZ, the worker's rows W82-S1, S2, S6, S8): S1 -- the preflight's "no IAM change" described the S3 side; the cell's own grant file carries the DynamoDB read, and the preflight is corrected by this note. S2 -- `source_date_index` is sparse
  (9,905 of 381,261 items), so the tool's `source` filter reads the base table per day and never uses it: ACCEPTED, and the grant is NARROWED to the least it needs: the three table ARNs and the one `date-index` ARN (drop the `source_date_index` ARN from
  `news_read_iam.tf` and from the ask's grant and widening sections). S6 -- the 14-day cap counts dates inclusively (15 refused): ACCEPTED as built. S8 -- the status flip is the issuer's, at the merge. The worker is re-seated for the S2 narrowing only.
  No criterion moves. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>complete</status>
<round>37</round>
<workstream>FWD22-W6</workstream>
<slot>~82</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
