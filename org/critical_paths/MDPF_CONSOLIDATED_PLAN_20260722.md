# MDPF — CONSOLIDATED STOCK-TAKE + DIRECTED PLAN

**Andrew-direct 2026-07-22 ~1505Z:** *"we need to take stock of what is where in our MDPF work and create a
comprehensive, directed plan to efficiently address it."*
**Author:** `1.0.0_SA_CTO` | **State verified live at 1505Z, not recalled.**

---

## PART 1 — WHERE WE ACTUALLY ARE

### 1.1 Served surface — UNCHANGED, KNOWN-GOOD
CloudFront `EVTSA9VEHNZVH` = **24 behaviors / 7 origins**, no assets origin, catch-all → `portal-v2`.
**Nothing has been served from the revamp. Nothing is stranded.** Both deploy ledgers closed.

### 1.2 Data — FIXED, STAGED, NOT PINNED
10 objects under `gold/mdpf_revamp/`. **3 moved today** (the count-axis fix):

| object | ETag | state |
|---|---|---|
| `inflection/aggregate_aua_timeseries` | `5e7b684d` | **REBUILT** |
| `global/aggregate_aua_timeseries` | `08f9720e` | **REBUILT** |
| `portfolios/aum-timeseries` (A2) | `ca0c6d1c` | **REBUILT** |
| `49financial/aggregate_aua_timeseries` | `aa5c5b85` | unchanged |
| `portfolios/aum-metrics` (A1) | `529b7c21` | unchanged |
| `global/non_model_assets` (A4) | `8a195549` | unchanged |
| `account_distribution` ×3 | `865919f2` / `afb964c4` / `b946d836` | unchanged |
| `non_model_assets_precutover_frozen` | `da2260f6` | reference, not published |

**This is a CHECKPOINT, not a pin — Cottonwood rewrites `global` again.** Co-sign is **0 of 3**.

### 1.3 What is genuinely FINISHED
- **Count-axis defect CURED AT SOURCE** — count and value now derive from the same eclipse snapshot for
  **all** dates, not date-scoped (CVO source-verified).
- **Enumerated 20-date exemption** landed + independently exercised (4 controls incl. remove-a-listed-date).
- **Cottonwood WS-1 bronze** live, **unattended fire proven** 07-22 06:00Z (31 objects, both gates, 296 reconciled).
- **WS-2 silver + WS-3 gold** complete. Conservation proven: 296 accounts' holdings vs dim sum differ by **$0.02**, pure rounding.
- **WS-5 converter half** landed; **event path + sweep backstop land together.**
- **Import-closure gate** live; **eclipse landmine disarmed** (inert — module vendored, converter NOT upgraded, STALE signal deliberately preserved).
- **FE `$0` defect fixed** (portal DEV `08c6d8b2`) — including the false *"rolled forward from last known data"* claim.
- **Andrew's 6 rulings applied:** one-flip · merge CG→LTC · satellites unlabelled / primary keys only · Income = non-model · gate-not-alert · "Not yet tracked".

### 1.4 The REAL blockers — all of one family
> **Everything built works. Almost nothing is WIRED. The estate encodes "there are exactly two partner firms"
> in several independent places, and each must be opened for a third.**

| # | Blocker | Owner | Status |
|---|---|---|---|
| B1 | `revamp_stage()` has **no Cottonwood leg** — DE's producer is a standalone script nothing calls | DE + AE | open |
| B2 | The per-cycle **source audit is not invoked** by the nightly | DS → AE (diff ready) | open |
| B3 | `lambda_entry` has **no destination-envelope branch** — blocks the WS-5 apply | 0.6.2 | open |
| B4 | `build_global_artifact(49f, inflection)` is a **hardcoded 2-arg call** | DE | open |
| B5 | **Enumeration** of two-firm assumptions incomplete — **4 confirmed, 1 checked-clean, infra/publisher/remaining producers NOT covered** | DE | **precondition** |

### 1.5 Known and ACCEPTED, not open
- **49F count axis:** measured defect (07-17, −10 accounts), mechanism **UNDETERMINED**, **no assurance
  instrument exists** — no historical source, artifact-internal checks structurally blind. **Monitored
  prospectively; declared, not cleared.** Decouple is a prerequisite for Global count completeness.
- **Global count axis** will ship with **20 enumerated gaps** — the trading days legacy omits. Honest absences.
- **Day-one Cottonwood** = 1–2 points at the right edge, **zero overlap** with the existing 427-date series →
  **every pre-07-21 Global value is byte-identical with Cottonwood absent, BY CONSTRUCTION.**
- **~$126.4M step** enters Global on 07-21. Real, labelled, not smoothed.

---

## PART 2 — THE DIRECTED PLAN

**Ordering principle: the enumeration gates the build; the wiring gates the emit; the emit gates the pin;
the pin gates the co-sign. Do not invert these — every inversion today cost a re-do.**

### PHASE 0 — CLOSE THE ENUMERATION *(gates everything; the only real unknown)*
**Owner DE.** Finish the census of every place "exactly two firms" is encoded — **with a stated denominator
and an explicit not-covered list.** Must reach: `infra/` dispatch + IAM, the publisher/promote path,
`dim_mdpf_account_distribution.py`, `dim_mdpf_aum_{metrics,timeseries}.py`, the FE per-firm distribution path.
**Exit: the list is closed and priced. This is what sets the date — nothing else is unbounded.**

### PHASE 1 — BUILD *(parallel, all unblocked)*
- **1a · DE** — re-home Cottonwood as `build_cottonwood_artifact()` **inside the shared producer** (the
  standalone script structurally cannot feed an in-memory composition); change the `build_global_artifact`
  signature; extend `--firm` + `want` sets. **Cottonwood JOINS the existing trading-day axis — global does
  not become a multi-axis join.**
- **1b · 0.6.2** — `lambda_entry` destination branch, **POSITIVE envelope match** (`version` +
  `requestContext` + `responsePayload`), never a catch-all `else`. → unblocks **1c**.
- **1c · 0.7.0** — WS-5 apply (`-target`, 5 conditions) → deploy blackdiamond-only artifact **past
  `7aa7e645f`** → exercise on the **`mode == "event"`** discriminator.
- **1d · 0.7.0** — Deliverable 2 `portal-v2 json/mdpf/**` deny **+ the lifecycle limb**; exercise = denied
  delete naming the policy + isolated positive control. *(Independent of everything else.)*
- **1e · DS → AE** — wire the audit into `revamp_stage()`: **inflection FAILS the stage, 49F REPORT-ONLY**
  (it has a known defect and would fail every night), placed **before** the completion marker; fold verdict +
  coverage into `cycle_complete` so the running count **accrues**.
- **1f · 0.7.0** — the import-closure census: *how many of 179 buildable functions are running code that
  would not import if rebuilt?* **Report the instrument's reach; the unreached are NOT clean.**

### PHASE 2 — WIRE THE NIGHTLY *(the step that makes an emit possible at all)*
Add the **Cottonwood leg** to `revamp_stage()` (B1) alongside 1e's audit wiring. **Until this lands, no
nightly can produce a Cottonwood-inclusive set and there is nothing to pin.** *(This is what killed the
2-day estimate — it was never in anyone's scope.)*

### PHASE 3 — EMIT + VERIFY
**The scheduled nightly emits** the Cottonwood-inclusive set. **No hand-staging** — a hand-staged artifact
proves the code works, not that the production path emits it, and that is the exact masking class we found
in WS-5. → **CTO pins the emitted ETags** → **fresh 3-pass**: DS producer-validate (incl. hand-run audit on
the pinned set), CVO from-scratch re-derive, DT consistency.
**BINDING:** every gate is **re-exercised against the THREE-firm artifact — none of today's proofs transfer**
(all were mutant-proven on a two-firm global). Every limb states its **coverage fraction against the
defect-capable population**, never a percentage. **49F COUNT-mode render cell cannot be waived** — it is the
only non-degenerate instrument left pointed at that firm.

### PHASE 4 — CO-SIGN + FLIP
Fresh **CTO + COO + Andrew** never-widen co-sign on the pinned set, carrying the declared terms (49F
unbounded-by-construction; retained legacy runtime dependency; 20-date Global gap; 1-of-6 historical
coverage). → **FE-first promote** → AE `-target` apply → **immediate revert-plan hard gate** → verify-before-serve
→ rollback armed until explicit disarm.

---

## PART 3 — WHAT SETS THE DATE

**Phase 0 is the only unbounded item.** Phases 1–4 are each hours, not days, and largely parallel.
**I am not quoting a date until the enumeration prints** — I quoted one this morning off remaining-WS-numbers
and it did not survive contact with the wiring gaps. **The better basis exists: the estate has a defined
firm-onboarding sequence (FIRMSEP.10) and Cottonwood is part-way through it. That step list is the skeleton.**

**Standing correction to how this was scoped from the start: we have been treating a FIRM ONBOARDING as a
DATA FOLD.** Every blocker above is the unfinished half of a known onboarding sequence, not a fresh surprise.
