# 3.0.0_SA_CVO~Z -- session close 1618-1650Z, 2026-08-27

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

> **WRITTEN FOR A ZERO-CONTEXT SUCCESSOR.** Andrew-direct (relayed verbatim by `1.0.0_SA_CTO~Z`,
> msg 9289 + addendum 9291): *"i will close you all out and reinstantiate you fresh."* This log is
> not a handoff to a continuing seat -- it is the ONLY thing the next `3.0.0_SA_CVO~Z` has.
> **Certification STATE at this seat is authoritative and is deliberately NOT copied into any peer's
> log** (a second record of one state is a divergence surface). If it is not here, nobody has it.

---

## 1. WHAT THIS SEAT IS

`3.0.0_SA_CVO~Z` -- site-Z lane of the Chief Validation Officer. **Verifier-not-fixer.** Certifies
decomps, mans the surprise channel (Rule 27 stage 5), and holds the LD-0319 load-time parity control.
**Constitutionally independent: MSTR does not outrank a CVO ratification verdict** (`org/XXX.md`
Authority hierarchy). Comms confined to {~Z seats} + {MSTR} + {0.8.0_AE} per LD-0325.

Session start state: NOT REGISTERED, no watcher, 26 unread backlog going back to 08-25. The seat had
been dark. Registered PID 1664, Monitor task `bremqkuxl`.

---

## 2. THE CERTIFICATION METHOD -- THE THING MOST LIKELY TO BE LOST

Two procedures this session PROVED. The verdicts are in the deliverable; **the methods are not, and
a successor facing the same hazards will otherwise re-invent or miss them.**

### 2a. THE VINTAGE GUARD -- and the negative-control half is the whole point

Two seats warned that the artifact I was certifying had moved twice that day and that certifying v1
would certify a wrong member set plus a withdrawn taxonomy verdict. I did not accept the warning;
I measured it:

```
git merge-base --is-ancestor a1c38e8c53 origin/SITEZ   -> ancestor      (correction 1)
git merge-base --is-ancestor 8e188d4f42 origin/SITEZ   -> ancestor      (correction 2)
git merge-base --is-ancestor f58160dd8e HEAD           -> YES           (remote is in my history)
git merge-base --is-ancestor 506a1626f0 origin/SITEZ   -> NOT ancestor  <-- THE CONTROL
```

**THE FOURTH LINE IS THE ONE THAT MATTERS.** `506a1626f0` was my own commit, known-unpushed. Running
it proves the ancestry test CAN RETURN NO. Without that arm, three "ancestor" results are equally
consistent with a test that always says yes -- and "verify the vintage" without the negative control
is the version that passes when it should fail. **Certify from the REMOTE ref, never a working-tree
copy** (`MSYS_NO_PATHCONV=1 git show <ref>:<path>`); a local tree is a snapshot.

### 2b. I CORRECTED MY OWN SWEEP MID-CERTIFICATION -- a successor will hit the same false positive

Testing which roster field separates the 9 IS-A satellites from the 5 HOLDS-A blends, I scored "the
two value sets are disjoint" and got SEVEN candidates. **Four were wrong:** `id`, `lastUpdate`,
`name`, `rowNumber` are UNIQUE PER ROW, so they are disjoint between ANY two disjoint row sets **by
construction**. That is identity, not class information.

**Had I stopped at the first pass I would have reported "the roster CAN express the criterion, just
key on `id`" -- nonsense that reads as a finding.** Rule: partition fields by cardinality and
EXCLUDE every field whose distinct-value count equals the row count BEFORE testing separation, and
state the exclusion in the result. Banked to memory as `a-row-unique-field-is-vacuously-disjoint`.

---

## 3. CERTIFICATION STATE -- AUTHORITATIVE, LIVE vs SUPERSEDED

### 3a. ETFS_SATELLITES (D4) -- **DONE. CERTIFIED WITH FINDINGS.**

- Artifact certified: `workflows/atom_decomposition/runs/etfs-satellites/20260827T160438Z/DECOMP.md`
  read at `origin/SITEZ @ f58160dd8e`. Author `2.0.0_SA_COO~Z`, issuer `1.0.0_SA_CTO~Z`.
- Deliverable: `org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoZ_ETFS_SATELLITES_DECOMP_CERTIFICATION_20260827.md`
  `@205546c65c`, **amended `@a025e2be91`**. Read the AMENDMENT -- it changes F1.
- Mechanical census: **21 cells + 4 invariants.** The announcing message (9237) said "23 cells";
  its own per-surface breakdown (4+5+3+3+3+3) sums to 21. The ARTIFACT is right, the MESSAGE was not.

**Reproduced EXACTLY** off my own pull of the roster page (34,454 B on S3 = 34,454 B local; rc=0 is
not evidence of bytes): denominator 65 / pageCount 1 / totalResultCount 65; the nine canonical
members; Satellite 90 = 0 accounts and 98 = 11; the `Core | Satellite 98` collision pair 9-vs-11;
all five blends at accountCount 1; negative controls `Opal Satellite 99` / `25` both ABSENT.

| finding | status NOW | owner |
|---|---|---|
| F1 membership predicate underivable | **LIVE, SHARPENED, RULED** (see 3b) | COO~Z author / CTO~Z issuer |
| F2 `modesFor(firm)` has no four-postulate record | **LIVE, P1** | `1.0.0_SA_CTO~Z` |
| F3 join-key mismatch on `Opal Satellite 60` | **LIVE, P1** | DE via the TO cut |
| F4 `SAT-b-4` "19 excluded rows" frame undeclared | **LIVE, P2** | COO~Z author |
| F5 stale "no CVO seat on this fabric" line | **CLOSED**, acted on by CTO~Z | -- |
| F1's PROPOSED REMEDY (`hierarchy.children[]`) | **SUPERSEDED -- FALSIFIED** | -- |

**F3 is the sharpest and is easy to lose:** `Opal Satellite 60` carries
`displayName = "Opal - Satellite 60"` (a dash); the other eight match `name` exactly. The
roster->detail join therefore breaks on 1 of 9 members -- **the member with the second-highest
account count (81)** -- and the failure mode is SILENCE (empty reads as "no weights", not "key did
not match"). `SAT-a-2`'s oracle already catches it; **what is missing is the FIXTURE.** Member 60 is
the natural mutant for the resolution path exactly as `SAT-b-4` uses the 98 pair for membership.

### 3b. F1 -- THE RULING. SETTLED BY THIS SEAT. DO NOT RE-OPEN WITHOUT NEW EVIDENCE.

I marked F1's remedy INFERRED because I had not run it. `1.0.0_SA_CTO~Z` (9274) then measured it:
**84 detail files synced whole, 121 child nodes, MAX DEPTH REACHED = 1, ZERO satellite-id matches,
POSITIVE CONTROL 18 of 18 child ids resolving to top-level models.** `2.0.0_SA_COO~Z` (9275) agreed
on 4 specimens BY THE SAME METHOD -- **repetition of one instrument, not corroboration by two.**

What it showed: `Opal Sat 50+ 15% cash` composes Intermediate-Term .5 / Short-Term .15 / Ultra
Short-Term Income .35 and **never references `Opal Satellite 50`**. THE BLENDS HOLD THE SATELLITES'
INGREDIENTS, NOT THE SATELLITES. So Andrew's IS-A vs HOLDS-A criterion is correct and **is not
evaluable against rebalancer at ANY depth** -- not the roster (mine), not the detail (theirs).

**RULING: ship the DECLARED NINE as data, labelled a declared set with a named owner; amend
`SAT-inv-2` to say so on its face.** The reasoning is NOT "we tried and failed" -- it is A VALUE MUST
CARRY ITS CLAIM, and `held` is a LEGAL claim value. **The defect was never that the set is a list; it
is that `SAT-inv-2` CLAIMS "a declared predicate over the roster" while the mechanism IS a list.** A
fake predicate would be strictly worse: a `measured` label over a `held` value. inv-2's PURPOSE
survives -- its rationale is "a hand list inherits SOMEONE ELSE's omission", and an Opal-declared,
Opal-owned list is a different object from an inherited one.

**THE REVIEW TRIGGER, AND IT IS NOT A MONITOR** (the alarm/monitor moratorium binds): it goes inside
`SAT-b-2`'s EXISTING oracle -- print roster rows matching canonical `Opal Satellite <N>` beside the
declared nine, fail on any symmetric difference **in either direction**. As a MEMBERSHIP PREDICATE
the name form is wrong and Andrew ruled it so; as a DRIFT DETECTOR it decides only "a human must look
at this row". Same expression, different job, different correctness bar.

**EFFECT: `SAT-b-2` + `SAT-inv-2` are BLOCKING FOR TO-MINT ON THE MEMBERSHIP SURFACE ONLY.** The
other five surfaces can be cut. `1.0.0_SA_CTO~Z` stated their nine-name recommendation is a
recommendation into the certification, not a ruling over it, and that they will cut TOs to my text.

### 3c. D1_NAMEDISCOVERY -- **PENDING. NOT STARTED. IT IS THIS SEAT'S.**

`1.0.0_SA_CTO~Z` had an Andrew-APPROVED rec to certify it themselves as named alternate; **they
declined to execute it because this seat was live** (msg 9246) -- an alternate exists for an
UNAVAILABLE primary, not an unobserved one. **The certification is CVO's and has not begun.**
CTO~Z handed over a completed staleness re-derivation to inherit rather than repeat:
- The three scope forks are UNMOVED; all Andrew-directs touching the name space predate authoring.
- **ONE staleness stands and it is a header line, not a cell:** the decomp header reads
  `placement LAPTOP`; superseded by `ANDREW_DIRECT_20260826_2352Z_PLACEMENT_MAP_D8_AND_MP_TO_SITEZ.md`.
  **D1 IS SITEZ.**
- Shape: 20 cells / 16 criterion-bearing / 0 criteria (NOT-YET-EVALUABLE, no TO cut).
- **TREAT THAT AS A PRIOR UNDER TEST, NOT AS DISCHARGED** -- CTO~Z's own words; it is their read,
  not a certification, and this seat's independence is the point.
- Its cited precedent is the thing to hold it to: `D1_CATVIEWS`' decomp was certified, went stale
  under a sovereign word 4h later, and stayed stale 21h while work was delivered against it.

### 3d. D8 / MDPF_COTREMEDIATION stage-3 decomp -- **CERT OWED, NOT STARTED**

Delivered by `2.0.0_SA_COO~Z` at 16:35Z this session. Also still owed from the round-1 doc's tail:
the earlier `workflows/atom_decomposition/runs/mdpf-cotremediation/20260825T161149Z/` decomp (38
cells, `@7807a52e75`) is **SOLO and UNCERTIFIED**, and every TO cut from it carries "UNCERTIFIED
DECOMP" stated by the issuer. **Both are this seat's.** COO~Z's binding constraint, carried verbatim:
target architecture PARKED, Rule 17b NOT amended, no migration authorized; D8's first work is a
CENSUS and the conformance AXIS is a Rule-24 authoring act D8 ESTABLISHES rather than inherits.

---

## 4. SURPRISE CHANNEL STATE (this seat MANS it)

**Filed this session** into `org/surprise_channel/MDPF_COTREMEDIATION/INVESTIGATION_v1.md`
`@506a1626f0` -- items **S18** and **S19**, from `0.7.0_AE_CloudOps~Z` msgs 9174 / 9242.
Doc now holds 19 items; 9 ARMED, 0 ARMED without a disarm owner (verified mechanically).

- **S18** BLOCKING x ARMED, GROUNDED. R2 is ALREADY BUILT on the EventBridge **SCHEDULER** plane
  (`cot-bd-session-daily-et`, ENABLED, `cron(30 7 * * ? *)` America/New_York). `events list-rules`
  and `scheduler list-schedules` DO NOT OVERLAP -- the issuer's 137-rule census was correct,
  complete, and structurally unable to contain the answer. **DISARMED same-turn by the surfacing
  seat, which is NOT remediation: the spec sentence that armed it is still on the page and is TRUE
  within the Rules plane, so a successor re-reading it re-arms the hazard with a correct-looking
  citation.**
- **S19** OBSERVATION x ARMED, GROUNDED. Two carries on served `global` that no hypothesis explains:
  `2026-07-29 <- 07-27` (2 trading days) and `07-30 <- 07-27` (3). Both PREDATE the 08-14 kill and
  neither is a mint day. **ARMED is recorded WITH ITS BASIS: it rests on the mechanism being
  UNKNOWN, not on a demonstrated live one.**
- **>> OPEN AND HELD BY THIS SEAT, NOT ROUTED: the S19 measurement.** Re-run
  `lib.trading_calendar.trading_days_behind` over the ~20 trading days since 2026-07-30. A clean run
  makes the condition historical and the item INERT; a recurrence makes it live. **I told
  `0.7.0_AE_CloudOps~Z` this seat holds it. IT HAS NOT BEEN RUN.** <<
- `org/surprise_channel/ETFS_SATELLITES/` **does not exist and should not be pre-created** -- the
  channel opens on first item. No ETFS_SATELLITES surprise has been surfaced.

---

## 5. LD-0319 PARITY CONTROL (permanent, runs FIRST at every CVO~Z load)

`comp-system --check` -> **`06 STALE: age 26h exceeds TTL 24h`.** DRIFTED, so it is the first work
item -- and the correct act is to SURFACE, not to fix.

**DO NOT REGENERATE 06 FROM SITE Z.** A site-Z regen writes UNKNOWN-VINTAGE graph rows into the
laptop-maintained 06 because comp-kuzu is not reachable here (CTO~Z ruling). Surfaced to
`0.0.0_AB_MSTR~Z` msg 20260827T163920Z.
- **`comp-kuzu` DOES resolve bare on this box, and that does NOT overturn the ruling.** RESOLUTION IS
  NOT EXECUTION -- `command -v` sees a forwarder file and cannot see whether its target works.
- **INSTRUMENT TRAP, points the wrong way:** the 06 artifacts' mtime is TODAY (written by the merge
  checkout) while their CONTENT vintage is 26h. **MTIME IS THE CHECKOUT, NOT THE GENERATION.**

### LD-0318 scoped re-arm -- ARM NOTHING. Zero crons at this seat.

`org/projects/NFRA_SYSPARITY.json` now reads **`status: closed`** while its own `blocking` field
describes an ONGOING project naming the per-domain loop as NEXT -- **two fields, one file, opposite
readings.** The XXX.md CVO~Z row's stop-condition is "NFRA_SYSPARITY closes -> DISCHARGE".
**BOTH READINGS CONVERGE ON ARM NOTHING**, so the unresolved question BLOCKS NO ACT and must not be
escalated as though it does. **The row stays UNSTRUCK and UNANNOTATED** -- striking a
sovereign-authored clause on this seat's own authority would manufacture a discharge of Andrew's word
from inference, and a "held pending" annotation would itself read as a gate.

---

## 6. FABRIC EVENTS THIS WINDOW THAT CHANGE WHAT A SUCCESSOR SHOULD BELIEVE

- **THERE IS NO PARITY GATE ON D1/D4.** `0.0.0_AB_MSTR~Z` broadcast one in at least four messages,
  then RETRACTED it in full (msg 9286): Andrew-direct *"there is no gate on parity, we are going to
  be proceeding now."* The gate was manufactured from a statement of intended sequence. **I had
  surfaced the scope question rather than adjudicating it in either direction, with a stated default
  (proceed on cert work already in flight, start no new one) so nothing was held while it resolved.**
- **PARITY IS AN INSTANT, NOT A STATE.** SITEZ lacks 24 CLOUD-only commits, CLOUD lacks 5 SITEZ-only;
  both is-ancestor checks FAIL **after a correctly-executed two-leg reconcile**, because both fabrics
  kept committing. Nobody is at fault. Convergence deferred to end of session by Andrew's word.
  **My three commits are on `origin/SITEZ` but NOT yet visible from the laptop -- do not cite them as
  cross-fabric-readable until after the end-of-session convergence.**
- **A misattribution I corrected:** `2.0.0_SA_COO~Z` (9275) credited this seat with disarming the AC7
  fixture and widening it to 307 noncurrent versions. **Not mine** -- `0.0.0_AB_MSTR~Z`'s, by their
  own words in 9272, and they confirmed it. Mechanism worth keeping: `bc570d9e0d` is a REMOTE HEAD
  containing several seats' commits, and reading a shared head attributes its contents to whoever was
  most recently discussed. Discriminator is `git log -1 --format=%an` on the COMMIT, not the head.
- **Audit-archive returns 18 findings on EVERY site-Z startup** in tamper vocabulary. Already
  adjudicated by `0.0.0_AB_MSTR~Z` (msg 9111) as a device-axis artifact: committed baseline vs
  gitignored device-local logs, i.e. two different files sharing a path. **Do not re-escalate.**
  Owner `0.7.0_AE_CloudOps`, gate `1.0.0_SA_CTO`.

---

## 7. Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-system --check` | LD-0319 load control | **WARN** | 06 STALE 26h vs 24h TTL; surfaced, NOT regenerated (site-Z rule) |
| `comp-which` | A.3 mandatory EXERCISE | **PASS** | forwarder RAN and produced its own banner -- scored on OUTPUT, not rc |
| A.3 PATH denominator | `.tools/comp-*` sweep | **PARTIAL** | 98 of 105 resolve bare; the rest need explicit `.tools/` prefix |
| `audit-archive-invoker` | XXX.md A.2 | **WARN** | 18 findings, identical to the pre-adjudicated device-axis set |
| `to-check.py --all` | B.1, both serial forms | **PARTIAL** | suffixed=0 (known SEATED-prose blindspot), base=2 ACTIVE |
| `safe-commit.sh` | 3 commits | **PASS** | risk-reflex CLEAN 1/1351 each; msg-verify MATCH each |

**What worked:** scoring `comp-which` on OUTPUT rather than rc -- the rc does not discriminate
match-from-no-match, and the A.3 exercise half is what distinguishes a live forwarder from a resolved
dead one. **What failed:** nothing tool-side. **Gap found:** `to-check.py --assignee` still returns 0
for this seat's suffixed serial; the discriminator is the `**SEATED: serial**` prose notation, not
the tilde (already recorded in XXX.md). A zero there is NOT evidence of holding no work -- I read the
base serial to find the 2 ACTIVE TOs.

---

## 8. Files Modified

See commit messages: `506a1626f0`, `205546c65c`, `a025e2be91`. Two paths only --
`org/surprise_channel/MDPF_COTREMEDIATION/INVESTIGATION_v1.md` (68 insertions, an APPEND: verified
19 items parse, no duplicate ids, 0 ARMED-without-owner, CRLF count 0) and the certification
deliverable (186 + 96 insertions).

---

## 9. Blockers

**NONE at this seat.** Every open item has a named owner and an event trigger:
- F1/F2/F3/F4 remediation sits with `2.0.0_SA_COO~Z` (author) and `1.0.0_SA_CTO~Z` (issuer). Not held
  on CVO -- the ruling is issued.
- The S19 measurement is HELD BY THIS SEAT and unstarted (section 4). **That is an unstarted item,
  not a blocker, and it is the one thing a successor is most likely to drop** because it lives in an
  item's `disarm_owner` field and in one message rather than in a TO.
- 06 parity drift is `0.7.0_AE_CloudOps` / laptop-side; surfaced, not chased.

---

## 10. Current State / Next Steps

**Registration:** `3.0.0_SA_CVO~Z`, PID 1664. **Watcher:** Monitor task `bremqkuxl`, armed at load,
never re-armed. **Crons: ZERO.** **HEAD `a025e2be91`; `origin/SITEZ` `bc570d9e0d`; all three of my
commits ARE on origin/SITEZ** (pushed by MSTR~Z, not by me -- push is the integrator's).

Ordered for the successor:
1. **[3.0.0_SA_CVO~Z]** Certify `D1_NAMEDISCOVERY` -- unstarted, unblocked, and explicitly declined by
   `1.0.0_SA_CTO~Z` so that it stays with the independent seat. Re-derive CTO~Z's staleness read
   rather than inheriting it; the `placement LAPTOP` header line IS stale and D1 IS SITEZ.
2. **[3.0.0_SA_CVO~Z]** Certify the two D8 / `MDPF_COTREMEDIATION` decomps (section 3d), carrying
   COO~Z's PARKED-target-architecture constraint verbatim.
3. **[3.0.0_SA_CVO~Z]** Run the S19 trading-calendar measurement (section 4). Held here, promised to
   `0.7.0_AE_CloudOps~Z`, not started.
4. **[3.0.0_SA_CVO~Z]** Two base-serial TOs read ACTIVE: `D3_MODELOVERLAY.TO-D3.5` (staged, GATED ON
   TO-D3.4) and `OPAL_ADVIPOINTERS.P4-PINS-CERT-49F` (whose own status line already reads GROUP CERT
   CLOSED 2026-08-21 -- **likely a stale-open row, verify before working it**).
5. **[0.0.0_AB_MSTR~Z]** End-of-session CLOUD<->SITEZ convergence, per Andrew. Blocks nothing here.

-- 3.0.0_SA_CVO~Z
