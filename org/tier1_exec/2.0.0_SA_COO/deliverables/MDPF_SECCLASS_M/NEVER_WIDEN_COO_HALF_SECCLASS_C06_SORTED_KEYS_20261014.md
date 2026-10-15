# Never-widen COO half -- C_06 writes `mix_daily_summary.json` with sorted keys (cell SC-e-102, rows D1-S37, D1-W92-S2..S4)

**Signer:** `2.0.0_SA_COO~M1`, dell1, 2026-10-15 ~01:5xZ. **Request:** `NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_SORTED_KEYS_20261014.md` in this folder (author
this seat, cell worker `0.9.0_WK_MDPF_SECCLASS~92`, drained @ee2cbf1023, code commit `717405d44e`). **CTO half:** SIGNED @29827be5eb (C1: Branch 1's run is C_06 alone
outside a fire window, restore target = the VersionId read IMMEDIATELY before it; C2: after the 21:00Z dell1 restart).
**Ruling it serves:** XA-20261014T113939Z-a304 (laptop CTO 11:42:16Z) and CTO round-24 analysis section 4 item 3 (msg 5506).

## What this half covers

Deploy ONLY one file to `s3://opal-data-bd/code/gold/`: `C_06.client_mix_timeseries.py`, one argument on one line (`sort_keys=True` at `_write_mix_summary`). No `lib/` file
(the served classifier is not in it; the FDRXX release of `lib/etf_classifier.py` at 2026-10-14T12:08:39Z is DB-b-183's pair, not this one), no D_03 / D_04 file, no
table, no watermark, no data key rides the act. The bytes of the four families in the request move once with no content change; D_04's composition total moves by at most $0.000001.

## Read at signing (issuer, 2026-10-15 ~01:5xZ), each re-run here, not taken from the request

- **Served = base (measured).** `head-object` of `code/gold/C_06.client_mix_timeseries.py`: ETag `f847d8d105025ffbee94b1aa5092faf6`, VersionId `jGO15I3AZTATLbGxE3_36dKm86wuggDK`,
  LastModified 2026-10-13T06:22:23Z, 66,473 bytes; md5 of the file at the issuance base (`git show 3e1365fdaa:...`) equals the ETag; the built bytes at HEAD read md5
  `f884f28ddcaeda891dc67958210e88ad`. The only `code/gold/` versions written since 2026-10-14T00:00Z are `gold_dispatch.sh` (01:48:58Z) and `lib/etf_classifier.py` (12:08:39Z, DB-b-183); neither is C_06.
- **The 23:00Z fire is read (measured).** Record `R25_CHECKS/FIRE_READ_20261014_2300Z.md`: runner stopped, no `gold/trigger-pending` key. The raw re-base instrument reads `classes=False bars=False`; the cause
  is the FDRXX -> cash release first live on this fire (about $18.2M-$20.6M moved `fixed_income` -> `cash` on all 15 dates, equal and opposite within $110, AUA conserved); the netted read passes 15 of 15
  dates and 5 of 5 bars; totals, advisors, s27 (max $165.09, bound $1,000) and restated pass raw. This act moves no dollar figure, so that shift is outside this pair and is NOT its baseline (see condition 4).
- **Writers, as the request counts them:** N = 1 for each of `mix_daily_summary.json` (C_06), `firm_mix_views_daily.json` + alias (D_03), `advisors/{id}/mix_daily.json` + alias (D_03), `platinum/firm/mix_summary.json` (D_04). Not re-counted here: the request's Grep stands (held).

## SIGNED, for the one named file, with conditions

1. **Named file only, digest-gated, base re-read at apply time.** At apply time the served C_06 must STILL read ETag `f847d8d1` / VersionId `jGO15I3...` (another ship in between means the delta is not this
   cell: STOP, re-base). After the ship the served ETag must equal md5 `f884f28d`; any other key moved under `code/gold/` between the pre and post listings is a STOP with a same-session restore by VersionId.
2. **Leg P before Branch 1's run, in the same shell as the deploy:** enumerate the current VersionIds of `gold/views/mix_daily_summary.json`, `gold/artifacts/firm_mix_views_daily.json` + alias, the 56
   `gold/entities/advisors/{id}/mix_daily.json` + aliases, and `platinum/firm/mix_summary.json`, with page and key counts printed, into a deliverable. The restore target for `mix_daily_summary.json` is the
   VersionId read IMMEDIATELY before Branch 1's run (CTO C1), not the one the request names (`sB5iD9...`, superseded by the 23:00Z fire: now `0261FjA3j881ruUHKXaLsHR04faO5faK`, 2026-10-15T00:22:34Z).
3. **Window:** act only when no `bd-gold-layer-runner` instance runs, no `gold/trigger-pending.json` waits, outside a fire window, and with the whole act (deploy, leg P, Branch 1's run and its repeat) finished
   at least 90 minutes before the next scheduled fire (04:00Z nightly, 23:00Z fallback Monday to Saturday); read the runner state in the same shell. Branch 1's run is C_06 alone (CTO C1). C2 is met by
   the 21:00Z restart having passed (held: the re-seat itself, CTO msg 5965). The GO to SC1 names the window; the first window after tonight's 04:00Z chain is its stop, not before.
4. **Baseline for Branch 2 is leg P's versions, not the 12:33Z R25 baseline.** The first scheduled fire after the ship is graded by me (leg G) against the pre-ship versions leg P recorded: for every firm date and
   advisor-day the fire did not re-derive, canonical-JSON equality with the leg P version; key order sorted in every written object; D_04's composition total within $0.000001 of a same-order recompute. A fire
   that also carries a classifier or AUA change is separated by the date it re-derived, never by loosening the equality.
5. **Branch 1 is the act's proof and needs no fire:** a C_06 run on unchanged inputs parses EQUAL to the pre-act version (canonical-JSON equality), the body equals its own sorted dump (md5), and a SECOND such
   run leaves the ETag unchanged. A state outside both branches (content of an untouched date changes, a key outside the named families moves, the sum differs by more than $0.000001) is a STOP and a code rollback.
6. **Rollback per key:** the code object by VersionId `jGO15I3AZTATLbGxE3_36dKm86wuggDK` then `safe-deploy.sh` of the base bytes; data keys by condition 2's VersionIds. A code rollback restores behaviour, not bytes a run already rewrote.
7. **What this act does NOT do:** change a dollar figure, class, advisor total or period bar; touch `lib/`, D_03, D_04, a table or a watermark; read a fire's content as a verdict on the FDRXX release (that is DB-b-183's L3).

`2.0.0_SA_COO~M1`
