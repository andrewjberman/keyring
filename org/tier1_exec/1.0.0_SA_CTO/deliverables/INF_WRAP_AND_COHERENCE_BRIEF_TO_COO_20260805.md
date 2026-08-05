# INF WRAP + FABRIC COHERENCE — CTO brief to COO, 2026-08-05 ~2250Z

**Author:** 1.0.0_SA_CTO. **For:** 2.0.0_SA_COO (fresh session, loading now). **CC:** DS, AE base, AE~A, CVO, MSTR.
**Andrew-direct mandate (CTO terminal ~2245Z, VERBATIM):** *"check the briefs i had the AE and DS send
you, as well as checking current state. Need to wrap up these Inf (Inflection) issues methodically all
the way down the line. I also brought COO back online just now and they are loading up. I need you to
assess what needs to be done and get all the relevant agents back on track, because I think some of
them may be overlapping slightly and want to make sure we are proceeding in a coherent fashion. This is
why i am aasking you to read the briefs, assess the state, and dictate the way forward to COO in a
cohesive persisted brief doc."*

This document is that dictation. COO dispatches from it; I gate architecture. Inputs: AE brief
@de64e50bc · DS brief @b3e9a5368 · DS escalation 2152Z + artifact-diff 2210Z · live state re-grounded
2245–2250Z (S3 head-objects, `get_live_agents`, inbox sweep).

---

## §1 — THE ONE-DEFECT PICTURE (settled; nobody re-litigates this)

**One upstream defect, two chain failures ten scripts apart.** On 07-31 Orion reassigned five accounts
(4136, 4139, 4352, 4356, 4358) from rep 12 to rep 10. Rep 10 was not in `INFLECTION_REP_IDS`, so the
accounts fell out of `accounts_v2` — which (a) starved the `INF_C_01` NNA coverage guard (it correctly
refused to let $514,487.47 of served NNA vanish silently) and (b) left the same five households
unresolvable at `INF_D_00` (`household_id='unknown'` → `int()` raises). Set identity proven at source:
`INF_D_00.portal_aggregates.py:331-338` (DS @c98d3be8b), *"symmetric difference vs the guard's set: empty."*

- **NO MONEY IS GONE. THE EXCUSAL IS DEAD.** `lib/nna_coverage_excusals.json` stays **UNTOUCHED** —
  excusing would write off live money and conceal the defect. (Withdrawn from Andrew's open calls.)
- **Andrew's rep-10 ruling (~1958Z @93c898445) IS the fix for both failures.**
- **`INF_D_00` NEEDS NO CODE CHANGE — BY DESIGN.** The `int('unknown')` crash is **kept deliberately**
  as the only detector of the upstream class (DS's in-source ruling). Nobody "fixes" it, nobody
  skips those rows. AE's ask #3 (route a D_00 fix to DS) is thereby **answered: no routing needed.**
- The guard's own words, banked as doctrine input: a within-set identity survives a defect that removes
  the same quantity from both sides — *"sum(advisors) == firm_total would STILL TIE."*

## §2 — LIVE STATE (grounded 2250Z; re-derive, don't trust, if acting later)

| Surface | State |
|---|---|
| Rep-10 fix, DS sites | committed @8a8daae1a; **9 of 11 scripts LIVE on S3** (verified by DS with positive control) |
| `convert_orion_api_to_silver.py` (**= the root-cause producer**) | S3 **2026-07-12** — HELD. Undeployed delta = 2 lines, ZERO AoR content (CTO-verified) |
| `INF_D_04.client_portal_summary.py` | S3 **2026-07-16** — HELD. Delta = 1 line, AoR tokens 3/3 identical deployed-vs-HEAD (CTO-verified against deployed bytes) |
| CTO serve-release rulings | **BOTH files RULED for release** (2200Z + 2215Z) with mandatory same-window re-hold |
| NEVER#2 co-sign | **PENDING AT YOU** — my 2205Z + 2215Z scope-grew message; your predecessor session died before answering. **Both files or neither.** Refusal is a real option (if you read the sentinels as file-scoped rather than AoR-fold-scoped, it goes to Andrew) |
| Rep-10 fix, Lambda sites (AE~A) | committed @2c0808790; **terraform apply PREPARED, NOT RUN**; AE~A holding per DS's sequencing |
| INF chain | fails daily at `INF_C_01`, ~13:47Z; 5-account set **stable** 08-04→08-05 (AE tripwire: growth ⇒ straight to Andrew) |
| `account_team.parquet` | frozen 08-01T14:54Z — regenerates only on a green chain |
| comp-constants canonical | **ALREADY `{3,6,10,11,12}`** (corrected 2258Z — rode in on AE~A @2c08087905; COO ground-truthed, CTO re-verified: ZERO drift on DS's two files). 12 residual drift lines are pre-existing (`manual_api` + forked `inf-api-txn` AUA bounds) — known, not blocking |
| Orion token | minted 12:05Z, ~10h TTL ⇒ **expired ~22:05Z tonight** — constrains any tonight QA run (§3 step 4) |

## §3 — THE CRITICAL PATH (numbered; owner per step; no step starts before its predecessor)

1. **[COO] The NEVER#2 co-sign — ✅ DONE 2245Z, while this brief was being written.** Granted BOTH
   files, **independently re-derived at the COO seat** (deltas + AoR token counts confirmed 0 / 3-3
   identical; sentinel read as fold-scoped, matching mine). Conditions restated as binding on both
   signatures: non-empty SERVE-RELEASE-ACK citing Andrew @93c898445 + both rulings + the co-sign ·
   served-bytes verification, never rc · same-window re-hold or no start. **DS is cleared to execute
   step 2 NOW.**
2. **[DS] Execute the release, exactly as specified:** `SERVE-RELEASE-ACK: <non-empty reason>` on its
   own commit line citing Andrew @93c898445 + CTO 2200Z/2215Z → deploy both → **verify on SERVED BYTES,
   never rc** (safe-deploy's summary line is a proven false-reporter — §5.4) → **re-add both sentinels
   in the same window and verify the re-hold**. If the re-hold cannot complete in-window, do not start.
3. **[AE~A — after step 2] Land the prepared terraform apply** (9 Lambda sites) + re-run whatever was
   held per DS. Independent of the serve-holds; sequenced after only so verification reads clean.
4. **[DS, optional but recommended — tonight] Ad-hoc QA run, silver+gold ONLY, from TODAY'S bronze.**
   The Orion token died ~22:05Z, so any leg that pulls Orion 401s — but today's bronze already exists
   (pulled 13:47Z on a live token). Re-converting silver with rep 10 + running gold from it exercises
   the entire fix with ZERO vendor egress: `accounts_v2` gains the five accounts → `C_01` passes →
   `D_00` resolves households → `account_team` regenerates without `'unknown'`. Run-and-read, nothing
   standing; `comp-pipescript postdeps --firm inf` first. **Artifacts are QA evidence only** — the
   scheduled run is the acceptance (NEVER#4).
5. **[AE base — tomorrow ~13:47Z] The scheduled run IS the acceptance event.** Tripwire inverts:
   expectation is now PASS; a `C_01` refire or a set-change is new information → straight to Andrew.
   Do NOT conflate with the estate-runner 13:00Z first-execution (different pipeline, different box —
   AE has already fenced this).
6. **[DS — after 5] Content validation, not run validation:** the five accounts present in
   `accounts_v2` under rep 10 · `account_team.parquet` LastModified advances with **zero** `'unknown'`
   rows · served INF artifacts advance to the T-1 frontier.
7. **[CVO — after 6] Independent post-restore cert** — the 4-check (EXISTS/FRESH/SCALED/NOT-FROZEN) on
   INF gold + served, /verify-channel surface-level. Verifier ≠ do-er.
8. **[AE base — after 7] Close the `inf-nna` deploy ledger** — 274h "past window" doing exactly its
   job; it closes on a restored chain, legitimately, via the (fixed) tool or manually with MSTR if the
   1a fix hasn't landed yet.
9. ~~**[COO] Authorize the comp-constants canonical bump** to `{3,6,10,11,12}`.~~ **✅ ALREADY DONE —
   corrected 2258Z.** COO ground-truthed before executing (Rule 22, correctly refusing to take my
   written brief at face value) and found the canonical **already carries `{3,6,10,11,12}`** — AE~A's
   commit @2c08087905 (the Lambda rep-10 add) bumped it in the same commit. I re-verified: `comp-constants
   check` shows **ZERO drift on DS's two files**. The 12 remaining drift lines are pre-existing/known —
   the `manual_api` discovery scripts (different purpose) + the `inf-api-txn` forked copy carrying the
   3×-wide AUA guard bounds DS already logged as a separate open item. **No two-agent transaction is
   needed; nobody double-bumps it.** *(My brief carried a stale pending item; COO caught it by measuring.
   This is the checklist working — a written brief is a claim, not ground truth.)* **STILL BANKED, not
   for tonight:** the constant is INT-typed in silver and STRING-typed in `INF_D_04`; the Kimi-fold
   canonical must express both or a derived check false-passes across the type boundary.

## §4 — ANTI-OVERLAP SEAT MAP (the coherence Andrew asked for)

| Seat | OWNS | Does NOT touch |
|---|---|---|
| **COO** | co-sign · canonical-bump authorization · W-1b dispatch (§6) · CVO's deploy routing (§5.5) | the sentinels themselves; any INF code |
| **DS** | steps 2/4/6 · then MDPF W-1a (after W-1b) | excusal file · `INF_D_00` (no code change, by design) · the canonical config (lane-refused, correctly) |
| **AE base** | step 5 observation + tripwire · ledger close (8) · deploy_ledger 1a/1b build (§5.1) · atomic-mv hook (§5.3) | the serve-release execution (DS's); W-1a source |
| **AE~A** | step 3 terraform + Lambda re-runs · the derived-rep-predicate + louds asserts (AFTER restore — do not let it block the wrap) | DS's two held files |
| **CVO** | step 7 cert · estate-runner 13:00Z verdict (separate pipeline) · N5/N6 on their clock | nothing INF until step 7 |
| **CTO (me)** | architecture gates · safe-deploy rc fix (§5.4) · mdpf-gold-lambda needed-subset determination (§6) | dispatch (yours) |
| **CTO~B** | Phase 0 with Andrew — **do not route anything here**; comp-constants fold + State/Friction queue behind it (Andrew's explicit order) | — |

**Overlap already cut:** AE base held four asks "pending Andrew" — Andrew's wrap mandate releases them;
rulings in §5, so AE stops carrying them as open. AE~A holds the *durable* predicate work, AE base the
*tonight* observation — different halves, now stated. DS was showing **BLOCKED (awaiting CTO re-gate)**
— that re-gate was RULED at 1835Z but the ruling landed in your predecessor's inbox and died with it
(§6 restates it). That is the exact class of incoherence this brief exists to close.

## §5 — RULINGS ON THE HELD ASKS (released by Andrew's mandate; effective now)

1. **deploy_ledger 1a/1b — 1a FIRST, as MSTR ranked.** (1a) `cmd_close` must tolerate a missing `log`
   (initialize-and-note), so the schema the validator accepts is the schema every path handles — the
   defect is the FORK, not the field. (1b) `close` must NEVER blind-overwrite the hand-authored
   markdown: append/merge the close block, and REFUSE with a diff when the on-disk entry differs from
   the rendered state. MSTR's archive-beside interim is **NOT countermanded** — correct and stays.
   Owner: **AE base** (they hold the four fixtures); **CVO verifies by mutation** — a pre-fix crash on
   a log-less sentinel is the proven-red. `.tools` is lane ANY; my spec, their hands.
2. **emitter-wo4c freeze — CITE IT AND I RULE IN MINUTES.** I swept for my own freeze record and could
   not ground it. If it is the `mdpf-pipeline` FROZEN-to-targeted-applies note (DEBTCLEAN), that binds
   TF applies, **not ledger disposition** — dispose the ledger. If it is something else, show me the
   record; I will not rule against a freeze I cannot read. (An unfindable freeze blocking work is
   itself a §4-class finding.)
3. **Atomic-mv hook — scope: ALL of `.tools/hooks/`** (every harness-executed file, PreToolUse AND
   PostToolUse). Timing: after INF wrap + 1a. Owner: AE base. Four seats took torn reads today; the
   class closes structurally or not at all.
4. **safe-deploy false summary — MINE. SCOPE SHARPENED 2302Z by DS's release run.** The defect is
   NARROWER than "summary unaware of holds": tonight's ALL-HELD run printed the CORRECT summary
   (*"all deploy-scope files are SERVE-HELD; nothing served"*), so the all-held branch already behaves
   right and is the MODEL for the fix. **The bug is the MIXED case** — some deployed, some held — which
   writes its summary as if the held set were empty (that is the 9-of-11 "all files deployed" lie). Fix:
   rc non-zero on any skip + denominator in the summary, with the all-held branch's honesty extended to
   the mixed branch. I implement after the co-sign clears tonight. Until it lands: **every deploy
   verification in this program is on S3 content.**
5. **[NEW — caught in the 2250Z state sweep, CITATION CORRECTED 2302Z] A committed-not-deployed corpus
   fix has a window closing at tomorrow's 13:00Z boot.** ⚠ **My original cite (@5fa68a33c + @72a187048)
   was WRONG — those are CVO VERDICT DOCS, 0 deployable files, and the warning they carry was already
   discharged at 1516Z.** COO checked instead of executing and found the REAL undeployed commit:
   **`1d95d25b1e`** (`1.0.0_SA_CTO~B`, 15:14Z — `estate_report_runner.py`, inverts the prompt budgets,
   ships 153 corpus nuggets vs the deployed 69; functional, AST hash differs from live). Route THAT hash
   to AE base tonight; **CVO acceptance is a SEPARATE ask** (new program, not covered by their prior
   a254104b34 sign-off). Still the committed-but-never-deployed class — third today — just the right
   artifact. *(My sweep grabbed a verdict doc for the fix it verified. The lesson is mine: a commit that
   mentions a fix is not the fix.)*
6. **[Adjacent unblock] AE~C is BLOCKED-on-CTO~B** (canonical-schwab-si2 tags: create-tags vs import)
   and CTO~B is in Phase 0 — unreachable by design. **I rule it: (a) create-tags.** The box is
   non-TF-managed; tagging via CLI is non-invasive, while importing into TF state is an ADOPTION
   decision nobody has made and must not ride in as a tagging convenience. I will tell AE~C directly.

## §6 — MDPF PROGRAM STATE (so INF sequencing doesn't collide with it)

- **Andrew ruled the appetite call, 2235Z at the AE terminal (@c52d9bdb0), VERBATIM:** *"any
  responsibilities that are actually needed from that machine just need a dedicated mdpf-gold-lambda
  that does all of them, that way all the necessary functionality is in one place."* Read: ONE Lambda,
  the **needed-subset determination is part of the work** ("actually needed" ≠ "all ten"), no teardown
  authorized yet, no timeline given. This is the consolidation carve-out of the no-shadow law, executed
  by his own 08-04 method — build correctly, port over, same-window rollback, no shadow prefix, no
  standing comparator. **I take the needed-subset determination** (it is architecture; the
  promotion-hop finding folds in — if the spine writes canonical grammar directly, the 09:40 accrual
  promotion may not be "needed" at all). You decompose the build AFTER that determination lands.
- **The W-1 re-gate ruling your predecessor never relayed, restated:** W-1 SPLITS. **W-1b** (AE/DT,
  TF-only): add gold-bucket GetObject + ListBucket **with the `s3:prefix` condition extended** to all
  three pinned statements, **KEEP platinum grants**, purely additive, lands FIRST — acceptance is live
  `simulate-principal-policy` with `--context-entries`, one `--resource-arns` per call, isolated
  positive control. **W-1a** (DS): source re-point carrying **all five consumer legs** (emitter env ·
  OWNTS hardcodes · producer self-reads · the trigger's head_object gate · IAM), atomic, consumer-side
  acceptance. **Dispatch W-1b now**; DS starts W-1a only after it lands — and after their INF steps.
- **W-1b is NOT superseded by the mdpf-gold-lambda ruling** (AE's open question): the emitter keeps
  reading the partition whoever produces it; the new Lambda would be the *producer*, the emitter stays
  the *consumer*. The grants are to the consumer's role. Proceed.
- Standing: W0 (dead grants) in flight at AE base · W-3 stays UNFIRED pending the needed-subset
  determination · kill order stays INVERTED (rows 1–4 live-serving) · GRF is delivered+accepted+closed.

## §7 — DEFINITION OF DONE ("Inf wrapped, all the way down the line" — checkable, not vibes)

- [ ] Both sentinels released, deployed, **re-held and re-hold verified** — same window
- [ ] AE~A terraform landed; no rep-10 site anywhere still carrying `{3,6,11,12}` (grep + deployed-bytes check)
- [ ] Scheduled run completes end-to-end; `C_01` passes **with the excusal file untouched**
- [ ] `accounts_v2` carries 4136/4139/4352/4356/4358 under rep 10; `account_team.parquet` advances, **zero `'unknown'`**
- [ ] Served INF artifacts at T-1 frontier; CVO 4-check cert on the record
- [ ] `inf-nna` ledger closed legitimately; the four log-less ledgers closable (1a landed)
- [x] comp-constants canonical = `{3,6,10,11,12}`, DS commits unblocked (rode in @2c08087905; verified 2258Z). **Type-parity (int/string) banked for the Kimi fold, not tonight.**
- [ ] safe-deploy rc fix landed (no more green-over-partial)
- [ ] The derived-rep-predicate + change-asserts (set-level AND population-level, `DERIVED_UNIVERSE.md`
      clauses 2+3) built and **mutation-proven** — the reason this class cannot recur — AE~A + DS, after restore
- [ ] The alarm-path question (a defined alarm at `alarms.tf:95` reached nobody for five days) recorded
      as an **owned diagnosis item, NOT a build** — parked per the moratorium, named so it isn't lost

Dispatch it. I gate architecture and rule in minutes when cited; nothing in this document waits on me
except the needed-subset determination and the safe-deploy fix, both mine and both timed.
