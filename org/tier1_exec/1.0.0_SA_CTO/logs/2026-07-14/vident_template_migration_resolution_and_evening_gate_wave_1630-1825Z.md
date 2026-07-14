# 1.0.0_SA_CTO -- VIDENT TEMPLATE MIGRATION: resolved end-to-end (Andrew-direct) + the evening gate wave (1630-1825Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE, DEPLOY

## THE VIDENT RESOLUTION (Andrew-direct: "audit, assess, implement the replacement, logging the resolution")

**Trigger:** AJ's forward (received 15:35Z) of Vident's 2026-07-14 notice (Amrita Nandakumar,
President): all model changes move to their new "Active Manager Model" template; out-of-process
submissions will be delayed post-migration. Template obtained from Andrew's Downloads
(`Vident Template - Active Manager Model - FINAL.xlsx`), spec extracted from its Instructions
sheet (96 rows read in full).

**The new vendor law:** flat single-table FULL-MODEL file, 13 exact headers (Date/FundTicker/
BloombergTicker/ExchangeCode/YellowKey/CUSIP/SEDOL/ISIN/Currency/RecentPrice/TargetWeight/
TradeIndicated/TradeInstructions); TargetWeight = decimal FRACTION, column MUST sum to 1;
full portfolio only (deletions at weight 0; partial models refused by Vident); CASHTARGET
residual row; file `FUND_Model_YYYYMMDD.xlsx`, subject `FUND Model YYYYMMDD`, recipient
trading@videntam.com, 2:00PM ET cutoff; min-identifier combos (SEDOL alone = combo 4).

**Audit (complete surface, denominator enumerated):** the OLD template lived in THREE vendored
generator copies -- `portfolio_excel_generator/lambda_function.py:155` (PM export),
`trade-workflow-handler/src/excel_generator.py:19` (the execute path that EMAILS Vident via
send_brokerage_email), `trade-dashboard-api/src/excel_generator.py:19` (download) -- plus the
portal upload parser (`fileParser.ts`, old-format), routing config (PFDE/PFOE/PFFA/PFFV ->
vident; recipients test-wired), and 4 config.py copies naming the RETIRED real address
(trading@vfrmsolutions.com).

**Assessment finding:** the new template requires the FULL MODEL at every generation point, but
submission records stored trades only. Securities are immutable post-create (verified: no edit
endpoints) => the model can be frozen at export. Structural change: new submission records carry
`model_securities` (full model, fraction weights, Decimal for Dynamo) + `template_version`;
the twins regenerate from it; pre-migration in-flight records keep a LEGACY fallback (loud).

**Implementation (commit b9d61307c + map 1b7b77f62, audited lane override on Andrew's word;
lane owners 0.7.0 + 0.5.0 notified same-turn, both ACKed):**
- New 13-col generator in the export lambda (both payload shapes; MIN_MODEL_WEIGHT_SUM=0.5
  partial-list refusal; oversubscribed refusal; CASHTARGET computed at generation; sum-to-1
  asserted at every exit -- this producer will not emit a file Vident would misread).
- Twins rewritten byte-identical (their comment-only drift retired); model path + legacy fallback.
- Email laws in email_utils (vident branch): filename/subject exact, dated in ET (zoneinfo,
  precedented in this lambda); `trades@opalcapital.com` footer PURGED (Rule 23 -- domain we do
  not own, was in Vident-bound mail).
- config x4: real-address comment -> trading@videntam.com. LIVE WIRING UNTOUCHED (still test ->
  andrew@) -- flipping to the real vendor address is Andrew's go-live word, not mine.
- Download filename law via ResponseContentDisposition (internal S3 audit keys unchanged).
- Portal (DEV, 24fd10d0): upload parser detects the new template and GUIDES (the new file
  carries no deltas; parsing it as a trade file would fabricate trades). Merge conflict on
  surface-check.yml resolved THEIRS (same-lane 0.7.0 newer iteration).

**Validation BEFORE deploy:** harness in scratchpad grounded on the VENDOR'S OWN file as
positive control -- headers tie 13/13 (the control caught MY first read: I truncated the
vendor's 13th header with a max_col=12 dump and nearly shipped 12 columns), refusal mutants
fire (oversubscribed/partial), legacy percent-recovery byte-path intact, cash residual exact.
ALL CHECKS PASS. commit-gate clean x9.

**Deploy (ledger 20260714T1802Z, CLOSED 4/4):** 5 artifacts rebuilt from source (member sets
verified against DEPLOYED zips first), uploaded with base64 content-sha256 metadata (caught my
own hex-format error against the existing convention -- would have made every plan dirty),
read-back verified; source map sha registration x5; TF applies 0/1/0 (portfolio-management) +
0/4/0 (trade-pipeline) via safe-apply; 0-diff replan x2; live CodeSha256 x5 == uploaded;
import/execution smoke x5 (structured responses, zero ImportModuleError); tags
trade-pipeline-v1.20.0 + portfolio-management-v2.2.0 pushed --follow-tags; unpushed=0.

**Residuals, named honestly:**
- RecentPrice emits blank (no price source in the flow; not part of any min-identifier combo).
  Flag to AJ/Vident if they want it -- needs a price wire, separate scope.
- Exchange/YellowKey/Currency default US/Equity/USD (mirrors Vident's own example for a
  comparable US-listed model); every row satisfies combo 5 structurally + SEDOL where present.
- Manual/upload-born vident submissions (trades-only by nature) take the LEGACY fallback until
  re-pointed -- Vident accepts old format during their migration window; the PM-export lane
  (the primary) is fully compliant now.
- Live-path end-to-end proof = the next real PM export (records + file verified then); the
  generator logic itself is vendor-template-proven pre-deploy.
- Andrew decisions pending: (1) flip BROKERAGE_EMAILS vident -> trading@videntam.com live
  (SES-sandbox note in config may be stale -- verify at flip time); (2) reply to AJ (drafted on
  request); (3) optional controlled live test-fire before first real use.

## The evening gate wave (same window)

- **Schwab swap gate SIGNED** on 0.6.2's exercised expectation report (fbdb335b4; zero-int
  claim verified myself at e9d1a6817); 0.7.0 APPLIED + VERIFIED v0.9.0; probe-v2 landed roster
  + 2 template bodies. Delta-5 rulings: pin extension AUTHORIZED follow-on; 0-row-shell law
  ADOPTED (2025-01-09 = closed day); schwab ratchet queued strictly AFTER orion drain
  (shared-DLQ cross-attribution).
- **DS int64 fix reviewed APPROVED zero changes** (7724a02a3; the allowlist-guard test called
  out); 0.7.0 staged + I GO'd option (a); **dtype swap LIVE v0.10.0** (orion smoke correctly
  SUBSTITUTED with drain-exercise proof -- ratified). BD 05:00Z first fire now on fixed schema;
  eclipse heals tomorrow 16:00Z.
- **D1 Apply B GO'd, then RE-GATED on 0.7.0's surfaced 38-second cross** with DS's cell-4
  correction (fees quiet-day 0-row = land-flagged, never refuse) -- r2 confirmed, **LIVE
  v0.11.0**, first fire tonight 02:30Z, DS co-reads. D1 = the LAST 49METATABLES convergence
  input; the architecture session with Andrew arms on the landing.
- **Orion drain v2** running (2,340 landed; v1's botocore hidden-retry blindness caught +
  redesigned: AWS_MAX_ATTEMPTS=1, CW-sequenced, listing-based completion -- ratified).
- **Dual-COO collision** resolved (Andrew picked fresh PID 31880; predecessor stood down clean;
  my interim PID-ACK protocol stood down; /watcher orphan-doctrine fix routed + landing).
- **C9 cond-3 CLOSED 4/4** (early-fire claim falsified as TZ artifact, corrected @ 5a073c3bc);
  INF-adjacent slice-producer silence parked with hold owners (Door-5-adjacent, no action).
- **Rulings:** BDAPIMIG P1-DURABLE = SUPERSEDE-BY-D1a w/ named completion condition;
  SCHWABAUTO flex NO REDLINE (satisfied-by-C3, tail parked under OPAL_RUNNERS); pycache gate
  candidate routed -> COO staffed as AMENDMENT-1 on the safe-commit TO.
- **My review gate queue (next):** 0.6.2 delta-5 (96867ae10, suite 169+7, 12 vintage refusals
  retired on real bytes) + 0.6.2 V2-2(b) puller level-up (c03a8...).

## MCP traffic

~15 sent / ~14 received this window. Andrew-direct relay banked (NFRA_WEBSITE via 0.7.0~A).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-which | "black diamond metadata template tables" | near-tie routed | led to comp-grep on-rails |
| comp-grep | 'vident' / 'generate_vident_excel' / 'meta/templates' | 26 matches/16 files, denominators printed | the vident audit surface + the BD metadata producer (ingest-mirror rider) |
| comp-pulse | risk-reflex (auto in safe-commit) x4 | REFLEX CLEAN x4 | one immune-response citation read (config.py recorded-claims -- different node, filename match) |

Raw aws listings on opal-data-assets carried audited rail-checked markers (no comp-tool models
the monolith yet -- gap noted this morning, unchanged).

## Files Modified

b9d61307c (9 lambda/config files, audited lane override), 1b7b77f62 (source map), portal
24fd10d0 + fileParser commit (DEV), deploy ledger 20260714T1802Z (opened+closed), this log.

## Blockers

None mine. Vident go-live decisions with Andrew (recipient flip; AJ reply; optional test-fire).

## Next Steps

- [1.0.0_SA_CTO] delta-5 review + V2-2(b) review (queue head); 22:00Z triple-verdict read;
  cell-6 veto window closes ~22:30Z; architecture session arms on D1 first-fire + bridge proof.
- [0.7.0] drain to wall/completion; deletion TO; 02:30Z fire artifact check next wake.
- [0.4.0_DS] D1 co-read at 02:30Z expectations; eclipse heal verify tomorrow 16:00Z.
- [0.6.2] awaiting my two reviews; ratchet on 0.7.0's lane-clear.
- [0.5.0] 22:00Z triple-verdict (laptop stays on).
