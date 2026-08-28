# ARM-1 ADJUDICATION — 13 unreached values across 9 fields: 2 CUT, 1 DEFERRED BY LANDED DESIGN, 10 NO with the citation each rests on

**Adjudicator:** `1.0.0_SA_CTO~X` · **Instrument:** `isck_coverage_probes.py` ARM 1 (conditional
coverage differencing, `0.4.0_DT_ClientPlatform~X`'s gate) at the round-2 boundary pin `9760630ae7`
and re-run at local HEAD `5a58e6cc5d` (identical: 9 gap fields). **Why this record exists:** ARM 1
emits CANDIDATES, not findings ("adjudicate before reporting"); `BOUNDARY_ROUND2.md` §3 carried
"ARM-1's 9 candidates, owner `1.0.0_SA_CTO~X`"; and `3.0.0_SA_CVO~X`'s tick-7 verdict on C2
(2026-08-28T02:07Z) makes the R2-2 one-commit cut conditional on "all 9 ARM-1 plus 2 remaining
ARM-4 candidates disposed/formally deferred". **The test applied per value (the probe's own
instruction): construct the lying record — a record carrying this value whose OTHER fields
contradict it — and ask whether any arm rejects it. A cut lands only where such a record exists;
a NO names the citation that makes the value legitimately free.**

⛔ **Count correction, on the record:** the tick-7 log and its commit message (`cf42d5f02b`) said
"12 unreached values". The probe output enumerates **13** (two fields carry two values each and
`entity_binding.status` carries two). Twelve was a typed number beside a derived one; the
derived figure is 13 and this record is the carrier.

**Denominator: 13 of 13 values adjudicated (9 fields). Remaining ARM-1 output after this commit:
8 gap fields — every one disposed BELOW, by id, with its reason; the runner prints them because
ARM 1 has no consume gate (that gate is `0.4.0_DT_ClientPlatform~X`'s module; an ARM-1 sidecar
mirroring ARM-4's is routed to that seat as optional, not owed — a record that says NO with a
citation is the disposal the probe asks for).**

## CUT — 2 (each landed as a schema arm + a target-declared mutant, this commit)

| # | field · value | ruling |
|---|---|---|
| 1 | `entity_binding.status` `open` | **`open -> valid_to: null`.** The lying record: `status: open` with `valid_to: "commit:…"` VALIDATED (constructed; mutant `binding.open-with-valid_to`). An open binding carrying an end instant is a closed binding wearing open's label — the exact mirror of DT-4 (`closed -> valid_to nonempty`), which only bound one direction. §3.5 already says `disputed` MAY carry `valid_to: null`, i.e. the doctrine treats a null end as the open-interval carrier; the schema now says so for `open`. Survives R2-2: status becomes a projection, and a projection that reads `open` while its interval has an end is a contradiction the ledger must also reject — the arm is the schema face of that invariant, not a mutable-status artifact. Owner: the writer. |
| 2 | `state_observation.failure_state` `partial` | **`partial -> evidence_refs REQUIRED`.** The lying record: `failure_state: partial` with the full fingerprint triple and NO evidence VALIDATED (constructed; mutant `observation.partial-no-warrant`) — byte-for-byte a record that could equally be an `observed` with nothing partial about it; the value asserts "I could not see all of it" and carries no warrant of WHAT it could not see. R2-5 gave `observed_absent` exactly this arm for exactly this reason ("absence-without-warrant is the unfalsifiable cell"); `partial` is the same cell one step over. The probe's NOTE that presence-keyed coupling "may already protect" the value is answered: the coupling binds the fingerprint TRIPLE (what was seen), never the warrant (what was not). Positive coverage: 15th fixture `state_observation_partial`. The new arm is require-only; its forbid-mirror question is ruled class A (evidence is monotone) in `ARM4_ADJUDICATION.md` in this same commit, so ARM 4 never prints it NEW. Owner: observer. |

## DEFERRED BY LANDED DESIGN — 1 (the ARM-4 class-D pattern; re-adjudicate iff R2-2 fails to land)

| # | field · value | ruling |
|---|---|---|
| 3 | `entity_binding.status` `disputed` | The attacked-dry R2-2 design (`R2_2_DERIVED_STATUS_DESIGN.md` @7c093caff5, CVO-CVR2-2b) makes contests their OWN record with a typed target `entity | binding`; the `disputed` overlay on the binding's status axis dissolves at the landing (checklist line c), so any arm cut on `disputed` today is reversed at the landing. Cutting a control scheduled for reversal is churn, not coverage. §3.5's carve-out (`disputed` MAY carry `valid_to: null`) stands until then. |

## NO — 10, each with the citation that makes the value free

| # | field · value | ruling |
|---|---|---|
| 4 | `bridge_assertion.claim_origin` `producer_declared` | NO. `ISCK_CONTRACT.md` §2 :81-82: "needs no external warrant by definition"; §3.1 arm table binds `independently_observed` / `rule_derived` / `model_inferred` only. The forbid direction (no evidence on a declaration) is anti-law — evidence is monotone (ARM-4 class A; DT~X 76651: "carrying MORE than required is not a lie"). No lying record exists: a producer declaration with or without evidence contradicts nothing. |
| 5 | `bridge_assertion.claim_origin` `human_adjudicated` | NO. §2 :82: "traced by the CVO rubric per the standing carry, not by schema". A require on `adjudicated_by` here would conflate ORIGIN (who asserted) with REGISTRY ADJUDICATION (who resolved a contest) — the one-field-two-intents defect DT-R2-6 just retired. Re-open only if the rubric carry is discharged into schema, and then on `claim_origin`'s own field, never on `adjudicated_by`. |
| 6 | `bridge_assertion.verification_standing` `unverified` | NO. §2 :83 "the honest free cell"; §3.14 :255 "FREE OF REQUIRED WARRANTS by design — no arm may DEMAND evidence … from a seat that has not checked"; ARM-4 CUT-4's lesson (FREE means free of REQUIRED warrants, not of forbids) is already enforced on the one forbid that applies (`unverified -> delta_summary forbidden` lives on `coherence_evaluation.integrity`, not here). |
| 7 | `coherence_evaluation.currency` `unknown` | NO. §3.14 :249-250 and :255 verbatim: `unknown` "by resolving the target — evaluator" and "`unknown`/`unverified` FREE OF REQUIRED WARRANTS by design". A forbid of `delta_summary` on currency `unknown` would be keyed on the wrong axis: the delta is integrity's product and ARM-4 CUT #4 already forbids it on `integrity verified\|unverified`. |
| 8 | `entity_binding.binding_basis` `producer_declared` | NO — same citation as #4; §3.1 :99-100 makes the arm table bind EVERY consumer of the enum identically (R2-3), so the disposition propagates by the same rule the arm does. |
| 9 | `entity_binding.binding_basis` `human_adjudicated` | NO — same citation as #5, propagated per §3.1 :99-100. |
| 10 | `identity_relation.claim_origin` `producer_declared` | NO — same citation as #4, propagated per §3.1 :99-100. |
| 11 | `identity_relation.claim_origin` `human_adjudicated` | NO — same citation as #5, propagated per §3.1 :99-100. |
| 12 | `materializer.current_status` `retired` | NO. §3.8 :198 "`retired` by decommission (owner)" — terminal, no successor obligation (a retired materializer has NO successor version by definition, so neither `superseded_by_version` REQUIRED nor FORBIDDEN is a lying-record test: DT~X 76651 rated retired-with-successor "arguably coherent (retired for one reason, replaced by another)" and kept it BY DESIGN). Under R2-2, `current_status` becomes a projection of lifecycle events; `retired` is then derived, not asserted, and the arm question moves to the ledger. |
| 13 | `mint_receipt.collision_preflight` `deferred_to_reconciliation` | NO. §3.18 :307 verbatim: "`deferred` needs no warrant (the deferral IS the honest state, and the reconciliation record carries its own)". The forbid direction (no evidence on a deferral) is class-A anti-law. |

## Post-R2-2 landing re-run (2026-08-28, same day)

ARM 1 at the landing tree: **8 gap fields, the same eight** (rows 4–13 above; `entity_binding.status`
now 2 of 3 reached with `disputed` the deferred remainder). The landing's new enums arrive with
their conditionals reaching EVERY value by construction — `event_kind` 2 of 2, `target_kind` 2 of
2, `outcome` 3 of 3 (`merged` REQUIRES `consequence_refs` like `upheld`, per §3.21's own sentence
— caught by this re-run as a 9th gap and cut in the landing commit, mutant
`contest.merged-without-consequence`); `recoverability` and `status_basis` carry no conditional and
are NOT EXAMINED by ARM 1 (declared, §6 — `status_basis` is a `const`, not a discriminant). No new
candidate survives.

## What this record does NOT claim

- It does not claim the 8 fields ARM 1 will keep printing are "covered" — they are UNREACHED BY
  A VALUE-KEYED CONDITIONAL and adjudicated free. Coverage and freedom are different words.
- It does not claim `source_frontier` / `surface_version` are clean — ARM 1 is structurally blind
  to them (no discriminant), and they are Round 3's named targets (memo §7; C3 verdict).
- Two seats have not yet read this record. `0.4.0_DT_ClientPlatform~X` (the probe's owner) and
  `3.0.0_SA_CVO~X` re-verify at the commit; a NO overturned by a constructed lying record re-opens
  the row by id.
