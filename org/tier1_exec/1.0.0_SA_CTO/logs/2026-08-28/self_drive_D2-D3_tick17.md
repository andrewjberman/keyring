# /self-drive D2 & D3 — tick 17 (2026-08-28 19:50Z) — state: ARMED

Covers tick 17 (tick 16 logged @eb26d28015). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: an ARMED-candidate disarmed with a
named owner, one law-file line landed and broadcast, the campaign's first per-100 report with its
send-plane reconciliation, and the 04:35Z acceptance pre-registered at two seats on distinct planes.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342, 0 claimed-not-member. Push: all
six of this seat's commits today are ON origin (@2afd4ddd4e, ancestry after fetch); the base seats
are OFF the window OPEN/CLOSE frames on Andrew's "do not bother them" (MSTR 78901) — the two-limb
CLOSE oracle + a newest-MSTR-frame read before any `safe-commit` is this seat's standing control.

## Calls (§1-2)

**Zero.** No adjudicable, no RESERVED.

## Verdicts / rulings since tick 16 (§3)

- **Issuer records (COO 78819):** TO-A4-AEC AC1-3/5 MET on the issuer's own read-back; AC4 =
  the 04:35Z fire; **~K KEPT as the fire reader for BOTH AC4 rows** (TO-A4-AEC's and TO-A3-AE's,
  whose seat is released). TO-R2-DS AC0 recorded; serving-gate branch applies; b-2 proceeds.
  **CVO 78828** confirmed TO-A4-AEC AC1/2/3/5 on the live plane (third instrument; the corrected
  stagger is in the deployed rule description — the right carrier); **CVO 78824** corroborated
  DS~V's two census items and corrected its own 78644 ground on grain (the "DE blocked" premise
  narrows to one card; verdict (a) stands on its other grounds).
- **ARMED-candidate (CVO 78829 ← ~K 78799 item 1): `record-terraform-deploy.sh` half-writes the
  source map under bun on this device and still commits "ci: record deploy".** Corroborated on the
  RECORD plane: at 17db393744 `artifact_sha256` moved while `last_deployed_commit` /
  `last_deployed_at` did not — and ~K's sharper fact (78890): the sha line was SWEPT from
  `build-and-upload.sh`'s tree write, not written by the record tool; a moving sha is not evidence
  the tool ran. **DISARM OWNER NAMED (78837): `0.8.0_AE_CloudComp`** — the guards' owner
  (`git_bash_resolver.py` / `msys_argv_guard.py`); the fix is the caller order at `:182` (prefer
  python3 over the native bun) or routing through the guard, plus the stale docstring; obligations
  carrier row 7 **item (k)** (COO 78861 — the letter is (k); my "(l)" was a citation slip, reconciled
  by COO). **INTERIM executor check** stated: after any record run, confirm all THREE source-map
  fields moved, hand-correct and say so in the ledger's L1. ~K ran it retroactively on its own deploy
  (78843): 3 of 3 moved + content read (`git log -1 -- <file>` == the recorded commit) + live read
  (CodeSha256 == artifact_sha256). Its L1 was silent (the half-write was found after close) →
  **RULED (78857 = COO 78861, one voice): an explicit dated ADDENDUM block below the CLOSE, never a
  silent edit of a closed leg** — landed @6c67b9c170, 61 insertions / 0 deletions, the pre-append
  5,604-byte prefix re-hashing identically, `deploy_ledger.py check` still CLOSED. DISARMED ≠
  REMEDIATED.
- **Law-file edit (mine): `org/XXX.md` A.2 gains one additive paragraph @5fc6086005** — the
  STALE-BASELINE + UNCOVERED-AUDIT-LOG pair are OWNED-UNTIL-rv0057-f001 (exec A.2 also defers;
  COO carrier row 3 d+e; re-raise 08-30); a seat that sees them does not re-file. Three seats had
  re-filed the pair in one day (COO, ~K, DS~V; CVO named the carrier gap). Diff verified as one
  hunk before the pathspec commit; broadcast 6 of 6 (78846-78851) with push state; MSTR owns the
  file and relays cross-fabric. ON origin @2afd4ddd4e.
- **04:35Z acceptance PRE-REGISTERED at two seats on distinct planes:** ~K's executor read (78835:
  four arms — trigger log with `runner=insurance` AND the `{"leg":"insurance"}` payload as the
  discriminator; reporting-pull log `BD49F-INSURANCE` to the attested total with no
  `BD49F-REPORTING` line; head-object per page with the denominator; the same day's 00:00Z main
  run as negative control; refusal path via 0.6.0's RequestId offer; no self-authorised fix);
  **CVO's certifying read (78880 @2afd4ddd4e) on FOUR planes the executor does not use** — the
  trigger's marker object by S3 VERSION with `runner=insurance` (neighbouring versions `main`/`fees`
  as the control), CloudWatch METRICS per function (reporting-pull Invocations 1 / Errors 0; chain
  runners 0; 00:00-00:10Z as control), the bronze artifact plane against an 11-object baseline, the
  reporting prefix gaining nothing — with a MECE outcome vocabulary PASS / NOT-FIRED / REFUSED /
  PARTIAL / CONTAMINATED. Divergence between the reads is the finding; neither seat reconciles.
- **Campaign PER-100 #1 (~L 78907):** ledger @0bc0e8e588 — **102 of 534** ARTIFACT-COMPLETE at the
  CITED HASH (104 lines / 102 distinct dates, newest 2024-11-27; 2 superseded in place), 0
  non-complete, 0 HARD-STOP. GRAIN CORRECTION by COO 78918, confirmed by ~L: the report's
  "103 lines / 101 dates" was counted from the working tree BEFORE the commit while the live writer
  appended; from per-100 #2 every number derives from `git show <hash>:<ledger>` after the commit,
  with both the commit and the send-plane snapshot timestamps printed. **The send plane printed
  beside the rows RECONCILES both ways** (131 commands; 106 campaign sends over 102 dates; five
  sends without a row, all five explained — two V14-2 exercises, the 07-10 TimedOut re-driven, the
  10-04 Cancelled, one in flight — ZERO unexplained); 2c8385ec vindicates CVO's "the ledger is not
  a send log" on its own instrument. 0 foreign sends today (the 14 Failed are 08-26/27, Andrew's).
  105.6s median; ~12.7h remaining → arrives at the 12:45Z pause with ~100-150 outstanding; the
  four-item pause bundle lands with the campaign live behind it. Next boundary date 200.
- **Window frames:** MSTR 78901 — not a delivery defect; base CTO/COO/CVO are off the recipient
  lists since window 16 on Andrew's word; per-recipient maps show the serials ABSENT, not QUEUED;
  whether base seats return to the frames is at Andrew via MSTR.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @2afd4ddd4e, ls-remote read 19:50Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · ledger read · `git diff`
  hunk count on XXX.md before the pathspec commit (1 hunk) · `git merge-base --is-ancestor` ×6
  after fetch · `git ls-remote` + MERGE_HEAD.
