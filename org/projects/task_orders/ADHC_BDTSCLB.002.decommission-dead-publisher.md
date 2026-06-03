<task_order>
<metadata>
  <to_id>ADHC_BDTSCLB.002</to_id>
  <project>ADHC_BDTSCLB (follow-on to .001 dual-writer hardening)</project>
  <title>AE: decommission the dead bd-portal-advisor-publisher Lambda — PREP fully, HOLD the destroy/apply for Andrew's explicit nod</title>
  <assigned_to>0.6.0_AE_PartnerETL</assigned_to>
  <issued_by>2.0.0_SA_COO</issued_by>
  <issued_date>2026-06-03</issued_date>
  <status>dispatched — PREP NOW, apply HELD for Andrew nod (CTO ruling 171434Z)</status>
  <dispatch_held>false</dispatch_held>
  <priority>LOW — harmless-dormant (can't write, crashes pre-write); no urgency. Cleanup/attack-surface reduction.</priority>
  <references>
    <ref type="ruling">CTO 171434Z: decommission CONCUR architecturally; GATE the terraform destroy on Andrew's explicit nod (infra deletion = human nod per autonomy rules)</ref>
    <ref type="finding">0.6.0 AC4-conclusion 170853Z: publisher DEAD (dormant ~2026-04-07, FATALs at load_sources nna mismatch, fully superseded by D_02/gold chain, zero consumers, S3-fan-out hasn't fired ~2mo)</ref>
    <ref type="rule">CLAUDE.md Rule 1-6 + Rule 18 (safe-apply/HALTGT). Infra deletion = Andrew-nod-gated.</ref>
  </references>
</metadata>

<scope>
Decommission bd-portal-advisor-publisher — a DEAD, BROKEN, FULLY-SUPERSEDED Lambda. This is belt-and-suspenders beyond bd-v2.25.0's writer-removal (.001): removing the whole module eliminates the dual-writer class ENTIRELY + clears dead/broken infra + unused IAM (attack-surface + comp-aws-census-noise reduction).

DEADNESS EVIDENCE (0.6.0, already established): dormant since ~2026-04-07; today's first-invoke-since FATAL'd (pyarrow nna-column mismatch at load_sources, pre-any-write); everything it produced (book.json / timeseries.json / mix_timeseries.json) now produced by D_02 + the gold chain; ZERO live consumers; the S3-notification fan-out (gold/pipeline-complete.json -> bd-portal-publisher -> fan-out) hasn't triggered it in ~2 months.

## PREP NOW (do not apply):
1. Scope the full Terraform removal: the bd-portal-advisor-publisher Lambda module + its IAM role/policy + the S3-notification binding that's supposed to fan-out to it (confirm removing the binding doesn't affect bd-portal-publisher's other fan-outs — surgical to THIS dead target only). KEEP bd-portal-publisher itself + any live fan-outs.
2. tf plan -> capture the destroy plan (expect: Lambda + IAM + notification binding destroyed, NOTHING else). Verify 0 collateral.
3. comp-iam gaps after (confirm no other role/path depended on it) + note the comp-aws-census delta (one fewer Lambda).
4. Recoverable-via-git note: the module is in TF/git -> re-addable if ever needed (it won't be — superseded).
5. Update lambda-source-map + pipeline_inventory (remove the entry).

## HOLD:
- Do NOT run the destroy `terraform apply` until COO relays Andrew's explicit nod (CTO flagged it to Andrew; low-pri/no-urgency — he nods whenever).
- On the nod: safe-apply (HALTGT) the destroy -> 0-diff-after verify -> tag -> record-terraform-deploy. RAVC2 to COO + CTO.
</scope>

<acceptance>
- [ ] PREP: scoped TF removal (module + IAM + S3-notification binding, surgical), destroy-plan captured w/ 0 collateral confirmed, comp-iam-after clean, source-map/inventory removal staged. RAVC1 the prep to COO.
- [ ] HOLD the apply for Andrew's nod (COO relays).
- [ ] On nod: safe-apply destroy, 0-diff-after, tag, RAVC2. ADHC_BDTSCLB fully closed (hardening .001 + decommission .002).
</acceptance>
</task_order>
