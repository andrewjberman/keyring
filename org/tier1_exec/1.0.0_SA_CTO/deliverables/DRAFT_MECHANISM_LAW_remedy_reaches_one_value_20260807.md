# DRAFT — proposed entry for `docs/doctrine/MECHANISM_LAWS.md`

**Status:** DRAFT for `3.0.0_SA_CVO` review. **Not committed to doctrine.** They asked for the draft
and will review + land it; MECHANISM_LAWS is their surface and I do not commit into it.
**Author:** `1.0.0_SA_CTO~C`, 2026-08-07. **Placement rationale (theirs):** *"it is a failure-shape
law, not a verification-control law, so it sits with the taxonomy material rather than in
CONTROLS_OVER_CARE."*

---

## THE REMEDY THAT REACHES ONE VALUE ON ITS OWN AXIS

**A remedy proposed for a multi-value axis must state which values it does NOT move. An axis whose
values require different remedies presents as one workstream and is several.**

This is Rule 24 postulate (iv) — the stability frame — applied to REMEDIES rather than to schemas.
Rule 24 binds a taxonomy at authoring time; this binds a **fix** at proposal time, and the test is the
same one: *name the axis, then ask whether ONE remedy moves every value together.*

### The test

1. Name the axis the remedy claims to serve, and enumerate its values.
2. For each value, ask: **does this specific remedy structurally reach it** — not "could a similar
   effort reach it," but does *this* one.
3. **Name the values it cannot reach, in the proposal.** Not in a follow-up, not as future work.

### Why it is a distinct failure shape

**A remedy that reaches one value of four is not 25% of a fix; it is a fix plus three unnamed gaps
that now look closed.** The proposal reads as complete because the axis was named once and the remedy
was named once, and nothing in the sentence *"fix the seam, then type the termination"* exposes that
three of four termination kinds are untouched by it.

**The failure is invisible in the direction that matters:** after the remedy lands, the axis is
reported as addressed, and the unreached values are now harder to surface than before — because the
workstream that would have found them is closed.

### Diagnostic instance (2026-08-07, `NFRA_VERTHARVEST` §4.2)

A discriminator distinguishing business verticals from engines was to be built on **termination
kind** — what a chain's output is finally consumed by. The proposed remedy was a graph seam fix
(emitting a `GOVERNS` edge so a served URL can traverse to its bucket).

| termination kind | reached by the seam fix? |
|---|---|
| portal route / S3-served surface | ✅ **yes** |
| email recipient | ⛔ **no** — no S3 traversal reaches a human inbox |
| analyst artifact / deck / CSV | ⛔ **no** — local output, never in the graph |
| external API caller | ⛔ **no** — access-log plane, not the object plane |

**One of four.** The remedy is correct and worth doing; the plan built on it silently covered a
quarter of its own axis.

⭐ **AND THE THREE UNREACHED VALUES SHARE ONE CAUSE, WHICH IS THE GENERALISABLE PART.** They are the
same blindness already recorded at a different grain: *any product whose delivery is an email, a
report to a person, or any other non-artifact channel* is structurally invisible to artifact-based
instruments — **"they do not look neglected, they look nonexistent."** That blindness nearly caused a
live daily product to be proposed for decommission (`ceo-digest`, Phase-0 row 6), and it would have
caused the same class of instrument to silently drop every email-terminating vertical. **One cause,
two grains, and the remedy at either grain reaches neither instance.**

**COROLLARY: when the unreached values share a cause, they are not three gaps — they are one gap
appearing three times, and it will not close incidentally.** A plan that lists them as separate
follow-ups has mis-scoped the work in the direction of looking tractable.

### Relationship to neighbouring laws

- **Rule 24 (iv)** binds the SCHEMA at authoring. This binds the REMEDY at proposal. A schema can pass
  (iv) and still attract a remedy that fails this.
- Distinct from *a control must fire on the defect event* — that law is about a control's TRIGGER;
  this is about a remedy's REACH.
- Distinct from the retrieval-denominator family: nothing here is mis-measured. **Every number is
  correct and the coverage claim is still false.**
