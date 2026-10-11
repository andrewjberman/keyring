# ADVI_COTBKF round 61 -- L9 grade of CB61bi1-AC2 (the registry attribute for the CRM-scope selector)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T07:01:23Z. Row ADVI_COTBKF-D2-S94.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_61_DRAIN_END_20261011.md @004f8ae2ce (msg 4329)`; record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~88/CRM_SCOPE_ATTRIBUTE_RULE24.json`.

| limb of CB61bi1-AC2 | verdict | this seat's evidence |
|---|---|---|
| the row chosen is the row the selector chose before 5f962296ae | **MET** | The old selector (`s3-lgic-firm-buckets.tf:197` at `5f962296ae^`) took the managed FIRM rows carrying `masters`. Commit 5f962296ae adds `masters` to the inflection row only. Before it, cottonwood was the one managed row with masters. At HEAD the new selector (`:198`) takes the row whose `restricted_prefix_hosts` holds `commonwealth`: cottonwood, and no other of the 4 FIRM rows carries the field |
| each postulate's evidence resolves at its cited line, and the subtraction ran over every scope row | **MET** | This seat printed the cited lines: `scopes.json:162-171` (the cottonwood row, its bucket, manager, masters and the new field), `systems.json:73` (the key `commonwealth`), `lib/opal_naming.py:459-462` (the masters check), the `.tf` at `:96`, `:199`, `:200`, `:207`. Each says what the record claims. The subtraction is 14 rows less 1 |
| the token census carries denominators and the name collides with nothing | **MET** | The record's census before the edit: 0 hits in 79,319 files. This seat's census now: 16 hits in 11 of 88,149 files, every one this cell's own (the `.tf`, `scopes.json`, the record, the proof, the orders, the packet, the ruling and inbox copies) |

**Verdict: CB61bi1-AC2 MET.** `lib/opal_naming.py validate` reads OK (54 system rows, 14 scope rows, 0 warnings) on this seat's run.

## The record's own caveat, which stands

No validator reads the new field. `validate` passes with it, without it, or with a value that is no `systems.json` key. A hand
edit that sets it on the wrong firm row would point the three Deny statements at that firm's bucket, and `one()` guards only the
count of rows. That is a follow-on for the registry's owner (a validate limb: every value is a systems key).

## Not graded here

CB-bi-2 is stopped with its AC1 reading FAIL as written; its judgment criterion is not owed until the order is complete. This seat
ran no terraform command and did not read the plan proof.

---

# Addendum: CB61bi2-AC2 (the plan proof), graded 2026-10-11T08:40:26Z

**Input:** msg 4496 (CB-bi-2 complete @f7badf1aae), updating the round 61 packet @004f8ae2ce (msg 4329); report `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB2/shared_infra_plan_proof.md`. Row ADVI_COTBKF-D2-S102.

| limb of CB61bi2-AC2 | verdict | this seat's evidence |
|---|---|---|
| the watched pattern covers the CRM restricted-prefix statements, the break-glass role and the firm bucket policies, each named by address | **MET** | The report lists 12 watched addresses. This seat read the plan JSON itself: both break-glass addresses and both firm bucket policies are in it. The CRM statements are not a resource; they are 3 Deny statements inside the cottonwood firm bucket policy, whose text is equal before and after |
| the control of step 2 is real | **MET** | At the branch base the old selector line fails `one()` at init with 2 managed firm rows. That is the same selection this seat derived for CB61bi1-AC2 (cottonwood and inflection, both carrying masters) |

**Verdict: CB61bi2-AC2 MET.** The selector fix moves none of the resources it feeds: 10 of 10 firm-bucket rows read no-op.

## What the plan also shows, which is not this criterion

- **Two creates are the break-glass role and its policy.** They exist in code only (rows D2-S93 and D2-S95, ARMED). The third Deny
  statement names that role as the one writer of the restricted prefix; with the role absent, no principal passes it. That fails
  closed.
- **The other two changes are this box's credentials, not the estate:** the plan wants to create the portal bucket and replace its
  encryption configuration because two reads were denied (row D2-S92, ARMED). An apply of this root from dell2 would act on them.
  The CTO has ruled that no seat applies it from dell2.
- This seat ran no terraform command. The plan JSON is the applier's artifact, read here.
