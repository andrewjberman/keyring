# ANDREW-DIRECT 2026-09-30 ~13:0xZ to ~14:0xZ (09:0x to 10:0x ET) at the 4.0.0_SA_CRO terminal -- three asks in one session

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Channel:** Andrew typed at this seat's terminal (Claude Code, laptop fabric). Times are the harness clock (UTC).
**Scope:** VERBATIM record of each ask and what this seat did. No seat's work changes on it; nothing here is a gate.

---

## Ask 1 (~13:0xZ) -- a Desktop shortcut into the home Mac

Andrew pasted a five-step setup note (Mac Screen Sharing on, Tailscale on the laptop, a saved connection named
"Home Mac" to 100.98.173.75:5900, keep the Mac awake, test over a hotspot) and wrote, verbatim:

> "I need you to help me get this set up"

then:

> "I already made the necessary permissions updates to the mac device, i want to create a shortcut on this device
> desktop that taps into the mac device. The premise is this way, we can run more compute, and delegate jobs to
> that box."

**Done on this laptop (measured):**
- Tailscale 1.102.2 already installed; `tailscale status` lists `andrews-macbook-pro` at 100.98.173.75 (macOS).
- `Test-NetConnection 100.98.173.75 -Port 5900` -> TcpTestSucceeded True (path via DERP relay `mia`).
- No VNC viewer was installed. `winget install RealVNC.VNCViewer` failed (vendor download 404); `winget install
  TigerVNC.TigerVNC` 1.16.2 succeeded -> `C:\Program Files\TigerVNC\vncviewer.exe`.
- Shortcut FILE `C:\Users\AndrewBerman\Desktop\Home Mac.lnk` -> `vncviewer.exe 100.98.173.75:5900 -RemoteResize=1
  -Shared=1` (read back from the .lnk).
- NOT done by this seat: the VNC password entry and the hotspot test (Andrew's, interactive).

## Ask 2 (~13:2xZ) -- figures for Alongside's partner scorecard

Andrew pasted a request from Alongside's data manager (five items: total platform AUM managed by Opal; Opal-managed
AUM by firm; as % of total firm AUM; total Opal product AUM in ETFs; % of Opal-managed AUM) and wrote, verbatim:

> "I need you to get me the following figures, should all be identifiable via mdpf numbers from 9/28."

Then he narrowed it (~13:4xZ), verbatim:

> "Just figure out the tax sma, should be about 20m in here i think mostly in 0833 account but need the total
> (<Tax SMA Accounts.xlsx on the Shared site>) i have the per firm splits just by checking network fetch on the
> Model Portfolios page."

**Read before the narrowing (served, `platinum/mdpf/{scope}/*`, source_vintages 2026-09-28):**
- global aum-metrics `total.aum` 2,073,473,418.29; `model_aum` 1,783,707,728.11; `non_model_aum` 289,765,690.18;
  accounts 8,242.
- per-firm aggregate-aua frontier row (as_of_last 2026-09-28): 49financial opal_aggregate_aua 1,749,389,715.05
  (model 1,459,624,024.87); cottonwood partner_custody_total 542,466,251.80 (model 179,296,256.09); inflection
  model 144,787,447.15 (custody NULL at 09-28, source_vintage_last 2026-09-25, status BEHIND).
- Opal ETF product AUM: NOT in the MDPF catalog (opal_discover returns no ETF-AUM row); not pursued after the
  narrowing.

## Ask 3 -- the Tax SMA total (the deliverable)

**Method.** Workbook `Tax SMA Accounts.xlsx` (Shared site, item 01L6LHKFXVVTRR73M6KZGIHM4FY2ATNK4U, modified
2026-09-29T12:49Z) read through the gateway: 16 rows, 14 with an account number, 9 marked Traded=Yes. Each number
matched on the trailing 8 digits of `account_id` in `s3://opal-data-assets/schwab/08335338/silver/fact_rps_s2/
date=2026-09-28/` and `.../fact_acc/date=2026-09-28/` (7,559 rows each), and in the 0824 master's same partitions
(7,471 rows). Value = `net_mv_plus_cash` (the same full-envelope quantity the 49F basis uses).

**Result, business date 2026-09-28 (Schwab CRS20260928):**

| population | accounts | net_mv_plus_cash |
|---|---|---|
| all accounts on 0833 whose `managed_account_investment_strategy` starts "Opal Tax SMA" | 12 | **16,878,834.41** |
| of which in the workbook | 10 | 14,887,345.40 |
| of which NOT in the workbook (opened 2026-09-11 and 2026-09-14, SMA 145) | 2 | 1,991,489.01 |
| workbook accounts on NEITHER Opal-ingested Schwab master (by number and by surname) | 4 | not measurable here |

The four unmatched are workbook rows 7, 8, 12, 13 (workbook estimates 3.38, 1.07, 2.85, 3.00 Mn; rows 7 and 8
are marked Traded=Yes). 16.88M plus the two traded-but-absent estimates is about 21.3M, which is the "about 20m".
One workbook account (row 3) is on 0833 at 0.00. No "Opal Tax" strategy account exists on 0824.

Raw partitions and per-account output stay in the session scratchpad (`scratchpad/taxsma/`), not committed:
they carry names.

## Relay acted on in the same window

0.0.0_AB_MSTR msg 103236 (relay of site-Z 1.0.0_SA_CTO~O, Andrew "yes thats fine on naming exception"): ASK 1
to this seat, rows X11/X12 in `infra/logic/06_CONFORMANCE_LEDGER.md` section 6 -- landed in the commit after this one.
