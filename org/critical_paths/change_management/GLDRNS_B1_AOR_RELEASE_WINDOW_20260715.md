# DEPLOY-COMPLETION LEDGER — GLDRNS.B1 AoR RELEASE WINDOW (opened 2026-07-15 22:42Z)

**Status: OPEN — closes only with the chokepoint RE-ARMED (NEVER#6 + COO condition: the safety back = closed)**
**Owner: 0.4.0_DS_ClientPlatform~B · Authority: Andrew sovereign GO verbatim x2 @ aab5f21d5 · CTO gate-owner
confirmation 224747Z · COO both-halves co-sign 225320Z/225340Z (AMEND-48 conditions verbatim) · Door-5 open by
0.7.0 225853Z (their ledger closed 22:58Z)**

## REVERT ARTIFACTS — CITED BY PATH, PRE-STAGED BEFORE THE CHOKEPOINT FLIPS (the binding condition)

| # | surface | revert artifact (path) | exercised? |
|---|---|---|---|
| 1 | served platinum spine (firm 2,316 + advisors 26 objects) | `s3://opal-data-inf/backup/served_spine_PRE_AOR_RELEASE_20260715T225000Z/{firm,advisors}/` — counts tied 2,316/2,316 + 26/26 | **YES** — one key restored via `backup/_restore_exercise_20260715T225000Z/` and md5-tied to live (`5c1910ad…`) per CTO pin 1 |
| 2 | gold/canonical (the stamp surface, 1,410 partitions) | the 07-13 ETag-verified 8,805-object backup (`s3://opal-data-inf/backup/served_spine_PRE_TIMELOCK_2026-07-13T184646Z/` family) — **still current: gold last written 07-10, before the backup** | verified-current by LastModified; restore = the un-stamp recovery op (AMEND 20: a recovery, not a rollback — which is WHY the pre-stamp verify is the binding control) |
| 3 | fold switch | delete the `INF_AOR_FOLD_ACTIVE = "1"` line (commit `9932a3dd5`) + `safe-apply` → empty export → dispatch default 0 (servicing basis returns) | mechanism exercised in reverse tonight (the dark introduction) |
| 4 | silver rescue converter | `s3://opal-data-inf/backup/pre_rescue_20260715T2259Z/convert_transactions_to_silver.py` (one `cp` back) | banked pre-overwrite, md5 of banked == pre-deploy live read (`70110fbe…`) |
| 5 | Door-5 collision state | `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/door5_decollide_20260715/revert.sh` — 0.7.0's one-command full-state restore, 4 copies banked md5==ETag 4/4, committed `030ffaeb7` BEFORE the open | 0.7.0's ledger, closed 22:58Z |
| 6 | chokepoint re-arm | remove `INF_GOLD_DISPATCH_RELEASE` from the trigger env (CTO's mechanism, same vehicle that sets it) — **fires in-session the moment stage-B outputs are verified** | the refusal side exercised live tonight (harness ARM 4) and on 07-13 (0.7.0, mode-agnostic) |

## STAGE-1 MOTIONS — COMPLETE, evidence inline

1. **Step-0 snapshot + exercised restore** — row 1 above. MANDATORY-FIRST honored (taken 22:50Z, before any motion).
2. **Fold switch ON (dark wrt dispatch):** TF commit `9932a3dd5`; plan diff = exactly `+ INF_AOR_FOLD_ACTIVE = "1"`;
   applied ~22:56Z; live env verified: `INF_AOR_FOLD_ACTIVE=1`, `INF_GOLD_DISPATCH_RELEASE` ABSENT (still held),
   `INF_GOLD_DISPATCH_HOLD` present, PERF ceiling untouched (Door 2 sealed — the risk-reflex HOLD citations on
   lambdas.tf were read; the ceiling var was not touched).
3. **Silver rescue deployed (the frozen-3 in-order chain step, CTO-confirmed 224747Z):** pre-rescue banked (row 4),
   siblings 0/0/0, local==origin `77009b25…`, deployed + download-verified TIE. The rescue = `10273505d`
   (rep_id rescued from household_rep_mapping — the same canonical map — + `rep_id_source` provenance column).
4. **Door-5 de-collided by 0.7.0** (225853Z): silver→gold both basenames, annotated copy PRESERVED (CTO pin 2),
   post-verify ETags identical pairs, silver keys untouched, revert armed (row 5). Step-zero FATAL clears.

## THE RUN PLAN (modes grounded in the deployed trigger + dispatch)

```
SENTINEL (CTO+COO string on inf-gold-trigger)             <- THEIR motion; window's only remaining pre-run gate
STAGE A  trigger mode=gold-a                              <- resolver (fold ON, pin auto-set) + A-group dims.
                                                             INF_C_01 NOT in this chain; D-group NOT in this chain.
                                                             NOTHING STAMPS, NOTHING SERVES.
PRE-STAMP VERIFY (the sovereign's "see if it gets it right"):
         timelock_preview on the FRESH SSOT (pinned to the partition the resolver read)
         + fold_map == 164 / explicit == 837
         + invariants: FIRM TOTAL $133,107,667.64 UNCHANGED TO THE CENT · phantom resolution path armed ·
           joe DOWN ~$2.1M / peter UP ~$1.6M / patrick UP ~$1.03M (incl. $52,604.80) on the proposed re-key
         ANY OTHER READING = STOP -> restore from rows 1-5 -> chain re-held -> report. NO STAMP.
STAGE B  trigger mode=full                                <- bronze pulls revive (txn feed catches up 07-10->now;
                                                             ceiling self-heals on fresh bronze) -> silver (RESCUED
                                                             converter; rep_id rescue kills the phantom at source)
                                                             -> resolver re-pins -> gold A/B/C: INF_C_01
                                                             FOLD -> LOCK -> STAMP with the full guard battery
                                                             (residual RAISES if the phantom survives; coverage
                                                             continuity; roster usability; fold-landed 6-way)
                                                             -> D-group serves the platinum surfaces.
POST     served-spine read vs the invariants + vintage DISCLOSED TO ANDREW with the numbers (COO c2)
         -> CHOKEPOINT RE-ARMED same session (row 6) -> this ledger CLOSED
         -> CVO~B V4 re-take on the served artifact (their lane, live since 22:37Z).
```

**Stamp-order absolute throughout: the fold carries real data (837/874 explicit AoR on the 07-15 scheduled row,
verified twice today by independent derivations) BEFORE any lock; the first stamp is immutable and is taken only
after the pre-stamp verify reads exactly the pre-registered numbers.**

## RUN LOG (appended as the window executes)

**RUN 1 (23:29:20Z dispatch, mode=gold-a): DIED AT +13 SECONDS.** Launch receipt clean (fold forward echoed,
pin set); background chain exited 23:30:43 (pinned by its own exit-trap 5-sudo fingerprint in the journal);
zero S3 writes; watchdog CORRECTLY reaped the idle box at boot+10min (its persistent log, verbatim: "no gold
process; last sighting 452975s ago" — and the same log shows 07-11/07-12 with identical signatures). The
traceback was UNREADABLE: the chain log lived on tmpfs and the power cycle wiped it. Prime-suspect mechanism
(grounded locally, NOT yet confirmed on-box): the dispatch's ADHC_COMPIL.013 gate — `comp-freshness chain inf`
exits 1 HERE on the held chain's own frozen artifacts (txn silver 130h + all gold ~130h) = the run built to
heal the staleness blocked BY the staleness. Runner-side confirmation requires the readable log (below).

**RUN 2 (00:14:37Z dispatch, DIAGNOSTIC REPRODUCTION per COO AMEND-55 grant): DIED +16s — AND DELIVERED.**
The instrumentation (66fd803e7) worked on first exercise: the exit trap shipped the chain log to
diagnostic/chain_logs/chain_gold-a_20260716_001441.log at 00:14:58. THE TRACEBACK, VERBATIM:
`FATAL: sync_scripts() basename collision -- COLLISION: aor_attribution_audit.py` between
`code/gold/_aor_exercise/lib/` (07-12 leftover, sha a304fd6a…) and `code/gold/lib/` (07-15 22:21 —
**~B's own G3 missing-lib deploy CREATED this collision**; run-1's +13s death = the same FATAL,
retroactively explained). ROOT CAUSE OF THE PRE-FLIGHT MISS, owned: the AMEND-51 sibling check covered the
four prefixes' TOP LEVELS; sync_scripts flattens RECURSIVELY — the exercise subprefix was in the flatten's
domain and outside the census. **RETRACTED: the comp-freshness/.013 prime-suspect** — the log answers it:
"comp-freshness not found in PATH -- freshness gate skipped" (the tool is ABSENT on the runner; the local
exit-1 measured ~B's box, not the runner; .013 is VACUOUS on the box it guards — debt list). Bonus: the
guard printed "collision OK (identical x2)" for both de-collided pairs — 0.7.0's Door-5 form verified by
the guard's own read. FIX (CTO gate pending): cp canonical over the _aor_exercise copy (byte-identical,
nothing deleted) + a RECURSIVE basename census over all four prefixes before run 3.

**RUN 3 OUTCOME (00:25:32Z dispatch): STAGE A MECHANICALLY COMPLETE — AND THE PRE-STAMP BAR FIRED. STAGE B
STOPPED.** Step zero passed (census fix held); resolver ran fold-ON in production first-ever (SSOT 00:25:54Z,
874 rows / 164 movers / pinned digest tie); A-group dims rebuilt 00:26:00-55Z; 250KB chain log shipped;
box self-stopped; NOTHING STAMPED, NOTHING SERVED. VERIFY: fold 164 ✓, explicit 837 ✓, firm total
$133,107,667.64 to the cent ✓, phantom present-unmoved ✓ — **CHANGED ROWS 0 of 9,510 vs the pre-registered
mover backfill = ANY-OTHER-READING = STOP.** MECHANISM (grounded from the ledger's own events): the 07-13
fold-OFF seed wrote 873 'baseline' events carrying THE SERVICING KEYS as AoR (peter 628/patrick 141/joe 83/
iwm 21 == the rep_id map); run-3 wrote the 164 real 'change' events (noel 64/joe 64/patrick 22/peter 15);
first-observation-extends-backward therefore resolves ALL history to servicing and noel inherits nothing.
A stamp tonight would have FROZEN SERVICING HISTORY FOREVER WITH EVERY GUARD GREEN — the stamp-order trap's
live firing, CAUGHT BY THE PRE-STAMP CONTROL. The fold-then-lock order is why this is a pre-stamp DESIGN FIX
(re-seed the ledger baseline from the real first-available AoR) and not a recovery. FORK SURFACED to
CTO+COO (+ Andrew's one-liner likely, it construes his "first available AoR"): seed-as-infrastructure-artifact
(re-seed, intent) vs seed-as-first-observation (letter, contradicts the project's purpose). Window paused at
the bar; chokepoint re-arm triggered on the exit report 003314Z.

**THE FIX, BUILT + DRY-VERIFIED (write HELD for Andrew's word):** the design's own docstring
(advisor_timelock.py:489-491) rules the fork in (a)'s favor in the code's own voice — "ABSENT (0 keys) ->
a LEGITIMATE zero... the current resolution IS the first observation and it backfills all history." Fix form
= BANKED-EMPTY (bank ledger+state, empty both; the producer's own first_run seeds the TRUE baseline — no
hand-authored history). DRY ORACLE RED-then-GREEN: live-ledger arm reproduces 0-change; ledger-absent arm
reads **1,257 rows re-keyed / noel +$8,401,521.22 / joe +$7,384,568.89 / patrick +$3,448,754.37 /
peter −$18,744,660.92 / iwm −$490,183.56 / conservation −0.00 / phantom unmoved** — THE TRUE A1-BACKFILL
NUMBERS, superseding the pre-fold trio as the preview bar (co-read to pre-register before resumption).

**BAR RE-REGISTRATION (CTO governance precision 005003Z — TWO COMPUTATIONS, TWO BASES, discriminated so the
record can never read as a moved goalpost):**
- **The OLD preview trio** (joe −$2.1M / peter +$1.6M / patrick +$1.03M) was the **PRE-FOLD, TIME-LOCK-ONLY
  prediction** — the correction of the 07-08 transfer's nightly-rewrite, computed BEFORE Andrew's A1-backfill
  ruling existed. It was the never-widen half's named basis (225320Z). It is NOT wrong; it answers a
  question the ruled computation no longer asks.
- **The ARM-2 numbers** (noel +$8,401,521.22 / joe +$7,384,568.89 / patrick +$3,448,754.37 /
  peter −$18,744,660.92 / iwm −$490,183.56; conservation −0.00; changed_rows 1,257 == the 164 mover
  accounts' historical rows; phantom present-and-unmoved at the preview instrument) are the **RULED A1
  BACKFILL over the TRUE baseline** — the computation Andrew's "we backfill the first available AoR"
  actually commands. **$18.7M moving off peter's history is a magnitude the signatories see, not inherit:**
  COO's FRESH signature is asked explicitly on these numbers (CTO's ask in flight); Andrew's fork word
  carries the magnitudes. The served-spine bar is OTHERWISE UNCHANGED (phantom GONE / Patrick's $52,604.80
  home / noel present / sum ties to the cent / the three-leg exclusion oracle).

**COO FRESH SIGNATURE: IN (AMEND 57, ARM-2's numbers named exactly). The resumed-verify bar is now, in
full: {the five ARM-2 deltas TO THE CENT · conservation −0.00 · changed_rows 1,257 SET-IDENTICAL to the
164 movers' historical rows · NAMED-KEYS-ONLY x/1,257 with denominator (both sides of every re-attribution
within the named canonical set; ZERO catchall/unknown/unmapped either side — conservation cannot see
garbage-into-catchall, the 04-28 lesson; iwm as donor = the catchall SHRINKING, and the check proves no row
flows the other way) · phantom present-and-unmoved} at preview; the unchanged served-spine bar after.
Instrument built + syntax-checked: resumption_verify.py (single script, prints every arm with PASS/FAIL +
denominators, exits nonzero on any miss = STOP). ONLY ANDREW'S WORD REMAINS.**

## 🟢 ANDREW'S WORD — VERBATIM RECORD (the fork ruling)

> **"Go a"** — Andrew-direct, CTO terminal, **~01:2xZ 2026-07-16** (time per CTO's correction 012807Z; his
> broadcast landed 01:27:44Z immediately after the reply). SCOPE: a direct reply to CTO's recommendation
> package carrying the threefold (a)-authority + the ARM-2 magnitudes INCLUDING noel +$8.40M / peter
> −$18.74M + the banked-empty form + the resumption sequence — so COO's post-dates-magnitudes condition is
> satisfied BY CONSTRUCTION. Ruling: fork option (a) — the 07-13 fold-OFF seed is NOT "the first available
> AoR"; re-seed via BANKED-EMPTY; finish under AMEND-54 + AMEND-57.

**RUN 6 OUTCOME (02:21Z dispatch): SAME pre-stamp refusal — AND THE LAST HOLE IS ONE FLAG.** The healed
pull ran (census: identical x2, the new bytes) but its roster emission sits behind `--with-roster`
(promoted file :242-247/:283-291 @ 57538722f) and the dispatch CATALOG row passes only `--upload-bronze` —
the Lambda's call site passes the flag; the chain catalog never did. Change-3's THIRD half-landing, one
flag wide. Abort 40+ scripts pre-stamp; NOTHING MOVED; AMEND-57/58 untouched. FIX STAGED (uncommitted,
one line: the catalog row gains `--with-roster`), proposed 024307Z; fires on CTO word with the same
discipline (commit -> deploy -> verify -> census 189/175/10/0 pre-stated -> lock release -> redispatch).

**THE FORK-HEAL EXECUTED (02:18-02:20Z, CTO GO 021535Z riders 1-5 ALL SATISFIED):** promotion source
byte-tied to the RUNNING Lambda artifact (md5 c6bcb30e == infra repo == the exercised bytes; CodeSha256
1hNkq/apHg cited); promoted to repo canonical @ 57538722f; 3 old copies banked
(backup/pre_pullheal_20260716T0218Z/); deployed byte-identical x3 (gold + manual_api + bronze-runner) and
download-verified TIE each; census oracle PRE-STATED 189/175/10/0, READ 189/175/10/0 — PASS. **PER RIDER 4:
THE REDISPATCH IS THE SAME CO-SIGNED FINISHING RUN — AMEND-57 numbers UNCHANGED (the abort was 40+ scripts
before C_01; the fold basis and the true-baseline ledger are untouched); AMEND-58's word covers mode=full
reaching the stamp on those numbers.** Bronze revival recorded as the window's own deliverable landing early,
THROUGH the authorized run (inside co-signed mode=full, not a back door).

**RUN 5 OUTCOME (01:44Z dispatch, mode=full): ABORTED AT INF_A_0 — TWO GUARDS RIGHT, ONE FORK HOLE.
NOTHING STAMPED, NOTHING SERVED.** The pull phase ran healthy — **THE BRONZE FEED IS REVIVED (txn/perf/
positions current for the first time since 07-10; the rescued txn converter ran; the ceiling self-healed)**
— but the runner's pull copy (05-12 vintage, repo-same) lacks change-3's roster half (_emit_roster lives
ONLY in the Lambda fork), so the converter's join hit its documented silent fall-through and emitted a
columnless 07-16 accounts_v2; the round-8.2 re-pin honestly moved to those bytes; the resolver's firebreak
REFUSED them, verbatim: "accounts_v2 has NO advisor_of_record_raw column... Refusing to serve pre-fold
under an active switch." FIX PROPOSED (CTO gate pending 021429Z): promote the Lambda pull to repo canonical
+ byte-identical deploy to both flatten copies; rerun self-heals the 07-16 partition in-run. AMEND-57
numbers UNCHANGED; the true-baseline ledger untouched by the abort.

**STEP (4) IN FLIGHT: CO-READ COMPLETE, BOTH HALVES PASS** (CTO 014029Z; COO 014125Z/AMEND 58 — the
145-subset ruled IN-BAR by row-set identity both directions, 1,257/1,257). **MODE=FULL WORD GIVEN 014157Z.**
First dispatch 409'd on run-4's stale lock (that chain had provably exited — its 250,074B log shipped by its
own trap at 01:35:03); released explicitly by the mechanism's own form (delete, logged), re-dispatched
**01:44:00Z (cmd d738fc87, lock-full-f54c4581113f): FOLD -> LOCK -> STAMP -> SERVE, three legs excluded,
guard battery in-run.** Watch armed on stamp/serve/exit; the launcher's empty-log first-ship is a known
monitor artifact (the chain re-ships the same key on its real exit).

**STEPS (2)+(3) EXECUTED (01:33-01:39Z): RUN 4 = THE TRUE-BASELINE RUN — AND THE BAR IS MET, ALL TEN ARMS,
FIVE DELTAS TO THE CENT.** Resolver first_run authored the true baseline (874 events: peter 497 / patrick 158 /
joe 147 / noel 64 / iwm 8 — vs the poisoned seed's 628/141/83/0/21); resumption_verify.py: noel +8,401,521.22 ✓
joe +7,384,568.89 ✓ patrick +3,448,754.37 ✓ peter −18,744,660.92 ✓ iwm −490,183.56 ✓ conservation −0.00 ✓
changed_rows 1,257 ✓ (145 changed accounts ⊂ 164 movers; 19 movers carry no historical NNA rows) NAMED-KEYS-ONLY
1,257/1,257 ✓ phantom +0.00 ✓. VERDICT: BAR MET. Sent to the CTO+COO co-read 013952Z; mode=full on their word.

**STEP (1) EXECUTED on the word (01:28:40Z):** bank `s3://opal-data-inf/backup/aor_ledger_pre_reseed_20260716T012840Z/`
(2 event files / 17,838B — count+bytes TIED to live pre-delete — + the state cache); all three keys deleted;
ledger verified ABSENT (0 objects) = the design's legitimate-zero. **ROW-9 REVERT (from the script's own
output): one `aws s3 sync` back from the bank + one `cp` for the state cache — cited verbatim in the run log.**

**RESUMPTION SHAPE (window closes clean if Andrew's word is not tonight; resumes on his word):**
(i) HELD script: bank + empty the ledger (revert = ONE SYNC BACK from the script's own banked output —
the bank path prints at run time and is cited here as the row-9 revert artifact by construction) ->
(ii) CTO flip -> gold-a re-run (resolver seeds the true baseline via first_run; dims re-derive) ->
(iii) PRE-STAMP VERIFY must read the ARM-2 numbers EXACTLY -> (iv) CTO flip -> mode=full (stamp + serve;
exclusion in the live dispatch) -> (v) served-spine co-read (phantom GONE, Patrick's $52,604.80 home, noel
present, exclusion oracle: the three legs' listings unchanged) -> re-arm -> vintage disclosed to Andrew ->
ledger CLOSED. Nothing stamped, nothing served, all reverts banked meanwhile.

**RUN 3 (as planned pre-dispatch): THE WINDOW'S OWN STAGE A — rides the ORIGINAL AMEND-54 co-sign
byte-unchanged** (COO ack 002044Z; scope 194d3d674, split bar, reverts, exclusion oracle, in-session re-arm).
Pre-dispatch evidence, cited per COO's fold-in: DIGEST PIN resolved by computation (repo HEAD lib =
md5 b7a9e89fd4f5f10ed7c9d1d2fc30a4d5 AND sha256 b06f8a6724639a03… — ONE set of bytes; the FATAL cited
sha256, the census cited md5/ETag, same file); (1) the cp executed 00:21Z, both keys ETag b7a9e89f/20,149B;
(2) census oracle PRE-STATED 189/175/10/0, READ 189/175/10/0 EXACTLY — step zero provably clear;
run-2's dead lock (lock-gold-a-9e70319ac26a) verified-held then RELEASED EXPLICITLY by the mechanism's own
form (delete of gold/dispatch-lock.json — trigger :118/:508, dispatch :182), confirmed ABSENT. Debt filed
by CTO (comp-learns-backlog): the vacuous on-runner .013 gate + dead-code check_freshness — post-window.

## REVERT ROWS ADDED (7-8)

| 7 | dispatch pre-exclusion bytes | `s3://opal-data-inf/backup/pre_exclusion_dispatch_20260715T2335Z/orion-gold-dispatch.sh` (ETag 3aef4ae7… == the bytes deployed before tonight's exclusion+hotfix deploy; one cp back restores) | banked + ETag-verified vs pre-deploy live |
| 8 | run-1 forensic artifacts | watchdog log + last-gold stamp read live (quoted in the ledger above); boot log + watchdog diag already in S3 | n/a (evidence, not a revert) |

## RUN SCOPE — GATE-OWNER RULING (1.0.0_SA_CTO, 23:2xZ, PRE-FLIP per COO 232148Z; adopts COO path (b))

**Tonight's run is CHAIN-WIDE with the THREE pre-round-8 serve legs HELD this window** (CVO~B evidence
232031Z: `INF_D_02c.client_directory` / `INF_D_04.client_portal_summary` / `INF_09.generate_partner_analytics`
deployed at pre-consumer-migration vintages, md5 vintage-tied, ABSENT from the G3 bundle manifest, dispatch-
invoked `--upload` at orion-gold-dispatch.sh:268,270,271). Under fold-ON those three would move served output
on PRE-CANONICAL attribution logic — outside the never-widen signature. Ruling terms:

1. **STAGE A: unaffected** — mode=gold-a carries no D-group leg; nothing serves. The sentinel flip proceeds.
2. **STAGE-B PRECONDITION (named, blocking):** before mode=full dispatches, ~B GROUNDS AT SOURCE the mechanism
   that keeps the three legs from moving served output this window — first candidate: the repo-HEAD
   `DEPLOY-SERVE-HELD` sentinel (does it gate the upload at runtime, cited file:line @ commit?). If it
   hard-refuses serve: deploy the three at HEAD (round-8 bytes, self-held) = the exclusion AND the vintage fix
   in one motion, B1-authorized. If it is inert prose: ~B proposes the exclusion mechanism and CTO gates it.
   NO ungrounded mechanism dispatches stage B (Rule 22).
3. **POST-RUN VERIFY (the exclusion's oracle):** the three served surfaces' listing (key+ETag+LastModified)
   UNCHANGED across the window — a listing read, not a self-report. Recorded here before close.
4. **The three consumers' serve-lift** = a LATER deliberate bundle at migrated vintages (COO path (b) verbatim:
   "migrated vintages ride a later bundle"), NOT part of this window.
5. COO's co-sign covers this scope as given (232148Z path (b)); CVO~B's item is thereby SEQUENCED-NOT-BLOCKING
   for stage A and CONSUMED as the stage-B precondition above.
