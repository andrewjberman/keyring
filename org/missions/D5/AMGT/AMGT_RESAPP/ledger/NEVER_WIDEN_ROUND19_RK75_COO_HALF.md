# AMGT_RESAPP round 19 -- never-widen pair, `AMGT-rk-75` -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: SIGNED at issuance.** The CTO half is
owed by `1.0.0_SA_CTO~Z` at `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND19_RK75_CTO_HALF.md`, under a
heading naming `AMGT-rk-75`. The order's AC1 refuses to act on one half.
**Sources:** decomposition s.27; the rk-48 as-landed pair `ledger/NEVER_WIDEN_RK48_AS_LANDED_HALVES.md` (CTO @1ed2e24638,
COO @0b71e7f5ab); `ledger/ROUND_ANALYSIS.round18.md` s.4 @5f10ddf969 `:61-70` (re-projection RULED, plain-English
reader sentence, CSL's sentence given verbatim); row `AMGT_RESAPP-Z-S192`; msgs 23976, 24007, 24011, 24015; the order
`task-orders/AMGT_RESAPP.TO-AMGT-rk-75.readable-not-searched-reason.md`.
**Measured at the cut:** 2026-09-21, read-only, by the issuer, at HEAD `54066b102b`, the sentences re-measured at `5f10ddf969`. The order's AC3 re-reads every value
at spawn; where a re-read differs, the ROLLBACK TARGET is the worker's AC3 value, never this file's.

## `AMGT-rk-75` -- the readable NOT_SEARCHED reason, re-projected in place

### THE ACT

ONE run, by `0.9.0_WK_AMGT_RESAPP~75`, of `enrich.main([... "--as-of", "2026-09-19", "--reproject-public-profile",
"--write-pool"])` for each of three names, with `BRIGHT_DATA_API_KEY`, `LUSHA_API_KEY` and `ANTHROPIC_API_KEY` unset
(order AC5). The mode GETs each stored object, replaces ONLY `ceo_public_profile` with the new projection of the
object's own stored `ceo_profile`, validates, and writes through `enrich.write_document`. Ledgered under slug
`amgt-rk75-readable-not-searched-reason`, opened before the first write and closed on the read-back.

### BLAST RADIUS

What the act MAY move, and nothing else:
- **(B1) Three keys, one new version each:** `s3://opal-data-harvest/management/v1/{CAT_US_Equity,CSL_AU_Equity,
  6861_JP_Equity}/2026-09-19.json`. At the cut each has 2 versions and 0 delete markers, and the latest are CAT
  `Gb71vifhZHBDVpvq2ZGODr.WwZg.j.VW`, CSL `YOJ.tfyEZbNNVLc.XW2Z9e1w64kyAepe` and 6861
  `HQl_.COQdPLdSopmRf.tQisuZF0LsMjR` (the rk-48 as-landed state RETAINED by the pair above). The new version differs
  from its predecessor ONLY at `ceo_public_profile.basis` (the code string becomes the plain-English sentence from
  the producer's ONE table `ceo_search.NOT_SEARCHED_SENTENCES`, keyed by reason code) and
  `ceo_public_profile.reason_code` (added). The written sentences: CAT and 6861 `"No officer on the roster has a chief-executive title, so the CEO web search was not run."`; CSL `"No verified company website was found, so the CEO web search was not run."` (the CTO's words).
  `ceo_profile`, including its own `reason`, is NOT changed. Measured on a scratch simulation of the ruled table over
  the three live objects: changed top-level `["ceo_public_profile"]` and changed leaves `["basis", "reason_code"]`, 3
  of 3; `ceo_profile` byte-equal 3 of 3; schema-valid under the patched schema 3 of 3.
- **(B2) The served reason line, CAT only.** On `/api/scoped/amgt/security/CAT_US_Equity/thesis`,
  `management.ceo_profile_reading.reason` moves from `"NOT_SEARCHED / NO_CEO_ON_ROSTER -- 0 url(s), 0 fact(s)
  verified of 0 proposed"` to `"No officer on the roster has a chief-executive title, so the CEO web search was not run."`, and
  `management.ceo_public_profile` gains `reason_code`. `reading` stays `NOT_SEARCHED` and `urls_returned` stays None:
  the adapter's `returned (\d+) url` regex (`scoped_amgt.py:2374`) matches neither the old nor the new text.
  **CSL and 6861 move nothing served BY THIS ACT**: `read_management` serves the CEO block only for a resolved
  roster with officers (`scoped_amgt.py:2512-2530`), and both read `management_status ABSENT / ZERO_OFFICERS` live at
  the cut. **R19-C (`AMGT-rk-77`, same round, row Z-S194) changes that rule and redeploys the adapter under its OWN
  pair**; once it lands, CSL's and 6861's CEO reading is served with the sentences above. That change is R19-C's act
  and R19-C's blast radius, not this half's: this act writes no adapter path and R19-C writes no management object.
  The order's AC6 passes in either drain order.

NOT moved, and asserted by the order's AC6:
- `ceo_profile` (byte-equal) and every other top-level key, including `generated_at`, `officers`, `fallback` and
  `lusha_enrichment`;
- any other dated key (the as-of is pinned to 2026-09-19);
- `management/v1/_pool/` (3 objects, newest `2026-09-19.json`, ETag `7a1197377a0fff0e4e861ebc5208cf4a`);
- the raw Bloomberg population, whose object counts under `raw/bloomberg/<key>/` are CAT 12, CSL 14 and 6861 14
  (exec_officers stamps 0 / 2 / 2);
- the adapter Lambda, which is not redeployed;
- any other name's object.

### WRITER CENSUS -- the ACT's own write set first, one call deeper (row Z-S192's lesson), then the keys' writers

**The act's write set: N = 3 S3 writes, one per key.**
- The re-projection mode's only writer is `enrich.write_document` (`enrich.py:792-795`), which calls
  `crosswalk.write_pool` (`crosswalk.py:839`).
- One level deeper: that is ONE conditional `put_object` (`IfMatch` the current ETag), plus `head_object` reads. It
  skips the put when the stored `document-sha256` already equals the payload, so a re-run after success writes nothing.
- The mode reaches none of the paths below. The order's test arm `test_reproject_changes_only_the_projection` patches
  each of them to RAISE and still passes, and AC6 checks the raw count directly, live:

| path the mode does NOT reach | what a plain `--write-pool` re-run would do there (measured at HEAD) |
|---|---|
| `build_document` | rebuild the roster from the filings source; CSL's was rewritten by rk-72 @c1fdd952e1 |
| `apply_bloomberg_fallback` / `bloomberg_fallback.pull_exec_officers` | a LIVE Bloomberg `ReferenceDataRequest` for CSL and 6861, plus a NEW `raw/bloomberg/<key>/<stamp>/exec_officers.json` each, because `write_raw = args.write_pool` (`enrich.py:859-860`, `bloomberg_fallback.py:147-180`). This is exactly the unnamed write Z-S192 recorded |
| `prospecting_page` / `_lusha_client` | none here: all three read `SKIPPED`, with no declared domain in `domains.json` |
| `_serp_module` | none here: every `ceo_profile` is NOT_SEARCHED, and the environment carries no key |
| `compute_pool` / `write_pool_object` | skipped; the mode never writes the pool |

**The keys' writers: 3 call sites, all through `enrich.write_document`:**
- `enrich.main` (`:908`), which is this act, in the new mode;
- `lib/research/management/batch.py:170`;
- `integrations/bloomberg/research/management_posture_batch.py:223`.

No round-19 order and no schedule runs either batch.

**The served value's rules: N = 2, both read.**
- The producer's projection: `project_ceo_public_profile` with the ONE table `NOT_SEARCHED_SENTENCES` (4 codes, the
  subtraction in the order's section 1: 11 values minus 7 set only under another status), and a named fallback (the
  stored reason, else the old composed string) for any code the table lacks. The ONE production call site
  (`enrich.py:640`) and this act's mode both call it, so a future live run writes the same sentence.
- The adapter's `ceo_profile_reading` (`scoped_amgt.py:2388-2440`) plus the `read_management` resolved-roster gate
  (`:2512-2530`).

### EXPECTED OUTCOME -- read from the producer's and the adapter's own rules, both branches

- **Branch A, the pre-act state as measured** (3 of 3 `ceo_profile.status NOT_SEARCHED`, `serp_requests 0`, VersionIds
  equal to the cut): every key gains one version with the two-leaf diff above. CAT's served reason becomes the
  table sentence. CSL and 6861 are unchanged on the served route while R19-C is undeployed, and serve the table
  sentence once it is. Pool and raw counts are unchanged.
- **Branch B, any pre-act value differs** (a writer moved a key since the cut, or a status is not NOT_SEARCHED): the
  order's STOP RULE fires at AC3. No ledger entry opens and nothing is written.
- **Branch C, a key's stored bytes already equal the new payload:** `crosswalk.write_pool` performs no put, and that
  key keeps 2 versions. AC6 would then read `versions 2 was 2`, which is correct for that key and is reported as such.

### PER-KEY ROLLBACK

Read from THIS act's pre-act values (the order's AC3, saved to the worker's `.scratch/rk75_pre/`). The cut values
above are for orientation only.
- **Each of the three keys:** `copy_object` from its AC3 pre-act VersionId (CAT `Gb71vifh...`, CSL `YOJ.tfyE...`, 6861
  `HQl_.COQ...` at the cut), then read back sha256 equal to the AC3 baseline. No version is deleted.
- **Served value:** restored by the key rollback, since no other store holds it.
- **Pool, raw stamps, adapter, other names:** nothing to roll back, because the act writes none of them.

Rollback trigger, any one of:
- a changed top-level key other than `ceo_public_profile`;
- a changed leaf other than `basis` or `reason_code`;
- `ceo_profile` not byte-equal;
- a failed schema validation;
- a moved raw count;
- a new dated key;
- a moved pool object;
- a served reason (CAT, or CSL / 6861 once R19-C is live) not equal to its table sentence.

The ledger leg then closes with the rollback proof, and a BLOCKING row is filed.

### NOT COVERED

This half does not cover, and the act may not perform:
- any enrich run without `--reproject-public-profile`;
- `build_document`;
- a Bloomberg, Lusha, SERP or model call;
- any other as-of;
- any other name, including a batch or fleet run;
- a `_pool/` write;
- any change to `scoped_amgt.py` or an adapter redeploy;
- a portal change;
- deleting any object.

The held branch `wk-amgt-14-50` shares two file NAMES with this order's write surface (`enrich.py`,
`management.schema.json`). It is not read, and it is not a surface of this act.

**Signature (COO):** signed `2.0.0_SA_COO~Z`, 2026-09-21, at the round-19 issuance (the issuance commit's hash is
the signature's vintage).
