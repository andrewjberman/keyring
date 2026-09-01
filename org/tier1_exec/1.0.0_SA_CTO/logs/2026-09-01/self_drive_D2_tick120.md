# /self-drive D2 — tick 120

**Seat:** `1.0.0_SA_CTO` · **State:** ARMED · **Cron:** `e106e9c8` · **UTC:** 2026-09-01 ~15:1xZ
**Ticks covered:** 120 · **Carrier:** `org/XXX.md:633` @`e706f59f62` · **Paired:** `/drive` @ `2.0.0_SA_COO`

```
COMPLETION: 2 of 10 -> NOT DONE      ledger: 38      open_tos: 17
CURSOR: DERIVED from commit 218935323e @ 10:29:25-04:00 -- the rule landed this session
MOVEMENT: 4 seats / 7 commits.  POSITIVE CONTROL FIRES: 1.0.0_SA_CTO present (2)
OPEN CALLS: 0 new adjudicable
```

**The cursor rule I landed at `0c4ba9a8cd` was exercised on its first tick and its positive control
passed** — my own serial appears in the movement scan, which is exactly the check that would have
caught COO's future-dated cursor.

---

## Driver acts

### 1. G-1 — NOT settleable from its carrier, and my own number was over-claimed

I reported G-1 as *"floating from 51 days."* **`comp-schedule` prints that field with its own
disclaimer attached to every row** — DERIVED from the carrier's last EDIT, a WEAK proxy, it dates the
edit and not a human confirming the gate is needed. **I carried the value and dropped the label**, to
a tool that had pre-empted exactly that.

G-1's sentinel is one line naming two conditions with no discharge record; its subject phrase returns
**83 hits across 142,069 files**. Settling it is a scoped read. **G-1 stays ARMED and explicitly
UNSETTLED** rather than assumed stale from a number that does not measure staleness.

>> **THE STRUCTURAL FINDING: G-4 carries its own discharge state and I settled it in ONE read. G-1
   carries two condition NAMES and cannot be settled by reading it AT ANY LEVEL OF CARE, because the
   information is not in the carrier. The difference is not diligence — it is whether the author
   wrote the discharge state INTO the sentinel.** A one-line sentinel is a POINTER, and elsewhere
   decays. <<

### 2. The memory system — the afternoon's durable finding, and it is not about the pipeline

`3.0.0_SA_CVO` named the mechanism: **a COMPACTION.** The `simulate-principal-policy` conditioned
false-deny trap was known since **2026-07-13**, in **two independent entries** in `MEMORY_FULL.md`
(one explicitly warning *"do NOT dedupe"*) — **and `MEMORY_FULL.md` is not loaded at startup.**

```
  the archived line already recorded THIS afternoon's epistemics, seven weeks early:
  "the unconditioned positive control passes while the conditioned one silently false-denies --
   A POSITIVE CONTROL THAT CANNOT EXHIBIT THE FAILURE MODE IS NOT A CONTROL."
```

⛔ **The compaction was CORRECT by its own rules and silently disarmed the knowledge.** Fix landed in
the hygiene section that caused it: **archiving is DISARMING, not filing** — never compact out an
entry that must fire UNPROMPTED (instrument traps, false-deny modes, NEVER-class hazards); compact
narrative instead. **And the tell that recall failed is WRITING A DUPLICATE** — which is how this was
found, because I wrote one.

I merged today's incident into the pre-existing entry and deleted my duplicate.

### 3. Measurement: `92077`'s discriminator does not fire, and that located the real gap

```
  chain_20260901T094639Z.log, whole file:
     "at or before"        0     <- the POST-FIX signature
     Traceback/NoSuchKey   0     <- the PRE-FIX signature
```

**A test whose two outcomes are BOTH absent has not been run.** Cause, from the log's own line:
`MANIFEST (local): /tmp/49f_chain_work/perfrp_projection/out/manifest_...json` — **the perfrp stage
writes its manifest LOCAL-ONLY while the a07 stage two lines above logs a successful S3 upload.**

>> `emitter_tail` — the sole carrier of every refusal reason — **is in that unuploaded manifest. Five
   seats read a bare dash in a log all afternoon because the reasons were never in the log.** This is
   a STANDING observability gap: **no chain run's refusal reasons survive the instance cycling.** <<

## The afternoon's shape, recorded because it is the lesson

**SEVEN hypotheses raised, all dead or retracted. TWO were mine, and one I relayed into five inboxes
with a sovereign quotation attached** — which lends a claim credibility it has not earned.

⛔ **NOT ONE DIED ON A BAD MEASUREMENT.** The empty `asof` was real. The `implicitDeny` was real. The
6-to-0 is real. The 82-file sync is real. **What kept failing was the SENTENCE CONNECTING a real
measurement to a conclusion.** Hence the tick's last act: naming the unstated premise under COO's
sync measurement (*did the two invocations share a filesystem?*) **before** it is crossed, rather than
retracting an eighth time after.

⭐ **And the seats were the control, working as designed:** `0.7.0_AE_CloudOps~M` ran a test that could
have convicted its own accelerator and it did; `3.0.0_SA_CVO` retracted its strongest finding four
minutes after sending it; `0.4.0_DS_ClientPlatform~G` withdrew a self-attribution for a defect it had
not caused; `2.0.0_SA_COO` opened a channel nobody had read, measured both invocations at grain, and
**stopped without inferring.**

## RESERVED cards still at Andrew

- D3's order relative to D8 · whether the flow-ingestion defect widens the ruled 22.
- The PERFRP publish card, ONE card TWO limbs: (a) did 08:5xZ narrow the 04:0xZ ratification;
  (b) PER-FAMILY or PER-SET (per-set unsatisfiable by construction).

## Compiler Tools

`git log --format=%aI` for the DERIVED cursor (the new rule, self-exercised) · `directives-check.py
--json` + completion scan · `.tools/comp-schedule` · `comp-iam gaps` with a 243-hit positive control ·
direct greps of `chain_20260901T094639Z.log` **under the new question** · `comp-find --corpus all`
(denominators printed). No `head` on any census.

**PUSH STATE, MEASURED:** `0c4ba9a8cd`, `218935323e`, `72322d7f9c`, `a21267939d`, `4022ebae4a` and this
log LOCAL. `origin/CLOUD` = `c85701ebca` (fetch 13:4xZ) — perishable.

**State:** `ARMED` · next tick on the cron.
