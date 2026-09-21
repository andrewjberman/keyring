# AMGT_RESAPP round 20 -- never-widen pair, R20-A (+ R20-B folded) -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: SIGNED at issuance.** The CTO half is
owed by `1.0.0_SA_CTO~Z` at `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND20_RK79_CTO_HALF.md`, under a
section headed with the same cell id. The order does not act on one half (its AC1).
**Sources:** decomposition s.28; PRD v0.16 @2d0da569e7 `C-EXEC-MANAGEMENT` (`:764-767`, `:768`, `:777`, `:783`);
Andrew-direct ~19:5xZ record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_195xZ_AMGT_RESAPP_KEYENCE_SEARCH_YES_LUSHA_R20_YES.md`
@4bcfed0e0d (*"Yes on Keyence and Yes on Exception."*, read at `:13-15` as ONE Bright Data CEO search on
`6861_JP_Equity`, one name, one search, no repeat, no schedule); CTO msgs 24036, 24039, 24049 (the five calls ruled,
CSL's second write added), 24055 and 24058 (`ROUND_ANALYSIS.round19.md` s.2-s.4: R20-B folded into this cell, no fetch,
the census, no adapter redeploy); rows Z-S192 (the write-set lesson), Z-S195..Z-S197, Z-S200, Z-S202; the order
`task-orders/AMGT_RESAPP.TO-AMGT-rk-79.jp-president-and-readable-roster-reason.md`.
**Measured at the cut:** 2026-09-21 ~20:3xZ, read-only, by the issuer. Every value below is re-read by the order's AC3
at spawn; where a re-read differs, the ROLLBACK TARGET is the worker's AC3 value, never this file's.

## `AMGT-rk-79` -- one CEO web search for Keyence, readable roster reasons, CAT marked incomplete: THREE writes

### THE LITERAL KEY LIST (ruling (b), msg 24058) -- the census's result, 3 keys, denominator 15

1. `s3://opal-data-harvest/management/v1/6861_JP_Equity/2026-09-19.json` -- the search and the readable reason.
2. `s3://opal-data-harvest/management/v1/CSL_AU_Equity/2026-09-19.json` -- the readable reason, no search.
3. `s3://opal-data-harvest/management/v1/CAT_US_Equity/2026-09-19.json` -- marked `INCOMPLETE-NO-CEO`, no search.

Census, measured over the newest management object of ALL 15 names: RESOLVED rosters with no chief executive (after
the v0.16 JP rule) = **1 of 15 (CAT)**; the 7 other RESOLVED rosters each carry one. So the list is 6861 + CSL + CAT +
0 further hits. The order's AC3 re-runs the census at spawn and STOPS if it reads anything but `[CAT_US_Equity]`.

### THE ACTS

- **AC5 (6861):** ONE run of `python -m lib.research.management.enrich --research-stored-ceo --security-key
  6861_JP_Equity --as-of 2026-09-19 --write-pool`: reads the stored management object and the filings source object,
  re-derives `roster_reason` / `absence_reason_evidence`, runs `ceo_search.ceo_profile` ONCE on the STORED officer
  Tetsuya Nakano (read as CEO under the v0.16 JP rule), projects `ceo_public_profile`, validates, ONE conditional put.
- **AC6 (CSL):** ONE run of `... --rederive-roster-reason --security-key CSL_AU_Equity --as-of 2026-09-19
  --write-pool`: reads the stored object and the CURRENT filings object (`GzAiBH5L...`, rk-72's rewrite), re-derives
  `roster_reason` (the rule sentence built from the object's own battery attempts) and `absence_reason_evidence` (its
  current reason), ONE conditional put. No secret in the environment.
- **AC7 (CAT):** ONE run of `... --rederive-roster-reason --security-key CAT_US_Equity --as-of 2026-09-19
  --write-pool`: reads the stored object and the STORED filing (`G8qBiPSV...`); the executive-officer pointer names
  Item 1D, which the stored object does NOT hold (measured: only the Item 10 cut and an Item 1A / Item 7 excerpt; the
  full document is not in the pool or on disk), so the roster is marked `INCOMPLETE-NO-CEO` with a readable reason
  naming the unread section; ONE conditional put. No fetch, no secret.
All three under ONE deploy-ledger entry opened before AC5 (AC4, legs L1-L3) and closed on the read-back (AC9).

### VENDOR EGRESS (Andrew's per-use word, 6861 only)

- **Bright Data** (`serp_opal`): ONE `serp_brightdata_records(query, max_pages=1)` call for 6861 -- **at most 3 SERP
  requests** (1 request plus the code's own retries, ONLY on a captcha or a 5xx, `retries=2`, `serp.py:400, :459-462`;
  never a 4xx retry, never a retry the worker adds). Query `"Tetsuya Nakano" Keyence CEO` (`ceo_search.py:538-539`),
  locale `gl us` / `hl en` (ruling 4, msg 24049).
- **Result pages**: at most 3 direct GETs to the hosts the search returns (`max_pages=3`, `:609`); LinkedIn never.
- **Anthropic** (`claude-opus-5`): at most 4 calls, `max_tokens 2000` each, page window 7000 characters; worst case about
  US$0.35 (`:107-110`). **Cap: US$1.00.**
- The mode checks `cost.serp_requests <= 3` and `cost.model_usd <= 1.00` BEFORE the write; exceeded -> BLOCKED, nothing
  written. It REFUSES before any call when the stored `ceo_profile.search.query` is already set or the accession
  differs.
- **CSL and CAT: ZERO vendor calls, ZERO fetches** (AC6/AC7 run with every vendor key unset). **Not covered:** any other
  name; a second search; Lusha; any Bloomberg call; any EDGAR fetch (the fetch of CAT's 10-K is carded to Andrew by the
  CTO, s.3(a)); a schedule.

### BLAST RADIUS

What the act MAY move, and nothing else (bucket versioning `Enabled` on all three):
- **(B1) 6861:** one NEW version differing from the pre-act version ONLY at `roster_reason`,
  `absence_reason_evidence`, `ceo_profile`, `ceo_public_profile`. At the cut: 3 versions, 0 delete markers, latest
  `1Hm1g.MqxkFnnyRqLgQlwSiB925mRG9G` (3827 bytes, sha256 `29e6a873...d72c349e`).
- **(B2) CSL:** one NEW version differing ONLY at `roster_reason` and `absence_reason_evidence` (the evidence mirror:
  measured, it is the filings reason `roster_reason` is derived from, not a byte copy). At the cut: 3 versions, latest
  `u_iDxPeXTBMyIMZtwYwJYVU53iwMdgiS` (9494 bytes). `roster_status` stays `UNRESOLVED-SOURCE`; the 14 officers,
  `fallback` and every other field stay byte-equal.
- **(B3) CAT:** one NEW version differing ONLY at `roster_status` (`RESOLVED -> INCOMPLETE-NO-CEO`), `roster_reason`,
  `section_refers_to`, `absence_reason_class` (`None -> pull-missed`) and `absence_reason_evidence`. At the cut: 3
  versions, latest `tJMJuD2oIO1ONv6dngrilLVgX4tOS3qU`. Its one officer (Derek Owens) and every other field stay
  byte-equal.
- **(B4) What a manager sees** (the DEPLOYED adapter serves each object; no redeploy -- ruling (c)): 6861's roster reason
  line and CEO line; CSL's roster reason line; **CAT's whole management block changes class, from SERVED (1 officer, no
  CEO) to ABSENT / `ROSTER_UNRESOLVED_NO_FALLBACK` / `roster_status INCOMPLETE-NO-CEO` / the Item 1D sentence /
  `officer_count 1`, with the officer table withheld** -- measured against the deployed bytes (`get-function` zip,
  `scoped_amgt.py` sha256 `9832f57a...` equal to the repo; `read_management`'s not-RESOLVED branch, repo `:2615-2634`).
  It is never served RESOLVED with no CEO (ruling s.4).

NOT moved (asserted by the order, AC8): the other 12 names' SERVED management blocks (sha256 before and after), every
other management key, `management/v1/_pool/` (3 objects, newest ETag `"7a1197377a0fff0e4e861ebc5208cf4a"`),
`raw/bloomberg/` (CAT 12, CSL 14, 6861 14 objects), `filings/v1/` (count unchanged), the crosswalk, the adapter function
and its artifact (CodeSha256 `hP+6OO5P...`), the portal.

### WRITER CENSUS -- the ACT's own write set, one call deeper, then the keys' writers

Z-S192 (rk-48's run wrote 2 raw Bloomberg stamps no half named, through enrich's fallback re-pull) is why the act's own
write set is counted first, one call below the entry point.
- **The act's S3 write set: N = 3, one per key.** Both modes write only through `write_document` (`crosswalk.write_pool`:
  one conditional `put_object`). Neither reaches `build_document`, `apply_bloomberg_fallback` (`write_raw` -- the
  raw-stamp writer), `bloomberg_fallback.*`, `prospecting_page`, `_lusha_client`, `compute_pool` or
  `write_pool_object`; `--rederive-roster-reason` also never reaches `ceo_search.*`. The order's test arms patch each of
  those to RAISE and assert exactly one put per run, and AC8 re-counts `raw/bloomberg/`, `_pool/` and `filings/v1/`
  live. `ceo_search.ceo_profile` makes NO S3 call. The reads (management objects, filings source objects via
  `roster.load_source_object`) write nothing. The schema file edit is repo-only, not an S3 write.
- **Writers of the three keys: 2 entry points, both in `enrich.py`** -- `enrich.main`'s build path and the re-projection
  / re-derivation modes (`--reproject-public-profile`, AMGT-rk-75; this order's `--research-stored-ceo` and
  `--rederive-roster-reason`). No round-20 order and no schedule runs the build path; the order runs its two modes
  once per key.
- **The served CEO line (6861) has 2 rules, both read:** `ceo_search.project_ceo_public_profile` (the producer's sentence
  table) and the adapter's `scoped_amgt.ceo_profile_reading` (`:2385`, `:2423-2470`). The adapter is unchanged.
- **The served management class (CAT) has 1 rule, read in the DEPLOYED bytes:** `read_management`'s four branches (no
  officers -> ZERO_OFFICERS; BLOOMBERG_FALLBACK -> SERVED fallback; `roster_status != "RESOLVED"` ->
  `ROSTER_UNRESOLVED_NO_FALLBACK`; else SERVED). `INCOMPLETE-NO-CEO` with 1 officer and `roster_source FILING` takes the
  third branch.
- **Other readers of `roster_status`, read:** `enrich.compute_pool` (`:760`) skips any non-RESOLVED roster (the tenure
  pool is NOT recomputed by this act; CAT's one officer carries no role start, so a later pool run is unmoved by it);
  `posture/packs.py:188` lists a non-RESOLVED roster as absent with its reason (truthful); `batch.py` counts RESOLVED
  only. `management.schema.json`'s `roster_status` enum gains `INCOMPLETE-NO-CEO` (one value).

### EXPECTED OUTCOME -- read from the producers' own rules, every branch

- **6861, searched branch (expected: `verified_site.host "www.keyence.co.jp"`):** the search runs once;
  `ceo_profile.ceo_name "Tetsuya Nakano"`, `name_source BLOOMBERG_FALLBACK`, and ONE of `CURATED` (-> `CONFIRMED`),
  `NOTHING_FOUND` (-> `SEARCHED_NOTHING_FOUND`), `UNREADABLE` (-> `SEARCHED_LINKS_UNREADABLE`), `SEARCH_FAILED` (->
  `SEARCH_FAILED`, the sentence keeping the "the SERP primitive raised" prefix -- named debt, ruling 2), each with its
  approved sentence. **Not-searched branch** (only if no `verified_site` at spawn): `NOT_SEARCHED / NO_VERIFIED_SITE`,
  zero spend. Every branch: `roster_reason` = *"The Japanese annual securities report (Yuho) was found, but its officer
  section is empty, so no officers could be read from the filing."*
- **CSL:** `roster_reason` = *"No filing could be matched to CSL: the SEC ticker belongs to a different company; the
  company files no recent 10-K with the SEC; no European (ESEF) annual report is filed under its LEI; neither the
  company website nor the ASX listing page led to an annual report within the crawl limit; and there is no
  national-regulator source for this listing yet."* (measured by prototype on the current filings object);
  `absence_reason_class` stays `pull-missed`; served SERVED (fallback) as today, reason line changed.
- **CAT:** `roster_status INCOMPLETE-NO-CEO`, `roster_reason` = *"The 10-K lists its executive officers in Item 1D,
  which was not read, so this roster is incomplete."*, `section_refers_to` = *"Information required by this Item
  appears in Item 1D of this Form 10-K."*; served ABSENT / `ROSTER_UNRESOLVED_NO_FALLBACK` / that sentence /
  `officer_count 1`. **If** a later spawn read found Item 1D held (branch A), CAT would instead be parsed from it --
  measured NOT held, so branch B is expected and is the one this half signs.
- **All three:** no served reason contains a literal `None`; each object validates against the schema (with the one new
  enum value); zero contact fields; the census after the act reads 0 of 15.
- **Refusal branches (nothing written for that key):** a stored query already set, an accession mismatch, a validation
  failure, a re-derivation that would move officers or a BLOOMBERG_FALLBACK status. **Cap branch (6861: spent, nothing
  written):** a cost over the cap -> BLOCKED.

### PER-KEY ROLLBACK

Read from THIS act's pre-act values (order AC3, bytes saved to the worker's `.scratch/rk79_pre/<key>.json`); the cut
values are shown for orientation only.
- **6861:** `copy_object` from the AC3 pre-act VersionId (`1Hm1g.MqxkFnnyRqLgQlwSiB925mRG9G` at the cut), then read back
  sha256 equal to AC3's.
- **CSL:** `copy_object` from the AC3 pre-act VersionId (`u_iDxPeXTBMyIMZtwYwJYVU53iwMdgiS` at the cut), read back.
- **CAT:** `copy_object` from the AC3 pre-act VersionId (`tJMJuD2oIO1ONv6dngrilLVgX4tOS3qU` at the cut), read back.
- No version is ever deleted. **The vendor spend** (6861): not reversible, bounded by the caps, covered by the word.
- **Everything else:** nothing to roll back -- the act writes nothing else.

Rollback trigger (any one, from AC8): a changed top-level key outside a key's allowed set; a moved officer list; a
moved sibling (any of the other 12 served blocks); a `raw/bloomberg/`, `_pool/` or `filings/v1/` count or ETag change;
`schema_valid False`; a contact field; a served literal `None`; a census after the act other than 0 of 15; CAT served
RESOLVED. Each written key is rolled back, the ledger legs close with the rollback proof, and a BLOCKING row is filed
(disarm_owner `2.0.0_SA_COO~Z`).

### NOT COVERED

This half does not cover, and the act may not perform: a second search or any retry beyond the code's own; any vendor
call on CSL or CAT; any key other than the three listed; a run dated other than `2026-09-19` (a new dated key no half
covers); a Lusha call; a Bloomberg call or any `raw/bloomberg/` write; an EDGAR fetch or any `filings/v1/` write; a roster
rebuild that changes officers (`build_roster` is used for reason fields only); any `_pool/` write; an edit to the adapter
or the portal (no redeploy -- ruling (c)); `_CEO_RE`; reading "President" as CEO for any non-JP listing; any
`roster_status` value other than the one added; deleting any S3 object version. **Named debt, not covered:** the
SEARCH_FAILED sentence's "the SERP primitive raised" prefix -- *"the next adapter redeploy moves ceo_profile_reading to
key on the reason_code field rk-75 added, and the prefix goes"* (msg 24049). The held branch `wk-amgt-14-50` is not
read or named as a surface.

**Signature (COO):** signed `2.0.0_SA_COO~Z`, 2026-09-21, at the round-20 issuance (the issuance commit's hash is
the signature's vintage).
