<task_order>
<metadata>
  <to_id>ADVI_FEREFI.W2b</to_id>
  <project>ADVI_FEREFI</project>
  <title>DS: 49F AUM-mode total_aua fee-split (D_02 gold dedup edit) — completeness fast-follow to W2, kills 49F AUM-mode "approx"</title>
  <assigned_to>0.4.0_DS_ClientPlatform</assigned_to>
  <issued_by>2.0.0_SA_COO</issued_by>
  <issued_date>2026-06-03</issued_date>
  <status>closed -- COO verified-done sweep 2026-06-10 (Andrew directive; ground-truth: parent project complete in registry or work landed/superseded per git)</status>
  <dispatch_held>false</dispatch_held>
  <priority>MEDIUM-HIGH — completeness/consistency (avoid INF-vs-49F AUM-mode asymmetry); fast-follow, does NOT block INF #6 ship or the promote.</priority>
  <references>
    <ref type="prd">docs/architecture/ADVI_FEREFI_PRD.md item 6 ("both firms, real splits, no approx label" — firm-AND-mode-agnostic)</ref>
    <ref type="ruling">CTO ruling ws-charter_1428Z: 49F AUM-split IN SCOPE as W2b; faithful to directive not a new product call; flagged to Andrew visibility/override only</ref>
    <ref type="finding">DS W2 RAVC1 (c42c5e6ed msg): 49F NNA-mode fee-split already served; total_aua_fee_paying ABSENT on 49F -> AUM-mode toggle inert</ref>
    <ref type="rule">CLAUDE.md Rule 17 (fee classification = business logic = GOLD tier) + Rule 13/14/14a/15 + comp-pipescript io/postdeps + comp-validate</ref>
  </references>
</metadata>

<scope>
49F's served advisor timeseries already carries NNA-mode fee-split (nna_canonical_fee_paying + per-role aua_fee_paying) — NNA-mode fee toggle works. But total_aua_fee_paying (AUM-mode) is ABSENT -> 49F AUM-mode fee toggle falls back to unsplit total_aua (inert). INF now has it (W2, F11-C). Close the asymmetry: emit deduped total_aua_fee_paying/_no_fee per period for 49F.

## THE EDIT (gold-tier, Rule 17):
- 49F D_02 (black_diamond gold) — add a deduped total_aua split (fee_paying / no_fee) at the firm/advisor per-period grain the Lifetime-Activity timeseries consumes, so the publisher surfaces total_aua_fee_paying on the served artifact.
- DS flagged this is a careful edit into an intricate melt/dedup aggregation (modest but non-trivial) — dedup discipline matters (avoid double-count on the total_aua split; sum(fee_paying)+sum(no_fee)==total_aua per period to the cent).
- HONESTY (carry in code + for FE label): 49F equal-split backfill on pre-data periods (honesty flag #3) — don't over-claim "no approx" for backfilled history.

## DEPLOY (full DS gold cycle — this IS gold, unlike INF's Lambda):
- comp-pipescript io (column gaps) -> comp-validate (all-pass before signal) -> comp-pipescript postdeps (the publisher/rollup that emits the served timeseries — confirm the total_aua split propagates to platinum/advisors/{id}/timeseries.json) -> Rule 13 commit->push->S3/SSM deploy cycle.
- VERIFY against the ACTUAL served 49F timeseries (not a partial proxy): total_aua_fee_paying present -> hasFeeSplitSeries fires in AUM-mode -> 49F AUM-mode "approx" dies.

## SEQUENCING (CTO):
- Does NOT block the INF #6 ship or the FE #6 tail.
- TARGET the SAME held promote bundle IF W2b lands before Andrew GOs the promote (promote held on his INFOTD/INFNNA smoke = runway). If not ready by promote-GO -> INF ships, 49F AUM-split rides a later promote. DO NOT hold the promote on W2b.
</scope>

<acceptance>
- [ ] 49F served advisor timeseries carries total_aua_fee_paying/_no_fee per period; sum(fee_paying)+sum(no_fee)==total_aua per period to the cent (dedup-correct).
- [ ] hasFeeSplitSeries fires in AUM-mode for 49F (verified against the ACTUAL consumed served artifact); AUM-mode "approx" gone for 49F.
- [ ] Gold discipline: comp-validate all-pass + comp-pipescript postdeps confirmed; Rule 13 deploy cycle complete.
- [ ] RAVC2 to COO (CC CTO) with served-artifact confirmation + honesty flag #3 restated for the FE label.
- [ ] On W2b served-verify + W2 (INF) served-verify -> COO signals RD-AI to do the #6 FE tail covering BOTH firms (drop the approx for INF + 49F AUM-mode).
</acceptance>
</task_order>
