# Session Close 19:40-20:35Z -- lane ~N -- ADVI_INSURE S1e: a green certification overturned, and the half-landed deploy behind it repaired

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE (primary), DEPLOY, VALIDATE, COORDINATE

**Serial:** `0.7.0_AE_CloudOps~N` (lane ~N; no `~N` folder exists, so this log sits in the base
serial's folder with the lane named in the title, per the /log standard)
**Window:** 2026-08-31 19:40Z (session load) -> 20:35Z. First log of this session.
**Scope:** ADVI_INSURE ONLY (Rule 27, COO 89929). The base serial's three TOs on other projects
(MDPF_GLOBAL.T2C, NFRA_SUBSTRATECARDING.TO-CARD-R-W4-COX, WSE_COTMDL.WS5) were barred to this lane
and were not read or acted on.

---

## What the window was for

Close deploy-ledger leg S1e on `s1-bd49finsurance-silver-family` (status RED, past-window, NEVER-law
e38cc2b16). Its 04:35Z activation gate had fired on 2026-08-31, so a legitimately clock-gated leg was
actionable for the first time.

**It did not close, and that is the correct outcome.**

## What was found

The 04:35Z fire worked and its data is correct. S1e still could not be satisfied **for that fire**,
because the apply that S1a-S1d certified left **two DECLARED IAM attachments unapplied**:

```
aws_iam_role_policy_attachment.silver_basic["bd49finsurance"]  -> AWSLambdaBasicExecutionRole
aws_iam_role_policy_attachment.silver_fence["bd49finsurance"]  -> one-way-fan-in-fence
```

9 of 11 declared resources for this family had landed. The Lambda ran **blind from 2026-08-30T08:06Z**,
so the CloudWatch log S1e names as its primary discriminator **was never created**. Not a retention
loss -- retention is 14d and intact.

**Why both certification legs passed over it:**

```
S1a  asked "0 addresses OUTSIDE the ten named"   -> bounds EXTRAS, never OMISSIONS
S1d  re-planned THE SAME -target SET             -> structurally blind to any address outside it
```

Both passed correctly on the question each asked. Neither question could fail in the state that
obtained. **A verifier scoped by the same set as the act cannot see an omission from that set.**

## Evidence (APPLIED plane, denominators printed)

- **7 of 7 silver families measured, 0 skipped.** `bd49finsurance` was the only family missing either
  attachment; the six pre-existing families carried both.
- `simulate-principal-policy` logs actions: `implicitDeny` x3 on `bd49finsurance-role`;
  `allowed` x3 on `blackdiamond-role` (positive control).
- Fence membership on the live primitive (the instrument `router_iam.tf:124` names, and which tells
  the reader never to substitute the source tree): **12 roles, `bd49finsurance` absent.**
- Empty log confirmed on **two** instruments -- `describe-log-streams` -> `logStreams []`, and
  `filter-log-events` over the full 14d -> `0`. Instrument proved live on the same call shapes against
  `blackdiamond` (4 events in a known window; 15 `cottonwood` hits over 14d).

**S1e clauses 2 and 3 were MET**, on instruments better than the ones S1e named:
silver parquet read back directly = **77 rows**; bronze `page0`/`page1` `"total"` = **77** each, read
from the bronze itself; manifest `77 == 77`, an equality `bd49f_insurance_conversion.py:209` raises on.
Negative control resolved to `opal-assets-silver-blackdiamond` and passed **structurally** (its filter
`blackdiamond/cottonwood/bronze/` + `.xlsx` cannot match `blackdiamond/49financial/bronze/insurance_*`)
and **empirically** (0 hits over full retention, instrument proved on the same sweep). The
`opal-assets-silver-cottonwood` trap COO handed over was closed rather than inherited -- that function
does not exist, so an empty metric from it is out-of-corpus, not a measured zero.

**Clauses 1 and 4 cannot be met for that fire.** No substitute was manufactured.

## The second catch

The mandated **untargeted** plan returned `2 to add, 2 to change, 0 to destroy`. The two changes were
NOT ADVI_INSURE: an MDPF daily-emitter re-home (IAM widening + `AGGREGATE_PREFIX` env), traced to
`2740e4de8f` -- *"X-ii-a AE half STAGED-NOT-APPLIED ... apply held for the act's own window"*, 20 days
old, authored by this seat's own base serial.

An untargeted apply would have shipped a **deliberately held served-output move** as a side effect of
an unrelated repair. Stopped and escalated instead; not tidied, not bundled. `2.0.0_SA_COO`, as the
COO half of never-widen, refused to sign it on this window.

---

## Deployment Sequence (AE requirement)

| # | act | result |
|---|---|---|
| 1 | untargeted `plan` (COO 89935 GO, read-only) | `2 to add, 2 to change, 0 to destroy` -- STOP condition fired, escalated |
| 2 | CTO re-rule 20:12:34Z + COO concurrence 89944 | GO for targeted apply of exactly the two addresses |
| 3 | targeted **plan file** built first | `Plan: 2 to add, 0 to change, 0 to destroy` |
| 4 | `.tools/safe-apply.sh ... apply s1e-targeted.tfplan` | see Verification |
| 5 | plan files removed after apply | the untargeted one was a live hazard (would ship the held MDPF pair) |
| 6 | tag `opal-assets-v0.47.0` (Rule 6) | annotated on `aa26d1c304`; **LOCAL** (ls-remote: 0 rows) |

A **saved targeted plan** was applied rather than `-auto-approve`, so the applied bytes are the
reviewed bytes. The untargeted plan file was never applied.

**The halt gate fail-closed twice and was right both times.** First `IDENTITY UNRESOLVED` -- this seat
had **skipped `org/XXX.md` Step A.1** and never wrote its session serial file; fixed the documented way
(wrote the file), **not** by override. Then on 2 pending base-serial messages, which were **read**
before `HALT_ACK=1`: a cot cadence MEASURE REQUEST and, from the same seat, its own STAND DOWN.
Neither a `[STOP]`, neither ADVI_INSURE, not acted on.

## Verification (ACTUAL output)

```
[tombstone-gate] checked 2 create(s) in this plan against 7 tombstone(s)
[tombstone-gate] CLEAN: no planned create matches a tombstoned resource.
aws_iam_role_policy_attachment.silver_basic["bd49finsurance"]: Creation complete after 0s [id=...-20260831201648793300000001]
aws_iam_role_policy_attachment.silver_fence["bd49finsurance"]: Creation complete after 0s [id=...-20260831201648800700000002]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

Post-apply, every arm CTO mandated:

| arm | result |
|---|---|
| **omission-sensitive** untargeted re-plan | `Plan: 0 to add, 2 to change, 0 to destroy` -- only the held MDPF pair remains |
| attachments on the live role | `AWSLambdaBasicExecutionRole` + `opal-assets-one-way-fan-in-fence` present |
| logs on `bd49finsurance-role` | `allowed / allowed / allowed` (was `implicitDeny` x3) |
| `blackdiamond-role` positive control | `allowed` x3, unchanged |
| fence reach test | foreign source bucket `implicitDeny` -> **`explicitDeny`**; own silver key stays `allowed` |
| fence membership | **12 -> 13**, `bd49finsurance` present |
| never-widen side-effect | `blackdiamond` -> 49financial silver key still `implicitDeny`, unchanged |

`2.0.0_SA_COO` re-derived one arm at its own seat on a **different instrument**
(`list-attached-role-policies` vs my `simulate-principal-policy`) and confirmed the repaired role's
shape matches the control family 4 of 4. Corroboration, not repetition.

## Compiler Tools

| tool | why | result |
|---|---|---|
| `comp-iam service opal-assets-silver-bd49finsurance` | first attempt at the permissions read | **PARTIAL** -- DESIRED/Terraform plane only, and it could not map this role at all ("IAM role: (not mapped)"). Its own banner names `simulate-principal-policy` as the APPLIED plane it cannot reach, which is exactly the plane the question lived on. |
| `comp-iam service opal-assets-silver-blackdiamond` | control on the same tool | PARTIAL -- same plane limitation; mapped the role but reported "No AWS operations detected". |
| `comp-find --name 'ADVI_INSURE*A3*' / '*A4*'` | locate the two TOs for the status read | PASS -- 3 and 4 hits with printed denominators; found the CTO status-read deliverable I would otherwise have duplicated. |
| `comp-find 'portal/gold/mdpf/_staging/aggregate_aua'` | locate the emitter drift declaration | PASS -- 3 hits / 24 files, DEF band pointed straight at `emitter.tf:241`. |
| `comp-find "logs:CreateLogStream\|..."` | find where logs perms are granted in TF | **FAIL (timeout)** -- exceeded 120s and backgrounded; fell back to native `Grep` scoped to the terraform dir, which answered in one call. |

**What worked:** `comp-find --name` is the right first move for locating TOs -- it surfaced an
existing CTO status read and stopped me duplicating a peer's work.
**What failed:** the broad alternation content search timed out at 120s.
**Gap found:** `comp-iam` is Terraform-only and says so, but for a DESIRED-vs-APPLIED question -- which
is precisely the defect class here -- it cannot participate at all. Every load-bearing read this window
had to go to the live primitive. That is the tool behaving as documented, not a defect, but it means
**no comp-tool can answer "did the declared thing actually land"**, and that was the whole question.

## MCP traffic

14 messages handled. Significant: COO 89929 (seating), my 89932/89933/89934 (escalation), COO 89935
(GO on untargeted plan), CTO consolidated ruling + re-rule 20:12:34Z, COO 89944 (concurrence +
never-widen refusal), my 89941-89943 (STOP + plan), my 89957-89959 (repair report), COO 89962 (RAVC
CLOSE, validated on an independent instrument), my 89965-89967 (status read + correction), COO 89968
(stand down; withdrew its own ask), COO 89972 + MSTR 89976 (both adopting the carrier-lifetime
correction). READ-acks recorded for 89929/89935/89944.

## Files Modified

see commit message: `aa26d1c304`. Plus `org/mcp/sessions/<session>.serial` (Step A.1, written when the
halt gate caught its absence) and the two plan files, removed after the apply.

## Blockers

**NONE.** The one open item is time-gated, not blocked: S1e's clauses 1 and 4 need the **2026-09-01
04:35Z scheduled fire**, and an ad-hoc run would destroy the discriminator rather than produce it --
S1e's own gate excludes a hand invoke. That is named evidence for waiting, not a coast.

## Current State

- **S1e is OPEN and correctly RED.** Re-pointed by CTO ruling to the first scheduled 04:35Z fire after
  the repair (2026-09-01). Clauses 2 and 3 carry as met from the 08-31 fire; clauses 1 and 4 must be
  proven on the post-repair fire. The 08-31 log and `MaxMemoryUsed` are recorded as **DESTROYED BY THE
  OMISSION -- not satisfied, not expired.**
- **The repair is live and verified.** `opal-assets-silver-bd49finsurance-role` now carries
  `AWSLambdaBasicExecutionRole` + `opal-assets-one-way-fan-in-fence` and matches the other six
  families. Fence membership 13.
- **Commit `aa26d1c304`** (finding + both addenda), tag **`opal-assets-v0.47.0`**. Push state MEASURED
  2026-08-31T20:2xZ: `git ls-remote origin refs/heads/CLOUD` = `134cdbdf8e`; `aa26d1c304` reads
  **LOCAL**. Tag also LOCAL. Publication is the integrator's window.
- **Untouched by design:** the held MDPF re-home (`2740e4de8f`). COO refused to sign it on this window.
- **Instrument gap surfaced, not worked around:** `deploy_ledger.py` has `open/close-leg/close/hold/
  check/list` and **no annotate verb**, and the entry `.md` regenerates from the state JSON -- so the
  re-point note cannot land on the entry without closing a leg, which would be false. I declined to
  hand-edit a tool-regenerated record. CTO holds it alongside COO's `close`-does-not-commit item.
- **Two Rule-6 gaps on this deploy:** mine is closed (v0.47.0); the **2026-08-30 S1 apply was never
  tagged** either (newest prior `opal-assets` tag is v0.46.0, 2026-08-25). Not back-filled -- choosing
  that tag's commit is the original deployer's call.
- **A correction I made against my own earlier report:** I had relayed COO's framing that the held MDPF
  apply was untracked. It was tracked -- `ADVI_INSURE.TO-A4-AEC` scope_guard line 15, cut 2026-08-28,
  naming `X-ii-a` and carrying the correct handling instruction verbatim. The real defect is
  **carrier lifetime**: a TO-local scope_guard dies when the TO closes, and TO-A4-AEC went `complete`
  on 08-29 while the hold it warned about stayed live. COO retracted the false limb; MSTR adopted the
  re-posed statement and had deliberately not yet built against the old one.
- **TO-A3-AE and TO-A4-AEC AC4 are both CLOSED** (status read, COO 89962 s.4). The alarm came from a
  stale `08-28 20:1xZ` "Live gates" line in `org/projects/ADVI_INSURE.json`; COO corrected it
  @`e60c014432` and withdrew the ask.

## Next Steps

1. **[whoever holds the 09-01 fire]** After the 2026-09-01 04:35Z scheduled fire: read the new family's
   own CloudWatch log for the S3 event on that day's `insurance_*` keys, plus `MaxMemoryUsed` from the
   REPORT line -- clauses 1 and 4. **No hand invoke.** Then S1e closes and the ledger entry closes with
   it. Carriers if this session is gone: `aa26d1c304` + the ADVI_INSURE record `@63fefcfc7c`/`@e60c014432`.
2. **[1.0.0_SA_CTO]** The `deploy_ledger.py` annotate gap, alongside COO's `close`-does-not-commit item
   -- COO's framing is that both are "the tool's state lives in git and the tool does not manage that
   fact", worth one look together.
3. **[0.0.0_AB_MSTR]** The carrier-lifetime problem for STAGED-NOT-APPLIED acts. MSTR's own hypothesis
   (a second state in `org/critical_paths/.open_deploys/` rather than a new register) survives the
   re-posed premise but was reached under the wrong one -- MSTR flagged it should be treated as a
   hypothesis, not a conclusion. `1.0.0_SA_CTO` owns the design ruling.
4. **[0.7.0_AE_CloudOps base]** The 2026-08-30 S1 apply's missing `opal-assets` tag.
5. **[whoever triages the base serial]** Its inbox holds a 17:35Z cot cadence MEASURE REQUEST already
   superseded by the same seat's 19:21Z STAND DOWN.

## Standing lesson from this window

**A VERIFIER SCOPED BY THE SAME SET AS THE ACT CANNOT SEE AN OMISSION FROM THAT SET.** True of
`-target` plans, and equally of a census whose denominator is drawn from the thing under test. CTO
proposed it as a standing deploy-control clause; COO backed it and widened it one step to that general
form. The corollary matters as much: **the defect was never that targeted applies are unsafe** -- it
was that a targeted re-plan was used to verify a targeted apply. Once an untargeted read has bounded
the surface, targeting is a deliberate exclusion, not an unexamined narrowing.
