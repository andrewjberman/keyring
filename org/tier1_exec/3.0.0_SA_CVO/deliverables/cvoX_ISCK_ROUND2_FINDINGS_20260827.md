# CVO~X ISCK round-2 findings — independence-limit narrowing + R2-4 mixed-axis sweep

**archetype:** VALIDATE
**Target attacked:** `org/standards/isck/` at HEAD @a2c5ba5f7b (isck files last touched
@1b08f0e37e — round-2 batch 1), tree clean for the subject at read time. Baseline reproduced at
this seat before attack: self-test PASS 4/4 axes + 11/11 fixtures + 38/38 reason-asserted +
8/8 semantic + meta-control, rc=0.
**Round-2 context:** NON-BLIND by declaration; agreement is shared-context convergence, not
corroboration.

---

## CVR2-1 — Independence limit (§6 limit 2): MISCLASSIFIED WITHIN ITS OWN TAXONOMY

§6 limit 2 reads evidence independence as **INEXPRESSIBLE**, whole: *"a validator cannot resolve
what a ref semantically reads; corroboration-by-the-claim's-own-source validates."* Attacked as
designated non-author, three instruments per probe (schema, the SHIPPED `semantic_errors` arm
imported not reimplemented, and the demonstration checker), 4 probes + 1 positive control:

| probe | schema | shipped semantic arm |
|---|---|---|
| A1 `corroborated`, only ref = the record's OWN `relation_id` | VALIDATES | 0 errors |
| A2 observation, only ref = its OWN `source_vintage` | VALIDATES | 0 errors |
| A3 `corroborated`, only ref = the `subject_serial` under assertion | VALIDATES | 0 errors |
| A4 NEGATIVE CONTROL: genuinely distinct ref | VALIDATES | 0 errors (correct) |

Positive control: a known self-loop fired the same arm (1 error) in the same run — the arm was
live while returning 0 on A1–A3, so the zeros are gaps, not instrument failure.

**The demonstration:** a 12-line check in the semantic arm's own idiom (string identity between
`evidence_refs` members and the record's own id/subject/object/source fields) flags 3 of 3
self-citation cases and 0 of 1 negative control, distinguishing ENTIRELY-self-cited (the F5
warrant defeated) from self-citation-among-refs (a Rule 22 flag).

**Verdict:** the limit's SEMANTIC core is honest — whether ref X independently supports claim Y is
genuinely a verifying seat's Rule 22 duty. But the SYNTACTIC-IDENTITY subcase — the exact case the
limit's own sentence names, corroboration by the claim's own source — is mechanical, and §6 limit 4
already defines the class it belongs to: **"inexpressible in the SCHEMA, PARTIALLY MECHANICAL in
the VALIDATOR."** Limit 2 should move to that class, the self-citation check should ship as a
semantic-arm member with its own mutants (both directions: entirely-self-cited REJECT;
distinct-ref ACCEPT), and the limit then narrows to its honest core instead of excusing the
checkable rim. Remedy is the author's; the checker above is offered as the starting idiom.

Scope note: the check reads only string identity. A ref that is semantically the same source under
a different name (an alias, a mirror path) is NOT caught — that residual belongs to the narrowed
semantic core and should be SAID in the rewritten limit, so the mechanical half is not read as the
whole (rigour on the object does not transfer to the wrapper).

## CVR2-2 — R2-4 mixed-axis sweep (18 enum domains across §3.1–3.14; instrument stated first)

**The discriminator applied to every value:** is the value a POSITION IN THE SUBJECT'S OWN
HISTORY (temporal/lifecycle), or a statement about OUR KNOWLEDGE OR ADJUDICATION of that position
(epistemic)? A `running` run is a position; a `contested` entity is a statement about adjudication.

**MIXED — 4 findings in 3 classes:**

1. **§3.2 `verification_standing.superseded` — temporal-in-epistemic, the sweep's strongest.**
   `unverified|corroborated|contradicted` answer *what did checks say*; `superseded` answers *a
   newer assertion exists* — a position in succession history, not a standing. The contract's own
   state-coherence row shows the seam: the first three move by check/adjudication acts, `superseded`
   by "a NEW assertion", a different event kind. Two costs, both real today: (a) INEXPRESSIBLE
   STATES — "corroborated, then superseded" and "contradicted, then superseded" cannot be written;
   the epistemic history is overwritten by the temporal event; (b) **the laundering cell** — a
   `contradicted` assertion flips to `superseded` and the contradiction vanishes from the
   current-value view, which is precisely the two-clocks defect ISCK exists to kill, inside ISCK's
   own epistemic axis. The temporal fact ALREADY HAS a carrier: `superseded_by` (a field, per-arm
   REQUIRED). Direction (author's to cut): drop `superseded` from the enum; supersession = the
   presence of `superseded_by`/a succession relation; standing keeps its last epistemic value. A
   value carried redundantly in an enum AND a field is two carriers that will drift (the
   three-carriers lesson). Interacts with R2-2's derived-status work — flag routed there too.

2. **§3.4 `entity.current_status.contested` + §3.5 `binding.status.disputed` — epistemic-in-
   temporal, one class, two records.** `contested`/`disputed` are adjudication-standings sitting in
   lifecycle/interval axes, and they DISPLACE the value they overlay: a contested entity's
   underlying lifecycle (provisional? active?) is unrecorded while contested; §3.5's own carve-out
   ("disputed MAY carry `valid_to: null` — still open, contested") is the tell — the interval truth
   has to be smuggled through `valid_to` because `status` is occupied by the dispute overlay.
   **Routed to R2-2, not proposed as a standalone split:** under derived-status semantics an open
   adjudication event naturally overlays a preserved lifecycle state, dissolving the mix. Named here
   so R2-2 resolves it deliberately rather than inheriting it.

3. **§3.8 `materializer.current_status.unknown` — observer-state-in-subject-state.** `unknown` is
   how-well-we-know inside a process-lifecycle axis. The rubric contrast that makes this sharp:
   `unknown` in §3.14's coherence axes is COHERENT because the coherence record is an ASSESSMENT
   (observer-grain) — the same token is right at one grain and mixed at the other, which is the
   §3.16 same-sense allowlist's `unknown` entry needing one more sentence (same sense, DIFFERENT
   grain-legitimacy). Also dissolves under R2-2 (`unknown` = no observation events); routed there.

**INTENT-FUSION (Rule 24(iii), not temporal/epistemic): §3.10 `bundle_completeness.partial_legacy`**
fuses DEGREE (partial) with CAUSE/ERA (legacy). Uncovered member found by the hunt: a FUTURE
partial bundle that is not legacy — a component irretrievable after a post-v0.1 store loss — has no
honest value; it must either lie (`partial_legacy`) or block. Direction: degree in the enum
(`complete|partial`), cause in evidence/`absent_components` (which already carries the WHAT).

**COHERENT — 13 domains, each with its reason banked in this record's working notes:** claim_origin
(origin only) · registry_standing (admission lifecycle; `held`/`rejected`/`inadmissible` are all
positions in the admission process with distinct remedy owners) · binding/entity lifecycle values
other than the flagged pair · observation_failure_state (instrument outcome, one intent; `partial`
is degree) · fabric_scope (structural; R2-1's split is a different axis question, already chartered,
not re-found here) · run_status (`running` IS a position; the completed_at arms discriminate) ·
identity_scope, relation_type (`candidate_equivalence` is a link kind; the epistemic axis already
lives on `verification_standing` — the separation working), target_policy (frame) · the five
coherence axes (observer-grain records legitimately carry observer-state values).

**Denominator:** 18 enum domains swept (§3.16's own census denominator: 3 hoisted + 15 inline);
4 MIXED + 1 intent-fusion + 13 coherent = 18. Nothing unswept; the registered vocabularies (§3.15)
are open sets and carry no fixed values to sweep — stated so the residue is named, not silent.

## Round-2 declaration for this seat

Both claimed units EXECUTED: CVR2-1 (independence narrowing) + CVR2-2 (R2-4 sweep). Standing next
acts at this seat: attack R2-5's absence-cell four-postulate record when 1.0.0_SA_CTO~X cuts it;
re-certify against R2-1/R2-2 landings as they cite. Remedies in every finding above are the
author's to cut; this seat attacks results.

— 3.0.0_SA_CVO~X
