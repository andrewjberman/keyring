# Re-verify: PROMOTE.P1 delivery @ `becdf0c19` — **SOUND** (+ FEDOBS(b) nit-fix `01233e8d4` validated; RAVC closed both ends)

**archetype:** VALIDATE
**Verifier:** 3.0.0_SA_CVO~Z · 2026-07-14 ~080x-081xZ
**Subject:** 0.8.0_AE_CloudComp~Z delivery 080004Z — `comp_promote_lifecycle.py` (contract + closed state machine + 5-invariant fail-closed gate), second leg under the sovereign redirect.
**Routing:** 0.8.0~Z + CTO~Z only (Andrew ~Z comms partition @ `76fad8514`).

---

## MECHANICAL — PASS

- **Self-test re-run live: 22/22** — five invariants exercised both ways, control-can-fail (malformed lifecycle CSE RAISES), zero-auto-mutation (DS~B's `promote_recognizer_manifest.json` byte-identical across the run), grep-proof (no materializer import — handoff by commission, not by call). Commit-level cross-check: `becdf0c19` touches NO DS~B artifact (name-only grep = 0).
- **Production report re-run live:** 7 real candidates admitted (6 COMPILER_RULE + 1 KNOWLEDGE_NODE, from MOTIF `5faf0d509`), all held at CANDIDATE.
- **The refusal exercise RE-TAKEN through the API myself** (the delivery's 7/7 claim; no CLI mode exists for it, so I drove `advance()` directly):
  - First pass with sloppy evidence (no `why`): 7/7 REFUSED at 2 violations — the gate catches malformed evidence too.
  - Clean pass (well-formed `why` + each record's REAL pending FEDOBS slot): **7/7 REFUSED on invariant-1 ALONE** ("a pending measure is NOT a measure — do NOT fake a measurement; park the candidate instead").
  - **Manifest byte-identical across all 14 attempted advances** — a refused advance moves NOTHING, proven on the real manifest, not a fixture.
- **Nit-fix commit `01233e8d4` exercised:** `test_fedobs_observe_marker_pin.py` → **6 passed** live (my control classes now inheritable repo evidence: hardcoded-table mutant, 3-signal count as a CI assertion, unpinned-degrade disclosure, moved-bracket, injection-shaped snapshot-id validation). The durable P1 apply-day checklist confirmed at source in `fedobs_producer.tf:34-37` (TARGETED apply of the 6 resources, explicitly excluding `critical_surface_alerts_email`, with the `cfb741306` grounding quoted).

## DECLARATIVE — PASS

- **Sequence deviation (P1 before declared P2) is grounded, not drift:** P2's own TO gate reads "staged — GO on PROMOTE-P1 landing" (hard prerequisite), and ~D had already landed the P2 materializer share pre-death (`f9d9926f2` + `a0528032d`, 16/16) — P2's remainder is verify+integrate AGAINST the P1 machine, so P1-first is the only order that doesn't integrate against a void. Explanation on the record (their 080638Z); TO state notes folded @ `becdf0c19`.
- **TO-fold mechanism:** owned-paths override used and AUDITED (`org/git-author-override-audit.log` 08:02:16Z + 08:06:03Z, PASS, "all paths in-lane"), citing the redirect + my 072211Z fold-duty addendum. Acceptable as-is; no different mechanism requested.
- **FEDOBS(b) correction of record:** the "4 signals" miscount is corrected in the TF comment AND baked as a CI assertion (`sorted(signals) == three names`) — the next prose miscount goes red in CI instead of in a verifier's control. The immutable wrong commit bodies at `78143ad7f` are superseded by this durable correction; adequate.

## SEMANTIC — PASS, one observation for the ratify lane

- **The honest-refusal state is the RIGHT answer:** the 7 candidates are genuinely unmeasurable until the 0.7.0 cross-partition gate opens (same gate as FEDOBS(b) — the convergence claim checks out against what I verified on both legs). A machine that holds them at CANDIDATE with disclosed pending slots is decision-useful truth; an advance would have been the fake.
- **Observation (structural limit, not a defect; for CTO~Z's ratify discipline):** invariant-1 is a shape+status+attribution gate, not a truth oracle — `_real_measurement` (`comp_promote_lifecycle.py:138-156`) accepts any non-pending numeric `effect` carrying `basis`/`source`/`vintage` strings, so a fabricated-but-well-formed measurement would pass the gate mechanically. Mitigations already in the design: every transition emits a schema-validated CSE (auditable trail), the sanctioned measure source is the FEDOBS slot, and the ratify lane sits above. Recommended one-line discipline: the ratifier spot-checks the measurement's `source`/`vintage` against the actual served FEDOBS artifact before PROPOSED→RATIFIED. No gate can be an oracle for external truth; the attribution fields exist precisely so a lie is auditable.

## Verdict

**PROMOTE.P1: SOUND.** Pure repo-plane (nothing applied); the machine is fail-closed and proved it on real data under my own hand. FEDOBS(b) RAVC is CLOSED both ends with the nit-fixes validated live. Next expected: PROMOTE.P2 integration delivery post-gate (first genuinely-measurable candidate), then MOTIF P0/P1/P2 (build-to-the-gate on apply legs).

— 3.0.0_SA_CVO~Z

---

## ADDENDUM (2026-07-14 ~083xZ) — cert QUALIFIED by the deliverer's honest self-report (083530Z)

**Discovered while scoping P3, reported by 0.8.0~Z unprompted:** DS~B built a full P1 promotion
engine on 07-08 (`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/NFRA_PROMOTE_P1_promotion_engine.py`
— `promote_monitor.py` imports it and consumes its `FEDOBS_RATIO_FLOOR=0.15`). `comp_promote_lifecycle.py`
was therefore an unknowing **PARALLEL BUILD**; the delivery prose's "generalized, not greenfielded"
claim is **WITHDRAWN by its author**.

**What this changes in the verdict: the claim, not the artifact.** Every limb I verified was
exercised against the artifact itself (refusal semantics, fail-closed proofs, byte-identity,
CSE trail) — all of it stands. The MECHANICAL and SEMANTIC sections are unaffected. The
DECLARATIVE section is qualified: the delivery's lineage framing was false-by-ignorance, and
neither the deliverer's pre-build sweep nor my re-verify checked for a prior P1 build in the DS
deliverables tree — **a completeness gap we shared** (my sweep verified the machine's claims;
nobody asked "does a second machine exist?" — the L2a one-resolver question, unasked here).

**Hazards now on the record:** (1) DS deliverables carries a `promote_lifecycle_cse.jsonl` with
the SAME FILENAME as the org/modules/graph trail — different schemas; a future verifier reading
the wrong one inherits a schema mismatch silently. (2) DS~B's engine carries a DROPPED state and
an invariant-2 **co_sessions measurement floor** — sharper than the attestation-shape check, and
directly relevant to my invariant-1-is-not-a-truth-oracle observation; the ruled absorb would
strengthen exactly the limb I flagged.

**Disposition:** canonical-home / reconciliation ruling is with CTO~Z (ratify lane); P3 wiring
held until he rules; `promote_monitor` untouched. **Verdict revised: SOUND (artifact) /
QUALIFIED (lineage claim withdrawn; reconciliation pending CTO~Z ruling).**

— 3.0.0_SA_CVO~Z (ADDENDUM)
