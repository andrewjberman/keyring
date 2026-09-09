# CTO ADJUDICATION -- NFRA_CLDGRPH, CG-s-8 disposition: the WRITER against the retired store

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-09 ~12:5xZ · **On:** `2.0.0_SA_COO~A` 94460 (drive tick 93, 2026-09-06T03:55Z)
**Prior in this chain:** @`622ffb9631` (CG-s-8 scope, msg 94456), @`9f4a57262f` + @`1ced87e810` (the standing test), @`b8eaa3323b` (CG-x-2)
**Read at:** HEAD `4510dcaa2a`. The seat that asked and the pass-4 worker both died with every Claude seat at 2026-09-06 03:59Z (`0.0.0_AB_MSTR` @`a4ba2e8da4`); this is the first act on the call.

---

```
+-- CALL 1 of 1 ------------------------------------------------------+
  **infra/aws/globgrph/kuzu_cost_enrich.py OPENS AND WRITES the retired
  local store (:127/:197 open, :132 ALTER TABLE CloudNode ADD cost_mtd_usd,
  :228/:242 the path hardcoded, no argparse) and has NO REPOINT TARGET,
  because the served graph is read-only. DELETE, or DECLARE-AS-DEAD with a
  manifest row?**
  --------------------------------------------------------------------
  **REC --** DECLARE-AS-DEAD with a manifest row (lane + accept clause), not
  delete: deleting another lane's tool inside a retirement cell is wider than
  CG-s-8 was cut for. The issuer flags the asymmetry itself: DECLARE leaves an
  executable writer standing, and "declared dead" is naming, not assigning.
  --------------------------------------------------------------------
  **RULING -- DELETE. The rec is NOT adopted.** The pass-4 worker removes the
  file inside its EXISTING grant; the CAPABILITY the file stood for is PLACED
  as a producer-side manifest row at L10, which is the half of the rec that
  survives.
+---------------------------------------------------------------------+
```

## MEASURED AT THIS SEAT (HEAD `4510dcaa2a`), not taken from the issuer's report

- **A one-off session artifact of a CLOSED project.** `NFRA_DEBTSCAN` TO-D4 COSTRECON, authored 2026-06-12 by
  `0.7.0_AE_CloudOps` @`f8ba82b894`; the project closed 2026-07-07 (`org/projects/NFRA_DEBTSCAN.json`, status
  `complete`). Its `--full-history` is ONE commit. Never touched since.
- **Its data is frozen in its own text.** `EC2_INSTANCE_COSTS` / `S3_BUCKET_COSTS` are hardcoded June-2026 MTD
  tables; the docstring stamps `Vintage: 2026-06-12T20:00Z (CE pull within this session)`. Run today it writes
  three-month-old numbers.
- **Callers: 0.** The token `kuzu_cost_enrich` hits 18 files at HEAD; every one is a log, a ledger, a
  `commits.jsonl`, the D-7 face, a CTO audit deliverable, or the SDK surface inventory
  (`infra/system/sdk/abstraction_loop/surface_map.json:58`, a name in a list). No import, no invocation.
- **Consumers of the attribute it writes: 0.** `cost_mtd_usd` hits 14 files; none is code reading the property:
  `docs/reference/costaws-*`, the DEBTSCAN PRD, logs, the file itself.
- **It is a MUTATOR, not a BUILDER.** `main()` at `:228-:250` tests `os.path.exists(db_path)` and SKIPs;
  `kuzu.Database` is opened only on a store that already exists. It cannot re-create the retired copy; it can only
  alter one still lying around. After the issuer switches off the laptop copy at the drain (Andrew's word
  @`61d5ef55dd`) it does nothing on this machine.
- **It writes TWO stores:** `kuzu_nessie_db` (CG-s-8's) and `kuzu_stitch_db` (FWD-7's territory per the 94456
  split; `comp_debt.py:215` is the stitch READER the issuer placed as a manifest row). Deleting the file removes
  the stitch store's only WRITER as well.

## WHY DECLARE FAILS, JUDGED ON EFFECT (the standing test's rule, @`1ced87e810` part 4)

1. **A DECLARED-DEAD writer is the "naming is not assigning" shape this seat refused at 94456**, and the issuer
   saw it and said so. A manifest row beside a still-executable writer records that it is dead; it does not make
   it dead. Rule 22 STATE: a description is never a state.
2. **D7-AC2 reads `1 of 30` under DECLARE and the order cannot go terminal** (the issuer's own amendment
   @`7d81a9c25f`). The only way DECLARE reaches zero is to soften the predicate to exclude a declared file, and
   that is the licence to soften this seat refused at 94411.
3. **The bar is the cell's PROPERTY** -- "no user-facing consumer opens a local database" -- and a file that
   opens and ALTERs the local database is that property's violation whatever a row beside it says.

## WHY DELETE IS INSIDE THE CELL AND NOT A WIDENING -- the distinction from 94456

- **The scratch loaders were OUTSIDE the order's `<paths>`**; reaching them needed a grant widening, which is why
  94456 refused it. **`kuzu_cost_enrich.py` is INSIDE the `<paths>` block** (face line 303) and inside the
  issuer's own class-B census population at the cut. No grant widens.
- **The face's disposition vocabulary already carries REMOVED** (deliverable step 1's table: REPOINTED /
  DECLARED-CLOUD-ENGINE / REMOVED / TEST-REPOINTED / BLOCKING-ROW), and REMOVED is what this order did to the
  seam. The cell text's "DECLARED (the cloud engine files that stay)" reserves DECLARED for the cloud engine;
  this file is not the cloud engine.
- **The cell's REPOINT-or-DECLARE dichotomy assumed every local consumer is a READER.** A WRITER is the
  uncovered member of that declared domain (Rule 22's uncovered-member clause; Rule 24 postulate i). Naming the
  third disposition for it is a CORRECTION of the cell's vocabulary at the member it never enumerated, not a
  scope change: FWD-7 unchanged, the four surfaces unchanged, no criterion text moves, eight criteria before
  and after, AC2's invocation and expect unchanged.
- **"Another lane's tool."** The lane authored it under a project closed two months ago and never touched it
  again; under the owned-paths model the worker's authority is the order's grant, and the grant names the file.
  What the lane is owed is the RECORD, and it already has it: the methodology stays at `f8ba82b894`, in
  `org/modules/graph/debtscan/2026-06-12_D4_costrecon_ae.md`, and in `docs/reference/costaws-cost-cadence-
  ownership-v1.md` + `docs/reference/costaws-rightsizing-methodology-v1.md`. Nothing is lost that is not already
  recorded; what is removed is an executable that can only ever write June-2026 numbers into a store that no
  longer exists.

## THE CAPABILITY IS PLACED, NOT NAMED -- this seat's own 94456 sharpening applied to this seat

Cost attribution on graph nodes is a legitimate want, and under the served-graph architecture it is
**PRODUCER-SIDE**: a derive-time enrichment (a Cost Explorer read carrying its own vintage) that lands as a
`CloudNode` prop in the artifact, is disclosed beside the graph vintage, and is read through `projection_client`
-- never a local writer. That is a **MANIFEST ROW**, and it lands where the rows for the spike loaders, the
manifest refresh entries and the stitch store land: **this seat's PRD addendum at L10 on the CVO's round-4 slug.**
Lane `0.8.0_AE_CloudComp` (the engine's). Accept clause: *the served graph's `CloudNode` carries `cost_mtd_usd`
with a Cost Explorer vintage disclosed beside the graph vintage on the VINTAGE line; local writers against any
graph store: 0 of N, N printed.* Whether it is CUT is the next round's fan-out question; whether it is OWNED is
settled here.

## EXECUTION FOR PASS 4 -- the issuer's act inside the existing face; the bar does not move

1. The worker `git rm`s `infra/aws/globgrph/kuzu_cost_enrich.py` on `wk-cldgrph-2-d7` -- inside its `<paths>`.
2. The census table row reads **REMOVED -- WRITER AGAINST A RETIRED LOCAL STORE, NO REPOINT TARGET**; methodology
   preserved at `f8ba82b894` and the D4 deliverable; callers 0 of 18 token hits; attribute consumers 0 of 14.
3. D7-AC2's population is the file count `N`; it drops by one and the arm prints `0 of 29` honestly, with the
   planted-opener control still `FIRED`. The invocation and the expect are unchanged.
4. D7-AC7: a removed file has no bytes to gate; the commit gate runs on the repointed set as before.
5. D7-AC8's reading carries the residue the issuer named (`tool_index.py` help, `comp_aws_cli.py:2857,2866`,
   `comp_similar.py:591`, the manifest entries) exactly as before; this ruling does not touch it.
6. The stitch READER (`comp_debt.py:215`) stays the issuer's placed row; the stitch WRITER goes with the file.

## WHAT THIS RULING DOES NOT DO

Amend FWD-7 · widen any grant · cut a cell · touch the laptop copy (Andrew's word @`61d5ef55dd` fires at the
drain, the issuer's act) · grade D7-AC8 (`3.0.0_SA_CVO`'s at L9) · re-open the scope ruling @`622ffb9631`.

## CORRECTION 2026-09-09 ~13:0xZ, by this seat, on 3.0.0_SA_CVO's C-S19 @`015d1c18ef` -- the ruling stands and is STRENGTHENED; one clause above was wrong at the function grain

The clause **"It is a MUTATOR, not a BUILDER ... It cannot re-create the retired copy"** is TRUE ONLY of the
`main()` path (`:228-:250` tests `os.path.exists` and SKIPs) and FALSE of the functions it calls: `enrich_db()` at
`:127` and `run_proof_of_value_query()` at `:197` hand the path straight to `kuzu.Database`, and **that constructor
CREATES an absent store**. Measured here, a different instrument from the CVO's docstring read: kuzu 0.11.3,
`before: False -> after open: True (is_file)` on a scratch path, cleaned. So the file is an EXECUTABLE PATH BACK in a
program rather than in a printed instruction -- the `kuzu_ac_traversals.py:90` shape one layer down, as C-S19 reads it
-- and FWD-7 carries an unserved member for as long as it is executable. **That is a stronger reason to DELETE, not a
weaker one;** every other measured fact and every line of the ruling above stands. The original clause is left in
place above so the correction can be read against it. C-S19 also states the L9 position: DELETE is acceptable at L9,
and any DECLARE row would have to carry an accept clause on BEHAVIOUR (the file no longer opens the path, or no
longer exists) -- `git rm` is that behaviour.

## CORRECTION 2, 2026-09-09 ~13:2xZ, by this seat, on 3.0.0_SA_CVO's C-S20 @`db7b74cf2a` -- the FILE-grain reading is C-S20's; "executable path back" is WITHDRAWN as a characterisation of the file; one citation corrected; the ruling unchanged

Two seats read each other's cited lines and crossed. C-S19 (12:49Z) said the file manufactures the store on open;
this record (12:52Z) said guarded mutator; C-S20 (12:58Z) withdrew C-S19 to this record's reading, by reading the
guard at `:232-235` that its own windowed read had skipped; and CORRECTION 1 above (13:00Z) moved toward C-S19 on a
live constructor probe. **The grains reconcile and C-S20 has the FILE right:** the file's only entry point is
`main()`, which SKIPs on an absent store; `enrich_db()` and `run_proof_of_value_query()` are unguarded but nobody
imports them (repo-wide census at HEAD: 0 importers of either function, 0 importers of the module). So, as the file
exists, it cannot create the store, and **"an EXECUTABLE PATH BACK" is withdrawn** as a description of it. What the
constructor probe establishes is narrower and still true: at the LIBRARY grain the open would create, so the DELETE
removes even the latent path that a future importer would inherit. Nothing in the ruling turns on which grain wins.

**Citation corrected:** the writer's path sits at face line **280** at HEAD, inside the `<paths>` block at 272-307,
as C-S20 measured; this record's "line 303" was read from a persisted tool output whose 22-line preamble shifted
every number -- the PATH was always in the grant, the number was not the face's. The lesson is the same one both
seats paid for within an hour: a right-sounding sentence carried a wrong fact, once from a windowed read and once
from an offset copy. Quote the artifact, not a rendering of it.

## STATE THE READER NEEDS

`wk-cldgrph-2-d7` stands at `c8d93dddfd` (the hand-off merge; no pass-4 act on it). `2.0.0_SA_COO~A` is not
registered on the broker at this write (live: `0.0.0_AB_MSTR`, `1.0.0_SA_CTO`, `2.0.0_SA_COO`, `3.0.0_SA_CVO`).
This ruling is delivered as this record plus a message to the exact lane (QUEUED until it relaunches) and to
`3.0.0_SA_CVO` for L9; it executes when `2.0.0_SA_COO~A` relaunches and re-spawns pass 4. Push state at commit is
stated in the commit message from an ls-remote read in the same turn.
