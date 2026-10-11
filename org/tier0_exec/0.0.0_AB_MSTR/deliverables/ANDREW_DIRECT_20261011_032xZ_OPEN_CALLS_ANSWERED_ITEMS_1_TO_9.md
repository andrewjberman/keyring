# Andrew-direct 2026-10-11 ~03:2xZ -- open calls answered, items 1 to 9

Channel: the laptop `0.0.0_AB_MSTR` terminal, in answer to that seat's numbered list of the 19 cluster open calls (16 distinct
asks), read from `python .tools/open-calls.py list --all --cloud` at ~03:13Z.

## VERBATIM

"1.) Yes. 2.) Yes on Monday. 3.) We already declared that Muni will just be a custom model, no SMA inclusion, therefore the
answer is no. 4.) Yes we can make the exception for now. 5.) Yes delete is fine. 6.) Delete. 7.) Delete. 8.) Delete. 9.) Doesn't
matter, don't touch. 10-16 I will deal with later."

## The numbered list he answered (as the laptop MSTR printed it)

| # | Call id(s) | Box | Ask |
|---|---|---|---|
| 1 | sitez-20261011T012754Z-c719 | sitez | May FWD-4's CLIENT branch (a client-firm mail naming Andrew is texted to him) stand as a qualified essential wait, read when the first real client mail arrives? (COMM_ASSIST) |
| 2 | sitez-20261009T150500Z-4d5a | sitez | May a seat ask Alyssa, on Teams, to send one portal-figure question to the Opal Bloomberg account? |
| 3 | dell1-20261009T055557Z-203a | dell1 | Is Opal_Muni_Sleeve ($550,823, the 40% sleeve of one blended Cottonwood account) Opal's Muni SMA, or exclude it with a reason (C-MUNI-VERIFY; MDPF_STRATID) |
| 4 | sitez-20261011T003538Z-5bdf | sitez | Acknowledge an R20 declared exception for the two legacy Black Diamond IAM role names (bd-merge-daily-lambda-role, bd-pipeline-task-role) so IAM-w-2 can adopt them into Terraform under their live names (NFRA_IAMROLES202609) |
| 5 | dell1-20261009T110120Z-bf6d, dell1-20261009T110109Z-838c, dell1-20261009T110110Z-5f4b | dell1 | Delete the two retired Terraform state objects s3://opal-313476888478-terraform-state/canonical-schwab-si2-schedule/tfstate and .../opal-assets-absence/tfstate (state proven empty) |
| 6 | dell1-20261009T110121Z-c20b, dell1-20261009T110111Z-69ef | dell1 | Delete the orphan CloudWatch log group /aws/lambda/opal-assets-absence-check (function gone) |
| 7 | dell1-20261009T051507Z-f23d | dell1 | Delete the stray S3 object s3://opal-data-assets/bloomberg/global/silver/demand_state/request=ETFS_RIVALS-HISTORY-OWED-DAILY/state.json |
| 8 | dell2-20261009T092211Z-62ea | dell2 | Delete C:/dev/_scratch265 (worker ~265 scratch, 21 MB, outside the repo) |
| 9 | dell1-20261009T084628Z-86a2 | dell1 | Rotate anthropic-api-key |
| 10-16 | sitez 21c5, 8ed7, f0d2, a519, 058e; dell2 01c5, 3cb1, fbb1 | sitez, dell2 | Acts only he can do |

## As recorded (no scope added)

1. YES.
2. YES, on Monday (2026-10-12).
3. NO: "Muni will just be a custom model, no SMA inclusion."
4. YES, the exception, "for now".
5. to 8. DELETE, each.
9. "Doesn't matter, don't touch": no rotation.
10. to 16. Left OPEN: "I will deal with later."

## Routing

Each call is closed with its ruling by the box that lists it. The deletes in 5 to 8 are executed there by the seat that opened
the call. The laptop manager carries the verbatim answers to each box's manager over the agentbus and names this file to
`1.0.0_SA_CTO`. Row 4 was not in the 03:13Z list, so it may already have been closed; site Z confirms.

## Amendment 03:2xZ -- items 5, 6 and 7 were already done (1.0.0_SA_CTO msg 108185)

The deletes for items 5, 6 and 7 were executed on the laptop on 2026-10-10 at 13:56Z by `0.7.0_AE_CloudOps~CTL`. Receipt:
`org/tier2_senior/0.7.0_AE_CloudOps~CTL/deliverables/ADHOC_DELETES_20261010/RECEIPT.md` @46cca3496a, on origin CLOUD.

- The two tfstate objects and the stray state.json have delete markers on versioned buckets, read 404, and their versions
  survive.
- The log group reads describe 0.

dell1 was told (bus 4b201752) not to re-execute them, and to close rows bf6d, 838c, 5f4b, c20b, 69ef and f23d SUPERSEDED citing
that receipt. 86a2 closes DECLINED and 203a closes NO.
