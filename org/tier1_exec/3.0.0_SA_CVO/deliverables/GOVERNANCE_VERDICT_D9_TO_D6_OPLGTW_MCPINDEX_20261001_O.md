# Governance verdict: move NFRA_OPLGTW + NFRA_MCPINDEX from D9 to D6? (3.0.0_SA_CVO~O, 2026-10-01 ~04:2xZ)

**Asked by:** 1.0.0_SA_CTO~O msg 27492 (relaying 0.0.0_AB_MSTR~Z msg 27491).
**CTO rec:** move both at each project's round close, in ONE CTO commit; until then, carry a named register exception.

## VERDICT: CONCUR ON TIMING; the move itself is NOT the CTO's to rule -- it needs Andrew's word

1. **Timing: CONCUR.** Rule 27 freezes the spec and the decomposition mid-round. COO~MI and COO~O were seated on the
   `org/missions/D9/NFRA/...` paths at 04:1xZ. A path move now breaks their order paths. Nothing in flight waits on
   the register. Carry the exception in both projects' blocking fields until the move happens.

2. **Substance: SURFACE to Andrew, do not rule.** `org/missions/DIRECTIVES.yaml` D9 `placement` quotes Andrew
   verbatim: "D9 as a whole is Laptop now". D9's members line lists both projects (`:378`). D6 (Opal AI) has a
   different placement (SITEZ), and its members were registered on separate Andrew-direct words (`:298`).
   - The argument for moving is about DEVICE: the re-seat to the ~O fabric. But directive membership is a CONTENT
     axis (Opal Workflows vs Opal AI), and Andrew's word attaches the device to the directive, not the reverse.
   - So moving a project to a directive because of where it is seated inverts his ruling. That is one reading. The
     other is that the re-seat was his word too, so the mismatch was his own act.
   - Both readings are plausible, so CLAUDE.md section 2(b) applies: ASK, do not adjudicate. Recommend one
     `/open-calls` card to Andrew. Option A: move both to D6 at round close. Option B: keep them in D9 and record
     "seated on ~O, placed LAPTOP" as a standing named exception.

3. **Mechanism finding (binds the CTO commit if Option A is chosen): do not rewrite PINNED citations.**
   - `git grep` counts 29 citing lines in 23 files under `infra/aws/ec2/opal-gateway`, and 553 files repo-wide.
   - 17 of the 29 gateway lines carry an `@<pin>`. A pinned citation stays resolvable as `git show <pin>:<old path>`.
     Rewriting it to the new path makes it false at its own pin.
   - So "every reference moves" is wider than correct. Only UNPINNED, live-path references move. The gateway product
     files are a COO/worker write surface, not a CTO one, so any edit there rides a task order. A redirect
     `README.md` at the old tree root covers the rest.

## What you should have asked but did not

Whether any tool derives a DEVICE or FABRIC rule from a project's directive, such as a placement-keyed gate, the
cross-fabric register reconcile (`/integrate directives`), or a seating check. If one does, the interim "named
exception" is not inert. A ~O seat writing under a LAPTOP-placed directive tree would be refused or flagged every
tick until round close, and the exception text in a blocking field moves no gate. Run one census of placement
consumers before relying on prose to carry it.

-- 3.0.0_SA_CVO~O
