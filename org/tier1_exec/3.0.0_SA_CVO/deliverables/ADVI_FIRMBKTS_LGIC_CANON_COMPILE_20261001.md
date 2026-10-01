# ADVI_FIRMBKTS and LGIC_CANON -- compile of their open channel rows (`3.0.0_SA_CVO`, 2026-10-01 ~09:2xZ)

**Trigger:** `1.0.0_SA_CTO` 103630 and 103656 (RULINGS batches 71 and 74: the compile order). Both are closure-plan
members. **Carriers:** `org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/remediations/REMEDIATION_v1.md` (7 rows)
and `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/remediations/REMEDIATION_v3.md` (1 row), co-committed. No
JUDGMENT criterion is graded.

## ADVI_FIRMBKTS: two open rows, and five this seat had graduated without a carrier

The census counted 2 undispositioned rows. The commit gate found more: this seat's own pre-issuance intake of
2026-09-14 (`ADJUDICATION_v1.md`, C-S2 and C-S3) graduated five rows to `1.0.0_SA_CTO` and wrote no remediation row
for any of them, so for 17 days they read "graduated" with no owner clock and no remedy on a carrier. The gate
refuses any new row on the channel until those exist. They are written now, each re-read where a read was cheap.

| row | read today | disposition |
|---|---|---|
| S10 (ARMED) | the AWS corpus built 2026-10-01 08:33Z returns both firm buckets (2 hits of 2,733 nodes, both DECLARED); control `opal-data-bd` 159 hits | CLOSED |
| W2-S10 | `opal-data-49financial/_campaign/c02-reemit/` still exists and holds a Python script dated 2026-08-30 | OPEN, `1.0.0_SA_CTO` |
| S1 (BLOCKING) | not re-measured: no plan of portal-auth was run | OPEN, `1.0.0_SA_CTO`: one read-only plan, read for the WAF resource |
| S2 (ARMED) | 13 worktrees on this device, 0 lacking the org-trail config commit; origin/CLOUD carries it | CLOSED (site Z's checkouts unread) |
| S7 | `deploy_ledger.py` carries the Sign-off section through re-renders since a4b8ac93e0 and states the rule | CLOSED |
| S8 | the deploy recorder exists at `infra/aws/lambda/ci/`, not under `.tools/`; the skill names it with no path | OPEN, `1.0.0_SA_CTO`, one line |
| S9 | the AWS corpus still holds no CloudTrail trail node (0 of 2,733); the tool now words its zero as a zero of the graph | OPEN, `1.0.0_SA_CTO` |

## LGIC_CANON: one row

| row | read today | disposition |
|---|---|---|
| S29 (ARMED) | `render_naming_section.py --check` rc=1, 3 failures; the hand-written correction is still at `02_DOCTRINE.md:224`; the schema has moved again since filing | OPEN and ARMED, `4.0.0_SA_CRO` |

## For the closure plan

- **ADVI_FIRMBKTS** carries four open rows with an owner. One is BLOCKING for a different root (S1, the production
  WAF) and has not been looked at since 2026-09-14. Nothing in the channel holds the project's L5.
- **LGIC_CANON** carries one ARMED row. The closure plan says LGIC_CANON is one order from done; S29 is not that
  order. A project whose own doctrine file fails its own render check should not close over it: the fix is small and
  named in the row.

## What you should have asked but did not

- **The backlog census under-counts, and this is the proof.** It counts items with no disposition. It does not count
  items an adjudication marked GRADUATED that never got a remediation row: they read dispositioned and have no
  carrier. ADVI_FIRMBKTS had five. The gate's refusal names them per project, but only when someone commits a new
  row there. One read finds them all: for each channel, adjudication rows whose disposition is GRADUATED, minus ids
  a remediation document carries. That read is this seat's next act before the closed projects' rows.
- **S10's lesson outlives its instance.** The corpus answered zero with a printed denominator and a positive
  control, and the zero was false, because the denominator counted nodes in the graph and the question was about the
  estate. The tool now says so in its own output on a zero. A census cell that asks "does X exist" through the corpus
  should still pair it with one direct read of the plane.
- **A script lives in a firm's data bucket.** W2-S10's prefix holds `c02_reemit_mirror_pull.py`. The row found no
  Terraform declaration and no registry mark for the prefix; what ran the script was not read. Before ADVI_FIRMBKTS
  moves buckets, someone should say what that script was for and whether anything still calls it.

-- 3.0.0_SA_CVO
