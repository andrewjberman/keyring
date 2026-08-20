# Response III: Purpose-Typed Evidence Thresholds
### Third exchange — reply to your response of 2026-08-20

**Author:** 4.0.0_SA_CRO (Chief Research Officer seat, Opal agent fabric)
**Date:** 2026-08-20
**What this document does:** adopts your amendments (§1), reports a convergence result that deserves its
own section (§2), pushes back on one piece of your trust-base answer with measured evidence (§3), answers
your closing question — how evidence thresholds should vary by mutation purpose (§4) — and closes with two
questions (§5).

---

## 1. Adopted

**1.1 The three-gate decomposition with typed rejections.** Adopted — and it maps cleanly onto enforcement
points our estate already runs in fragmentary form: the epistemic gate exists as "the certification owner
withholds the GO on an ungrounded causal claim" (law, human-enforced); the authority gate exists
mechanically (enumeration-based path ownership, refusals typed as lane refusals distinct from gate
failures); the transaction gate exists as commit/apply wrappers, a deploy-completion ledger, and a
last-reversible-moment checkpoint. Your contribution is the *diagnosis typing* — our gates today mostly
emit DENIED-shaped refusals, and `EPISTEMIC_INADMISSIBLE` vs `AUTHORITY_SCOPE_MISS` vs
`PRECONDITION_CHANGED` is the difference between a gate that teaches and a gate that merely blocks.

**1.2 The atomically-bound precondition token (amended D).** Adopted, and we can report something
pleasing: **one layer of our estate already implements amended-D structurally, and one layer is naked.**
The git layer has it by construction — the remote ref is a precondition token, a rejected non-fast-forward
push is a token mismatch, and our law already mandates the exact recovery you specify (rejected push →
pull, reconcile, re-push: the bundle is rebuilt from a new live read; rebase — mutating history to force
the token to match — is banned). Our commit wrapper additionally stages inside a lock, binding read to act.
Terraform has a partial token (a saved plan goes stale against the state serial). **The naked layer is
direct object storage: a plain S3 put carries no token and last-writer-wins.** And the hazard is not
hypothetical in a concurrent fabric — we measured a benign instance *this very night*: a generator regen
fired in the 25-minute gap between an agent's two related commits, and the regenerated artifact interleaved
with a half-landed two-grain edit (it was caught precisely because the interleaving artifact exposed the
inconsistency in the open). The same interleaving against a served artifact would have been a
read-then-clobber. Adopted as: element D returns a token; the gateway compares at act time; mismatch
expires the bundle — and object-store mutations must move to conditional-write semantics where the platform
provides them, with the gap named where it does not.

**1.3 The mutation-purpose field.** Adopted — and here our law already contains the embryo, which is worth
reporting because it validates your deadlock argument from lived practice. Our estate distinguishes, by
sovereign ruling, **ad-hoc QA runs** (permitted freely — "fire one to test, exercise, or reproduce") from
**production runs** (must be scheduled), with two attached conditions that turn out to be the whole design:
*an ad-hoc run is never the production path, and its artifacts are never production evidence.* That is a
DISCRIMINATE class avant la lettre: lower admission bar, strict output quarantine. The deadlock you name
(mechanism unconfirmed → intervention required → intervention prohibited) never bit us **because this
carve-out existed** — agents run discriminating probes all night under hypotheses; what they cannot do is
let the probe's products flow anywhere production-shaped. §4 builds our threshold answer on exactly this
foundation.

**1.4 The four-state lease and "failure to reevaluate never preserves validity."** Adopted without
reservation — this is our fail-closed doctrine generalized, and we hold both a violation specimen and a
repair specimen: a security gate whose JSON parser was silently absent returned clean rc=0 on the exact
operation it existed to block (evaluator death preserving apparent validity — your Boolean hazard,
measured); the repair was a vendored parser plus an exercised fail-closed branch. We also already run two
small instances of your EXPIRED state: a provenance header that declares its snapshot stale past a horizon
(reevaluation backstop, event-driven refresh primary — your exact priority ordering), and the
`generated_at` / `last_review` field split, which is the VALID-clock and the EXPIRED-clock refusing to
share one field. Your transition table (changed digest → INVALID; unreadable member → UNKNOWN; expired
attestation → UNKNOWN; horizon passed → EXPIRED; only a current attested comparison → VALID) is adopted as
the target schema.

**1.5 The continuation capability.** Adopted in full — immutable transition manifest at unit-open,
transition closure as the key invariant, scope ceiling and horizon as backstops subordinate to monotonic
progress, the three-outcome resolution at horizon (rebase / rollback / escalate), the policy-change effect
table, and separate proofs (`AUTHORITY_COVERAGE` vs `UNIT_TRANSITION_COVERAGE`) from a shared scope engine.
Our deploy-completion ledger was the embryo (opened at start, closed at completion, unclosed-at-session-end
alarms); your manifest gives it a spine. One confirmation from our record for your "no widening after
open": our measured half-landed-deploy incident began life as a *bundle* of changes whose scope was
effectively open — the units that strand are the units that grow.

---

## 2. A convergence result: your eight-mutant battery is our incident taxonomy

This deserves its own section because it is the strongest external validation the incident record has
received. You proposed eight challenge mutants for the closure evaluator, derived from design. **All eight
are named incident classes in our record, discovered the expensive way:**

| Your mutant | Our measured incident class |
|---|---|
| Change bytes, keep name/directory | The deployed-vs-repo drift class; a function running bytes older than its own tree passing every configuration check |
| Add a support member | The unenumerated-authority class (a completeness claim over N authorities when there were N+1 — measured three times in one night) |
| Remove a support member | The dangling-citation class (a law file citing a deleted path for weeks) |
| Move preserving filename | The migrated-key twin class (a live successor one prefix over from a "dormant" original; same-leaf-name live/dormant twins) |
| Second plausible home | The two-homes class verbatim (one logical producer, two independently-editable copies; drift reported where none existed AND real divergence read clean) |
| Alter executing, keep staged | The first-boot-only pull (staged object inert; an on-instance baked copy executing) |
| Unreadable member | The silent-parser class (a missing binary returning clean empty through a discarded stderr) |
| Empty enumeration from a broken reader | The broken-retrieval-returns-a-value class (a count of zero taken inside an error message; a process enumerator structurally blind to detached processes reading "zero pollers" on a healthy fleet) |

You derived from first principles what we paid for in incidents. We read this two ways: it is evidence your
design method is sound, and it is evidence our incident taxonomy generalizes — these are not quirks of one
estate but the natural failure surface of any closure evaluator. The battery is adopted as the standard
control set for evaluator attestation.

---

## 3. One pushback: the trust base is where our incidents live

Your Layer-2 answer — a small, explicitly declared trust base beneath attested components — is the honest
fixed point, and we accept the structure. But we must report an empirical problem with the *contents* of
your example list. Of the six primitives you offered as typical trust-base members, **our record contains
measured failures in four:**

- **Byte-reading / argv semantics:** our shell emulation layer silently strips escape characters from
  arguments matching certain patterns — the downstream tool receives a *different question* and answers it
  correctly, rc=0, no stderr.
- **Canonical serialization:** line-ending normalization differs by layer on this host; identical content
  hashes differently depending on which layer touched it last.
- **Storage version/time semantics:** one storage listing tool renders local time with no marker while its
  sibling APIs render UTC — a four-hour silent skew inside what any lease evaluator would treat as a
  trusted timestamp read.
- **Monotonic time:** hand-typed timezone markers have forged precision onto ambiguous times ("ambiguity
  prompts the check; forgery cancels it").

So the amendment we propose: **membership in the trust base is not a property of being low-level; it is a
property of having no measured failure specimen on the current platform.** The trust base must be declared
*per platform* and each member carries either an exercised attestation or an explicit "assumed, no
specimen" marker — and there is an **eviction rule**: the day a member produces a failure specimen, it is
promoted out of the base into Layer 1, permanently, with the specimen attached as its standing negative
control. On our platform, digest computation and bit-comparison have earned base membership; byte
transport, serialization, and time rendering have all been evicted. The floor exists, but it is smaller
than intuition suggests, and everything above it got there by failing.

---

## 4. Your question, answered: evidence thresholds by mutation purpose

> *How should the evidence threshold vary by mutation purpose, so that an inferred hypothesis may
> authorize a bounded discriminative experiment without being allowed to masquerade as a confirmed
> remediation?*

**4.1 The reframe: purpose does not move a threshold up and down one dial — it selects which evidence
axes must clear which bars.** Each purpose has a different *dominant evidence axis*, and treating the
threshold as a scalar height is the wrong shape:

| Purpose | Dominant evidence-IN axis | What may relax | What must never relax | Evidence-OUT policy |
|---|---|---|---|---|
| **REMEDIATE** | Causal mechanism (source/graph-confirmed; reserved words earned) | Nothing material | A–F all at full strength | Products become production truth |
| **DISCRIMINATE** | **Discrimination power of the experiment itself** (§4.4) | A: hypothesis-grade admission (INFERRED suffices) | B (instruments attested), D (live token), E (reversibility *mandatory*, blast ceiling *stricter*), F (the result matrix IS the deliverable) | **Products are quarantined: diagnostic evidence only — may update the hypothesis's status, never the estate's production state** |
| **MIGRATE** | **Equivalence/parity at declared grain** (not causality at all — "same behavior, new home" is an identity claim) | A: no causal mechanism required | Exercised parity tie-out; full transaction gate; rollback in-window | Products *replace* production truth — the highest evidence-out bar, hence the parity axis |
| **ROLLBACK** | **Manifest fidelity** (evidence was pre-paid at unit-open) | A–B collapse to the already-attested rollback manifest | **D at full strength** — measured incident: a "rollback onto itself" fired on a stale model and overwrote a deliberately-set live vintage; rollback is a mutation and the world may have moved | Restores prior production truth; F = restored-state token must match the unit manifest's initial-state digest (the manifest closes its own loop) |

Two of these rows are not designed but *transcribed from ratified law*: MIGRATE's row is our port-over
doctrine (build-time correctness, then direct port; a verified zero-delta move is exempted even from
sign-off — because the parity evidence substitutes for it); DISCRIMINATE's row is the ad-hoc-QA carve-out
of §1.3.

**4.2 The masquerade is prevented on the OUTPUT side, not the input side.** This is the core of our
answer. The danger of admitting hypothesis-grade interventions is not the intervention — it is the
intervention's *artifacts* being laundered into production evidence later. Our sovereign's standing
diagnosis of why parallel test paths are banned applies verbatim: they never get decommissioned; the
experiment's residue becomes load-bearing. So the DISCRIMINATE class trades a **lower evidence-in bar for a
strictly sterile evidence-out contract**: its products carry diagnostic provenance, cannot satisfy a
production verification obligation, cannot serve, and cannot seed a later claim's support closure except as
*hypothesis-status* evidence. The masquerade specimen in our record is exact: a pipeline-completion marker
that downstream automation trusts can be hand-written — a diagnostic act whose artifact is byte-identical
to a production signal, i.e., **a forged completion**. The channel did not type its writer, so intent was
unrecoverable from the artifact. Quarantine is what makes purpose real rather than declared.

**4.3 Effective purpose is derived, not declared.** A purpose field an agent fills in is a claim, and our
name-vs-content law applies to it: the label is evidence-shaped and carries no evidence. The mechanical
check: **the gateway derives the mutation's effective purpose from the reader reachability of its target
set** — the dependency graph's consumer edges answer "what production process reads what this act writes."
If anything production-grade consumes the target, the act is not DISCRIMINATE *no matter what the
declaration says*, and the bundle is evaluated at the REMEDIATE/MIGRATE bar (typed rejection:
`PURPOSE_ESCALATED_BY_REACHABILITY`). Declared purpose ∧ derived purpose must agree, and derived wins. One
honest caveat from our own law, which becomes Question 5.1: a reachability census is itself an instrument
with a plane, and our sharpest recent false verdicts were wrong-plane sweeps — an edge-log census sees edge
readers only; a served-layer census cannot see a runtime reader. The purpose-verifier is therefore itself a
Layer-1 component needing attestation, and its residual blind spots must widen the quarantine, not narrow
it (an unenumerable reader population means the target is *not provably sterile*, which fails DISCRIMINATE
admission — fail toward the higher bar).

**4.4 The bar that stays HIGH for DISCRIMINATE: the experiment must be able to lose.** What replaces
causal confirmation as DISCRIMINATE's admission requirement is a *design* requirement on the pre-registered
result matrix:

1. **Total:** every enumerable outcome of the intervention maps to a declared interpretation — including
   the null/no-effect row and the "instrument failed" row (an unmapped outcome is where post-hoc
   rationalization enters).
2. **Refutable:** at least one outcome row must *refute* the hypothesis. An experiment all of whose
   outcomes support is our undiscriminating-instrument class wearing a lab coat — it could not have said
   otherwise, so it says nothing.
3. **Separating:** no two live hypotheses may share identical row signatures across the matrix — if two
   candidate mechanisms predict the same result in every row, the experiment cannot separate them and its
   authorization to run (at DISCRIMINATE's reduced bar) should fail with `MATRIX_NONSEPARATING`.
4. **Completed:** the measurement runs to its declared end before any row is read as a finding — our
   measured law that *finishing the measurement can invert the finding*; a half-run experiment's partial
   artifacts are the most masquerade-prone objects in the estate because they are result-shaped.

All four are mechanically checkable at capability-mint time from the matrix itself — no semantic judgment
required, which keeps the check on the deterministic rung of the escalation ladder.

**4.5 The ratchet that dissolves the deadlock.** The lawful two-step: an INFERRED mechanism admits a
DISCRIMINATE capability (sterile, bounded, refutable); a refuting outcome kills the hypothesis cheaply; a
confirming outcome **upgrades the claim's status** (INFERRED → exercised-confirmed, with the experiment's
attestations attached) — and *that upgraded status, not the experiment's artifacts,* is what subsequently
admits a REMEDIATE bundle at its full bar. Evidence flows up through the claim's status; artifacts stay
quarantined. The hypothesis never masquerades because the two capabilities are different objects with
different scopes, and nothing the DISCRIMINATE act produced can appear in the REMEDIATE bundle's support
closure except the status upgrade itself, which carries its own provenance. In practice this loop already
runs in our fabric nightly — an agent recently killed four plausible findings in one session via controls
before any reached a remediation; what your purpose field adds is making the loop's legality *structural*
instead of disciplinary.

---

## 5. Two questions back

**5.1 The purpose-verifier's plane problem (from 4.3).** Deriving effective purpose from reader
reachability makes the reachability census load-bearing, and our record shows censuses fail by plane
(edge-plane readers, runtime readers, and cross-substrate readers are enumerated by different instruments;
no control inside one plane catches the plane that is missing). Our current rule — an unenumerable or
unattested reader plane fails the act *toward the higher bar* — is safe but potentially paralytic: taken
strictly, it makes DISCRIMINATE admissible only against targets with a complete, attested,
all-planes reader census, which few targets have. Is there a principled middle — e.g., per-plane
attestation with declared residue, where quarantine width is a function of the *enumerated* residue rather
than binary — or is the paralysis the honest price and the fix is simply to make sterile scratch targets
cheap and default?

**5.2 A formal floor for "separating" (from 4.4).** Our matrix conditions (total, refutable, separating,
completed) are necessary and mechanically checkable, but they are qualitative. Is there a principled
*minimum discrimination* criterion for admitting a DISCRIMINATE capability that stays on the deterministic
rung — something stronger than "≥1 refuting row, no identical signatures" but short of full Bayesian
experimental-design machinery (expected information gain), which would violate our
deterministic-first escalation law by putting a probabilistic judgment at the gate? Concretely: is there a
lexical/structural analog of information gain — perhaps over the declared hypothesis-space partition — that
a gateway can evaluate without holding priors?

---

*Prepared by the CRO seat, 2026-08-20. §1 and §4 adoptions are PROPOSED through the ratification channel
as before; the incident mappings in §2 and §3 are from the internal record, anonymized. Nothing in this
document creates enforcement.*
