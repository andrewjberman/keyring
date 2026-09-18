# AMGT_RESAPP round 13 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ HEAD at the time of the packet commit (see that commit), LOCAL.
**Written:** 2026-09-18 ~17:3xZ, after the round's last two orders closed (`AMGT-rk-22` complete, `AMGT-rk-26`
withdrawn). Same artifact class as `ROUND12_L8_PACKET_20260917.md`: the COO's own end-of-drain handoff, not a
substitute for `3.0.0_SA_CVO~Z`'s L8 channel compile or its L9, both of which have run throughout this round
(rows `Z-S169`/`Z-S170`/`Z-S171`, msg 23610, msg 23668).

## 1. Round state, final

**97 orders, 97 terminal -- `_open_tos_census` reads OPEN 0 of 97** (the gate's own resolver, called directly
at the withdrawal commit `5dc9089ca7`; not a status-word count). The two that closed this session:

| order | terminal state | how |
|---|---|---|
| `AMGT-rk-22` management-posture-producers | **complete** | worker `~32`; AC1/AC2 re-verified by this seat on a fresh instrument against live S3 before the drain (`d268e74b0a`) |
| `AMGT-rk-26` render-capture | **withdrawn** (issuer) | Andrew-direct 2026-09-18 ~17:1xZ, *"write off the frontend TO"*; measurement row `W31-S3`; record face of the order carries the verbatim word and what it leaves for L9 (`5dc9089ca7`) |

Every other order's terminal state is unchanged from `Z-S170`/`Z-S171`'s sweep and the CTO's register row.

## 2. Round-13 acceptance -- 24 PASS / 3 FAIL, and all three FAILs are criterion defects (unchanged)

Per `3.0.0_SA_CVO~Z`'s own per-criterion sweep, corroborated by `1.0.0_SA_CTO~Z`'s terminal-by-instance bucket
(SEVEN -> THREE by real re-runs this session, msg 23646):

| criterion | why it fails | ruling on file |
|---|---|---|
| `rk-20` AC1 | `<expect>` names a shape the world never had | `W27-S9` / `Z-S161` |
| `rk-23` AC1 | sends a raw slash where the page sends `%2F`; 33 of 33 measured on the page's own shape | `Z-S163` |
| `rk-30` adapter AC1 | demands MEASURED scores whose inputs the round never committed to produce | `Z-S173`: the ACT is complete, AC1 is NOT flipped, the unmet portion graduates |

**Ask:** grade them as the rulings state. `rk-30` adapter AC1 is not to be re-run or re-labelled (CTO msg 23650).

## 3. `AMGT-rk-22` coverage -- state the figure and its CAUSES correctly, so round 14 fixes the right stage

Population of record: **33 keyed names** (`crosswalk/v1/2026-09-15.json` `denominators.MEASURED = 33`; the
"34" that circulated this afternoon was the CTO's own error, retracted in msg 23692).

- **Posture: 33 of 33** served, clean.
- **Management: 12 of 33 served by status** -- the 12-name filing cap exactly. **7 carry officers (62 officers);
  5 carry ZERO officers**, all `UNRESOLVED-SOURCE`. Re-measured independently by the CTO on the served thesis bundle
  (msg 23698) and by the CRO on the Exec Management panel (msg 23697); this seat's figure agrees.
- ⛔ **The producer labelled those 5 `absence_reason_class = pull-missed`, and that label is WRONG for all five**
  (CTO, msg 23698, read at source): `ASML`, `PBR` -- the persisted 20-F carries an EMPTY officer section (Item 6 was
  not cut from the primary document: a filings-stage CUT defect); `HAL`, `INTU`, `KMB` -- *"no declared shape read
  this section"* (a roster-SHAPE gap in `roster.py`). Neither is a re-pull. **Carry to round 14 as two items in two
  stages, and relabel the five -- a completion record that says `pull-missed` would send round 14 to re-run a pull
  that already succeeded.**
- The earlier "management reached 14" figure was an S3 object-count artifact (2 `_pool/` index files), corrected
  at `6366933721`; it does not appear in this record.

## 4. `AMGT-rk-26` -- withdrawn, and what the withdrawal leaves open

**Measurement (row `AMGT_RESAPP-Z-W31-S3`, BLOCKING / ARMED, `disarm_owner` `1.0.0_SA_CTO`, filed by the worker,
landed by this seat under the audited override):** a mandatory two-step MFA challenge (Andrew-direct 2026-09-02,
"MFA required for all users", D12_PHONE_OTP_ALL_AWS) intercepts every login before any accessToken or refresh
cookie is issued, measured on BOTH documented automation logins; the auth-handler source carries no headless
bypass. The harness reaches the login form and the MFA screen and nothing past it. The worker correctly did NOT
read the MFA table or any signing secret to recover a code. This blocks headless authenticated capture as a
CLASS (~27 `.frontend-dev/testing` constitutions share the same login), not just here.

**Consequences for L9, stated so nothing closes by silence:**
- AC1 unreachable as written; AC2/AC3 (judgment) ungraded -- there is nothing to grade.
- **W27-S10** (does the edge forward the delivered path `%2F`-encoded or normalised) loses its only surviving
  oracle. `3.0.0_SA_CVO~Z` has already stated how it grades that case: *"dispositioned WITHOUT the discriminating
  instrument"* (msg 23610) rather than on a direct invoke that certifies its own assumption. That stands.
- The disarm is the CTO's, and it is one of two options that are Andrew's because both touch his MFA decision:
  a human completes the one-time code once in a HEADED session and the harness drives after it, or an MFA-exempt
  automation identity he alone grants. Neither is needed to close round 13 (CTO msg 23699, concurred).
- The worker's unlanded `.tools/frontend-dev.py` network-capture extension (a `page.on("response")` hook, a
  per-scenario log, `fill`/`press` actions) is preserved as a patch in this seat's deliverables
  (`AMGT_RESAPP_rk26_frontend-dev_network-capture_UNLANDED_20260918.patch`) for whichever round re-cuts the capture.

## 5. The portal, this round -- published to DEV, PROD held

- `origin/DEV` = `625a0888` (integrator `0.0.0_AB_MSTR~Z`, msg 23702, ls-remote after the push): round 13's two
  page halves (`6cbd3049` rk-19 label-and-link, `d74ff760` rk-30 ModelTab) plus their integrator merge, pull-merged
  by this seat onto origin's own admin-only gate commit `d8135e0a` (Andrew-direct 2026-09-17). Clean merge; the
  `App.tsx` resolution took origin's gate verbatim.
- **Build check on `625a0888`, run by this seat on Andrew's word:** `tsc -b` rc=0; `bun run build` rc=0; the merge
  touches exactly four files, all under `src/pages/SecurityAnalysis/` (+ `ThesisDriverChart.tsx`), plus the gate.
  Nothing the rk-26 worker did is committed anywhere (its only portal artifact was a gitignored `.env.local`).
- The DEV Build & Validate check has been red 4 of 4 runs since Tuesday (pre-existing, one of them another
  project's); compare the new run's failing step and error set against the previous run before attributing.
- **PROD stays held** on CVO verdict msg 23668's three conditions (round 13 closed; a CTO+COO never-widen pair on
  file for the promote; the DEV check green on its own merits). Andrew, 2026-09-18 ~15:0xZ: *"the Promote can wait."*
- Andrew's own observation at 17:0xZ that no data loads on any portal page on the local dev server is explained by
  s.4: with MFA blocking token issuance, every authenticated call has no bearer. It is an auth/environment fact,
  not a build defect; this seat did not reproduce it after the worker's server died and does not claim to have.

## 6. Carries to round 14 -- adjudicator-level, none this seat's to resolve inside round 13's decomposition

1. The Peers V measure-definition question is **Andrew's** (msg 23657/23662), not the CTO's L4 product; no round-14
   scores cell is cut until he answers.
2. `Z-S174` (CTO withdraws `Z-S164`'s unreachability conclusion): with egress authorized, Peers V computes for
   30 of 34 covered names using the measure as written -- the binding constraint was peer IDENTITY (224 of 1,658
   peer rows carry numeric SEDOL stems the resolver skipped), not the estimate fields. `NVDA_US_Equity` has model
   blocks but no MEASURED identity (outside the keyed 33).
3. `peers_v`'s EMPTY `absent_reason` on 33 of 33 -- a one-field fix, no new data.
4. `rk-30` adapter AC1's unmet portion (`Z-S173`).
5. Management's five zero-officer names: two stages, two fixes, relabel (s.3).
6. CTO msg 23698, verified at source: `batch.py:81-84` splits the S3 key on `/` and takes `parts[2]`, so
   `BP/_LN_Equity` and `NG/_LN_Equity` can never be built and the run reports success; and its census counts
   UNRESOLVED-SOURCE placeholder filings as real (188 = 12 real + 176 placeholders) -- one enable would write ~176
   zero-officer rosters the adapter serves as SERVED. Disabled today; both belong in front of whoever enables it.
7. `W32-S3` (posture keys for the two slash-bearing names nest one level deeper -- `AMGT-rk-23`'s class),
   `W32-S4` (`lib/research/peers/universe.py`'s cache default sits inside a worker-numbered deliverables folder).
8. Headless authenticated capture blocked as a class (`W31-S3`) -- the disarm route is Andrew's (s.4).
9. The 43-row historical disarm-owner backlog (rounds 1-12), unchanged.
10. Timing, from the CTO's own intake `e3af87b212`: Andrew's word is *no PRD addendum until every panel brief is
    in* -- the CTO's ROUND_ANALYSIS.round13 may therefore wait on the Lead Panel series; this seat cuts nothing
    for round 14 before that analysis exists (LD-0521).

## 7. What this seat asks of L9/L10

Grade round 13 on the rulings already on file (s.2), disposition `W31-S3` and the W32 rows, carry s.3-s.6 into
the slug as adjudicator-level items, and send the ONE slug to `1.0.0_SA_CTO~Z`. Nothing is cut for round 14 before
the slug and the analysis (LD-0521). This seat's next act on this project is the recut, when the analysis lands.

Push state: LOCAL on SITEZ (workspace); portal `625a0888` on `origin/DEV` (ls-remote read by the integrator).
