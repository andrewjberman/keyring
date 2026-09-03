# ANDREW-DIRECT at the CTO terminal, 2026-09-03 ~04:5xZ -- "Recs approved" on /open-calls (2 calls)

**Verbatim (all words):** `Recs approved`

**What was in front of him (the /open-calls output of 1.0.0_SA_CTO, 2 calls):**

- CALL 1 (BLOCKING): gate the CVO-to-worker send during L7-L9 -- (a) REFUSE the broker send, or (b) ANNOUNCE it to
  2.0.0_SA_COO and let it deliver. **REC (a) refuse** -- an announced message still reaches the worker; one check in
  the broker send path keyed on sender serial `3.0.0_SA_CVO`, a Tier-2 recipient, and a project row reading L7-L9.
- CALL 2 (CARRIED): extend gate (iii) so a route row is also refused while any investigation row under the project
  lacks a disposition -- yes/no. **REC yes** -- same file, same shape, same commit hook as the limb that refuses a
  route over an open TO.
- Withdrawn from the queue, decided in lane and shown to him: the water-test certifier is `3.0.0_SA_CVO` under the
  atom-decomp package's standing rule (the spine's L8 bound governs project limbs; the water test is not one); the
  integrator-only push guard is dropped as the CTO's own proposal (cadence stays Andrew's by word, LD-0522).

**Reading (scope = the two recs, verbatim, nothing wider):**
1. A broker send from `3.0.0_SA_CVO` to a Tier-2 serial is REFUSED while any tree project's `dep_stage` reads a
   limb in L7-L9. Refusal, not announcement. The refusal names the projects and the lawful route (up to
   `2.0.0_SA_COO`, or `1.0.0_SA_CTO` for a scope change). Mechanism: the shared send path every carrier uses.
2. Gate (iii) in `.tools/surprise-row-gate.py` grows a second precondition: a tree REMEDIATION row carrying a route
   is refused while any investigation row under the same project has no disposition.
3. The two in-lane decisions stand as stated (no objection raised; they were not calls).

**Authority chain:** this record; Andrew's earlier words in the same exchange via `2.0.0_SA_COO` records @10a4beaffb
and @de2d6d643c; spine v2.1 @aaa5a2b085 (L8 not-engaged set, L10 precondition); the compiled step logs
@8c366948b3 (gate-candidate class 4, OPEN -> now CLOSING).

**Execution this turn (1.0.0_SA_CTO):** the guard in the broker send path with a red-first exercise; the gate (iii)
investigations limb with a red-first exercise; commits via safe-commit; same-turn broadcast with push state stated as
measured. Applied state of the broker guard is DESIRED until the serving process restarts -- stated in the broadcast.
