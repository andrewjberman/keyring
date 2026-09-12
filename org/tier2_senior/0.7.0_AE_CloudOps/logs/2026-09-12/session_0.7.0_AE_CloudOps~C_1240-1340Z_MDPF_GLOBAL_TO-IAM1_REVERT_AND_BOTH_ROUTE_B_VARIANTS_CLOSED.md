# Session log — 0.7.0_AE_CloudOps~C — 2026-09-12 1240–1340Z — TO-IAM1: the revert, and both route-(b) variants closed by measurement

**archetype:** MIXED

**Seat:** `0.7.0_AE_CloudOps~C` · **Face:** `MDPF_GLOBAL.TO-IAM1` amendment 1 @`bcff22b113`
**Issuer traffic this phase:** `1.0.0_SA_CTO` msgs 96105 (revert authorized + one read), 96108 (scope correction + two reads), 96110 ((b2) accepted, nothing further asked)
**Order status at close:** `pending`, **AC4 FAIL**, OPEN on `MDPF_GLOBAL-S3`. Correct per the face.
**Prior logs this session:** `..._1050-1130Z_..._STOPPED_ON_POPULATION.md`, `..._1050-1240Z_..._GRANTED_AND_BLOCKED_BY_A_BUCKET_DENY.md`

## ⚠ A CORRECTION TO AN EARLIER COMMIT IN THIS LANE, CARRIED HERE RATHER THAN IN A COMMIT OF ITS OWN

**Commit `3e65500369`'s SUBJECT is wrong.** It ends *"S5's overreaching headline corrected in place"*, while
that same commit's body states at length — and its diff proves — that `MDPF_GLOBAL-S5` was **NOT** edited:
`surprise-row-gate` refused the in-place rewrite, S5 was restored byte-for-byte, and `MDPF_GLOBAL-S6`
carries the correction citing S5 by id.

⛔ **Why it is worth a line at all:** a subject is what `git log --oneline` shows, so a reader scanning the
log finds the false claim while the contradiction sits one level in. That is the same shape as this order's
own wrong-cause finding (`MDPF_GLOBAL-S2`) — **the durable, most-read artifact carries the false claim and
the correction lives where fewer people look.** I declined an amend (history rewrite on a shared branch)
and declined a dedicated commit (noise); `1.0.0_SA_CTO` 96110 ratified both refusals and directed exactly
this: one line in the next commit this lane makes anyway. This log is that commit.

## The revert (authorized, not unilateral)

Removed `IrptDirectory49fDimsRead` and `IrptDirectory49fDimsListScoped`, plus the `f49_bucket` local they
were the only consumer of — the local is itself a reference to another firm's bucket from this tree, which
is the same hard stop the statements tripped.

`Plan: 0 to add, 1 to change, 0 to destroy` · exactly 2 removed blocks, exactly the 2 intended Sids, 0
added · `Apply complete! Resources: 0 added, 1 changed, 0 destroyed` · 0-diff re-plan clean.
Applied plane: **34 → 32** statements, the five working `Irpt*` grants intact, **0** statements naming
`opal-data-49financial`, all three P0 Deny fences intact.

⚠ **One control I would not overstate:** the "0 added blocks" census has no independent positive control in
that plan, because there genuinely are no additions. The identical regex shape found 25 minus-lines and
resolved 2 blocks and 2 Sids, which validates the **form**, not the zero. Said rather than claimed clean.

Both removal sites carry long in-file notes, deliberately, so a future reader does not re-diagnose this as
a missing grant: the bucket Deny, the host measurement, why the Deny is a control, and the fact that the
data is not reachable another way.

## Route (b), both variants, closed by measurement

**(b1) move the DATA — closed (`MDPF_GLOBAL-S5`).** The five tables exist only at
`opal-data-49financial/gold/advi/dimensions/` (1098 / 1098 / 1098 / 2 / 2). Census of **all 23 prefixes**
this role may read: **0 of 35,538 objects** carry any of the five table names. The legacy shared root
`opal-data-assets/portal/gold/advi/` is **empty** — and *why* it is empty is the answer to whether it
should be refilled: the GOLDHOME re-point (Andrew-direct 2026-08-18, *"Ratified, proceed with the re-point
before the P2 apply"*) deliberately moved the ADVI gold root into the per-client bucket. Re-mirroring would
reverse that ruling **and** stand up a duplicate output path — its own NEVER, with his veto.

**(b2) move the COMPUTE — closed (`MDPF_GLOBAL-S6`).** One permitted principal exists,
`bd-exporter-ec2-role` (ARN matches none of the Deny's four patterns; `advi-49f-chain-access` grants
Get+Put on `gold/advi/*`). It cannot run the build:
1. **No live host** — `EC2_MANIFEST.json` `bd-exporter` → `instance_id: (none)`, against 27 services, while
   five sibling exporters/runners carry live ids, so the absence is specific rather than manifest-wide.
2. ⛔ **It denies itself a destination** — inline policy `cross-firm-bucket-deny`: `Deny s3:*` on
   `opal-data-cot`. Cottonwood is 1 of the 3 destinations. A Deny, not an absence.
3. It also lacks the two INF dims, the 49f xref and COT `fact_allocations` — absences, addable.

⭐ **And the dispatch was never the blocker:** `schedule.tf:180` resolves the target via
`local.irpt_ec2_manifest.services["mdpf-daily-runner"].instance_id`, with `:291`/`:302` pinning the refresh
role to that one instance ARN. **Configuration, not architecture** — so nobody should spend an hour there
later. The firm fences are the blocker.

## ⭐ Why both variants close — the frame, not a footnote

**The directory build is inherently a THREE-FIRM READ IN ONE PROCESS.** It loads 49financial, inflection
and cottonwood identity dimensions together and lands one artifact per firm. The estate's isolation design
is per-firm principals fenced from each other's data: the 49F bucket denies `cot-*`/`inf-*`/`mdpf-*`;
`bd-exporter-ec2-role` denies **itself** cottonwood. **So any single principal capable of this build is, by
construction, the cross-firm hole the design exists to prevent.** Two different mechanisms — a resource
policy on one host, an identity policy on the other — enforcing the same fence is what tells you it is a
design and not an oversight.

That is why there is no clever hosting answer here, and why the real question sits under route (c):
whether this should be three per-firm processes whose outputs are assembled by something that never holds
two firms' identity data at once. **Named, not chosen** — IRPT's architecture and Andrew's call.
`1.0.0_SA_CTO` is carrying the decision to him in these terms rather than as "grant a narrow exception or
give up a leg", because the narrow framing invites the exception by making it look small.

## My own defects this phase

- **S5's headline disposed of (b2) on (b1)'s evidence.** Caught by `3.0.0_SA_CVO` (96106) reading S5 against
  S3 from another project's channel, because six ungradeable IRPT_BCKEND outcomes sit downstream.
  ⭐ The shape is the useful part: this is the **same defect as `MDPF_GLOBAL-S1`** — a claim wider than its
  grounding — twice in one night by one seat, once as a denominator narrower than its population and once
  as a headline wider than its evidence. Recorded as a repetition rather than tidied into two slips.
- **I then fixed it the wrong way**, rewriting S5's fields in place. `surprise-row-gate` refused:
  *"Corrections are NEW items citing the old id; an edited history is a history nobody can audit."* Its
  audited override existed and was **not** used; S5 restored byte-for-byte and the restoration verified by
  parsing the row out of both commits and comparing (**identical: True**). S6 carries the correction.
- **Two counting errors caught before they were reported**: a census helper counted the literal string
  `None` as an object, and `--query length(Contents)` on a paginated list returned **per-page** counts
  (`1000` then `98` for a 1098-object prefix). Both found by reading output instead of exit codes; the
  published figures are client-side and filter the null sentinel.

## Compiler Tools

| tool | invocation | what it decided |
|---|---|---|
| `aws iam get-role-policy` / `list-role-policies` | on `bd-exporter-ec2-role`, `opal-advi-stitch-landing-role`, `consolidation-gold-runner-role` | Answered (i) and (ii). The decisive read was the policy literally named `cross-firm-bucket-deny`. All three carry audited `# rail-checked:` markers — `comp-iam` is declared NOT VALID for this family by the face and **has no bucket-policy or resource-policy surface at all**, which is exactly where this order's blocker lived. |
| `aws s3api list-objects-v2` | 23 readable prefixes + the 5 canonical tables + the legacy root | The 0-of-35,538 denominator that closed (b1), and the empty legacy root. |
| `comp-read` | `schedule.tf --enumerate 'instance\|target\|document'` | Established the dispatch binding as configuration (`:180`, `:291`, `:302`) rather than architecture. |
| `comp-find` | `'portal/gold/advi'`, `'opal-data-49financial' --band CONFIG` | Surfaced the GOLDHOME re-point — the ruling that makes refilling the shared root a reversal rather than a fix. |
| IAM census `docs/briefs/cmpaws-iam-census-20260909.json` | index over roles naming the bucket | Gave the 2-role candidate set **with its vintage stated (3 days)**; both candidates then verified LIVE rather than taken from the index. |
| `surprise-row-gate` | on the in-place S5 rewrite | REFUSED, correctly, and taught the rule at violation time. Override declined. |
| `deploy_ledger.py check` | 6 of 6 sentinels | Confirmed this lane strands nothing; surfaced `opsec-s15-reconciler-function` (another lane's, PAST-WINDOW) as one line to the CTO without chasing it. |

## State at close

- Commits on this order: `70e131626d`, `52986aca17`, `52cb121d0e`, `585a9d24c0`, `3e65500369`, plus this log.
- Channel `org/surprise_channel/MDPF_GLOBAL/INVESTIGATION_v1.md` carries S1–S6.
- Deploy ledger CLOSED, 6 of 6 legs. Two applies and one revert, all 0-diff. Nothing half-landed.
- Delivered and exercised: the two INF dimension reads and the 49f xref read. Applied-verified: the three
  firm destination writes. Dark by design of a control: the 49F dimension leg.
- **Nothing on this order is actionable by an AE lane until Andrew rules.** The AC4 instrument stays in
  `s3://opal-data-mdpf/diagnostics/aec-irpt-iam1/` and is mutant-tested, so re-proving is one SSM call
  whichever way he rules.
- **Push state:** LOCAL. This lane does not push shared branches (LD-0522).
