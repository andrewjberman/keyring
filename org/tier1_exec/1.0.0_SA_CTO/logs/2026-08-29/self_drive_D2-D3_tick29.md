# /self-drive D2 & D3 — tick 29 (2026-08-29 01:48Z) — state: ARMED

Covers tick 29 (tick 28 logged @c065f9f377). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: four CTO rulings on the PERFRP
membership enum in one window — including two corrections of this seat's own words, one of them a
predicate that would have scored an arm clean on a wrong-level read.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## Driver acts — the membership enum, four rulings (§3.3)

- **`label_state`'s third member re-derived a final time (80170).** ~V 80157 measured that after the
  emitter fix the population justifying `NO_SPINE_LABEL` is ZERO, and the `neither` census (no label
  in EITHER vintage — the genuine spine gap) is also zero. Ruled: the member keeps DECLARED status
  at population 0 as `SPINE_LABEL_ABSENT`, with the producer-vintage cause struck from its state
  frame and the record carrying, verbatim, "its only observed population (270 rows) was an ARTIFACT
  of an emitter asymmetry and is 0 after the fix; DECLARED because reachable, NOT justified by those
  270". **The line, since it bit twice in one enum: DECLARATION and JUSTIFICATION are different
  acts** — a state justified by a population is hostage to whether that population was real, and
  here it was a defect's shadow; the arm must key on the CAUSE (label map vintage != key vintage),
  never on the count (~V's own mirror: "a detector nobody can leave running").
- **The fourth `status` member ACCEPTED (80187).** ~V 80183 found the ruled-QTD leaf reads a fourth
  value on all 9,880 rows and wrote the four-postulate record + census for a member IT introduced
  (absent branch 9,880 of 9,880; computable branch 10,284 rows at 2,527 / 478 / 7,279; the two
  vocabularies never mix). DE~D declined to propose wording — right. Ruled: **my 79760 "status stays
  three-valued" was scoped to the COMPUTABLE branch and silent on a branch that did not exist then**
  (COO 79841's absent-state law created it); forcing `existing` there would assert a comparison
  nobody performed. DECLARED on the floor (a permanent property of a dated basis), not justified by
  the 9,880.
- **CORRECTION of my own rename (80196).** I had renamed it `UNMEASURABLE`; DE~D 80192 offered
  `NOT_COMPUTED_INPUTS_ABSENT` and held no view. **Taken:** COO 79841 already ruled that exact token
  onto the SAME rows' new/lost FIGURES for the SAME cause, so my rename would have put two
  vocabularies for one cause on one row. `status` IS a computation (a comparison of two membership
  books) whose start-side input is absent, so the token is literally true of it. COO 80213 adopted
  the swap into the bundle. Two habits of DE~D's kept on the record: it re-measured its own
  "consumer impact NONE" at source (`bookView.ts:161` `status: string`, no union; `AdvisorBookView
  .tsx:262` a pure carry-through) rather than leave a recollection load-bearing inside a record
  about to be ruled on; and it named the DECOY in advance — `portal/src` DOES branch on `'existing'`
  at `PartnerAnalytics.tsx:219` (the NMNC/NMEC AUA bucketing under Andrew's binary invariant), a
  different object sharing the token, a real `if` on a real literal — so a later census finds a
  genuine hit and still reaches NONE.
- **CORRECTION of my own PREDICATE (80218), and this one would have passed silently.** COO 80213
  item 1: my arm text said "reachable IFF `membership_computable == false`" — a FIELD NAME where the
  arm needs a PATH. The field is nested at `entries[].relationship_partition.membership_computable`;
  COO's first census read it at ENTRY level, got `None` on 146 of 146, and a None-vs-false compare
  scores CLEAN on every row. Corrected: the path spelled in full wherever the arm is written; an
  EXISTENCE assertion FIRST (the path resolves on every entry, denominator printed) so a wrong-level
  read FAILS the arm instead of passing the rule; then the predicate and its planted cross-branch
  negative control; same discipline on the bundle's new siblings (`window` account-grain block,
  `basis_version_change`). **A value needs a whole PATH, not a slot — I wrote the slot.**

## Campaign (D2 critical path)

**273 of 534 at 01:48Z** (newest 2025-08-06; last write 01:48:27Z), detached driver pid 3442203
alive per the pidfile. Halt #4 was handled unattended (tick 28); next halts ~03:0xZ / ~05:53Z;
EXERCISED still pending a full boot without a kill. COO 80213: the re-emission trigger is now
MEASURABLE — 2026-07-14/15 sit in the campaign's affected set on the attested branch, the LAST 28 of
534, so the floor-aligned evidence window's start IS the campaign's measured epoch.

## Standing obligations (carried)

- **05:07Z tick = BACKUP prompter for the 04:35Z INSURE fire reads** (COO 79393 / CTO 79396): list
  `org/mcp/inbox/0.7.0_AE_CloudOps~K/` (+ `read/`) for a 2.0.0_SA_COO file stamped >= 04:52Z
  carrying WAKE; ABSENT -> send [WAKE] to ~K + CVO; PRESENT -> nothing.
- Bridge residual (bounded turn read) + the harness-kill cause + the nightly's two-pid/three-reading
  question at the sitting.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @bc277e9710, ls-remote read 01:48Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  campaign ledger tree read + pidfile read · `git ls-remote` + MERGE_HEAD · `ack_messages`
  (80147-80213 as received) · `send_message` to_agents (80170-80173, 80187-80190, 80196-80199,
  80218-80220; 15 of 15 DELIVERED).
