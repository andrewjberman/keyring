# AMGT_RESAPP round 14 -- L9 adjudication (`3.0.0_SA_CVO~Z`)

**Adjudicated:** 2026-09-21, post-reboot, at HEAD `f5da024c78` (SITEZ, LOCAL). Grounds: the COO's drain-end L8
packet (`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND14_L8_PACKET_20260919.md` @`5c5a839234`), this seat's
own pre-close working record (`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND14_L9_WORKING_RECORD_20260919_Z.md`,
opened 2026-09-19T06:4xZ, 1125 lines of graded checks), and the COO's post-reboot re-verification (msg 23905,
`[DRIVE AMGT_RESAPP tick 1]`).

**VINTAGE, independently re-measured, not taken on relay:** `git log --oneline 04d2e4b2f1..HEAD -- org/missions/D5/AMGT/AMGT_RESAPP/`
returns exactly ONE commit -- the packet commit itself (`5c5a839234`). Nothing in the AMGT_RESAPP tree moved
during the outage; the two-day HEAD advance (`04d2e4b2f1` -> `f5da024c78`) is other projects' traffic. This
corroborates msg 23905's own claim on a second instrument (a commit-range read vs. the COO's `--since` log)
rather than accepting it as read.

## 1. The one declared JUDGMENT criterion: `rk-61` AC2

**DISPOSITION: NEITHER PASS NOR A FAIL CHARGED TO `rk-61`.** AC2 ("the battery passes, 0 failed") reads
literal evidence of "2 failed, 163 passed" and a PASS status. This is not the forge signature it resembles.

Grounds (working record s.3c, re-affirmed): the evidence is the most rigorous in the round on this point --
it prints the failures verbatim, runs a GRAIN check proving the two failures are disjoint from `rk-61`'s own
diff, and reproduces both failures independently on the shared tree at a named commit. Root cause (s.4h,
independently verified by this seat at HEAD): `rk-43` deliberately and correctly retired the two-value
`NOT_CONFIRMED_NOTHING_FOUND` sentence-parsed contract for a six-value field-only one; the two failing tests
assert the superseded contract. `rk-43` held no grant on the test file; of the five orders whose `<paths>`
touch `lib/research/api/tests/`, two carry WHOLE-DIRECTORY grants (`rk-37` PENDING at packet time, `rk-53`
complete) -- so the repair is **UNASSIGNED, not ungrantable.**

**L9 RULING:** AC2 stopped being a mechanical criterion the moment its literal bar became unmeetable for
reasons entirely outside the cell's own diff -- at that point it became a judgment call, which is why it is
graded here rather than self-graded (it was NOT self-graded; the worker's own row `W61-S1` states the
opposite, literal-terms FAIL, and files it honestly rather than papering over the disagreement). `rk-61` is
accountable for its own 9 of 9 new arms, all green, and is NOT accountable for a pre-existing, orphaned-grant
test failure it did not cause. **`rk-61` closes clean on this criterion.**

**CARRIED FORWARD, unresolved, and load-bearing for the round-14 analysis:** the repair itself remains
unassigned. Every later cell carrying a "the battery is green" criterion inherits this literal FAIL until
someone with a grant on `lib/research/api/tests/test_generation_and_pool_routes.py` fixes it. Naming an owner
for that one-line repair is a round-15 item, not a round-14 blocker.

## 2. Round-14 terminality -- confirmed, not re-measured from scratch

The COO's repaired-criterion map (packet s.2) and live-plane ledger (packet s.3) are accepted as measured:
this seat's own working record independently re-ran or re-derived the load-bearing claims in eleven of the
COO's cells (rk-31, rk-34, rk-40, rk-41, rk-33, rk-53, rk-49/48, rk-39, rk-61, rk-58, rk-60) across sections
4a-4t and 4 of this seat's own working notes, on instruments different from the worker's self-report in every
case (S3 object listings, live CodeSha256 reads, branch-scoped `git show`, AST parses, independent pytest
runs). No contradiction was found between the COO's packet and this seat's own measurement on any of those
eleven. **26 of 31 cells TERMINAL, confirmed.**

**The five open cells are graded per the COO's ask, and this seat concurs with the reasoning:**

| cell(s) | held by | L9 grade |
|---|---|---|
| `rk-32` + chain P (`rk-50/51/52`) | the bucket/tenancy word | NOT terminal. Blocks the COUNT, not any cell's correctness -- `rk-33`'s own acceptance rows (packet s.2, this seat's working-record s.4g) show the registry gate correctly REFUSING bronze/silver to `opal-data-harvest` under current registry state (Rule 30 working as designed), and the fork is Andrew's, declined by this seat at tick 77 and again here. |
| `rk-48` AC4-AC6, `rk-49` AC3/AC4 | the Bright Data word (5 criteria across 2 cells, packet s.2/working-record s.4j/4s) | **TERMINAL-BY-DESIGN, per this seat's own 4m/4r reading, as the COO's packet asks.** Both cells refused rather than manufactured a green: no schema relaxation, no placeholder `ceo_profile`, no live SERP call without Andrew's per-use word. Graded `N/A-BY-CONSTRUCTION`/`UNVERIFIABLE`, not a failing criterion -- and named in those exact words (not "not applicable") per working-record s.4j's taxonomy point, so the slug reads an outstanding dependency rather than a closed question. |
| `rk-49` DRAIN (separately) | the rotate-or-rewrite word (a revealed credential in one local, unpushed commit on the `~50` branch, row `W50-S4`) | An INCIDENT, not an exposure -- the credential fired into a channel row. CONTAINED (working-record s.4t, re-verified: `git merge-base --is-ancestor 6b1fd76215 HEAD` still FALSE, `origin/SITEZ` still behind, zero occurrences of the value at any read this seat performed). Not this seat's to route or rotate; recorded as a distinct THIRD word from the other two, per this seat's own s.4m ruling that collapsing gates loses which answer unblocks which cell. |

**Net: 26 terminal, 5 held on three separately-named Andrew words, zero contradictions found between the
producer's packet and this seat's independent re-verification.**

## 3. A packet claim this seat could NOT independently corroborate -- named, not silently accepted

Packet s.5 lists `W58-S2, W47-S2, W53-S1, W60-S4` among rows "disarmed by this seat" (the COO). Checked
against the surprise channel's own disposition census (`_latest_dispositions`, the tool's own function, run
fresh at HEAD over all 27 carriers -- not a hand-rolled re-parse, per this seat's own s.4d rule) and by direct
`grep` for each id across every adjudication/remediation carrier in the project:

| row | census disposition | what this seat found |
|---|---|---|
| `W60-S2`, `W60-S4` | `UNDER_INVESTIGATION` (no adjudication/remediation entry exists for either id, anywhere in the tree) | **SUBSTANCE CONFIRMED REPAIRED.** Two repair commits, `fae9316edb` and `928352b513`, land exactly on these rows' own described defects (WinError 193 on the tsc shim; the comparison call anchoring the wrong worktree list), and the packet's own cell table records "AC3 re-run after the second repair" as `rk-60`'s second instrument. **This is a HOUSEKEEPING GAP, not a standing hazard:** the code is fixed and re-verified, but no closing adjudication/remediation row was ever filed, so a census run against the surprise channel alone (rather than against the repaired-criterion map) would report these as open. Owed: `2.0.0_SA_COO~Z` files the closing row citing the two repair commits. Not blocking -- the underlying claim is true.|
| `W53-S1` | `UNDER_INVESTIGATION` | **SUBSTANTIVELY RESOLVED, per this seat's own prior analysis (working-record s.4e), not yet formally closed.** The chain L never-widen pair IS on file in the estate (CTO half @`ce9231d095`); only the worker's stale worktree lacked it, and `rk-53` correctly ran only the read-only/in-process criteria the absent-half path permits. Disarm path named already: `2.0.0_SA_COO~Z` citing row `Z-S178`. No new pair is owed. |
| `W47-S2` | `UNDER_INVESTIGATION`, class `OBSERVATION` | **The packet's "disarmed" is better read as "carried" -- this seat does not treat the difference as a defect.** `OBSERVATION` class does not gate a TO's `complete` flip the way `BLOCKING` does, and the row's own content is a discrimination note (a test passes coincidentally because the fixture's pool date and the name's own as_of happen to coincide), not an open hazard needing repair before close. |
| `W58-S2` | (not claimed disarmed on a careful re-read; packet's own parenthetical says "carried") | Consistent with the packet. The GATE (x)/(rk-55 vs rk-58) contradiction this row names is a real cross-order design finding for the CTO, not a round-14 defect -- carried below. |

**L9 RULING on this section:** none of the four reclassifies any cell's terminality. Three of the four
(`W60-S2`, `W60-S4`, `W53-S1`) are substantively sound and only administratively open; the fourth (`W47-S2`)
was never a blocking claim. This seat verified the packet's row-disposition claims against the surprise
channel's own instrument rather than accepting them on relay (Rule 22 GRAIN/DISCRIMINATION), found the
substance correct in every case, and is naming the one real gap -- unfiled closing rows -- as a completeness
item rather than reopening anything.

## 4. Findings carried to the round-14 analysis

This seat ratifies the COO's eight findings (packet s.6) without qualification -- each was independently
checked against this seat's own working record and none conflicts. Adding, from this seat's own grading
(full detail in the working record; stated here once each, not re-derived):

1. **The criterion-defect class is round 14's dominant defect shape**, and it has a sharp subtype: a probe
   that reads a wrong key returns `None`/a constant for every input and passes silently, rather than
   erroring -- `W38-S3`'s `model_status` read is the clean instance. A wrong access path does not fail loud;
   it reads as data.
2. **A bind added at re-signature changes the act without changing the prose that describes it, three times
   in one round** (`W43-S1`, `W49-S4`, and this seat's own s.4f on `rk-34`'s rollback disagreement). Every
   worker so far chose the later authorizing text correctly, but each had to choose, unreviewed. The remedy
   is that a re-signature bind must carry its edit to every clause it contradicts, in the same act.
3. **A sign-off whose text is date-relative or input-relative has a shelf life that expires silently**
   (`rk-31` survived an overnight boundary because its half named the act's SHAPE from the producer's rule;
   `rk-45`/`W47-S1` did not, because its half named the INPUT's state at signing). Doctrine-worthy beyond this
   round: a half should be graded on which of the two it read from, at signing.
4. **`W39-S2`: a guaranteed, currently-silent data-loss defect, never fired.** `pull_consumer.py` calls
   `stage_pull` with 4 positional args against a 3-parameter signature (AST-verified) inside a `try/except`
   that marks FAILED and then unconditionally deletes the SQS message -- so the first real traffic through
   this consumer would silently destroy every enqueued pull request. Measured NEVER FIRED: the served
   `packs/` prefix carries exactly one `status.json`, written 19 minutes before the defective call site was
   committed, and nothing since. EXPOSURE, not incident; the remedy is one argument, but it is unassigned
   like the `rk-61` repair above and should not wait for the box-side consumer's first real run to be found.
5. **The two-writer schema edge (`rk-48` -> `rk-49`)** is a decomposition finding, not a round defect: a
   REQUIRED schema block whose only writer is a gated live arm blocks every later in-place rewrite of the
   same objects. The edge was right; the grain (cell vs. live arm) was wrong.
6. **One CLI, two idioms, one round:** `comp-secrets get ... --reveal` piped through `$(...)` cannot yield a
   usable key (four-line descriptor block, not a bare value); `rk-40` used the working form, `rk-49` did not
   and obtained its value another way at zero cost. Separately, `--json --reveal` silently falls through to
   the text block. Both are CLI-contract gaps, not worker defects, and both are named once each rather than
   charged to either cell.
7. **`W60-S3` (carried forward, unrepaired, correctly so):** a ruled, unconditional `git worktree prune`
   step reached outside its own cell and cleared an unrelated round-10 entry, directly contradicting its own
   criterion's expected end-state. Grade the RULE, not the worker: an unconditional prune has no cell
   boundary, and the criterion that names the end-state already knew it needed one. Not blocking round 14's
   close; worth a round-15 repair to the provisioning script's remove verb.
8. **`W58-S2` (carried forward):** GATE (x)'s one-issuer-per-round refusal is wired into `to-pipeline-gate.py`'s
   newly-added-set limbs only, and its missing-`<round>` branch refuses exactly the shape `rk-58`'s own
   direct-act minter emits by design. `rk-55` and `rk-58` land contradictory requirements on the same gate --
   a design contradiction for the CTO to resolve, not a round-14 blocker (nothing in round 14 needed the
   minter to admit a round-tagged order).

## 5. What this seat asks of L10, stated now

Full L10 (every TO terminal, every row dispositioned) cannot stamp while `rk-32`/chain P are held on the
bucket/tenancy word. This adjudication is the CVO's L9 pass on the 26 terminal cells, handed to the CTO as
input to the round-14 analysis per the COO's request (packet s.7) -- it is not a claim that round 14 has
closed. When the bucket/tenancy word lands, `2.0.0_SA_COO~Z` re-opens rk-32/chain P under its own pair
section; when the Bright Data word lands, `rk-48`'s live arm runs first, then `rk-49`'s second in-place
rewrite, each under its own signed pair, per this seat's own s.4m ruling already on file. The rotate/rewrite
word is Andrew's/AE's alone.

**Owed before the eventual full close, named so it is not invented under time pressure:** (a) `2.0.0_SA_COO~Z`
files the closing adjudication rows for `W60-S2`/`W60-S4` (section 3 above); (b) someone with a grant on
`lib/research/api/tests/test_generation_and_pool_routes.py` repairs the two orphaned test assertions (section
1); (c) `pull_consumer.py`'s arity defect (finding 4) gets a one-argument fix before that consumer's first
real traffic.

-- `3.0.0_SA_CVO~Z`
