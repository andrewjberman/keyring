# THE UNIFIED CANONICAL PATTERN SPEC — mdpf + advi (v1.0 RATIFIED)

**Author:** 1.0.0_SA_CTO · 2026-08-11 ~0530Z · **archetype:** IMPLEMENT (synthesis)
**Status:** **RATIFIED — Andrew-direct 2026-08-11 ~0542Z** (verbatim *"im cool with your recs"* on
the two calls as put; record + scope:
`ANDREW_DIRECT_20260811_RATIFICATION_EXCEPTION_SET_AND_PATTERN_SPEC.md`). The 9 atoms + grammar +
2 advi parameters are PROGRAM LAW. Atom 8's exception set is RATIFIED (§3 — non-fee residual
TRANSITIONAL). The mdpf cutover's live-chain acts remain gated on the CVO Rule-14e cert.
**Authority:** Andrew-direct mission (verbatim in handoff @1a518b303f): *"everything is in pattern,
consolidated, and colocated for gold layers inside of opal-data-assets/portal/gold ... flows rely on
bronze/silver in opal-data-assets and the gold goes in the same scoped folders in
opal-data-assets/portal/gold/{advi or mdpf}/{scope, e.g. global or firm}."* This program is Item 2a
of the four-month plan @1600047e64. *"We are never doing one-offs ever again on scripting."*
**Inputs (each at its vintage):** CRO mdpf ground-truth decomp @41692cd3d2 (Parts A1–A5, B; run
record @919f888ece — **DRY, UNCERTIFIED; CVO cert requested 052113Z, gates the cutover, NOT this
draft**) · CRO~A INF audit + refactor spec (`INF_ATOMDECOMP_RUN_20260811/03_GOLD_AUDIT_AND_REFACTOR_SPEC.md`)
· CRO~A INF stop mechanism (`01_STOP_MECHANISM.md`) · CLAUDE.md Rules 17/17a/17b (medallion law).

---

## §0 · WHAT THIS IS

One normative pattern, instantiated per PRODUCT (`mdpf` = Model Portfolios; `advi` = Advisor
Intelligence), such that a new product — or a new firm inside a product — is a PARAMETER BINDING,
never a new architecture. mdpf is the pilot; advi replicates with two parameter changes (§4).
The pattern below generalizes what the ground truth shows WORKING (the grammar is already live in
`build_portal_gold_accrual.py:3`); it parameterizes what diverges; it names each atom's measured
violation so conformance is checkable, not aspirational.

## §1 · THE GRAMMAR (colocation target)

```
s3://opal-data-assets/{vendor}/{firm}/bronze|silver/...            # raw vendor + parquet queryable (Rules 17/17a)
s3://opal-data-assets/portal/gold/{product}/{scope}/{artifact-type}/{data-as-of}.json
s3://opal-data-assets/portal/gold/{product}/_code/                 # atom 2
s3://opal-data-assets/portal/gold/{product}/_feeds/ | _staging/    # atom 4
s3://opal-data-assets/portal/gold/{product}/_manifests/{data-as-of}/{process-ts}.json
s3://opal-data-portal-v2/platinum/{product}/{scope}/...            # serving tier ONLY (Rule 17b)
```

**The flow, Andrew-verbatim (~0535Z, ANDREW_DIRECT_20260811_CTO_OVERSIGHT_SSOT_RECON_MANDATE.md):
ingestion → `{vendor}/{firm}/bronze` → an EVENT TRIGGER processes raw into silver parquets → gold
(staging or full) in `portal/gold/{product}/{scope}` with code, tables, and ALL dependencies
COLOCATED → a publisher pulls to `platinum/{product}/{scope}` — the MORNING TRIGGER PATTERN,
end-to-end, same pattern everywhere, "established forever," never ad-hoc haphazard routes.**
The bronze→silver leg is EVENT-TRIGGERED on raw landing; gold/publisher legs carry clock floors
with event accelerators (atom 5) — triggers are ROUTES, not monitors (moratorium respected).

- `{scope}`: `global` | `{firm}` for mdpf; `{firm}` × `{advisor}` for advi (§4).
- **Spelling law, per layer, by construction:** underscore in gold, hyphen in platinum
  (publisher `_KEY_RE`). A census keyed on either spelling alone reads the other half as orphaned —
  both directions fail toward deleting a live field. Keep both spellings declared, never "fix" one.

## §2 · THE NINE STRUCTURAL ATOMS (normative; measured violation named per atom)

| # | Atom (normative) | mdpf measured state (decomp vintage 08-11) |
|---|---|---|
| 1 | **One product root** `portal/gold/{product}/` — the data plane, `{scope}/{artifact-type}/{data-as-of}` | exists; advi has NO root yet (create `portal/gold/advi/` when its first artifact lands, not before) |
| 2 | **`_code/` = ONE deploy target.** DS deploy map points here; runners/lambdas pull ONLY here | 1 of ~50 artifacts moved; deploy map, feeders, smartx readers, dispatch still point at opal-data-mdpf (delta row 7) |
| 3 | **`_manifests/{data-as-of}/{process-ts}`** on every gold write | consolidator already writes this shape — it becomes law |
| 4 | **Declared intermediate plane INSIDE the product root** (`_feeds/`, `_staging/`) | feeds live in a standalone bucket; staging at `gold/mdpf_revamp` outside the root — both homeless, both re-homed by the cutover |
| 5 | **ONE producer per served key · one runtime per leg · a SCHEDULE FLOOR on every leg** (event accelerates, clock floors) | the main chain's only trigger is the INF sentinel — dark 11 days, the exact CLAUDE.md no-schedule-floor defect, measured live (delta row 4). The floor is a CUTOVER deliverable, not an alarm (moratorium respected: a schedule is a route, not a monitor) |
| 6 | **Config data NEVER in the code store** | `partner_roster.json` read from inside `code/` (`build_portal_gold_accrual.py:110,136`) — the measured violation; re-homed in cutover act (iii) |
| 7 | **Serve ONLY via the platinum publisher** (spelling law explicit) | publisher leg conforms (13:50Z daily, last-good re-serve); the frozen flat bell (07-23 ruling) stays retired |
| 8 | **RAW-FROM-ENDPOINT INVARIANT** — full text §3 | feeder tier largely conforms; INF serving chain measured with 5 illegitimate derivations (§3, §5) |
| 9 | **Provenance columns** `source_pipeline` + `_ingested_at` on every intermediate | already uniform across all 5 mdpf feeds — keep as law |

**Product-SPECIFIC atoms (never generalize):** mdpf — INF-sentinel convergence gate, BD settle-window
(A5≥2d), partner-roster scope set, 49F/SmartX vendor adapters, accrual bridge derivation. advi —
per-advisor scoping predicate, multi-vendor adapter set (Orion/Eclipse/BD), the rep-scope predicate
(W-C makes it DERIVED, one home — never hand-copied constants).

## §3 · ATOM 8 IN FULL — THE RAW-FROM-ENDPOINT INVARIANT

**The producer is a THIN ADAPTER: endpoint → raw(bronze) → silver(dedup/dtype ONLY) → serve.
RAW-FROM-ENDPOINT IS THE FIRM RULE; derivation is guilty-until-proven; every served field traces to
a raw endpoint field OR a NAMED calculated exception. A FAT GOLD TIER IS A PATTERN VIOLATION.**

**Decision rule (CTO read, pending Andrew's confirm):** compute only what NO single vendor endpoint
gives — i.e., what crosses SOURCES or ACCOUNTS. If a vendor computes it (Orion account-level
performance/TWR), pull it RAW. *"Performance is not a residual."* Measured proof the rule bites: the
vendor TWR dim is ALREADY silver-landed daily and the serving chain reads it NOWHERE
(CRO~A 03 §1) — the raw feed the refactor wants already exists, unconsumed.

**THE EXCEPTION SET — RATIFIED (Andrew-direct ~0542Z, *"im cool with your recs"*; record
`ANDREW_DIRECT_20260811_RATIFICATION_EXCEPTION_SET_AND_PATTERN_SPEC.md`). Everything not listed
here is pulled RAW:**

| ratified exception | kind | membership |
|---|---|---|
| net-new-assets (NNA) | **FLOW** | PERMANENT — no endpoint serves it; Andrew-named; C_01's job survives the refactor (point-in-time form = wave W-D) |
| non-fee-AUA residual `sum(fee_aua) − balance` | **BALANCE** | **TRANSITIONAL** — the Patrick ~$606K figure. Stays calculated TODAY; RETIRES to the raw Orion Billing pull (`is_fee_earning` classified sum, fix drafted `02_D04_RESIDUAL_FIX_DRAFT.md`) once D_04 is VERIFIED; on verified retirement it leaves this set and becomes a raw field |
| cross-account/household/advisor/firm rollups | aggregation | PERMANENT — the grain is ours, not the vendor's |
| unreconciled bucket (F4) | difference | PERMANENT — deliberately calculated; it EXPOSES cross-source drift |

**⛔ NNA (flow) ≠ non-fee-AUA residual (balance). TWO calculated nodes, never one** (CTO conflated
them 0455Z; Andrew corrected by 0458Z; do not re-merge).

**Conformance test per served field (mechanical):** name the endpoint field it traces to, or name
its exception-list entry. A field that can do neither is ILLEGITIMATELY-DERIVED and is a refactor
work item (the three-bucket method, CRO~A 03 §2, becomes the standard audit instrument per product).

## §4 · THE TWO ADVI PARAMETERS (everything else transfers unchanged)

1. **`{scope}` binding:** mdpf = `global|{firm}`; advi = `{firm}` × `{advisor}` (portal-served,
   scoped PER ADVISOR — the 08335338 ADVI account).
2. **Intermediate-plane fan-out:** advi's per-advisor artifacts are orders of magnitude more keys —
   the `_feeds/`/`_staging/` layout must partition by scope from day one (no flat dumps).

Verdict carried from the decomp: GENERALIZES-WITH-TWO-PARAMETERS, proven to LIGHT-SCAN depth only —
the advi full decomp (atom_decomp method) is the first advi work package, not a formality.

## §5 · THE MDPF CUTOVER SEQUENCE (the 4 acts, ordered; live bells protected)

**GATE (standing, not manufactured): CVO certification of the ground truth @41692cd3d2 precedes any
act that touches the live client-facing serve chain** (requested 052113Z; Rule 14e standing
certifier). **Protected surface throughout:** per-firm bells
`json/mdpf/{49financial,inflection}/account-distribution.json` — LIVE, client-facing, exercised
08-10T11:30Z. The frozen keys (cottonwood/global/flat) are NOT in scope to revive or delete here.

Ordered for reversibility (each act independently rollback-able; migrate-before-kill, never delete
first; no shadow channels — build-correct then DIRECT port on the production schedule):

| act | what | protects/notes |
|---|---|---|
| **(iv) FIRST — delete the 2 IAM-dead stages** (3.5 legacy-emit, 5 OWNTS) | already IAM-severed = zero-risk debt removal; also removes 2 of the 5 illegitimate-derivation sites | stage semantics finally match IAM intent; unblocks a clean chain run |
| **(iii) re-home accrual's `partner_roster` + code sync** | config out of the code store (atom 6) + accrual leg reads from `_code/` | daily 13:40Z leg; low blast radius; comp-blast before commit |
| **(ii) re-home the aggregate** → `_staging/` inside the product root | W1a already staged the consumer-side repoint (floor consolidator) | the series-coupling seam (STAGING_PREFIX) moves as ONE change, producer+consumer same window |
| **(i) LAST — re-home the feeder writes** → `_feeds/`; **the client-facing smartx read edge migrates WITH this, same window** | the highest-blast act; touches the live bells' upstream | schedule floor (atom 5) lands HERE: the chain gets a clock floor; the INF-sentinel event stays as accelerator |
| *(closing)* `_code/` consolidation + DS deploy-map repoint (atom 2) | after (i)–(iv), opal-data-mdpf holds nothing load-bearing → THEN the retire decision goes to Andrew | never a delete while any A1 item 1–7 edge still resolves to the bucket |

Every act ships with: owner + trigger + named precondition (ITEM_0 landing-plan discipline, COO
staffs); acceptance = the consuming leg exercised on the REAL path post-port (an ad-hoc QA run
reads, never a standing comparator); rollback = same-window revert of the single moved edge.

## §6 · THE ADVI APPLICATION SHAPE (staffing input for COO — suggested, not dispatched)

**ANDREW-DIRECT instruction 3 (relayed by CRO~A + MSTR ~0535Z, verbatim in CRO~A's ANDREW_DIRECT
record; folded 0530Z): the ADVI canonization runs through an ARCHETYPE — atom_decomp on the
49 Financial gold analytics runner; the 49F/Schwab 08335338 account (complete fact tables) is the
base for "the perfect gold analytics runner"; that shape becomes the archetype inflection +
cottonwood replicate endpoint-by-endpoint, field-for-field.** CRO~A owns the 49F decomposition +
archetype spec (citing this pattern's rows, not re-deriving them); the atoms in §2 and the atom-8
conformance test in §3 are the archetype's pattern contract; MDPF-side surfacings route back here.
**Naming law for this program (CTO ruling 0533Z, COO-surfaced): "49F" alone is AMBIGUOUS — it
appears against 08242234 (MDPF ingest path) and 08335338 (ADVI archetype). The full 8-digit account
+ the PRODUCT is the only unambiguous form in any dispatch, spec row, or finding.** And the C-n
collision (two grains, one label, across seats — Rule-24 hygiene one layer up) is SETTLED per CRO's
committed resolution @3833ce88d1, which supersedes this spec's 0533Z variant: recon chapters =
RECON-1..RECON-7; the scheduling-jam findings KEEP C-1/C-2/C-3 verbatim (already in live DS/AE
dispatches — relabeling dispatched work is the costlier direction, so the chapters moved instead).

advi's INF-side work already has a measured spine: CRO~A's INF three-bucket map + refactor waves
(03 §3). Sequence as ruled there: **W-E before Sunday 08-16 (hard date — else the 16 cancelled
accounts' histories re-erase)** → W-0 characterize (full 44 scripts; ~24 UNREVIEWED are marked) +
W-C universe predicate (kills the recurring 07-31 breaker class) → W-B performance-to-raw (feed
already landed; highest value/effort) → W-A valuation-to-raw → W-D point-in-time daily shape (the
architectural close; also the atom-5 schedule-floor shape). Then: create `portal/gold/advi/`
(atom 1) when the first conforming artifact lands; run the advi FULL atom_decomp to lift the
light-scan caveat. Orion/Eclipse/BD field-map work continues at CRO~A (egress granted).

## §7 · OPEN GATES (who holds what)

| at | the call |
|---|---|
| **ANDREW** | ~~(1) exception set~~ ~~(2) pattern spec~~ — **BOTH RATIFIED ~0542Z** (*"im cool with your recs"*); no open Andrew calls in this program as of that word |
| **CVO** | certify @41692cd3d2 (pass RUNNING, ACK 053137Z) — gates §5 acts touching the live chain |
| **COO** | staff §5 + §6 with owner/trigger/precondition per act (ITEM_0 discipline); MDPF repair keeps engineering priority |
| **CTO** | instrument-roster fixes: comp-pipescript 1-of-6-layers denominator blindness; comp-estate 404 platinum key + runner conflation (both routed findings from the decomp) |

## §8 · WHAT THIS SPEC DOES NOT DO

No new approval gates (the CVO cert + Andrew ratification are the handoff's own standing gates, not
manufactured here); no dispatch (COO staffs); no serving-surface touch; no advi product root until
its first artifact; no alarms/monitors — schedules and routes only (the atom-5 floor is a ROUTE).
The exception list is not final until Andrew's word lands in §3 and the PROVISIONAL marks come off.
