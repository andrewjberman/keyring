# /self-drive ~O fabric -- tick 82 (1.0.0_SA_CTO~O, 2026-09-27 19:5xZ-20:37Z)

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d.

- **Andrew-direct ~19:5xZ** (record @785fc4d71f):
  - Call 1: "/sprint for Andrew only", YES. COO~O issued OG-s-1, the `.env` roster in `deploy-to-ec2.sh`, as a narrow
    release (@95e499c916). The OA-g-3 backfill is superseded, and W3-S22 disarms on the landing. This seat owes the
    CTO never-widen half at OG-s-1's PHASE A.
  - Call 2: BD added MFA around 06-23. COO~O amended MX-s-4 A3 (@58828bb740): step 1 consumes bd-49f-auto-login's
    durable trust token.
- **Andrew-direct ~20:1xZ refinement,** verbatim: "see if you can just have a rest api pull for those tables. shouldnt
  need to make another 49 Financial bd crawler to get the long-trust token because we already have it with that
  existing crawler".
  - Routed to COO~O (file 20260927T203308Z): REST pulls via the `data/black_diamond/API/` catalog, on the
    `blackdiamond/49f/session` secret.
  - The pattern is `bd-49f-runner` / `bd-49f-fees-runner`; check first whether fees is already covered. 49F only.
- **Row NFRA_MCPINDEX-Z-S29 ARMED (@749f78a0e2):** a plaintext BD 49F portal password sits in 2 tracked bd-exporter docs,
  in git since c4eeb4b8d6.
  - Disarm: Andrew rotates the password; the new value goes to Secrets Manager only; the docs carry a pointer.
  - No history rewrite is proposed. Offered to Andrew: replace the literal in both docs now.
- **R2-k step 3 needs no cell** (COO~O 200529Z): the grant-writer Lambda does not exist yet. MP-a-1 creates it from a
  tree that already carries the deny put.

**Cards at Andrew:**
- (1) the switchover sitting (an act);
- (2) the BD password rotation (row Z-S29), and whether to replace the doc literals now.

**Completion test:** NOT DONE. 0 of 4 projects are complete.

state: ARMED
