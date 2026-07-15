# 0.5.0_AE_OpalETL -- THE CUTOVER NIGHT: laptop leg retired + v1.3.0 live (2026-07-15 22:45-23:58Z)

**archetype:** DEPLOY

Continues session_feed9_now_and_name_map_1913-2115Z.md + the fire-close log. The window Andrew
re-timed at ~22:4xZ ("we do everything in our power to complete the consolidation NOW") ran
end-to-end in ~75 minutes with zero stranded legs.

## 1. V2-1 review arc (pre-cutover, filled the wait)

- CTO REVIEW PASS 231419Z (he md5-tied the guard lift himself: dea80c78... both copies).
- msn strike BUNDLED per his ruling -> authored as the second reviewed commit e45606d46
  (-89/+30; tombstone cites the full chain; source=msn HISTORY rows preserved as carry-forward
  -- the strike removes the TIER, not the past; tier numbering kept). His fast-review PASS
  232938Z on his own diff read. Tag bump 233744Z: v1.2.0 consumed by the flip leg -> v1.3.0.

## 2. THE CUTOVER (Andrew pace order via CTO 224440Z; ledger 2259Z, CLOSED 23:47Z @ f66d2f5ae)

Split: 0.7.0 = TF/deploy legs 1-3; me = fire+verify legs 4-5. As run:
1. [0.7.0, v0.20.0] V2-8 converter LIVE -- first build defective (missing mirror closure +
   stub runtime), CAUGHT by the import-health smoke PRE-WIRING, zero consumers; corrected
   closure live-tied, reviewed sha256s unchanged; designed-refusal re-smoke proved import
   closure on the deployed artifact.
2. [0.7.0, v0.21.0] Rules 6-8 LIVE as DS filled them; 14 configs verified, 11 pre-existing
   intact; rule 9 msn never landed.
3. [0.7.0, tag etfs-netassets-v1.2.0] SILVER_ROOT="" LIVE (env read-back exact).
4. [me] VERIFY FIRE 23:37:27Z (pre-fire live env read; sha 40KaO/7j held -- one variable).
   Harness: bronze 4/4 fresh 23:37:34; legacy LIVE silver 5/5 fresh 23:37:39 (flip PROVEN);
   event wiring PROVEN (4 writes -> 4 converter invocations timed to them); conservation
   85+23=108 ties. THE LETTER-GAP: fact tables stamped 23:30 (pre-fire) -- **STOP-AND-REPORT
   filed rather than self-adjudicated.** CTO ruling 234422Z: CLEAN-BY-MECHANISM w/ rider 1
   (writer identity) -- resolved GREEN: the 23:30 writer WAS opal-assets-silver-etf itself
   (RequestId 1be4423f; 2,549ms WRITE-run vs 156-780ms skip-runs -- DURATION discriminated the
   code path where log-silence could not; this converter prints nothing even when writing).
   Provenance source-confirmed by 0.7.0 (TriggeredRules Sum=1: the container sweep's designed
   23:30 slot, first sweep after the real converter -- converted the 22:00 backlog; negative
   controls closed all other cells). NET: BOTH conversion paths (sweep-write + event-skip)
   exercised on one partition with byte identity.
5. [me] Windows task "ETF NetAssets Daily Probe" DISABLED 23:45Z, verified State=Disabled.
   **THE LAPTOP LEG IS RETIRED.** Recovery runbook in the ledger (one command + one hand-fire,
   1-day T-1 bound). AC3 tomorrow 22:00Z = the named full-letter confirmation; FAIL =
   re-enable immediately, no adjudication.

## 3. THE v1.3.0 PRODUCER SWAP (ledger 2349Z, CLOSED 23:55Z @ b399a0a38)

Both approved commits, one artifact: build+upload write-VERIFIED 16,988B (both modules zipped);
source-map sha committed pre-apply @ a8dfef12f; plan gate MET EXACTLY (0/1/0, only
s3_object_version + source_code_hash); safe-apply 6s; 0-diff textual; **THREE-WAY TIE EXACT
built==uploaded==live = 4/6gMExwwY1w3No9D4AeTARMXZaVjDHf1cBYq7yL5gw=**; tag
etfs-netassets-v1.3.0 pushed --follow-tags. The landing guard + persisted manifests + retry
client + the msn strike are LIVE. Tomorrow 22:00Z = ONE fire, TWO named confirmations (AC3
guard verdict + cutover full-letter).

## Compiler Tools

comp-pulse (auto, every safe-commit this window x6) -- all REFLEX CLEAN, measured. The
source-map risk-reflex citation re-fired on the ci commit; same memory read + honored earlier
tonight. No comp-tool covers the SmartX/ETF vendor surfaces (standing gap). Raw aws this
window: operational only (invoke, get-function-configuration verifies, CloudWatch reads for
the rider-1 instrument, the shim throughout).

## MCP traffic

In: CTO x5 (pace order, V2-1 PASS, strike PASS, tag bump, leg-4 ruling, cutover ack), 0.7.0 x4
(GO-6/ETA, leg-1 start, legs 1-3 complete, provenance answer), COO x2 (V2-1 GO context, acks).
Out: 11 (pace ACK + confirm, refs, ledger notices, STOP-and-report, provenance ask, completion
evidence x2 waves, v1.3.0 evidence). Every loop closed; nothing pending on me.

## Open at close (the whole lane)

- [TOMORROW 22:00Z] the one fire, two confirmations. FAIL path: ledger runbook (re-enable +
  hand-fire) + report. My watcher discipline re-arms tomorrow's landing check on the NEW
  producer's guard output (its manifest at {source}/{scope}/meta/pulls/20260716/).
- [parked, Andrew's word] Tax SMA (deferred) - Opal Equity Growth (parked).
- [days] MSTR LCLRPO data/smartx disposition.
