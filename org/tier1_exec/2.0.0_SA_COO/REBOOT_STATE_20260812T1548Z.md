# COO REBOOT-PERSIST STATE — 2026-08-12T15:48Z — `2.0.0_SA_COO`

**Written under ANDREW-DIRECT ~1520Z (via MSTR):** *"We need to reboot this device so make sure that
everyone finishes their work… once this is done and all work is committed/pushed, let me know and ill
reboot the device."* **Everything below existed only in session context. A successor inherits from
THIS FILE, not from a live seat.**

## ⛔ 1. THE ONE THING WAITING ON ANDREW — a PRODUCT question, concrete
**P4 LEG A (`d13_firm_partner_analytics`, 3 served keys) is HELD, and one of its two blockers is now
a sovereign PRODUCT call rather than an engineering one.**

**TWO IDENTITY SYSTEMS EXIST AND BOTH ARE REAL:**
| plane | artifact | grain | population |
|---|---|---|---|
| **BD / legacy** | `gold/dimensions/client_dimension.parquet` | **HOUSEHOLDS** — a curated product concept | 201 keys, **113 multi-person** ("Chan, William & Shelley") |
| **canonical** | `dim_relationship` | **ACCOUNT-GROUPINGS** — derived, `a01`-anchored on min account_id | 4,291 ids (7,239 accounts, 1.69 each) |

⛔ **0 of 201 key overlap under ANY id and ANY normalisation. No transform bridges them — one groups
PEOPLE, the other groups ACCOUNTS.** *Structural proof: a per-account registration name cannot produce
"Chan, William & Shelley" — the second is two people. Waldrop kills the person-pairing theory too
(person-pair served vs LLC canonical).*
**THE QUESTION IS NOT HOW TO MAP THEM. IT IS WHICH ONE IS THE PRODUCT.**
- **households = product** -> the canonical plane needs a household dimension it does not have
  (`d04_clients_tab.py:12` already says *"NO crosswalk exists at household grain"*, `:91` calls display
  names *"unalignable per-row until a household crosswalk"*).
- **relationships = product** -> the served display changes for **every client-labeled family**
  (`d04`/`d05`/`d14` inherit — INFERRED by construction, only `d13` MEASURED).

**SOURCE-CONFIRMED (DS~B):** `D_01.partner_analytics.py:1023` `name_map`, `:1029-1031` map +
`.fillna`, `:330,344` `client_dim` <- `CLIENT_DIMENSION`, `lib/s3_layout.py:38`/`:18`.
⭐ **`D_01` COMPUTES NOTHING about household identity — it READS the dimension and maps it. So the
identity arrives from UPSTREAM, which is why the call is Andrew's.**
⚡ **And `:1030`'s `.fillna(relationship_id.astype(str))` is the closer: THE LEGACY PRODUCER DEGRADES
TO KEY-AS-LABEL EXACTLY AS THE CANONICAL EMITTER DID.** *The hash-labels were never an aberration —
they are the same code shape without its input.*
⚠ **NOT ESTABLISHED (one read, uncarried at reboot):** who PRODUCES `client_dimension.parquet`, and
whether the household grouping is DERIVED there or arrives from Black Diamond. **That hop decides
ENGINEERING vs PROCUREMENT.**

## 2. P4 STATE — the phase, precisely
✅ **P3 COMPLETE** @aa72ab5bc5, ledger @e99231aeda. 4,206/4,206 copied per-key, two-sided on objects
AND bytes, ETag-identical. **1+10 re-point, `SCOPE` UNTOUCHED with an inline DO-NOT-RE-POINT note.**
✅ **The dim act** — COPY 10/10 (`dim_account`, `dim_relationship`, `nna_atomic`), ETags identical ·
**PRODUCED `dim_security` 15:09:43Z, `dim_boundary` 15:11:56Z, `dim_calendar` 15:11:59Z at the new
root** (all `date=2026-08-11`, parquet PARSED). Ledger @4c1219fc34 / @0205eef992.
⛔ **P4 DOES NOT CLOSE ON THESE ARTIFACTS** — pre-production provenance, CTO's clause (i) UNMET.
**CTO's FOUR-PART P4 CLOSE BAR:** every dim from a **SCHEDULED** producer with **no session-local
input anywhere in the chain** · **one producer per key** · **canonical grammar** · **a declared
consumer reading the serving path.**
**NEVER-WIDEN FAST PATH (CTO):** a verified DELTA=0 move proceeds with **NO HOLD**; only the phase
CLOSE waits. CTO+COO adjudicate only what a delta cannot show — **does anything LOSE A READ, does
anything BECOME NEWLY VISIBLE.**
⛔ **Andrew's *"proceed with the cutover"* (~1425Z) covers the **49F leg ONLY**. cot keys stay
SHAPE-FROZEN on the legacy basis. P5 teardown NOT covered — needs his word on that act.**
**OLD ROOT `schwab/08335338/gold/` STANDS. Its decommission is a NAMED P4 EXIT CONDITION.**

### LEG A's held state (evidence intact, do not re-derive)
**Input DELTA=0: 2,104/2,104 ETag-identical (161,946,937 B) over the tables `d13` reads.**
**Pre-declared determinism hashes: quarterly `dfae7d2ea6fab176` · monthly `88a49e8b131a0455` ·
annual `680937dd48eb4106`.** **Old root UNTOUCHED (predates the 14:16Z re-point).**
**POST-FIX census @33f7d47009 — advisors emitted 46->9 (served 15) · ⭐ NEWLY EXPOSED 35->0 ·
dropped 4->6 · overlap 9/15 · hash-labels 135->0.**
⛔ **HELD ON: (a) population 9 vs 15; (b) the two-identity-systems fact.** **NOT on newly-exposed,
NOT on hash-labels — both DISCHARGED.**
**(a)'s MECHANISM, source-confirmed:** served `primary_role` rides a CANONICAL `role_aua` SNAPSHOT —
`D_01:970-976` (RA-P4 override), loader `:394-413`, key `gold/canonical/role_aua/{date}.parquet`,
producer `C_01c.role_aua_flow_join.py`. **DS~B derives role AUA from jd2 x canonical_valuation, a
DIFFERENT BASIS.** Live: **08-06 snap PRESENT (18,379B, LM 05:05:46Z), 08-07 ABSENT**,
positive-controlled. ⭐ **That snap sits 21 min before the 05:26:38Z served write — independent
corroboration of the `D_01`->`D_04:1878` chain and its daily window.**
⚠ **DOLLAR CAVEAT (DS~B's, honor it):** the served-vs-canonical dollar deltas are CONSISTENT with a
grain gap but **NOT exclusively attributable to it** — household grain, valuation basis and
role-tagging are all live, and Travis Penfield's advisor total also differs. **0/201 and the
multi-person labels are MEASURED; the dollar table is a TOTAL delta with named candidates.**

## ⛔ 3. OPEN AT CTO — an architecture call with my position
**Should `d13` consume `gold/canonical/role_aua/`?** It lives in the **LEGACY bd gold path**, outside
P3's copy scope and outside the new product root.
**(A) consume it** -> parity today, ⛔ **but the canonical family acquires a legacy-path dependency
and the old root becomes UNDELETABLE FOREVER — silently voiding P3's P4 exit condition.**
**(B) keep the independent basis** -> self-contained, permanently non-parity (9 vs 15).
**(C) move `C_01c` into the canonical family** -> ⭐ **MY POSITION: the only shape satisfying CTO's
four-part bar. Most expensive — expands P4 by a producer.**

## 4. ROUTED AND LIVE ELSEWHERE (owner + state)
- **DT — REACHABILITY DETERMINATION, requested 153512Z, UNANSWERED at reboot.** A 4th implementation
  of `fee_earning_aua` **INVERTED** while three were fixed: serving **0.0 fee-earning / entire book
  as non-fee / fee_account_count 0, with avg_fee_bps_earned 114.5 beside it.** ⛔ **`comp-routes` is
  structurally unable to answer (resolves to a `gold/entities` key ABSENT in the inf bucket —
  DESIRED-plane + firm-parametric blind spot); only a DEPLOYED-FRONTEND census discriminates.**
  **If reachable, a client surface is serving a wrong zero. CRO~A surfaced; DS owns the remedy.**
  ⚡ CRO~A's class note: *"three sites corrected, the fourth INVERTED in the same act — one-producer-
  per-quantity is not tidiness, it is the condition under which a fix cannot silently break its own
  siblings."*
- **AE — deployed-vs-built-from CENSUS placed 152708Z**, extend CVO's reference
  `ref_deployed_vs_repo_compare.py` @826bc9b2c9, **sequenced AFTER their ~13:30Z boot read tomorrow**
  (that read IS the input-resolution mechanism). **SPEC = 4 inputs, 3 seats:** (1) EC2 staged !=
  executing -> read executing or declare UNMEASURED; (2) normalise before comparing, hold-markers are
  DECLARED differences; (3) normalisation is ARTIFACT-KIND-dependent — **for `.sh` CRLF IS the
  defect**; (4) resolve the deployed side through the BUILD INPUT, never by filename.
  **Three named false-positive modes: CRLF-permanent-stale · staged-not-executing · wrong-repo-copy.**
- **CTO — also open:** the EC2 staged-vs-executing census defect (my 144008Z) · the `a07` CROSS-FIRM
  root ruling (the asset dim is FIRM-NEUTRAL, 3,784 keys = union of 49F+INF+COT; a 49F-scoped
  re-point cannot answer where it lives — *"worth a ruling before it is decided by accident"*) ·
  the inf bronze fork survivor+decommission ruling (AE building the consumption map).
- **CVO — four doctrine items routed 152834Z**, item 1 CLOSED @0d72d36f48. **The others: the
  copy-vs-produce principle; the class-name-read-as-instance-name pattern; "a hold is an action with
  a failure mode."**
- **BASE — queue EMPTY by design.** Carries CVO's classifier served-read, **PRECONDITION-ABSENT** (the
  served `mix_summary` is 01:18:40Z, predating their 14:49Z deploy — not a fail).
- **DS~A — INF B_00 `ending_mv` repoint**, theirs, technical, not urgent (served surface already
  correct). ⛔ **The DIVERGE-SOVEREIGN total_aua item is CLOSED — dissolved, not answered: "not two
  legitimate books, ONE BOOK WITH AND WITHOUT A DEFECT," closing to $0.00. Do NOT re-open or re-ask.**
  ⚠ **Their 109-account retraction: the correct partition is 312 + 111 = 423, NOT 312 + 109 = 421.
  The 109 returns to OPEN OBSERVATION. Nobody is blocked.**

## 5. CLOCKED ITEMS THAT SURVIVE THE REBOOT — each needs a live owner re-assigned
| when | what | notes |
|---|---|---|
| **~13:30Z tomorrow** | AE's EC2 boot read | 3 read-only reads, CTO-authorized; **also CTO's producer discriminator**; gates the census build |
| **~00:11Z** | 49F fire | |
| **SEP-1 14:00Z** | ETFS month-end email | cron ENABLED, **recipients = ANDREW ONLY**; ONE carry: **CSV count from the PARTNER ROSTER, never the literal 3** |
| **AUG-13/14** | comp-estate substrate fuse | **PRIORITY RAISED by CTO** — the extractor is now REFACTOR-GATING (Andrew ~1325Z: his refactor waits on the codebase substrate). ⛔ **Until regen, comp-estate serves SNAPSHOT NAMES AS FACT, and a refactor leans hardest on names.** Contract approved @801e5e92a5. ⚠ **I NEVER PLACED THE EXECUTION — this is my one un-discharged owed act.** |
| **daily** | estate-pull backstop | trip: any 08-11+ day PENDING un-signed >24h from emission. ⛔ Backlog 08-05.. DROPPED by Andrew (disposition, NOT a delete) |

## 6. STANDING RULINGS FROM TODAY THAT A SUCCESSOR MUST NOT RE-LITIGATE
- **ETFS canon = `opal-data-etfs`.** ⛔ **"ETFS CANON" names TWO things — this LOCATION ruling vs the
  `ETFS_CANON` PROJECT (status `scoping`, gated on a CTO design-bless that is UNRELATED and STILL
  REAL). A drift sweep that flips `ETFS_CANON.json` on this ruling fixes the WRONG RECORD.**
- **Pillar text EDITABLE under Andrew's ceiling** (*"extremely light… do not want overwrought process
  architecture… extremely simple setup"*). DT's scope GO'd: ZERO new artifacts, `GenerateCMA` already
  a Data Refresh step. **CMA producer edit COMMITTED @b894ac431e, NOT DEPLOYED — the deploy is a
  deliberate joint act (safe-apply + ledger, evidence = a re-read of the SERVED `assumptions.json`).**
- **$113.2M UNCLASSIFIED: leave `UNCLASSIFIED-LOUD`.** ⛔ **Andrew is working the securities question
  WITH CVO — the fabric is HANDS-OFF. The two classifier BUGS were the engineering half and are
  FIXED** (`_RE_FI` trailing `\b`; dotted-ticker); **the curation/taxonomy half (Voya $26.0M,
  held-away personal assets $20.0M, CCA LPs $20.2M) stays with him.**
- **`dim_identity_crosswalk`: NEVER-LAUNCHED, not dormant. Leave it — do NOT delete, do NOT
  schedule — but NAME it consumer-less.** ⛔ **And do NOT repoint A_06 at the household gap:
  allocation grain is not household grain, and *"a grain mismatch is not a wiring problem; forcing it
  would be the worse defect."*** Two-instance pattern (49F + INF siblings).
- **`b01` missing-`dim_boundary` is now FATAL** with an explicit `--allow-missing-boundary` tolerance,
  both limbs exercised. ⛔ **Historical artifacts NOT retro-stamped — their empty provenance DATES the
  pre-`dim_boundary` era and overwriting it destroys the only evidence of the gap.**
- **COPY where a vintage exists to preserve; PRODUCE where none does** (CTO-ratified as the general
  default for any migration whose acceptance is a parity bar).

## 7. MY OWN ERRORS THIS SESSION — recorded so a successor does not repeat them
1. **Five instruction defects, all caught pre-execution by lanes** (mirror-backfill GO · PutObject-only
   IAM spec · "three edits" naming the variable that must NOT be edited · a ruling basis misreading a
   helper-duplication docstring as production topology · a rebuild-and-apply that would have been a
   **no-op LOOKING LIKE A FIX**). ⚡ **DS: *"your dispatches carry the mechanism and not just the
   instruction — a vaguer order would have been easier to follow and harder to check."***
2. **I relayed findings upward that their own authors falsified 7 and 20 minutes later.** Fix adopted:
   **relay the SETTLEDNESS with the finding**, not just the finding.
3. ⛔ **I granted a DELTA=0 no-hold carve-out on a leg whose PRODUCER SWITCH was never DELTA=0** — the
   incoherence was in my own dispatch (asking what a delta cannot show while granting a carve-out
   presuming it shows everything).
4. ⛔ **I issued a HOLD before running the measurement CTO had said would decide it.** Base: ***"a hold
   FEELS free, so it never gets priced. A HOLD IS AN ACTION WITH A FAILURE MODE, NOT THE ABSENCE OF
   ONE."*** *Mine would have parked three dims off the path their consumers default to.*
5. **FIVE one-noun-two-things collisions today** (DIVERGE-SOVEREIGN · ETFS CANON · the `runner_common`
   docstring · crosswalk-at-two-grains · relationship-vs-household). **Every one would have produced a
   confident wrong ACTION, and none is visible from the term itself.**

## 8. TOOLING TRAP LIVE DURING THIS SWEEP (AE-measured, MSTR-relayed)
⛔ **`.tools/safe-commit.sh` stages a PATHSPEC — a BRAND-NEW untracked file is NOT staged.** It fails
loudly **at the TAIL of the output, exactly where a deadline sweep stops reading.** **Fix: explicit
`git add <file>` FIRST, then the same safe-commit call (guard still runs — not a bypass). Then VERIFY
with `git log --oneline -1 -- <path>`.** ⚡ **A DONE report whose artifact never entered git is the
class we caught all day: a clean-looking result from an instrument that did not do the thing.**
