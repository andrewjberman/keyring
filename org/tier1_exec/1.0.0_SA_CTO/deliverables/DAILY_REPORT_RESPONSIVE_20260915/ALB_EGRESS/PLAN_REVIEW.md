# ALB egress scoped plan review

Authority: Andrew-direct cfcb13e03f item 1; base CTO Msg96866 assigns this
one-rule repair to `1.0.0_SA_CTO~A` end to end. The change-management ledger
is open at `org/critical_paths/change_management/20260915T0343Z_opal-gateway-alb-oidc-egress_deploy_completion.md`,
committed with its sentinel at `f98358be5b`.

The full saved plan triggered Msg96866's explicit stop condition: it has
three updates, namely the approved ALB SG egress change and descriptions
on two unrelated WAF IP sets. Both WAF address sets stay empty (0 to 0),
but those resources are outside the approved scope. Nothing was applied.

A second READ-ONLY plan, using `-target=aws_security_group.alb`, is ready:
exactly 0 additions, 1 in-place update, 0 destroys/replacements. The group
is `sg-02571ff2f33d2f9d4`; only `egress` changes. Existing TCP8080 VPC egress
is preserved and TCP443 to 0.0.0.0/0 is added. There is no resource drift
within this scoped plan. JSON summaries are adjacent to this note.

Saved scoped-plan SHA-256:
`00715c0dac2a7f5481d06e8fd352ac247531f94681ae85feafe568207c9d5a2b`.
Raw saved plans and JSON are private under
`%LOCALAPPDATA%/CodexSeatScratch/1.0.0_SA_CTO~A/daily-responsive/alb-egress/`.

Base CTO has the full-plan stop report and this concrete scoped alternative
for adjudication. No apply, WAF edit, Gateway service deployment, push or
merge has occurred. A post-apply SG-only re-plan can establish zero diff for
the repair; the full-tree re-plan would still disclose the two unrelated
WAF description updates. Those cannot honestly be called a clean full tree.
