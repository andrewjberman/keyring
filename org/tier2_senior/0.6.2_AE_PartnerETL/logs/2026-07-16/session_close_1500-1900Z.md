# 0.6.2_AE_PartnerETL -- session close: two Andrew-direct rulings recorded, a cross-lane P0 diagnosed + cured in 3h, a Door-6 instrument finding, and TWO over-claims of my own caught and corrected

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, TRACE, COORDINATE, SCRIBE
**Date:** 2026-07-16 | **Window:** ~15:00Z -> ~19:0xZ (since log `36802ccf3`) | **Serial:** 0.6.2_AE_PartnerETL

## Summary

Andrew took direct control of my lane mid-window and redirected me twice. Both redirects produced more than
my own board would have. **The window's two most valuable outputs were, again, corrections of my own work.**

- **TWO ANDREW-DIRECT RULINGS recorded verbatim + broadcast same turn** (XXX.md law) ->
  `memory/feedback_0833_advisor_intelligence_0824_model_portfolios.md`.
- **WP7 mapping pass -> RULED INTO THE CONTRACT** (CTO 160659Z): PURPOSE column, `MONOLITH_MASTER` as
  per-family config resolved BY purpose (no constant, no default, ambiguous = STOP at CTO's desk). My line
  *"never-sum is why you can't add them; Andrew's ruling is why you can't substitute them"* is the
  amendment's own text. **It also corrected CTO's own frame** (his 155859Z "rebuild from 0833 expected"
  carried the silent selection one level up).
- **INF_D_04 P0: diagnosed -> briefed -> CURED SAME SESSION.** Brief `97e9fb72b`, correction `770ae4800`.
  All 11 artifacts stranded since 07-10T14:51Z rewritten + validated on served objects; header
  `data_as_of` 07-09 -> **07-15**, page-internally consistent.
- **Door-6 marker finding -> 2 cells at CTO's gate.** Andrew's push (*"it is not enough to just sniff around
  it and leave it at that"*) is what turned it from an aside into a routed cell.
- **BD API recon** (Andrew-directed web scan): architecture established, catalog gated, no probe taken.

## The two Andrew-direct rulings (VERBATIM -- the phrasing IS the ruling)

> "They need to be recognized for different purposes. 0833 is the master for Advisor Intelligence for 49
>  Finacnial. 0824 is the master for Model Portfolios for 49 Financial."
> "Both are Schwab accounts, but they have different business logic purposes."

> "I dont give a shit about the 01_raw folder"
> "that is all going to be deprecated very shortly, we already have backfill programmatically from the
>  schwab box and its already all in bronze and silver for both schwab accounts"

**The never-sum law now has its REASON attached:** the split is a BUSINESS-PURPOSE split, not a
basis-accounting artifact. Substituting one master for the other is not a wrong-number bug -- it is
**serving one product's data to a different product**. And Model Portfolios (0824) is a
`comp-surface-check` SEV1 surface that per LD-0273 CANNOT BLOCK and is blind to its own SEV1s -- so a
0824->0833 substitution would land where nothing gates it.

## The INF_D_04 chain (cross-lane, Andrew-directed; INF is not my lane)

**SYMPTOM -> ROOT CAUSE, in order:**
1. Portal header "as of Jul 9, 2026" -> **NOT a cache**: artifacts written 07-10T14:51Z carrying
   `data_as_of 2026-07-09`. The portal renders `data.data_as_of` faithfully. Stale AT SOURCE.
2. Write-date census: **18 fresh (07-16 14:57-15:00Z) vs 11 stranded (07-10, one contiguous 43s block)**.
3. Reverse-map: stranded -> INF_D_04; fresh -> D_00/D_00c/D_02b. **Not "group D" -- the group is healthy.**
4. All D_04 inputs FRESH today incl. `accounts_dimension_latest.parquet` (14:08:51Z, the AoR-touched dim)
   -> **not starvation**. Atomicity (11 missing together, none partial) -> dies before write #1.
5. **RESOLVED (b) NEVER DISPATCHED** (CTO, `chain_full_20260716_134730.log:112` -- D_04/D_02c/INF_09 absent
   from the run set). Mechanism source-confirmed `orion-gold-dispatch.sh:344-346/364-368`: CTO's own
   **GLDRNS.B1 window exclusion `194d3d674`** of three pre-Round-8-migration consumers, **restore clause
   never fired** when the window stamped 07-16 03:51Z. He owns the miss.
6. **CURED:** restore `1ca265e6d` + trio deployed (4/4 full-body GET) + supervised `--single` runs under
   CTO's NEVER#4 ruling (172129Z: supervised completion-of-a-ruled-restore, not the ad-hoc class).
   Door-6 sentinels measured untouched (`--single` writes none, source `:1874-76`).

**ANDREW'S AoR HYPOTHESIS: right PROVENANCE, wrong LAYER.** It stemmed from the AoR *work* (the window's
dispatch exclusion) but NOT the AoR *logic*. The Round-8 `household_headline_map(expect_nonempty=...)` call
I named as prime suspect was **never reached**. **Refusing to assert it is the only reason DS~B did not
spend the P0 editing correct code.**

## TWO OVER-CLAIMS OF MY OWN, CAUGHT AND CORRECTED (the window's real lesson)

**1. "SCOPE = ONE SCRIPT, PROVEN 1:1" was a COINCIDENCE OF COUNTS** (caught by 0.4.0_DS_ClientPlatform~B).
The 11 stranded artifacts were never D_04's 11 writes -- they were the **union of the excluded TRIO's**
outputs. `client_directory.json` is INF_D_02c's; base `partner_analytics.json` is INF_09's single write,
which the `partner_analytics_{*}` glob over-matched. **Both returned `<no script mapped>` in my reverse-map
and I moved past two unresolved rows instead of asking why they would not resolve.** The counts matched only
because the trio was co-excluded. Had they not been, "one script" would have sent the fix hunting a
single-script cause for a three-script exclusion. **The conclusion survived; the proof did not. That is luck,
not method.**

**2. "zero HTTP call sites -> delegates to a .NET assembly"** (my own catch, earlier window, same class):
a negative result from a grep pattern that never contained `HttpWebRequest`.

**THE LESSON, EARNED SYMMETRICALLY ON ONE SCRIPT IN ONE AFTERNOON:** a `comp-pipescript io` manifest's
**READS enumerate REFERENCED-not-required** (the bronze-orion dead end I nearly shipped as the cause) and
its **WRITES enumerate GLOB-MATCHED-not-owned** (the 1:1). **Neither list is an ownership claim, and a count
that matches across both is not evidence of anything.** Direct consequence, now at CTO's gate: **a script
census must come from the DISPATCHER's own IDs, never from a manifest's globs** -- an artifact-derived
census would have reproduced exactly my error.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-platinum summary` / `page PartnerAnalytics --firm inflection` | trace the Jul-9 header to its key + producer | `partner_analytics_{param}.json` -> `data.data_as_of` via auaDonutSegments -> `INF_D_04 :: build_partner_analytics()` |
| `comp-platinum reverse` (x10) | map stranded vs fresh artifacts -> scripts | stranded=INF_D_04; fresh=D_00c/D_00/D_02b. **2 rows returned `<no script mapped>` and I skipped them -- that was the tell** |
| `comp-pipescript io INF_D_04` | I/O manifest (13 READS / 11 WRITES) | gave the shape -- **and both its lists misled me** (see over-claims) |
| `comp-glob` (x3) | locate D_04 / aor_resolution | first hit was the **bd** D_04 -- firm-separation catch, wrong tree |
| `comp-grep pipeline-complete infra/` | establish the ADVI<->MDPF coupling at source | **4 consumers on ONE sentinel** -- coupling ESTABLISHED |
| `aws s3 ls/cp` (many) | served-artifact truth + 13b run-time denominators | 18-fresh/11-stranded census; `data_as_of` reads; marker contents |
| `aws logs describe-log-groups` | hunt the dispatch discriminator | found the marker path; the deciding log was CTO's |
| `py_compile` INF_D_04 | rule out syntax/import-shape | PASS -> failure is at run, not parse |
| WebSearch/WebFetch (x5) | Andrew-directed BD API recon | base URL + OAuth + APIM headers found; catalog gated |

**What worked:** grounding one layer below the record every time -- the tool's source over COO's
instruction, live `get-role-policy` over my own log, the SOURCE over `comp-pipescript io`'s parse, the
version history over an mtime. **What failed/caught:** the two over-claims above; plus the bd-tree
`comp-glob` hit (would have been a firm-separation error); plus my `01_raw` master hunt, which Andrew killed
as a question about a corpse. **Gap found:** the Door-6 completion marker carries no script census and
`git_sha:"unknown"` -- routed as 2 cells.

## Blockers

None self-owned. Standing gates: **HAND HELD on the zero-row thread** (COO 145710Z, pending Andrew -- an
instruction, not a blocker); WP8-DECOM cell 3 queued behind the P0; marker cells sequenced after nightly #2.

## Current State (ZERO prior context assumed -- the handoff surface)

- **INF_D_04 P0: CLOSED + CURED.** All 11 artifacts rewritten 17:45Z; `data_as_of` 07-15 == `clients_tab`;
  attribution == C_07 stamped headline. `D_02c` single follows on CTO's word; **`INF_09` heals on nightly #2
  (07-17)** -- the one live tail. Restore `1ca265e6d`; brief+correction `97e9fb72b` / `770ae4800`.
- **DOOR-6 MARKER, 2 cells at CTO's gate:** (1) completion marker gains a **script census** (dispatched IDs
  + per-script rc) + `git_sha` resolution -- schema-ADDITIVE, **sequenced AFTER nightly #2** (do not change
  a Door-6 instrument mid-repair); (2) the general form -- *"a green produced by two different worlds"* --
  gets a ledger line citing my P2 `841e5e04b` + 0.6.0's ratified class. **ADVI<->MDPF coupling ESTABLISHED
  (not the cause):** `gold/meta/pipeline-complete.json` is ONE sentinel firing `mdpf-daily-trigger`,
  `inf-portal-publisher`, `inf-etf-ownership-daily`, `inf-gold-freshness-guard`. **Consequence: you cannot
  hold MDPF without also holding ADVI.** And `inf-portal-publisher` **deliberately dropped its duplicate
  write paths** (INFPUBLISHERDEDUP 05-12) -- so when D_04 dies **nothing else produces header_metrics**; no
  fallback, by design. **UNEXPLORED:** `inf-gold-trigger:11` "checks pipeline-complete before dispatch;
  skips if already done" -- a sentinel that both GATES dispatch and SIGNALS completion is a re-entrancy
  hazard. I named it; I did not clear it.
- **WP8-DECOM cell 3 = MINE (CTO 164923Z):** the SI2 box pulls its code from
  `s3://opal-data-schwab/_ops/canonical-schwab-si2/sdd-daily-pull.ps1` -- **that bucket is Andrew-ordered
  decommissioned**, so the code home must move BEFORE stage D5 (read-only). My motion: propose the new home
  (Rule 12: local -> S3 -> EC2; target bucket must SURVIVE) at CTO's gate, then re-point + one exercised
  pull-and-run as the AC. **The daily ~09:46Z SI2 cycle must not skip a beat across the re-point.**
- **BD API RECON (Andrew-directed):** base `https://api.blackdiamondwealthplatform.com`; OAuth
  `https://login.bdreporting.com/connect/token`; headers `Authorization: Bearer` + **`Ocp-Apim-Subscription-Key`
  => AZURE API MANAGEMENT**, which means every API carries a built-in OpenAPI/YAML export (matching BD's own
  "OAPI3 / retrievable as YAML" claim). **The catalog `/products` 404s unauthenticated** -- unlike Orion
  Eclipse's PUBLIC swagger, BD's is entitlement-gated by design ("APIs follow your user entitlements").
  Only `/`, `/authentication_password_flow`, `/sso_workflow`, `/signup`, `/signin`, `/reset-password` are
  indexed. **NO gateway probe taken** -- reading public docs is not the same act as an unauthenticated
  request to a vendor's API gateway, and BD is not on the lifted egress list. Realistic unlock = a dev-portal
  account (`/signup`; they name a Solutions Team) -- a relationship question, not a technical one.
- **PUSH DISCIPLINE BINDING** (Andrew 15:43Z via COO/CTO 154831Z): push ONCE PER WORK-PACKAGE CLOSE;
  ref-lock -> `git pull --no-rebase`, one retry, then wait >=2min. Never force, never rebase.
- Schwab lane unchanged: both masters at parity, leg-4 CLOSED, V2-2 CLOSED (`d7a9cdabe`), converter
  v0.17.0 @ 3008 (**no further resize this week -- CTO-ruled**), retry residual DEFER-BEHIND-WP7.
  **NEVER SUM 0824/0833.**

## Next Steps

- **[0.6.2 self]** (1) WP8-DECOM cell 3 -- new code-home proposal to CTO w/ the 09:46Z no-skip sequencing.
  (2) Zero-row thread: HAND HELD, no verb, pending Andrew. (3) SI2 P2 post-mortem is DELIVERED
  (`841e5e04b` + prior-art amend `3711cc63a`); doctrine promotion is CTO's call, not mine.
- **[1.0.0_SA_CTO]** the 2 marker cells (after nightly #2); doctrine routing on 0.6.0's ratified class +
  my section-8 checklist; the `inf-gold-trigger` re-entrancy question if he wants it chased.
- **[0.4.0_DS_ClientPlatform~B]** `INF_09` heals on nightly #2; `D_02c` single on CTO's word. Recovery
  singles on mode-stamped consumers need the trigger env carried (`INF_AOR_FOLD_ACTIVE=1`, `lambdas.tf:107`)
  -- his runbook line, CTO banked it.
- **[2.0.0_SA_COO]** bd-49f items 2/3 at Andrew's word; the bbgtml BYPASS pair correction to 0.2.0_DT.

## MCP traffic

~20 in / ~14 out. Significant: **Andrew-direct x2** (recorded + broadcast same turn); CTO (WP7 finding RULED
IN + it corrected his own frame; D_04 SETTLED (b) + he owned the restore miss; NEVER#4 ruled; marker routed
as 2 cells; WP8-DECOM cell 3 assigned); COO (push discipline binding; my zero-row caution carried to Andrew
verbatim in my own words); DS~B (P0 briefed -> ACKed -> cured; **he caught my 1:1 over-claim**); 0.5.0 (P2
ACK; measured that `rps` is absent from the bd-49f alarm set). All RAVC loops CLOSED; nothing pending an ACK
from me.
