# ANDREW-DIRECT 2026-08-20 ~00:57Z — TrueShares STANDING egress APPROVED

**Channel:** Andrew, directly at the `0.4.0_DS_ClientPlatform` terminal, in response to
`/open-calls` (1 card rendered 2026-08-20 ~00:55Z).
**Recorded:** 2026-08-20T005731Z, same turn, per the record+broadcast law (`org/XXX.md`).

## VERBATIM

> **"Yes to your question, egress approved"**

## THE QUESTION HIS "YES" ANSWERS — reproduced exactly as put, because the scope of the
## answer is the scope of the question and nothing wider

> **Does your 2026-07-31 TrueShares egress approval extend from a ONE-TIME pull to a STANDING
> daily one, and cover the issuer's own holdings sheet on its Google-hosted export URL?
> (yes / no)**

**RULED: YES to both halves.** The 2026-07-31 one-time TrueShares entitlement now extends to a
**STANDING daily pull**, and it **covers the issuer-published holdings sheet served from the
Google-hosted CSV export URL**.

## SCOPE — STATED, NOT ADJUDICATED

**I am the receiving seat and I do not adjudicate the breadth of his word** (`org/XXX.md`:
*surface, do not adjudicate* — in BOTH directions, neither narrowing nor widening). What follows
is the question's own scope, so a reader can see exactly what was asked and answered:

**WHAT IS COVERED**
- Vendor/publisher: **TrueShares**, already a live standing daily source (`etfs-netassets-daily`,
  ENABLED `cron(0 22 * * ? *)`).
- Feed: the **issuer-published holdings sheet**, reached via the Google Sheets CSV export URL whose
  id is embedded in the fund page the estate already downloads daily.
- Cadence: **standing / daily**, superseding the one-time character of the 07-31 word.
- Funds: **DIVZ and IDVZ** (the two TrueShares funds; PFDE/PFOE holdings already land daily via the
  Pathfinder FILEPOINT CSV and were never in question).

**WHAT IS *NOT* COVERED — no inference, no widening**
- This is **NOT** a general vendor-egress lift. Every other vendor stays exactly where it was.
- **`ycharts_*` REMAINS HELD**, along with every vendor not already on the standing-lifted roster
  (ORION · SMARTX · cot-BD · arxiv · ECLIPSE).
- It authorises **fetching this feed**. It is not a ruling about what is built on it, where it is
  served, or any downstream product decision.

## WHY THIS CALL EXISTED AT ALL (one paragraph, so the record is self-contained)

The D4b provenance read (2026-08-19, `@afd2d831fe`) established with **zero egress performed** that
the DIVZ/IDVZ holdings CSVs already in-repo came from a TrueShares-published Google Sheet under
Andrew's explicit 2026-07-31 approval — and that the **wide** Q1 vendor-egress ask was therefore
**not required** and was never sent (no new vendor, no new feed; the publisher is already entitled
and already scraped daily). What honestly remained was the narrow question above: one-time →
standing, and whether the issuer's own Google-hosted sheet sits inside that entitlement. That is
the question he answered.

## THE URGENCY THAT MADE IT TIME-SHAPED (and now discharges)

The TrueShares sheet is **CURRENT-DAY-ONLY and carries no history** — its date cannot be chosen.
Capture is therefore **FORWARD-ONLY**: every day without the standing pull was a day of DIVZ/IDVZ
holdings **permanently lost**, and the 2026-07-31 CSVs are the only historical snapshot that will
ever exist. That cost stops accruing the moment the pull is enabled, which is why the enable should
not sit.

## STATE AT THE MOMENT OF THE RULING

- **D4c Phase A is BUILT and committed** `@541a393798` — the holdings fetch path in
  `etfs-netassets-daily`, sheet id **DERIVED** from the already-downloaded page (never hardcoded),
  exercised against real bytes with negative controls that RAISE on a missing link and on two
  ambiguous links.
- **THE PULL IS STILL OFF.** `TS_HOLDINGS_ENABLED` defaults to `"0"` **in code**, so DISABLED is the
  fail-safe default. The enable is a **single environment variable** set in Terraform.
- ⛔ **THE ENABLE IS NOT MY ACT.** `infra/aws/terraform/**` resolves to `infra/aws/**` →
  `CLOUD_OPS_OR_ETL`, and DS is not among its 11 members (measured, not assumed). COO's carve-out
  tonight covered `infra/aws/lambda/etfs-pipeline/**` only. **Routed to `0.7.0_AE_CloudOps`.**

## OBLIGATIONS DISCHARGED THIS TURN

1. **RECORDED** — this file, verbatim, with channel + time. Committed.
2. **BROADCAST same turn** — MCP to `2.0.0_SA_COO`, `1.0.0_SA_CTO`, `0.0.0_AB_MSTR` (separate
   sends; an in-body cc copies nobody), plus `0.7.0_AE_CloudOps` who holds the enable and
   `4.0.0_SA_CRO` whose D5 program consumes the resulting feed.
3. **NOT self-executed beyond my lane** — I did not flip anything in Terraform.

**Note for COO:** you told me at 22:29Z you were putting this same scope confirmation to Andrew
tonight. He answered it at my terminal instead. **It is one call, answered once** — if your version
is still queued, it is now closed, not pending.
