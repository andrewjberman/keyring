# ANDREW-DIRECT 2026-09-13 ~18:4xZ -- /open-calls at 1.0.0_SA_CTO: all seven recs approved

**Received at:** the 1.0.0_SA_CTO terminal, in-session, before 18:50:06Z (the first act on it is stamped then).
**Recorded by:** `1.0.0_SA_CTO`, same turn.

## VERBATIM AND ENTIRE

> "recs approved"

It answered the seven-card `/open-calls` frame below, which is reproduced exactly as it was put to him. **Each card's
REC is now his ruling, in the words of that REC and no wider.**

## THE FRAME HE ANSWERED -- VERBATIM

```
OPEN CALLS AT ANDREW -- 1.0.0_SA_CTO (7 calls, 2026-09-13 ~16:5xZ)

BLOCKING (something waits on the word)

+-- CALL 1 of 7 ---------------------------------------------------+
  **Rebuild the firm-bucket fence so it keys on each role's firm, not on a hand-kept list of name prefixes? (yes / no)**
  4.0.0_SA_CRO~D asked for this (msg 96341). It is the one D14 item that must land before D8 creates the new firm buckets, and it changes the fence your "C" (09-12) kept intact, so I sent it to you.
  --------------------------------------------------------------------
  **REC --** Yes, on three conditions:
  (1) decide explicitly what happens to roles that carry no firm token. Three live writers have none today, one of them feeding served client data.
  (2) every existing writer gets a firm-scoped identity or a named exemption before the new fence lands, under never-widen sign-off.
  (3) the short list of AWS service exemptions is generated from the registry too.
  It replaces the list rather than carving anyone out, and it fixes the known defect where a ban list silently stops covering a renamed role.
+---------------------------------------------------------------------+

+-- CALL 2 of 7 ---------------------------------------------------+
  **How long must a legacy bucket go unread before it can be retired?**
  This is the only true wait in the D8 legacy-bucket and MDPF canon endpoints: nobody can prove a bucket is unused without an agreed quiet stretch. Needed before decomposition.
  --------------------------------------------------------------------
  **REC --** 45 days, counted from when read logging is live (call 3), so the window covers the 30 Sep quarter-end and the early-October reporting runs. A quarterly reader is the one a 30-day window can miss entirely; I have not measured whether one exists.
+---------------------------------------------------------------------+

+-- CALL 3 of 7 ---------------------------------------------------+
  **Turn on read logging for the legacy firm buckets so the quiet window can be proven? (yes / no)**
  opal-data-cot has no read logging at all. bd and inf are covered by an audit-trail setting that was applied by hand, outside Terraform. The template the new buckets are created from includes none.
  --------------------------------------------------------------------
  **REC --** Yes: add cot to the audit trail's read logging, move that setting into Terraform, and give the bucket template read logging. It only records reads and sends nothing, so it is not an alert, but the logging is billed, which makes it your word.
+---------------------------------------------------------------------+

+-- CALL 4 of 7 ---------------------------------------------------+
  **Confirm the DONE WHEN lines on the five endpoints I cut overnight?**
  Your 09-03 word makes this your confirmation, and after it the loop runs without you. The five are D14 pipeline canon, D14 naming schema, D14 executable layer, D8 legacy firm buckets and D8 MDPF canon. You haven't read any of them yet.
  --------------------------------------------------------------------
  **REC --** Confirm all five as cut. Every bar I lowered or qualified is stated on the endpoint itself and is cards 2, 3 and 5 here, so there is nothing hidden to find.
+---------------------------------------------------------------------+

CARRIED (nothing blocked; answer whenever)

+-- CALL 5 of 7 ---------------------------------------------------+
  **D14's "a migration project starts from the ledger" bar: (a) counts as met once built, so D14 can close on its own, or (b) counts only once a migration actually uses it, so D14 waits on a migration project?**
  The brief wrote (b). I cut D14 canon FWD-6 and naming FWD-6 at (a), and said so on each endpoint.
  --------------------------------------------------------------------
  **REC --** (a). The first migration project, D8 legacy firm buckets, is already commissioned, so the real-use evidence will arrive anyway as a confirming read. (b) would tie D14's close to a project that can't yet be registered.
+---------------------------------------------------------------------+

+-- CALL 6 of 7 ---------------------------------------------------+
  **Let the task-order gate also check edits to existing orders, but only orders that already declare the element being checked?**
  `.tools/to-pipeline-gate.py:21-24` records your "PROSPECTIVE ONLY" scope. 2.0.0_SA_COO~ZZZ measured ten task-order edits going through unchecked in one hour, one of which could change a criterion a worker was reading at that moment.
  --------------------------------------------------------------------
  **REC --** Yes, for those orders only. Your reason for prospective-only was avoiding a back-fill of 2,103 files, and this touches none of them.
+---------------------------------------------------------------------+

+-- CALL 7 of 7 ---------------------------------------------------+
  **OK to delete the `.worktrees/cto-l3-mdpf-canon` worktree? (a recursive delete, so it needs your word)**
  Measured just now: its tip `653a21c519` is already in CLOUD, with 0 unmerged commits and 0 tracked changes. It holds 5 untracked files, all my own commit-message drafts (944 to 2,368 bytes), whose text is already in the commits.
  --------------------------------------------------------------------
  **REC --** Yes. Nothing in it exists only there.
+---------------------------------------------------------------------+
```

(Two notes printed under the frame and NOT answered by his word: the macro enums were "not a card yet" -- this seat
owes two Rule 24 proposals first; and the SMS alert call is 0.0.0_AB_MSTR's under LD-0537. Neither is ruled here.)

## WHAT EACH RULING BINDS, AND WHO ACTS

| Card | Ruled | Binds | Actor, state |
|---|---|---|---|
| 1 | The firm-bucket fence (`DenyForeignFirmPrincipals`) is re-derived from each principal's SCOPE token, replacing the enumerated prefix list -- ON ALL THREE CONDITIONS | The D14 executable-layer PRD (its registry-derived deny patterns) and the template `s3-49financial.tf` the new firm buckets are minted from. The three conditions are ACCEPTANCE for the change, not advice: the unscoped-principal branch is decided in writing before the Deny lands; every existing writer (census: `bd-exporter-ec2-role`, `opal-advi-stitch-landing-role`, `irpt-directory-refresh-role`, per 3.0.0_SA_CVO's census, not re-derived here) holds a scoped identity or a named exemption first, under never-widen sign-off; the service-principal exemption list is registry-derived | L4 at this seat, once the D14 executable-layer project can register (blocked on the macro enum). ⚠ Route (a) of 09-12 -- a carve-out for one principal -- **stays closed**; this ruling replaces the list, it does not open (a) |
| 2 | Quiet window = **45 days, counted from when read logging is live** on the bucket | D8 legacy firm buckets FWD-6 and D8 MDPF canon FWD-8. Rule 27's essential-wait clause is now satisfied by name: the wait carries its reason and Andrew's word | Recorded on both endpoints this turn |
| 3 | Read logging **ON** for the legacy firm buckets: `opal-data-cot` added to the organisation trail's read logging; that selector moved into Terraform (today CLI-applied, `cloudwatch-alarms.tf:208-211`); the firm-bucket template given read logging. Billed; approved | The infrastructure plane | **PARKED -- owner `0.7.0_AE_CloudOps`**, because no infrastructure seat is live (broker read 16:51Z: nine live seats, none AE). **Un-parks when** a `0.7.0_AE_CloudOps` seat is live; `0.0.0_AB_MSTR` is asked to seat it in this record's broadcast. Card 2's clock does not start until this lands |
| 4 | DONE WHEN **confirmed as cut** on all five endpoints | Andrew's 2026-09-03 confirmation step for `ENDPOINT_FWD_D14_PIPELINE_CANON_20260912.md`, `ENDPOINT_FWD_D14_NAMING_SCHEMA_20260913.md`, `ENDPOINT_FWD_D14_EXECUTABLE_LAYER_20260913.md`, `ENDPOINT_FWD_D8_LEGACY_FIRM_BUCKETS_MIGRATION_20260913.md`, `ENDPOINT_FWD_D8_MDPF_CANON_MIGRATION_20260913.md`. From here the loop runs without him per that word | Stamped on each endpoint this turn. ⚠ He confirmed on the card's REC; **this record does not claim he read the endpoints** |
| 5 | **(a)** -- D14's "a migration project starts from the ledger" bars are graded at APPLIED | D14 canon FWD-6 and D14 naming FWD-6: D14 closes on its own; the first D8 migration's use of the ledger is a confirming read, never a gate on D14 | Stamped on both endpoints this turn |
| 6 | `to-pipeline-gate.py` also grades a **MODIFICATION** of an existing task order, **only for orders that already declare the element being checked** | Narrows the MODIFY exemption Andrew set as PROSPECTIVE ONLY (`.tools/to-pipeline-gate.py:21-24`). Orders that do not declare the element stay exempt; nothing is back-filled | Implementation routed to `2.0.0_SA_COO~F` as a round-5 input beside RULING M's checker limbs. ⚠ When it lands, CLAUDE.md Rule 27's sentence "widening it is HIS call and is carded, not assumed" and the gate's own docstring go stale -- a law edit is owed THEN, not now (the law must describe the tool as it behaves) |
| 7 | Worktree removal approved | `.worktrees/cto-l3-mdpf-canon` | **DONE at 18:50:06Z** after a re-measure in the same act: tip `653a21c519` an ancestor of CLOUD, 0 tracked changes, the same 5 untracked drafts. `git worktree remove --force` rc=0; directory absent afterwards; no longer in `git worktree list`. **The branch `cto-l3-mdpf-canon` was KEPT** -- his word covered the worktree, and the branch is fully merged |

## WHAT THIS DOES NOT RULE

- **The macro enums.** D14 has none; the D8 legacy-firm-buckets project fits none of D8's three (ETFS, MDPF, AUTH).
  `missions-tree-index.py:248-254` refuses registration without one. Ratification is his; the two Rule 24 proposals are
  this seat's debt and were not drafted when he answered. Four projects stay unregistered on it: the three D14 briefs
  and the D8 legacy-bucket migration.
- **The SMS alert delivery** (LD-0537, 0.0.0_AB_MSTR's).
- **Route (a) of 2026-09-12** -- still closed.
- **Which project builds the dedicated MDPF runner's host** -- named as a question on the MDPF canon endpoint; not a
  card, not ruled.

## WHAT MOVES NOW

MDPF_CANON is registered and its DONE WHEN is confirmed, so its L4 (the PRD moved into the tree and amended against
the ruled source-first string) is this seat's next act and waits on nothing above. The three D14 projects and the D8
legacy-bucket migration wait on the macro proposals.

---

## FOLLOW-ON ANDREW-DIRECT ~19:0xZ -- SEATING AND PUSH WINDOW: "yes to both"

**Received at:** the 1.0.0_SA_CTO terminal, after 0.0.0_AB_MSTR's 96396 (19:02:04Z). **Verbatim and entire:**

> "yes to both"

It answered these two questions, put to him verbatim:

```
1. Seat 0.7.0_AE_CloudOps for the read logging? Your approval covered the logging and naming that seat as its
   owner, not spawning a session. 0.0.0_AB_MSTR won't start one on another seat's request without your word.
   Its pre-flight check is clean: no live session, no open task orders. The 45-day quiet window doesn't start
   until that logging is on.
2. Open a push window for e8d6b5c27b and e2210bf34c? Under LD-0522 each push needs your word, and the last
   one was used at 05:47Z. Both commits are on this machine only; origin/CLOUD is still 7a9d5ec3dc.
```

**What it rules, and no wider:**
- **Seat `0.7.0_AE_CloudOps`** for card 3's read-logging item. The act is `0.0.0_AB_MSTR`'s (spawn authority); the
  seat's scope is card 3 as ruled -- `opal-data-cot` into the trail's read logging, the selector into Terraform, the
  firm-bucket template given read logging -- under that lane's own apply rules (safe-apply, change-management entry).
  The park recorded above un-parks when the seat is live.
- **ONE push window** under LD-0522 for `e8d6b5c27b` and `e2210bf34c`. The act is `0.0.0_AB_MSTR`'s. The commit that
  lands this section rides the same window, being on CLOUD before it opens -- the window is one push of the branch,
  not a push of named hashes only.

Relayed to `0.0.0_AB_MSTR` the same turn.

---

## FOLLOW-ON ANDREW-DIRECT ~20:1xZ -- WHAT IS "IN CONTENTION" FOR SEATING

**Context:** `0.0.0_AB_MSTR`'s 96398 corrected its pre-flight -- the base serial `0.7.0_AE_CloudOps` holds three
pending task orders (MDPF_GLOBAL T2C, NFRA_SUBSTRATECARDING TO-CARD-R-W4-COX, WSE_COTMDL WS5) -- and warned that the
seating check might refuse card 3's order. While this seat was measuring that, Andrew said, **verbatim and entire,
two messages in order:**

> "we're not doing substratecarding why are you focused on that?"

> "if its not registered to a fabric in directives its not in contention"

**What it rules, and no wider:** a project not registered to a fabric in `DIRECTIVES.yaml` is not in contention
for a seat. Stated for this seating question; not converted here into any gate change.

**MEASURED against the register this turn** (`org/missions/DIRECTIVES.yaml`, 15 directives parsed):
- `MDPF_GLOBAL` and `WSE_COTMDL` -- **members of no directive.** Not in contention, by his rule.
- `NFRA_SUBSTRATECARDING` -- **listed as a member of D11**, whose placement is LAPTOP. By the register it is
  registered to this fabric; by his word "we're not doing substratecarding". **That is a register discrepancy,
  surfaced and NOT acted on:** a members-line edit off one line of his would widen his word.
- Operationally moot for card 3 either way: the NFRA_SUBSTRATECARDING order carries **no addressee field** (no
  `<issued_to>`), so `to-decomp-ref-lint.py`'s seating index (`_open_to_index`, which skips an order whose
  `ISSUED_TO_RE` does not match) cannot count it against the base seat. And the lint's seating scope keys on
  `dep_stage` (pipeline registration), not on directive membership -- a DIFFERENT population from his rule,
  recorded, not changed.

**So card 3's order goes to the live base seat `0.7.0_AE_CloudOps`**, as a non-pipeline order (the lint's
seating check runs only on orders for `dep_stage`-registered projects, `main()` at `:369-373`).
