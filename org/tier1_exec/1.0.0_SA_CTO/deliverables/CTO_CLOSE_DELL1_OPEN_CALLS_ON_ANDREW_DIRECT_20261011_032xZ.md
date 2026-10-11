# dell1 open calls closed on Andrew's word (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~03:2xZ)

**Record:** `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261011_032xZ_OPEN_CALLS_ANSWERED_ITEMS_1_TO_9.md` @5e10dd2dc5.
That commit is on `origin/box/laptop` and not yet in `box/dell1`; the quotes below were read at that pin (`git show`). It was
relayed by `0.0.0_AB_MSTR~DELL1`, msg 3422.

Andrew, verbatim at the pin (lines 8-10): "3.) We already declared that Muni will just be a custom model, no SMA inclusion,
therefore the answer is no. ... 5.) Yes delete is fine. 6.) Delete. ... 9.) Doesn't matter, don't touch."

| call id | item | ruling |
|---|---|---|
| `dell1-20261009T055557Z-203a` | 3 | NO. Opal_Muni_Sleeve is not Opal's Muni SMA; Muni is a custom model with no SMA inclusion (C-MUNI-VERIFY, MDPF_STRATID). |
| `dell1-20261009T084628Z-86a2` | 9 | No rotation of `anthropic-api-key`. |
| `dell1-20261009T110120Z-bf6d`, `-110109Z-838c`, `-110110Z-5f4b` | 5 | YES, delete the two retired Terraform state objects. The delete is routed to `2.0.0_SA_COO~B1` as a fact. |
| `dell1-20261009T110121Z-c20b`, `-110111Z-69ef` | 6 | YES, delete the orphan log group `/aws/lambda/opal-assets-absence-check`. The delete is routed to `2.0.0_SA_COO~B1` as a fact. |

Closing a row records the decision. The deletes themselves are the routed seat's acts, each read back after it runs.

-- 1.0.0_SA_CTO~DELL1
