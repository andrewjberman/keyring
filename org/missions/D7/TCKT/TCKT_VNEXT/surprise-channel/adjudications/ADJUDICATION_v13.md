# TCKT_VNEXT: CVO adjudication, round 20 part 4 (the PROD read of FWD-11, R20PROD-AC2J)

<sweep_watermark>2026-10-17T10:30Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-17.

L9 grade by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-17T10:30Z, a seat that did none of this work. Input:
`org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_PROD_READ.md`, blob eefbe931f831 (msg 10495; verified by `git hash-object`). The
criterion is read from TV2's order `TCKT_VNEXT.TO-R20-PROD...md`.

## The byte-identical shots: checked, not assumed

The packet states that both PROD PNGs are byte-identical to DEV shots. I confirmed it:
- `prod_filer_completed` = the DEV re-shot, sha256 `63e2e9d1186f805a...`;
- `prod_meeting_form` = R20 `meeting_form`, sha256 `8415867a52f7e923...`.

An identical image cannot show which server it came from, so this seat tied the shots to PROD by four reads it made itself:
1. **The run's script.** `r20_prod.py` sets `ORIGIN = "https://opalinvest.dev"`, calls `pg.goto(ORIGIN + "/ticket-center")`, and writes each
   PNG with `pg.screenshot(...)`. No copy and no read of a DEV file appears in the script.
2. **The trace.** `R20_PROD_TRACE.json` records `PAGE ORIGIN window.location.origin = https://opalinvest.dev` at 10:05:55Z and the shot saved
   at 10:06:01Z; the file's mtime is 06:06:01 local. Its request census lists one host, `opalinvest.dev`, and no `localhost`.
3. **The live PROD bundle**, fetched by this seat from `https://opalinvest.dev/ticket-center`. The index serves `/assets/index-BvqT28eK.js`,
   the bundle in TV2's census. Its Ticket Center chunk `index-BrJQIMwF.js` carries:
   - `"data-slot":"meeting-outcome-line",className:"text-xs font-medium text-white/80"`, the contrast fix `2a64d211`;
   - `Confirm this time` and `Propose these times`;
   - the type-list filter `.filter(([a])=>a!=="trade_request")`.

   It carries none of the c05e3dda upload strings (`This is the placeholder form`, `attachment-upload`, `Open form`: 0 each). The one
   `Submit trade request` is PROD's older hidden form.
4. **Plausibility of identity.** The same component, the same CSS classes, the same data and the same clip produce the same pixels, whether
   from a dev server or a production build.

## Grade

**TCKT_VNEXT.TO-R20-PROD R20PROD-AC2J MET.**
- **The PROD page draws the confirmed outcome on the completed ticket with no control: MET.** The shot is the image this seat measured at
  10.10:1 in v12 (identical bytes), the page is tied to PROD as above, and the PROD bundle carries the light-ink class.
- **The meeting form is readable: MET.** It is a white panel with navy ink. As in v11, "on the light canvas" has no light canvas to stand
  on: the page is the dark theme (row D2-C-S6, unchanged).
- **Trade Request is absent from the type list: MET.** TV2's recorded options are Service Request, Meeting Request, Other and Analysis
  Request, and the PROD bundle's own filter drops `trade_request`.

## FWD-11: the PROD leg is a read; the ratified DONE WHEN asks for the journey

**FWD-11 is REALIZED on DEV in full (v12). On PROD, the read is exercised and the drive is not.** The ratified DONE WHEN: "on DEV, then PROD
by 2026-10-24: a synthetic Opal staff user files a Meeting Request ...; the OPEN ticket lands in the coordinator's queue; the coordinator
confirms one time or proposes another on the ticket; the filer sees the outcome on the same ticket."
- **Exercised on PROD:** the filer sees the outcome on the same ticket, after completion, readable.
- **Not exercised on PROD:** the filing and the coordinator's confirm.
  - The ticket was filed and confirmed through the DEV page (the backend is the one `opal-ticket-api`).
  - The PROD form was opened but not submitted, and no PROD coordinator acted.
  - The PROD bundle carries the same form and controls code, so the gap is small. But the PROD page has not been driven, and run-pair
    AMENDMENT 7 scoped the PROD leg read-only without a PRD addendum narrowing the outcome.

**Two ways to close it, before 2026-10-24.**
- **Recommended:** run the two missing acts once on `https://opalinvest.dev`. A synthetic filer files one Meeting Request, a synthetic
  coordinator (a one-attribute routing window, as in R18 and R20) confirms it on the PROD board, and the filer re-reads it. Grade it on
  shots and the contrast number, as here. This is one small run with the same pair shape already signed twice.
- **Or:** the CTO writes an L10 addendum that makes FWD-11's PROD leg a read of a DEV-driven ticket. That is an ENDPOINT change, and this
  seat's ratified-text half re-opens.

Until one of those lands, this seat reads FWD-11 **NOT REALIZED on PROD**.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S8",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-17T10:30Z",
    "one_line": "Round 20 part 4 L9: R20PROD-AC2J MET (PROD tied by script, trace, census and the live bundle, not by the byte-identical PNG); FWD-11 PROD leg read-only, so the PROD filing and confirm remain unexercised against the ratified DONE WHEN.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "R20PROD-AC2J as ordered; FWD-11 DONE WHEN: on DEV, then PROD, a synthetic staff user files, the coordinator confirms, the filer sees the outcome on the same ticket.",
    "world_is": "PROD (opalinvest.dev, bundle index-BvqT28eK.js, chunk index-BrJQIMwF.js) carries the light-ink outcome line and the trade_request type filter and none of the c05e3dda upload strings; TV2's run read the real completed ticket on PROD; the ticket was filed and confirmed through the DEV page; the PROD form was not submitted and no PROD coordinator acted.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_PROD_READ.md blob eefbe931f831 (msg 10495)",
        "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_prod/R20_PROD_TRACE.json; r20_prod.py lines 28, 192, 224, 258",
        "https://opalinvest.dev/assets/index-BvqT28eK.js and assets/index-BrJQIMwF.js, fetched by this seat 2026-10-17 ~10:2xZ",
        "org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md FWD-11 (lines 89-95)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row; the FWD-11 PROD gap is routed to the CTO with two closes (drive the two acts on PROD, recommended; or an ENDPOINT addendum)."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
