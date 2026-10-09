# CTO fold -- three unblock approaches (UB-48b3 ETFS_RIVALS, UB-ea48 AMGT_CORPUS, UB-cbf8 MDPF_SECHIST)

**Folded by:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~04:1xZ. The CRO's approaches (`4.0.0_SA_CRO~DELL1`, 04:01Z-04:03Z) are read through
`python .tools/unblock.py show --id <id>`. Each COO's drive reads this file. The CVO signs off each fold.

## 0. Shared: ONE site-Z Terminal sign-in pre-flight, before 10:45Z

This supersedes point 3 of `CTO_RULING_UNBLOCK_FOLD_SITEZ_TERMINAL_SIGNIN_20261009.md` @3bedaf97f8. Its other points stand.

- One act serves the 11:00Z RIVALS vehicle run, SECHIST's 11:00Z pull and the AMGT 13:00Z fire. It follows
  `integrations/bloomberg/READ_HERE.md` section 2: `bbg_credentials.py --check`, then `bloomberg_health`, then ONE `reference_data`
  read. A sign-in (`bbg_signin.ps1 -Phase fill`, then `-Phase submit` only if signed out) happens only if the check fails.
- **Metering:** `bloomberg_health` and the port read are not draws. The one `reference_data` read IS a draw. It goes on
  MDPF_DEMQUE's books as a tier-1 (production daily pull) request of 1 security x 1 field. `2.0.0_SA_COO~Q1` enters it, by hand
  until the quote cell lands, the same day. No other field is requested.
- Owner: site Z names it. The ask goes from `0.0.0_AB_MSTR~DELL1` to `0.0.0_AB_MSTR~Z`. One ask is made, by `2.0.0_SA_COO~V1`, for all
  three projects. `2.0.0_SA_COO~H1` and `2.0.0_SA_COO~C1` do not send their own.

## 1. UB-48b3 -- ETFS_RIVALS (`2.0.0_SA_COO~V1`)

- Acts 1-3 are the COO's own work, with no fold. Call 8276 is RULED: option A, one standing tier-3 request
  (XA-20261009T033809Z-8c1a). So act 3's COO half covers branch A only, and the option-C branch is dropped.
- **Act 4 FOLD:** the FWD-24 negative-control plant rides act 3's never-widen pair as its own KEY: one `security_universe` row with
  `first_seen` = the run date, a security with no stored close, marked so it can be told apart, rollback = remove that row. The pair
  names the row before and after. A key only, with no new cell. The per-run grader is written before act 3.
- Residual risk recorded: 2026-10-09 is a Friday. A missed 11:00Z leg moves J1 to Monday 2026-10-12.

## 2. UB-ea48 -- AMGT_CORPUS (`2.0.0_SA_COO~C1`)

- Parts B and C: no fold. They proceed now, read-only, with zero Bloomberg calls.
- **Part A FOLD, conditional:**
  - **C2 reading:** on the (b) half, "that run" is the 07:00 ET vehicle run. A re-pin after it, within leg r's Start-In scope, is
    allowed.
  - **The build:** leg b (build `field_map.json`, one-file commit `<p>` on parent `6402de5137`) runs now on dell1.
  - **The re-pin:** it runs after the 11:00Z vehicle run and before 12:45Z, only if site Z names a lane that may run leg r. Site Z's
    four per-project lanes hold no act until Andrew answers (site Z msg 32344). The re-pin needs both equality checks to read equal.
  - **The fallback:** with no named lane, no `<p>` registered by 12:45Z, or either check unequal, nothing is re-pinned. The 13:00Z fire
    runs on `6402de5137` as signed.
  - **Re-sign:** the COO's AMENDMENT on the (u) COO half lands first. This seat then re-signs the (u) CTO half against it.

## 3. UB-cbf8 -- MDPF_SECHIST (`2.0.0_SA_COO~H1`)

- Move 1: section 0 above. The one `reference_data` read is a queued tier-1 draw.
- Move 2: the COO settles with the TO-SH-t3 reader, before 13:01Z, whether "Lenovo Group LTD" is a clean name. If it is not, the COO
  files a surprise row on MDPF_SECCLASS now.
- **Move 3 FOLD:** this seat writes the round-2 analysis pre-draft in two branches (PASS: cut round 3 from PRD section 2 enrichment
  items 1-6; FAIL: re-arm TO-SH-t3 on Monday 2026-10-12's scheduled pull, plus a pre-flight before it). It is filed at
  `org/missions/D8/MDPF/MDPF_SECHIST/ledger/` before 11:00Z. It is a draft, and the analysis issues only after TO-SH-t3 and TO-READ-R2-L3
  report. Card A (FWD-2) remains held for Andrew and is untouched.
