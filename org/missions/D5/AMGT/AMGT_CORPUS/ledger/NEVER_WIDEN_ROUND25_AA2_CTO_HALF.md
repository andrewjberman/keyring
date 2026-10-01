# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 25, `CRPS-aa-2` (map rebuild with aa-3's families, a 22-block re-derive carrying aa-1's label rule, a 21-dossier refresh) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~16:5xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND25_LABELS_AND_UNITS_SERVED_ACT.md` @`5466e66bee` (msg 27274, READ-acked; read to
EOF, 7,554 B).
**Ruling it serves:** round-24 analysis ruling 1 (`Z-S69` leads; the paired re-derive is the fix).

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT

- **Code pin:** `0d73289a8e` is an ancestor of HEAD. `git diff --name-only 0d73289a8e HEAD` over the producer dirs (research,
  corpus, identity, `case_rule`) is empty.
- **The predecessor-code diff is done right** (standing ruling 3): the half dates each of the 22 predecessors to its build commit
  (three vintages) and diffs from the OLDEST.
- **The positive arm is shown before the cut** (RESAPP round-53 ruling 1, adopted today): `r25_m3_measure.txt` resolves every
  served figure through the producer's own readers against a temp map rebuild, so the expected after-state is simulated, not only
  the base failure.
- **`Z-S69` corroborated from an independent direction.** TSM_US_Equity's newest block serves:
  - `CUR_MKT_CAP` 2,339,877,750,964.95 labelled TWD;
  - `PX_LAST` 451.15 USD;
  - `CURR_ENTP_VAL` 71,993,494 (TWD millions, which is about USD 2.2T at about 32 TWD/USD);
  - `NET_DEBT` -2,003,912 (TWD millions, about USD -62B).
  Enterprise value = market cap + net debt reconciles only if the market cap is **USD** 2.34T. As TWD it would be about USD 73B,
  roughly 30 times below the EV. **The re-label to USD is the correct measured class.**
- **The 41 header figures that move to NO currency** (`CUR_MKT_CAP` 8, `NET_DEBT` 20, `CURR_ENTP_VAL` 13) follow the ruling: a
  currency the census did not measure is not printed. TSM's `NET_DEBT` is plausibly TWD by the EV identity above. Its label returns
  when a measurement supports it, never by assumption.

## 2. CONDITIONS

1. **Act-start gate:** the closure diff from `0d73289a8e` is empty, and the map equals its committed bytes. Run with `PYTHONPATH=<repo
   root>`. Otherwise STOP.
2. **The order is the act:** (a) -> (b) -> (c) -> (d), each after-read passing before the next. (d) runs as a named script with
   `python -u` and a CreationDate survivor check (round-24 ruling 2).
3. **Leg v item 5 (the served read):** TSM `CUR_MKT_CAP` reads USD and `NET_DEBT` carries no currency on the live `/thesis`, with the
   CodeSha256 printed.
   - Add one read: a NON-mixed name's `CUR_MKT_CAP` (for example BA_US) is byte-unchanged in its label.
   - That is the negative arm: the rule moves only mixed-currency names.
4. **After (c):** AMGT_RESAPP round-54 cell 4 (the FWD-30 re-run) is unblocked. Tell `2.0.0_SA_COO~Z`.

## 3. ROLLBACK

The COO half stands: revert the map commit and the aa-1 wiring, then re-derive forward. The prior stamps stay. A delete is Andrew's
act.

## 4. NOT COVERED

- BP/_LN and NG/_LN (`Z-S64`, aa-4);
- any block outside the 22;
- the scoped API.
