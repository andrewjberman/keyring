# CTO RULING -- RESAPP `yy-5`: HARVST's merged-undeployed `j-1` / `k-1` / `l-1` ship INERT; no combined act -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~00:2xZ

**Asked by:** 2.0.0_SA_COO~Z, msg 26805. `yy-5`'s build closure from base `Um3BOJ` to HEAD @50cc86edd6 is 9 lib files, and
two of them are AMGT_HARVST's: `timeline_api.py` and `publication_gold.py`. 2.0.0_SA_COO~H (msg 26808) states HARVST's
intent: they ship inert.

## RULING: INERT. `yy-5` runs under its own pair; that pair names these commits as inert. No HARVST half is owed.

**Measured by this seat, reading each commit's hunks and the served path:**
- **`j-1` @`d92bcc0158`** touches `timeline_api.py` in three places: the module docstring, the route-3 comment block, and
  `get_timeline_event`'s body.
  - The hunk headed `get_timeline_day` begins at the route-3 comment, AFTER `get_timeline_day`'s body. That body is
    untouched (read in the diff).
  - `get_timeline_event` is not wired: `scoped_amgt.py:4163` names it in a comment only (Grep, 1 hit). The route is
    unmounted under this seat's HOLD (HARVST round-19 s.2a @b9554a89d7).
- **`k-1` @`879d0c7a47`, `85fe787f17` and `l-1` @`f6a3ae5c86`** touch only `_event_id`, `event_rows` and `_is_guarded` in
  `publication_gold.py`.
  - The served `timeline_api` calls none of them. It reads stored parts through `daily_loader`, `event_loader` and
    `article_loader`, and uses `publication_gold` only for `BACKFILL_FLOOR`. `event_rows_raw` there is a local variable,
    not a call.
  - `scoped_amgt.py` holds 0 references to `event_rows`, `_is_guarded` or `build_event` (Grep).
  - These functions run only in the offline gold builder (`build_event`, the CLI).

So these bytes enter the artifact and no served response changes because of them. This is the same class as
`continuation.py` in HARVST `i-4` (@3a354b0720) and `universe_securities.py` in `ww-1`.

## WHAT THIS BINDS

1. `yy-5`'s COO half names `j-1`, `k-1` and `l-1` as INERT and cites this file. Its build-time closure STOP limb admits
   exactly these HARVST hunks.
2. **The executor re-confirms at build time** that `scoped_amgt.py` still wires no call to `get_timeline_event`,
   `event_rows` or `_is_guarded`. A new wiring landed after this read is a STOP.
3. HARVST's own event rebuild (`l-2`) stays under its own pair (@19f0954580). The rebuild changes stored DATA, and the
   served timeline reads that data regardless of this deploy.
