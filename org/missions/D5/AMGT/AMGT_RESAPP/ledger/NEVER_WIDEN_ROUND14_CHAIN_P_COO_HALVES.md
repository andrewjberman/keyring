# NEVER-WIDEN CO-SIGN -- COO HALVES. Round 14, chain P (peers). One section per co-signed cell.

**Signer:** `2.0.0_SA_COO~Z`, at the L6 cut, BEFORE any spawn. **Counterpart:** `1.0.0_SA_CTO~Z`'s CTO halves at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_P_CTO_HALVES.md` (DESIRED plane). **This plane:**
APPLIED and EXERCISED. Neither half stands alone; each worker reads BOTH before its first live act and STOPS with a
BLOCKING row if either is absent or lacks its cell's section. `rk-50` (R14-P1) writes only the three validation names'
raw bytes and R-1 pool objects -- keys no served route resolves until `rk-31` lands -- and its census marks it NOT
co-signed; the issuer leaves that as drafted (pool writes on unserved keys are covered by its own change-management
entry) and notes that the moment `rk-31`'s crosswalk lands, `peers/v1/<key>/<as_of>.json` for the three becomes served
through the adapter's whole-object read (`read_peer_set`, `scoped_amgt.py:1244-1278`); that reachability is the reason
`rk-51`, which writes `scores/v1` for the same three keys, IS co-signed.

**Home, settled by Andrew ~21:1xZ (relayed by `1.0.0_SA_CTO~Z`, msg 23778):** `opal-data-harvest` is THE designated home for ALL
AMGT_RESAPP data content and pipelines, bronze included, structured to the canon (an R20 departure from R4 that `0.0.0_AB_MSTR~Z`
is registering as two rows). No `amgt` scope row (Andrew declined it, msg 23774). So every bronze raw address in this chain is
`lib/opal_naming.py address()` output whose bucket MUST read `opal-data-harvest` -- and until the two rows land the builder still
prints the shared `opal-data-assets`, in which case the live arm is DEAD: nothing is written, the criterion records the builder's
line as REFUSED-BY-REGISTRY, one row carries it (the REGISTRY GATE amendment in `rk-50` and `rk-51`). A write of any AMGT_RESAPP
object to `opal-data-assets` is covered by NO half. Pool objects stay at their `opal-data-harvest` prefixes, where every reader keys.

## `AMGT-rk-51` -- peers V from SA with floors; scores for the three validation names (R14-P2; FWD-8, S162 (1), C-PEERS-V-FLOORS)

**THE ACT.** ONE Bloomberg refdata pull for the V fields on the three keys, landed raw at
the builder's address for `bloomberg` / `harvest` / `bronze` / `peers-v-fields` / `<key>` (scope token `harvest`, CTO L4 ruling @2560e04f46), whose bucket MUST print `opal-data-harvest` (registry-gated), then
`run_scores --security-key <K>` writing `s3://opal-data-harvest/scores/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<as_of>.json` --
three NEW dated keys. THE KEY FILTER IS A SOURCE CHANGE THIS CELL MAKES (order step 3b, on CTO msg 23830): at HEAD
`run_scores.run()` (`:216-238`) iterates EVERY keyed name of the newest crosswalk (33 now, 36 once `rk-31` lands) and
`main()` takes only `--as-of`/`--dry-run`; the cell adds `security_keys` + a repeatable `--security-key`, and a bare run
REFUSES unless `--all-keyed` (never passed by this order). Until that change is built and its unit test passes, no live
run is authorized by this half.

**BLAST RADIUS.** 3 raw bronze stamps + 3 NEW `scores/v1` dated keys. The 33 covered names' `scores/v1` objects are NOT
rewritten (AC5's discriminator: `rerun_of_covered_today 0 of 33` -- NO covered name gains a today-dated key; the ETag of an old
newest object is NOT the discriminator, because the reader takes the NEWEST dated key and the served value would move
without a deploy -- CTO msg 23830). Served: the scores
route serves a key the crosswalk carries -- the three are served the moment `rk-31`'s crosswalk lands; the 33 do not
move. NO Lambda, NO Terraform, NO IAM, NO schedule.

**WRITER CENSUS of `scores/v1/<key>/<as_of>`: N = 1 writer** -- `lib/research/scores/run_scores.py` (dated key per run;
the round-13 scores producer, whose IAM prefix grant was the round-13 pair `NEVER_WIDEN_ROUND13_SCORES_PREFIX_GRANT_*`).
No schedule writes it (`comp-schedule` at the cut: 0 on `scores`). Rule read: a run writes `<as_of>` for the keys it
is handed and no other key.

**EXPECTED OUTCOME, both branches (read from `peers_v.py`'s rule with the floors as the order inlines them).** A name
whose SA peer set (`rk-50`'s R-1 object) carries >= the floor of members with the V fields present: `peers_v` served
with the floor-satisfied flag and the member count as denominator. A name below the floor, or whose R-1 object is
ABSENT (`rk-50` refused on it): `peers_v ABSENT` with `absent_reason` naming the floor or the missing object -- and the
order fixes the `peers_v.py:270-277` `absent_reason` defect the drafter measured, so the reason is a real string, never
None. Either branch: 3 dated keys land (an ABSENT score object is still an object); the 33 untouched.

**PER-KEY ROLLBACK.** Pre-act: `head_object` on the 3 `scores/v1` keys for `<as_of>` (expected 404) and `list_objects_v2`
on the 3 bronze prefixes, recorded in the entry; plus the ETag list of the 33 covered names' newest scores objects
(AC5's baseline). Rollback = delete the 3 new dated keys and the 3 new bronze stamps. Nothing is restored.

**NOT COVERED:** any `scores/v1` write on a covered name; a run over the 33; a fourth name; an `amgt` scope row.

## `AMGT-rk-52` -- the peers page serves the SA-shaped object (R14-P3; FWD-8) -- co-signed AT PROMOTE, not at build

**THE ACT this round: NONE on the served plane.** The worker builds `PeersTab.tsx`, `cscTable.ts`, `types.ts` and the
harness fixture (one S3 GET of `peers/v1/CAT_US_Equity/<newest>.json` to build the fixture -- a read) on its portal
branch; `./node_modules/.bin/tsc -b` and the harness prove it; the page is graded by a JUDGMENT criterion at L9. No
deploy, no promote, no gitlink bump (LD-0367/0368: the integrator pushes the shared portal branch; PROD promote HELD).

**BLAST RADIUS this round: nothing served moves.** This section exists so that the PROMOTE, when Andrew lifts the hold,
is already scoped: the blast radius of that later act is the portal DEV/PROD build (every page in the bundle), its
rollback the previous build's commit on the shared branch, its writer census N = 1 (the integrator's push). That act
gets its OWN pair at the time; this half covers no promote and authorizes none.

**NOT COVERED:** a portal push; a promote; a headless authenticated session (MFA blocks it as a class -- the page cell
tests the adapter directly and carries a JUDGMENT criterion, card 6).

Signed `2.0.0_SA_COO~Z`, 2026-09-18, at the round-14 cut.
