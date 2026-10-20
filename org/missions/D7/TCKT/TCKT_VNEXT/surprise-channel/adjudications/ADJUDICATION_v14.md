# TCKT_VNEXT: CVO adjudication, round 20 part 5 (FWD-11's PROD journey; the package null pair)

<sweep_watermark>2026-10-20T04:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-20.

L9 grade by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-20T04:10Z, a seat that did none of this work. Input:
`org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_PROD2_AND_PKGNULL.md`, blob 33a4b45c9b88 (msg 11201; verified by `git hash-object`).
Criteria are read from their orders: TV2's `TCKT_VNEXT.TO-R20-PROD2...md`, and `task-orders/TCKT_VNEXT.TO-R20-LM7...md`.

## What this seat read itself

**The PROD journey:**
- **The three shots, opened as images.**
  - `prod_filer_waiting`: "Waiting for the coordinator", no meeting control.
  - `prod_coordinator_controls`: the white panel, two "Confirm this time" and "Propose these times", readable.
  - `prod_filer_confirmed`: "Confirmed for 2026-10-26 14:00 ET (R20 PROD run 20261019) by tckt-r20-pcoord-20261019@opal.invalid on Oct 19,
    2026" in light ink, with no meeting controls panel. The row's own Claim and Complete are the ticket actions.
- **Not reused images.** Their sha256 prefixes (`045d41289a8e`, `2354f1aff499`, `eab05f1f9004`) differ from every earlier R20 DEV and PROD
  shot.
- **The contrast**, measured from `prod_filer_confirmed`'s pixels (PIL, WCAG): the line's bands are text rgb(209,212,217) on rgb(25,38,67),
  **10.10:1**.
- **The PROD origin.** The trace records `PAGE ORIGIN window.location.origin = https://opalinvest.dev` for both the filer (18:11:27Z) and the
  coordinator (18:16:43Z). No `localhost` appears in the result or the trace.
- **Live cleanup and routing, read by this seat at ~04:0xZ:**
  - `dynamodb get-item opal-tickets TCK-20261019-c50b4967 --consistent-read` returns no Item.
  - Control: the protected `TCK-20261017-5af976ff` is returned.
  - Live `ROUTING_MATRIX.meeting_request.primary` = `[jeanette@opalinvest.com]`.

**The null pair:**
- **The Lambda change, 17073aff04e.** Inside `package_ticket`, 11 lines are added and 0 removed. A lone null is refused with 400 naming
  both keys; a missing partner falls to its own required check (400); a null pair skips the I7 check. `report_ref` and `original_ref` are
  untouched.
- **The live package**, downloaded: the zip sha256 equals the live `CodeSha256` `LuJO3wFDoQ9rhK4lXZpubHgNBlJqPVNErVgzMQePTI0=`, and its
  `lambda_function.py` equals 17073aff04e and the drain 99267e3a254 byte for byte (135,537 bytes).
- **The page change, e83292d0** (in portal `origin/PROD` `e890aaa94fea`, ls-remote read). It is three files. `NO_COMMENTARY_SENTENCE =
  'Commentary not available'` replaces only the commentary row's content when `commentary_ref === null`, with no Open control.
- **Field map.** `PACKAGE_FILES` maps original to `original_ref`, form to answers, report to `report_ref` and commentary to `commentary_ref`,
  so a null pair (`pdf_ref` is the commentary PDF) leaves the other three as before.

## Grades

**TCKT_VNEXT.TO-R20-PROD2 R20PROD2-AC2J MET.** The filer filed on the PROD page, and the coordinator confirmed on the PROD page. The filer
reads the confirmed line at 10.10:1 with no control. The ticket and both identity rows are gone, and routing is restored to jeanette alone,
both read live by this seat.

**TCKT_VNEXT.TO-R20-LM7 R20LM7-AC3J MET** on the live source, the tests and the PROD page code. A null pair is admitted, and a lone or
missing one is refused. The page reads a null commentary as "Commentary not available", not as an error, while the original, form and
report rows render as before. Nothing else in `package_ticket` or the package block changed.

Limit, as the packet states: no real null package exists on PROD yet, because the packager that posts one ships later. This grade is of the
rule and the reader, not of a live null package end to end.

## FWD-11

**FWD-11 REALIZED.** The ratified DONE WHEN, "on DEV, then PROD by 2026-10-24: a synthetic Opal staff user files a Meeting Request ...; the
OPEN ticket lands in the coordinator's queue; the coordinator confirms ...; the filer sees the outcome on the same ticket", is now exercised
on both tiers:
- **DEV:** ADJUDICATION_v12.
- **PROD:** this grade, filed, confirmed and read on `https://opalinvest.dev`.

Stated limits, none of which is in the DONE WHEN:
- The coordinator was a synthetic stand-in inside a one-attribute routing window (the CTO's ruling (b)).
- jeanette's own first confirm is the organic arm.
- Mail delivery was not exercised (`WE_DL_UNCONFIGURED`, as designed).
- One ticket, one firm, one viewport.

**Trade Request (`TO-R20-PROD3`) is not graded.** It was cancelled by the CTO's msg 11040; its byte read-back is UNPROVEN (rows D2-S62 to S64),
and three 31-byte residue objects await Andrew (CTO row 6e7c). FWD-10 is not touched by this adjudication.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S9",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-20T04:10Z",
    "one_line": "Round 20 part 5 L9: R20PROD2-AC2J MET (filed, confirmed and read on the PROD page, 10.10:1, cleanup read live) and R20LM7-AC3J MET (null pair live, page reads 'Commentary not available'); FWD-11 REALIZED on DEV and PROD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "TCKT_VNEXT-D2-C-S8"
    ],
    "spec_asserts": "FWD-11 DONE WHEN: on DEV, then PROD by 2026-10-24, a synthetic staff user files, the coordinator confirms, the filer sees the outcome on the same ticket. R20LM7-AC3J as ordered.",
    "world_is": "PROD journey on https://opalinvest.dev 2026-10-19 18:11-18:29Z: three new shots, outcome line 10.10:1 (measured here); ticket TCK-20261019-c50b4967 absent and routing jeanette-only (read live here). Live opal-ticket-api source equals 17073aff04e (zip sha256 = CodeSha256); page e83292d0 in origin/PROD.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_PROD2_AND_PKGNULL.md blob 33a4b45c9b88 (msg 11201)",
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_prod2/ (three PNGs, R20_PROD2_TRACE.json)",
        "live: dynamodb get-item opal-tickets; lambda get-function-configuration and get-function opal-ticket-api",
        "git diff 17073aff04e^ 17073aff04e -- infra/aws/lambda/ticket_center/lambda_function.py; portal e83292d0"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row; D2-C-S8's PROD gap (filing and confirm not driven on PROD) is closed by TO-R20-PROD2."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
