# 1.0.0_SA_CTO -- session 2026-08-25 04:00-05:20Z: Andrew affirmed PUBLISH INTENT gated on backend validation; he disambiguated "Supervised" ten minutes after I ruled on the wrong basis; the twr fix went armed and verified in four layers; and a raw-hash check nearly filed a FALSE PROVENANCE ACCUSATION against a correct deploy

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE

Continues `session_2330-0400Z_msgverify_built_and_twice_self_broken_d0_closed_canon458_registered.md` (@7ee525a868).

## 1. Andrew-direct x2, both recorded verbatim + broadcast same turn

**(a) PUBLISH INTENT AFFIRMED, GATED ON BACKEND VALIDATION** @742fc3dfec. VERBATIM: *"I do want to publish i want to
get this shit live but we need to validate that it actually works on the backend side."* Binds: the direction is
forward; the gate's test is **ACTUALLY WORKS = EXERCISED** (Rule 22a's BEHAVIOR layer in his own words); and it
**ANSWERS THE HOLD-3 CARD** -- it RATIFIES the PRD s.14 shape and WEIGHTS leg (a) CHAIN as operative, lift unchanged
at the promote act. Does not touch the two holds' independence. RE-ORDER: the twr D-1 mirror remedy became the
critical path to a sovereign publish intent, not a diagnostic.

**(b) "SUPERVISED" IS TWO MEASURES** @130ae4cd97. VERBATIM: *"...'Supervised' AUM from the perspective of Cottonwood,
which is the whole 458m. Then there is 'Supervised' AUM from the perspective of Opal, which is the derived value where
we take the residual account value of any account with Opal Models contained within the portfolio. For our purposes in
Model Portfolios display taxonomy, we are referring to the Opal Definition."*
!! **IT LANDED TEN MINUTES AFTER I RULED A SUPERVISED FIGURE ON THE WRONG BASIS.** My 68689 quoted
`$303,397,550.13` against a Cottonwood-supervision predicate; **WITHDRAWN**. The Custom-Models half
(`$6,622,450.40`, the name+location supersession) STANDS -- it turned on model-ness, not supervision.
COT_CANON458's 458M basis is UNAFFECTED and correct there. **RULED: every artifact/criterion/card carrying a
Supervised figure DECLARES ITS PERSPECTIVE on its face** (`supervised_basis: opal-models-residual` vs
`client-supervision-fact`).
**IT COST NOTHING BECAUSE THE LANE WAS EMITTING `predicate='unavailable'` WITH THE PENDING RULING NAMED** rather than
guessing a default -- the window existed because a seat refused to fill a gap. COO's classification is the keeper:
this is the ONLY **PERSPECTIVAL** instance of tonight's one-label-two-meanings family (the rest are TEMPORAL, fixable
by a vintage). **A vintage cannot fix a perspectival collision; only a declared basis can.**

## 2. Rulings issued
- **category-views -> ALL_SCOPE**, `global` GAINS ITS OBJECT (my earlier absent-not-empty ruling **superseded by his
  word**, stated as such: absence was honest only while global was uncomputable). **The one-value SCOPE-SET axis is
  RETAINED as a declared per-type property** -- `a4_expected` derives from it, and a silently deleted axis is how the
  next type gets hardcoded.
- **NAME+LOCATION SUPERSESSION GRANTED**: an Opal-named portfolio from that location IS a Custom Model, in the STORED
  class. Composition-absence yields as a proxy where he supplied the direct criterion; it stands elsewhere. Registry
  entries carry the minted/reverted/re-minted history so nobody re-litigates a reverted decision blind.
- **MINT THE MISSING STATUS (option B), option A DECLINED**: DS~H's BLOCKING was that the ratified acceptance was
  unachievable without manufacturing a BMV -- 17 accounts did not exist at D-1. CVO's framing decided it: **the
  criterion is not wrong, the AXIS is incomplete** (`piv.get()` returns the same `None` for a load failure and a
  nonexistent account). Narrowing the criterion would have **encoded today's population fact into a ratified
  sentence** -- the moment-as-mechanism class DS~H themselves named. Result on real data:
  `{OK: 6393, UNCOMPUTABLE-ZERO-BMV: 922, NO-PRIOR-BALANCE-ACCOUNT-ABSENT: 17}`, **REFUSED-NO-BMV = ZERO, acceptance
  satisfied AS WRITTEN**.

## 3. !! MY ERROR: I CARRIED AN UNMEASURED DEPLOY CLAIM ONTO THE CRITICAL PATH
DS~H reported their work "committed local, unpushed, therefore undeployed"; **I repeated it into a push request to
MSTR and told Andrew it was the highest-leverage item he had.** It was already pushed AND deployed. DS~H retracted
against themselves, CVO stopped it with a controlled ls-remote read, COO upheld, MSTR closed it from the integrator
record. **CVO's naming of the hazard is the durable part: a push of already-pushed commits SUCCEEDS -- it would have
closed a critical-path item having changed nothing, and an ACT THAT CANNOT FAIL IS NOT A REMEDY.**

## 4. TWR READINESS CLOSED -- four layers, each with a control
| layer | verdict | control |
|---|---|---|
| pushed | all 3 commits ancestors of live tip | fabricated hash reads not-on-remote |
| S3 code channel | `comp-pipescript deployed` MATCH | denominator printed |
| EXECUTING BYTES | **AE~G read the ACTUAL `ssm get-document` runCommand, not the TF comment**: `aws s3 sync .../_code/ --delete` FRESH EVERY RUN -> no baked-copy hazard on this chain | my own 68737 generic rule would have wrongly rejected this; CVO withdrew their Lambda caveat as unsupported HERE (it belongs to the MDPF pinned-package vehicle) |
| schedule | `cron(45 12 * * ? *)` UTC, **ENABLED**, target advi-49f-gold-dispatch | my first probe used `events describe-rule` -- WRONG SERVICE, failed LOUD; correct read via `scheduler get-schedule`, bogus name -> ResourceNotFound |
**Both fix halves confirmed IN THE DEPLOYED BYTES** (`_pull_prev_valuation_into_mirror` 2 hits @03:01:42Z;
`NO-PRIOR-BALANCE-ACCOUNT-ABSENT` at :73/:94 @05:06:45Z; positive+negative controls both). **12:45Z runs the complete
fix with nothing human in the path.** Per Andrew's own rule the SCHEDULED run's artifact is the evidence -- never the
QA exercise.

## 5. !! THE CRLF NEAR-MISS -- the defect I documented caught its own documenter
My first verification hashed the deployed object against `git show <mint>:<path>`: **MISMATCH** (`22b0a5c2` vs
`1c270bed`). That reads as *"deployed from an uncommitted working tree"* -- a **provenance accusation against DS~H's
deploy**, and FALSE. **Normalised CRLF->LF: IDENTICAL** (`1c270bed` == `1c270bed`; deployed 240 CRLF pairs, blob 0).
**This is verbatim the defect I wrote into `comp-closure`'s header at ~02:5xZ** (*"a CRLF-deployed member vs LF
committed copies reads eq:false ON A CORRECT DEPLOY... the shape that produces a FALSE PROVENANCE ACCUSATION"*).
**What saved it: three signals disagreed** -- `git status` CLEAN, the token grep found the mint PRESENT, the hash said
mismatch. **A hash alone would have convicted.** OPERATIVE RULE, now on live evidence: any deployed-vs-committed byte
comparison NORMALISES LINE ENDINGS **AND SAYS THAT IT DID**.

## 6. Delivered to Andrew
A card-by-card exec view of every active project grouped by its DIRECTIVES.yaml entry (D0/D1/D2/D3/D4 + the two
unhomed), each with design intent, live `dep_stage`, progress, and what stands in the way -- read from the registry
and DIRECTIVES.yaml at the moment of writing, not recalled.

## MCP traffic
~10 multi-recipient acts (38 deliveries, all DELIVERED); ~35 inbound, every one READ-acked. Two corrections against
myself (the push claim; the Supervised basis). Zero traffic to any CRO serial.

## Compiler Tools
| tool | invocation | result |
|---|---|---|
| git ls-remote / merge-base --is-ancestor | push-state, 3 commits + negative control | PASS -- and the control is what made the verdict quotable |
| comp-pipescript deployed | c02_twr_engine.py | MATCH, denominator printed |
| aws s3api head-object / s3 cp + grep | deployed bytes, both files, pos+neg controls | PASS -- the mint and the mirror pull both PRESENT |
| aws scheduler get-schedule | the floor's live state | ENABLED cron(45 12) UTC; `events describe-rule` first = wrong service, loud failure |
| python normalised hash compare | deployed vs mint blob | the CRLF near-miss, s.5 |
| safe-commit -F (msg-verify live) | 3 commits | all MATCH; hashes verified path-scoped |
What failed: my `events describe-rule` probe (wrong service, correctly loud). Gap: none new -- the CRLF class was
already documented and this is its second live instance.

## Blockers
**None at this seat.** At Andrew: ~12 open cards; the push question (two instances, fetch-arrival, not a web merge);
COT_CANON458's directive home. At COO: TO cuts on COT_CANON458 + cap repair. At the fabric: 12:45Z.

## Current State -- for a reader with zero context
The 49F performance backend was computing ZERO returns (twr_daily refused 7,335 of 7,335 rows) because the chain's
per-run mirror staged only date=D while `c02_twr_engine.py` reads BMV from date=D-1 in that same mirror. Both halves
of the remedy -- the D-1 pull in `chain_49f_entrypoint.py` and the minted `NO-PRIOR-BALANCE-ACCOUNT-ABSENT` status in
`c02_twr_engine.py` -- are ON origin/CLOUD and IN `s3://opal-data-49financial/_code/`. The runner syncs that prefix
fresh every run, so the 12:45Z scheduled fire executes them. QA exercise gave OK 6,393 / zero-BMV 922 / absent-at-D-1 17 /
REFUSED-NO-BMV 0. Andrew's publish gate is EXERCISED backend validation; the scheduled artifact is the evidence.

## Next Steps
- **[Andrew]** the cards; the push question; COT_CANON458's directive home.
- **[0.4.0_DS_ClientPlatform~H]** the mint's four-postulate record; read the 12:45Z artifact.
- **[3.0.0_SA_CVO]** (c) re-derivation fires on that artifact; channel rounds.
- **[2.0.0_SA_COO]** claim assembly starts at the artifact; COT_CANON458 + cap-repair TO cuts.
- **[1.0.0_SA_CTO]** read the 12:45Z run; the PIPMAP proposals; the owed gate-battery run.
