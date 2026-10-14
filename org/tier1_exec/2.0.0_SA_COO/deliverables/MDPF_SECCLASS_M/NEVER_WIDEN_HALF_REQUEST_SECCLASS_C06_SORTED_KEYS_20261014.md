# Never-widen half request -- C_06 writes `mix_daily_summary.json` with sorted keys (cell SC-e-102, rows D1-S37, D1-W92-S2..S4)

**Author:** `2.0.0_SA_COO~M1`, dell1, 2026-10-14 ~13:0xZ. **Cell:** `SC-e-102` (worker `0.9.0_WK_MDPF_SECCLASS~92`), drained @ee2cbf1023 (code commit `717405d44e`). **Ruling it serves:** XA-20261014T113939Z-a304 (laptop CTO 11:42:16Z): the
follow-up that C_06 writes JSON with sorted keys, under its own pair; CTO round-24 analysis section 4 item 3 (msg 5506). Claim words: `measured` = read this session; `held` = cited from a record.

## What is changed (the fix, built, LOCAL on `box/dell1`, not deployed)

One argument on one line, `C_06.client_mix_timeseries.py` `_write_mix_summary` (`:670`): `json.dumps(payload, sort_keys=True, separators=(',', ':'))`. Nothing else in the file; the other three `json.dumps` calls (watermark, relationship JSON, relationship views) are unchanged.
Tests: `tests/test_c06_sorted_keys_r25.py` (7 passed, including the difference control that the unsorted dump differs by insertion order) and the three sibling C_06 suites (30 passed, unchanged); both re-run by the issuer at trunk (measured).
Why: C_06 wrote the same parsed JSON with a different `advisors` byte order on every run, so the object's ETag moved each time (XA-a304; row D1-S37).

## The act (by a CloudOps lane, after both halves sign)

1. Open a change-management ledger before the act; close it at completion.
2. Deploy ONLY this file to `s3://opal-data-bd/code/gold/`, outside a BD gold run: `bash .tools/safe-deploy.sh data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`.
3. Precondition (measured 2026-10-14 ~13:0xZ, `head-object`): the served C_06 is ETag `f847d8d105025ffbee94b1aa5092faf6`, VersionId `jGO15I3AZTATLbGxE3_36dKm86wuggDK`, LastModified 2026-10-13T06:22:23Z, 66,473 bytes, and that equals the md5 of the file at the issuance base
   (`git show 3e1365fdaa:data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`). The built bytes have md5 `f884f28ddcaeda891dc67958210e88ad`. The deploy delta is exactly the one line.
4. Nothing from `lib/`, D_03, D_04, a table, a watermark or a data key rides the act. D1-S39 (a pair that ships `code/gold/lib/` names DB-b-181's classifier radius): this act ships one script and no `lib/` file, so it states that the served classifier is not in it.

## Blast radius

**The act writes:** one code object. **The first C_06 run after it writes** `gold/views/mix_daily_summary.json` (canonical bucket `opal-data-49financial`, key `advi/49financial/platinum/views/mix_daily_summary.json`) with the same content in sorted key order.
Measured on the served object now (VersionId `sB5iD9.LuxAWSYF77RFYvWY4uCbVSA1.`, 2026-10-14T11:27:24Z, ETag `afd57529819e7f511b5a2534600af5f3`): 2,296 firm dates and 56 advisors (74,034 advisor-days); the firm dates are already ascending; **the class keys are in alphabetical order on 0 of 2,296 firm dates; the advisor keys are not sorted.** So the bytes move on every firm date and advisor, and the content does not.
**Objects downstream of it whose bytes move once, with no content change** (D1-W92-S2; surveyed by the worker, `held`; line numbers re-read by the issuer, `measured`):
- `gold/artifacts/firm_mix_views_daily.json` and its legacy alias: `D_03.composition_artifacts.py:510-518` writes `firm_daily` in iteration order;
- every `gold/entities/advisors/{id}/mix_daily.json` (56) and each legacy alias: `D_03:558-565`;
- `platinum/firm/mix_summary.json`: `D_04.client_portal_summary.py:578` (D1-W92-S3): D_04 sums the class values in snapshot order, so a different order can move the composition total in its last float digit. **Measured bound:** over all 2,296 firm dates the largest absolute difference between the insertion-order sum and the sorted-order sum of the class values is **2.4e-7 dollars**. The claim is that the served total moves by at most $0.000001.
**Not touched:** the relationship JSONs and views, the watermark, `etf-classifications`, the period views (`lib/mix_views.py:68,74` sort their input), E_25 (reads the wrong key `firm_daily` and returns its error dict; D1-W92-S4, unchanged by the act).

## Writers

**Writers of `gold/views/mix_daily_summary.json`: N = 1** -- `C_06 _write_mix_summary` (`:663-676`, put at `:673`), called by the retained pass and the merge path. **Writers of `gold/artifacts/firm_mix_views_daily.json`: N = 1** (`D_03:510-518`, with its legacy alias).
**Writers of `gold/entities/advisors/{id}/mix_daily.json`: N = 1** (`D_03:558-565`, with its legacy alias). **Writers of `platinum/firm/mix_summary.json`: N = 1** (`D_04:578`). Counted by reading the call sites of the key constants (`FIRM_MIX_VIEWS_DAILY`, `advisor_mix_daily_key`, `platinum/firm/mix_summary.json`) in `data/black_diamond/scripts/gold/[A-E]_*.py`, 2026-10-14.

## Both branches of the expected outcome

- **Branch 1, a C_06 run on UNCHANGED inputs after the deploy:** `mix_daily_summary.json` parses EQUAL to the pre-act version (canonical-JSON equality, per XA-a304) and its body equals its own sorted dump (md5 of the served body equals md5 of `json.dumps(json.loads(body), sort_keys=True, separators=(',', ':'))`); a SECOND such run leaves the ETag unchanged (byte determinism). This is the act's proof and it needs no fire.
- **Branch 2, the first scheduled fire after the deploy (new inputs by design):** the D_03 families and D_04's object change content only through the fire's own new date and any AUA restatement, which the read-back separates: for every date and every advisor-day that the fire did not re-derive, the content equals the pre-fire version under canonical-JSON equality; the key order in the written objects is sorted; D_04's composition total differs from a recompute in the same order by at most $0.000001.
- A state outside both (content of an untouched date changes, a key outside the named families moves, or the sum differs by more than $0.000001) is a STOP and a code rollback.

## Rollback

Code: restore the prior object by VersionId `jGO15I3AZTATLbGxE3_36dKm86wuggDK` (ETag `f847d8d1...`), then `safe-deploy.sh` of that file's base bytes. Data: leg P (the ship's pre-act read) enumerates the current VersionIds of the four families above (mix daily summary; firm_mix_views_daily and alias; the 56 advisor `mix_daily.json` and aliases; `platinum/firm/mix_summary.json`) with page and key counts printed;
the mix daily summary's restore target today is `sB5iD9.LuxAWSYF77RFYvWY4uCbVSA1.` (ETag `afd57529`). A code rollback restores behaviour, not bytes a run already rewrote; a restore by VersionId does.

## Reach

Objects whose bytes move at the first run that writes them: 1 (the mix daily summary, C_06) then 1 + 1 alias + 56 + 56 aliases + 1 downstream (D_03 and D_04) at the first fire; content moved: none by the act. The act changes no dollar figure, class, advisor total or period bar.

## COO half: UNSIGNED

Left for `2.0.0_SA_COO~M1` (signed in the sibling file once the re-base read of the 23:00Z fire is in).

## CTO half: UNSIGNED

Left for `1.0.0_SA_CTO`. Read: the named file only; the blast radius (bytes of the four families move once, content does not; D_04 total at most $0.000001); the writer counts (N = 1 each); both branches; the rollback per key.
