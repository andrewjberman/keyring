# NFRA_C3MATERIALIZE sec-6: the pass set does not exclude a DEGENERATE identity layer

**Issuer:** `2.0.0_SA_COO~X` (the `/drive NFRA_C3MATERIALIZE` loop, Andrew-direct 2026-08-28 ~05:04Z)
**Status:** PROPOSAL. Nothing here is written into the PRD. Sec-6 defines what `complete` MEANS, so
amending it is the design lane's call, not the issuer's.
**Ruling this composes with:** Addendum 1f @`76c688fa3d` (6.2's N declared at the L4 cut, BEFORE the
first scheduled run -- *"a bar set after its data is a fit"*) and Addendum 1g @`194679fa9d` (the pass
set = all five DISCHARGED on ONE build).

---

## 1. THE MEASUREMENT

Take a DEGENERATE identity layer: it assigns the SAME identity to every node and reads nothing about
what any node is. Score it against sec-6 as the PRD words each test.

| Test | PRD's own words | Degenerate layer | Why |
|---|---|---|---|
| 6.1 RENAME | *"Rename an anchor resource, re-run, does the identity survive?"* | **PASSES** | a constant identity survives every rename by construction |
| 6.2 PERSISTENCE | *"what fraction of identities survive with continuous succession?"* | **PASSES** | a constant identity persists at 100% across any N |
| 6.3 FIRM SEPARATION | *"The fused model must not do worse than its own inputs."* | **FAILS** | one identity across firms destroys the bd/inf boundary |
| 6.4 DISCRIMINATION | *"A view that cannot distinguish is excluded"* | **PASSES** | scopes VIEWS ENTERING the fusion, not the identity layer's OUTPUT |
| 6.5 PORTABILITY | *"runs against portal and knowledge plane without code change"* | **PASSES** | a layer that reads nothing needs no special case anywhere |

**4 of 5 pass. The single test that catches a useless identity layer is 6.3 -- and 6.3's current
state is `EVALUATED_FALSE`.**

## 2. WHAT THIS IS AND IS NOT

**IT IS NOT an allegation about the build.** The PRD says identity is a signature over four views and
that a rename moves one of four, so the implementation is not constant. The claim is about the
CRITERIA, on the DISCRIMINATION axis of evidence law: *could the evidence differ if the claim were
false?* For 6.1, 6.2 and 6.5 as worded, **no** -- each is satisfied by a layer that distinguishes
nothing, so passing them is not evidence that an identity layer was built.

**The asymmetry is structural, not accidental.** 6.1 discriminates OLD vs NEW in one direction only:
*"Today: guaranteed NO -- the hash changes. Under signature matching: should be YES."* It rejects a
layer that is too BRITTLE. Nothing in it rejects a layer that is too PERMISSIVE, and permissive is
the failure direction that ships silently -- a brittle layer announces itself on the first rename.

**And the guard is on the one test already known to fail.** 6.3 is currently the entire defence
against over-permissiveness while also being the open item. Whatever wave 3 and the firm-carrying
view do for 6.3's re-run, the pass set should not rest its only discriminating weight on it.

## 3. PROPOSED: A PAIRED NEGATIVE ARM ON EACH OF THE THREE

Every arm below runs on the SAME build as its positive half, per Addendum 1g. **These RAISE the bar;
none of them relaxes anything.** Declared now, BEFORE L4 exists, on 6.2's own stated principle.

**6.1 -- add SUBSTITUTION.** Positive: rename an anchor resource, identity SURVIVES. Negative:
replace it with a genuinely different resource at the same position, identity MUST NOT survive.
Report both, and a build that passes the positive while also passing the negative has FAILED 6.1.

**6.2 -- a 100% persistence rate is a FAILURE SIGNAL, not a pass.** Positive: the fraction surviving
with continuous succession, printed beside N and the identity count. Negative: nodes genuinely
removed or replaced between nights MUST show a succession BREAK. Retain the per-night series so
decay shows as a slope (already ruled) AND so a flat 100% is visible as the degenerate tell it is.

**6.5 -- portability must carry CONTENT SENSITIVITY.** Positive: the pipeline runs against the portal
and the knowledge plane without code change. Negative: the two planes hold genuinely different
content, so the identities produced MUST differ between them. Identical output on both planes is not
portability -- it is a layer reading nothing, which is exactly what 6.5's own rationale
(*"because nothing in it reads what a node is"*) makes easy to mistake for success.

## 4. WHAT I AM NOT DOING

- **Not editing the PRD.** Sec-6 is the completion definition; amending it changes what `complete`
  means. Design lane's call.
- **Not declaring 6.2's N.** Ruled to the L4 cut. Declaring it early would move an act ahead of its
  ruled trigger on my own authority.
- **Not claiming these arms are complete.** They are three specific holes found by one adversarial
  read against one degenerate case. A different degenerate case may find more; the read is cheap and
  should be repeated by someone who did not author these arms.

## 5. WHY IT IS RAISED NOW RATHER THAN AT L4

`sec6_state.tests['6.2'].wall_clock_note`: **sec-6 completion >= (L4 build) + N nights, floor 5.**
It is the only test whose cost is nights rather than work and it cannot be compressed later, so
everything still outstanding between the L4 cut and the first scheduled run adds to the completion
date one-for-one. 6.1 and 6.5 currently carry `blocked_on: "L4 identity must exist"` and **no oracle
at all** -- no population, no pass condition, no instrument. Whoever runs them after L4 would define
success having already seen the artifact, which is the fit hazard 6.2's rule exists to prevent,
unguarded, on two of the three outstanding tests.

Raising it after L4 would be raising it at the one moment the answer costs nights.
