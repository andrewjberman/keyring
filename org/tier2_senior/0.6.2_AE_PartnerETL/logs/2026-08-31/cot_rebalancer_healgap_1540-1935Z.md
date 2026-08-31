# 0.6.2_AE_PartnerETL — 2026-08-31 15:40–19:35Z — a typo lookup that surfaced MDPF_HEALGAP

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE, IMPLEMENT

## Window

Session start (registration 15:4xZ) to 19:35Z. Prior log: 2026-08-26. Whole session.
5 commits, ~14 significant MCP dispatches, 0 deploys, 0 vendor calls.

## What was asked

Andrew-direct at this terminal, VERBATIM (recorded + broadcast same-turn per org/XXX.md,
committed `c7d3f01ce4`):

> i want you to check the black diamond rebalance endpoint, there was a spelling error in opal
> conservativeo or conservatove, something like this, for cottonwood. find it.

then, after I surfaced that a vendor call needs his per-use word:

> you have egress, go get it

## Answer delivered

`Opal Long Term Conservatiove` — vendor typo for *Conservative*. GUID
`c973839d-c476-4e0f-a43f-40d22526aae5`, `rebalanceModelType=Strategy`, 0 accounts / 0 assignments,
wraps `Opal Conservative Growth` 100%.

**ALREADY CORRECTED VENDOR-SIDE.** Same GUID renamed to `Opal Long Term Conservative` in the 24h
window between the `2026-08-07T06:00:43Z` and `2026-08-08T06:00:44Z` landings; correct on all 13
dates sampled through `2026-08-30T06:00:44Z`.

⭐ **THE EGRESS GRANT WAS NOT SPENT — 0 vendor calls.** Rule 17a keeps the vendor's JSON
byte-for-byte in `opal-data-assets`, so the vendor's own bytes were readable from Opal-owned S3
inside ordinary autonomy. Recorded GRANTED-NOT-EXERCISED so no later reader infers a spend from an
authorization.

## The incident it surfaced

`cot-rebalancer-runner` raised on all 3 invocations 06:00:41 / 06:01:35 / 06:03:26Z
(`RuntimeError: rebalancer /auth/token 200 but no access_token`), landing **0 of 3** bronze feeds
for 2026-08-31 against a 3-of-3 control on 08-30. Cookie healed unattended 11:33:37Z; nothing
re-ran. Became `MDPF_HEALGAP` (D8) on Andrew's word, minted by `0.0.0_AB_MSTR`.

**Severity bounded (my sweep):** 1,659 keys / 41 distinct dates / 2026-07-21..08-30 = 41 calendar
days / **0 fully-missing, 0 partial**. 2026-08-31 is the FIRST hole in the feed's life. This
retired my own earlier "UNKNOWN whether earlier dates are holed" and `1.0.0_SA_CTO` amended the
brief §4 (`20e792edd3`).

**Discriminator I ran** (COO named it as first, on my surface): `bd-cot-keepalive`
2026-08-30T18:00Z→08-31T12:00Z, 19 hourly buckets, **Invocations 4.0 in 19/19, Errors 0.0 in
19/19** (expected 76 at `rate(15 minutes)`, observed 76). RC-B (keepalive gap) **FALSIFIED**;
RC-A (ordering) stands. Gap-sensitivity **BOUNDED** by a negative control: `cot-rebalancer-runner`
in the identical query shape returns **1 of 19 buckets** for a known 18h gap, so a gap renders as
ABSENT BUCKETS, and the keepalive had none. Errors non-triviality shown by the same control
(rebalancer Errors = 3.0 matching its 3 known raises). CVO re-derived independently (`d0cafda69f`);
COO landed `INSTRUMENT_GAP_SENSITIVITY_BOUNDED` (`118e9b30b6`).

**Residual I did NOT close, carried unweakened into the record:** this bounds NON-INVOCATION and
RAISED-ERROR only. It does not bound *invoked, rc=0, vendor touch silently ineffective*.

## THREE ERRORS OF MINE, at the width I made them

**E-1 — a false ORDERING claim about my own act.** I reported my commit as landing ~4 minutes
BEFORE MSTR's 17:39:51Z handoff. Measured: `3e20c92fdf` author==commit date `17:47:08Z` — 7m17s
AFTER. `1.0.0_SA_CTO` caught it by reading commit metadata instead of my report. `0.0.0_AB_MSTR`
had built a scoping ruling on my timestamp and withdrew it publicly; CTO issued a rework, withdrew
it, reinstated it. **Four messages across two senior seats on a minute I never measured.** The tell
was in my own sentence: I quoted THEIR time to the second off a header and MY OWN as "17:3xZ" —
mixed precision inside one comparison maps which half you actually read. Banked to
`feedback_self_subject_claims_measure_before_quoting` as its third form.

**E-2 — I read a comment and called it a declaration.** I claimed `cot-bd-session-trigger` is NOT
Terraform-managed, citing `cot-detection-layer.tf:25`, in my design note §4, in `7572c6d6e2`'s
message, and in msgs 89882/89883. That comment heads a `data "aws_secretsmanager_secret"` block —
its subject is THE SECRET; the lambda appears only as a subordinate clause. The lambda is declared
at `cot-pipeline/lambdas.tf:20-37`. **I never opened `lambdas.tf`.** The brief's L4 and CTO's
ownership routing both inherited it FROM ME — the inherited-claim class with me at the origin.
Found by `2.0.0_SA_COO` (F-1). My "route the cadence to CloudOps" ask is withdrawn; the surface is
mine.

**E-3 — a retrieval I did not read is not a search I ran.** I wrote "the cadence is not in this
repo" and called the 11:33Z heal "n=1". My own `comp-find schedule_expression` sweep had printed
`cot-pipeline/schedule-et.tf:90: cron(30 7 * * ? *)` with
`schedule_expression_timezone = "America/New_York"` ON SCREEN. 07:30 ET = 11:30Z. It was never n=1;
it was a declared TF-managed schedule firing 3.5 min late, already in my hand.

**Caught before escalating (not an error, the control working):** `account_attributes` looked 3
days stale and I nearly filed it as a second hole. Weekday census: **12/12 weekdays landed, 0/4
weekends landed** — a weekday-only feed, trailing absence is Sat 08-29 + Sun 08-30, Monday's date
due 09-01. HEALTHY. The CLAUDE.md trading-calendar NEVER rule is exactly what stopped it, and a
false second hole would have read as corroboration on top of a real one. Not broadcast, so nothing
to retract.

## Root cause as it now stands (COO F-3, better than mine)

An **ORDERING defect**, not only a recovery gap: the runner fires 06:00Z; its session mints
11:30Z ET. It therefore executes 5h30m BEFORE its own daily mint, at **maximum session age
(~18.5h), every single day**. 41 of 41 prior days survived on absolute-lifetime margin, not design.
`cot_rebalancer_runner.tf:171` still reads `PLACEHOLDER 06:00Z -- exact time = CTO/WS-4
chain-timing confirm`; that confirm never happened. Fix is build-ladder RUNG 1 — one
`schedule_expression` — not the new mechanism I proposed. My contribution stands only as the
retry-budget-vs-window diagnosis (`maximum_retry_attempts=2` spent in ~3 min beside
`maximum_event_age_in_seconds=21600`, AWS-capped so uncloseable by that knob) and the dead-guard
precondition.

## The dead guard (accepted, reverted, returns via decomp)

`_already_landed()` calls `get_object` inside a bare `except Exception: return False` on a role
with **no `s3:GetObject`** — measured on the APPLIED plane with controls:

```
s3:GetObject  <stamp key>          -> implicitDeny, MatchedStatements []
s3:PutObject  <SAME key>           -> allowed          (positive control)
s3:ListBucket <cottonwood prefix>  -> allowed
s3:ListBucket <49f prefix>         -> implicitDeny     (negative control, firm-sep holds)
```

So it returned False for every date forever — never skipped, structurally could not — and
**`--force` is inert in the deployed bytes**. This killed my own second-fire recommendation
(it would have doubled vendor egress daily, not skipped). Fixed `3e20c92fdf`, **reverted
`725685f85a`** per CTO's gate so it returns through the D8/COO decomp path. Evidence survives at
`725685f85a`'s parent.

⚠ **The existing unit test was GREEN against the dead guard** because `FakeS3.get_object` succeeds
unconditionally — the fixture grants a permission the deployed role denies. Baseline falsification
run rather than assumed: of the 3 arms I added, **2 FAIL against the pre-fix guard** and the third
PASSES for an unrelated reason; I labelled that third a regression guard, not evidence.

## Deployment Sequence + Verification (AE requirement)

**NO DEPLOY OCCURRED. Nothing was applied to any live surface this session.**
Zero Terraform runs, zero `update-function-code`, zero vendor calls, zero production writes, zero
backfills. `3e20c92fdf` carried **0 deploy-scope files** (`data/*/scripts/{gold,silver,bronze}/*.py`
count = 0), so the pre-push deploy gate had nothing to do and the push deployed nothing; Lambda code
moves by Terraform only. **The live `cot-rebalancer-runner` still carries the dead guard**, before
the commit, during it, and after the revert. DESIRED != APPLIED != EXERCISED — this window produced
DESIRED only, and CTO's "exercise it on a known stamped date" is UNMET by construction.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | A.3 exercise probe | PASS | forwarder RAN (own banner), not just resolved |
| `comp-find` | `-i 'onservat...'`, `--all` | PASS | 1,488 hits / 139,346 files; denominator printed |
| `comp-find` | `-i 'onservatiove' --all` | PASS | 33 hits / 33 shown, found the typo carrier |
| `comp-find` | `rebalance`, `schedule_expression`, TO sweeps | PARTIAL | returned `schedule-et.tf:90` — **I failed to READ it (E-3)**; tool fine, operator not |
| `comp-iam` | `service cot-rebalancer-runner` | PASS | DESIRED plane; `s3:ListBucket [GRANTED]`; own DENY-OVERLAY-INCOMPLETE caveat noted |
| `to-check.py` | `--all --assignee` | PASS | 1 active TO / scanned 2224; THIRD-POPULATION 84 (0 open) bounds the blindness |
| rail gate | fired twice (raw `grep -r`, raw `aws iam`) | PASS | correctly routed; one `# rail-checked:` marker used with a stated reason (condition-key eval is not a comp-iam capability) |

**What worked:** `comp-find`'s printed denominators made the 41-of-41 severity bound trivially
citable. The comp-rail gate fired correctly on both a raw recursive grep and raw `aws iam`
inspection.
**What failed:** nothing in the tools. **Gap found:** `comp-iam` cannot evaluate a request against
an `s3:prefix` CONDITION KEY — it lists perms and reconciles TF-vs-live, but the question "does this
StringLike condition admit this exact prefix" needs `simulate-principal-policy --context-entries`.
That is the documented reason on my one rail-checked marker, not a complaint.

## Blockers

**BLOCKED-ON-ANDREW (evidence-cited, 2 items):**
1. One-shot `cot-rebalancer-runner --date 2026-08-31` — vendor egress + ~89-object production write.
   `1.0.0_SA_CTO` relayed an Andrew GO at 185158Z; I am holding for his direct line in my own
   session because he is LIVE here and confirmation costs one line, while every CTO message today
   carries `Sender-unverified` with no broker row. CTO ACKed the hold as not-a-rejection (89906).
   STAGED: cookie fresh (secret LastChanged 11:33:37Z), 08-31 stamp confirmed ABSENT.
2. `MDPF_HEALGAP` PLACEMENT — open sovereign call; blocks every TO off the decomp. All 10 cells
   declared PENDING-ANDREW.

Not blocked, correctly out-of-lane: the design ruling (`1.0.0_SA_CTO`) and the atom-decomp
certification (`3.0.0_SA_CVO`).

## Current State (zero-prior-context handoff)

- **Live surface UNCHANGED.** `cot-rebalancer-runner` (role `cot-rebalancer-runner-role`) still has
  the dead `_already_landed()`; `--force` inert. 2026-08-31 bronze remains 0 of 3 feeds.
- **My commits:** `c7d3f01ce4` (Andrew-direct egress record), `7572c6d6e2` (design note),
  `863c9b766f` (AMENDMENT 1 retracting my own cost model), `3e20c92fdf` (guard fix),
  `725685f85a` (revert of the guard fix, CTO-validated + ACCEPTED).
- **PUSH STATE, MEASURED:** `725685f85a` is LOCAL. `origin/CLOUD` = `59b1b34540` by COO's
  `git ls-remote` at 19:32:04Z; my own last read was `20e792edd3` at ~17:5xZ. `0.0.0_AB_MSTR`
  offered to sweep the revert into the next window.
- **Guard evidence for the decomp** is recoverable at `725685f85a`'s parent — do not re-derive it.
- **Deliverables:** `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/`
  `ANDREW_DIRECT_20260831_EGRESS_GRANT_BD_REBALANCE.md`,
  `COT_REBALANCER_POSTHEAL_RETRY_DESIGN_20260831.md` (+ AMENDMENT 1).
- **My other TO** `COT_SUPERVISED.G1-G7` reads PENDING but leg G1 is DELIVERED and running as a
  scheduled daily table (`blackdiamond/cottonwood/bronze/account_attributes/`, weekday-only,
  12/12 weekdays landed). No stalled work behind it. **The `<status>` is a claim and is stale.**

## Next Steps

1. **[Andrew]** the 2026-08-31 one-shot (fires immediately on his word) and `MDPF_HEALGAP`
   placement.
2. **[1.0.0_SA_CTO]** design ruling — now with a fifth option (move the fire past the mint, rung 1),
   no ownership blocker (F-1 retired), and the dead-guard precondition.
3. **[0.6.2_AE_PartnerETL, me]** on placement: re-derive the 07:30 ET mint margin
   (`schedule-et.tf:85-88`, EST-worst-case 12:36Z chain-done vs the 13:30Z floor) BEFORE any time
   is proposed. Propose no time until then.
4. **[2.0.0_SA_COO]** atom-decomp remains UNCERTIFIED + SOLO; any TO cut before CVO certification
   carries that on its face.
5. **[me]** correct the stale `<status>` on `COT_SUPERVISED.G1-G7` — record drift, not work.
