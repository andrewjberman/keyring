# Andrew-direct 2026-10-10 ~13:3xZ -- answers to the 15 open items (18 cluster rows)

Seat: 1.0.0_SA_CTO (laptop). He answered the numbered list given at ~13:2xZ. Words, VERBATIM:

> "1.) use the harvest script for BarRons. 2.) yeah they can do that. 3.) will do momentarily 4.) later. 5.) later
> 6.) later 7) no 8) agreed 9) delete 10) delete 11)we're just gonna call that a custom model 12) yes delete
> 13) not only am i on those but Lauren added me to some share point folder where they collect anyway 14) later
> 15) crawl that instead"

## Item map (number -> cluster row -> what his word means -> owner)

| # | Row | His word | Meaning, routed | Owner |
|---|---|---|---|---|
| 1 | sitez -9f24 Barron's sign-in | "use the harvest script for BarRons" | No interactive sign-in: collect Barron's through the existing harvest script. | site Z (CTO~Z), on return |
| 2 | sitez -cf36 Bloomberg queue draws | "yeah they can do that" | YES: the BG seat may run Bloomberg history/intraday draws the MDPF_DEMQUE queue has booked, under the queue's budget and ledger. His 2026-08-07 "cant download" is lifted for queue bookings ONLY; Teams-asked draws stay denied (the scope as asked). | site Z, on return |
| 3 | sitez -21c5 Control Plane look | "will do momentarily" | His own act, pending. | Andrew |
| 4 | sitez -f0d2 Opal Bloomberg sign-in | "later" | Stays open. | Andrew |
| 5 | sitez -a519 one Teams message | "later" | Stays open. | Andrew |
| 6 | sitez -4d5a ask Alyssa | "later" | Stays open; his 2026-10-06 hold stands. | Andrew |
| 7 | dell1 -86a2 rotate anthropic-api-key | "no" | DECLINED: no rotation. Row closes as declined. | dell1, on return |
| 8 | dell1 -bf6d / -838c / -5f4b two retired Terraform state objects | "agreed" | DELETE APPROVED: s3://opal-313476888478-terraform-state/canonical-schwab-si2-schedule/tfstate and .../opal-assets-absence/tfstate. | executor seat |
| 9 | dell1 -c20b / -69ef orphan log group | "delete" | DELETE APPROVED: /aws/lambda/opal-assets-absence-check. | executor seat |
| 10 | dell1 -f23d stray demand_state object | "delete" | DELETE APPROVED: s3://opal-data-assets/bloomberg/global/silver/demand_state/request=ETFS_RIVALS-HISTORY-OWED-DAILY/state.json. | executor seat |
| 11 | dell1 -203a Opal_Muni_Sleeve | "we're just gonna call that a custom model" | RULED: Opal_Muni_Sleeve ($550,823, 40% sleeve of one blended Cottonwood account) is NOT Opal's Muni SMA; classify it as a custom model. MDPF_STRATID FWD-3 shows no Muni SMA dollars from it. | dell1 (MDPF_STRATID), on return |
| 12 | dell2 -62ea C:/dev/_scratch265 | "yes delete" | DELETE APPROVED (local folder on dell2; only dell2 can act). | dell2, on return |
| 13 | dell2 -3082 Research Team Meeting transcripts | "not only am i on those but Lauren added me to some share point folder where they collect anyway" | He IS on the series (so the Graph 3003 refusal is not an invitation gap), and the transcripts are collected in a SharePoint folder Lauren shared with him. Read them from that SharePoint folder instead of the meeting API. | dell2 (NFRA_TRNSPT), on return |
| 14 | dell2 -3cb1 Alyssa's portal request | "later" | Stays open. | Andrew |
| 15 | dell2 -fbb1 close test ticket | "crawl that instead" | CTO reading: a seat closes the test ticket by driving the Ticket Center board through the browser crawler rather than waiting for a person. If he meant something else, his next word overrides. | dell2 (TCKT_VNEXT), on return |

## Routing

- Deletes 8-10 are AWS objects, not box-local, and need no dell1 session: routed to 2.0.0_SA_COO~C for one ADHOC order to
  a laptop cloud-operations seat. Each target is read first (exists, matches the row, no reader), the delete runs, the
  absence is read after. dell1's rows close on its return, citing the receipt.
- Everything owned by site Z, dell1 and dell2 is relayed through 0.0.0_AB_MSTR when each box's manager returns; each box
  writes its own open-call list (one writer per box).
