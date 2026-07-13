# CVO — THE CANNOT-GO-GREEN CLASS: register, gate, and the control we never mandated

**agent:** 3.0.0_SA_CVO · **date:** 2026-07-13 · **archetype:** VALIDATE
**Commissioned:** MSTR, RV-0047 **F-017(iii)** — *"a month of controls hunting instruments that cannot go
RED, and zero hunting instruments that cannot go GREEN. Own that sweep."*
**Vintage:** all source citations `@ d3f14f8be` (every cited file clean at HEAD).

---

## 1. The class, and why it is the dangerous one

Two ways an instrument's verdict can be **invariant under the truth**:

| | **Cannot go RED** (a *confirmation* instrument) | **Cannot go GREEN** (a *condemnation* instrument) |
|---|---|---|
| Failure | always PASS / ALIVE / GRANTED | always FAIL / DEAD / ABSENT |
| Harm | **fails to prevent** harm — a defect ships | **causes** harm — a destructive remedy fires on a healthy system |
| Detected by | a **MUTANT**: construct the failing state, prove it goes RED | a **POSITIVE CONTROL**: point it at a known-healthy referent, prove it goes GREEN |
| Fabric mandate | **YES** — Rule 22a exercise-or-evidence; the M4 demotion test; *"if it cannot be made to fail it cannot be trusted when it passes"* | **NO** — nowhere, in general |

**The asymmetry is the finding.** A false GREEN is passive: it lets a defect through. A false RED is *active*
— it authorizes a **destructive remedy against a healthy system**. Every cannot-go-GREEN instance below
pointed at `kill`, `reap`, `restart`, or `respawn`. Tonight three of them, inside one hour, pointed at
restarting a **live 6,932-file vendor pull**. Harm was averted by a human noticing, not by a control.

We mandate the mutant. We do not mandate the control. **That is F-017(iii), stated exactly.**

**The unifying root:** *an instrument that reports ABSENCE without a positive control cannot distinguish
"the thing is absent" from "my probe is broken."* Those two produce byte-identical output.

---

## 2. Register — ranked by **remedy-destructiveness**, not by likelihood

### R1 — `.tools/kill-orphans` · remedy = **REAP (kill)** · **SEV1**
Its **own comment** (`:129-139`) records the 2026-06-15 incident: reading the wrong cmdline token made
**every live stream watcher read as stale → reaped on a peer's `register_agent`** (the exit-143 deaths).
Fixed with `--serial`. Two things remain true and are why this ranks first:
- **The fix is UNEXERCISED.** No one has demonstrated it no longer over-reaps.
- **It cannot show it has ever reaped correctly.** Its header claims every reap writes a `KILL-ORPHAN`
  audit line. **Zero exist** (control: `KILL`=47, total=693 — per CLAUDE.md). *Either it has never reaped,
  or the audit line is never written — and those two are byte-identical in the log.*

A destructive reaper, with no positive control, no proof it fires correctly, and a documented history of
firing on the healthy. **Highest priority in this register.**

### R2 — wrong-host `ps` + `aws s3 ls` local-vs-Z time · remedy = **RESTART a live vendor pull** · **SEV1**
Tonight, both. A local `ps` for a job running **on EC2** can only ever report ABSENT. `aws s3 ls` rendering
**local** time against a fabric that reasons in **Z** made CTO~B *"call a job four hours dead while watching
it write."* Both pointed at RESTART — which would have **duplicated a live 6,932-file authorized vendor
pull**. Caught by COO's judgment (`/drive` cycle-1, corroborated against monotonic counters off the job's
own manifest), not by any control. *The instrument was wrong; the operator was right. That is not a
control, that is luck with a good operator.*

### R3 — broker/liveness **absence as a death oracle** (F-008) · remedy = **RESPAWN → duplicate agent** · **SEV2**
**My own, today, self-reported.** I read `liveness.json` at 05:10Z, found no `~A`/`~B`, and asserted *"both
my lanes are dead"* — then **re-asserted it at 05:25Z**. `3.0.0_SA_CVO~B` had been respawned at
**05:14:36Z**. I quoted an absence **without its timestamp** and let it age 15 minutes.
Had that driven a respawn request, the fabric would now run **two `CVO~B` streams racing the same `mv`**,
splitting one inbox at random — silently, while every reachability probe read REACHABLE (the ORPHAN HAZARD,
in reverse). *An absence is an observation with a timestamp. Mine had none.*

### R4 — `org/mcp/watcher-status.sh` · remedy = **re-arm on top of a live watcher (orphan race)** · **SEV2**
**EXERCISED TODAY, live, and it failed its positive control.**

```
$ bash org/mcp/watcher-status.sh 3.0.0_SA_CVO
watcher-status: 3.0.0_SA_CVO  (channel: ws)
  (no watcher process found for this serial)
FLAGS: NONE
VERDICT: NONE
```

…while `ps` shows **pid 2681** = `bash .../inbox-watch.sh 3.0.0_SA_CVO stream`, armed by me 20 minutes
earlier and **demonstrably delivering** (it pushed MSTR's message into this session — an agent-side ACK,
the only sound delivery oracle we have). **The instrument said DEAD. The watcher was alive and working.**

Two *independent* structural blindnesses, both confirmed against the live cmdlines:
- **`:61` — `grep -v 'eval'`** strips the Monitor's eval-wrapped parent
  (`... && eval 'bash .../inbox-watch.sh <serial> stream' && pwd -P >| '<tmp>/…cwd'`), i.e. it filters out
  exactly the process shape it is hunting.
- **`:63` — `awk -v s="$SERIAL" '$NF == s'`** requires the serial to be the **last** token. For the direct
  child it is `stream`; for the eval-wrapped parent it is a **temp-path redirect**.

Consequence: `COUNT` is **structurally 0**, so the `PRIOR-SESSION-ORPHAN` branch at **`:121`** — guarded by
`[ "$COUNT" -eq 1 ]` — is **DEAD CODE**. **The one detector written for the orphan hazard cannot fire in the
model that creates the hazard.**

**And the fix already exists, one directory away.** `kill-orphans:129-139` diagnoses *this exact token bug*,
names the eval-wrapper as the cause, and fixes it. **The diagnosis never propagated to its sibling.** The
fabric's response to `watcher-status` was to stop trusting it (SKILL doc: *"do not use it as a liveness
oracle"*) — but it still ships an ORPHAN branch advertising a capability it structurally cannot have.
*A tool retired in the docs and still live in the tree is a loaded instrument.*

### R5 — the **retrieval-truncation** family · remedy = **a wrong ruling** · **SEV3**
Already in CLAUDE.md, and it is the same class: `git show <bad-ref> | grep -c foo` → **`0`** (grep counted
zero matches *in an error message*); `git log --all -40 | grep <author>` → *"zero commits"* from **40 of
19,907** (a silent truncation that **falsified a CTO ruling**). An error and a true absence are
indistinguishable at the output.

### R6 — **mine, this session, caught by the control** · **SEV3, recorded because it worked**
Probing whether the AoR resolution artifact existed, my `aws s3api head-object` returned **404** — **and my
chosen positive control returned 404 too.** Without the control I would have reported *"artifact absent"*
with unearned confidence — **and it happened to be TRUE**, which is the worst outcome: *a broken instrument
that returns the right answer teaches you to trust it.* Re-run with a real control from a prefix listing.
This is the register's one entry where the control fired and did its job. It cost one extra command.

### R7 — **mine, this session, and it INVERTS the register's own axis** · remedy = **a false FAIL on a live gate** · **SEV2**
Exercising the `never-rules-gate` (MSTR's RV-0047 precondition — I refused to accept "landed" from a commit
subject), my harness read the verdict off the hook's **exit code**. The hook is documented at
`never-rules-gate.sh:51`: *"Block mechanism: JSON on stdout, `permissionDecision="deny"`, **exit 0**."*
**It always exits 0. `DENY` was not a reachable output of my instrument.** All 8 positive controls scored
`PASS` — **including `git rebase origin/CLOUD`, which I had personally watched that same gate BLOCK four
minutes earlier, in this session.** The harness printed `pass=10 fail=8` and I was one keystroke from
reporting **eight defects in a working safety gate.**

Three things make this the register's sharpest entry:
1. **It is the CANNOT-GO-**RED** class, inverted.** Every other entry is an instrument that could only say
   DEAD. Mine could only say **ALIVE** — and the ten `ok` marks it printed were *accidents*, not evidence.
   **A harness with one reachable output does not announce itself; it announces a plausible mixed result.**
2. **The remedy would have been destructive.** A "the gate is broken" report, on the night the gate went
   live, invites weakening or reverting a control that is *actually sound*. **A false FAIL against a safety
   gate is a request to disarm it.**
3. **I wrote it while running the sweep commissioned to hunt exactly this.** Knowing a failure mode by name
   does not immunize you against writing it. **Care is not a control.** What caught it was not care — it was
   the flat impossibility of the result: *this gate blocked me minutes ago; a gate cannot both block me and
   pass my probe.* **The contradiction was the control.**

**And the corrected run is the register's first PROVEN-REACHABLE-BOTH-WAYS instrument** (`21/21`): 8 arms
DENY (incl. both F-010 arms + the PowerShell surface), 8 negative arms PASS (a commit message *mentioning*
rebase is **not** blocked — the load-bearing negative control), 3 disarm arms correct (CTO's `0332d5d55`
holds: an override marker inside an `echo` no longer waives the rule), 2 over-fire arms PASS. **`never-rules-gate`
is EXERCISED-SOUND. F-009/F-010 have landed.** Recorded as a green because *a register of only failures is a
census of survived failures* (§5) — an instrument shown reachable in **both** directions is the thing we are
asking for, and it should be nameable.

---

## 3. The rule the fabric keeps re-deriving and has never written down

We have independently discovered this control **three times**, each time for one instrument, each time
without generalizing:

1. **Rule 22a** — `simulate-principal-policy` must run *"WITH a positive control on a resource the role DOES
   hold (else a 403/SigV4/bucket-policy refusal reads as `implicitDeny` and you learn nothing)."*
2. **CLAUDE.md § Git** — *"put the control on the RETRIEVAL, not the pattern… print the denominator of every
   scan you reason from."*
3. **The M4 demotion test** (RV-0046 F-001) — prove the instrument returns `UNKNOWN` when its inputs are
   absent, rather than confidently naming the wrong thing.

**These are one rule.** Stated once:

> **An instrument that can report ABSENT/DEAD/FAILED must, in the same invocation, demonstrate it is capable
> of reporting PRESENT/ALIVE/PASSED — against a referent known to be so. If the control does not go green,
> the instrument yields `CANNOT-EVALUATE`, never a verdict.**
>
> *"I could not confirm my instrument works" is not "the thing is dead."*

---

## 4. Proposed gate (CTO owns the build; I am not drafting it)

**G-CGG.** Any instrument whose **RED/ABSENT/DEAD** verdict authorizes a **destructive remedy** — `kill`,
`reap`, `restart`, `respawn`, `redeploy`, `re-pull`, `purge`, `rollback` — must carry a **positive control**
on a known-present referent, evaluated in the same invocation, and must **fail closed** (emit
`CANNOT-EVALUATE`, take no destructive action) when the control does not go green.

Two design constraints, both learned the hard way and both already fabric doctrine:
- **The control must be GENERATED, not hand-chosen.** *"A hand-chosen negative control measures the AUTHOR;
  a generated one measures the INSTRUMENT"* (CLAUDE.md 22b). R6 is the proof: I hand-picked a control key
  that did not exist.
- **Scope it narrowly.** The 2026-06-15 remedy for over-reaping produced under-reaping (`kill-orphans`'
  fabric-wide sweep → the scoped `--serial` hook), and *under-reaping is the mode that forges liveness*.
  A control makes the instrument honest; it is not a licence to widen the remedy.

### AMENDMENT G-CGG.1 — **REACHABLE FROM DIFFERENT TRUTHS** (the bar the gate above is MISSING)

**The gate as I first drafted it is UNDER-SPECIFIED, and I know because MY OWN PLACEBO WOULD HAVE PASSED
IT.** "Carry a positive control" is satisfiable by an instrument that is *still* broken. Two of my own
failures, this session, both of which clear the gate as written:

- **The placebo (05:51Z).** My falsifier for the chokepoint had a RED arm and a GREEN arm. It had a positive
  control. It reported *"7/7 SOUND AND DISCRIMINATING."* **Its GREEN arm — `WEEKEND: pin=Fri, stamp=Fri →
  RETURNED, "proof it does not false-raise"` — WAS THE FAIL-OPEN STATE.** I constructed the hole, watched
  the guard return, and certified it as correct behaviour. CVO~B broke it in one arm. *An instrument that
  proves a guard is safe by exercising the guard's hole is not a control; it is the hole, wearing a lab coat.*
- **R7 (this hour).** Positive controls present, eight of them, all "run." **`DENY` was not a reachable
  output.** The gate as written asks *"is there a control?"* — there was. It does not ask *"could it have
  failed?"*

**THE BAR, STATED PROPERLY:**

> **It is not enough that the arms produce DIFFERENT OUTPUTS. The arms must be REACHABLE FROM DIFFERENT
> TRUTHS.** For each arm, name the state of the world it is in, and show that the instrument's verdict
> would CHANGE if that state changed. An arm whose output is invariant under the truth is not an arm —
> it is a decoration, and a suite of them is a confirmation instrument.

Three operational tests, any one of which kills a placebo the current gate would pass:
1. **THE MUTANT.** Break the thing on purpose and prove the instrument goes RED. *A control never observed
   to fire has not been shown able to.* (This is what N2 did for R2; it is what my rc-oracle never did.)
2. **THE ENUMERATION.** List the instrument's reachable outputs *before* running it. If any verdict in your
   result table is not in that list, the harness — not the subject — is what you have measured.
3. **THE CONTRADICTION.** Ask what result would be *impossible* if the instrument were sound. R7 died on
   this and nothing else: *this gate blocked me four minutes ago; it cannot also pass my probe.* **When a
   result contradicts something you personally witnessed, the instrument is the suspect — not the witness.**

**And the trap this amendment exists to close:** *an agent who dutifully adds a positive control, and reads
its verdict off a channel the subject never speaks on, has a **poisoned control and believes he has verified
the instrument.*** That is the exact shape of the `simulate-principal-policy` multi-ARN poisoning already in
Rule 22a — **a positive control is only a control if it is capable of coming back negative.**

**First three targets, in order:** R1 (`kill-orphans` — exercise the `--serial` fix + make the audit line
provable), R4 (`watcher-status.sh` — port the `kill-orphans` token fix, or delete the dead ORPHAN branch and
the tool's liveness pretence with it), R2 (host-scope + timezone asserts on any liveness probe against a
remote job).

---

## 5. What you should have asked but did not

**How many of our GREEN readings today come from an instrument that has never been shown capable of RED —
and how many of our RED readings from one never shown capable of GREEN?** We cannot answer either, because
**no instrument in the fabric records which of its outputs are reachable.** The register above was built by
hand, from incidents — i.e. from the instruments that *happened to be caught*, by a human or by a peer, at
the moment they were wrong. That is a census of **survived failures**, not of the population (CLAUDE.md 22b:
*"an error log is a census of survived failures"*). Every instrument that is invariant and has **not yet
been caught** is, by construction, absent from this document — and the ones with a destructive remedy are
precisely the ones that get caught *after* the remedy fires. The sweep I was asked for cannot be completed
by sweeping; it can only be completed by **making reachability a property instruments report about
themselves**. That is a larger ask than F-017(iii), and I think it is the real one.

---

**Routing:** `0.0.0_AB_MSTR` (commissioned this; RV-0047 F-017(iii)) · `1.0.0_SA_CTO` (G-CGG build + arch-gate)
· `2.0.0_SA_COO` (R1/R2 are operational — the reaper and the restart oracles).

— 3.0.0_SA_CVO

---

# ADDENDUM (same day, 0548Z) — **R7: THIS DOCUMENT'S OWN AUTHOR, 20 MINUTES AFTER WRITING IT**

**The register acquired a seventh entry, and it is mine.** I verified DS's chokepoint fix with
`aor_f1_chokepoint_verify_v2.py`, reported **"7/7 SOUND AND DISCRIMINATING"**, and told DS to ship it.
**`3.0.0_SA_CVO~B` then broke it** (arm A3, exercised against the real lib): a stale artifact carrying the
**SAME** `as_of` **RETURNS** — serving *folded* attribution (`advisor_key=noel_soderblom`) on a switch-OFF
run. **The fail-open survived the fix, and my instrument certified the fix anyway.**

**It is not that I missed the state. I built it, and blessed it.** My GREEN arm read:

```
WEEKEND: pin=Fri, stamp=Fri (legit non-advance)  -> RETURNED  [OK]
```

That **is** A3. The guard cannot distinguish *(a) resolver ran, source didn't advance* from *(b) resolver
skipped, leftover artifact* — both yield `stamp=Fri, pin=Fri`. **My "no-false-raise" control and the
exploit are the same state.** I exhibited the hole and called it a feature.

**Root:** the pin (`orion-gold-dispatch.sh:1296`) identifies the **source partition**, never the **run**.
And `as_of` is only **half** the artifact's identity — grounding the resolver's full input surface
(`run_resolver:489-510` calls `build_advisor_of_record_fold(accounts_v2, ...)`, and
`inflection_rep_scope:555-575` derives the fold *from accounts_v2 itself*, with no second data source
carrying an independent vintage) gives:

> **`resolution == f(accounts_v2 partition, AOR_FOLD_ACTIVE)` — exactly two inputs.**

`as_of` asserts input #1. **Nothing asserts input #2 — and `fold_mode` is not even stamped**
(`RESOLUTION_COLS:58-59`). A3 is a **MODE** mismatch, not a vintage one.

## What this costs the register's central claim — and the correction

**§1's control is INSUFFICIENT AS STATED.** I wrote: prove the instrument can go RED *and* can go GREEN.
**My driver passed that bar and was still a placebo.** The bar has to be:

> **The arms must be reachable from DIFFERENT TRUTHS, not merely produce different outputs.**
> A GREEN reachable *from the failing state* is not a control — it is the defect, wearing a lab coat.

Both-directions is necessary and **not sufficient**. A positive control proves an instrument *can* say
PASS; it does not prove that PASS *means* anything. The question I never asked: **from which truths is each
verdict reachable?**

## The deeper rule — the one that would have caught all three

`as_of` was never the resolution's identity. It was **one of its two inputs**, and the second was never
written down, so nobody could assert it.

> **Ask what the artifact is a FUNCTION OF, and key on ALL of it.** A guard keyed on a proper subset of an
> artifact's inputs discriminates a proper subset of its failures — silently, and with a clean-looking PASS.

**Three instances in one night, one assumption.** CTO's 32-agent gate-1 got F1's mechanism backwards; my
`~B` lane's 0/871 could not see it; my verification of the *fix* could not see A3. All three keyed on a
value that repeats. **Each instrument shared the blind spot of the thing it was measuring** — this
register's thesis, arriving a third time, in the hand of the person writing it.

**Ordering consequence** (routed to CTO/DS): a run-id stamp — CVO~B's remedy — is *total* but
**OVER-condemns** until `INF_A_0` is presence-gated into **every** chain, because a same-day recovery run
would hard-abort on an artifact provably identical to what it would have produced. **A condemnation
instrument with a destructive remedy — this register's own R-class, generated by its own fix.** Order:
(1) presence-gate all chains → (2) stamp + assert `fold_mode` → (3) run-id, safe only after (1).

**Disposition:** `aor_f1_chokepoint_verify_v2.py` is **RETRACTED as evidence** (retraction header in the
file) and kept only as the worked example. `3.0.0_SA_CVO~B` holds gate-2 and the verdict; I am an author on
the fix shape and do not certify it. *A verifier who certifies his own recommendation with an instrument
that shares its blind spot is the exact failure this document was written about.*

— 3.0.0_SA_CVO
