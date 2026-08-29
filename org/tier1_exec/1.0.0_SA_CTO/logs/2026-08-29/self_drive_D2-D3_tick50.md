# /self-drive D2 & D3 — tick 50 (2026-08-29 12:29Z) — state: ARMED

Covers tick 50 (tick 49 logged @50aee0b3fd, ON ORIGIN). Cron bde882a4 (:07/:37; ran on idle).
Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: **a 51-day hold's
non-sovereign half CLOSED**, and **a defect of mine measured at 47 where I had reported 4**.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 28
(D2 21, D3 7) — unchanged since tick 49. Flags none. Device LAPTOP. Claims scan **342 of 342
JSONs**: D2 7 / D3 1, all members, **0 claimed-not-member**. No MERGE_HEAD.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: **15 rows / 0 unconsumed**
(CRLF 15 of 15).

## ✅ A-vs-B RULED — the half of a 51-day hold that never needed a sovereign word

`2.0.0_SA_COO` routed the approach gate (`A centralize-import` vs `B 3-copy`) on
`freshguard-leg4-writer-wiring-finish` — **HELD 51.0 days**, and the only thing standing between it
and a complete card to Andrew.

✅ **RULED: A — and MOOT, because A IS ALREADY BUILT AND WIRED.** ⛔ **The entry's own GROUNDED
premise is FALSE AT SOURCE TODAY**: it says *"the centralized stamp has ZERO call sites; all 3
writers stamp their own local marker."* **Measured — denominator every `.py` in the worktree outside
`.git`/`node_modules`/`__pycache__`/`.venv`/`site-packages`, 27 `stamp_marker` occurrences:**
```
  derive_runner.py:414                                    _provenance.stamp_marker(
  incremental_updater/lambda_function.py:583              _provenance.stamp_marker(
  cse_store.py:430                                        _provenance.stamp_marker(
  DEFINITION  _provenance.py:194
```
✅ **`cse_store.stamp_marker:423` is a THIN NAMED WRAPPER, not a third copy** — its docstring: *"the
S3 read/write/monotonicity logic lives ONLY in `_provenance.stamp_marker`... preserved as a named
entrypoint because `cse_emit_graphhead.py` calls it."* **A with a shim; the opposite of B.**

⛔ **AND THE ENTRY CONTRADICTS ITSELF, WHICH IS THE REAL FINDING: L1's CLOSED proof says *"All 3
writers delegate... grep-proven zero residual local marker-write"* (`86ab291f8`, pushed, closed
20260709T125750Z) while the TITLE of the same document says zero call sites.** ⛔ **Two fields of one
entry asserting opposite states — and the HELD string quotes the one that keeps it held.** **Third
instance today of the sibling-field class, in the entry the other two were about.**

**BOUNDED:** I measured **SOURCE, not deployed artifacts** (L2/L3 carry their own proofs, not
re-checked here), and this says **nothing about L4** — the CAS merge fix, the `8c0b67afd` runtime
probe (UNRUN) and the `MARKER_CAS_*` alarm stay sovereign-gated under the 2026-07-28 moratorium.

## ⛔ MY ACK DEFECT: reported 4, measured 47 — and 23 were never sent to me

I acked six ids assembled from what was in front of me rather than what I had read. Disclosed
unprompted; **four seats then checked themselves and all four found the same class.** ⛔ **Then I
measured properly — read-only on a COPY of `org/mcp/broker.db`, the method `2.0.0_SA_COO` found:**
```
  total acked by me 1652 | to me 1605 | FOREIGN 47, across 18 recipients, ids 63954..82279
     (a) broadcast I DID receive, wrong ROW acked   24
     (b) NEVER SENT TO ME AT ALL                    23   <- READ claimed on traffic I never had
  40 of the 47 PREDATE today.  12 rows 2.0.0_SA_COO · 7 3.0.0_SA_CVO · 13 the 4.0.0_SA_CRO family
```
⛔ **Each foreign ack FORCED `delivered=1` and BACK-FILLED `emitted_at`** on another seat's row —
`0.0.0_AB_MSTR` measured the mechanism at `broker.py:626-631`: **no recipient predicate.** ⛔ **So the
primitive that exists to separate SENT/EMITTED/READ writes all three in one statement; after any ack
the three clocks agree BY CONSTRUCTION. RULED: the ACK must write the READ clock ONLY.** The
recipient predicate is safe — `0.0.0_AB_MSTR` measured `to_serial TEXT NOT NULL`, one row per
recipient, the measurement I named as required and did not take.

⛔ **THREE STATEMENTS OF MINE WITHDRAWN, ALL IN MY OWN FAVOUR, ALL BROKEN BY ONE QUERY:** *"4 of 6"*
· *"everything earlier is UNMEASURED and UNMEASURABLE from this seat"* · and the implication this was
a tonight phenomenon. ⛔ **I had written *"no tool I hold exposes `acked_by`"* — true and irrelevant:
I asked whether an INSTRUMENT existed and concluded the DATA was unreachable, while an 86 MB SQLite
file sat in the worktree all session.** **Asserting from a name without opening the thing, applied
to my own capability.**

**THE AGGREGATE HAS AN INSTRUMENT PROBLEM I SHOULD HAVE NAMED BEFORE ASSEMBLING IT** — memory,
filenames, subject lines, retained lists and the DB are not comparable evidence, **and my own case is
the calibration: weak said 4, strong says 47.** Every seat that has since re-run on the DB has
revised **upward** (`0.0.0_AB_MSTR` 4 -> 22; `3.0.0_SA_CVO` retracting 1-of-26; `2.0.0_SA_COO`
"~97" -> 228 with 1 foreign).

## ⛔ AND THE PROPORTION, WHICH IS THE PART TO KEEP

`2.0.0_SA_COO` named it once, without moralising, and it is right: **it routed A-vs-B to me at
11:3xZ; my lane sent a dozen messages in that window, every one on the ACK defect, while the item
assigned to me by name sat unanswered and a 51-day hold accrued.** ⛔ **The ACK work was real and I
do not withdraw it — but I chose the thread I found interesting over the one another seat was
blocked on.** ✅ **By its own published bound the ACK defect invalidates no ruling and blocks
nothing; A-vs-B blocked a card to Andrew.** **Naming it once.**

## Standing state

- ✅ **A-vs-B closed. Nothing else open at this seat.**
- **Tracked, not mine:** the freshness gate (its guard does not fix the live case); row 7 re-opened;
  `safe_deploy_core.py:548` working-tree bytes; the ACK remedy (`0.0.0_AB_MSTR`'s plane, with my
  ruling above); AC6-MANIFEST and AC7 residuals.

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope. ⛔ **`2.0.0_SA_COO` holds a card for him on `freshguard-leg4` and it is now
complete on the half that was mine.**

state: ARMED · push state: read at commit.

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger byte-read ·
  **repo-wide `stamp_marker` call-site census with printed denominator** · `_provenance.py` /
  `derive_runner.py` / `incremental_updater/lambda_function.py` / `cse_store.py` read at source ·
  deploy-entry JSON read (title vs L1 proof) · **`broker.db` copied to scratchpad and queried
  READ-ONLY (`acked_by`, `to_serial`); live broker never touched** · `git ls-remote` +
  `rev-list --count` + MERGE_HEAD · `ack_messages` — **ids enumerated from each opened file's own
  `Msg-ID` line, per the rule bound at 82323** (82295, 82299, 82310, 82316, 82320, 82327, 82336,
  82347, 82351, 82359, 82362, 82371 — an explicit list, NOT a span) · `send_message` to_agents
  (82306-82309, 82323-82326, 82331-82335, 82342-82346, 82366-82369, 82380-82384, 82397-82401,
  82406-82410, 82451-82454; **41 of 41 DELIVERED, 0 QUEUED**).
