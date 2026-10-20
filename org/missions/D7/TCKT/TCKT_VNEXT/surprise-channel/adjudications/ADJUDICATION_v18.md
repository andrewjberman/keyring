# TCKT_VNEXT: CVO adjudication, round 21 (the Trade Request attachment read back on PROD, R21RB1-AC2J)

<sweep_watermark>2026-10-20T16:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-20.

L9 grade by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-20T16:20Z, a seat that did none of this work. Input:
`org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R21_TRADE_READ_BACK.md`, blob 7b3002661641 (msg 11416; verified by `git hash-object`).
The criterion is read from TV2's `TCKT_VNEXT.TO-R21-RB1...md`.

## What this seat read itself

- **The two shots, opened as images.**
  - `prod_trade_form_filled`: the placeholder form named as one ("This is the placeholder form ... No trade is sent."), Cottonwood
    Capital Advisors, `tckt-r21-trade-synthetic.csv`, "Submit trade request".
  - `prod_trade_filed`: the row `TCK-20261020-645d7017`, Trade Request, open, with "Claim", "Open form" and "Complete".
- **The trace** names one origin, `https://opalinvest.dev` (15:45:03Z), and no `localhost`. The Open route answered 200 with
  `[expires_in, filename, url]`, and the listener was registered before the press.
- **The stored bytes, fetched by this seat** with `s3api get-object opal-data-cottonwood
  .../85de6b5ed04b4ac5a14ea677949c1981/tckt-r21-trade-synthetic.csv --version-id lway93Q_YhLuvb25e3M__smeGKeFABbC`: 31 bytes, `text/csv`,
  sha256 **`b0b2b41f6ccc3d552457c98840b0b47a3415781f9a36aa0d8600a5aca8a73455`**. That equals both the recorded upload hash and the
  read-back hash, so the object at rest is the upload and the read-back is not an echo of a local file.
- **Cleanup, live.**
  - `dynamodb get-item opal-tickets TCK-20261020-645d7017 --consistent-read` returns no Item.
  - Control: the protected `TCK-20261017-5af976ff` is returned.

## Grade

**TCKT_VNEXT.TO-R21-RB1 R21RB1-AC2J MET.** The filer's Trade Request attachment was opened through the PROD page's Open route, and its
bytes read back equal to the upload, re-verified at rest by this seat. The residue is named: four 31-byte synthetic objects with keys and
versions in the result.

Limits, as stated: one ticket, one firm, one synthetic filer and one 31-byte file. The bytes were fetched from the presigned `url` rather
than shown in a browser tab. The organic arm, a real form opened by Andrew, is not exercised.

## Notes for the CTO's analysis (not conditions of the grade)

1. **The outcome is FWD-10, not FWD-11.** The PRD's FWD-10 is "An Opal person files a Trade Request ... the ticket carries the form", and
   its DONE WHEN is "on DEV, then PROD by 2026-10-24".
   - This grade exercises FWD-10's PROD leg: file, attach, and open from the ticket page with the bytes equal.
   - No FWD-10 DEV-leg packet has reached this seat; R18 PART 2 stayed held. Whether the DEV leg ran, or is to be run, is the CTO's to
     state before FWD-10 reads REALIZED.
2. **The residue delete may not need Andrew.**
   - The four objects are routed to Andrew as row 6e7c, because the applier's `s3:DeleteObject` is denied (CTO msg 11005).
   - Andrew's standing word of 2026-10-16
     (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_134xZ_SYNTHETIC_TEST_DELETES_NEED_NO_CALL_OPAL_TERMINAL_GONE_DELL2.md`)
     reads: "you can delete synthetic and test files any time, i do not need an open call". That is by listed key and VersionId, from the
     record that wrote them.
   - The open question is which principal holds the delete, not Andrew's word.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S16",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-20T16:20Z",
    "one_line": "Round 21 L9: R21RB1-AC2J MET -- the Trade Request attachment opened on the PROD page reads back byte-equal (sha256 b0b2b41f..., re-fetched at rest by this seat); this is FWD-10's PROD leg, and its DEV leg is unshown.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "R21RB1-AC2J as ordered; FWD-10 DONE WHEN: on DEV, then PROD by 2026-10-24.",
    "world_is": "opal-data-cottonwood .../85de6b5ed04b4ac5a14ea677949c1981/tckt-r21-trade-synthetic.csv @ lway93Q_... is 31 bytes, sha256 b0b2b41f6ccc3d552457c98840b0b47a3415781f9a36aa0d8600a5aca8a73455 (fetched here); trace origin https://opalinvest.dev; ticket TCK-20261020-645d7017 absent (read live).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R21_TRADE_READ_BACK.md blob 7b3002661641 (msg 11416)",
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r21_trade_prod/ (two PNGs, R21_TRADE_TRACE.json, R21_TRADE_RESULT.json)",
        "live: s3api get-object at the recorded version; dynamodb get-item opal-tickets",
        "org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md FWD-10"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
