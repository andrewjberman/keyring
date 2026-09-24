# AMGT_RESAPP round 25: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T11:4xZ at HEAD after `78e0781e7f`, LOCAL on SITEZ.
**Inputs:**
- The COO's packet `ledger/ROUND25_L8_PACKET_20260922.md` @`78e0781e7f`, and the two orders.
- The channel census.
- This seat's own instruments, all local, with no network, no key read and no store write: the three suites on the
  merged tree, an in-process stub probe of `lusha.harvest_company`, and an exception-class census of the sinks that
  battery step 1 now lets propagate.

## Round state

**2 of 2 terminal:**
- `rk-98`, B2 filings bronze wiring, @`8dd72465b6`.
- `rk-99`, B4 Lusha harvest wiring, @`0c5dcc7c06`.

The sweep reads PASS 12 / FAIL 0 / UNVERIFIABLE 0 of 12 criteria over 2 orders. The order files carry 12 criterion
ids (6 + 6), and **0 of 12 are judgment criteria**. No criterion was graded on a literal miss. Neither worker filed a
row, and the channel holds no `W98`/`W99` row.

Suites re-run by this seat on the merged tree: filings 86, harvest 72, and management 95 with 13 subtests. Each
equals its order's AC0 baseline plus the new tests: 79 + 7, 64 + 8, and 95.

## rk-99: probed on arms the COO's probe did not use

The COO's probe covered an email-bearing result and a `KEPT_FIELDS` mutant. This seat probed three other arms:
- **Empty roster:** refused with `ValueError` BEFORE the client or the page is touched (client 0, page 0), so no
  credit is spent on a name with no roster.
- **Default `write=False`:** status CALLED, `written` False, 0 S3 puts.
- **The second limb of the guard.** `KEPT_FIELDS` holds no contact-like key (0 of 12). An allow-list edit that adds
  `phoneNumbers` is still refused, by `enrich.is_contact_key`. So the guard's two limbs are independent.

`scrub` drops phone and email, and keeps `linkedinUrl`. That matches C-LUSHA-EXCEPTION, which keeps ONE public
professional-profile URL (`profile_url`). `record_hash` is added by `store.write_contact_match` (`store.py:361-368`),
not by `KEPT_FIELDS`, so the lineage the contract names is present on write. The enrich seam only adds lines: 0
removed.

## rk-98: the narrowed catch, read on the exception classes

Battery step 1 now catches `(RuntimeError, ValueError)`. `_sec_ticker_table` raises `RuntimeError` only when
`_call_http_get` returns no data, and `_call_http_get` catches every exception from the HTTP call itself. JSON and
UTF-8 decode errors are `ValueError` subclasses. So network behaviour is unchanged.

Census of what a sink can raise:
- `HarvestStoreError` and its four subclasses (`BronzeImmutableError`, `LushaExceptionError`, `NotHarvestHomeError`,
  `SilverRowError`) derive from `Exception` only, and all propagate.
- botocore `ClientError` also propagates.

So no writer failure can be read as a failed attempt, as ruled.

**Exposure noted for the B2 RUN cell, not this one:** the packet's s.3 item stands. Step 1 hands the ticker table to
the sink once per NAME. If `bronze_put` raises `BronzeImmutableError` on a second put to the same key, a multi-name
`--write-bronze` run now fails loudly on the second name. That is the correct side to fail on, but it would stop the
run. The run cell's AC0 must read this.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S383",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T11:45Z",
    "one_line": "L9 GRADE RECORD for round 25: 2 of 2 terminal, sweep 12/0/0, judgment 0 of 12; suites 86/72/95 on the merged tree; rk-99's guard refuses an empty roster before any client call and catches a contact key through its second limb; rk-98's narrowed catch lets every store exception propagate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_RESAPP --round 25: PASS 12 / FAIL 0 / UNVERIFIABLE 0 of 12 over 2 orders; order files carry 6 + 6 criterion ids, judgment=\"true\" in 0.",
        "pytest on the merged tree: filings 86 passed, harvest 72 passed, management 95 passed + 13 subtests.",
        "In-process stub probe, key env var unset: harvest_company with officers=[] raises ValueError with client 0 / page 0 calls; default write=False gives 0 puts; KEPT_FIELDS + phoneNumbers is refused by the is_contact_key limb.",
        "Exception census: HarvestStoreError and its 4 subclasses and botocore ClientError are not RuntimeError/ValueError subclasses, so they propagate through step 1."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it.",
    "world_is": "Both cells do what their orders require, on instruments other than the ones the orders named.",
    "notes": "Grade carrier only. The B2 run cell reads bronze_put's equal-bytes behaviour at its AC0 (packet s.3).",
    "dismissal_reason": "Grade record: this row carries the round-25 L9 grade and dispositions no item; the enum has no record value."
  }
]
```
