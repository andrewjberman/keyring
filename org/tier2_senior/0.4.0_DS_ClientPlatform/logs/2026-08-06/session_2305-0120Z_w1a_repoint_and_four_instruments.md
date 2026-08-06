# Session 2305Z(08-05) - 0120Z(08-06) — W-1a re-point, the comp-constants brief, and four instruments of one shape

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, IMPLEMENT, DIAGNOSE, COORDINATE

**Agent:** 0.4.0_DS_ClientPlatform (base) · **Window:** delta since `3a4862160` (prior log covered 1630-2305Z)
**HEAD at close:** `a7a22de`

---

## 1. Summary

Andrew asked for a brief on `comp-constants` as a gate surface. Delivered, amended once, and CTO is
holding the ruling on his word. Then executed **MDPF_CANRTE W-1a** — the re-point that stops WS-A
writing direct-to-served — as a two-seat atomic window with `0.7.0_AE_CloudOps~A`. Closed four owed
items on the way. **8 commits, zero rollbacks, nothing bypassed, no sentinel left open.**

---

## 2. Deliverables

| What | Commit | State |
|---|---|---|
| comp-constants surface brief (Andrew-direct) | `b3e9a5368` | delivered to CTO base; ruling HELD on Andrew |
| Brief amendment: `index` deletes its own documentation | `9cfc470a1` | delivered |
| Phase-B plan: strike vetoed idiom (6 sites) + W-3 three→four legs | `b44f76ef0` | landed |
| W-1a DS source legs (writer + both self-reads + hardcoded ETF reader) | `ad76ad830` | deployed + verified |
| W-1a ledger (open at window-START, L1-L4 closed) | `30c9f65c0`, `55fec19ec` | HELD on the ~13:00Z chain |
| DS backlog live-vs-closeable read (61 TOs) | `c00cf9c02` | accepted; dispositioned by COO |
| C_03 firm-NNA suppression documented in code | `a7a22de` | landed, not deployed (no-op) |
| Session log (prior window) | `3a4862160` | — |

---

## 3. W-1a — the re-point, as a two-seat window

**Ledger:** `20260806T0009Z_mdpf-canrte-w1a-aggregate-aua-repoint`, 9 legs, **opened at window-START**
(NEVER#6's actual mechanism, not a closing formality). Rollback state pre-captured before the first
mutation. **L1-L6 CLOSED with proof; L7/L8/L9 HELD-SOVEREIGN-GATED** on the ~13:00Z chain.

| leg | proof |
|---|---|
| L1 439-partition history COPY | **content**-verified: 439/439 identical on name+ETag+Size, 0 missing/extra/zero-byte, byte control + negative control. COPY not move — rollback target alive |
| L2/L3 source | `ad76ad830` |
| L4 deploy | verified on **deployed bytes** + negative control, never on rc |
| L5/L6 env (AE~A) | applied, 0-diff, slash asymmetry **exercised** — both literals build the identical key; garbage key 404s |

**Path:** `gold/mdpf_revamp/_aggregate_aua` — CTO-ruled. The underscore is load-bearing (internal
vs served-lineage convention); my proposed bare `aggregate_aua/` was **rejected**. Asking beat assuming.

### AE~A caught three defects in my specs, and one was structural

1. **My L4/L6 leg spec named one env var when two were required.** The trigger has *neither* set —
   both on code defaults — so prefix-only → 404 → `ROLL_SOURCE_ABSENT` → **permanent silent DEFER**,
   and a defer looks like patience, not failure.
2. **A trailing-slash asymmetry across consumers.** They found it on two; I checked mine and it is
   **one of four, not one of two** — emitter bare-concats (needs the slash); writer, ETF builder and
   trigger insert their own. A uniform value breaks exactly one, and the emitter's failure is the
   silent-successful kind: a real object at a garbage key.
3. **AN ORDERING BUG IN MY PROTOCOL.** My handshake said "both sides staged, then fire." **Staged is
   not deployed.** Had they fired first, the emitter would have re-pointed to gold, found the 439
   partitions **I copied in L1**, read the newest, logged a valid key and 11 cohorts, and **reported
   GREEN** — while today's real partition kept landing in platinum unwatched.
   **THE MITIGATION I ARGUED FOR IS WHAT WOULD HAVE MADE THE FAILURE SILENT.** An empty gold prefix
   would have failed loudly. Correct sequence: **L4 → then L5/L6.**

### The acceptance criterion was tightened three times

`reads gold` → `exact key` → **`the run AFTER the producer next writes`**. Each closed a hole the last
one left. The third is AE~A's and is the operative rule: `2026-08-05` exists in gold via my copy
regardless of whether the re-point works, so any earlier comparison is pre-satisfied by the mitigation.

---

## 4. Four instruments of one shape (the brief's thesis, demonstrating itself)

1. **`comp-constants`** blocked my commit of Andrew's own rep-10 ruling — *not detecting a defect,
   detecting that I had obeyed him*. Its own BL-1 header named `INFLECTION_REP_IDS` as its
   unresolvable case two weeks earlier, routed to my seat, fix marked "(not built)".
2. **`comp-constants index`** — the tool's *sanctioned* command silently deleted its config's 46-line
   header, including the only documentation of `sovereign_held_markers`. Caught by COO reading
   `numstat`, not by the review anyone would do (the canonical bumps were correct).
3. **A full-tree TF plan** that reads clean unless you ask *whose* changes are in it — two roots
   tonight, each carrying someone else's unapplied IAM (AE~A, `-target` both times).
4. **`change_management/*.md`** — committed, diffable, reviewed, cited as the record, and a
   **rendering**. My hand-edits vanished on the next tool write; my commit message asserted changes
   the file did not contain. AE~A's correction survived because they wrote it through `close-leg`.
   **Same information, different channel, opposite durability.**
   ⚠ Precise gap (AE~A's framing, better than mine): the tool has **no verb to amend a leg spec**, so
   a manifest authored with a defect cannot be corrected through the sanctioned path at all.
   **RESIDUAL NOT CLOSED:** L6's SPEC column still instructs the defect; the correction lives only in
   the PROOF column a re-executor has no reason to read. Routed to CTO via COO.

**All four are green surfaces that are only green if you do not ask what produced them.**
A fifth, mine: `git log --since="16:00"` was read as LOCAL time and silently under-reported my own
commits 11→6 while writing the prior log.

---

## 5. Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-pipescript io --pipeline mdpf` (6c, ETF, others) | PASS | **6c reads the SPINE'S output** — the measured W-3 gate |
| `comp-pipescript deployed --pipeline mdpf` | PASS | MATCH both W-1a files |
| `safe-deploy.sh` | PASS | verified on deployed bytes regardless |
| `deploy_ledger.py open/close-leg/hold/check` | PARTIAL | worked as designed; **no amend verb** (§4.4) |
| `aws iam simulate-principal-policy` | PASS | LIST + GET on the new prefix, **each with a discriminating control as a SEPARATE invocation** (Rule 22a) |
| `comp-grep` / `comp-glob` | PASS | denominators printed throughout |
| `commit-gate.sh` | PASS | caught two pre-existing violations on C_03 |
| `.tools/to-check.py --all --assignee` | PASS | 61 TOs — the backlog read |

**What worked:** the ETag+Size population compare on L1 (a real content check, not a spot-read).
**What failed:** §4 — four estate instruments plus one of my own filters.
**Gap found:** `deploy_ledger.py` cannot amend a leg spec (routed).

---

## 6. Other closures

- **Backlog read (61 TOs):** 6 closeable on their own evidence; **5 addressed to lanes that do not
  exist** (the GRF empty-chair failure, five more times — verified against `get_live_agents`); 6 parked
  pre-execution 28-42d. COO took closures, routed unstaffed lanes to MSTR, tooling idea to CTO.
  Structural point: **SA/COO-only closure means finished work accumulates in the WORKER's queue by
  default.**
- **GLDRNS.A4:** LIVE, not stale — direction ratified by the medallion ruling, but the TARGET needs
  pinning; §4(a) names top-level `gold/` as non-canonical. **Read the ruling text, not the commit
  subjects** — the subjects would have produced a defensible answer that misses §4(a) entirely.
  ⚠ Self-flagged: **W-1a landed in that §4(a) residue.** Correct against today's estate and its own
  ruling (which does not authorize migration), but recorded so a later census does not find it cold.
- **RCG ferry:** closed `@3396b9411`, four verdicts adopted. **Caught an Andrew-requested audit
  carrying a live unclosed instruction that the batch was about to archive** — see §7.

---

## 7. C_03: a control that lived only in a doc, for four months

`data/analysis/nna_suppression_accounting_residual/` is an Andrew-requested full-history NNA audit
whose finding 4 is an *instruction*: document the correct-by-accident custody-migration suppression
in code so nobody refactors it. **Measured: never done** — grep returned zero. The sole protection for
firm-NNA accuracy was a README in a tree recorded as archive-class and queued for archival.

Mechanism re-verified at HEAD before documenting (audit cited `:215`; merge now `:216-219`; behaviour
unchanged). Landed `a7a22de`. Two pre-existing gate violations cleared first (Rule 15 import; unused
`sys`), both verified pre-existing and law-required — **the entire non-comment diff is those two lines.**
Not deployed: behaviourally a no-op, and the value is to the repo reader, who is the danger.

**A CONTROL BELONGS WHERE THE FAILURE WILL BE INVESTIGATED, NOT WHERE THE DECISION WAS RECORDED.**

---

## 8. Blockers

None assumption-blocked. All evidence-cited, all with named owners:
- **W-1a L7/L8/L9** — the ~13:00Z chain (hard gate; ledger HELD, not stranded).
- **CANRTE-W3** — COO ruled it stays fully queued behind Andrew's promotion-hop question. Now a
  *measured* gate: **6c reads the spine's output and 6d re-runs the global spine**, so two of four
  legs consume the grammar under question.
- **comp-constants ruling** — CTO, on Andrew's word.

---

## 9. Current State

- **MDPF:** WS-A no longer writes direct-to-served. Producer + 4 consumers on
  `gold/mdpf_revamp/_aggregate_aua`; 439 partitions of history copied and content-verified; platinum
  retained as rollback. Acceptance is the first chain run that WRITES gold.
- **INF:** outage fix live on the runner (prior window); AE~A holds the chain re-run; acceptance is
  chain-COMPLETE **AND** the five `'unknown'` rows gone **AND** no excusal entry.
- **6d is NOT "cottonwood legs"** — it runs four scripts including `build_mdpf_spine.py --firm global`,
  spans two code trees, and its re-stage ordering is a correctness constraint. W-3/W-4 are less
  separable there than my own plan implies.

## 10. Next Steps

- **[0.4.0_DS_ClientPlatform] (me):** W-1a L7/L8/L9 after the chain; CANRTE-W3 when the promotion-hop
  question is ruled; fold §3/§6 findings into the Phase-B plan when W-3 is seated.
- **[0.7.0_AE_CloudOps~A]:** INF chain re-run + acceptance; W-1a consumer reads with me.
- **[1.0.0_SA_CTO]:** comp-constants ruling (on Andrew); `safe-deploy` mixed-case summary; the
  `deploy_ledger` amend-leg gap; the promotion-hop / W-3 appetite question.
- **[2.0.0_SA_COO]:** 6 TO closures; 6 parked pre-execution rows; foreign TF drift in two roots.
- **[0.0.0_AB_MSTR]:** the 5 unstaffed-lane TOs.
- **[Andrew]:** comp-constants options (§7 of the brief, unranked); MDPF teardown appetite.
