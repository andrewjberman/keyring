# 0.6.2_AE_PartnerETL~A -- MDPF_COTREMEDIATION D8: canonical-key repair, two lambda deploys, two root causes

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, VALIDATE

**Window:** 2026-08-26 13:47Z (session start / registration) -> 19:02Z. First log of this session;
prior log 2026-08-21. **Project:** MDPF_COTREMEDIATION / D8. **Lane:** ~A, one project (Rule 27).

---

## SUMMARY

Dispatched a one-file P0 (COO 72168/72188). Returned the reason it would have failed, then found a
second defect underneath it, then a third under that. Two production lambda deploys landed and were
verified on running bytes; both NEVER#6 ledgers opened at deploy-start and closed in-session.

Andrew's ~16:2xZ law ("never postpone to tomorrow what can be done this session") landed mid-window
and paid out inside ten minutes: the ad-hoc QA run it authorized FALSIFIED tomorrow's fire, which we
would otherwise have discovered at 13:31Z with the day gone.

---

## WORK DONE

**1. Startup.** `/watcher` found registration LIVE at PID 24336 with a summary claiming an armed
Monitor, but no `inbox-watch.sh` process existed for the serial. Two spaced probes aged 76s -> 308s
(frozen) and PID 24336 was dead in Windows space -- a predecessor that died ~13:45Z, not a live peer
and not a context-clear. Re-registered (PID 23792), armed Monitor `bfmxloz4l`, confirmed by an actual
`[INBOX]` round trip. Zero crons per XXX.md 1b-F Tier-2 row.

**2. P0 root cause read, not re-derived.** COO's dispatch pointed at commit `@17c38a26f2` (my own base
seat's template amendment). Read it rather than re-deriving the falsified vendor-drift hypothesis.

**3. THE DISPATCHED EDIT WAS ONE FILE. IT IS THREE.** Adding the canonical `by_model` key to
`build_cottonwood_mdpf_slice.py` alone unblocks cottonwood and then fails GLOBAL at a later leg on a
DIFFERENT error -- `dim_mdpf_account_distribution.py:450` unions the new key into `present`, `:451`
appends keys not in `_MODEL_ORDER`, `:461` calls `account_dist_display(mkey,'global')`, and crosswalk
`:201-203` raises `UnknownModelError` for any key absent from `GLOBAL_ACCOUNT_DIST_DISPLAY`. That
presents as the fix working. Grounded on two live artifacts (the sidecar is keyed by canonical
model_key; the served global account-distribution carries exactly the 7 display strings that map
holds). Both crosswalk homes moved together, byte-identical before and after.

**4. The reviewed edit, with the rename check run FIRST.** A rename would make the addition a silent
double-count, so it was tested before anything was added: model_id `09bfd1d1-...` appears in **1 of 29**
dim partitions over the full history 2026-07-21..2026-08-26; nothing was removed that day and no
existing model decreased. CONTRAST CONTROL: the 2026-08-21 reassignment DID show an exact-dollar
handoff, so the instrument can see a rename and saw none here. Composition discriminator (the ruled
test that put two Strategy rows OUT) returned the OPPOSITE result: `fact_model_blend` carries TWO child
rows for the model. Grain corroboration: `as_parent=0 / as_child=N` matches the confirmed canonical
models.

**5. Leg A -- lambda rebuild + apply.** Established that the runner executes the LAMBDA BUNDLE, not the
S3 script prefix, by opening the live bundle. This changed the deploy routing before MSTR filled a
seating that would not have fixed anything. Built at MINIMAL PIN `48c473caa1` (deployed vintage +
3 files, NOT HEAD) after finding that a HEAD build would ship 4,620 insertions including a NO-SHIP
module whose fatal predicate is imported at module level -- converting a 2-scope outage into a possible
4-scope one. Applied, verified on re-downloaded running bytes.

**6. Ad-hoc QA per Andrew's law -- and it FAILED.** Used `{"qa_local": true}` (consolidator :1328-1348,
ZERO S3 writes) rather than the gold-writing form COO had authorized, so tomorrow's acceptance
signature was not spent. Result 6/12, errors cottonwood+global. The original ValueError was GONE
(fix good) but a second defect was exposed.

**7. Second root cause, source-confirmed + itemised to the cent.**
`build_cottonwood_mdpf_pair.py:133` pre-filters accounts by the DIRECTLY-ASSIGNED PARENT model's
opal-ness, then descends the blend at `:159` -- so accounts under a non-Opal container holding Opal
children are dropped before `decompose` runs. WSE_COTMDL's `MODEL_DETAIL_SCOPE` widening (R1+R2, both
landed and exercised) took the blend from 19 parents/8 children to 46/17, making a pre-existing filter
defect reachable for the first time. **WSE_COTMDL is CLEARED** -- I checked whether COO's own
"R1 landed alone" warning had come true and measured it away rather than filing it.
PROVED THE DIM IS NOT INFLATING: `19,900,942.52 x 0.21 + 26,644,993.65 x 0.16 = 8,442,396.91`, exact
against the dim; the unweighted arm was $38.1M away. Full itemisation reproduces production's
`model=$140,410,927.00` to the cent and accounts for the entire 43,676,557.12 delta.

**8. Andrew-ordered sweep (17:56/17:58Z).** 81 distinct names scanned; DIVZ 1 (known), PFOE/PFDE/IDVZ/
Muni 0, Tax 9 (none Opal-shaped; sovereign-confirmed at 18:07Z). Adopted CVO's seed control (grammar
rediscovers the known positive -- FIRES) and reported the uncomfortable half of the substring control:
boundary and substring counts identical on every token, so the discipline is CORRECT BUT INERT on this
corpus, not proven by it. STRUCTURAL FINDING: `fact_model_blend` carries NO child-side `is_opal` and
all 17 child names are absent from the roster -- at child grain a NAME is the only classifier that
exists, which is why the Opal name-scan is load-bearing rather than convenient.

**9. Leg A-Prime.** Held at pre-apply through a `[STOP]` (CTO 72709: the fix imports the NO-SHIP
registry at module level). Measured it independently on the BUILT ZIP -- `mcr.display_label` ABSENT
from the bundle-vintage registry, so the apply would have AttributeError'd at the first cottonwood
call. Rebuilt on the one-symbol re-cut, then again on the DIVZ re-cut; applied at pin `5043bbe8d4`
after seven arms.

**10. Third root cause.** `dim_mdpf_aggregate_aua_timeseries.py:127/:2449` builds global's `by_model`
from a FIXED TUPLE derived from `CANONICAL_MODELS`, NOT the union its own docs claim
(`build_cottonwood_mdpf_slice.py:9-12` asserts union, and its parenthetical accounts 49F+INF only --
cottonwood is not in it). `opal_fixed_income` is the FIRST cottonwood key ever outside that set, so it
enters `model_aua` (a sum) but not `by_model` (a fixed iteration): delta exactly -8,442,396.92. Then
answered COO's three gating schema questions by MEASUREMENT -- the needed shape already exists in that
file and is used twice (the inflection blends: `model_id=None, served=False`, appended past the
registry filter), `SERVED_MODEL_KEYS` is NOT touched so 49F/inflection are structurally unaffected and
`0.7.0_AE_CloudOps~K`'s 12:45Z AC4 holds by construction.

---

## COMPILER TOOLS

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-which | `comp-which "how do I grep the repo"` | PASS | XXX.md A.3 mandatory EXERCISE (resolution is not execution) -- forwarder ran, produced its own banner |
| comp-find | `comp-find MDPF_COTREMEDIATION --files` | PASS | first-contact map: PRD, project JSON, both TOs, both change-mgmt ledgers |
| comp-find | `comp-find opal_ultra_short_term --files` | PASS | found the downstream key ecosystem (crosswalk, category registry, account-distribution) -- this is what surfaced the 3-file coupling |
| comp-find | `comp-find fact_model_blend --band DEF` | PASS | measured ZERO over 26,736 files with denominator printed; correctly a real absence (table is silver data, not a DEF) |
| comp-pipescript | `deployed build_cottonwood_mdpf_slice.py --pipeline mdpf` | PARTIAL | reported STALE; verdict later shown FALSE (see Gap) |
| comp-pipescript | `deployed mdpf_revamp_model_crosswalk.py --pipeline mdpf` | PASS | MATCH; also printed the two DECLARED-UNSWEPT channels that led to the bundle finding |

**What worked.** `comp-find opal_ultra_short_term --files` is the single highest-value call of the
session -- it turned a one-file dispatch into a three-file diagnosis by showing which consumers read
the key. `comp-pipescript`'s DECLARED-UNSWEPT lines were honest about their own blind spots and are
what pointed me at the lambda-zip channel.

**What failed.** `comp-pipescript deployed` reported STALE on
`code/scripts/assets_gold/build_cottonwood_mdpf_slice.py` for a file that WAS correctly deployed. It
compares a CRLF working-tree file against an LF S3 object, so the verdict can never turn green no
matter how many times the file is uploaded. Verified by CONTENT: normalised md5 identical on both
sides (`82d08cf2...`), the S3 copy carries the fix, and its 58,961 B ties to the lambda bundle's copy
independently -- three signals, one conclusion.

**Gap found (2, both routed, one already fixed).**
1. CRLF false-STALE inside a comp-tool's VERDICT. Reported 72464; `0.8.0_AE_CloudComp~F` FIXED it
   `@739c1ad8f9` and refined my exposure figure from 16 CRLF files to **4 confirmed false STALEs**,
   two of which lie OUTSIDE the three trees my census scoped -- their number is the better one.
   Defect is ONE-DIRECTIONAL: a STALE can be false, a MATCH remains trustworthy.
2. **`comp-pipescript` MATCH is TRUE AND SILENT ABOUT THE LAMBDA.** It certifies the S3 code tree; the
   runner executes a bundled zip. Distinct from (1) and pointing the opposite way -- (1) is a false
   alarm, (2) is a false all-clear. Surfaced to COO/CTO; covered by the bundle-channel doctrine on the
   record, no new filing requested.

---

## DEPLOYMENT SEQUENCE + VERIFICATION (AE role addition)

### DEPLOY 1 -- Leg A (canonical key), ledger `@1e73554830`

Sequence: mint minimal pin (isolated worktree, `48c473caa1` = deployed vintage `530ba66971` + 3 files)
-> `build_package.py --pin` -> pre-apply zip diff vs deployed bundle -> upload artifact with
`--metadata content-sha256` -> set `MDPF_GOLD_COMMIT` from the pin actually built with -> targeted
`safe-apply` -> post-apply proof on re-downloaded bytes.

ACTUAL OUTPUT:
```
Plan: 0 to add, 1 to change, 0 to destroy.
Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

POST-APPLY (re-downloaded running bundle):
  LastModified   2026-08-25T19:38:55Z -> 2026-08-26T15:29:34Z
  CodeSha256     UVT5XRX3R2O3zsr+g2QTPrD2DDYlQilSP+IfmjD2mIc=
              -> 3/897ecG2Xzal+0Xl+Ygoshsqccd6smAcMwygv8KjZQ=
  CodeSize       684,807 -> 701,490 (= the built zip exactly)
  build_cottonwood_mdpf_slice.py  opal_fixed_income  FALSE -> TRUE
  mdpf_revamp_model_crosswalk.py  opal_fixed_income  FALSE -> TRUE
```
Control was real: pre-state read FALSE on both modules. Also fixed a live drift found in passing --
`MDPF_GOLD_COMMIT` claimed `1daf1913dd` while the deployed zip's own manifest said `530ba66971`, so
every A6 run manifest had been stamping a vintage its own bytes did not match.

### DEPLOY 2 -- Leg A-Prime (decomposition fix), ledger in `@1b76475372`

Seven pre-apply arms, all against the DEPLOYED bundle: MEMBERS diff (1 file + manifest, nothing rode
along) / NO-mcr-import by AST over ALL scopes / SYMBOL CLOSURE 17 refs 0 ABSENT / cited literal with 0
live `display_label` call sites / NEGATIVE CONTROL / DIVZ placement / `sys.modules` post-apply.

ACTUAL OUTPUT:
```
Plan: 0 to add, 1 to change, 0 to destroy.
Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

POST-APPLY (re-downloaded running bundle):
  LastModified   2026-08-26T15:29:34Z -> 2026-08-26T18:21:12Z
  CodeSha256     3/897ecG2Xzal+0Xl+Ygoshsqccd6smAcMwygv8KjZQ=
              -> LdShsMmFvrPHq7aW8zCI1zIN7o4YdgkRHHlpFfPO/xs=
  CodeSize       701,490 -> 723,461 (= the built zip exactly)
  MDPF_GOLD_COMMIT 48c473caa1... -> 5043bbe8d47e0a0948d6896c3092c576fa28494a
  :133 pre-filter as LIVE CODE (AST)   True -> False
  cited literal absent -> present; live display_label calls 0; mcr import nodes NONE
  OPAL_SMA_LEAF_KEYS (DIVZ -> meta.sma_l0)  absent -> present
```
NEGATIVE CONTROL, and it is the arm that makes the rest mean anything: ARM 2 was FIRST POINTED AT THE
RUNNING COPY, which predates the `mcr` import entirely and therefore could never have shown the arm
firing. Re-subjected at the superseded build `e9d7c37976` it FIRES at line 66. An arm that cannot fail
is not a control.

Both ledgers: opened at deploy-start, CLOSED in-session, no leg stranded. Rollback available and
unexercised (COO ruled NO ROLLBACK -- reverting restores TWO failures instead of one).

---

## FILES MODIFIED

See commit messages: `ae106b1124`, `041969c39a`, `1e73554830`, `1b76475372`. Extra context:

| File | Note |
|---|---|
| `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py` | +28/-0, of which exactly TWO lines are non-comment (the CANONICAL_KEY + DISPLAY_NAME entries). CRLF file -- preserved 1006 -> 1034, 0 bare LF |
| `data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py` | GLOBAL_ACCOUNT_DIST_DISPLAY entry |
| `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/mdpf_revamp_model_crosswalk.py` | SAME edit, second home. Byte-identical before (`d43c99ac`) and after (`0d8980b1`) |
| `infra/aws/terraform/mdpf-pipeline/gold-lambda.tf` | MDPF_GOLD_COMMIT set from the pin actually built with, twice |

---

## MCP TRAFFIC

~95 messages handled, all ACKed on the READ clock. Significant only:

- COO 72168 DISPATCH (D8 seating) · 72188 P0 sharpened · 72284 RAVC2-ACCEPTED · 72320/72361 deploy-lane
  rulings (Leg A mine; minimal pin) · 72878 sequencing · 73083 NO ROLLBACK
- CVO 72185 independent 13:50Z read (SPLIT 2 PASS) · 72304 lane correction (ACCEPTED) + book-move ARMED
  · 72444 withdrawal of its own :994 signature after my falsification · 73125 file-geography correction
  (ACCEPTED)
- CTO 72596 NO-override ruling · 72684 Leg A-Prime is AE · 72709 `[STOP]` · 72723 one-symbol re-cut
- Andrew-direct relayed x6: Opal Fixed Income is a Custom Model (15:2xZ) · never-postpone law (16:2xZ) ·
  Client-Opal-Supervised segment (16:34Z) · MP layering L0/L1/L2 (16:36Z) · DIVZ is an Opal SMA
  (17:42/17:45Z) · sweep items closed + "all recs approved", SERVE conditional-YES (18:07/18:10Z)
- Issued: 72277 (3-file finding), 72359 BLOCKING (HEAD build unsafe), 72563 (ad-hoc failed), 72575
  (which side moved), 73063 (global root cause), 73092 (three schema questions answered), 73115
  (covered-set risk), 73133 (my own citation degradation)

---

## BLOCKERS

**NONE at this seat.** Two items are open and both are correctly owned elsewhere:

1. **Global 9/12** -- the `GLOBAL_MODEL_KEYS` fix is a Rule 24 schema act. `1.0.0_SA_CTO` rules the
   shape; `0.4.0_DS_ClientPlatform~T` holds the lane. Evidence-cited, not assumption-blocked: cause is
   source-confirmed at file:line and all three gating questions are answered by measurement.
2. **SERVE** -- Andrew's conditional-YES turns on a green grade we do not have. Sovereign, not blocked.

---

## CURRENT STATE

`mdpf-gold-lambda` is RUNNING the Leg A-Prime bundle: `CodeSha256
LdShsMmFvrPHq7aW8zCI1zIN7o4YdgkRHHlpFfPO/xs=`, `LastModified 2026-08-26T18:21:12Z`, `CodeSize 723,461`,
`MDPF_GOLD_COMMIT 5043bbe8d47e0a0948d6896c3092c576fa28494a`. Built from ephemeral pin `5043bbe8d4` on
retained branch `legA-prime3` (the branch MUST stay -- the vintage stamp and in-zip manifest both cite
it). Artifact at `s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip` VersionId
`hAFXzyqIdtpFHJDPahO6QOuRWf.fnfJF`; rollback is the prior VersionId
`uGLKSxGv0WkvTRNfQQznjaOOzFvsCm8m` plus reverting `MDPF_GOLD_COMMIT`, one `safe-apply`.

A9 graded by `0.4.0_DS_ClientPlatform~T`: **cottonwood GREEN** (identity gate flipped FAIL->PASS on the
SAME comparison that failed at 43,676,557.12; delta 0.0100 present, 43676557.1200 ABSENT),
**global FAILS** -> 9/12, `errors=['global']`, A9 NOT MET, serve does not fire.

Global's cause, source-confirmed: `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:127`
`GLOBAL_MODEL_KEYS = SERVED_MODEL_KEYS + (2 blends)` and `:2449 for mkey in GLOBAL_MODEL_KEYS:` --
global's `by_model` is a FIXED TUPLE, not a union. `opal_fixed_income` is the first cottonwood key
outside it. Remedy shape (measured, not ruled): `ModelEntry("opal_fixed_income", None, "Fixed Income",
"model", False)` in BOTH crosswalk homes + append to `GLOBAL_MODEL_KEYS` -- THREE file-edits, and
`:2450 entry_for_key(mkey)` makes register-and-append ONE change (both partial states fail loud; the
two-homes divergence is the QUIET one).

All four commits are LOCAL on CLOUD and ride integration (integrator-only push gate).

---

## NEXT STEPS

1. **[1.0.0_SA_CTO]** Rule whether `opal_fixed_income` takes the inflection-blends' shape. Facts are in
   73092; file geography corrected in 73133 (three files, two of them the crosswalk's byte-identical
   homes).
2. **[0.4.0_DS_ClientPlatform~T]** On CTO's ruling, write the three-file edit; run my 73115 test in the
   SAME turn -- list dates where `opal_fixed_income` `model_value` is None AND the date is in
   `meta.covered_dates` AND the label is not `interpolated_estimate`. Non-empty = the exact set the
   global fold will mark as gaps (`:2470-2500`, `gap = True` branch).
3. **[3.0.0_SA_CVO]** Verify the 2026-08-27 13:30Z SCHEDULED fire on the pre-registered absolute bar.
4. **[0.6.2_AE_PartnerETL~A, me]** Reachable, holding diagnosis context + rollback. Andrew authorized
   ONE BD dim-436 catalog READ (CALL 2, 18:10Z) with `2.0.0_SA_COO` dispatching the executing seat and
   the g4/probe tooling context in this lane -- NOT started, awaiting that dispatch.

---

## SELF-CORRECTIONS THIS WINDOW (4, all mine, all caught before they load-bore)

1. **$38,103,539.26 residual -- WRONG, true value $2,869,379.04.** I named "full account value minus
   the Fixed Income slice" after the segment Andrew had defined twenty minutes earlier; the bulk of it
   is OTHER Opal models. Two Tier-1 seats had already quoted it and one CERTIFIED it as corroboration.
   Caught by itemising, corrected in the handover's s.1 so it reached both seats before a third quote.
   **This is `feedback_residual_bucket_is_a_claim_not_a_remainder` firing with the memory in context** --
   memory updated with the instance and with why the guard did not fire (it must trigger on output that
   looks RIGHT, not output that looks wrong).
2. **A5 denominator** -- gave `$2,869,379.04` as "across all 129 dropped accounts"; it is the 2-account
   non-Opal-parent subset. Second denominator error on the same finding.
3. **Ledger corrupted by an UNQUOTED heredoc** -- bash command-substituted every backticked term in my
   replacement strings and SILENTLY DELETED them, leaving grammatical rows with values gone. Rewrote
   with a non-shell writer; disclosed in the ledger and the commit. Failed LOUD only because none of the
   eaten terms was a real command. **My first check for the damage (grep for empty backtick pairs) found
   NOTHING -- bash consumes the whole construct, so the obvious detector cannot see it.**
4. **Citation degradation, mine, on restatement.** 73063 named
   `dim_mdpf_aggregate_aua_timeseries.py:127` correctly and in full; 29 minutes later 73092 quoted the
   crosswalk and wrote a bare "`:127`", which reads as crosswalk:127. Both sites sit at line 127 of
   their own files. Caught by `3.0.0_SA_CVO` 73125. **No relay to blame -- I was the source, I was
   correct, and I corrupted my own record restating it.**

Three probes also returned uniform $0.00 on BOTH arms before the instrument was right (leading-space
join, masked `Account Number`, roster-only name map). Each time the UNIFORMITY is what stopped a wrong
number being quoted -- a uniform result across both arms is an INSTRUMENT signature, not a defect
signature. The one figure quoted without that guard is the one that was wrong.
