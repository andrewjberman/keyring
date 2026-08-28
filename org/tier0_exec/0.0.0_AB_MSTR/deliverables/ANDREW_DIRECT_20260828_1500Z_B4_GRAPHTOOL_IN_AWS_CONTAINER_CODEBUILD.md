# ANDREW-DIRECT 2026-08-28 ~15:00Z at the 0.0.0_AB_MSTR terminal -- B4 (graph-tool) runs in an AWS container, not on the workstation

**Received by:** 0.0.0_AB_MSTR, at this terminal, in answer to B4 card #2 (pushed 14:58Z: "May DT~X start Docker
Desktop + pull the graph-tool image (egress) on this box for the read-only B4 measurement?").

**His word, VERBATIM:**

> have htem do it in an aws container, codebuild or whatever their product is on there

## Reading, at verbatim scope (relayed, not adjudicated wider or narrower)

1. **Card #2 is ANSWERED, and the answer is a substitution, not a yes/no:** the B4 graph-tool measurement
   (CTO~X 78044's branch (a)) runs **in an AWS container** -- CodeBuild, "or whatever their product is on
   there" (the seat doing it picks the AWS container product: CodeBuild, ECS/Fargate, Batch...). **NOT** a
   Docker Desktop daemon start and **NOT** an image pull on Andrew's workstation. That branch is closed by
   this word.
2. **"have them do it"** -- the seats do it; MSTR relays and seats. The role-fit builder is
   0.4.0_DT_ClientPlatform~X (CTO~X 78044); an AWS container run is an infra act (CLAUDE.md rule 13: DT/AE =
   infra), so the standing infra rules travel with it unchanged: dependency graph BEFORE any cloud change
   (rule 20), Terraform via `safe-apply` never bare `apply` (NEVER-9), no shadow pipeline (NEVER-5), a
   change-management ledger entry if it lands as a deploy. Nothing here is a new gate -- these are the rules
   that already bind the act.
3. **What the word covers:** the AWS-side image pull / build / run for the B4 read-only conformance
   measurement against CRO~X's oracle @b4caea27f0. **What it does not say:** anything about the oracle
   (unchanged), the L2 STRUCTURE view's remedy beyond the measurement, or any other egress. "whatever their
   product is" delegates the product choice, not the scope.
4. **What it does NOT lift:** nothing outside B4. The estate-report backlog and the SITEZ reconcile remain
   open at Andrew on their own cards.

## Provenance

- Card #1 (pip graspologic, disposable venv): Andrew "you have egress" at the DT~X terminal ~14:47Z (DT~X
  78002; ledger row 18 @525e695f4d). Measurement: PASS on most clauses, FAIL on per-run convergence (DT~X
  78036); CTO~X call 78044: oracle unrelaxed, branch (a).
- Card #2: MSTR push 14:58Z + CTO~X RESERVED list; answered here ~15:00Z.
- Broadcast: same turn, MCP to 1.0.0_SA_CTO~X, 2.0.0_SA_COO~X, 0.4.0_DT_ClientPlatform~X, 3.0.0_SA_CVO~X,
  4.0.0_SA_CRO~X.
- Push state at write: origin/CLOUD @67f01b5c27; this record LOCAL until the next integration window.
