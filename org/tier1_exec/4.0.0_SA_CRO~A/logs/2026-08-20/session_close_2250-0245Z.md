# 4.0.0_SA_CRO~A — session close, 2026-08-19 22:50Z -> 2026-08-20 02:45Z

**archetype:** MIXED
**secondary_archetypes:** TRACE, DIAGNOSE, VALIDATE, COORDINATE

Respawn session (predecessor died ~2119Z, clean, nothing stranded). Wind-down is Andrew-directed
(~0245Z: *"write a /log and include these next-steps in it, then you will be done for the night, we
will address these tomorrow"*) — not self-initiated.

---

## 1. WINDOW SUMMARY

Two briefed acts became a night-long BD investigation that ended with a vendor API plane located,
a cent-exact three-leg tie-out, and four false findings killed by controls rather than by care.

**11 commits**, all under `4.0.0_SA_CRO~A`:

| commit | what |
|---|---|
| `4724daa901` | ACT 1: qt6 group-grain EMV re-run (T1-ORACLE L1 authority leg) |
| `3f396819ee` | identity residual = MARKET APPRECIATION, flat, negative result |
| `0e424d7279` | roster reconciliation 215 vs 201 — ADJUDICATED, immaterial |
| `89afa744ad` | ANDREW-DIRECT "All recs approved" |
| `5a6e555618` | endpoint sweep NEGATIVE + `/Api/DataMining` non-discriminating |
| `53848a2527` | sweep round 2: refusal obtained; `*.bdreporting.com` wildcard catch-all |
| `083ddf0d45` | sweep round 3: REST pursuit exhausted + self-correction |
| `85e2662ddd` | ANDREW-DIRECT "Both recs approved, also you have egress" |
| `7b23221c6a` | THE BI PLANE LOCATED (from Andrew's HAR, zero egress) |
| `8e37f53710` | ANDREW-DIRECT "you have egress there too, go ahead" |
| `01aac6af61` | BI plane LIVE probe: account grain + 4th control kill |

---

## 2. THE TWO BRIEFED ACTS

**ACT 1 — DELIVERED.** Ran persisted template 517678 (`OPAL_CROA_Probe_GroupKey_qt6`) at
`asOfDate` 08/18/2026: run 517753, 636 rows = 216 groups x 3 months. Positive control passed —
Travis Penfield Aug EMV **456,773,323.40**, reproducing the predecessor publication on a fresh run.
Handed DS~B `{group: emv}` JSON + 636-row CSV; they consumed it `@e03f16f9a2`.

**ACT 2 — DROPPED BY THE SOVEREIGN.** The spawn brief said both acts were authorized; COO's
`[STOP]` (225625Z) and MSTR's `[STOP-CONFIRM]` (225803Z) arrived before I reached it. I concurred
and grounded the determination on the PRIMARY record (Andrew's own verbatim ~1830Z *"I give you
egress to keep scanning BD"* plus a same-turn scope note), correcting COO's citation of "two
independent records" which were both DS~B documents from one derivation.

Andrew approved the write at ~0100Z; I measured it on a throwaway probe first and it FAILED ON
CONTENT — `Primary Portfolio Group` (436) carries TWO distinct values across 33,477 rows (33,473
`No Master Advisor Assigned` / 4 `Liv Shin`), maps to `masterAdvisor`, and sits at PORTFOLIO level.
He reversed to DROP at ~0135Z. **Template 390224 was never written.**

---

## 3. THE BD PLANE INVESTIGATION (the night's main arc)

**Sweep phase — honest negative.** 12 paths / 6 subdomains, plane not located. Obtained the
pre-registered refusal in BD's own words: `POST /v1/run {"templateId":5}` -> **404 "Template Not
Found, SourceId=5"**; `{"exportType":...}` -> 400. Mechanism found at zero egress: system templates
are EXPORTS keyed 1:1 by `exportType`, not queries keyed by templateId.

**Andrew supplied a HAR of his own dashboard session** — which moots the parked browser-observation
instrument question entirely (the sovereign performed the observation; I read a local file).

**THE PLANE: `bd3.bdreporting.com/advisor/api/v1/`** — a different API on the SAME HOST I had
already swept. `ClientView` is likewise a PATH, which is why `clientview.bdreporting.com` timed out.

**THREE-LEG CENT-EXACT TIE-OUT** (Travis Penfield, 216 groups each):

| leg | EMV |
|---|---|
| my qt6 datamining probe (517678 / run 517753) | 456,773,323.40 |
| Andrew's HAR capture | 456,773,323.40 |
| my LIVE `/advisor/api/v1/Dashboard/data` call | 456,773,323.40 |

Proves what the predecessor scan could only assert: the qt6 group-grain read IS the advisor's
dashboard number.

**Account grain exists**: `levelType=Account` -> 7,625 rows / 5,361 distinct accountNumber
(broader than fam 7,202 and the export 6,155), carrying `supervisedEmv`/`unsupervisedEmv` per
account — which qt6 cannot express at all.

---

## 4. FOUR FALSE FINDINGS, ALL KILLED BY CONTROLS — NONE BY CARE

| apparent finding | what made it look real | killed by |
|---|---|---|
| dim 436 inflates AUM +19.36% ($1.64B) | two correctly-computed numbers | same-moment control (it was a 23h VINTAGE gap; isolated effect = +0 rows, +0.000000%) |
| `/Api/DataMining/ExportSystemTemplate/5` -> 200, 5,534 B | plausible route returning content | invented PATH also 200 |
| `bi.bdreporting.com` -> 200 | **matched Andrew's own "Business Intelligence" brief** | invented SUBDOMAIN, byte-identical 242,826 B (wildcard catch-all) |
| "Travis has 5,361 accounts / $2.0B" | a real group id in a real filter param | invented GROUP ID returns identical rows — `values` is INERT |

**The pattern is the deliverable.** Not one was caught by inspection or plausibility. The
subdomain case is sharpest: it agreed with the sovereign's own words, which is exactly when a
finding stops being checked. **And a correctly-bounded negative is not coverage** — my sweep's
"exhausted, not found" was rigorous AND the target was never on the surface being swept.

---

## 5. SELF-CORRECTIONS ISSUED THIS SESSION

1. **`api.bdreporting.com` "live lead"** — retracted; invented route returns identical 429.
2. **Outlier over-claim** — "dominated by small-denominator artifacts" was false; only 6 of 30
   under $1M BMV, so 24 remain UNEXPLAINED and the artifact says so.
3. **Travis figure `456,773,300.00`** — that was the scientific-notation display, not the value;
   exact is `456,773,323.40`. Artifact carried the right number throughout.
4. **Carried DS~B's withdrawn 90.8% split** — dropped; verified by grep it never reached COO.
5. **F-010 class in my own tooling** — backticks in a `python -c` double-quoted string were
   SHELL-EVALUATED, silently deleting a column name and leaving a grammatical sentence with its
   subject removed. Caught only by a stray `Portfolio: command not found` on stderr.

---

## 6. COMPILER TOOLS

| tool | runs | result |
|---|---|---|
| `safe-commit.sh` | 11 | PASS — all landed; risk-reflex clean, denominators printed |
| `bd_endpoint_sweep.py` (as a library) | ~12 | PASS — auth/session helpers reused rather than reimplemented (build-ladder rung 2) |
| `comp-find` / graph tools | 0 | — see gap below |

**What worked:** reusing `bd_endpoint_sweep`'s `load_bd_session` / `get_bearer_token` /
`_raw_request` instead of writing a fourth BD client. The `.tools/aws` shim and `safe-commit`
wrapper behaved throughout.

**What failed:** nothing tool-side. My own `python -c` quoting (see §5.5).

**Gap found:** **there is no comp-tool for vendor-API surface knowledge.** Everything learned
tonight about the BD BI plane (endpoints, `levelType` grammar, the INERT `values` filter, the
separate bearer mint at `bd3/auth/token`) lives only in my deliverables. The next seat will
re-derive it — and will hit the inert-filter trap exactly as I nearly did. Candidate: fold into
`bd_endpoint_sweep` modes + the `data/black_diamond/API/domains/` docs (this is NEXT STEP 5).

---

## 7. MCP TRAFFIC

~30 messages handled; 25 acked (READ clock). Significant:
- **Fabric finding raised + closed:** `ack_messages` failing at my seat -> `0.8.0` diagnosed a
  version skew (broker carried pre-T1 bytes, my seat post-T1). Broker cycled 23:32Z; **it also
  surfaced a worse defect underneath — `check_inbox(mark_read=True)` asserting "READ ack recorded"
  UNCONDITIONALLY without checking its return (a FORGED READ CLOCK), fixed `@ee60ec75cc`.**
- Two `[STOP]`s received and concurred with; one `[QUIESCE]`/`[RELEASE]` observed (sends held ~4m).
- Corrected COO's "established as structurally non-exportable" (a prior stated as a measurement).
- Answered COO's ontology-lock-down capability question (§9).

---

## 8. CURRENT STATE (for a reader with zero context)

- **Template 390224: UNAMENDED.** Never written. Snapshot held at
  `<scratchpad>/t390224_SNAPSHOT.json` (session-scoped; regenerable by GET).
- **Householding one-shot grant: OPEN and UNCONSUMED.** Four seats each stopped the next from
  spending it. Record: `ANDREW_RULED_20260819_BD_HOUSEHOLDING_ONE_SHOT_SAMPLE_PLUS_PROBE_DESIGN.md`.
- **Egress held:** BD householding thread (Andrew ~0135Z) + BD BI/advisor plane (~0210Z). Both
  READ-SIDE ONLY and THREAD-SCOPED — they expire with their question. Not a standing lift.
- **Probe residue on the CALL-3 delete-on-ADVI_BDPARITY-close trigger:** BD templates
  517678 / 517685 / 517688 / **517766** (`OPAL_CROA_Probe_dim436_grain`); runs 517753 / 517767 /
  517768. **Deletion obligation recorded AT creation per COO 010352Z.**
- **Deliverables landed** under `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/`:
  `ADVI_BDPARITY_T1_ORACLE_QT6_GROUP_EMV_20260818.json`,
  `..._QT6_GROUP_GRAIN_20260818.csv`, `..._QT6_GROUP_IDENTITY_RESIDUAL_20260818.json`,
  `ADVI_BDPARITY_ROSTER_RECONCILIATION_215_VS_201_20260818.json`,
  `BD_SYSTEM_TEMPLATE_PLANE_SWEEP_20260820.md`, `BD_BI_PLANE_LOCATED_FROM_ANDREW_HAR_20260820.md`,
  `BD_BI_PLANE_LIVE_PROBE_20260820.md`, plus 3 ANDREW_DIRECT records.
- **HAR handling:** `C:\Users\AndrewBerman\Downloads\BI_scrape_BD_dashboard.har` stays in
  Downloads. **No credential, token, cookie or client row from it is committed anywhere.**
- **DS~B is culled** — the consumer of the L1 authority proof no longer exists. My last message to
  them is QUEUED and will never be read. The proof stands in the record for whoever resumes it.

---

## 9. ONTOLOGY LOCK-DOWN — capability answer given to COO (022356Z)

Andrew's 08-19 ruling puts lock-down ahead of all graph work, CRO base LEADING. Base CRO and CVO
were both culled at ~0210Z. COO asked whether this LANE could carry it.

**Answer: "yes, but NOT the propagation" — measured, not assumed.**
`.owned-paths.yaml` ANY_EXEC enumerates `4.0.0_SA_CRO` (base). **It does NOT list
`4.0.0_SA_CRO~A`**; the only CRO lane enumerated anywhere is `~SWEEP`. So `org/modules/**` is
**mechanically refused at this serial**. s4 exit-bar work: yes. `Unreconciled_Aua`: yes, but a
contested cell arguably wants the seat that contested it. **Whether Andrew's "CRO base leads"
travels to a lane is HIS reading of his own word** — I answered capability only and did not lobby.

⚠ **A lead owning a critical path with one leg it cannot mechanically execute is worse than no
lead, because it LOOKS owned.**

---

## 10. BLOCKERS

**NONE.** Nothing is blocked. Two items are event-gated (Monday c02-CFINPUT acceptance; THU probe)
and one is Andrew's own action (the 49F-contact endpoint question, approved ~0135Z).

---

## 11. NEXT STEPS (rendered ~0235Z; Andrew: *"we will address these tomorrow"*)

Ranked; rank 1 is the default. All five are SELF-EXECUTABLE under egress already held.

1. **[DEFAULT] COVERAGE MEASUREMENT — may retire the one-shot entirely.** Compute the
   pre-registered decision number |H INTERSECT fam-only| / 1,925 (against fam 7,202 / joint 5,277)
   from the BI account-grain payload. BI returns **7,625 accounts, broader than fam's 7,202**, so
   it can plausibly clear the 90% bar. The decision table is already written, so the result cannot
   be argued into either bin afterward. Closes the chartered question (the BD-native
   `dim_relationship` source change) on data already pulled, **without spending the sovereign
   grant.**
2. **ACCOUNT-TO-GROUP PRIMACY.** Chase attribution via the `advisorview` flow (`initial-load` ->
   `multiPortfolioGroups` with `selectedIds` -> `result`) and `/request/api/grouping/{z-id}` —
   the two leads Andrew's own HAR session performed. This is dim 436's successor question and what
   `bridge_group_account.is_primary` needs. Open-ended; the plane's filter semantics already fooled
   me once.
3. **HARNESS VINTAGE AUDIT (off-axis, highest consequence).** Audit the matched-window harness for
   the stored-baseline-across-a-vintage-boundary defect BEFORE Monday, when it becomes
   `ADVI_49F.c02-CFINPUT`'s acceptance oracle. That exact defect manufactured a $1.64B phantom
   finding tonight. **An acceptance oracle carrying a known-class defect certifies a fix on false
   evidence.**
4. **SUPERVISION SPLIT INTO PARITY.** Route account-grain `supervisedEmv`/`unsupervisedEmv` into
   the ADVI_49F supervision-sleeve GRAIN convention (ADDENDUM A6), which currently has no source
   that can express it. Value without urgency.
5. **PERSIST THE PLANE.** Fold BI-plane knowledge into estate tooling so it is not seat-local —
   endpoints, `levelType` grammar, the INERT `values` filter, the separate bearer mint. The
   inert-filter trap will fool the next seat exactly as it nearly fooled me. (This is §6's gap.)

**Cross-agent handoffs:** none outstanding. The L1 authority proof awaits whoever resumes
`[0.4.0_DS_ClientPlatform~B]`'s thread; `[2.0.0_SA_COO]` holds the lock-down lead question for
Andrew.
