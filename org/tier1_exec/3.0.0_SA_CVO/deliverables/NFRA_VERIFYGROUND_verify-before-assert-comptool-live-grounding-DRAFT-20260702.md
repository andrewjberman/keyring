# NFRA_VERIFYGROUND — Verify-Before-Assert: Comp-Tool + Live Grounding

**Author:** 3.0.0_SA_CVO · **Date:** 2026-07-02 · **Status:** RATIFIED — Rule 22a committed `012e24fcb` (CLAUDE.md line 41); COO adopted announce-mode (`20260702T195103Z`); tool-briefs → CTO next /drive cycle.
**Origin:** the bd-49f ModeMarker incident + Andrew's two asks (comp-tool-grounded verify; fold into RAVC) + item #3 (Terraform/drift governance).

---

## 0. The motivating incident (the canonical worked example)

The bd-49f `session-trigger` role's `ModeMarker` IAM statement was authored `Action=["s3:PutObject"]` **only** at the 06-29 chain landing (`7a6108fde`) — write the marker, but no `s3:GetObject` to read it back. The runner-run leg reads that marker (`bd-49f-session-trigger/lambda_function.py:93`) to route → `AccessDenied` → **bd auto-ingest silently broken 06-29 → 07-02**. It was invisible because (a) 0.6.0's un-freeze backfilled *out-of-band* so the read-path was never exercised, and (b) reading the config/`.tf` would have looked complete.

Three lessons, each becomes a clause:
1. **State ≠ design.** At 18:34Z the fix was *committed* (`bb638b747`, `.tf` had GetObject) but *not applied* — live was still PutObject-only. `comp-iam` reading the `.tf` (DESIRED) would have said "fixed"; only live `get-role-policy` showed the truth.
2. **"Works" needs exercise, not a config read.** "Auto-ingest works" was not verifiable from IAM — the kill-cookie *exercise* surfaced it.
3. **It was a code bug, not drift.** Live matched the `.tf` (managed, grouped in `bd-pipeline/`, 0-diff plan). Root = code-review miss + never-exercised — *not* a governance/out-of-band failure. (Estate audit confirmed grouping is clean; one replicated shape found in cot — vestigial, see Clause 2.)

---

## 1. Clause A — Dual-grounding of a verification claim  *(the core rule)*

A RAVC that **gates an action** (fix / cert / ruling / dispatch / GO) on a **{control-state, IAM, deploy-parity, freshness, resilience}** claim must carry a `grounding:` citation with **both** of the following, as applicable:

- **(A) State/control claim → comp-tool + live-primitive.** Cite the on-rails comp-tool (`comp-iam`/`comp-freshness`/`comp-pipescript deployed`/`comp-routes`) for the graph-aware/DESIRED view, **AND** the live primitive (`aws iam get-role-policy`, S3 head, CloudWatch, `describe-*`) for the **applied** truth. The live read is **mandatory** when the claim concerns (i) a fresh/in-flight change, (ii) anything the comp-tool models as DESIRED-only (`comp-iam` default), or (iii) a phantom-backstop risk (declared-but-maybe-unapplied).
- **(B) Behavior / "works" / "GREEN" claim → exercise-the-path.** Cite the *exercised-path* evidence (the test that fails if the claim is false) — not a config read. "X works / is-resilient / auto-runs" requires an exercise (the kill-cookie model), not a permission/config read.

**Verdict semantics:** a comp-tool DESIRED verdict *alone* for an applied claim, or a config read *alone* for a behavioral claim, is `INFERRED` — **non-actionable**. The cert/dispatch owner (COO/CTO/CVO) **withholds GO** until the grounding is complete. (Extends the existing Rule-22 `grounding:` doctrine + the TO-compiler-gate withhold.)

**Scope:** **action-gating claims only** (Andrew-confirmed) — a claim a fix/cert/dispatch *rests on*. Not every casual observation (avoids gate-fatigue per the CLAUDE.md over-gating warning; mirrors Rule 22's "resting on a causal claim" trigger).

**Enforcement (tiered, Andrew-confirmed):** hard-withhold for SEV1/served-critical + IAM/security claims; nudge (HUD-style) elsewhere.

---

## 2. Clause B — Paired-permission lint  *(deploy-time review gate)*

An IAM statement granting a **write** (`s3:PutObject`/`dynamodb:PutItem`/…) on a **marker/state/sentinel/mode object** that the same principal (or a sibling leg in the same chain) **reads back** must also grant the paired **read** (`s3:GetObject`/…) — and vice-versa. A write-without-read (or read-without-write) on a routing/state object **fails review**.

- **Would have caught bd** at authoring (06-29), not day-3.
- **Estate evidence:** `cot-pipeline/iam.tf:60` `WriteModeMarker = PutObject`-only on `session-trigger-mode.json` — same shape; grounded as **vestigial** (cot never reads it), routed to the cot owner to remove or pair. `inf-pipeline` has `Write*Marker` + `ReadSentinels` — pairing appears present; per-marker confirm pending.
- **Impl:** a `comp-iam gaps` / pre-commit lint pass over `Sid` names matching `*Marker|*Sentinel|*Mode|*State|*Complete` on single-object resources → flag unpaired.

---

## 3. Clause C — Coverage requirement

Every Lambda / critical resource must be (i) in a **managed grouped module** (Andrew's grouping principle), **AND** (ii) **sha-tracked** in `lambda-source-map.json` (`artifact_sha256`) so CI code-drift-detection covers it.

- **Estate evidence:** grouping is clean (all in domain modules). But **40 Lambdas are not sha-tracked** → outside CI code-parity. Mostly ancillary; **sensitive subset to fix first:** `trade-authorizer`, `trade-auth-handler`, `opal-bd-transaction-consolidator`, `opal-inf-value-parity`, the served-guards. (Full list in the audit appendix.)
- **Gate:** the existing Rule-4 source-map requirement, upgraded from "has an entry" to "has an `artifact_sha256`," verified by `comp-lambdamap parity` (no NO-RECORD on critical fns).

---

## 4. Clause D — Estate drift scan, FOLDED INTO safe-apply  *(Andrew item #3; Andrew-decided 2026-07-02: fold into safe-apply, not a standalone CI job)*

Out-of-band change (change without `terraform apply`) must be **detectable continuously** — and the natural chokepoint is **safe-apply itself**:
- **safe-apply runs the pre-apply `terraform plan`** and treats a non-zero **pre-existing** diff (i.e. live already drifted from `.tf` before this change) as a **drift alarm**, not silent noise. So every apply doubles as a drift check on its module; a module never applied stays covered by the scheduled sweep below.
- Supplement: `comp-lambdamap parity` (code) + `comp-iam reconcile` **against a fresh census** (IAM) — today's `comp-iam reconcile` runs against a stale census, so it needs the freshness fix (§6.1). A low-frequency scheduled `terraform plan` over modules not recently applied backstops the safe-apply-folded check for cold modules.

---

## 5. RAVC `grounding:` field spec (the operational fold)

Every action-gating RAVC of the claim-types above emits:
```
grounding:
  claim: "<the assertion>"
  type: {IAM | control-state | deploy-parity | freshness | resilience}
  desired: "<comp-tool + output>"          # (A) the graph/declared view
  applied: "<live-primitive + output>"     # (A) REQUIRED for applied claims
  exercised: "<the test run + result>"     # (B) REQUIRED for 'works/GREEN' claims
  verdict: {GROUNDED | INFERRED}           # INFERRED => non-actionable, GO withheld
```
Canonical example (bd ModeMarker): `desired: comp-iam (would show DESIRED .tf) ; applied: aws iam get-role-policy -> action=['s3:PutObject'] (bug live) ; exercised: kill-cookie -> runner Invocations 0->1, 3/4 tables landed -> GROUNDED`.

---

## 6. Tool briefs (pair the rule with tooling so it survives time pressure)

**6.1 `comp-iam --live`** — a mode returning DESIRED + applied + delta in **one** call (on-demand-fresh reconcile), so (A) is one call not two. Rationale: the reason agents skip the live read is friction; remove it. Today `comp-iam reconcile` exists but runs against a stale census — make the census on-demand-fresh (or `--live` bypasses the census entirely with a live `get-*-policy` for the queried roles).

**6.2 paired-permission lint** — `comp-iam gaps` extension: flag write-without-read / read-without-write on marker/state objects (Clause B). Pre-commit + CI.

---

## 7. Rollout (announce-then-enforce, per NFRA_COMPRAIL)

1. Land the `grounding:` field + the two tool briefs (nudge mode).
2. Announce; agents adopt the field on action-gating RAVCs.
3. Enforce (hard-withhold) on SEV1/IAM/security first; nudge elsewhere; escalate per the ramp.
4. Close the estate baselines: cot marker, the 40 sha-tracking, the drift-scan CI job.

---

## Decisions — RESOLVED (Andrew-direct 2026-07-02)
1. **Home = AMEND Rule 22** (extends the existing grounding doctrine; not a new numbered rule) → shipped as sub-clause **22a** (text below).
2. **Clause D = FOLDED INTO safe-apply** (the pre-apply plan is the drift chokepoint; scheduled sweep backstops cold modules) — see §4.
3. **Hard-withhold tier = SEV1 + IAM + Security only** (nudge everywhere else).

## The CLAUDE.md Rule 22a wording (for commit on Andrew's nod)
> **22a. Ground a verification claim on the RIGHT layer.** A claim that GATES an action: STATE/IAM → cite the comp-tool (graph/DESIRED) AND the live primitive (`get-role-policy`/`head-object`/`describe-*`) for APPLIED truth — mandatory for a fresh/in-flight change (`comp-iam` default = DESIRED, cannot tell landed-from-planned); BEHAVIOR/"works/GREEN" → EXERCISE the path (the test that fails if the claim is false), never a config read. Comp-tool-DESIRED-alone (an applied claim) or a config-read (a behavioral claim) = `INFERRED`, NON-ACTIONABLE → cert/dispatch owner withholds GO (**hard-withhold for SEV1 / IAM / security; nudge elsewhere**). Gate: the RAVC `grounding:` field carries `desired`(comp-tool) + `applied`(live) + `exercised`(the run); **safe-apply folds** the pre-apply drift-plan check + the write-without-read (marker/state object) paired-permission lint. Why/incident + full spec: `org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_VERIFYGROUND_...20260702.md` (bd-49f ModeMarker: PutObject-only 06-29→07-02, silent because never-exercised; `comp-iam` DESIRED would have read the committed-not-applied fix as GREEN).

---

## 8. Day-1 dogfood evidence (2026-07-02 — the rule caught real errors the same day it landed)

The discipline is not theoretical — it corrected four would-be-wrong CVO calls this session:
1. **P2 gate-3 below-tier-deny (bounded-scan false-negative).** A bounded (evening-window) audit scan returned **0** min_tier_denied records. Under 22a-B I did NOT assert "no below-tier-deny exists" (which would have wrongly demanded a fresh probe) — I ran the full 5359-record scan, which **grounded the actual record** (`readonly-cert-probe@` DENIED min_tier on the deployed gateway @22:32:50Z). *Don't assert on incomplete grounding.* → cert PASS, CTO-acked.
2. **WS-4 AC-2 root (mechanism-grounding).** I observed AC-2 not firing (a DEFER'd perf dim slips through) but did NOT assert the *cause* until I **read the served `dashboard.json`** and confirmed it exposes only a top-level `data_as_of`, **no per-dim as_of map**. Grounded the mechanism (Rule 22), not just the symptom. → the AC-2 gap is now a scoped emit-side fix (DE), not a hand-wave.
3. **sha-baseline key-structure.** My first coverage check looked for a `provenance` key and would have reported "missing"; I re-read the **actual** committed entry shape (`artifact_sha256_provenance`) before asserting → 6/6 GREEN, no false alarm.
4. **The P0 hypothesis-overturns.** "Schwab box stopped / vendor stuck" (falsified — wrong instance checked), "inf self-clears at 16:00Z" (falsified — inf was broken), "assets_v2 format landmine" (overturned by a fresh-silver-today exercise). Each was an `INFERRED` symptom-claim that source/live-grounding overturned before it drove a needless fix.

## 9. Rollout status (as of 2026-07-02, EOD)

- **Rule 22a:** LAW — committed `012e24fcb`, CLAUDE.md line 41.
- **`grounding:` field (Clause A + §5):** ADOPTED announce-mode by COO (`20260702T195103Z`) — applied to the COO acceptance bars + all action-gating RAVCs going forward.
- **Tool-briefs (§6.1 `comp-iam --live`, §6.2 paired-perm lint) + Clause-D safe-apply fold (§4):** routed to CTO for the **next /drive cycle** (build-before-hard-enforce; CTO delegates the safe-apply AE build).
- **Estate baselines (Clause B/C):** cot vestigial marker (`cot-pipeline/iam.tf:60`) → routed DS~C; the sensitive sha-subset (6) → **committed `97059db92`, CVO re-confirm GREEN**; remaining ~34 → `comp-lambdamap baseline` follow-on TO (0.7.0~A owns).
- **Enforce ramp:** nudge-mode now; hard-withhold on SEV1/IAM/security as the tool-briefs land. CVO verifies each tool/gate lands + FIRES (exercise-not-config-read — 22a on 22a).
