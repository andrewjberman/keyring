# ADVI_BDPARITY.T1-ORACLE -- build + measure under the lifted fence (2115-2210Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, TRACE

**Serial:** `0.4.0_DS_ClientPlatform~B` | **Window:** session start ~2115Z -> 2210Z (first log of session)
**Commits:** `b8b80ad48f` (oracle + report + proof), `c8165c3659` (vintage stamp). Unpushed -- lanes commit, integrators push.

---

## Summary

Startup (watcher armed task `b38q033em`, registered PID 34156, session-serial file stamped, 13 active
TOs read via `to-check --all`), then built and measured ADVI_BDPARITY.T1-ORACLE end to end. The fence
lifted on Andrew's ~2012Z group-based book ruling; I built the oracle, measured every leg I am
authorized to measure, printed the Travis-class delta as the expected headline, and left serving
untouched.

The shape of the session was set by one constraint found early: **the oracle's authority leg (a live
qt6 read) is vendor egress I do not hold.** Rather than treat that as a blocker, I found the landed
no-egress substitute (`comp-find --name '*bd49f*'` surfaced the live daily pull vehicle), measured
both remaining legs across all 201 groups, and exercised the authority leg against CRO~A's published
value carried explicitly as RELAYED. The residual is an authorization residual, not a build gap.

## What was built

`data/assets/scripts/gold/runners_49f/oracle_book_tieout_qt6.py` -- a three-leg group-grain tie-out
(L1 BD-native qt6 EMV / L2 landed `allocation_390224` membership / L3 our gold `canonical_valuation`),
legs chosen to differ in DERIVATION. Deliberately NOT a chain stage: `chain_49f_entrypoint.py:_stage_list`
is an explicit hardcoded list carrying 0 references to it. Structurally incapable of a vendor call --
no `boto3`, no `urllib`/`requests` -- so L1 is an input file, never an action. Basis stamped into every
artifact and printed at the head of every run. Cross-group totals structurally refused.

## Measured (as_of 2026-08-18, denominators printed)

30,577 export rows -> 29,907 after collapse; 201 groups; 6,155 distinct accounts; 5,579 (90.6%) in 2+
groups; our canonical 7,315 accounts.

Travis Penfield (318 members): BOOK group-based **$392,556,451.10** / OURS V(t) **$377,433,506.75**
(284 matched, 34 unmatched) / BD-native qt6 EMV **$456.8M RELAYED** -> headline **$79,366,493.25
(+21.03%)** = MEMBERSHIP $64.2M + COVERAGE $25.3M + VALUATION -$10.1M.

### Findings

1. **The -$10.1M "valuation gap" is mostly a MEASURE MISMATCH.** The export's `Account Market Value`
   is positions grain: ties our `net_mv_positions` at -0.163% vs -2.683% against `net_mv_plus_cash`;
   adding the export's separate `Cash Market Value` makes the fit WORSE (+1.160%). NOT closed --
   per-account identity fails (2 of 284 to the cent), so this is a named candidate mechanism on
   aggregate evidence, not a root cause.
2. **CRO's $405.4M reproduces byte-for-byte as the RAW ROW SUM and double-counts $12.8M** across 9
   accounts sitting under 2+ portfolios in one group (estate-wide 573 such keys / 670 extra rows).
   Correct membership figure $392,556,451.10. CRO's decomposition is undisturbed (built on BD's own
   member list). Two other CRO figures re-derived EXACTLY: the 201/6,155/90.6% census and the
   role-tagged union $348,726,019.90 / 241 accounts.
3. **`Primary Portfolio Group` (dim 436) is not in the landed export** -- template 390224 selects only
   2 Portfolio-Group dims. Today's L2 is MEMBERSHIP, not the primary-group PARTITION the ruled basis
   names, so `bridge_group_account.is_primary` cannot be built from it. Routed as a T2-DIMS input.
4. **`Portfolio Group Market Value` (col 89) is a trap** -- constant per portfolio (2,842 of 2,875),
   varies within 179 of 201 groups; it is the denominator of `Account Allocation`. Deliberately unused.

## Controls (run, not asserted)

- **M1 (zfill(10) join removed): FIRED** -- L3 collapsed 284 -> 0 matched, $377.4M -> $0.00.
- **M2 (dedup bypassed): DID NOT FIRE** -- 0 of 201 group book figures moved, |delta| $0.00. The
  collapse is enforced by `build_membership`'s dict keying, not the dedup call. Docstring corrected to
  credit the enforcing mechanism. Reported rather than buried: a rule credited to the wrong mechanism
  is how the load-bearing one gets deleted later as redundant while the decorative one is kept.
- **Determinism: STABLE** -- identical sha256 `aaad066a...98135` over two runs.
- **T1-3 as a checked condition, 4 independent probes:** 0 stage refs / `comp-find` 1 hit across 26,980
  files and that hit is the tool's own docstring / no network or S3 client in the file /
  `platinum/advi/49financial/` 0 keys.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` (content) | `comp-find "qt6"` | PASS -- 141 hits / 26,964 files, bands HEAD=13 SURFACED=46 CONFIG=3 DOC=79. Located the BD datamining payload set + fee-probe trace documenting the template->run->export flow. |
| `comp-find` (`--name`) | `comp-find --name "*bd49f*"` | PASS -- **the load-bearing call of the session.** 17 hits; surfaced `opal-assets-bd49f-daily-pull`, the live authorized vehicle already landing the group->account map. Without it the L2 leg reads unavailable and the oracle has no measurable half. |
| `comp-find` (content) | `comp-find "oracle_book_tieout"` | PASS -- 1 hit / 26,980 files, and that hit is the tool's own docstring. This printed denominator IS the T1-3(b) no-consumer verdict. |
| `comp-which` | `comp-which "how do I grep the repo"` | PASS -- forwarder RAN (banner produced), XXX.md A.3 exercise half. PATH 97 of 97 bare. |
| `.tools/commit-gate.sh` | on the new script | PASS -- "pre-commit gate clean for 1 file(s)". |
| `.tools/proof-of-spec-check.py` | instance + `T1-1,T1-2,T1-3,T1-4` | PASS after fix -- first run INVALID with 17 real structural violations, all fixed; final VALID rc=0, coverage 4/4. |

**What worked:** `comp-find --name` turned a would-be blocker into a measurable leg -- the estate
already had the pull vehicle (BUILD LADDER rung 2, and I did not build a second one). Its printed
denominators did real evidentiary work twice: the 1-hit/26,980-files frame is what makes T1-3(b) a
verdict rather than an anecdote.

**What failed:** nothing tool-side. `aws s3 cp` with a `/cygdrive/c/...` destination silently wrote to
a stray relative `C:\cygdrive\...` tree while reporting success -- cost one round trip; native `C:/...`
destinations work.

**Gap found:** the proof-of-spec artifact-coverage heuristic keys on the
`{firm}-{group}-{artifact}-{check}` id grammar, but a TO that fixes its criterion ids (here T1-1..T1-4)
makes the stem tokens structurally unable to appear -- so a fully-battery-covered artifact must be
declared as an exclusion to pass. Declared with the reason; a gate candidate at most, not chased.

## Files Modified

See commit messages: `b8b80ad48f`, `c8165c3659`.

## MCP traffic

5 total. Received: AE_CloudOps GRANT-LIVE (platinum/advi/49financial Put granted + sim-proven;
publisher schedule shell awaits my invocation contract -- P4-EMIT row, held pending COO sequencing).
Sent: COO ACK at start; COO delivery report; CRO~A (the $405.4M correction + the qt6 re-run ask under
their standing grant); CTO (Q3 gate-owner FYI, no GO requested).

## Blockers

**None.** The live qt6 run is NOT a blocker and is not recorded as one: it is an authorization
residual, evidence-cited (standing lifts cover cot-BD explicitly not bd/49f; the 49f grant is
Andrew-direct and continuing at `4.0.0_SA_CRO~A`, who read OFFLINE ~10min at my check). Template
517678 is already persisted in BD, so it is a re-run, not a build.

## Current State

- Oracle lives at `data/assets/scripts/gold/runners_49f/oracle_book_tieout_qt6.py` @`b8b80ad48f`.
  Run it as: `python oracle_book_tieout_qt6.py --as-of <D> --alloc-export <allocation_390224 data.xlsx>
  --canonical-valuation <canonical_valuation data.parquet> [--qt6 <group EMV json/csv>] [--group <name>]`.
- Inputs, both landed and current: `s3://opal-data-assets/blackdiamond/49f/bronze/allocation_390224/2026-08-18/data.xlsx`
  (as_of 08-18 pulled 08-19T02:30:33Z = correct T-1) and
  `s3://opal-data-49financial/gold/advi/canonical/canonical_valuation/date=2026-08-18/data.parquet`.
- Deliverable `org/tier2_senior/0.4.0_DS_ClientPlatform~B/deliverables/ADVI_BDPARITY_T1_ORACLE_BOOK_TIEOUT_20260819.md`;
  proof `.../ADVI_BDPARITY.T1-ORACLE_PROOF_OF_SPEC.json` VALID rc=0 @`c8165c3659`.
- Serving untouched: `s3://opal-data-portal-v2/platinum/advi/49financial/` remains 0 keys.
- Other three TOs held, not started: T2-DIMS (gates ADVI_IDSPINE.WP-1 at DS base, plus finding 3),
  D3.3 (gates TO-D3.2 + D2 publisher active), WP-5 (P4-class, behind T1-ORACLE).

## Next Steps

1. [`4.0.0_SA_CRO~A`] One qt6 group-grain EMV re-run at as_of 2026-08-18 under the standing grant
   (template 517678, already persisted, 636 rows) -> hand over as `{group: emv}` JSON/CSV. Completes
   T1-1's authority leg across all 201 groups. Also: confirm or correct my $405.4M finding.
2. [`2.0.0_SA_COO`] Sequencing call -- cut the publisher invocation contract for AE tonight (their
   GRANT-LIVE is waiting on my word), or hold it behind WP-5.
3. [`1.0.0_SA_CTO`] No action requested. The dim-436 partition-key gap is a served-semantics
   precondition to be aware of before any book figure is served.
4. [`0.4.0_DS_ClientPlatform~B`] On the qt6 file landing: re-run the oracle with `--qt6`, and the
   201-group L1 tie-out completes without further build.

## Surprise channel (no action taken)

- `aws s3 cp` with a `/cygdrive/c/...` DESTINATION silently writes to a relative `C:\cygdrive\...`
  tree while reporting success. Pre-existing, estate-wide -- that tree holds scratch from at least 6
  other sessions. Nothing deleted. Use native `C:/...` destinations.
- `opal-data-bd/silver/allocations/` last partition 2026-08-14 on what reads as a weekly Friday
  cadence (07-31 / 08-07 / 08-14) -- healthy on that reading, flagged ONLY because CRO's scan
  describes that map as landing daily. **No outage claimed.** The feed this oracle uses is daily and
  current at T-1.
