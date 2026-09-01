# D2 (Advisor Intelligence) — MEMBER-SET STATE INDEX

**Author:** `4.0.0_SA_CRO~A` · **UTC:** 2026-09-01
**Authority:** Andrew-direct 2026-09-01, verbatim: *"take all the D2 projects and figure out where
we're at for all and build out proper briefs on state so we can address them one after another in
our new canonical workflow pattern."*

⛔ **THIS INDEX IS NOT A BRIEF AND `/endpoint --forward` MUST NOT BE POINTED AT IT.** Its consumer is
a person choosing what to work on next. Each project's brief is its own file, because
`/endpoint --forward` cuts outcomes from **one** brief at a time.

---

## 1. THE MEMBER SET — authoritative, from `org/missions/DIRECTIVES.yaml` D2

**Ten projects.** Two complete, eight active. (This matches `1.0.0_SA_CTO`'s independently measured
`COMPLETION: 2 of 10` at D2 drive tick 126.)

| # | project | state | brief |
|---|---|---|---|
| 1 | **ADVI_PERFRP** | active — **the purpose project**, live regression | `advi-perfrp-merge-forward-brief-20260901.md` |
| 2 | **ADVI_49F** | active — the canonical chain everything else runs inside | `advi-49f-state-brief-20260901.md` |
| 3 | **ADVI_BDPARITY** | active — the check-our-work harness | `advi-bdparity-state-brief-20260901.md` |
| 4 | **ADVI_INSURE** | active — backend near-live, frontend at zero | `advi-insure-state-brief-20260901.md` |
| 5 | **ADVI_STITCH** | active — Phase A landed, Phase B correctly not started | `advi-stitch-state-brief-20260901.md` |
| 6 | **ADVI_COTKEY** | active — investigation ANSWERED, remedy unscoped | `advi-cotkey-state-brief-20260901.md` |
| 7 | **ADVI_ROSTERCOLS** | active — PRD drafted 09-01, nothing scoped | `advi-rostercols-state-brief-20260901.md` |
| 8 | **OPAL_ADVIPOINTERS** | active — the pattern program; self-declared stale dates | `opal-advipointers-state-brief-20260901.md` |
| 9 | ADVI_49FSRC | **complete** (parked by Andrew's word: the 0824 union is OUT) | none — see §4 |
| 10 | ADVI_BDPLAT_RESTORE | **complete** (BP-1..BP-6 all PASS, closed 2026-08-19) | none — see §4 |

---

## 2. WHERE THE WHOLE DIRECTIVE ACTUALLY STANDS — one paragraph

**The 49F canonical chain is healthy and current** (8 gold tables, newest partition `date=2026-08-31`,
which is the correct as-of). **What is broken sits one layer above it**: the PERFRP projection stage
built 0 of 11 families on 2026-09-01 while fourteen other stages in the same run consumed the same —
richer — partition and wrote 30 objects. That regression is **live, uncaused, and nine hypotheses
deep.** Meanwhile **four of eleven PERFRP leaves are served**, and the L3 Performance card — the exact
grain on Andrew's original screenshot — is **not** one of them. INSURE's backend is a step from live
and its **frontend is at zero**. STITCH's Phase A is on the planes. COTKEY's answer is sitting in a
PRD with nothing scoped against it. **Nothing in D2 is blocked on knowledge; several things are
blocked on a decision or a scheduled fire.**

---

## 3. THE THREE FACTS THAT CUT ACROSS EVERY MEMBER

**(a) ⛔ A stage that produces nothing reports success.** `chain_49f_entrypoint.py` maps any emitter
failure to `emitter_refused`, excludes that from `hard_fail`, and puts no floor on `built`. Eleven
by-design refusals and total failure of all eleven print **byte-identical `STAGE OK rc=0`**. This is
why a four-day repeated as-of and then a full production stop were both invisible from any single
run. **It affects PERFRP, INSURE and ADVI_49F simultaneously**, because they all run as stages in one
chain.

**(b) ⛔ D2's purpose project does not follow D2's own ratified pattern, and the deviation is
undeclared.** `perfrp_emit_core.py:23-25` — *"this module has no S3 write path at all"*; a recursive
listing of `gold/advi/` for `perfrp` returns **zero objects**. The ratified spec requires gold output
to be parquet with the publisher as the estate's only JSON producer. PERFRP inverts it. Consequences:
the projection is unobservable after a run, a partner binding is against eleven scripts rather than a
table, and parity has nothing persisted to compare. **Owner: `OPAL_ADVIPOINTERS` / CTO architecture.**

**(c) ⛔ Four PRDs carry a superseded distribution restriction naming `4.0.0_SA_CRO`.**
`ADVI_PERFRP_PRD.md`, `ADVI_INSURE_PRD.md`, `ADVI_STITCH_PRD.md`, `ADVI_COTKEY_PRD.md` all read
*"nothing on this subject to `4.0.0_SA_CRO`"* (Andrew ~2026-08-24 16:1xZ), and the INSURE producer
lane reproduces it in every session-log header. Andrew's 2026-09-01 instruction to this seat
supersedes it **in fact**. **It is his to lift explicitly. No seat should infer the lift from these
briefs' existence** — and until it is lifted, every seat that reads those PRDs will keep routing
around the CRO.

---

## 4. THE TWO COMPLETE MEMBERS — why they got no brief

- **ADVI_49FSRC** — `status: complete`. Andrew's 2026-08-24 word took the 08242234 union **out**
  (*"the 08242234 union is NOT necessary; stitching happens against the BD legacy history"*), and
  the sourcing choices were held on Mike's confirmation. Its history section moved to `ADVI_STITCH`.
  **A brief would be briefing a closed decision.**
- **ADVI_BDPLAT_RESTORE** — `status: complete`, BP-1..BP-6 all PASS, closed 2026-08-19. Minted at
  true state 2026-08-25 because it had been a D2 member **with no project JSON**, which is why D2 was
  structurally unable to report its own completion. **The lesson is worth keeping even though the
  project is done: an unregistered member makes a directive unable to count itself.**

⚠ **Neither `complete` status was re-verified by this seat.** Both are taken from the register.

---

## 5. A SUGGESTED WORKING ORDER — reasoned, not a decomposition

Sequencing is COO's at step 5. This is a reading order for the briefs, with the reason attached, so
"one after another" has a defensible starting point.

1. **ADVI_PERFRP** — Andrew's stated #1 priority across all directives, and it carries the live
   regression. Its brief is already through step 1.
2. **ADVI_49F** — because fact (a) lives here and it is what made the PERFRP regression invisible.
   Fixing the observability is cheaper than diagnosing blind again.
3. **OPAL_ADVIPOINTERS** — because fact (b) is its call to make, and every other member's substrate
   question routes to it. Leaving it undeclared means the next partner is designed against a pattern
   nothing follows.
4. **ADVI_BDPARITY** — because it is one of Andrew's three named PERFRP acceptance axes and the
   estate is currently carrying a **false premise that parity is proven**.
5. **ADVI_INSURE** — Andrew ruled it distinctly lower priority than PERFRP; its next event is a
   scheduled fire, not a decision.
6. **ADVI_ROSTERCOLS** — cheap, visible to Andrew, and it has a live wrong-value trap (`custodian`
   declared as the data vendor) that will ship if someone sources it naively.
7. **ADVI_COTKEY** — the answer already exists; this is a decomp-and-decide, not an investigation.
8. **ADVI_STITCH** — correctly gated behind Fidelity; the near-term act is a census, not a build.

---

## 6. WHAT IS WAITING ON ANDREW ACROSS THE WHOLE DIRECTIVE

- **The PERFRP publish question** (reserved at 91668), two limbs: (a) did the 08-25 08:5xZ line narrow
  the 04:0xZ ratification, or answer the branch/PROD question only; **(b) is the attached condition
  per-family or per-set** — where per-set is unsatisfiable by construction, gated on a family that is
  a ruled deferral and will never emit.
- **The distribution restriction** naming `4.0.0_SA_CRO` in four PRDs (§3c).
- **`dim 436`** — a vendor template amendment, i.e. egress, reserved to his explicit per-use word.
  It is the sole remaining blocker on BDPARITY's T2-3.
- **The Since-Inception recommendation** — measured and recommended (cap at 1Y), not ruled.
- **The key of record for Cottonwood** — the one ruling COTKEY's PRD reserves.

---

## 7. WHAT THIS INDEX DOES NOT CLAIM

1. **No task order was read for any of the ten**, per Andrew's instruction and the midstream blind
   constraint. Nothing here says which TOs are KEEP / AMEND / RETIRE / ENDPOINT-INCOMPLETE.
2. **The two `complete` statuses are register reads, not verifications.**
3. **`OPAL_ADVIPOINTERS`' MDPF half is unexamined** — I scoped only its ADVI half.
4. **`D3_MODELOVERLAY` is out of scope** — it is D3's, not a D2 member, though COTKEY gates it.
5. **The per-project briefs carry their own limits**, and several are explicitly thinner-sourced —
   BDPARITY has no PRD of its own, ADVI_49F's registry entry is a defect list rather than a purpose,
   and COTKEY's Part IV is relayed rather than measured. **Read each brief's Part VII.**
6. **Status ages.** Every measurement here carries 2026-09-01 ~19:30–20:30Z.

---

## REFS

```
INDEX PATH     docs/briefs/d2-member-set-state-index-20260901.md
DIRECTIVE      D2 -- Advisor Intelligence (placement LAPTOP, one of six named laptop holds)
DIRECTIVE PRD  docs/architecture/D2_ADVI_49F_E2E_PRD.md
MEMBER SOURCE  org/missions/DIRECTIVES.yaml -> D2.members.projects (10 entries)
PRIOR ART      docs/briefs/d2-critical-path-sequencing-20260827.md (CTO, 08-27)
MEASURED AT    2026-09-01 ~19:30-20:30Z
```
