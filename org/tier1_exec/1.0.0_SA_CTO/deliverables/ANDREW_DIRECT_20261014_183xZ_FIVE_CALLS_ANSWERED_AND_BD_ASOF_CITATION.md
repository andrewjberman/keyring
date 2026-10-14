# Andrew-direct 2026-10-14 ~18:3xZ (laptop, 1.0.0_SA_CTO terminal) -- five cluster calls answered; the Black Diamond "as of" citation is wrong

Answering the five cards of the `/open-calls --cluster` frame of ~18:2xZ.

## VERBATIM

> "Open calls starting with Call 1: Yes, rec approved. Call 2: No, it is good that all that work is in place because its all so
> connected, and DELL2 has the capacity to manage it. Call 3: Probably not necessary, Dell1 should just drive FRMBCKTS through
> completion and ongoing testing and decommission, that way ADVI can be ready for actual work with canonical pipeline/bucket design
> and no weird forks/alt formats once we're ready to address it. Call 4: Yes, that is ok. Call 5: yes thats fine. Also on the
> Positioning side, i've noticed a citation today on the "Positioning" page whereby we said the Black Diamond holdings details are
> as of 5p ET October 14th. It is currently 2:37p ET on October 14th, so I think there is some adjustment needed to however we're
> managing the date citations from Black Diamond holdings. I believe I noticed the same issue in the Investor Reporting page."

## VERBATIM, second message (~18:4xZ)

> "Something I want to mention is that the laptop does not need to take on any of the work in the 4 items directly, so as a
> result, laptop driving through COMM_ASSIST and NFRA_CTLPLN does not lose us any ground."

**Applied:** the laptop drives COMM_ASSIST and NFRA_CTLPLN at the normal pace. This reverses this seat's ~18:0xZ messages to
`2.0.0_SA_COO~CA` (no new round) and `2.0.0_SA_COO~C` (close or hold).

## Applied

| # | call | answer | route |
|---|---|---|---|
| 1 | dell2 `1f3e`, `cand/dell2/anlreq-internal-filer-chooses-firm` (client-facing) | APPROVED | A dell2 seat closes it with `--by andrew --ruled-by andrew --decision approved --ruling <this file>`, then merge-forward. |
| 2 | laptop `503f`, move the Ticket Center trade and meeting channels to the laptop | DECLINED. dell2 keeps all three Ticket Center channels; "it's all so connected, and DELL2 has the capacity" | Closed on this file. The deliverables plan is updated. |
| 3 | laptop `7a4e`, lend a dell1 seat to Investor Reporting | DECLINED. dell1 drives ADVI_FIRMBKTS through completion, ongoing testing and decommission, so ADVI is ready for its real work on the canonical pipeline and bucket design, with no forks or alternate formats | Closed on this file. The plan is updated; ADVI_FIRMBKTS becomes dell1's lead. |
| 4 | dell1 `6e63`, `cand/dell1/mdpf-canon-aua-trend-groups-and-as-of` (client-facing) | APPROVED | A dell1 seat closes it `--by andrew`, as in row 1. |
| 5 | dell1 `c822`, `cand/dell1/sechist-frontier-label` (client-facing) | APPROVED | As row 4. |

## New defect he reported

At **2:37 PM ET on Oct 14**, the **Positioning** page cited Black Diamond holdings as **"as of 5 PM ET, October 14"**, a time still
in the future. He believes the **Investor Reporting** page shows the same thing. Whatever builds the Black Diamond date citation
has to state the time the data actually describes, never a time that has not yet happened. It goes to the projects that own each
page.

### Cause, read by this seat (portal working tree at ~18:4xZ)

- `portal/src/components/DataAsOf.tsx` (`DataAsOfCompact` and `formatDataAsOfCompact`, "Yang data convention") and
  `portal/src/lib/dateUtils.ts` (`create5pmETDate`) stamp a date-only value (`YYYY-MM-DD`) at 5:00 PM ET.
- A Black Diamond holdings file dated today therefore cites "5:00 PM ET, today" before 5 PM.
- `portal/src/pages/InvestorReporting/format.ts` already calls this "a fabricated precision". It strips the clock for inline
  dates but keeps it on the "as of" line.
- 35 page files use these helpers (Grep over `portal/src/pages`), including Positioning (`PositioningSummary`, `HoldingsTab`)
  and Investor Reporting (`HoldingsSummary`, `IdentityCard`).

### Ruling and route (cluster lead)

1. **One shared fix, owned by dell2 (IRPT_DASHBD, P1):** a date-only value never shows an invented clock ("as of
   October 14, 2026"). A clock shows only when the source supplies a real timestamp.
   - The fix lands in the shared helper, so every page gets it.
   - The tests re-pin the 5 PM cases, with a negative case: a today-dated value read before 5 PM ET shows no time.
   - It reaches PROD through merge-forward as a client-facing candidate, so it needs Andrew's approval.
2. **dell1 (Positioning's owner) and dell2 (Investor Reporting's) each read their Black Diamond date's meaning:** is
   the file's date the close the holdings reflect, or the day they were pulled? If it is the pull date, the citation
   carries the holdings' own date, not the pull date.
3. Neither is a reason to hold any other work.
