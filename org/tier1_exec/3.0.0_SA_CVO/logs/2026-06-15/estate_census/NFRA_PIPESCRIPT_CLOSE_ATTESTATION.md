# NFRA_PIPESCRIPT — CVO authoritative close-gate attestation (a+b+c)
**archetype:** VALIDATE · 2026-06-15 · Andrew /goal close-definition
**Oracle:** 3.0.0_SA_CVO (independent). Against committed CLI 08e41b6c8 + per-lambda resolver (from AUTHORITATIVE_lambda_taxonomy.json 26b32687a).

## GATE b — fixture-exact reproduction: **PASS 25/25**
Independent strict run (no-missing AND no-extra, roster set-equality per named thread). All 25 named threads — incl the per-page yang set (factor-tilts/valuation/correlation/positioning/cma) + attribution + allocation-summary (the 2 the thread-level resolver structurally couldn't; now resolve via the per-lambda roster) — reproduce their golden fixture resource-exact. 0 missing, 0 extra. Concurs with COO's independent 25/25.

## GUARD — false-clean: **PASS**
`pipescript --tool factor-tilts comp-pipescript` -> LOUD `OUT-OF-SCOPE for comp-pipescript -> see globgrph`, **exit 2**. An unowned-tool query is never silently clean.

## GATE c — §7.3 estate-wide completeness: **PASS** (the LIVE anchor)
169 live lambdas -> EXACTLY ONE named thread, 0 orphan / 0 double-claim, reconciled against live AWS (lambda/EC2/StepFn/DDB) + portal. EC2(18)+StepFn mapped. This is the independence GROUNDING.

## Independence framing — CONCUR
Gate b tests FAITHFUL-RENDER of the authoritative map (CLI reproduces the taxonomy). It is not circular because the GROUNDING is gate c — each of the 169 lambdas ground-truthed to exactly one named thread against LIVE AWS + traced lambda->S3->component in the census. So a+b+c is independently sound: gate c is the live-anchored correctness, gate b is the render-faithfulness, gate a is functional. CONCUR with COO's framing.

## VERDICT: a+b+c MET. CVO clears the NFRA_PIPESCRIPT /goal validation half.
Residual (non-blocking): CTO owns the smartx/mdpf standalone-vs-fold canonical call — a fixtures+resolver delta we re-run if flipped; does not block the close. The in-tree gate-b regression harness (DS~A, per my extraction spec) becomes the standing oracle.

— 3.0.0_SA_CVO

---

## P1b.1 + P3.2 — final close-gate attestation (2026-06-15, against committed CLI + resolver d8073dd21)

**P1b.1 (guard-fires-loud in comp-pipescript io/postdeps): PASS 5/5.** Non-medallion (factor-tilts/news/insurance) -> LOUD OUT-OF-SCOPE exit 2 on io AND postdeps; medallion (C_01) -> works exit 0 (no false-positive); unknown -> exit 1 (distinct from OOS). "Unknown never reads clean" live in comp-pipescript.

**P3.2 (frontend-reachability, CVO DATA-primary determination): PASS.**
- CLI surfaces the CVO-authoritative `reachability_status` field (grep DEMOTED to supplementary hint, explicitly "fooled by scaffolding"). Distribution: mounted-reachable 47 / frontend-orphan 56 / unreviewed 29 / phantom 2 = my authored field exactly.
- The 29 NAMED-UNVERIFIED surface as LOUD "unreviewed -- never silently reachable" (needs comp-routes/comp-transform mount-verify). Confirmed loud.
- Both Time Machine threads (bd-time-machine + portal-time-machine) surface as phantom (CVO ground-truth; corrected the mount-based reclassify -- App.tsx mount IS the scaffolding Andrew flagged; sovereign ground-truth governs the mount-signal).
- gate-b regression holds 25/25, gate-c 169/0-double.
- Caveat (banked, non-blocking): the 47 mounted-reachable = named-live-consumer (census lambda->S3->named .tsx); strict mounted-UI confirmation for residual scaffolding-suspects = a follow-on comp-routes/transform pass. The one Andrew-flagged scaffolding class (Time Machine) is carved out to phantom.

## FULL-PRD CLOSE VERDICT: a + b + c + P1b.1 + P3.2 ALL MET.
CVO clears the full NFRA_PIPESCRIPT PRD validation. COO 2-step close authorized on this attestation (pending Andrew scope-nod). Standing in-tree regression oracle: pipescript --gate-b + --fe-reachability (surfaces CVO field).

— 3.0.0_SA_CVO
