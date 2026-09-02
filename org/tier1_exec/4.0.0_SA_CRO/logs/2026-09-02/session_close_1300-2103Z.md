# 4.0.0_SA_CRO — Session Close 1300–2103Z — a decomposition, an adversarial audit, a doc refactor, and Andrew's Azure/LDT thread

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, EXPLORE, SCRIBE, IMPLEMENT

**Serial:** 4.0.0_SA_CRO (base, no lane) · **Session:** registered 2026-09-02T13:0xZ, PID 84156
**Window:** 2026-09-02T13:00Z → 21:03Z · **Commits (mine): 2** · **MCP: 1 in / 1 out** · **Deploys: 0**
**Azure changes (external to this repo): 2** — an Owner grant and a budget consolidation.

---

## What happened

Startup, then four distinct pieces of work: an ad-hoc `/atom-decomp`, an adversarial audit for
`1.0.0_SA_CTO~A`, an Andrew-direct refactor of `org/XXX.md`, and Andrew's live Azure/Little Dog Tech
thread.

### 1. Startup (13:00–13:05Z)
`/watcher` + `org/XXX.md` Step 1b. Registration read **NOT REGISTERED** (not stale) and no
`inbox-watch.sh` process existed for this serial — a genuinely fresh session, so no orphan/live-peer
ambiguity arose and no kill was needed. Armed Monitor `bf85ke7r5`; banner `parent-tied: pid 597661`.
Probes: **A.2** 5 findings, all in the documented known set (3 NON-APPEND-EDIT all shrinking → the
direction test passes; 0 ERROR-FAILCLOSED; 2 owned-until-`rv0057-f001`). **A.3** `106 of 106` resolve
bare AND the mandatory EXERCISE line passed. **B.0** 7/7 READ, all stamped by my own serial.
**B.1** 0 active TOs (`scanned=2235`).

### 2. `/atom-decomp` on "comp-recon" (13:05–16:45Z) — commit `b1f37d5067`

**The subject Andrew named does not exist.** `comp-recon` is absent from `.tools/` (106 comp-* files),
absent from `--corpus all` over 144,645 files (4 hits, every one a substring of
"comp-**recon**ciliation" in prose), never added or deleted on any branch (git probe run **with a
positive control** on `comp-blast`, which returned 3 commits), and `comp-which` said in its own words
that the catalog does not cover it.

It RESOLVES to `comp-passcraft recon` — `.tools/comp-passcraft:2` self-describes as *"the
recon-scaffolding SDK"* and exposes that literal verb. Andrew's standing alternative (that CTO used
"recon" as a verb over an amalgamation) was therefore **not needed**; a literal referent exists.

DRY rectangle: 6 entities × 9 fields = **54 cells, 54/54 MEASURED**, MC1 rectangularity PASS.
**UNCERTIFIED deliberately** — Rule 14(e) requires certifier ≠ author, so no sealed mutant was planted
and `rectangle.final.certified.json` is absent.

The three axes Andrew asked for, kept separate: **universe** = unbounded, one target per invocation,
never enumerated (0 enumeration primitives across 802 lines; the 3 "glob" hits are `globals()`);
**derivation** = none, no universe object exists, only an 8-key hand-maintained annotation dict
(6 of 106 tools on disk, 6 of the 63-member AC-0 universe); **cadence** = NONE / demand-driven,
0 scheduler references across 457 hits. Six findings routed, four independent remedies.

### 3. Adversarial audit of `NFRA_CLDGRPH` for `1.0.0_SA_CTO~A` (18:5x–20:0xZ) — NOT COMMITTED

Andrew handed me CTO~A's audit handoff. Verdicts: **claim 1 BREACHED** (`resource_summaries_store.py`
appends to Iceberg with **zero** `stamp_marker` references over 384 lines — positive control returns 4
on `derive_runner`; the handoff listed it AS a stamper). Bounded today: neither projection file
ingests that table. **Claims 2 and 3 SURVIVE** — I traced the flag-gated chain CTO~A declared untraced
and it folds into the same in-memory graph, no second Nessie path.

**The headline was not any single claim but what three of them share.** The marker is not just the
trigger, it is the **data pin** (`kuzu_incremental_refresh.py:78` `StaticTable.from_metadata(nodes_loc)`
off the marker). The live marker was **rewritten today at 12:58:03Z carrying `committed_at_iso`
2026-08-06** — 27 days stale — which no `stamp_marker` write can produce. CAS is dormant by default
and **unset on the deployed Lambda (applied plane)**, so the archive path is unreachable and the
estate cannot distinguish a stale-bytes re-put from a real write of stale data.

⛔ **I could NOT test claim 5, and said so.** My `filter-log-events --filter-pattern` calls returned 0
for `MARKER_STAMPED` **and for `BATCH_END`, a token I had just seen in the same log group.** Positive
control FAILED → the instrument is dead and every one of those zeros is non-observation. I nearly
published them as a falsification.

### 4. `org/XXX.md` refactor (Andrew-direct, ~15:5x–16:01Z) — commit `4559e6fd4c`

Andrew, VERBATIM: *"This file has blown up, it looks like a bunch of bullshit and revisions between
lines 305 and 473 ... This is not a message board to post random shit that is happening in a session
it should be an operational doc for startup rules, like a more expanded claude.md for operating
procedures."*

Measured first: **Step 1b alone was 497 of 834 lines = 60% of the document**; every other section
scored 0–5% on dated/attributive/narrative markers. The rot was LOCALIZED. Result **834 → 596**
(−238, −29%); Step 1b **497 → 260**; flagged lines **55 → 15**; attribution lines **8 → 0**.
Nothing deleted — 278 lines preserved verbatim with original line ranges in
`docs/references/XXX_STARTUP_HISTORY.md`. 21/21 mechanism-retention check.
**F loop-arming table preserved BYTE-FOR-BYTE** (live Andrew-ratified arm authorizations, not a
formatting refactor's business); splice asserted the F and Step-2 boundaries before writing.
Found in passing: a **real corruption** — a paragraph had been inserted mid-sentence
("would make healthy watchers" … 5 unrelated lines … "suicide)").

### 5. Andrew's Azure / Little Dog Tech thread (20:0x–21:0xZ) — EXTERNAL, no repo commit

Read the Teams thread with AJ Graff and LDT support ticket **#41324** (Paul Schwegler, Purview DLP +
message encryption). Answered Paul's four Azure preconditions from LIVE measurement: subscription IS
in Opal's tenant (`homeTenantId == tenantId`, opalinvest.com); it IS PayAsYouGo not trial
(`quotaId PayAsYouGo_2014-09-01`, spendingLimit Off); `rg-opal-purview-billing` exists.

**Owner grant:** the agent's `az role assignment create` was **blocked by the permission classifier**
and I did not route around it — correct gate for an Owner grant to an MSP. Andrew ran it himself.
Verified by an INDEPENDENT `az role assignment list` read, not the create call's own output:
`LDTAdmin@opalinvest.com` (Little Dog Tech, `cc09bb0b-ee8c-43c0-a000-1eaf9357008a`) now holds Owner
alongside Andrew.

**Budget consolidation (Andrew-direct "fix that now"):** found TWO budgets. His instruction named
"the $100/mo one" — **there was no $100/month budget**: `Monthly_Budget` was $100 at **Annually**
grain with a single 100% alert. Executing literally would have left him WEAKER than before, so I
rebuilt rather than merely deleted. Azure refused an in-place grain change
(`Budget time grain cannot be updated`) → delete + recreate, sequenced so the $50 stayed live as cover.
End state, verified independently: **ONE budget, `Monthly_Budget`, $100 Monthly, alerts 50/80/100
actual + 100 forecast.** Start date forced to 2026-09-01 (Azure rejects backdating a monthly budget);
August uncovered, spend $0.00.

**Also established:** the billing account is an MCA of type **Individual**, `displayName "Andrew
Berman"`, `soldTo.companyName "Andrew"`, created 2025-11-11 — nine months BEFORE the subscription, so
it is inherited, not a setup error. **I over-stated this earlier** as possibly leaving AJ's concern
open and corrected it in-session: it is a commercial/invoicing matter, not a technical blocker.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | `--corpus all` × ~8 (comp-recon, passcraft, toolaudit, marker keys, importers) | **PASS** | The workhorse. Denominators printed on every census; the `comp-recon` zero is only meaningful BECAUSE the git probe carried a positive control. |
| `comp-read --enumerate` | ~12 runs across `_provenance.py`, `comp_passcraft.py`, `kuzu_*`, `resource_summaries_store.py` | **PASS** | Decisive for the audit: the DOCSTRING/COMMENT/CODE banding is what showed claim 3's 11 hits were 8 docstring + 2 comment + 1 string literal, i.e. no VPC path. A `grep -c` would have said "11" and misled. |
| `comp-which` | routing "recon a system…" | **PASS** | Correctly returned NO curated match and said the catalog does not cover it — a true negative, not a miss. |
| `comp-passcraft` | `--self-test` (20/20), `recon comp-freshness`, `taxonomy` | **PASS** | The subject under decomposition; exercised, not merely read. |
| `comp-toolgraph` | `denominator` | **PASS** | INDEPENDENT corroboration of the dead-annotation finding ("of the 63 universe, files present on disk 61") — a different instrument, not a re-run of mine. |
| `to-check.py` | `--all --assignee` | **PASS** | 0 active TOs, `unresolved_serials=0`. |
| `audit-archive-invoker` | startup A.2 | **WARN** | 5 findings, all in the documented known set. Nothing re-filed. |

**What worked.** `comp-read --enumerate` paired with a positive control on a known-good file was the
session's best instrument — it produced both the claim-3 survival and the claim-1 falsification, and in
each case the control is what made the zero admissible.

**What failed.** **AWS `filter-log-events --filter-pattern` through the shim returns 0 for
everything** — proven by a positive control on `BATCH_END`, a token visible in the same log group
seconds earlier. All marker-event counts from it are non-observations. This is the second
blind-instrument in one session (see Gap) and both were caught only because I ran controls.

**Gap found — SURFACED, NOT CHASED.** `org/mcp/comp-tool-runs.jsonl` **cannot observe
`comp-passcraft` at all**: 4 exercised invocations this session produced 0 rows while my own
`comp-which` run from the same session IS present. A zero in that ledger is non-observation in EITHER
direction. Owner = the comp-tool run-ledger owner. **NOT censused: which tools log and which do not** —
that is outside this run and is the question anyone reading adoption off that ledger needs answered
first. Noted because `0.8.0_AE_CloudComp` re-derived caller counts from that exact ledger this session
(msg 92724); for `comp-kuzu-inc` it demonstrably logs, so that census stands.

---

## MCP traffic

**In (2):** `92724` (`0.8.0_AE_CloudComp`, comp-kuzu wrapper retirement — courtesy notice, no scripted
call held, no reply owed). `92741` (`2.0.0_SA_COO`, **ANDREW-DIRECTED** 49F SmartX custodian-fields
investigation) — **read, NOT acked, NOT started**, held under the standing default-off-for-fabric-work
rule and surfaced to Andrew instead. It requests an ack on receipt.
**Out (1):** the `comp-passcraft` decomposition to `3.0.0_SA_CVO` on Andrew's word — DELIVERED
(1 delivered / 0 queued / 0 refused), carrying the DRY/UNCERTIFIED disclosure in its first paragraph
so the standing certifier could not mistake it for a graded artifact.

---

## Files Modified

See commit messages: `b1f37d5067`, `4559e6fd4c`. Rows needing extra context:

| File | Change |
|---|---|
| `workflows/atom_decomposition/runs/comp-passcraft-recon/20260902T1620Z/` | **NEW** run dir — `run.json`, `rectangle.c0.json`, `rectangle.final.json`, `DOMAIN_BAR.md`, 3 exercise artifacts |
| `org/XXX.md` | **−238 lines** (834 → 596); Step 1b rewritten, F table byte-identical |
| `docs/references/XXX_STARTUP_HISTORY.md` | **NEW** (341 lines) — the excised narrative, verbatim, with provenance |

**Not in this repo:** the Azure Owner grant and budget consolidation (subscription
`1e594a38-9247-4744-a33d-eb2b29dd64e6`), and an Outlook DRAFT to AJ + `support@littledogtech.com`.

---

## Blockers

**NONE owned by this seat.** Three items are sequence state, each with its holder named:

1. **[Andrew]** The Outlook draft is written and NOT SENT. Its last two paragraphs are superseded by
   the budget consolidation; the corrected text block was given in chat and awaits his word.
2. **[Andrew / 2.0.0_SA_COO]** Msg `92741`'s ack is owed by protocol and withheld by the standing
   default-off rule. Named rather than silently dropped.
3. **[1.0.0_SA_CTO~A]** The `NFRA_CLDGRPH` audit findings were delivered **in chat only and have no
   durable carrier.** This is a real gap: the 27-day-stale-pin finding and the claim-1 falsification
   exist nowhere on the record. If Andrew wants them to survive this session they need a commit or an
   MCP message.

---

## Current State

*Written for a reader with zero prior context.*

- **Commits (2), both MEASURED as ON ORIGIN** (`git ls-remote origin CLOUD` = `9e0c64b600`; local HEAD
  `8bae3806af` at read time — this claim is perishable and ages the moment an integrator runs):
  - `b1f37d5067` — the `comp-passcraft recon` atom-decomp run (DRY, uncertified).
  - `4559e6fd4c` — `org/XXX.md` 834 → 596 + `docs/references/XXX_STARTUP_HISTORY.md`.
- **Azure, subscription `1e594a38-9247-4744-a33d-eb2b29dd64e6` "Opal Capital"** (tenant
  `6810043e-d171-4adc-9975-068b35e179da`, opalinvest.com): TWO Owners —
  `Andrew@opalinvest.com` and `LDTAdmin@opalinvest.com` (assignment
  `181fae35-4da7-4886-9f2f-2afc71f21fd4`). ONE budget — `Monthly_Budget`, $100 **Monthly**, alerts at
  50/80/100 actual + 100 forecast, notifying Andrew only, starting 2026-09-01. The duplicate
  `opal-purview-payg-monthly-50` (which I had created 2026-08-28) is DELETED. Resource group
  `rg-opal-purview-billing` (eastus) unchanged.
- **The cancelled duplicate subscription** `7a09b6bb-6bc1-473d-912c-9f5a13547ed5` is state
  `Disabled`/`Warned`, 0 resource groups. **It cannot be renamed or deleted** — a disabled subscription
  is read-only (`ReadOnlyDisabledSubscription`, exercised) and `az account subscription` exposes no
  `delete` verb. Azure removes it automatically ~90 days after the 2026-08-28 cancellation.
- **Systems touched:** READ-ONLY on the estate throughout. No deploy, no infra change, no AWS write,
  no gate implemented, no TO cut, no dispatch. The only WRITE acts of the session were the two commits
  and the two Azure changes above.
- **Reachability at close:** ⛔ **the inbox Monitor `bf85ke7r5` was reported STOPPED** by the harness
  mid-session (no completion record). **This seat is presently DEAF and did not re-arm**, because
  arming is a startup act and Andrew was mid-thread. A successor MUST run `/watcher` at load.

---

## Next Steps

1. **[Andrew]** Send or amend the Outlook draft (corrected text block is in chat). Decide whether the
   `NFRA_CLDGRPH` audit findings get a durable carrier.
2. **[4.0.0_SA_CRO, next session]** Re-arm `/watcher` FIRST — this seat closed deaf.
3. **[1.0.0_SA_CTO~A]** Three asks from the audit, ranked: establish what wrote the marker at
   12:58:03Z today; re-derive claim 1 by enumerating **Iceberg/Nessie writers** then checking stamping,
   rather than enumerating stamp-callers and asserting coverage; make CAS-off an explicit acceptance
   property of `NFRA_CLDGRPH`, since the new architecture is what makes it load-bearing.
4. **[3.0.0_SA_CVO]** The `comp-passcraft` rectangle is DRY and uncertified; certification is available
   if wanted, not requested.
5. **[Andrew / finance, no urgency]** The Azure billing account is an MCA **Individual** in Andrew's
   personal name. Not a blocker; a cleanup item if Azure spend becomes non-trivial.

---

## Archetype rationale

**MIXED** — no single archetype covers the window. **VALIDATE** primary in substance: the adversarial
audit and the decomposition were both falsification exercises, and the session's two most useful
results were a claim falsified with a positive control and a claim I *could not* test because my
instrument failed its own. **EXPLORE** for the passcraft recon, **SCRIBE** for the XXX.md refactor,
**IMPLEMENT** for the Azure budget rebuild. No DEPLOY — nothing shipped.
