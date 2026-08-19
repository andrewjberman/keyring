# CVO VERDICT — D5 package (Alt Research: corpus ingest + materiality-ranked build queue)

**Reviewer:** `3.0.0_SA_CVO` · **Date:** 2026-08-19 · **archetype:** VALIDATE
**Package scored, vintage-pinned:**
- `docs/architecture/D5_ALT_RESEARCH_PRD.md` @375c874a9e (111 lines)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/D5_ATOMDECOMP/run_20260819.md` @375c874a9e (38 lines)

**Verdict: ACCEPT — 0 P0, 1 P1, 1 P2.** Deliberately thin and it says so, correctly: phase 1 is
complete, the store keeps its own PRD of record, and this PRD authorizes continuation rather than
re-legislating a working contract. Three things done right:

- **The registry was cross-checked against the filesystem, explicitly citing Rule 22** (run #1:
  *"registry content — cross-checked vs files below per Rule 22"*). Every phase-1 claim verifies at
  each checkable point (30 raw / 29 structured / 63-row queue / rank-1 UNH matches). **This is the
  map-vs-territory discipline applied to our own records, unprompted.**
- **The declared run range is CORRECT** (`cells #1-#10` against a run of #1–#10) — the defect D1 and
  D3 both carry is absent here.
- **A Rule-24 grain issue was raised proactively rather than found by review**: §3 makes explicit that
  the build queue has **two member kinds** — 63 ranked SECURITIES ("which names justify coverage")
  and 3 named PIPELINE CANDIDATES ("which data products were called for") — *"they are not one list."*
  That is the taxonomy law being applied at authoring time, which is where it is supposed to bind.

---

## P1-1 — For CTO. This run declares no verdict vocabulary at all — the fifth variant across six packages.

D2/D7/D1/D3 each declared a verdict set in their run header. **D5's header declares none** (Author /
Authorization / Method / Boundaries only), yet the table uses **MEASURED** and **RECORD**, plus two
split-verdict rows (#3 *"MEASURED (count); dup-pair decomposition = RECORD"*, #5 *"MEASURED (counts);
… NOT reconciled this run"*).

Under your @36a7fbd70e ruling the vocabulary must be stated **in-artifact** with per-value
expected-value eligibility, so this run is non-conforming as it stands. **No new ask** — your family
ruling already covers it; flagging so D5 is not skipped when the remaining runs conform at their
absorption commits, since an *absent* declaration is easier to miss than a *wrong* one.

**No illegal derivation found:** the RECORD-sourced "28 unique" does not appear as an expected value —
TO-D5.1's acceptance is *"raw byte-fidelity re-hash + structured count advances + queue rebuilt"*, with
no hardcoded count. Checked specifically because that is the pattern D0's TO-5 failed.

---

## P2-1 — For CTO. "Cosmetic" is a claim about consumers, and no consumer check was run.

Run #5 flags that `mentions.jsonl` carries 4 records where the registry narrative implies a larger
index; §5.3 and TO-D5.3 classify this as *"cosmetic reconciliation, not blocking."*

**The classification is probably right** — the queue derives from `altdata_build_queue.csv`, not from
mentions — **but "cosmetic" asserts that nothing downstream reads the file, and that was not
measured.** It is an inference about consumers presented as a property of the discrepancy. One
`comp-blast`/name scan over `mentions.jsonl` settles it in seconds and converts an assumption into a
finding either way. Cheap, and it is the same class as D3's P1-2 (a consumer named by assumption
rather than by measurement).

---

## Explicit deferrals

- **The m365 shared-folder + 50-message chat-paging constraints (run #8)** — source-confirmed in the
  registry, already routed to CTO as architecture items, and correctly kept OUT of scope. Ingest being
  *"structurally operator-paced"* is an honest constraint statement, not a gap.
- **Teams retention (run #9)** — unowned residual, surfaced with a proposed parking scope (§7 Q2).
  Correctly not adjudicated here.
- **No §5.1 matrix rows** — accurate; no gold script, Lambda, or portal component ships under D5. The
  filesystem-verification substitute is the right evidence for a continuation PRD.
- **Event-gating with no self-start** — matches S10 and is stated three times. Conforming.

---

## What you should have asked but did not

**An event-gated artifact needs a freshness contract, because the gap between emission and activation
is unbounded by design — and this queue is on a collision course with Rule 25.**

The queue is explicitly held for *"the day Andrew's prioritization word activates it"*, with **no
self-start**. That is correct. But the ranking it will be activated *from* has a vintage nobody has
declared:

- The corpus runs **2026-04-07 → 2026-07-31** plus one 08-03 transcript.
- The ETF weight side rests on `source_{divz,idvz}_holdings_**20260731**.csv`, and §4 says it
  *"refreshes when new holdings snapshots land"* — **so if none land, the weights stay frozen at 07-31
  and nothing announces it.**
- §7 Q1's proposed default on activation is *"top-5 by firm weight (UNH/PM/MPLX/CVX/NVDA)"* — a
  ranking computed from that frozen basis.

**Rule 25 (Andrew-direct 08-11): stale ≥90 days ⇒ DORMANT unless a DECLARED exception.** A 07-31 basis
reaches that bar around **2026-10-29**. D5 declares no TTL, so on the current text the queue silently
becomes dormant-by-default while still presenting as the ready-to-activate artifact — **and the first
thing that would happen on Andrew's word is a build decision made from a ranking nobody re-derived.**
Firm weights move with holdings; a top-5 from July is not a top-5 in November.

**Recommend (cheap, no machinery, moratorium-clean):** (a) the queue declares its TTL or its exception
kind under Rule 25 — this is plausibly a LONG-TTL-LIVE artifact like the CMA case, but that must be
*declared*, not assumed; and (b) the §4 activation protocol's **first step** re-derives or explicitly
re-affirms the ranking basis and **prints its vintage** beside the recommendation. Not a monitor — a
line in a procedure that only ever runs on his word.

**Why this is the unknown-unknown rather than a P1:** nothing is wrong today, and the defect cannot be
observed by reading either artifact — it only appears in the interaction between an event-gated design
and a dormancy rule that lives in a different document.

— 3.0.0_SA_CVO
