# Seven instances of one shape, two of them mine, and the seventh nearly rewound production -- 3.0.0_SA_CVO

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, SCRIBE

**Date:** 2026-08-26
**Task Order:** ad-hoc -- session start 13:31Z through 16:14Z; MDPF acceptance second-read, four adjudications, two law/doctrine edits
**Status:** COMPLETE

---

## Objective

Wake, arm, and man the surprise channel. The session opened 19 minutes before a time-boxed MDPF
publisher acceptance read that `2.0.0_SA_COO` had declared UNMANNED for independent verification,
and closed having adjudicated four schema/control questions, corrected two of my own numbers, and
recorded a defect shape that recurred seven times in one working day.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | A.3 EXERCISE limb -- forwarder RAN, 104 of 105 resolve bare |
| comp-find | `comp-find proof-of-spec-check --files` | PARTIAL | resolved the file but returned it space-padded; `sed` then failed on the padded path |
| directives-check.py | `--json` | PASS | 11 live / 7 LAPTOP / 4 SITEZ, denominator printed; the basis of the /self-drive verdict |
| to-check.py | `--all --assignee 3.0.0_SA_CVO` | PASS | 2 active TOs, scanned=2111, 0 parse errors |
| comp-pipescript | (cited, not run by me) | FAIL | `deployed` returns STALE forever across the CRLF/LF boundary -- 16 of 159 files |
| proof-of-spec-check.py | run on class-D and class-A instances, true rc | FAIL | `VALID`/`rc=0` on an instance whose alignment join could not run -- 92 of 159 |
| deploy_ledger.py | (cited, not run by me) | FAIL | `--red` line true about the ledger, blind to a promote executed on the other fabric |
| safe-commit.sh | 7 commits, `-F` message files authored by the Write tool | PASS | msg-verify MATCH on every one |

**What worked:** `directives-check.py --json` answered a governance question in one call with its
denominator attached, which is what made the /self-drive adjudication cheap. `safe-commit`'s
`msg-verify` limb confirmed byte-length on all seven commits.

**What failed:** three instruments returned confident wrong answers this session and all three are
recorded above -- `comp-pipescript deployed`, `proof-of-spec-check`, `deploy_ledger.py --red`. None is
broken in the ordinary sense; each is correct about its own domain and silently wrong about the
question asked of it.

**Gap found:** no tool answers "is a ledger entry's OPEN state a property of the world or of this
device." That gap produced the near-rewind and is now closed by law rather than by a tool
(CLAUDE.md NEVER#6 @901cb6e7ff + @cost-clause).

---

## Work Completed

### 1. Startup and the 13:50Z MDPF acceptance second read

`/watcher` armed (Monitor `bv772bz5j`); no orphan existed for the serial -- `watcher-status`, `ps` and
a `NOT REGISTERED` broker read agreed, so the kill-before-arm question never arose. Registered PID
37348.

Offered `2.0.0_SA_COO` the independent verification its 72152 s.5 had declared unmanned, explicitly
NOT as a gate. Captured my own pre-state by `s3api` GET (not a relay); the four pre-fire VersionIds
matched `1.0.0_SA_CTO`'s 13:28Z pins character-for-character and the byte sizes matched
`0.7.0_AE_CloudOps~G`'s 12:59:11Z relay exactly -- three captures, three seats, nothing to subtract.

Built a leaf-field differ and self-tested BOTH ARMS before trusting it: identical input -> 0 deltas
and UNMOVED; planted `as_of_last`+`written_at` advance -> PASS.

**VERDICT, denominator 4 of 4 scopes:** `49financial` PASS | `inflection` PASS | `global`
REPUBLISH-NO-ADVANCE | `cottonwood` REPUBLISH-NO-ADVANCE. For the two failures the ONLY changed leaf
was `_provenance.written_at` -- 1 of 20,345 and 1 of 11,960.

**Root cause, from the run's own manifest** `_manifests/2026-08-25/20260826T133106Z.json`: Cottonwood
grew a model `Opal Fixed Income` with no canonical `by_model` key; the slice builder refused to
auto-slug (its own message: doing so "would silently add a row to the served Global union"), and the
global fold then refused to compose a total with a leg missing. **Two guards, right order, both
refusing correctly.** Both scheduled legs fired on time.

Reconciled the one numeric gap with `1.0.0_SA_CTO`: their 20,286/11,919 vs my 20,345/11,960 -- the
deltas are EXACTLY the list counts (59 and 41), their figure equals my scalar count to the unit.
Instrument convention, not data.

### 2. Four adjudications issued

| # | Question | Verdict |
|---|---|---|
| 1 | `/self-drive laptop directives` -- arm-time 5 or current 7? | **RE-RESOLVE TO 7.** Landed by CTO @eb92fd6a87 |
| 2 | D3 advisor unblock spec -- vendor-side? | **CONFIRMED**, one inference NARROWED; DS~S withdrew the clause and corrected the artifact @efd50eff41 |
| 3 | TO `<lifecycle>`/`<delivery>` two-field split (Rule 24) | **REWORK.** Axis 1 fails (i)+(iii); axis 2 fails (iii) by its author's own analysis |
| 4 | RECON_TOLERANCE predicate form | **Direction upheld, arithmetic replaced** with integer cents |

On (1) the argument I added was not the skill text but three measured decays in the carrier clause
itself ("of 9 live" -> 11; D1's member set no longer empty; `ADVI_BDPLAT_RESTORE` now carries
`status: complete`) -- a measurement that had already rotted in three places is not a boundary.

On (3) the uncovered member is **33 STAGED task orders**, and they are not one state: 13 announce a
gate, 1 announces it is explicitly UNGATED, 19 say nothing. A four-value lifecycle maps all 33 to
`OPEN`, preserving at n=33 the exact defect the schema exists to fix. There are THREE issuer intents
here, not two: disposition, RELEASE, delivery.

On (4) I reproduced DS~S's table row-for-row and added two arms they had not run (two-cents and
one-dollar, both correctly refused by both forms) -- which is what settled it: the integer-cents form
is CORRECT ON ALL FOUR ARMS, not merely looser. The trap: `$2,031,609,247`, the incident magnitude
the ruling was written against, is one of the five that PASS under the float form.

### 3. Findings surfaced and filed

- **`MDPF_COTREMEDIATION-S14..S17`** (@878be43536, @80122e6632) -- a PID limb in a death certificate
  INVERTS with time (pid 26224 moved serials in 17 minutes); the manifest reports
  `reconciliation: PASS` on a 6-of-12 run; the publisher stamped today's `written_at` onto
  yesterday's data.
- **`ADVI_INSURE-S8..S11`** (@6ddbbe7e67) -- filed for `0.4.0_DS_ClientPlatform~R` with the division
  of labour stated: their content figures, my GRAIN and COVERAGE checks only.
- **prompt.md `/c` census** -- 16 of 40 files mandated the arm-killing path, 0 the working form.
  `1.0.0_SA_CTO` swept it in 7 lane-scoped commits; I verified 0 residual.
- **`proof-of-spec-check` needle** -- confirmed AT EXERCISED (`rc=0` with "alignment: NOT EVALUATED")
  and corrected the reporter's number from 100% of 1,451 TOs to **92 of 159 instances**, a GRAIN
  correction (the checker runs on instances, not TOs).
- **`mdpf_aggregate_aua.py:699/:703`** -- cross-thread find; three sibling sites are SAFE and the
  difference is one `round()` call. Explicitly warned that a sweep "fixing all five" would rewrite
  three correct lines.

### 4. Two law/doctrine surfaces

- **`docs/references/.../INSTANCES_20260724.md` s.V-6** (@0df05ec441, addendum @0752c4b1a7) -- the
  consumer-side form: the basis WAS emitted, truthfully, beside the value, and the consumer still
  gets the wrong answer. `1.0.0_SA_CTO` landed the matching doctrine clause; I pinned its dangling
  pointer (@111d119fa3) after finding it cited a "forthcoming record" that already existed under a
  name the pointer would not find.
- **CLAUDE.md NEVER#6** -- my 72520 ruling landed as the cross-fabric inversion clause @901cb6e7ff;
  I verified it at source and found the COST half of this file's own landing bar missing from the
  law text (it was in the broadcast, which scrolls). CTO landed the cost clause.
- **Proposal, not landed** (@b68ba16530) -- a `_FABRIC/` home for surprise items with no project
  subject, with its Rule 24 four-postulate record and a token-hygiene census over a 7-file canon.
  The census earned its keep: bare `FABRIC` scores 20 as a common noun and `GLOBAL` collides with a
  live MDPF scope name.

---

## Decisions Made

1. **Offered verification without becoming a gate.** The read executed on spec at 13:50Z whether or
   not my report existed; stated in the offer and honoured.
2. **Refused to mint `_FABRIC/` on my own authority** despite manning the channel -- I returned two
   peers' schema proposals for rework on the four-postulate bar the same day, and holding myself to a
   lower one is the asymmetry that bar exists to prevent.
3. **Ratified "different, cause UNESTABLISHED"** rather than let a falsified mechanism rest on the
   record, because the next reader inherits the mechanism, not the caveat.
4. **Declined to rule on what LD-0405 means.** Read it at source instead: `requires_andrew_ratification:
   false`, `ratified_by: null`, MSTR-authored. The clause everyone treated as a sovereign prohibition
   is its author's own scope note. `2.0.0_SA_COO` withdrew the card rather than ask Andrew to
   adjudicate an agent's prose.

---

## Files Modified

See commit messages: `878be43536`, `80122e6632`, `6ddbbe7e67`, `0df05ec441`, `111d119fa3`,
`b68ba16530`, `0752c4b1a7`.

**Push state, measured this turn, not asserted:** six of the seven are ON `origin/CLOUD` (integrator
push); `0752c4b1a7` is LOCAL-ONLY. `git reflog | grep push` from this worktree: EMPTY -- I pushed
nothing.

---

## Blockers

**None at this seat.** I hold no gate and nothing waits on me. The `[STOP]` in 72499 is ACKed and
complied with; nothing of mine is staged for push.

---

## Current State

**MDPF 08-27 fire is the live acceptance.** Bar: BOTH `as_of_last` AND `_provenance.written_at`
advancing for `global` and `cottonwood` on the served plane
(`s3://opal-data-portal-v2/platinum/mdpf/{scope}/aggregate-aua-timeseries.json`). No ad-hoc invoke.
Andrew ruled `Opal Fixed Income` a CUSTOM model (verbatim in COO 72416), which supplied the INTENT no
instrument here could reach; `0.6.2_AE_PartnerETL~A` supplied the structure. Leg A is applied,
CodeSha256 moved to `3/897ecG...`, vintage `48c473caa1`.

**Watch list, corrected:** `cottonwood advances / global does not` -> the three-file fix did not fully
land. `written_at moves / as_of_last does not` -> the republish-that-did-not-happen. **A four-scope
refusal is NOT a signature** -- `0.6.2_AE_PartnerETL~A` falsified my 72429 s.3 by measuring the running
bundle: `mdpf_category_registry` is inert at the minimal pin, no packaged module imports it. My error
was a HEAD-source claim about deployed-bytes behaviour, on the rule I had cited at them six messages
earlier.

**Unexplained and separate:** cottonwood's dim moved 146,879,940.09 -> 191,504,659.67 (+7 accounts) on
2026-08-26. Andrew's ruling accounts for `$8,442,396.91` of it and NOTHING else; ~36.2M is unowned.
Filed ARMED, disarmed same-turn by putting the split on the record so the book move is not attributed
to the repair when both publish together.

**Estate-report proposals HOLD** (Andrew-approved, COO 72433 s.3). Corpus frozen 26 days at
`649fa25a4` (2026-07-31T02:23:07Z) -- grounded by me at source. WARN: The manifest CANNOT express this:
its corpus block is four counts plus `degraded_sources: []`, no vintage. Read the day's report JSON
`corpus_coverage.source_vintages` when the question is corpus currency.

**My open TOs:** `D3_MODELOVERLAY.TO-D3.5` (staged, gated on TO-D3.4) and
`OPAL_ADVIPOINTERS.P4-PINS-CERT-49F` (group pin + cert closed 2026-08-21 by the issuer -- a candidate
for closure, issuer's act not mine).

**Open at me:** nothing. **Open FROM me:** the `_FABRIC/` proposal at CTO/COO; the `:89` in-source
comment carrying my wrong "five uses" count, requested to be corrected with the `:1124` fix.

---

## Next Steps

1. **[3.0.0_SA_CVO]** Verify the 08-27 13:30Z scheduled fire against the bar above, on the served
   plane, with the corrected watch list. Object mtime is NOT the oracle.
2. **[1.0.0_SA_CTO / 2.0.0_SA_COO]** The `_FABRIC/` surprise-channel proposal (@b68ba16530) -- three
   fabric-level items are currently homeless and living in message records.
3. **[0.4.0_DS_ClientPlatform~S / whoever lands `:1124`]** Correct `mdpf_aggregate_aua.py:89` in the
   same commit -- it encodes my truncated "five uses" as fact, and the reader who responsibly reads
   the note before touching the constant is the one who inherits the error.
4. **[0.8.0_AE_CloudComp~F]** Revised TO-schema record with the three-axis-or-priced-fusion form, the
   coverage x outcome split, the derived-vs-asserted provenance mark, and joinability restated on the
   CEILING/ACTUAL pair (147 instances, 8.4% ceiling, ~4% actual). I turn it around on arrival.
5. **[1.0.0_SA_CTO]** The `freshguard-leg4` CTO approach-gate (A centralize-import vs B 3-copy) has
   been unanswered since 2026-07-09 and is the actual blocker -- not the alarm moratorium the
   withdrawn card named.

---

## The thing worth carrying out of this session

**Seven instances in one day of one shape: a field a decision-maker branches on that cannot express
what the artifact also says.** Gold manifest `reconciliation`; `proof-of-spec-check` `rc=0`;
`parse_to_file`'s `to_id`; the proposed `<delivery>` axis; the estate-report manifest's corpus block;
`deploy_ledger.py`'s summary on `freshguard-leg4`; `deploy_ledger.py --red` on `v2.1.165`.

**Two of them reached Andrew.** The seventh recommended an act that would have rewound production
five releases; `0.4.0_DT_ClientPlatform~C` refused the instruction on measurement, and per
`0.0.0_AB_MSTR`'s correction that refusal was **the entire control set** -- the push-holder named in
the stand-down was never structurally capable of making that push.

**Two of the seven were mine, and both were wrong-population numbers**: a joinability figure that
measured only the supply side of a join, and a `grep | head -6` census that reported five uses of a
constant that has eight. A correct classification over an incomplete population reads exactly like a
right answer.

Three seats hit the wrong-predicate version of this within minutes of correctly catching it in
someone else -- including me, while auditing the other two. **Naming a failure mode does not
inoculate you against it. Only measuring does.**
