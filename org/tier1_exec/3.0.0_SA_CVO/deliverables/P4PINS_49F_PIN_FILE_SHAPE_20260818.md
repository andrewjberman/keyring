# P4 PINS (49F) -- the per-key pin-file shape + precondition read protocol (prep, before the enumeration)

**Author:** 3.0.0_SA_CVO · 2026-08-18 ~1615Z · **archetype:** VALIDATE (instrument prep, no enumeration run)
**Authority:** TO `OPAL_ADVIPOINTERS.P4-PINS-CERT-49F` (GO 160719Z), criteria 49F-PIN-PRECOND / -FRESH /
-VINTAGE-STATED. **This file defines the SHAPE so the 08-21 enumeration is mechanical; it contains ZERO
pin values by design** -- a pin written before its precondition reads true would be the stale-vintage
class the TO exists to refuse.

## 1. THE PIN FILE, per key on the P4E-1 frozen list

Path grammar: `data/assets/scripts/gold/runners_49f/pins/pin_{emitter}_{leaf}.json` (committed; one file
per served key; a projection of `predeclared_divergences_49f.json` -- NO new instrument, run-and-read).

```json
{
  "key_n": 1,
  "legacy_served_key": "s3://opal-data-bd/platinum/firm/header_metrics.json",
  "advi_key": "s3://opal-data-portal-v2/platinum/advi/49financial/<leaf per P4E-1 mapping>",
  "phase": "PRE-FLIP",                        // -> "POST-FLIP" written as its OWN act, never edited in place
  "precondition": {
    "row0_served_as_of_T1": {"read": "<data_as_of from served bytes>", "evidence": "<s3 key + LastModified + the trading-day frontier per lib/trading_calendar.py>"},
    "first_unattended_canonical_write": {"read": "<canonical date={T-1} partition>", "evidence": "<head-object + the SCHEDULED run's own log id -- an ad-hoc write does NOT discharge this limb (NEVER#4: ad-hoc is never production evidence)>"}
  },
  "enumeration": {
    "served":    {"vintage_lm": "...", "content_date": "...", "sha256": "...", "framing": "content-date",
                  "emission": "04:00Z-T1-serve"},   // R1 RIDER @9988b2dd66: ALWAYS the 04:00Z T-1 serve
                                                    // (true landing ~05:27Z); the 23:01Z run is the
                                                    // T-2-evening preview and is NEVER a pin reference.
                                                    // Discriminator = the payload's own data_as_of vs the
                                                    // trading calendar, not the mtime clock.
    "canonical": {"vintage_partition": "date=...", "content_date": "...", "framing": "content-date"},
    "same_content_date": true                  // FALSE => the file is INVALID, enumeration refused
  },
  "pins": [
    {"field_path": "total.aua", "expected_delta": 0.0, "tolerance_abs": 0.0,
     "band_id": "D5|V3|...",                   // ties back to the registry row it projects
     "class": "identity|monetary|meta|backfill-pending",   // bar SS2 field-class
     "state": "MATCH-CLEAN|DIVERGE-in-band|DIVERGE-SOVEREIGN|MATCH-KNOWN-WRONG"}
  ],
  "stale_pin_law": "any re-emission of either side after this enumeration voids the file; re-pin, never patch"
}
```

## 2. WHAT THE PRE-FLIP EXPECTED VALUES ARE (folding the $122.5M class correctly)

The 08-06..08-11 registry pinned served-vs-canonical deltas at a STALE vintage. At the fresh
enumeration the expected values are NOT copied forward -- they are RE-MEASURED, then each is
adjudicated against its registry band (the registry supplies the BAND + the MECHANISM, never the
number). The Schwab-canonical authority class (@745ca6d78f: total.aua ~$122.5M, account_count
852, client_count 1241 family) is sovereign-RULED: expected to persist at fresh vintage in the
same direction; a MATERIAL CHANGE IN ITS MAGNITUDE beyond its band is itself a finding (the
composition moved), reported before any flip.

## 3. PRECONDITION READ PROTOCOL (49F-PIN-PRECOND, both limbs on evidence)

- Limb (a): served `data_as_of` == T-1 per the trading calendar (`expected_last_trading_day`),
  read from served BYTES, never from LastModified (LastModified moves on every rewrite of frozen
  content -- measured: 08-15 writes still carrying data_as_of 08-06).
- Limb (b): `s3://opal-data-49financial/gold/advi/canonical/*/date={T-1}` written BY THE SCHEDULED STAGE (RE-ANCHORED 2026-08-19 @RP-CVO-1, GOLDHOME-REPOINT: the old opal-data-assets/portal/gold/advi/49financial root is superseded per Andrew ~1730Z; the precondition reads the NEW root's first unattended write) --
  evidence is the run log of the schedule (AE's P2 TF names the rule), not key existence; a
  session-act write satisfies key-existence and fails this limb by construction.
- Both limbs cited in every pin file verbatim. Precondition FALSE on 08-21 => 4b re-dates IN
  WRITING with COO (the TO's own slip clause), never a silent wait.

## 4. POST-FLIP (the CERT group consumes this)

Post-flip re-base is a SEPARATE file (`phase: POST-FLIP`, own commit) expecting delta~0 of
new-serve vs canonical, plus bar SS8's four legs: values / write-side location / read-side
location / THE MIRROR LEG (legacy key untouched at its pre-flip timestamp where the flip should
not have moved it -- and where legacy RETIRES, that retirement is P5's, not the pin's).

## 5. RELEASES FOLDED (addendum 2026-08-18 ~1740Z)

- **Rows 14-16 (partner_analytics trio) RELEASED to EMIT** per the frozen list's own release
  mechanism (@556d40ecb2, CTO R-1; freeze @5f1076e9c1 intact, members untouched). **Pin
  denominator: 15 EMIT legacy keys -> 14 advi twin objects.**
- **Trio pin rows carry a `basis` citation** read from the payload's `provenance.views` per-period
  basis map (role_aua-canonical vs jd2-derived degrade): PIN AGAINST THE BASIS THE PROVENANCE
  DECLARES, never an assumed snap. Live snap coverage ends 2026-08-06 until the 23:01Z restore
  resumes C_01c -- a later-asof emission rides the DECLARED degrade on its current period; a pin
  that assumes the snap would fail on a design, not a defect (the D2-class trap, avoided by the
  citation).
- The trio's current-period population 15 == served 15 (DS~B measured; the $361M jd2-basis gap
  closed) -- so the OLD basis delta leaves the expected-delta table; the residual trio delta is a
  VINTAGE band (08-06 snap vs the enumeration date), stated per ss5.

-- 3.0.0_SA_CVO
