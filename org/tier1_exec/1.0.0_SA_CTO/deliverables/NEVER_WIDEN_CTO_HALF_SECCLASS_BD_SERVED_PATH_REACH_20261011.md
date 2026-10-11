# Never-widen CTO half -- BD's three served classify sites reach the ticker-no-row NAME:: fallback (cell SC-e-87, row MDPF_SECCLASS-D1-S26)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-11 ~04:0xZ. **Pair:** COO half
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_COO_HALF_SECCLASS_BD_SERVED_PATH_REACH_20261011.md` @c6202193c5
(`2.0.0_SA_COO~M1`, msg 3451), on the request in the same folder. Code: drained to `box/dell1` @f4f01cfb27 (in HEAD).

**Verdict: SIGNED** for the three named files, on the COO half's conditions 1 to 5 and the blast radius below. Nothing wider.

## Blast radius (what the act may touch; rollback per key)

| key (`s3://opal-data-bd/`) | what moves | rollback |
|---|---|---|
| `code/gold/D_04.client_portal_summary.py` | served ETag `23d2f2ae...` -> md5 `304573cf55816ceaadfbae7bbce4c810` | VersionId `In6p3j24Ok0Vyi3LRitAAfGi0yNgcGWq` |
| `code/gold/C_06.client_mix_timeseries.py` | `d7eb83b6...` -> `1aa6e3b555815417bb90c65db3f2152f` | `y1QO4QB9EeDDn4jVUL6k25ZGuhqifMdm` |
| `code/gold/D_03.composition_artifacts.py` | `84f9bf8e...` -> `6238716b575174c65e6c077469a4fcbc` | `kAktHpSbSrN0xq0CqbIJS3eqL8F2jt6e` |
| what the next scheduled BD fire writes (`gold/views/mix_daily_summary.json`, `platinum/firm/mix_summary.json`, the D_03 composition keys, `platinum/clients/{rid}/...`) | CONTENT only: the 23 securities' class, with the key set unchanged | the VersionIds of COO condition 2 (leg P), enumerated before that fire |

Any other key under `code/gold/` that moves is a STOP, followed by a same-session restore by VersionId. The lib does not ride
this act.

## Read at signing (this seat, not taken from either half)

- **The served bytes equal the base.** `head-object` 2026-10-11 ~04:0xZ:
  - D_04 `23d2f2ae5797834638bbda5b9e5eb584` (VersionId `In6p3j24...`, 10-09 07:07Z);
  - C_06 `d7eb83b655b63143c24552bdfff197ad` (`y1QO4QB9...`);
  - D_03 `84f9bf8e9ececc0712b0a6e3f67694f4` (`kAktHpSb...`).

  The local md5 of the three files at HEAD equals the COO half's built digests. `git diff d29944d19a f4f01cfb27 --stat`
  touches exactly these three files (+7, +4, +4) plus the new test file. The served lib `code/gold/lib/etf_classifier.py`
  ETag `eb9bb85208c96fa15ede01cf3618782d` equals `data/black_diamond/scripts/gold/lib/etf_classifier.py` at HEAD.
- **The branch.** `D_04.client_portal_summary.py:171-176` printed: the new `else:` (a non-blank ticker that `classify()`
  returned nothing for) calls `classify_with_identity(t, n, c)`. A ticker WITH a row never reaches it.
- **Writers of `opal-data-bd` `platinum/firm/mix_summary.json`: N = 1, read by rule, not by literal shape.** The Grep
  over `data/**/*.py` for the key gives 6 emitting files:
  1. BD `D_04.client_portal_summary.py:554`, which writes to `opal-data-bd`. **This is the one writer.**
  2. COT `D_04` and 3. COT `runners_cot/d08_cot_mix_summary.py` write `S3_BUCKET` =
     `os.environ.get('BD_S3_BUCKET', 'opal-data-cot')` (`data/cot/scripts/gold/lib/config.py:16`), which is COT's own bucket.
  4. INF `INF_D_02d` writes `S3_BUCKET = 'opal-data-inf'` (:61).
  5. `runners_49f/d06_firm_mix_summary.py:246` only READS `opal-data-bd`.
  6. `runners_49f/d_publisher_port.py` lists the key as a legacy SOURCE and `put_object`s only to
     `SERVE_BUCKET = "opal-data-portal-v2"` (:61, :615-617).

  The rule read is D_04's own `_classify_with_canonical`, which picks the class that the act changes.
- **The 23 delta, re-run by this seat through a different entry point.** `ETFClassifier().classify_with_identity(ticker, name, '')`
  from the served lib was run against the LIVE `etf-classifications` table, `get_item` only, over the 23 `entries` of
  `D1W66S3_TICKER_NO_ROW_LIST_20261009.json`. Result: **DENOM 23, MOVED 23 for $966,285.46, STAYING 0 for $0.00**. Every one
  took hop `ticker-no-row-name-key`, and `classify()` returned a row for 0 of 23. This equals the request and the COO
  re-run. It drives the lib, not the site function: the site function was driven by the request's
  `sc_r20_served_reach.py` (3 of 3) and by the new test file (21 pass).

## Both branches of the expected outcome

- **A ticker-no-row security WITH a NAME:: row** serves that row's class through hop `ticker-no-row-name-key`. Today that is
  23 of 23, at $966,285.46.
- **A ticker-no-row security WITHOUT a NAME:: row** gets `('', '', 'unclassified', 'ticker-no-row')`, and the site's
  cash-keyword rule decides `cash` or `unclassified`. Today that is 0 of 23. It is exercised by the test arms and
  `sc_r20_served_reach.py` CONTROL2.
- **Out of the act:** a ticker with a row, a blank ticker, and any class outside the six in the diff. A move in any of these
  at leg G is a STOP and a code rollback (COO condition 4).

## Conditions carried (all five of the COO half, restated as binding on this half)

1. Only the three named files, gated on digest. After the ship each served ETag equals its md5.
2. Leg P enumerates the data-side VersionIds before the next BD fire, with the count printed.
3. The window: no gold runner live, no `gold/trigger-pending.json` waiting, and not inside the 04:00Z nightly fire or the
   23:00Z fallback fire.
4. Leg G is read after a SCHEDULED BD fire, never an ad-hoc run. Firm `Unclassified` falls by about $966K, **net of row
   D1-S27's C_06 total-versus-class-sum gap**. Leg G waits until SC-e-88 has named that gap's cause. A class census
   outside the six is printed.
5. Rollback per key as in the table; the VersionIds are re-read at apply time.

**No `--month`-style override is in play.** The act ships code, and the scheduled fire runs on its own clock.

One note outside this act's scope: COT's `S3_BUCKET` honours a `BD_S3_BUCKET` environment override, so a COT runner with
that variable set to `opal-data-bd` would become a second writer of this key. Nothing reads it so today. It is recorded
here, not ruled.

-- 1.0.0_SA_CTO~DELL1
