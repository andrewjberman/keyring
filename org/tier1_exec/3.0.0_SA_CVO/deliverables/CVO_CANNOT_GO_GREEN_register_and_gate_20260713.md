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
