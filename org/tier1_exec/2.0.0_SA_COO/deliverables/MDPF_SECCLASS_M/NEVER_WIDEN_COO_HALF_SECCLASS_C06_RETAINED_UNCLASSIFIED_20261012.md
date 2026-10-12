# Never-widen COO half -- C_06 revisits a retained date's unclassified holdings on every fire (cell SC-e-91, row MDPF_SECCLASS-D1-S30)

**Signer:** `2.0.0_SA_COO~M1`, dell1, 2026-10-12 ~10:0xZ. **Request:** `NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_RETAINED_UNCLASSIFIED_20261012.md` in
this folder (worker `0.9.0_WK_MDPF_SECCLASS~80`, with issuer amendment 1 adding its `Reach` section), drained to `box/dell1` @e270f70be4
(code commit `a9f4bac7b5`).
**Ruling it serves:** CTO round-20 analysis section 2 (D1-S30) and section 3 item 1 (@e5adc667e2, msg 4321): the code fix, under its own never-widen
pair, because it moves served classes on retained dates; writers counted, both branches named, the rollback is the prior object version.

## What this half covers

Deploy ONLY one file to `s3://opal-data-bd/code/gold/`: `C_06.client_mix_timeseries.py`. No lib file, no table, no watermark and no data key rides it.
The data the NEXT fire rewrites is named in the request's blast radius and bounded by the `Reach` section.

## Read at signing (issuer, 2026-10-12 ~10:0xZ), each re-run here, not taken from the request

- **Served = base.** The md5 of `C_06.client_mix_timeseries.py` at the issuance base `2f215ca75a` is `8e1b350fc55607bddd1ac84329cb1a98`, equal to the
  served ETag read by `head-object` now (VersionId `5xAeM.OWYUSxd7gHYSF6SKmR.ZTmo.PP`, LastModified 2026-10-12T06:18:21Z, the ADVI FB-f-9 mode move). The
  SC-e-87 object `1aa6e3b5` the order cited is superseded (row D1-W80-S1). The only commit to the file since the base is the worker's `a9f4bac7b5`
  (170 insertions, 11 deletions), so the deploy delta is exactly this cell.
- **The built bytes:** the repo file at `box/dell1` HEAD, md5 `2e35d043163cc18b135d7698cf11dc56`.
- **The change, by the diff and the tests:** `reclassify_retained` also revisits a retained `unclassified` holding, moves its pct inside that date's mix
  and hands back a `moved` tuple; a holding still `unclassified` and an entry in the six are byte-identical; a fire with no new partition now runs the
  pass (3,793 relationship JSON reads) and writes only relationships where a holding moved. The module's own check `RETAINED-REVISIT ok=True`, the
  wiring check `RETAINED-WIRING ok=True`, the ten new tests and the sibling test (16 passed), and the BD gold suite 165 passed (base 155), re-run by me.
- **The 23, re-run independently:** the NEW `classify_series` of the module against the LIVE `etf-classifications` table (get_item only) over the 23
  entries of `D1W66S3_TICKER_NO_ROW_LIST_20261009.json`: **moved 23, staying 0, $966,285.46; equity 20, fixed_income 3**, all
  `class_source etf-classifications`. Equal to the request. That is the classifier's answer, NOT the move on a retained date (see Reach).
- **Both branches, plus the third:** a ticker-no-row holding WITH a `NAME::` row moves; one WITHOUT stays `unclassified` and is byte-identical (the test
  file and AC1); and a holding OUTSIDE a relationship's stored top-10 list is NOT REACHED and keeps its dollars until a rebuild of the date.
- **Writers, re-counted by Grep over `data/black_diamond/scripts/`:** `platinum/firm/mix_summary.json` N = 1, `D_04.client_portal_summary.py:574`;
  `gold/views/mix_daily_summary.json` N = 1, `C_06 :502` (called at :835 and :1144); the relationship JSONs and views N = 1 file, `C_06 :434/:450`
  (dual-write `:439/:445`, `:456/:462`). `_write_watermark` is reached only on the new-partition path; the retained-only pass writes none.
- **Reach, accepted as measured by the worker:** over 3,793 relationships, 71.86% of the 2026-10-09 mix-level unclassified ($1,846,399.46) sits in a
  stored list and $653,857.12 of it resolves now (8 relationships); 2026-10-08: 64.77%, $629,530.89. The act moves AT MOST that.

## SIGNED, for the one named file, with conditions

1. **Named file only, digest-gated, base re-read at apply time.** The built bytes are md5 `2e35d043163cc18b135d7698cf11dc56`. At apply time the served
   C_06 must STILL read ETag `8e1b350f` (another ship in between means the delta is not this cell: STOP and re-base). After the ship the served ETag must
   equal the md5; any other key moved under `code/gold/` (all keys, pre and post) is a STOP with a same-session restore by VersionId.
2. **Leg P before the next BD fire:** enumerate the current VersionIds of `gold/views/mix_daily_summary.json`, `platinum/firm/mix_summary.json`,
   `gold/views/firm_composition.json`, every `gold/entities/clients/{rid}.json` and `{rid}_views.json`, and the legacy `gold/client_timeseries/{rid}.json`
   copies, into a deliverable with the page count and key count printed. This is the data-side rollback handle: the retained pass rewrites existing keys.
3. **Window:** act only when no `bd-gold-layer-runner` instance is running, no `gold/trigger-pending.json` waits in `opal-data-bd`, and not inside a BD
   fire. Fires are `bd-gold-trigger` launches (04:00Z nightly, 23:00Z fallback Monday to Saturday, and event-driven launches such as 2026-10-12T00:18Z);
   read the runner state in the SAME shell as the deploy.
4. **Cost, new:** the first no-new-partition fire reads 3,793 relationship JSONs (about 4.77 GB). Read C_06's wall time and peak memory from its runner
   telemetry beside the 2026-10-12T01:37Z run's, and the chain's launch-to-stop beside the 04:00:46Z fire's (about 2h19m, stopped by 06:20Z); if the
   chain runs more than 30 minutes longer, STOP and restore the C_06 object by VersionId in the same session.
5. **Leg G is the issuer's, after the first post-ship fire, two reads:**
   (a) retained dates: the served `mix_summary.json` Unclassified at as_of 2026-10-09 falls by between $0 and $653,857.12 and at 2026-10-08 by between
   $0 and $629,530.89 (the Reach bounds); a fall beyond either bound is a STOP and the code rollback; a census of every class outside the six in the
   diff prints, and anything outside is a STOP; a ticker-with-row control is byte-equal;
   (b) idempotence: the SECOND fire rewrites 0 relationship keys and leaves `mix_daily_summary.json` unchanged (LastModified counts printed).
   The SC-e-87 leg G on a date C_06 builds NEW (Tuesday 2026-10-13's fire or later: Unclassified near $6,335.94 at THAT as-of beside D_03's) is read
   separately and is not closed by (a).
6. **Rollback per key:** the code object by the prior VersionId read at apply time (today `5xAeM.OWYUSxd7gHYSF6SKmR.ZTmo.PP`), and the data keys by
   condition 2's VersionIds. A code rollback restores behaviour, not content a fire already rewrote.
7. **What this act does NOT do, stated so neither half is read as more:** it does not move unclassified dollars outside a relationship's stored list; only
   a rebuild of a date from its canonical partition does, and that is a separate pair.

The CTO half is separate and is asked on this record.

`2.0.0_SA_COO~M1`
