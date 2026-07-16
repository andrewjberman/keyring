# A4 L4 executed: C_01/G4 port (carried-state) + trn_nna Layer-B moved gold-side + G->C map -- one window, parity to the cent

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, TRACE
**serial:** 0.4.0_DS_ClientPlatform~A | **window:** 2026-07-16 ~16:55Z -> ~18:15Z
**Session:** reinstantiation off the 164xZ handoff. /watcher: predecessor orphan pair
(2102683/2102634) identity-probed FIRST (broker LIVE was poller-manufactured -- PID 4680 =
agent-poller python, measured), then reaped; fresh Monitor bkv7372ie; LD-0290 serial file
written; partition watch re-armed unconditionally (date=2026-07-16, task bzz50ygw7). CTO's
three messages (WP7 gate-accepted / trn_nna ruling / L4-FIRST confirmed) read + acked 170454Z.

## L4 landed (commit 9c3d93bbf, pushed; lib deployed to S3)

1. **C_01.account_performance (G4 port)** -- pure core + runner, seed formulas verbatim;
   the plan's union-all caveat resolved as incremental-with-carried-state: data.parquet
   (window rows, absent-day-absent) + state.parquet (geometric-factor ledger, O(accounts);
   zero-BMV days link NEUTRAL + counted; dormancy carries without reset; reappearance links
   off the carried factor -- all fixture-proven). Runner REFUSES on continuity gap
   (latest prior partition != gains prev_date), c03-pattern gates + write-verify + read-back.
   C_02's runner stops refusing on this prefix. Suite 72/72 incl. the C_02 seam end-to-end.
   First live run gates on C_00 first-live (CTO family-review word) -- stated, not pending-silent.
2. **trn_nna disposition (CTO 165108Z, Rule-17 gold-tier)** -- classifier + txn-key hash
   MOVED verbatim to lib/schwab_trn_nna_gold.py (byte-compatible; bronze converter = retiring
   predecessor; both-ends unit tie in the suite). lib/schwab_flows.py: source=monolith|legacy
   behind ONE shared tail; master purpose-resolved (model_portfolios->08242234, NO default);
   unknown source REFUSES. Column correspondence MEASURED before authoring (tran_srcde==
   tran_code 26/26, source-desc 23/23, detail-desc 482/482, acct ids 320/320 zero-stripped,
   gross sums to the cent on the same delivery).
   **PARITY PASS two tiers, WITHIN-MASTER (0824):** tier-1 on 3 real deliveries row-for-row
   (54/54, 481/481, 82/82; txn-key sets tie; gross to the cent; incl. a 9,219-row bulk day);
   tier-2 full seam 2026-07-01..07-15: 0/10 dates mismatched, window totals tie to the cent
   (in 16,379,368.66 / out 4,478,350.96 both paths), identical unmapped censuses.
   **Depth census, divergences NAMED:** 58 legacy-only partitions = ALL pre-feed-floor
   (<2024-07-08, Entry-1 residue, Andrew's desk); 12 monolith-only = deliveries the legacy
   OneDrive chain MISSED (11x 2026-01 + 2026-04-30) -- monolith path recovers them;
   0 post-floor monolith gaps.
   **IAM (Rule 22a, live primitives):** bd-exporter-ec2-role (bd-gold-runner instance profile)
   = implicitDeny on the exact monolith key; positive control (held bd key) allowed, run in
   ISOLATION; ListBucket on opal-data-assets implicitDeny. THEREFORE default stays 'legacy'
   (env SCHWAB_FLOW_SOURCE); the flip rides the IAM grant (0.7.0 vehicle + CTO gate) then an
   explicit audited flip. Deploy: both lib files uploaded from COMMITTED bytes (git show
   9c3d93bbf:) to s3://opal-data-bd/code/gold/lib/, listing-verified, MD5==ETag byte-exact
   (5655e194... / 1b0904d1...). Deployed-vintage check first: repo last-touch 7c030faee
   (05-12) == deployed 05-12 -- no drift smuggled.
3. **G->C casebook map draft** (deliverables/CASEBOOK_GC_MAP_DRAFT_20260716.md, fold-ready):
   G-numbers from the seed scripts' OWN headers; holdings = collapses-to-reads; price-matrix
   retirement class measured LEGACY-ONLY (comp-grep canonical_prices = 0/41 seed files,
   anchor acabb3553); union-all caveat resolution recorded; trn_nna disposition recorded.
4. **Profiling (the Andrew rust/polars cell):** C_01 core 2x7,000-account builds = 235ms /
   11MB peak; monolith derivation adds ~2s over 10 partitions at the loader (6.2s vs 4.2s
   legacy) -- nothing at 0833/0824 volumes needs rust/polars.

## WP8-DECOM cell 4 (CTO 164930Z, to the BASE serial -- the push halt-gate caught it; my
lane Monitor does not watch the base inbox, noted as a real seam): OWNED, blocked-on the D2
redirect target ruling. Nothing to run today. From this window's work: the bd-gold trn_nna
consumer reads opal-data-bd (post-7c030faee unification), NOT opal-data-schwab -- no census
gap to surface from this lane.

## Compiler Tools

comp-glob/comp-grep (lane census, seed price-matrix census 0/41 w/ denominator, trn_nna
consumer census 21 hits/7 files -- sole 49F consumer confirmed; cot copy = separate firm,
untouched) | comp-pipescript io C_01 = EMPTY manifest (dynamic keys; tool says manual review
required -- the 1,008-line full-source read IS that review, A1/B_00 precedent) | comp-which
rail: rail-checked markers on parquet schema/value reads + S3 listing censuses (the recurring
no-comp-tool-reads-parquet gap, again) | commit-gate 7/7 (1 ruff F401 fixed at source) |
aws iam simulate-principal-policy per Rule 22a (ONE resource per call, isolated positive
control). Gap re-noted: parquet schema/value reads remain the rail-checked class.

## Next (in lane)

L3: pct_priced spec lines (C_01/C_02, STATEMENT-price coverage, acabb3553 anchor) -> then
verification legs: C_01 seed-vs-port identity within-master on a real date (gates on C_00
first-live) + the 3+run first_seen continuity check. Tomorrow ~09:46Z TRIPLE: daily runs
(a00/a01/c03 --upload on date=2026-07-16) + WP7 clean-cycle 1 + (~B's) bd49f first-fire.
Casebook folds pending at CTO: Entry 5 + the G->C map. WP8 cell 4 waits on D2.
