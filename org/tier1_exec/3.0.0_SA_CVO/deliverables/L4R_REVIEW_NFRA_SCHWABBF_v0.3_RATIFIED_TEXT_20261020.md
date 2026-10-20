# L4-R review -- NFRA_SCHWABBF PRD v0.3 @7a864849e9, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (laptop), 2026-10-20 ~14:5xZ. Delivered by 1.0.0_SA_CTO msg 109898 (acked). Half hash `0d1d82de3091`.
**Graded:** the PRD diff 6c3ded061f -> 7a864849e9: C-KEYFORM rewritten to vendor/firm scope, "Confirm FWD-8" removed from OPEN AT ANDREW,
one change-log entry. ENDPOINT is byte-unchanged from v0.2.

## Verdict: REFUSE

**Reason (one line):** CONTRACTS contradict each other. C-KEYFORM moves bronze to `schwab/<firm>/`, while C-NAMES and C-RECORD still address
`schwab/<master>/` (silver and meta included), and C-SCOPE still excludes the four Cottonwood masters that FWD-8 and C-ALONGSIDE pull.

## What clears v0.2's ground

- **FWD-8 is confirmed:** `ANDREW_DIRECT_20261020_143xZ_SCHWABBF_FWD8_CONFIRMED_BUILD_VENDOR_FIRM_PATHS.md`, "thats fine". The v0.2 refusal's
  ground is gone, and FWD-1 to FWD-8 stand as ratified text.
- **The builder output is as stated** (run by this seat): `address('schwab','49financial','bronze','acc','date=2023-10-17')` ->
  `s3://opal-data-assets/schwab/49financial/bronze/acc/date=2023-10-17`; `cottonwood` -> `.../schwab/cottonwood/...`; silver ->
  `.../schwab/<firm>/silver/dim_balance/...`.

## The three edits that make it signable

1. **One scope for the whole Schwab tree, or a stated reason for two.** The bucket today (listed by this seat) holds `schwab/08242234/`,
   `schwab/08335338/` and `schwab/08403355/`, each with `_ops/`, `bronze/`, `meta/` and `silver/`. v0.3 moves bronze alone to firm scope:
   - C-NAMES still prints `address('schwab','<m>', ...)` for bronze and silver, so a worker who follows it writes the old scope;
   - C-RECORD puts the held-days record under `schwab/<master>/meta/`;
   - the result is `schwab/49financial/bronze/` beside `schwab/08403355/silver/` and `schwab/08403355/meta/`: two scopes under one vendor.
   Andrew's words were "abiding by the path structure that already exists in that bucket" and "schwab vendor and 49 firm". The pattern he
   points to, `blackdiamond/49financial/`, carries bronze AND silver under the firm. Either silver, meta and `_ops` move to firm scope too
   (C-NAMES, C-RECORD, C-MOVE's object count, C-EQUAL's rebuild and C-READERS' census all follow, and silver readers widen the blast
   radius), or the PRD states that only bronze moves and why. That choice is the CTO's to make or to ask Andrew; this seat signs either
   one once the rows agree.
2. **C-SCOPE contradicts FWD-8.** It still reads "Three masters only ... The four Cottonwood masters ... join through C-ONBOARD when Schwab
   entitles them" and "No cell reads, pulls or names them." FWD-8 and C-ALONGSIDE pull those four now, through the Alongside login. C-SCOPE
   should say the Cottonwood four are in scope through C-ALONGSIDE, with C-ONBOARD kept for a master Schwab opens to the 49F login.
3. **One writer per firm prefix** (carried from v0.2 item 1, now sharper). Both FWD-7's route and FWD-8's route would write
   `schwab/cottonwood/bronze/...`. A contract should name the Alongside box as the only writer for the four Cottonwood masters, and keep
   them out of the 49F box's map.

## Still carried, not grounds

- v0.1 item 1 (`si2_daily_builder_named` types rule names outside its set) and v0.2 item 3 (an exact copy must not carry that ternary):
  both bind the Alongside root's first apply.
- v0.2 item 2: FWD-8 assumes the Alongside login sees all four masters, which is unread until the session exists.
- The paragraph of history under the ENDPOINT block is still there.

-- 3.0.0_SA_CVO
