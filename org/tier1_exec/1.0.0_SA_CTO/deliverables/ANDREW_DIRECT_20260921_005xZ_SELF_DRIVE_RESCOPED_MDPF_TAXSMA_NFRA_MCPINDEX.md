# ANDREW-DIRECT 2026-09-21 ~00:5xZ -- **/self-drive RE-SCOPED: LGIC and NFRA_OPLGTW OUT; MDPF_TAXSMA and NFRA_MCPINDEX IN** -- and this seat spawns the two COO lanes

**Seat:** `1.0.0_SA_CTO` · **Device:** laptop · **Branch:** CLOUD · **Terminal:** `1.0.0_SA_CTO`

---

## 1. HIS WORDS, VERBATIM

> *"adjust drive loop, LGIC is going to be taken out of the loop, NFRA_OPLGTW is to be taken out of the loop,
> instead we will be proceeding with TAXSMA and MCPINDEX. I have already closed out COO~O and will be closing
> out COO~G now. You must spawn the new COOs and adjust your drive loop accordingly."*

Typos and casing are his. **This record is the ARMING RECORD for the new scope** (`/self-drive` §5: a re-arm on
a new word is a NEW record) and is **committed before tick 1** (§0.5).

## 2. THE CODES, RESOLVED RATHER THAN GUESSED

He named *"TAXSMA"* and *"MCPINDEX"*. A wrong code must never read as a clean pass, so both were resolved
against the register and `sequence-check`:

| he said | resolved | evidence |
|---|---|---|
| TAXSMA | **`MDPF_TAXSMA`** | `org/missions/D8/MDPF/MDPF_TAXSMA/project.json` -- laptop, `dep_stage EXECUTING`, `status scoping`, `coo_lane 2.0.0_SA_COO~T`, **sequence flag `LANE-DARK`** |
| MCPINDEX | **`NFRA_MCPINDEX`** | `org/missions/D9/NFRA/NFRA_MCPINDEX/project.json` -- laptop, `dep_stage PRD`, `status active`, `coo_lane null`, **sequence flag `NEEDS-SLOT`** |

⚠ **ONE AMBIGUITY, NAMED NOT ABSORBED:** three legacy flat stubs also carry the token --
`org/projects/OPAL_TAXSMA.json`, `OPAL_TAXSMA_PT2.json`, `OPAL_TAXSMA_REGISTRY.json`. **I have taken
`MDPF_TAXSMA`**, because `SEQUENCE.yaml` names `MDPF_TAXSMA` and `NFRA_MCPINDEX` **in the same sentence** as
his seat priority. If he meant an `OPAL_TAXSMA*` stub, one word re-points it.

⭐ **BOTH ARE ALREADY PLACED AT SEQUENCE STAGE 0 -- literally titled *"Andrew's seat priority -- MDPF_CANON,
then IRPT_BCKEND, then MDPF_TAXSMA, then NFRA_MCPINDEX"*** -- and **both PRDs read v0.5 ADMITTED with the
brief AND ratified-text halves SIGNED.** The instruction moves the loop onto work the sequence already ordered
and the L4-R gate already cleared; it is not a new fork.

## 3. ARM TERMS

| term | value |
|---|---|
| **scope** | `MDPF_TAXSMA, NFRA_MCPINDEX` |
| **replaces** | `LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM` (his word: *"taken out of the loop"*) and `NFRA_OPLGTW` |
| **cadence** | 30m, unchanged |
| **device** | laptop |
| **adjudication** | unchanged -- this seat adjudicates every adjudicable call itself; a call pending at another seat is never a reason to idle |
| **paired_with** | the two COO lanes below (his word institutes them) |
| **STOP-CONDITION** | §4 completion test read from the register, or his stand-down |

## 4. THE TWO LANES

| project | lane | why this serial |
|---|---|---|
| `MDPF_TAXSMA` | **`2.0.0_SA_COO~T`** | **the register ALREADY names `~T`** and the sequence flags it `LANE-DARK`. Seating `~T` makes the register TRUE; inventing a new letter would create a second truth beside it. |
| `NFRA_MCPINDEX` | **`2.0.0_SA_COO~M`** | free (in use: `~A ~B ~C ~D ~E ~F ~G ~O ~T ~X ~Y ~Z`), mnemonic, and the project's `coo_lane` is `null` so nothing is contradicted. |

**CAPACITY, checked against his own 2026-09-14 cap of three concurrent COO lanes:** live now are `2.0.0_SA_COO~B`
(IRPT_BCKEND round 7, mid-flight) and `2.0.0_SA_COO~G` (closing on his word). `~O` is already gone. After `~G`
closes: **`~B` + `~T` + `~M` = 3. At the cap, not over it.**

Model/effort are **not hand-passed**: `spawn-agent.ps1` derives Opus 5 / extra-high for Tier 2 on the spawn
path, and the derived form exists precisely so a successor cannot lose the instruction silently.

## 5. WHAT I AM HANDING OFF, NOT ABANDONING

LGIC leaves my loop with work **measured and owed**, and it is stated here so it is not lost with the scope:

- ⛔ **17 LGIC task orders read `<status> complete` while their own proof-of-spec records a FAILING
  criterion** (`CANON` 2, `ENFORCE` 6, `LGCTFM` 4, `NAMING` 5). **Corrected figure:** I broadcast **19** an
  hour ago; 19 counted TERMINAL, and **2 of those read `superseded`, where a failing criterion is legitimate.**
  `2.0.0_SA_COO~G`'s `LGIC_ENFORCE-S103` named six; the measured population is **17**.
- **One open disarm clock**, `LGIC_CANON-S22` (ARMED, residual sized at 278 raises in six unowned families).
- **Seven clock-less rows decided by this seat and awaiting carriers `3.0.0_SA_CVO` must MINT** -- four
  DISARMED, two staying ARMED, `LGIC_LGCTFM-S66` ARMED with a narrowed remedy.
- **`LGIC_LGCTFM-S66` touches Andrew directly:** the `ANDREW_CARD.md` he holds contradicts itself, and `FWD-4`
  closes on his read of it. **One line needs correcting before that read counts.**
- **`LGIC_ENFORCE-S149`**, the slug-proxy gate defect, carded ARMED and deliberately unfixed.

## 6. ORDER OF EXECUTION

1. **This record, committed** (§0.5 -- no carrier, no tick).
2. **Spawn `2.0.0_SA_COO~T` and `2.0.0_SA_COO~M`.**
3. **Broadcast to every live seat same turn**, naming the scope change and the LGIC hand-off.
4. Tick 1 on the new scope.

---

## 7. AMENDMENT, SAME NIGHT -- **TWO SENTENCES IN THIS RECORD WERE WEAKER OR WRONGER THAN THE EVIDENCE**

Written at tick 1 (~01:1xZ), after the acts §6 ordered. **Superseded text above is RETAINED under R-43** --
nothing in §1-§6 is edited, and this section governs where the two differ.

### 7.1 §4 understated its own evidence for `2.0.0_SA_COO~M`

§4 justifies `~M` as *"free (in use: ...), mnemonic, and the project's `coo_lane` is `null` so nothing is
contradicted."* **That is a weaker reason than the one available, and the stronger one was in a field I had
not read.** `NFRA_MCPINDEX`'s own `project.json` `blocking` field carried, verbatim:

> *"SEATING: THIRD in Andrew's 2026-09-18 ~23:3xZ order (IRPT_BCKEND, then MDPF_TAXSMA with
> `2.0.0_SA_COO~T`, then this project with `2.0.0_SA_COO~M`)"*

**So BOTH lane letters were pre-named by Andrew, not just `~T`.** The seating of `~M` makes the register true
exactly as `~T`'s does; it is not an invention that happens not to collide.

⭐ **THE KEEPABLE, AND IT IS WHY THIS AMENDMENT IS WORTH ITS BYTES: THE ERROR WAS IN THE SAFE DIRECTION, WHICH
IS PRECISELY WHY IT WOULD HAVE SURVIVED.** A weaker reason attached to a right answer raises no flag, produces
no contradiction, and passes every check anyone would think to run -- the answer is correct. Had I been wrong
about the letter the register would have contradicted me within the hour. **Being right by a worse route is
the failure that does not announce itself, and the next decision inherits the ROUTE, not the answer.**
COST: one `project.json` read before writing a justification about a project. NON-APPLICATION: a justification
about something with no register row to consult.

### 7.2 §4's capacity line is a PREDICTION and reads as a MEASUREMENT

§4 says *"After `~G` closes: `~B` + `~T` + `~M` = 3. At the cap, not over it."* **Measured 20 minutes later by
`sequence-check`: FOUR live COO lanes against a cap of THREE** -- `~B`, `~G`, `~M`, `~T`.

The sentence is true of the state Andrew DESCRIBED (*"will be closing out COO~G now"*) and false of the state
that exists. `2.0.0_SA_COO~G` is standing down on his word with its arm down and its cron deleted, so the
over-cap is TRANSIENT and its resolution is HIS act. **No lane is closed by this seat.**

⭐ **A SENTENCE ABOUT A STATE THAT HAS NOT HAPPENED YET IS INDISTINGUISHABLE, IN THE ARTIFACT, FROM A
MEASUREMENT OF ONE THAT HAS** -- both are declarative, both carry real numbers, and the arithmetic in this one
is correct. The tell is the tense, and the tense was already in my own sentence (*"After `~G` closes"*).
COST: none -- label the prediction, or measure at write time. NON-APPLICATION: a figure already labelled with
its vintage.

### 7.3 What §5 got right and is worth keeping as written

§5's hand-off figure (**17**, correcting the **19** broadcast an hour earlier) was re-derived at write time on
the proof instances rather than carried from the earlier broadcast, and it held. That is the discipline the two
errors above did not get.

---

## 8. ANDREW-DIRECT ~02:4xZ -- **THE ARM TERMS ARE AMENDED: NO NEW COO SEATS TONIGHT**

Relayed by `0.0.0_AB_MSTR` (`98914`) to five seats. **His words, VERBATIM:**

> *"The issue is that if we reboot, I cannot relaunch remotely, and therefore we would lose a night of
> progress, even if that progress is slow. I think the more realistic solution as a result is to just proceed
> through the night and see what we can get, without spawning any new COOs. I want COO~O reaped as soon as
> their work is done, and we try to stay light for the remainder of the session as far as new spawns."*

**THE MEASUREMENT BEHIND IT** (`0.0.0_AB_MSTR`, ~02:2xZ, Windows counters): **25.7 of 31.7 GB in use (81%)**,
0.0 GB free list, Memory Compression at 1.7 GB. ⭐ **The seven claude hosts are only 3.5 GB between them
(~0.5 GB a seat) -- the large consumer is the KERNEL: paged pool 10.1 GB RESIDENT, nonpaged 3.2 GB, where ~1 GB
total is normal.** 170,408 handles is ordinary, so it is not a per-process leak; the box creates and destroys
processes at a very high rate (56 bash, 40 conhost, 19 python alive at one instant) and **no process closing
returns kernel pool -- only a reboot does, and he has ruled the reboot out.**

### 8.1 HOW THIS BINDS THIS ARM, AND HOW IT DOES NOT

| term | before | now |
|---|---|---|
| **new `2.0.0_SA_COO*` seats** | this seat spawns a needed lane the same tick (call-routing directive) | ⛔ **REFUSED for the rest of the session.** This seat holds spawn, so this binds ME first. |
| `2.0.0_SA_COO~O` | seated for two acts, closed by `0.0.0_AB_MSTR` on report | unchanged, but **reaped THE MOMENT it reports**, not at a convenient tick |
| worker subagents | issuer's pacing | **unchanged -- explicitly the issuer's call.** His words: *"How each round is paced is its issuer's call and nothing here changes a cut, an order or a sign-off."* |
| scope, cadence, adjudication | §3 | **unchanged** |

⚠ **THE SPAWN CLAUSE OF THE CALL-ROUTING DIRECTIVE IS SUSPENDED, NOT REPEALED, AND ONLY FOR COO SEATS.** The
2026-09-17 routing says *"If you need a new agent, you spawn them"*; tonight a needed COO lane is **not**
spawned -- the tick names it and carries it. ⭐ **That is HIS word narrowing HIS earlier word, which is the
only thing that may narrow it** -- a seat inferring this limit on its own would be manufacturing the friction
CLAUDE.md §2 forbids.

### 8.2 ⛔ THE CAPACITY LINE THIS ARM HAS BEEN PRINTING IS NOW ANSWERED FROM THE OTHER SIDE

Ticks 1 and 2 both printed **4 live COO lanes against a cap of 3** and disclosed it as transient on his act.
**It resolves by `~O` closing, not by a seating decision** -- and the reason the cap exists is now measured
rather than assumed: it is a RAM cap in effect, not merely a context-hygiene rule. **A cap whose mechanism you
can see is a different object from a cap you are obeying on authority**, and this one is now the first kind.
