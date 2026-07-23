# COT_ADVI_DIAG -- "not run in a week" diagnosed: chain RUNS daily; gold halts at A_03 since 07-21 on a 2-cell vendor text-format drift amplified by silver's object-sweep
**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, VALIDATE
**serial:** 0.7.0_AE_CloudOps
**window:** 2026-07-22 ~22:24Z -> ~22:47Z (Andrew-direct via CTO 222113Z -> COO TO @f8f2fbea0; read-only throughout)

## VERDICTS (the TO's five steps)

1. **GROUNDED:** "Cottonwood ADVI" = the `cot-pipeline` advi-cot thread (pipescript): cot-bd-session-trigger
   Lambda 4-phase EventBridge chain (cron(0 2) -> SSM session-fetch on cot-exporter i-0643a5bee8a8feabf ->
   bronze -> silver -> gold), serving s3://opal-data-cot/platinum/** to the AdvisorIntelligence Cottonwood
   tenant. DISTINCT from the 49F/0833 ADVI surface (opal-data-bd tree); firm separation maintained -- zero
   bd resources touched.
2. **FIRE HISTORY (census, denominators):** EventBridge default bus 141 rules (100+41, two pages), 10
   cot-matched, ALL ENABLED incl cot-bd-session-daily cron(0 2). Scheduler namespace: 10 total, 0 cot.
   Rule Invocations Sum=1.0 daily 07-08..07-22 (15/15), FailedInvocations EMPTY; lambda 3/3 phases daily,
   Errors=0. THE SCHEDULE NEVER STOPPED.
3. **TRADING-DAY FRESHNESS (calendar first):** Andrew's "a week" REFUTED as stated. Served platinum last
   build 2026-07-20T02:04:47Z (explicit-Z listing); header_metrics data_as_of=2026-07-17 = **3 trading
   days** behind the 07-22 frontier; write-lag 2 trading days. The "week+" perception likely comes from
   the STILL-frozen allocations/unrealized snapshot legs (as_of 2026-07-08 = **10 trading days**).
4. **KNOWN-FREEZE POINTER:** the A_03 crash is **NOT downstream** of project_cot_snapshot_zero_row_freeze_
   20260709 -- transactions was the healthy leg. Live state: that freeze is PARTIALLY CURED (holdings
   partitions 07-16/07-17/07-20 advancing at BD D+2; 07-20 landed 07-22T02:04:25Z). allocations +
   unrealized remain frozen at 07-08. Record stays open; closed nothing on it.
5. **LD-0333 INTERACTION: NONE.** First failure 07-21T02:03Z, ~40h before the 1819Z hold; nothing disabled.
   The 07-21T2314Z cot-ws5-rebalancer deploy postdates the first failure by ~21h -- ruled out by timing.

## THE MECHANISM (every hop artifact- or source-cited)

BRONZE: forwardfill_v2/transactions/TRANSACTIONS_DAILY_2026-07-21.xlsx -- full-column scan: 12,840
non-null Units, **2 NON-NUMERIC: rows 157+158 = str '9.6E-05'** (fractional shares exported as text).
Control 07-20: 13,303 non-null, 0 non-numeric. Delivery drift, 2 cells.
SILVER: cot_silver_merge.py:417-419 @5930dd45d ("Convert remaining object columns to string") -- 2 text
cells -> pandas object column -> sweep stringifies ALL. Artifact: silver/transactions/2026-07-21.parquet
units 12,840/12,840 str (07-20: float64). Deployed copy CONSTANT (s3 code/silver LastModified
2026-07-15T21:56:27Z; ran clean 07-16..07-20) -- input changed, not code.
GOLD: A_03.positions_cube.py:1001 `unit_txns['units'].abs()` -> TypeError bad operand type for abs():
'str' -> "ERROR: A_03 exit 1 -- chain halted" (cot-gold-run-2026072{1,2} logs, verbatim). SSM
opal-cot-gold-run Failed 07-21 (cmd 1784599424) + 07-22 (9f09c1e1-efa9); 07-20 "GOLD CHAIN COMPLETE
(exit 0)". Recurs nightly (full-table re-export carries the cells).
SERVED: platinum frozen at the 07-20 build. Invisible failure: SSM Failed has no consumer.

MEASUREMENT NOTE: initial SSM stdout was 24KB-truncated mid-A_02 -- the real failing step (A_03) found
only via the untruncated on-bucket log (logs/cot-exporter/gold-run/). A truncated success-tail reads
like a later-step failure; the full log is the instrument.

## ESCALATION + REPAIR (separate, CTO-gated, NOT executed)
Escalated to CTO 224551Z + COO 224628Z as a NEW live defect per the TO clause. Recommendation: (a)
silver-side coerce-numeric-before-object-sweep (DS lane, Rule 13/17); (b) idempotent silver re-run
07-21/22, nightly gold rebuilds itself at 02:00Z (no ad-hoc gold run); (c) optional A_03 guard.

## Compiler Tools
| tool | invocation | result | note |
|---|---|---|---|
| comp-which | cot ADVI question | PARTIAL | routed to raw hits, no curated rule -- coverage gap recorded per TO |
| pipescript | --list + advi-cot | PASS | named the full thread: producer/trigger/served/frontend |
| comp-pipescript deployed | cot_silver_merge.py | PARTIAL | scans opal-data-bd roots only -- cot code prefix uncovered (tool gap); vintage grounded via s3api on opal-data-cot/code/ instead |
| comp-grep | astype/object in cot_silver_merge | PASS | located the object-sweep :417-419 |
| aws events/scheduler/cloudwatch | census + fire metrics (rail-checked) | PASS | denominators printed; both namespaces |
| aws logs + ssm + s3api | lambda logs, command history, explicit-Z listings | PASS | the mechanism chain |
| openpyxl + pandas (scratchpad) | direct cell-type + parquet dtype reads | PASS | the decisive 2-cell finding + both controls |

**Gap found:** (1) comp-pipescript deployed does not cover the opal-data-cot code prefix; (2) SSM
gold-run failures have NO consumer -- a nightly deterministic FATAL was invisible until a sovereign
noticed the screen; (3) comp-which has no curated cot-ADVI rule.

## Next Steps
- **[1.0.0_SA_CTO]** gate the repair (silver coerce-numeric fix is DS-lane); route the three gaps.
- **[0.4.0_DS_ClientPlatform]** on CTO GO: the one-function silver fix + idempotent 07-21/22 re-run.
- **[0.7.0_AE_CloudOps]** back to IDLE: available after this log commits; nothing further without cascade.

---

## CLOSURE 2026-07-23 ~1028Z -- VERIFIED, mechanism proven by the cure

DS fix @2ed963ef6 landed 23:10Z (2.5h ahead of window; his ledger 20260722T2310Z closed). The 02:04Z
nightly then self-healed with ZERO ad-hoc runs: cot-gold-run-20260723-020651.log ends "=== COT GOLD
CHAIN COMPLETE (exit 0) ===" (Completed 02:08:57Z); platinum/firm/* advanced to 2026-07-23T02:08:56Z;
header_metrics data_as_of 2026-07-17 -> 2026-07-21 (T-2, inside the BD D+2 holdings contract, inside
CTO's 07-21/22 bar). Reported CTO 102905Z + COO 102911Z; MEMORY.md trigger discharged (deleted).
allocations/unrealized remain frozen at 07-08 -- standing record open, separate defect.

ALSO CLOSED same window (MSTR relay of CVO~Z finding): the stranded eclipse-converter artifact_sha256
in lambda-source-map.json -- live CodeSha256 grounded the WORKING-TREE value (deployed 07-22T14:50:08Z,
1 min after predecessor's 010d458e5 rebuild); committed @192d065c0 with consistent last_deployed_* .
ERROR OWNED: 192d065c0's last_deployed_commit tail was expanded FROM MEMORY (fabricated); self-caught
same turn vs git rev-parse, corrected @3c680049e (verified ancestor-of-HEAD). A provenance field is a
RETRIEVAL, not a recollection.

---

## 6d DISPATCHER WIRING 2026-07-23 ~1052-1102Z (morning batch, joint DS+AE) -- LANDED, ledger 5/5

**archetype for this arc:** DEPLOY. DS's revamp_stage 6d block (patch @3e7a59502) landed in
mdpf-daily-dispatch.sh @4528fa154 + AE PYTHONPATH resolution (the pair's ../../../mdpf repo-relative
insert cannot mirror on the runner; COT_PYPATH resolves imports from the synced canonical dirs, zero
module duplication). Six artifacts staged to s3://opal-data-mdpf/code/ ETag==md5 verified per key
(dispatcher 6f26beac; bdmp/pair/slice; silver/rebalancer_schemas; gold/dim_mdpf_aum_metrics).
**The import-chain EXERCISE caught 2 gaps a config-read missed:** dim_mdpf_aum_metrics ABSENT from S3
(pair imports it -- tonight's 6d would have died) + the unlisted transitive dep
mdpf_revamp_model_crosswalk (verified already on S3). Runner-sim probe: pair resolves bdmp +
_distribution_stats + calc_metric + quarter_ends clean. Ledger 20260723T1052Z CLOSED 5/5; NO schedule
change, NO TF, NEVER#4 held (the scheduled 02:04Z run IS the exercise); outcome banked as MEMORY.md
trigger 07-24 post-02:10Z (marker keys_staged=11, slice covered_dates nonempty). Compiler tools:
deploy_ledger x7, safe-commit x2, git apply --check, bash -n, s3api listing-verify x8, comp-glob/grep
(dispatcher + import discovery), runner-sim import probe.

---

## DRIFT CLOSE 2026-07-23 ~1110-1114Z -- CotDetectionSnsPublish re-added (declared==applied exactly)

0.6.2~A found (during his WS-1 targeted apply, correctly NOT swept): live cot_exporter_policy carries
CotDetectionSnsPublish (sns:Publish opal-bd-cot-cookie-alerts) that repo TF lacked -- the next FULL
apply on cot-pipeline would have silently removed a live grant. GROUNDED before acting: live
get-role-policy carries the statement verbatim; repo already declares the TOPIC (cot-detection-layer.tf:40)
AND the on-box publisher env (ssm.tf:137) -- the grant was the single missing limb of a TF-declared path,
corroborating hand-landed-or-never-repo'd. CTO disposition 111105Z: RE-ADD present-to-match-applied,
question-of-the-alert PARKED (no-alarms word), removal-if-ever = deliberate reviewed change never a
side effect. LANDED @20322eb30 commit-only; targeted plan now "No changes." = declared==applied EXACTLY,
landmine dead. Loops closed with 0.6.2~A + CTO; S1 sequencing ask at CTO (RF-9 rebuild couples to DS's
S5 twin -- one rebuild could carry both; his call, nothing staged).
Per CTO: two gates earned their keep in the finding's own provenance -- 0.6.2's safe-apply MSYS block +
HALTGT surfacing my 14h-stale S1 ask (the ask predated his watcher; the checkpoint delivered it).

---

## (b) CLOSED-ALREADY-SATISFIED 2026-07-23 ~1119Z (CTO ACK 111926Z)

CTO ordered the S1 (b) rebalancer event wiring built NOW; four live reads showed the estate had already
built AND exercised it on its own schedule this morning: manifest 20260723T060051Z mode=='event' (the
cron(0 6) runner completing into OnSuccess=opal-assets-silver-blackdiamond, config unchanged since
v0.31.0) + manifest 20260723T050009Z mode=='sweep' -- both paths proven independently, the S1 TO's
verbatim bar. 0.6.2's "sweep backstop is carrying it" refuted at the artifact (stale census). Built
NOTHING, opened NO ledger, and DECLINED the one buildable remainder (a per-object S3 .json notification)
because it would contradict the standing WS-5 shape ruling -- CTO: "an order that would un-rule a ruling
by wiring is exactly the kind of order that should die at stop-before-build, including when I am the one
who gave it." Third live-primitive stale-premise catch in 24h (RF-10, the pk-frontier no-op, this).
(a) unchanged: one rebuild carrying DS's S5 twin + RF-9 when the batch reaches S5; EOD decouple armed.

---

## RULE-11 INSTRUMENT UN-BLINDED 2026-07-23 ~1239-1246Z (CVO~Z via MSTR re-grounding)

verify-ec2.sh false-skipped 26/27 services on this host: jq.exe emits CRLF stdout (file clean LF), the
key loop's $SERVICE carried a trailing \r (not in IFS, survives word-splitting), the inner
.services["name\r"] lookup missed -> "No source_path" for every populated service. MSTR's re-grounding
mattered: CVO~Z's stated cause ("populate the manifest") was wrong -- 18/27 were populated; the fix was
the instrument, not the data. FIXED @9a9e92842 (tr -d '\r' at the iteration source, measured comment).
DIFFERENTIAL PROOF: pre-fix 26 skips reproduced; post-fix skips == exactly 9 == the genuinely-unpopulated
complement of MSTR's 18/27. First real read: 27 checked / 2 clean / 16 drift-signals / 9 skipped.
ROUTED TO CTO (not adjudicated): the 16 drift-signals' large counts (187/219 on bd trees) read as STALE
deployed_commit reference fields (deploy path likely never updates them), not real drift; + the 9
missing-source_path coverage item. Compiler tools: bash -n, verify-ec2 x4 (repro/differential), jq
behavior probe (MSTR's, cited), safe-commit.

---

## CRLF CLASS-SWEEP CLOSED 2026-07-23 ~1301-1305Z (CVO~Z sweep via MSTR)

The @9a9e92842 class generalized: CVO~Z swept 18 jq-using scripts, 3 unfixed sites, all landed
@41468f569. Site 1 sync-ec2-manifest.sh = the same key-iteration shape on a WRITER (would silently
sync nothing on this host) -- fixed + probed behaviorally WITHOUT running the writer (read-only
replication of key-extraction + lookup: 12/12 non-empty post-fix vs 0 tainted). Sites 2/3 =
value-capture strips (hedged/loud-fail classes, stripped at capture). parity-gates.sh already carried
prior art (7 strips -- the class was met locally before; the sweep made it estate-level).
MSTR's causal DE-LINK accepted: sync-ec2-manifest writes instance_id/_last_updated, NEVER
deployed_commit (grep 0) -- the stale deployed_commit reference layer remains the SEPARATE
CTO-routed batch-tail item, proceeding on its own mechanism-first grounding.

---

## DAILY-AUA ARC 2026-07-23 ~1413-1438Z (Andrew-direct dispatch -> mechanism -> walk-hold)

**DISPATCH:** emitter revival + full-lookback backfill (CTO 142132Z + derivation ruling 142316Z).
**MECHANISM (checkpoint 1, accepted "exemplary"):** the emitter NEVER stopped -- fires 17:15Z daily,
0 errors, faithfully re-emitting the frozen 07-18 served partition (Andrew's carried $1.782B = that
re-emit verbatim). Chain: platinum frozen because mdpf-daily-runner last completed 07-18T15:02Z;
trigger event-keyed on opal-data-inf Door-6 (last wrote 07-18T14:59:10Z); ROOT = inf gold chain FAILS
at INF_C_01 daily since 07-19: nna_coverage_guard.py:320 NNACoverageRegression -- roster dropped
accounts 609/1225/703/560 ($-44,206.28 SERVED NNA, 11-36 partitions each); the guard REFUSES the
history rewrite and the dispatcher withholds Door-6. A WORKING GUARD, not a dead pipeline (the
COT_ADVI class one level up). 4 identical fails 07-19..22; kill-switch NOT engaged (release present,
co-signed). Unblock = the guard's own excusals path -- DS evidence -> CTO/Andrew decision, not mine.
**BACKFILL PREP (conditions 1-6):** input census 430 partitions to exactly 2024-11-01; emitter has
native run_date override + --backfill (same code path); idempotency structural (PK/SK keyed upsert).
**CONTROLS (approved, pre-hold):** all 21 existing dates re-invoked on DEPLOYED bytes -- ALL 24 mdpf
rows byte-reproduced on all 21 incl the 07-18 pin; 6 partitions' etf_ownership rows upgraded
rolled_forward->fresh (original runs predated their etfs daily file; re-run reads the true per-date
file). Before-snapshots preserved. DESIGN FACT surfaced: the emitter reads a SECOND live source
(opal-data-etfs daily, :692-759) -- not a pure function of the served aggregate; the re-source
boundary must cut between the 49-custody leg and the etf-ownership leg.
**WALK HELD (CTO 143507Z via COO circularity finding):** a full-span walk would re-store the legacy
schwab_canonical estimate Andrew is moving off. ZERO historical writes (table-verified 21/588
unchanged). Ledger 20260723T1427Z closed truthfully (the tool correctly REFUSED hold-with-open-
activation-leg; legs closed as stood-down-with-proof); the corrected run (post DS derivation +
emitter re-source, my integration half) opens its own ledger.
**Instrument note:** the 21-invoke first attempt failed wholesale on --cli-binary-format (CLI v2 flag,
v1 host) -- clean CLI-level failure, nothing invoked; re-ran with the v1 payload form.

---

## RULINGS EXECUTED 2026-07-23 ~1440-1451Z: SNAPSHOTS DURABLE + RF-9 DECOUPLE DEPLOYED

(1) KEEP-ruling conditions: before-snapshots (21 files/588 rows, sha50cd4f87) committed to
deliverables/aua_before_snapshots_20260723/ @d15c83489; ledger 1427Z amended w/ the upgrade event.
(2) RF-9-ONLY REBUILD (ledger 20260723T1445Z closed 5/5, tag opal-assets-v0.32.0): vendored-parity
battery caught the EXPECTED deliberate divergence (rebalancer_* = pre-S5 production vs canonical
post-S5 @1351c74d9 -- the ruled scope); zip->artifact-bucket w/ content-sha256; targeted plan = pure
version+hash swap; safe-apply 0/1/0; 0-diff; LIVE-zip triple identity (built==Code.Location zip==
CodeSha256) w/ BD_TABLE_EXTENSIONS present; import-health probe = handled ValueError @1129, NOT
ImportModuleError. 0.6.2's RF-9 live ahead of tonight; sweep backstop no longer the carrier.
Compiler tools: deploy_ledger x14 (2 ledgers), cmp battery x8, terraform plan -target x4 + validate,
safe-apply x1, s3api head-object x2, lambda get-function/invoke probe, curl live-zip, git tag preflight.

---

## CONTROL SHAPE BANKED 2026-07-23 ~1514Z (CTO 151403Z, for the corrected backfill -- my next leg)

Andrew ruled C2: 49-total = fact_rps_s2.net_mv_plus_cash (silver/schwab/08242234, cash IN).
Controls for the corrected run, verbatim-banked: (1) C2-TIE per date TO THE CENT (pin 07-17 =
$1,665,338,126.76; month-end spot-grid + full-span programmatic equality sweep as primary);
(2) the 21 legacy rows = SUPERSEDED-WITH-MECHANISM, per-row pinned delta (+cash leg, +vintage),
restoration record = deliverables/aua_before_snapshots_20260723 @d15c83489; (3) denominators vs
silver partition depth per cohort, honest-absent enumerated; (4) idempotency proof + throttle +
two-limb boundary carry unchanged. GATE: DS's C2 derivation contract lands -> my emitter 49-custody
limb re-source integration (one-writer boundary at the limb split) -> deployed normal cycle -> walk
on corrected bytes, own ledger. Idle-warm on this thread until DS hands the contract.

## FEASIBILITY FACT BANKED ~1537Z (COO 153706Z, byte-verified): both backfill legs silver-reproducible.
Model leg: smartx fact_model_aum_daily intra-partition `day` series spans 2021-09-02..present (1,226
days) -- history rides INSIDE the latest partition, not across run_date partitions (the run_date-axis
sparsity I measured was the axis-confusion class). Custody leg: C2 fact_rps_s2.net_mv_plus_cash, 541
partitions, gaps=0, to 2024-05-24. Backwards portal->DDB flow unnecessary. Honest boundary: per-account
detail 07-14+ only. Design consequence carried: re-sourced emitter = three limbs, three input classes,
one writer (model=latest-partition day series; custody=per-date C2; etf-ownership untouched).
