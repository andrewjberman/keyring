# /self-drive D2 & D3 — tick 74 (2026-08-30 03:41Z) — state: ARMED

Covers tick 74 and the inter-tick acts since the tick-73 log (`28a4063922`, LOCAL at write; origin
`5a0e1df70b`). Cron `1c261f82` :07/:37 (fire delayed until idle). Paired `/drive D2 & D3 @ 2.0.0_SA_COO`.

## Scope (register-read, §0)

`D2 & D3` → 2 of 12 → 10 projects (1 complete). Open TOs **28 → 25** (ADVI_49F 4 → 1: c02-GROSSLEG,
c02-VINTAGE and c02-REEMIT CLOSED on CVO's grade 85168); register == fresh `to-check` at 25. Claims 342 of
342, 0 lag. Ledger **19 rows / 0 unconsumed**. Cap 19 of 20.

## Calls (§1)

**0 ADJUDICABLE. RESERVED: 3** — R1 `ADVI_49FSRC` close; R2 reach of the 21:23Z word; R3 the 49F SmartX feed's
custodian scope (**CVO CONFIRMED RESERVED 85116**, with the evidentiary note for the card: the feed lands under
`schwab/08335338/…`, i.e. the fabric has assumed Schwab-book since the feed was registered — a name, not a
definition). No pitch this tick (a queue of confirmed reservations is not re-sent).

## Verdicts since the tick-73 log (§3)

**0 on pitched calls.** Rulings that bind the scope, read on the record:
- **CVO 85168 — C02-g-3 ACCEPTED, c02-VINTAGE ACCEPTED.** R-3 `|Δ r_net| = 0` over 2,593,321; R-5 vintage on
  3,021,660 of 3,021,660, schema 1.1 on 535 of 535; R-4 PASS on its declared domain — the bar's author
  amended it to the relation form `(r_gross − r_net)·BMV == cf_net − cf_gross` (verified on the world at
  2024-07-23 on both negative-BMV fee rows, positive + negative controls). **H-4 lift condition MET.**
- **COO 85178 — H-4 LIFT:** AE base re-enables `advi-49f-gold-floor`, State ENABLED read live, closes the hold
  ledger; then the P2F-3b accelerator apply on this seat's per-apply gate for that plan shape.

## Driver's own acts since the tick-73 log

1. **The negative-BMV engine defect** (DS~N 85148, OBSERVATION × ARMED): confirmed at source
   (`c02_twr_engine.py:47` says *value*, `:224` tests `abs()` — the banked "abs() at the measuring step"
   class); 1,089 of 2,593,321 OK account-days carry BMV < 0 and are served with a sign-inverted `r_net`
   (0.042%; nothing client-facing reads `twr_daily` today). **DISARMED by ownership (85171 ≡ COO 85163):**
   engine limb DS~N as a new cell (first act: the affected-partition census), served-data limb COO + this
   seat's serve-gate under never-widen. **CONVENTION RULED:** a TWR over BMV < 0 is UNDEFINED → the engine
   REFUSES with its own status `UNCOMPUTABLE-NEGATIVE-BMV` (Rule-24 record: three members over the BMV
   domain; the new one does not move with the ZERO-BMV remedy). **Serve-gate condition (iii) added:** no serve
   while any OK row carries BMV < 0. **Corrected my own 85134** on the disposition half only (the 15 rows
   are a finding against the engine, not a bar footnote); the convention half stands. H-4 unaffected.
   COO cut C02-g-5 (engine, DS~N) + C02-g-6 (re-emission, AE~L, never-widen at plan time) against this
   seat's pre-registered bar (OK rows with BMV < 0 → 0 of N; refused rows carry the status; BMV ≥ 1 rows
   byte-identical; vintage unchanged). DS~N accepted the builder role (85182).
2. **M-2 converter deploy — APPLY word (85118)** on the exact ruled plan (2 rows on `schwab`: code +
   `OPAL_BUILD_COMMIT=5c7b2a9a6b`; 0 on the other five; 0 destroy); issuer word agrees (85122); read-back owed.
3. **Andrew-direct 03:35Z (via MSTR 85184):** sprint render dates must match the calendar — three published
   reports carried the wrong weekday. MSTR's one-arm fix on this seat's `render_daily_report.py` (display_date
   DERIVED from `date`, a typed mismatch FAILS) ACCEPTED as-is, not re-homed.

## In motion, not mine

Reporting-pull R-4 closes at the 04:35Z insurance-fire read (~04:40Z). BDPARITY BP1-2 on real anchors. The
floor's 12:45Z fire today recomputes Friday 08-28 (already served); Tuesday's is the first with new data.

## Completion test (§4)

**NOT DONE — 1 of 10.** REACHABLE 9 / UNREACHABLE 1 (`ADVI_49FSRC`, R1 at Andrew).

## Compiler Tools

`directives-check.py --json`, `to-check.py --all` (per-project sums), claims scan (both `prds[]` shapes); one
source grep on `c02_twr_engine.py` (Rule 22 before the ruling). No comp-state.

state: ARMED · next log at a verdict or tick 80 (floor)
