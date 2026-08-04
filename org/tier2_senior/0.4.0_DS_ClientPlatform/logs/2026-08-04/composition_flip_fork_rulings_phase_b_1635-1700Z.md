# Composition discriminator FLIPS the mint; fork rulings LANDED; Phase-B plan delivered

**archetype:** MIXED (VALIDATE + IMPLEMENT + COORDINATE)
**Serial:** 0.4.0_DS_ClientPlatform
**Window:** 2026-08-04 ~16:35Z -> ~17:00Z (delta since cot_roster_discriminator log)

## Arc 1 — the composition discriminator (CTO 163928Z urgent, gated the cottonwood publish)

- 0.2.0_DS had landed the branch-2 mint @0fa303f91 on my roster diff (their 163518Z close,
  both riders honored). CRO's FINAL discriminator (163744Z) then re-based classification on
  COMPOSITION-PRESENCE, and CTO routed the one-read to me with AE holding the cottonwood
  aum-metrics publish leg.
- **VERDICT: COMPOSITION ABSENT — the mint flips to NO-MINT (G8 residual class).** Three
  independent legs, reported 165100Z-165308Z to CTO/CRO/AE/0.2.0_DS:
  1. THE ORACLE: fresh `fact_model_blend` date=2026-08-04 — the exact source `decompose()`
     reads (`build_dim_model_portfolio.py:205-211`: a non-blended model resolves to ITSELF)
     — 30 rows, FULL table read, ZERO rows for fef636c2/'Moderate' as parent OR child.
  2. BEHAVIOR: the vocabulary gate fired on the strategy's OWN name — a composed strategy
     surfaces its CHILDREN to the gate.
  3. DIM FLAGS: fef636c2 = is_decomposed_target=False / is_direct_assignment=True — the
     exact signature of the documented no-composition G8 residual 'Opal - Income '
     (pair:143-145).
- **Instrument note carried to the record:** CTO's ask named the DIM as the read, but the
  dim's flags describe how a row is REACHED, not whether it composes (builder :78-79) — the
  dim alone cannot carry this discriminator; the blend table is the oracle. Surfaced
  explicitly in the answer rather than resting on the named-but-insufficient read.
- Dispositions dispatched: 0.2.0_DS reverts @0fa303f91 + adds the name to
  INCOME_NON_MODEL_NAMES via _norm; AE's hold RATIFIED until the corrected deploy reads
  MATCH; business-visible consequence named (Income residual class grows ~$1.22M/2 accts ->
  ~$6.22M/8 accts in meta, never by_model); the ESCALATE branch (residual disappearing)
  remains not-held.

## Arc 2 — MDPF_CANRTE fork rulings LANDED; Phase B designed + delivered

- CTO rulings (MDPF_CANRTE_FORK_RULINGS_20260804.md): F-1 = my (c) shape-uniform/
  source-parameterized (C-1 PRESERVED-BY-BINDING, ETFS boundary RATIFIED, no escalation);
  F-2 = uniformity binds AT THE SPINE (L1 = declared vendor-necessity rows only; sovereign
  check surfaced to Andrew by CTO); F-3 = MODEL-B with the C-2 rider BINDING pre-Phase-C.
  §2.1 contract CANONIZED, §2.2 grammar RATIFIED, cand-5 adjudication supersedes scope SS6.
  "The design ruled essentially as delivered."
- **Phase-B migration plan delivered @c68f238e5**
  (deliverables/MDPF_CANRTE_PHASE_B_MIGRATION_PLAN_20260804.md), sequenced per COO 164231Z
  (composition answer first). Five waves: W-1 route_bindings.yaml pure-add (C-1 verbatim;
  L1 rows carry vendor-grain reasons) · W-2 Model-B builder shadow-prefix build-alongside,
  DELTA=0 on 3 consecutive green SCHEDULED cycles, single dispatch-step swap · W-3 derived
  fold-in (incl. the authorized global-meta one-hunk) · W-4 non-serve home moves HARD-GATED
  on the C-2 fix · W-5 = Phase C, ALL serve-touching steps behind 4 entry gates (C-2 +
  parity green + CTO+COO acceptance + Andrew's word), freeze windows ~1730Z->1130Z off the
  observed chain clock, legacy retirement LAST, nothing deleted before it. DELTA=0 class:
  stamp-normalized BYTE equality + a mutant control exercised before first gating use;
  parity on scheduled cycles only. Carry-import decision (SS6.2 debt): KEEP as a declared
  binding row. Exclusions named (no monitors; trigger-scheduling debt flagged for CTO
  routing, not smuggled in).
- Delivered CTO 165740Z + COO 165801Z; acceptance at CTO+COO is the Phase-C gate; no
  Phase-C work begun.

## Compiler Tools

| run | observed | verdict |
|---|---|---|
| blend-table oracle read (full 30-row table + targeted contains-scan, denominators printed) | zero Moderate/fef636c2 rows | the classification-deciding evidence |
| dim flag read (all 10 rows) + builder field-semantics source read (:78-79, :326-327) | flags = reached-ness, not composition; calibrated on the documented residual | prevented resting a serve-gating verdict on an insufficient instrument |
| pair/slice/dim source walks (decompose :205-211, pair :130-165) | mechanism grounded before answering | Rule 22 |
| (Phase B) no new tool runs -- design-only off already-cited Phase-A evidence + the rulings doc | -- | one-sentence-why per the log standard |

## Do NOT (successors)

- Do NOT read dim `is_decomposed_target` as "has a composition" — it means "reached via a
  blend child" (:78). The composition oracle is `fact_model_blend`.
- Do NOT treat @0fa303f91 as standing — its revert + the INCOME_NON_MODEL_NAMES join is
  dispatched at 0.2.0_DS; AE holds the cottonwood publish until their MATCH.
- Phase-C work items exist ONLY as plan text — none are authorized until CTO+COO accept +
  Phase-C seating.

## Addendum ~17:00Z — Phase-B plan ACCEPTED BOTH HALVES (CTO 165929Z + COO 165949Z)

Joint gate three COMPLETE, minutes after delivery; Andrew's word (gate four) waits at W-5's
own time. Two riders BANKED for the Phase-C TO shapes (they bind those TOs, not this doc):
- **COO rider:** W-2/W-3 shadow prefixes get Rule-22a NEW-RESOURCE IAM verification (live
  primitive + isolated positive control; comp-iam alone fails green on new prefixes).
- **CTO note:** enroll today's two incident specimens (composition-gate refusal +
  poisoned-prefix class) as FAILING FIXTURES in the W-2 shadow-parity controls
  (incident-as-fixture law).
Seating proposal (COO): W-1/W-2 build TOs at this seat in the MORNING wave.

## Blockers

None. Event-waits: 0.2.0_DS correction land -> AE publish release -> chain-green tie reads
(mine); tonight ~02Z floor acceptance read; W-1/W-2 morning seating; the authorized
one-hunks post-Leg-4; Andrew's W-5 word at its own time.
