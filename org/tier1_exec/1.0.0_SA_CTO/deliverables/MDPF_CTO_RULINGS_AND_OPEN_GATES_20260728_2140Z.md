# CTO RULINGS + OPEN GATES — 2026-07-28, ~2005–2140Z session

**archetype:** COORDINATE
**Author:** `1.0.0_SA_CTO` (fresh session; predecessor PID 28724 died ~2000Z)
**Why this file exists:** ~15 rulings were issued across five lanes in this window and existed **only in broker
messages**. A broker message is not a record anyone will find in a week — I told two agents that tonight before
doing it myself. This is the durable carrier.
**Companion:** `MDPF_A2_SERVING_ORIGIN_RULING_AND_THE_SILENT_SENTINEL_20260728.md` (the findings).
**Doctrine landed this window:** `CONTROLS_OVER_CARE.md` §III-e `12cc4803f` · §III-f `627b7914e` · §III-g `4505b71fef`.

---

## 1. SOVEREIGN INPUTS THIS WINDOW (verbatim, with scope)

| time | verbatim | recorded |
|---|---|---|
| 171003Z | *"we dont care what legacy does, we want to move full force into the REVAMP canonical structure and deprecate legacy"* | DS @`bf986d81a` |
| 203435Z | *"Yes, cottonwood should be included"* | COO @`b95d8ce4a` |
| ~2134Z | *"how are the ETFs possibly delayed, we should be collecting that data daily"* (challenge; **falsified our stated cause**) | COO 213454Z |

---

## 2. THE STANDING RULINGS

**R1 — DEPRECATE LEGACY IS A DISINVESTMENT ORDER, NOT A DEMOLITION ORDER.** Legacy keeps running, unfixed and
undiagnosed. **Both `explicitDeny` holds STAY** — removing them is not deprecation, it is un-protecting the
serve. Teardown is the LAST step of the cutover. Grounding: *a known-wrong frozen number is strictly safer than
an unheld pipeline.*

**R2 — THE PUBLISHER CARRIES ITS OWN `ScheduleExpression`.** `cycle-complete.json` is an **accelerator only**.
Event-only triggering would be (a) the CLAUDE.md-named defect whose measured instance is this product
(`mdpf-daily-refresh-trigger`, `ScheduleExpression: None`, six-day freeze on fresh inputs) and (b) **born dead** —
that marker has never been written once. **This de-couples the publisher from Stage 6.**

**R3 — A-2 SERVING ORIGIN: OPTION 1, THE SEPARATE EGRESS PRINCIPAL.** Decided on Andrew's generalization
constraint (*anything that cannot absorb `advi` without a rewrite is wrong*): Option C is 9 exact-path behaviors
+ 9 hand-enumerated bucket-policy keys, so every new product/scope/type is hand-written infra. **The fence
governs WRITES, CloudFront governs READS — orthogonal planes.** A new **non-fenced** principal widens nothing for
the 12 existing members; 11 of 12 are ingest roles and the publisher is egress — a **misclassification**, not a
carve-out. **LANDED** `a11b8e2cc3`, applied+verified 8/8 on the live role, staging-scoped.

**R4 — NEVER#3 IS NOT DISCHARGED BY R3.** A-2 authorises the principal's **shape**, not standing up the first
automated writer onto a deliberately frozen, hand-published serve. **`var.mdpf_egress_live_serve_write_cosigned`
stays `false`; CTO half is mine, COO half outstanding, and it needs verified-publisher evidence to be worth
asking for.** *(The portal-v2 bucket policy carries **ZERO** deny statements — both Denies are PRINCIPAL-scoped
on `mdpf-daily-runner-ec2-role`, so a new principal is a second door, not a widening.)*

**R5 — COTTONWOOD: CANONICAL ONLY (reading 1).** The canonical builder already carries it
(`build_global_artifact(a49, ainf, acot)`, exercised ~15:00Z; `portal/gold/mdpf/cottonwood/` 4 types). Andrew's
instruction **already satisfied in the canonical lineage**. **GO to DS CANCELLED**, R1 intact. *(I dispatched a
legacy point-fix 40 min after ruling against legacy point-fixes; COO caught it mid-flight; DS reverted and
preserved the work as a patch.)*

**R6 — ROSTER: DECLARED ONCE AT THE AUTHORITY, READ NEVER RESTATED; TYPES DERIVED PER SCOPE.** Authority =
`data/mdpf/config/partner_roster.json`. **Resolve every divergence TOWARD the roster, never by reconciling the
roster to code.** Doctrine §III-e.

**R7 — PROVENANCE GOES IN THE PUBLISHER, NOT INTO CLOUDTRAIL.** **Do NOT enable CloudTrail data events on
portal-v2's legacy `json/` namespace** — it is an unsettled route, and Andrew's ordering is *canonical routes and
schedules first, monitoring only once the thing being monitored is settled.* **Instead: every artifact the
publisher writes carries who wrote it, when, from which source keys, at which vintage — producer-stamped, inside
the object.** Strictly better than CloudTrail for the need: survives in the artifact, answers *what produced this
content* rather than *which API call touched this key*, and cannot be absent for the period before someone
enabled it.

**R8 — A FRESHNESS VERDICT MUST NAME ITS OWN BASIS.** `vintage_bearing_feeders` is 2 of 5; `model_composition`,
`etf_net_assets`, `partner_held_etf` are tracked and **excluded**, so `status: "current"` is a partial verdict
presented as a total. **Add `basis_feeders` + `excluded_feeders` (with vintages) — the data is already in
`by_feeder`.** NOT ruling that the excluded feeders should become vintage-bearing (that needs semantics I lack);
**ruling that a verdict may never conceal which population it covered.** Publisher spec, not a legacy edit.

**R9 — NO SERVE RE-POINT, EVER, AHEAD OF THE PRODUCER.** A serve fix produces a hand-corrected object the next
producer run clobbers — the 07-23 split-brain, which §17.1 forbids — and it is a served-output move (NEVER#3).
**A correct number in a file nothing authoritative produces is worse than a wrong one, because it reads as
fixed.**

**R10 — TOOL REGISTRY: POPULATION HAS ONE AUTHORITY; ATTRIBUTES MAY LIVE APART IF DERIVED.**
`comp-coverage-map.yaml` is the sole population authority. `TOOL_MASTER.yaml` may remain an attribute store
**only if** its list derives from the authority and the generator **fails loud on divergence, both directions**.
Parity check must run in `comp-manifest-check`'s registration invariant — a hand-run generator is not a refresh
mechanism. *(Guard fired on first exercise: **authority 89, master 89, sets divergent by 12**.)*

**R11 — ONE PLAN OR NONE, ACROSS ALL THREE TOOL REGISTRIES.** A partial fix retires the symptom that would make
anyone look again, converting a visible inconsistency into an invisible one. **LANDED** `85a64cada`, invariant
proven with a frozen literal fixture + 3 source-file mutants.

**R12 — `EC2_MANIFEST` TRIGGER FIELD BECOMES REQUIRED, WITH A DECLARED-UNKNOWN SENTINEL PERMITTED.** Both
halves; the second makes the first landable. **22 of 27 services assert nothing about how they are triggered** —
an optional field cannot be audited for absence. Precedent already ratified one tree over:
`partner_roster.gate_coverage`'s `NOT_COVERED` convention. **Mine to route; not built.**

**R13 — STALE COTTONWOOD SCRIPTS: DO NOT DEPLOY.** Repo is newer for both; `pair.py` differs by **976 lines — a
different generation, not drift.** 17a: *which is RIGHT, not which is RUNNING.* **And the sharper reason:
`slice.py`'s new `holdings_total_by_date()` is the measured-vs-interpolated logic DS is HELD on — deploying would
move DS's held variable from another lane, silently, on the run meant to accept AE's grant.**

**R14 — `aum-metrics.json` + `account-distribution.json`: EXTEND THE DENY.** Both are served keys outside the
current protection, with a known clobber history and 3 candidate writers. **Protecting served output is what R1
preserves; it is not spending on legacy.** ⚠ Principal-scoped only — narrows the known clobberer, does **not**
close the class.

**R15 — `comp-which` REWIRE REQUIRES BYTE-IDENTICAL ROUTING.** Rule 21 makes it every agent's first reflex; a
speedup that alters one routing answer is a correctness regression on the estate's primary search instrument.
Corpus must include a query that routes to the `comp-grep`/`comp-glob` fallback — the path that failed open
2026-07-25 while `comp-which` itself resolved fine. **Owner `0.8.0_AE_CloudComp`; routed, not done.**

---

## 3. OPEN GATES — owner, state, what closes it

| # | item | owner | closes on |
|---|---|---|---|
| G1 | **never-widen co-sign** for the live-serve write | **CTO + COO** | verified publisher evidence, then one variable flip |
| G2 | **consolidated reader census** — `json/mdpf/*`+`json/portfolios/*`, `platinum/mdpf/aggregate_aua/*` (434 obj, 1 consumer measured = FLOOR), `etf_ownership_timeseries/*` + the bare product-level file | **`0.2.0_DT`** (GO issued 213509Z) | predicate + set reported, 401-gating residual carried forward |
| G3 | **emitter consumption defect** — source carried 07-28 current 49F ETF values, emitter wrote 07-06 `rolled_forward`. **Collection fine, consumption not.** Discriminator: same array yields FRESH for inflection (`rps_actual:49financial` vs `target_weight:inflection`) | **`0.7.0_AE` base** | the 3 ordered questions; **(3) `_total__partner_aua` = 0 with a current `as_of` ranked FIRST for severity** |
| G4 | **`mdpf_aggregate_aua.py` roster single-source** + sentinel in the SAME commit | unassigned (R5 cancelled it) | reopens only with the producer re-point |
| G5 | **roster runtime presence** — runner syncs ONLY `code/scripts/` with `--delete`, so both the cross-tree import AND the repo-relative read fail there | **`0.7.0_AE`** | a dispatch/`CODE_TREES` decision, not a table entry |
| G6 | **P1 accrual runtime exposure** — `build_portal_gold_accrual.py` reads the roster repo-relative; works in QA, would fail-close on the runner | **`0.4.0_DS`**, gate CTO | asked before P1 is scheduled |
| G7 | **976-line generation gap** on the two cottonwood emitters | **`0.4.0_DS`**, gate CTO | architectural review, **coupled to DS's held read-preference — neither moves alone** |
| G8 | **Option C staged machinery** — OAC + origin + 9 behaviors declared, **0 applied**, in a frozen tree | **CTO** | explicitly retired or marked superseded-by-`{product}`-generalization, with the reason |
| G9 | **§17.2's 9-row consumer table** vs DT's derived **23-key / 6-namespace** union @`ef18a5fac` | **CTO** | PRD carries the DERIVATION + residual, **never the number — it has been wrong four times (4→5→8→23)** |
| G10 | `HEADLINE_NONMODEL_FIRMS` basis — must NOT derive from the partner roster (*who exists* ≠ *whose non-model counts*) | **CTO** | a declared `headline_basis`, or an annotated literal citing its ruling |
| G11 | `|| return 1` sweep · `account-units` consumer trace · A2 remainder | **CTO** | outstanding |
| G12 | legacy-lineage stall ownership beyond G3 | **AE-base successor** | live |

---

## 4. CORRECTIONS AGAINST ME THIS WINDOW (five; the pattern is one)

1. **Ruled option 2 "dead, killed three ways" — the Terraform refuted me.** Option C already existed.
2. **Parked the critical-path gate** (AE ③) 13 minutes after ruling the publisher critical path — **by CATEGORY
   ("design-heavy") instead of by POSITION IN THE CHAIN**, while holding a handoff that named it as the gate.
3. **Nearly filed two instrument defects against `comp-routes`, which was right on both counts** — 25-vs-24 was
   the default behavior counted by one and not the other.
4. **Dispatched a legacy point-fix 40 minutes after ruling "no legacy point-fixes."** Routed meticulously by
   *lane* (Rule 13) and never checked it against my own ruling on *whether the work should happen*.
5. **Ruled A-2 while having personally written, 40 minutes earlier, that the Denies are PRINCIPAL-scoped and
   "nobody writes that prefix" is a convention not a control** — then authorised a new principal that writes
   there. AE-base measured the bucket policy and found what I had already recorded in prose.

>> **THE COMMON SHAPE: I recorded the hazard and then authorised the thing it warned about. In four of five, the
>> refuting evidence was already in my own text or my own instruments.** The failure is not missing knowledge —
>> it is not re-reading my own record before ruling on the thing it covers. **Three lanes caught three of these
>> before they cost anything; none was caught by me.** <<

**Also this window: I ran a `--since` window that resolved into the future, got `0`, and was one step from
reporting a peer's claim "unconfirmed."** The positive control caught it. **Both halves of that exchange were
saved by controls, not by care.**
