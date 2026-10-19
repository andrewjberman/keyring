# NFRA_OPLGTW -- ROUND-45 ANALYSIS (L10 answer; the round-46 enrichment list)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-19 ~08:2xZ.
**Answers:** `2.0.0_SA_COO~O`'s slug, msg 35918, `deliverables/2.0.0_SA_COO~O/L10_SLUG_ROUND45.md`.
**Issuer:** `2.0.0_SA_COO~O`.

## 1. As read

- **The round is terminal:** 4 of 4 complete. `round-close-check` reads MAY-CLOSE. There are 0 BLOCKING and 2 ARMED (Z-W94-S2,
  Z-S177), both carried.
- **Live is `6b1a9bd292`.** Ledger batch13 CLOSED 07:44:53Z.
  - My OG-ap-48 CT1-CT4 are all MET.
  - The repeated 149/270 counts were verified by my own lake list: exactly 270 objects in each window (log @49c43bebc5).
  - It is landed on box/sitez by OG-ap-49.
- **Z-W155-S1 is disarmed on evidence** (OG-ev-12, row Z-S403):
  - the ALB access logs hold no 429 on 2026-10-18 (14,837 lines);
  - the only 429s on 10-17 to 10-19 are 26 lines at 17:21:43Z on 10-17, all answered by this service, against exactly ONE lake row
    (the first refusal writes and the 10 s fold takes the rest);
  - so the refusal writer works in the service.
  - The 10-18 identity 429 this seat saw never passed the ALB. Its origin layer is not established, because no log in the account
    keeps bodies. I accept UNDETERMINED for that one event: it touches no outcome.
- **Z-S402 is now audible:** the counter and WARN line are live, and the first window read 0. The row stays open until a window of
  production traffic is read.

## 2. Ruling -- a round-N analysis, no addendum

The ENDPOINT is unchanged. The audit plane's two holes (a silent sink, an unbounded put) are closed, and the refusal-row hazard is
disarmed. Round 46 is small on purpose: the remaining candidates are a comment and a re-read. Neither justifies a release of its own.

### The round-46 list (ONE issuance)

1. **OG-ev-13: re-read the audit lake leg after a full day of production traffic** (slug item 2; OG-ev-11 ranks 2-4; Z-S402).
   Read-only.
   - Over 24 hours from 2026-10-19 07:44:53Z (OG-ap-48's close), read:
     - the journal's `audit-lake WARN` lines and the running count they carry;
     - lake objects per hour against `POST /mcp` lines per hour.
   - **The wait is essential, and its reason is stated:** the outcome is "the lake leg holds under a day of real traffic". Only
     elapsed traffic produces it, and no act can manufacture production load honestly. The cell's GO is therefore no earlier than
     2026-10-20 07:45Z.
   - Output, a verdict:
     - `HOLDS`: 0 WARN lines, and lake/hour tracks POST/hour;
     - `FAILS_SEEN`: WARN lines, with class and count;
     - `UNDETERMINED`.
   - It also explains the 2026-10-19 02:00Z-03:00Z hour of 2,896 lake objects, about 7 times baseline, from my lake list. The
     explanation is a tool-name histogram for that hour (counts only).
   - On `HOLDS`, Z-S402 closes, and moving the put off the loop (OG-ev-11 rank 2) is not cut.

### Ruled, not cut

- **The retry-count comment (slug item 1):** keep TWO sends. A retry helps a transient error, and the worst case of about 10 s
  holds. The comment is corrected in the next release that touches `audit.py` for another reason, never as a release of its own
  (a deploy costs more than a wrong comment). `pr6.AC2` is unchanged.
- **`admin_people_access.py`** (slug item 3): carried, on 2.0.0_SA_COO~MP's written yes only. That seat is not live.
- **Mounting `family_depth`** (slug item 4): carried until an outcome needs the route.
- **Slug item 5, the watcher-gap claim:** 0.0.0_AB_MSTR~Z measured that mail landing in a watcher's expiry gap IS replayed at
  re-arm (msg 35900; a control file was emitted on the first poll; NFRA1's gap was about 14 s).
  - NFRA1's slow reads are the idle-at-input case.
  - The bounded `conin-nudge.ps1` covers it (MSTR @c0ef1646b3, my bounds: an idle seat only, fixed text).
  - No new cell.

### Where the project stands against its endpoint

- What this seat knows to stand between the project and CLOSED is **FWD-21: one real harvest call by a named Opal asset manager**
  (open-calls row 5b35).
  - That is an act only Andrew can do: he names the person, and the person makes the call.
  - No cell of this fabric can perform it.
- The issuer should list in its next slug every FWD that does not yet grade REALIZED, so that this seat can tell whether round 47
  has build work at all or waits on that act.

## Amendment A1 (2026-10-19 ~08:5xZ): the FWD state changes round 46

The source is 2.0.0_SA_COO~O's `deliverables/2.0.0_SA_COO~O/FWD_STATE_20261019.md` @b2096831dd (msg 35922). **No FWD reads REALIZED
in any record.** 8 are HELD since 2026-10-07, FWD-21 is NOT MET, FWD-20 is built but not exercised, and 11 are ungraded. Round 36
promised a grade of the 2026-10-13 grade read at round 37, and it was never given. That lapse is this seat's.

### Grades given now (CTO), from `deliverables/0.9.0_WK_NFRA_OPLGTW~66/GD1_GRADE_READ.json` @123bf2d8ec

- **FWD-1 to FWD-8: NOT_REALIZED.**
  - On every one, at least one arm is a person-act not yet run: the owner and member walkthrough.
  - `tests/acceptance/A_ROWS.json` reads **20 of 20 NOT_EXERCISED**: 14 rows have a person half, 5 are person-only.
  - Every machine arm carries `claim: inferred`, from offline fixtures, never a served read.
  - Named gaps, from the record:
    - FWD-1: no member walkthrough, no fresh connection by the pilot user;
    - FWD-4: 0 `delivery_finished`, no opened download;
    - FWD-6: no grant change or revocation run;
    - FWD-7: no controlled load;
    - FWD-8: the rollback arm needs the operator and Andrew's word.
  - **The walkthrough cannot start yet:** `WALKTHROUGH_PROTOCOL.md` section 1 requires two input records, and neither exists:
    - `G-C_CONTROLLED_IDENTITY_AND_GRANT.md` (the controlled walkthrough);
    - `G-E_PILOT_IDENTITY_AND_GRANT.md` (the pilot user's tenant and object id, and his grant).

### The round-46 list, amended (ONE issuance; replaces the one-cell list above)

1. **OG-ev-13: unchanged.** The 24-hour lake re-read; GO no earlier than 2026-10-20 07:45Z.
2. **OG-gd-2: grade read for FWD-10 to FWD-19 and FWD-22.** Read-only, in the shape of GD1.
   - Per FWD and per proof arm: `ran`, `claim` (`measured` / `inferred` / `absent`), evidence paths, and the owed act with its
     operator.
   - No grade word: the grade is this seat's, at the round-46 analysis.
3. **OG-cd-2: mount the `family_depth` route and apply its read IAM** (`family_depth_read_iam.tf`, through `safe-apply`).
   - Then OG-ap-50, a release under its own never-widen: a NEW served route, so the ask names the widening and the process-wide
     state.
   - Then ONE driven read for FWD-20 (proof by a served read, per the PRD's FWD-20 line).
   - FWD-20 is the outcome that needs the route, which round 45 carried the mount for.
4. **G-C: the controlled-identity and grant record.**
   - This seat writes it, as the CTO act that protocol names: the principal class, the approved grant revision, the operator.
   - It is due before the round-46 analysis.

### Listed for Andrew (acts only he can do; each is on the open-calls list)

- **G-E, the Schwab pilot.** Name the pilot user's work identity and approve his grant, and sit the owner walkthrough as owner
  with the pilot user as member (A1-A20, `WALKTHROUGH_PROTOCOL.md`).
  - Citation: a person's identity and an entitlement grant beyond the existing grants, plus his own participation.
  - This is what stands between FWD-1 to FWD-8 and a grade.
- **FWD-21:** row 5b35, unchanged.

## Amendment A2 (2026-10-19 ~09:3xZ): correcting A1 on G-C and G-E

**A1 was wrong on two points.** I read `WALKTHROUGH_PROTOCOL.md` section 1 without checking the rulings made since.

- **G-C (controlled identity) is RETIRED.**
  - It was retired by 1.0.0_SA_CTO~O ruling 28152, on Andrew-direct 2026-09-30 ~07:2xZ (the status tag of
    `task-orders/NFRA_OPLGTW.TO-OG-g-1.controlled-identity-and-grant.md`).
  - The evidence `deliverables/0.7.0_AE_CloudOps~OG/G-C_CONTROLLED_IDENTITY_AND_GRANT_EVIDENCE.md` @51b504a56c records 0 of 38
    internal users qualifying.
  - **A1's item 4 (this seat writes G-C) is withdrawn.**
- **The pilot principal's identity is already verified.** OG-g-2 is complete and wrote
  `deliverables/0.9.0_WK_NFRA_OPLGTW~23/IDENTITY_PILOT.json`, with AC2 matching the pilot oid to the host-side roster pair by hash.
  - A1's "name the pilot user's work identity" is withdrawn.
- **What actually remains for FWD-1 to FWD-8 is the person-acts themselves:**
  - the owner and member walkthrough (A1-A20, 20 of 20 NOT_EXERCISED);
  - the protocol's other person rows, such as a second signed-in account.
  - Andrew's act is to sit it as owner with the pilot user as member.
  - `WALKTHROUGH_PROTOCOL.md` section 1 should drop its G-C precondition. That is a protocol edit, and the issuer's to cut.
- Round-46 list: items 1-3 of A1 stand (OG-ev-13, OG-gd-2, OG-cd-2/OG-ap-50). Item 4 is withdrawn.
