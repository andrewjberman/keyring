# Session log -- ADHOC.canon-r11-global-axis-deploy (0.7.0_AE_CloudOps~DELL1, 2026-10-17 ~15:20Z to ~16:00Z)

**archetype:** DEPLOY

GO msg 7623 from 2.0.0_SA_COO~D1; D4-PASS msg 7652. Order: org/tier2_senior/0.7.0_AE_CloudOps~DELL1/task_orders/ADHOC.canon-r11-global-axis-deploy.md. Ledger mdpf-canon-r11-global-axis-deploy-dell1-20261017.

## What was done
- Preconditions: pair sha256 9e7b1930... matches, COO sign @370cd85823, CTO half @78082bd6b6; pin 128fce3524 descends from d2f734fbac and is on origin/wk-MDPF_CANON-33; sentinel scan over 30 worktrees (FB-p-2 names the lambda as a consumer only, stated to the issuer).
- Before print, D4-ref (errors [global], 12 bodies), D2 (package built from the pin; 2 members differ; upload; one .tf value; one targeted safe-apply), D4-new (green, errors [], 16 bodies), issuer D4-PASS, emitter read, final print.
- Evidence: deliverables/canon_s6/. Responses stay outside the repo in C:/dev/_deploy_artifacts/canon_s6/ (sha256 in the ledger).

## Compiler Tools
- build_package.py --pin: rebuild of the deployed pin was byte-identical to the deployed object (positive control for the build).
- terraform plan -target: first run failed on an unregistered local module added by another seat (`terraform get` registers it, local only); second failure was my upload lacking the content-sha256 metadata the Terraform reads (re-uploaded before any apply). Gap: the order text does not mention the metadata requirement.
- safe-apply: seat-gates OVERLAP WARN with IRPT_BCKEND (mode WARN, proceeds); HALT-gate listed my own already-read messages, HALT_ACK=1.
- mdpf-code-equality.py: whole-tree BEFORE and AFTER identical (5 trees, 77 files, 43 equal, 34 not equal).
- A returned body is a {body, sha256} wrapper holding JSON text; comparing the wrapper reports every body as different. Decode first.
- comp-rail: denied nothing this session beyond a heredoc python containing the token `find(` earlier in the day.

## Open
- ADHOC.canon-r11-orion-reader-trail: L3 log read after 16:30Z 2026-10-17; L4 removal by 2026-10-19T18:39Z.
