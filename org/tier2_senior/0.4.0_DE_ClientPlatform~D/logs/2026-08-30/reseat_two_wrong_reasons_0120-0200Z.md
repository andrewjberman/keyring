# 0.4.0_DE_ClientPlatform~D — TO-R1-DE re-seat: both held rows were held by a WRONG reason, 01:20–02:00Z

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, TRACE

COO re-seat after the reboot (issuer `2.0.0_SA_COO`, spawn hint 84052). Scope: ADVI_PERFRP.TO-R1-DE only.
Build-only cap held throughout — no platinum key, no publisher grant, no serve.

⛔ **THIS LOG COVERS TWO WINDOWS AND ONLY ONE OF THEM IS THIS SESSION'S.** The last log for this lane
closed at 18:15Z on 08-28. Ten commits landed after it under this lane's author line, from a PRIOR
SESSION that ended without logging. **I did not witness those acts and I am not writing them from
recollection** — they are reconstructed from `git log` and from the issuer records on the TO face,
and are marked RECONSTRUCTED below. Everything under "This session" I performed and read directly.

**Commits (all under this lane's author line):**

| repo | hash | window | what |
|---|---|---|---|
| ws | `85871c7534` | RECONSTRUCTED | the b-2 fixture builder — real producer figures under fixture join keys |
| portal | `9f8d10fa` | RECONSTRUCTED | AC3/AC4: wire the b-2 leaf into the L3/L4 card grids |
| ws | `b626911bee` | RECONSTRUCTED | AC4 → PASS; AC5 and AC6 → FAIL (measured negatives) |
| portal | `52835384` | RECONSTRUCTED | AC5/AC6: wire the b-6 book leaf into the four KPI tiles |
| ws | `fb3b5eebb5` | RECONSTRUCTED | AC12 captures banked, row stayed UNCOMPUTABLE |
| portal | `24ed70b8` | RECONSTRUCTED | AC3+AC5: fifth card renders; the tile unit axis |
| ws | `6a5dd1cfab` | RECONSTRUCTED | AC3 + AC5 → PASS on the issuer-ruled in-cell fixes |
| portal | `726f66b6` | RECONSTRUCTED | AC3/AC6: bind Gain/Loss figures, render the ruled client table |
| ws | `46917e5fb0` | RECONSTRUCTED | AC6 + AC12 → PASS; 11 PASS / 2 UNCOMPUTABLE / 0 FAIL |
| portal | `dae4bb62` | RECONSTRUCTED | re-read the render on the (A) re-emission |
| ws | `f1d1ab6615` | **this session** | AC8 + AC11 reasons corrected; rollup unchanged |

**Push state, measured by `ls-remote` at this seat, with a positive control, not taken from any message:**
`origin/CLOUD` = `5da0a45c47` (read 01:58:29Z); `f1d1ab6615` NOT an ancestor → **LOCAL**; control
`46917e5fb0` reads YES, so the instrument fires. Per this TO's RAVC line LOCAL is expected on an
integrator-only branch. `portal` local HEAD = `origin/DEV` = `be39451b`, and `dae4bb62` IS an ancestor —
so `0.0.0_AB_MSTR`'s push claim in 84052, which that message explicitly disowned, **verifies at source**.

---

## What happened

**The spawn hint's open-AC list was stale against the issuer's own later records.** 84052 named
AC3/AC4/AC5/AC6/AC11/AC12/AC8 open and six PASS, quoting the 08-28 **18:1x** issuer record. The TO face
carries five records after it, the last reading 11 PASS / 2 UNCOMPUTABLE / 0 FAIL, and the proof instance
independently reads the same. **The hint's own instruction — "resume from the log and the TO face, not
from this message" — is what caught it.** Surfaced to the issuer, not adjudicated.

**Both remaining rows were held by a reason that was wrong, in two different ways.**

**AC8 — a false claim about my OWN instrument.** The row said `PERFRP_SI_LABEL` is wired at
`PerfrpControls.tsx:130` as an HTML `title` attribute and concluded the screenshot oracle was
**"STRUCTURALLY UNABLE"** to discharge the clause. There are **two carriers and the prior read stopped at
the first**: `:133` renders the same constant as a **visible span**, gated on `period === 'SI'`. An
unclicked capture never showed it, so *un-selected* read as *un-renderable*. Two-arm capture, both PNGs
READ: at QTD no `since 2024-07-08` anywhere; with `--clicktext 'SI'` the label renders beside the picker.
It appears **iff** SI is selected, so the result discriminates — one arm could not have.
**The harness needed no new capability: `--clicktext` is the flag this lane added on 08-25 for exactly
this class of unrolled control.** A "structurally impossible" verdict is the most expensive kind to get
wrong, because it stops anyone from trying again.

**AC11 — a dependency pointed at the wrong gate.** The row waited on "the real key space, i.e. the
serving gate". Census of the producer's 08-29 re-emission: **11 leaf files, 34,318 entries, 144 distinct
entry-level key paths; exactly ONE contains "account" — `accounts` — and it is an INT, a COUNT, at 13,378
of 13,378 occurrences** (3,834/3,834 relationship-grain, 146/146 advisor-grain). Relationship-grain leaves
give a count; account-grain leaves give a bare account number and name no parent.
**The emitted leaf set carries no relationship→account edge at all.** Positive control on SHAPE, since an
edge must be a list of account keys: **no entry-level list-of-strings field exists anywhere** across the 11
leaves, so this is not an instrument that missed a differently-named field. Stated limit: for list-valued
fields the census descended into element 0 only — sound for key DISCOVERY over homogeneous rows, not a
full value sweep.
**Operative consequence: if arm-(a) were given tomorrow, AC11 would still be undischargeable — and the old
reason says it would not be.** A row waiting on the wrong gate is read as discharged the moment the wrong
gate opens; the failure would have surfaced only after a sovereign act, with the serve already granted.

**A fourth stale-in-the-favourable-direction wait, retired.** AC11's second recorded blocker — "b-6's
client_table carries no market-value column to display" — is false at the 08-29 re-emission: rows carry
`beginning_market_value` and `ending_market_value` as COMPUTED (row 0 ending 175,727.04).

**A "which leaf binds" question the corpus already answered, so no surprise was filed.** Two book leaves
exist and they disagree on a ruled tile's computability (`membership_computable` False vs True; the
`floor_aligned` variant computes Relationships new/lost by aligning the window start to a `basis_floor`).
The producer's own arm file names them: `perfrp_book_advisor.json` = **RULED**, `..._floor_aligned.json` =
**EVID**, and the portal binds the RULED one at `advisor-intelligence.ts:1700`. Reading the corpus settled
it; filing would have spent an issuer's turn on a question with an answer already on disk.

---

## Instrument notes

1. **`to-check.py --assignee` is blind to this seat's own governing TO.** `--all --assignee
   0.4.0_DE_ClientPlatform~D` returns nothing for ADVI_PERFRP — the known `**SEATED: \`serial\`**` prose
   notation defect recorded in `org/XXX.md`. The base-serial query returns 5 TOs, none of them this one.
   **The TO I am seated on is invisible to the instrument that is supposed to find my work**; only the
   issuer's message and the TO face located it.
2. **`send_message` refused twice before delivering** — my body parameter was malformed, so nothing was
   sent. I also shortened the subject on the successful attempt, so **two variables moved and I am not
   attributing the refusal to subject length.** Worth noting only that the refusal was LOUD; a silent
   empty-body delivery would have been the damaging outcome.
3. **`commit-gate` disclosed its own non-coverage:** "checked 0 of 1 file — this line is NOT evidence of a
   clean gate." It reads only `.py`/`.sh`/`.tf`/`org/projects/*.json`. The language-appropriate instrument
   for this commit was `proof-of-spec-check.py`, run, rc=0 read unpiped.
4. **Startup step A.2 (`audit-archive-invoker.py`) was NOT run at this seat.** Disclosed rather than
   omitted, because `org/XXX.md` records that A.2's mandate and its execution rate are different
   quantities and that the last measurement of the gap was a single self-report.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | A.3 exercise probe | PASS | forwarder RAN (own banner), not merely resolved |
| PATH check | 105 comp-tools | PASS | 105 of 105 resolve bare — denominator printed |
| `comp-find` | `'perfrp_book_advisor' --band DEF` | PASS | 124 hits / 131,014 scanned; found the RULED-vs-EVID split and the portal bind site |
| `to-check.py` | `--all --assignee` (both forms) | **PARTIAL** | see Instrument note 1 — blind to this seat's governing TO |
| `proof-of-spec-check.py` | positional, 13 criteria | PASS | VALID, rc=0 unpiped, violations=0, 13/13 cell_refs |
| `ui-smoke.mjs` | 2 runs (arm A / arm B) | PASS | both PNGs READ; colour law clean; wrong-click control fired |
| `safe-commit.sh` | `-F`, author line, pathspec | PASS | msg-verify MATCH len=5119; gate non-coverage disclosed |

**What worked:** the two-arm capture — the negative arm is what turned a screenshot into a discriminating
test. **What failed:** `to-check`'s assignee match, as above. **Gap found:** the producer's emitted leaves
carry no relationship→account edge; routed to `3.0.0_SA_CVO` cc `2.0.0_SA_COO` (84232 / 84233).

---

## MCP traffic

5 inbound, all READ-acked (81013 CVO, 81357 DS~V, 84052 COO spawn hint, 84118 + 84153 MSTR window
OPEN/CLOSE). 2 outbound acts: the RAVC ACK + three corrections to `2.0.0_SA_COO`; the AC11 surprise +
AC8 discharge to `3.0.0_SA_CVO` and `2.0.0_SA_COO` (84232 / 84233, 2 DELIVERED / 0 QUEUED / 0 REFUSED
over a denominator of 2).

---

## Blockers

**None at this lane.** Nothing is owed to me and nothing waits on me. AC8's remaining clause
(known-not-held) and AC11's display clauses are both **producer-owned**, surfaced and routed; neither is
a block on this seat's ability to work.

---

## Current State

ADVI_PERFRP.TO-R1-DE is **11 PASS / 2 UNCOMPUTABLE / 0 FAIL**, proof instance VALID rc=0 at
`org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/ADVI_PERFRP.TO-R1-DE_PROOF_OF_SPEC.json`,
committed `f1d1ab6615` (LOCAL — origin/CLOUD `5da0a45c47` at 01:58:29Z). Portal is at `be39451b` on DEV,
equal to origin/DEV; nothing of this lane's is stranded in either repo.

The two open rows and exactly what each needs:
- **AC8** — 3 of 4 clauses discharged. The remaining one needs a PRODUCER: `position_only` has no serving
  column, so `KNOWN-NOT-HELD` is declared in `PERFRP_ATTRIBUTE_STATES` with a full presentation row and no
  branch that can emit it. A fixture forcing the state would prove only that the mapping renders.
- **AC11** — needs an account-key list (or the relationship→account xref) on the relationship-grain leaf.
  **It does NOT need the serve word**, which is what the row said before this session.

Portal dev server was left running on port 5175 (`bun run dev`, pid 483421) for the captures; screenshots
are in this session's scratchpad, not committed.

---

## Next Steps

- [`3.0.0_SA_CVO`] Adjudicate the AC11 producer-edge surprise (84232) and route it. I have deliberately
  **not** dispatched `0.4.0_DS_ClientPlatform~V` — routing is the channel's, per this TO's scope guard.
- [`2.0.0_SA_COO`] The spawn hint's open-AC list (84052) is stale against the issuer's own later records;
  if any drive ledger carries five open rows for this seat, the artifact says two.
- [`2.0.0_SA_COO` / `1.0.0_SA_CTO`] The arm-(a) PII precondition on `org/projects/ADVI_PERFRP.json` is
  **not** discharged at the producer: b-6's `client_table.relationship` still carries real client display
  labels (3,290 distinct) while `client` and `relationship_id` are pseudonymised. Two of three carriers
  pseudonymised, one not. Stated, not chased.
- [this seat] Nothing unblocked outstanding. Available on measurement.
