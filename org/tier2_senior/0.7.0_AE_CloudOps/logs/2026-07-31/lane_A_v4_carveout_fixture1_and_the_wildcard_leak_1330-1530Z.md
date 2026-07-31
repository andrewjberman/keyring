# ~A: v4 carve-out relayed, fixture-1 rebuilt as a DETECTOR, and a mid-key wildcard leak my own battery would have passed over

**archetype:** MIXED (VALIDATE + IMPLEMENT + COORDINATE)
**Serial:** `0.7.0_AE_CloudOps~A` (session 59c5ee8f, PID 33196, Monitor `b5guvgbz3`)
**Window:** 2026-07-31 ~1330Z -> ~1530Z (9:30 -> 11:30 AM ET)
**Prior log:** `lane_A_startup_and_aug1_runtime_verify_1303-1325Z.md` @`18c41ed145`
**Verbatim record:** `lane_A_andrew_direct_v4_carveout_granted_1330Z.md` @`3e93fd8e92`

## The carve-out, and why the relay mattered more than the work

Andrew granted the estate-report v4 carve-out at my terminal ~1330Z (verbatim in the record log above).
**Three live seats were each independently parked on that exact word** -- `~B` ("parked pending Andrew's
carve-out word"), MSTR (RESERVED item "~B v4"), CVO ("regime-status at Andrew"). Recorded + broadcast
same turn per XXX.md. Scope fenced explicitly: it unparks the named project and **nothing** else -- not
TAP, not the 8 base TOs, not the $532K INF orphan. *A grant is where over-reading happens.*

**I did not take `~B`'s lane.** Andrew addressed ~A; the seat holding the work with context and a clean
seam was ~B. I relayed and offered to take only the gate. CVO then converted the near-collision into a
**separation-of-duties split**: ~B authors, I exercise -- *the author of a boundary must not be the one
who proves it for the lift.*

## Fixture 1: from a thing that could not fail into a detector

| | before | after |
|---|---|---|
| corpus | live, still-appending path | frozen copy, **pinned by sha256** |
| assertion | a COUNT (`8 stored`) | **enumerated by `dedup_key`**, 10 named utterances |
| on drift | indistinguishable from a grown file | **REFUSES to run** (exit 2) |
| on a dropped utterance | "not 10" | **FAILS and NAMES which** (exit 1) |

**BOTH failure paths EXERCISED, not asserted** -- truncated corpus -> refused; injected key -> failed
naming it. PASS state 10/10 over 498 rows. Delivered @`ece68dad0d`, @`0bc4646b62`, @`8f10cc62cc`;
**CVO ACCEPTED**.

**The cross-verification lattice is the part worth keeping.** ~B's keys, my detector, ~B's changed code,
each verified from the other side: I refused to re-derive their enumeration (a copy wearing a
verification's clothes is perfectly correlated with what it checks); they closed the confirmation gate
by running MY detector at THEIR post-fix HEAD; then they changed the classifier under me (213 forged
quotes removed corpus-wide) and told me **not** to trust their assurance -- so I re-derived at their new
code myself. 10/10, no drift. **Their control PREDICTED it; my fixture CONFIRMED it from outside.**

**~B's custody finding, banked as its own class:** they are a FRESH session and did **not** hold the
ground truth CVO attributed to them -- their predecessor did. **Provenance attaches to a SESSION, not a
SERIAL; a log inherits the claim without inheriting the evidence.** They re-established it themselves
rather than launder a record through a matching serial.

**The coverage bound now prints in the fixture's own output**, on ~B's finding: **a fixture is a SAMPLE.**
213 forged quotes (5.9% of a 3,628-record corpus) sat misclassified as human speech *the entire time
fixture 1 was passing*, because this one session contained none of those classes. **The fixture was green
and the corpus was wrong simultaneously, and neither fact disproved the other.**

## The mid-key wildcard leak -- the sharpest thing today, and it was aimed at me

`~B` found that the ruled shape `*/text-input/*` LEAKS. **I reproduced it on a policy document I authored
myself**, sharing no substrate with their draft or the applied policy:

```
CONTROL  {day}/text-input/x.md                   -> allowed
         {day}/signed-review/x.md                -> implicitDeny   <- MY battery's DENY cell. CORRECT.
         {day}/signed-review/text-input/evil.md  -> ALLOWED        <- the leak
```

**IAM's `*` matches `/`.** So my step-4 battery **would have returned GREEN over a live
producer-writes-the-reviewer-surface hole** -- not through a broken instrument but through an honest one
**aimed one segment too shallow**. That is worse than my VOID case, because *the VOID case announces
itself.*

Fix `/????-??-??/text-input/*` verified **5/5, both directions** -- including two ALLOW cells, because
**a fix that only denies is satisfiable by denying everything**. CVO adopted that as standing: *every
tightening proves it did not over-tighten, or it is a denial dressed as a fix.*

**My residual, found by probing rather than trusting the name:** `????-??-??` is a **SHAPE matcher, not a
date validator** -- `aaaa-aa-aa/text-input/` is ALLOWED. CVO reached the same finding independently by
position-analysis and **extended it: `?` also matches `/`**. Severity read RATIFIED as offered: not the
leak's class (that crossed the producer/reviewer fence; this pollutes the producer's own namespace) --
**recorded as a known bound, gate not held on it.** Written down because *"date-shaped" reads like a date
constraint and the next person will believe the name* -- a name that overstates its own guarantee is the
stale-record class at birth.

**Three standing battery cells now, all the same family -- a battery can be ENTIRELY HONEST and still
prove nothing:** fallback-mutant FIRST (else every verdict describes a principal the code never used) ·
the DISCRIMINATOR (all-deny = VOID, never "boundaries held") · the NESTED SIBLING (`*` is not `[^/]*`).

## Errors I made, and the one shape they share

1. **`ajb.ps1` "untracked"** -- wrong. It was landing (`@81660e0f2a`) *while I observed it*: `A ` -> `??`
   -> tracked-and-clean across three reads. CTO nearly composed a `.gitignore` protection off my premise.
2. **Told Andrew step-0 was waiting on him** ~30 min *after* his YES discharged it.
3. **A positive control pointing the wrong way** -- I "proved" an identity test worked by checking a file
   that could not possibly match. That shows it can say DIFFERS, not that it can say IDENTICAL. Redone;
   conclusion held but had not been earned.
4. **`5.9%%` rendered literally** -- caught only by reading the actual output.

**(1) and (2) are one shape: a claim TRUE WHEN FORMED, asserted after it stopped being true.** The
carrying rule: *when I report that something is blocked ON A PERSON, that is the claim most worth
re-checking before saying it, because it is the one that makes someone act.*

**I disarmed my own staged battery** @`4280d68923` when CVO's ruling superseded it 25 minutes after I
wrote it -- it had become a FALSE-FAILURE trap (it asserted DENY on past-day, which the new ruling makes
EXPECTED), so against a *correct* policy it would have reported a healthy boundary as broken. Hard
`exit 99`, zero output, EXERCISED. **A false failure on a gate is not a safe error: it manufactures
pressure to fix a fence that is right.** CVO ratified the disarm form.

## Shared-worktree discipline

Push blocked repeatedly by another seat's STAGED work. **I proved those paths were NOT on origin, so
unstaging would have destroyed unpushed work -- I waited rather than cleared**, and did not force-clear an
`index.lock` either. CVO confirmed they made the same call on the same collision. All 7 of my commits
verified on origin against a **freshly fetched** ref (a remote-tracking ref can be stale), with a control.

**`ajb.ps1` is HANDS-OFF by Andrew's word** -- read-only diagnostics only, left byte-identical.

## COO seat verification (and a stale record of mine, corrected)

LD-0367 (integration window, `:55-:00` hold, base MSTR sole integrator) arrived from `2.0.0_SA_COO` -- a
seat my records said was **KILLED 07-30**. Per standing memory (`send_message` has no sender auth; a
surprising Tier-1 sender is an ASSERTION), I verified on **three independent** signals -- broker, `ps`
process truth, and same-day commits + `LD-0367.md` on disk -- not two broker calls, which is one signal
counted twice. **All agree: COO was RESPAWNED (LD-0365). My record was the stale thing, not their
message**, and that is the dangerous direction: it teaches an agent to read a legitimate order as a
forgery. Corrected in MEMORY.md; receipt confirmed to COO.

## Deployment Sequence + Verification (AE addition)

**NO DEPLOY. Zero AWS mutation.** Every AWS call read-only (`get-role-policy`, `s3 ls`,
`list-objects-v2`, `head-object`, `get-function*`, `scheduler get-schedule`) plus `simulate-custom-policy`
against **policy documents I authored myself** -- never the applied policy (CVO's explicit instruction)
and never ~B's draft. No Terraform, no safe-apply, no tags.

## Compiler Tools

| Tool | Why | Result | Note |
|---|---|---|---|
| `comp-which` | Rule 21 reflex before raw calls | ROUTED | -> `comp-trigger` (1.50 of 68 ranked) |
| `comp-trigger etfs` | what fires the Aug-1 report | PASS | denominator printed: 142 rules + 12 schedules |
| `comp-glob` / `comp-grep` | locate capture tool + CLI surface | PASS | comp-grep WARNED me that `\|` is literal in Python re -- a real save |
| `commit-gate.sh` | Rule 14, every `.py` | PASS x3 | |
| `comp-surface-check` / `comp-pulse` | in safe-commit x7 | CLEAN | denominators printed (1 file vs 1622 danger nodes) |

**Gap found:** `comp-trigger` renders `schedule: -` for EventBridge **Scheduler** entries -- it carries
the expression for events-rules but not schedules, so it could not tell me the fire time, timezone or
flex mode. Went to `aws scheduler get-schedule` with a `# rail-checked:` marker. **A tool that can only
report the EXISTENCE of a schedule cannot answer "when does it fire".**

## Blockers

**None of mine.** Step 4 waits on ~B's step 3 (apply) -- released, not blocked. Two at Andrew, neither
urgent today: the **retention ruling** on his own verbatim words (keeps the corpus out of the repo), and
MEMORY.md sitting **~456 bytes over its own 17,408 cap**, where the overflow is the NEWEST entries.

## Next Steps

1. **[0.7.0_AE_CloudOps~B]** step 3 apply; signal me. I will not poll and self-start.
2. **[0.7.0_AE_CloudOps~A]** step-4 applied battery on that signal: fallback-mutant FIRST, discriminator,
   per-principal ALLOWs (past-day ALLOW **expected**), cross-principal DENYs, nested-sibling cell,
   residual cell, storage exercises. Evidence to CVO; **I do not lift the hold.**
3. **[0.7.0_AE_CloudOps~A]** Aug-1 ETFS fire, 10:00 AM ET tomorrow. Verified ready; **the cheap
   sufficient re-check is the renderer's VersionId** (`chTZ82Vf...`) -- md5 equality would NOT reveal a
   re-upload.
4. **[Andrew]** retention ruling. **[MSTR]** MEMORY.md cap.
