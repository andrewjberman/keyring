# 2.0.0_SA_COO — SESSION LOG, 2026-08-24 19:26Z → 22:2xZ

**archetype:** COORDINATE

**Session:** spawned 19:26Z (fresh; serial NOT REGISTERED at probe, no orphan watcher, no peer — Monitor `btv7w2ppy`
armed on the `/cygdrive/c` prefix). **Zero crons** (XXX.md 1b-F COO row: `/drive` OFF; no live scoped authorization).
**Prior log:** `SESSION_CLOSE_1348Z.md` — this log does not repeat it.

---

## 1. ⛔ CURRENT STATE — the handoff for a fresh seat

**Three stage-3 decomps authored and landed; two certified; five round-1 TOs cut and seated; five Tier-2 lanes live and
executing.** Everything I authored is committed. The tree's ~190 other dirty paths are NOT mine (they pre-date this
session — the same disclosure my 13:48Z log made).

| project | `dep_stage` | where it stands | who holds it |
|---|---|---|---|
| **D1_CATVIEWS** | **EXECUTING** | decomp **v2** (28 cells) CERTIFIED @60d4e2f1b4; round-1 TOs cut; r1 cell DONE (`@a0643a35fc`), r4 resumed on a corrected basis, c1/c2 census delivered | `DS~F` (gold/registry) · `DE~C` (portal) |
| **ADVI_PERFRP** | **EXECUTING** | decomp (36 cells) CERTIFIED @62598c1bfb (no P1); three TOs cut + seated; all three lanes ran spec-at-pickup and two returned findings | `DS~G` · `DE~D` · `AE~G` |
| **ADVI_INSURE** | **DECOMP** | decomp (33 cells) landed @b23bbe1f6d, amended pre-cert on CTO's Q-i1/Q-i2 rulings; **CVO cert PENDING** | COO → CVO; seating STAGED (0.6.0 + DS first) |
| **ADVI_STITCH-A** | PRD | next decomp in the CTO dispatch order (PERFRP → INSURE → **STITCH-A**); PRD read, run S1–S12 read | COO |
| **ETFS_POSITIONING** | EXECUTING | round-2 is the **site-Z** chain (D4 placed SITEZ-until-done); laptop residue = AE TO-5 apply + round-1 close. Proof instances back-filled → first fully joined project | site Z / AE |

**Commits authored this session (11):** `6a4eded191` (CRO off-limits record) · `469a9e9868` (D1 v2 decomp) ·
`1ce9b2d6bc` (PERFRP decomp) · `2f35896ff7` (D1 round-1 TOs + EXECUTING) · `38dd5f8853`→`36ced6391d` (PERFRP TOs, cut
then seated) · `b23bbe1f6d` (INSURE decomp) · `898fdcb3bd` (DE AC1 amendment) · `6e0959e57d` + `a718eb0cd0` (ETFS
back-fill, two lanes, two audited overrides) · `ad503ce567` (PERFRP amendments) · `3837078c1c` (D1 amendments).
**All LOCAL on CLOUD, riding MSTR's integration window** — none is pushed by this seat.

---

## 2. What I delivered

**Three stage-3 decomps**, each with the stage-3 open declared on its face (surfaces · reduced-cohort disclosure ·
certifier + alternate · placement · Rule 24 records · certification state), invariant cells cut FIRST, s.11 rulings
inherited as a FIXED table checked both directions, and alignment denominators printed with `criteria: 0 =
NOT-YET-EVALUABLE` stated as its own state rather than omitted. Cell-id counts were controlled by `grep -o` against
the stated total BEFORE each commit — that control caught my own 20-of-28 shortfall on D1 v2 (the 14 carried cells
were referenced in prose, not declared) and is why CVO's extractor found 28/28 rather than a discrepancy.

**Five round-1 TOs**, one project per Tier-2 lane instance, each carrying `<decomp_ref>`, the certification state on
its face, criteria with `cell_refs` both directions, printed alignment denominators, a SPEC-AT-PICKUP oracle table,
and the scope guard. A mechanical control before commit: 0 unresolved `cell_refs`, criterion sets == `expected_criteria`.

**Three findings of my own, each fixed in the decomp rather than left for an executing seat:**
- **D1 — the GRAIN finding.** Andrew's Client L1 is a per-ACCOUNT fee predicate; the MDPF Client substrate is a
  (firm × date) RESIDUAL. A per-account predicate cannot partition a firm-level residual, so `c1..c3` exist. A
  renderer-only reading would have shipped a split with nothing to split.
- **PERFRP — the premise that does not exist.** The plan's `fact_account_return_daily` is a CONTRACT, not a table
  (live: 8 canonical tables, `twr_daily` = 9 columns), and the gains trio is excluded from the scheduled chain by
  determination, landing nowhere. A decomp cut against the plan's column names would have dispatched a projection
  over a table nobody builds. CTO confirmed; CVO re-derived independently.
- **INSURE — the spine key.** `dim_account_xref` carries NO relationship column and insurance accounts have no Schwab
  id, so s.11 #3's stated mechanism cannot join; the relationship comes from BD's own relationship surface.

---

## 3. ⛔ The pattern that defined this session: executing seats falsified premises faster than the document plane could

**Six premise corrections in three hours, five of them found by the seat that had to USE the spec.** This is the
strongest evidence I have seen that the pipeline's stage-4 spec-at-pickup rule is the load-bearing one.

| # | finding | who | what it saved |
|---|---|---|---|
| 1 | `comp-transform schema-check` has NO DOMAIN on `ModelPortfolios.tsx` (no `types.ts`; the check aborts before its own header) — a 0-MISSING that **could not have been anything else** | `DE~C` | AC1 scored met off a vacuous zero; replaced by a typecheck mutant on declared response types |
| 2 | r4's reconciliation universe was one dim partition, which structurally cannot see Andrew's own example | `DS~F` | a Custom set reconciled against a universe that excludes the model he named |
| 3 | **"Opal Conservative Growth" IS `opal_long_term_conservative` — PRIMARY, ruled 07-23** | `DS~F` (against their own prior report) | **$34,585,361.39 of Primary AUA moved to Custom on a client-facing view, on a label hunch, past an F5 guard keyed on `member_id` that would have raised nothing.** MY RULING was the vehicle — see §4 |
| 4 | **Inflection is NOT dark** — the `supervised` token zero was an artifact; `is_fee_earning` is live at account grain (911/911 accounts) | `DS~F` | a decomp state-axis value (`DARK`) that did not exist; 2 of 3 firms usable, not 1 |
| 5 | `PRF-inv-1`'s byte-identical-bundle oracle names an artifact the build does not emit (ONE chunk carries both protected tabs AND the `d-4` target) — **unsatisfiable, not strict** | `DE~D` | a false green at sign-off certifying an untested property; also two ratified requirements contradicting |
| 6 | the "11 twins" premise was stale in BOTH TOs — 12 ENTRIES / 15 TWINS / 10 LIVE, three grains the wording mixed | `AE~G` | **DS-AC13 would have PASSED A MECHANICAL CHECK WHILE BEING FALSE** |

**The class, and it is the one CVO named against their own bar:** *a cell can be perfectly aligned and still name an
artifact the world does not contain.* Alignment is a property of the DOCUMENT; oracle viability is a property of the
WORLD, and no join over ids can see it. CVO has added a seventh check to their bar for it. **Both instruments —
mine and theirs — were honest and both were blind in the same direction; the seat that built the thing was not.**

---

## 4. ⛔ My own defects this session

**(a) I RULED A REGISTRY PLACEMENT FROM A LABEL IN A REPORT.** On DS~F's (correct, measured) observation that two BD
rows are distinct, I ruled "register Opal Conservative Growth as Custom." It IS `opal_long_term_conservative`, ruled
by Andrew 07-23, and the crosswalk's own line says *"Key by id, never the label."* DS~F caught it at the keyboard
before writing a line; nothing was committed. **A ruling on a served number needs the id-level read AT THE RULING
SEAT, not only at the executing seat** — I had the lane's evidence and did not open the file that assigns identity.
Retracted to all three seats it reached, same turn.

**(b) TWO TOs I WROTE CARRIED A STALE DENOMINATOR AND AN UNRUNNABLE ORACLE** (findings 5 and 6 above). Both were
faithful transcriptions of my own decomp; the decomp was wrong. Corrected at the CELL, not just the criterion — on
DE~D's insistence, which is what stops the next round re-deriving it.

**(c) A TO PHRASING DEFECT THE NEW GATE CAUGHT.** ETFS TO-1's `<decomp_ref>` read *"cells d-1, d-2 (reads a-1..a-6;
constrained by a-7/a-8)"* — the reads-clause and the boundary clause **parse as declared cells**, so the checker
correctly refused: *"the TO claims a cell it never discharges."* The declared set is the DISCHARGED set. Also: the
id-space scan cannot tell a citation from a QUOTATION, so quoting the old phrasing re-triggered it.

**Pattern across all three: I was wrong in the DOCUMENT plane while being confident in it, and each was caught by
someone reading the ARTIFACT.**

---

## 5. Rulings issued (14) — the ones a successor must not re-litigate

Surprise routing (seats surface by MCP, CVO files — no registry widening) · D1 `category_views` emits PER-FIRM ONLY,
`global` absent-not-empty · `PRF-c-3` runs AFTER the c04 battery (a c04 abort must BLOCK a client-facing performance
projection; fail-closed costs one run) · `AC5` run-ahead granted to AE~G (read-only, no emission dependency) ·
`D1-h-v4` stays with a FIXTURE exercise (0 live firms; a render path with no test fails the first time it is real) ·
Option A on the consolidator collision (4th artifact type + per-type scope map; **B refused because it inverts the
ruled-exception register, C refused because it contradicts absent-not-empty**) · BD-plane Custom members go in a
registry-side table, NEVER the crosswalk (its `model_id` is the sole join key; a BD GUID there corrupts served
parity) · the 18 Satellite strategies HELD + DISCLOSED · Moderate Income disclosed WITH its reverted-mint history ·
plus the three retractions/amendments in §4.

**Routed above my line rather than assumed:** the `a4_expected` contract-shape edit (CTO) · the AGG project's
pipeline question (Andrew, via CTO~X) · the concurrency-cap repair as a D0 TO candidate (CTO routing) ·
OPAL_KIMIPIPELINE-S1's disarm (owner dark → held visible at this seat, not queued to a dead inbox).

---

## 6. Compiler Tools

| Tool | Result | Gap / lesson |
|---|---|---|
| `comp-find --name` / `-i` | located every PRD, project JSON, TO and portal surface this session | **The `-i` habit paid twice**: `comp-find -i 'fixed income' data/mdpf` = 0/60 was HONEST IN SCOPE and I read it as an estate absence — CVO's widened run found the model live on the BD/assets plane |
| `comp-find` (content) | per-firm `supervised` census: cot 125/114 · 49F 19/152 · inf 0/230 | ⛔ **THE inf ZERO WAS A TOKEN ARTIFACT.** My own L-4 limitation predicted it; DS~F's widened census discharged it. A measured zero in a named scope is honest; the INFERENCE from it was mine |
| `python .tools/proof-of-spec-check.py` | 3/3 ETFS instances VALID rc=0 with the join computed (TO-1: 23-cell id space, fwd-1 6/6, fwd-2 5/5, bwd 5/5) | **Found a real defect on its first real corpus** (§4c). Also: `to_ref` must be a BARE resolvable path — provenance inside it reads as a false citation |
| `mdpf_category_registry.py` self_test | 14 members / 9 view nodes / 14-of-14 resolve; Custom = 3, all `served=False`; SMA `strategy_id` set = {divz, pfoe, muni, tax} = his four verbatim | The registry IS its own population — the one denominator here that cannot be a sample |
| pyarrow one-partition schema reads | `twr_daily` 9 cols / `canonical_valuation` 20 cols / `dim_account_xref` 6,201 rows, 10 cols **no relationship column** | The INSURE spine-key finding came from a column list, not from prose |
| `aws s3 ls` (rail-checked, presence only) | gold/advi = 4 prefixes · canonical = 8 tables · silver = 20 (lots+txn 6/6) · blackdiamond = `49f/` + `cottonwood/` only | ⛔ Every one marked `# rail-checked` with its reason: a PREFIX ENUMERATION is not a freshness read and `comp-freshness` is per-artifact — the right tool for a different question |
| `comp-transform schema-check` | **NOT run by me** — DE~C ran it and found it has no domain on the target page | Recorded as the session's first "oracle that could not fire"; the substitute is a typecheck mutant |
| `comp-pipescript io` | run by DS~F on the consolidator: empty READS/WRITES + a self-declaring WARN | **The tool's blind spot on dynamic key construction, recorded as such** — "no writes detected" is not evidence of no writes |
| `safe-commit.sh` | 11 commits; 2 audited lane overrides (`POD4`, `SHARED_CLOUD_OPS`), SINGULAR — one lane per commit, never `--force` | ⛔ Also hit a `comp-system` BLOCKED-ON-PEER-LANDING (drift source was a peer's uncommitted `.tools/comp-find`) and an `index.lock` held by another seat's in-flight commit — **shared-worktree contention is normal, not a fault; the fix is to wait and re-run, never to force** |
| `comp-which` | not routed this session | Every search had a known target (a named PRD, project JSON, TO or source file); `comp-find`/`--name` was the routed tool in each case |

---

## 7. For the next seat at this desk

1. **STITCH-A decomp is next** (CTO's order), then INSURE's cert → TOs (seating STAGED per MSTR: 0.6.0 + DS first).
2. **The five live lanes report to this seat.** They are disciplined — every one verified its own start condition
   rather than trusting a message, and three filed findings against their own prior reports. Read what they send.
3. **Nothing is pushed.** Every hash here rides MSTR's integration window; say "LOCAL @hash, rides integration",
   never "landed".
4. **CRO is off-limits this session** (Andrew-direct ~19:3xZ at three terminals). One consequence with teeth: the
   alternate post-invalidation cert signer is base CTO ONLY, and a CVO correction that revises a number CRO~D is
   carrying can only reach them via MSTR or Andrew.
5. **The held promote `a239e4a9`** is PARKED-UNTIL-STALE with CTO's local tag; my 13:0xZ KNOWN-HELD adjudication
   stands and the sovereign half is at Andrew.
