# /self-drive NFRA_OPSEC202609 -- ticks 11-12 (2026-09-03 ~15:4xZ-16:2xZ), 1.0.0_SA_CTO~Z

state: ARMED | cron 30635e1e (:13/:43) | carrier org/XXX.md CTO row @f41a37322e | paired: solo | last log: tick 10 @f091fc8c54 (+ correction @8a88085266)
scope: NFRA_OPSEC202609 (D12, site-z) -> 1 project (denominator: 1 of 13 live directives) | device SITEZ | completion test: NOT DONE

## The stretch: an Andrew-direct kill, a remediation, and four defects of this seat's own found by other seats

**ANDREW-DIRECT ~14:0xZ** (record @9dbe3652ef, corrected @e11a766aa3): *"ok we need to move along here, i killed the
tier2 workers because we were having API connection issues, I need you to remediate and restart from wherever they
left off with COO, spawning the necessary workers so we can proceed."* Both worker resume points were measured from
the deploy ledgers rather than assumed, the package went to `2.0.0_SA_COO~Z` (19818), and spawning stayed that seat's
act under the standing ruling.

**THE HAZARD, found and now CLOSED.** `terraform import` had put `module.firm_demo.aws_dynamodb_table.partner_table`
into the partner-firms STATE while `infra/aws/terraform/partner-firms/demo.tf` was never committed. Verified on two
instruments: `terraform state list` showed the resource beside the three real firms, `git ls-files` showed it was the
only one of four without a declaration. Discharged at **f570d3981e** by `0.7.0_AE_CloudOps~S` as its first act on
respawn, exactly as sequenced. Verified here four ways before calling it closed: in HEAD by `cat-file -e`, staged
clean, `git status` empty, and `log --diff-filter=A` naming the commit. `3.0.0_SA_CVO~Z`'s row Z-S41 was the durable
carrier and `2.0.0_SA_COO~Z` filed the disarm at Z-S43.

## Four errors by this seat, each caught by a different seat

**1. Severity overstated (Z-S41, corrected @e11a766aa3).** This seat called it "a DESTROY plan against a live
partner-tenant identity table" -- imminent data loss. `3.0.0_SA_CVO~Z` challenged it and flagged that the deciding
value was unmeasured by both of us. Measured here: `DeletionProtectionEnabled: True`, with a positive control on
`opal-partner-49financial` also True. **A destroy would be REFUSED BY THE API.** The true cost was a shared Terraform
root blocked for three real firms -- serious, and not what was claimed.

**2. The chase was unfair (19828, withdrawn in 19832).** This seat asked the COO to "name in one line" what blocked
the spawn. Nothing did: it had seated both lanes at 15:45:34Z and 15:45:44Z, **four minutes before the chase
arrived.** The question implied a delay that did not exist.

**3. The restart instruction was already false when written (19843).** The r2b ledger carried L5/L6 `proof: null` and
this seat read absence-of-proof as absence-of-act, instructing the respawned worker to "re-quote the plan and apply".
`0.0.0_AB_MSTR~Z` found the apply had already run (Z-S42). Confirmed here independently -- PITR ENABLED, five tags,
SSE KMS -- and the instrument the integrator had not reached for settles the timing: **PITR's
EarliestRestorableDateTime is 13:21:50Z, and point-in-time recovery cannot restore to before it was switched on, so
that value IS the apply.** L4 closed at 13:20:39Z, putting the apply about seventy seconds later, before Andrew's
kill. That pin discharged Z-S42's own unmeasured limb and became Z-S44.

**4. v0.9 re-pointed the manifest and never carried the split into the rest of the PRD (fixed in v0.10
@a554b9d197).** `2.0.0_SA_COO~Z` asked before cutting a decomposition against it (19842) and the question found three
things: section 3's OWNS list never gained the new bucket, S28's `accept` read 18 where section 4 stops at 17, and
S5 still named S17 as its `waf-logs/` carrier. **And fixing the third created a dependency CYCLE between S5 and S28,
which this seat caught before commit** -- S28 is an ALIGN on a live bucket and needs nothing before it. Cycle check
across all 28 rows now reads NONE. The COO's unmappable column was `accept` = the section 4 property number, per
section 8's own contract line; its shape (a) and shape (c) were both right at once. Census answered: **20 of 20**,
and it cut v0.1.7 at 03fbe25e92 immediately after.

**THE CLASS, five instances today and now unmistakable:** every one attached a faithfully measured fact to a
consequence the measurement did not establish -- a plan line read as an outcome, a null proof read as a null act, a
worktree count read as a commit count, a subtraction across two planes read as a census. The evidence was never
missing. It was measured on one plane and spent on a claim about another.

## Scope state (denominators printed)

| project | status | dep_stage | faces in flight | rows | ledger |
|---|---|---|---|---|---|
| NFRA_OPSEC202609 | active | EXECUTING (round 2) | TO-OP-S-2 (~Z, ledger open, L1/L2 closed with the rollback exercised FIRST), TO-OP-S-16-17-8R2 + TO-OP-S-25-26-27 (~S), TO-OP-S-1 cut and staged | 44 | 4 rows |

Both worker lanes LIVE and working. Three deploy ledgers open, all inside their windows. Completion test: **NOT DONE**
-- 1 of 1 members REACHABLE, 0 complete. RESERVED cards at Andrew on this scope: **none**.

## Compiler Tools

- resume points: the two `.open_deploys` entries read leg by leg, not the workers' summaries
- the hazard: `terraform state list` + `git ls-files`; closure re-verified by `cat-file -e HEAD:`, `ls-files --stage`, `status --porcelain`, `log --diff-filter=A`
- the severity correction: `describe-table` with a positive control on a sibling firm table
- the apply pin: `describe-continuous-backups` EarliestRestorableDateTime as the applied-at instrument; `list-tags-of-resource`
- v0.10: staged and graded through the conformance limb's real entry point, ran-discriminator present; a manifest-wide cycle check written for the occasion
- push state: LOCAL (0.0.0_AB_MSTR~Z integrates SITEZ; the leg is ASSESS-ONLY and the push was declined at the terminal)
