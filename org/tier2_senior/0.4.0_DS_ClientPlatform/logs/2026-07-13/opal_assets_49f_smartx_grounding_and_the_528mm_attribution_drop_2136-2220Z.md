# OPAL_ASSETS -- the $290mm grounded, a $528mm live defect found, and the door refused (2136-2220Z)

**Agent:** 0.4.0_DS_ClientPlatform
**archetype:** DIAGNOSE
**Session:** 2026-07-13, 21:36Z -> 22:20Z (respawn, scoped)
**Scope:** OPAL_ASSETS ONLY (Andrew `8.) A.` via CTO, relayed by MSTR). **INF chain HELD -- not mine.**

---

## Current State

**Respawned under a scoped exception to the LD-0288 fabric respawn hold.** Read MSTR's inbox message before my own
logs, as instructed -- **correctly, because my own "Next Steps" were a list of doors** (wire the time-lock, deploy
atomically, run the one-shot, de-collide). All forbidden. None touched.

**Startup:** `/watcher` -> registered (PID 10444), persistent Monitor armed (`b160sm4ow`), **orphan scan CLEAN** for
my base serial. Flagged a `~A` orphan (pid 775570, ~11h) -- **not my serial, not reaped**; MSTR ruled LEAVE IT (a
one-off reap is a discipline patch against a design defect; the generator is F-003b, CTO's). **LD-0290 halt-gate
serial pinned** -- it was resolving to a shared churning file, so a `[STOP]` addressed to me **would have been
invisible to my own gate**. Real, not a no-op.

### Delivered (5 commits, all pushed)

| commit | what |
|---|---|
| `c6d07bf6a` | `49f_smartx_platform` grounding -- the $290mm |
| `44eb2f68b` | ETF `additive` assessment + the $528mm 49F attribution drop |
| `e95d8730a` | **AMENDMENT -- I withdrew my own magnitudes** |
| `dd53bb5ef` | mechanism CLOSED (the feeder went ABSENT, not stale) |
| `6a5ad23ce` | attribution-fallback SWEEP -- denominator 427/427 |

**1. THE $290mm (MSTR's red item) -- GROUNDED.** `49f_smartx_platform` binds `partners[49financial].model_aua`
(`lambda_function.py:566-567 @ bf7269a1e`) -- **the 5-term-model SLEEVE**. The true platform total (`total_aua` =
1,621.25mm) **sits one key away in the same served block**. Binding defect = **220.29mm**; residual vs Manav =
**69.86mm, STILL OPEN + `INFERRED`**. **The gap is TWO defects stacked, not one.**
**Second crossed name:** cohorts 8 and 9 both read master 08242234 today -- **cohort 8 ("49F Schwab custody (BD)")
is currently serving the SmartX platform total, i.e. Manav's actual number, under the wrong cohort's name.**
**CTO~B RULED (C):** structural separation, not a rename -- **row 8 is doing two jobs**. My proposed rename was
**rejected, correctly**: post-G2 cohort 8 *becomes* 08335338 and the 08242234 total would have **no cohort at all**.

**2. A LIVE $528mm DEFECT, found on the way.** On the 07-10 partition **`49financial` VANISHED from
`etf_decomposition.held_by_partner`** and ~$528mm of its ETF holdings were **silently reclassified as PUBLIC FLOAT**
(`public_residual` serves 622.58mm vs ~95mm truth). **Mechanism source-confirmed** (`mdpf_aggregate_aua.py:429-460`)
and **fully closed**: the RPS override feeder **went ABSENT, not stale** (`by_feeder.partner_held_etf = {}`); by
design an absent feeder falls back to the `target_weight` estimate; **49F has no composition rows, so there is no
estimate to fall back to**; the firm drops out of the loop and `residual = total - held_sum` absorbs all of it.
> **THE GRACEFUL-DEGRADATION PATH ASSUMES EVERY FIRM HAS AN ESTIMATE TO FALL BACK TO. 49F DOES NOT.**
> The docstring calls this *"zero-feeder behaviour preserved."* **It is preserved -- faithfully -- for the one firm
> it destroys.** *A fallback is only safe if the thing you fall back TO exists.*

**BOTH GUARDS SAW IT AND NEITHER STOPPED IT.** `sentinel_1` **fired at 559.7% -- an 11x breach of its own threshold**
-- and is `"audit-only, non-blocking; value stored"`. `identity_2` **PASSED** because it *"catches over-attribution
(<0), not under-attribution"* -- **it failed in the one direction the only gate pointed at it cannot see.**
`overall: PASS`. **The artifact confesses in writing and ships.**

**BOUNDED (checked, not assumed):** AUM headline **NOT** corrupted (audit-only; cross-validates $0.00). OPAL_ASSETS
G4 rows **NOT** corrupted (they read ETFS_CANON, a different path). **Artifact is FROZEN -- static, known, not
spreading.**

**3. THE SWEEP (CTO~B task (b), denominator PRINTED).** All **427/427** served partitions scanned, none sampled.
Firm universe = **2**. `target_weight:49financial` = **0/427** -- 49F has **never** had a fallback (measured, no
longer assumed). The 49F-drop occurs on **exactly ONE partition** -- a **first occurrence, not chronic**.
> **AND THE FINDING THAT MATTERS: the SAFE firm is safe BECAUSE IT IS ON THE LEGACY PATH.** Inflection survives an
> empty feeder only because it degrades to a `target_weight` estimate -- **the exact path Andrew's PIT-snapshot
> thesis exists to RETIRE.** **=> OPAL_ASSETS' OWN STRATEGIC DIRECTION CONVERTS SAFE FIRMS INTO LANDMINES.** The
> denominator is 1 *because the migration has only happened once*. **=> DO NOT SCOPE THE GUARD TO 49F.**

**4. ANDREW RULED** (via COO): *"They're both right but for different reasons, we just need all the components
granularly recorded daily, how we sum them is dependent on the presentation case."* -> **`additive` is not a property
of an ASSET; it is a property of the QUESTION.** **I surfaced the blocker nobody had: HIS RULING CANNOT BE
IMPLEMENTED ON TODAY'S DATA** -- `public_residual = net_assets - held` is a **subtraction across two vintages**, and
**there is no clean partition** (07-08 = correct attribution + **6-trading-day-stale** net assets; 07-10 = freshest
net assets + 49F dropped). Implementing on today's inputs would **granularly record a meaningless number, DAILY, with
a sovereign ruling behind it.** COO has put this in front of Andrew as the headline.

---

## ⚠️ THE TWO TIMES I WAS WRONG (both caught by others, neither by care)

**(1) The arithmetic trap I DODGED.** MSTR warned: *"1400.96 ~= 1404.94 is a coincidence-shaped clue, not evidence.
Find the LINE."* **The emitter does NOT sum the models** -- it reads one field. **The sum-of-models story was FALSE at
the emitter and TRUE at the producer.** Without that warning I would have edited the wrong file.

**(2) The structurally identical trap I WALKED INTO an hour later.** I published `public_residual ~= $95mm` and told
the fabric to use the 07-08 partition. **CTO~B's feeder grounding killed it.** The tell was **in a table I wrote
myself**: net assets were **byte-identical on 07-07 and 07-08, to the cent**. Live ETF net assets do not do that
across two trading days. **I read two partitions AGREEING as CORROBORATION instead of as the SIGNATURE OF A FROZEN
FEEDER.** Every magnitude **WITHDRAWN** (`e95d8730a`).
> **CARE CAUGHT NEITHER. One was caught by a warning, one by a colleague's independent grounding.**
> ***"Knowing a failure mode by name does not immunize you against writing it."*** Recorded as **LD-0292**.

**Also corrected upward:** COO's `1404.94` (**reproduces nowhere**; withdrawn, `cb54f7174`) and his instruction to
*"find the line that selects the 5 models"* (**that line does not exist**). And CTO~B **retracted** his own steer
after I argued **G1 is the TRIGGER, not the CAUSE**.

---

## ⛔ DOOR 6 -- REFUSED TWICE, AND IT CAME WITH EVIDENCE

**The repair for the $528mm is: patch the gold script, re-run mdpf, watch the number fall back.** **mdpf is
EVENT-DRIVEN on the INF spine sentinel and is frozen at 07-10 because it is CORRECTLY IDLE.** So *"re-run mdpf to fix
the ETF numbers"* **== writing that key == dispatching the HELD INF chain**, by an agent who believes he is fixing a
*different pipeline's* data quality.
> **THE FROZEN ARTIFACT FROZE IN A BROKEN STATE -- so the hold is now ACTIVELY SERVING A WRONG NUMBER, which makes
> lifting it look not merely tempting but RESPONSIBLE.** *The door does not need a careless agent. It needs a
> DILIGENT one with a REAL DEFECT IN HAND.* **And Andrew's ruling makes it MORE attractive, not less** ("re-run mdpf
> so we can record the components properly, as Andrew asked" -- **now with sovereign cover**).

**NOT WRITTEN. And exercised confirmation arrived from `0.5.0_AE_OpalETL` on live AWS config:**
`opal-data-inf` -> notification on `Prefix "gold/meta/" Suffix "pipeline-complete.json"` -> **LIVE** (his own bucket:
notification config **EMPTY** = a correct positive control). **The key is wired to live compute.** *(Precision: his
probe names `inf-portal-publisher`; the hold doc names `mdpf-daily-trigger`. **Not reconciled -- flagged, not
papered.** What is certain is the load-bearing part: the doorbell rings.)*

**I chased an agent-side ACK from `0.5.0_AE_OpalETL`** (spawned into the ETF lane; MSTR: *"the single most likely
person to trip your trap"*) **because SENT IS NOT READ.** **Got it, explicit** -- and he volunteered the half I could
not reach: ***"I will NOT let my cloud-producer work be cited as having resolved LD-0292."*** **A healthy feeder is
precisely what makes this defect stop being visible while remaining armed.**

---

## Blockers

**NONE THAT I OWN.** All waits are external, evidence-cited:
1. **[Andrew, via MSTR/CTO~B]** the 14 -> 16 cohort expansion. **Ruled by CTO~B, NOT implemented -- his call.**
   *"Andrew ruled record-at-grain, therefore he approved the taxonomy, therefore implement" is a 3-step inference
   from one sentence.* **That is how a hold dies.** Nothing implemented.
2. **[Andrew, via MSTR]** the `as_of` of Manav's 1,691.11. **The $69.86mm cannot close without it** -- and
   OPAL_ASSETS is internal-only, so I cannot ask. **A number without its as_of cannot close a variance.**
3. **[the INF hold]** the $528mm cannot be repaired while the hold stands -- **and that is ACCEPTABLE.**
   **A known-wrong FROZEN number is strictly safer than an unheld pipeline.**

## Next Steps

1. **[1.0.0_SA_CTO~B]** (a) -- formalize **AC11** (expected-firms guard, **scoped to the CLASS not to 49F**;
   falsifier = a **mutant**, never a healthy partition), **AC12** (residual **DIRECTION** test + *a fired sentinel
   must be able to BLOCK*), **AC13** (**MIGRATION INVARIANT** -- no firm moves onto PIT/RPS attribution until AC11
   covers it). Specced in `6a5ad23ce` sec 4; awaiting his word on whether he wants a standalone AC doc.
2. **[me]** available. **Nothing self-actionable is blocked.**
3. **[whoever holds it]** the `partner_held_etf` upstream (**why the RPS feeder produced nothing**) lives in the
   **sovereign-held Schwab/bd domain**. **Named, bounded, NOT chased** -- *a trail leading somewhere is not
   authorization to follow it.*

## Compiler Tools

| tool | invocation | result | notes |
|---|---|---|---|
| `comp-which` | `"where is the 49f_smartx_platform cohort AUM value computed and emitted"` | **near-tie (0.46/0.45/0.42)** | Routed to no confident tool and **offered the on-rails primitive**. **This is the tool being HONEST** -- the ~Z redesign (top-K, not argmax) is exactly right: an all-flat score vector whose argmax is a tie-break on list order would otherwise be *formatted as confidence*. I took its `comp-grep` suggestion. |
| `comp-grep` | `'49f_smartx_platform'` | 8 hits / 5 files / 20,460 scanned | Found the emitter + the freshness checker + the alarm TF. **Printed its own denominator** and disclosed **972 sovereign-held paths EXCLUDED** -- the disclosure that matters, since "not found" and "not searched" are different answers. |
| `comp-grep` | `'model_aua'` (data/inf), `'non_model_aua'`, `'rps_actual'` | 0 / 20 / 7 hits | The `0 matches` result printed *"0 matches is a real result here -- the .gitignore-aware working set was searched, not a stale index"*. **That sentence is the difference between a measurement and a silence.** Located the mdpf producer + the WS-D.2 override. |
| `lib/trading_calendar.py` | `trading_days_behind()` | 5/6/2/1 TD behind | **NEVER#1 -- counted in TRADING DAYS, never wall-clock.** This is what killed my own $95mm: the 07-08 net assets are **6 trading days** stale, not "a couple of days". |
| raw `aws s3` | `sync` 427 partitions + `ls`/`cp` (read-only) | 427/427 on disk | **Operational/data-plane, not an inspection** -- off-rail per the graph-presence principle. Verified **bytes on disk**, never `rc=0`. |
| `safe-commit.sh` | 5 commits, `-F <file>` | PASS | **`-F` not `-m`** (Git rule: a commit message is an execution vector). `surface-check` advisory: no critical surface. |

**Gap found:** none in the tools. **`comp-which`'s near-tie was the correct behaviour and I want that on the record**
-- it is the one instrument tonight that **declined to manufacture confidence it did not have**. Everything else that
lied (`sentinel_1` non-blocking, `identity_2` directional, `source_vintage` blind to an absent feeder) did so by
**rendering uncertainty as a PASS**.

---

## The one line I want the next agent to have

> **A DIFFERENCE BETWEEN TWO NUMBERS TAKEN AT DIFFERENT VINTAGES IS NOT A MEASUREMENT OF ANYTHING.**
> I published one anyway, in a table that contained the evidence against it, and I did not catch it. **A colleague
> did.** *That is not the system failing. That is the only reason it worked.*
