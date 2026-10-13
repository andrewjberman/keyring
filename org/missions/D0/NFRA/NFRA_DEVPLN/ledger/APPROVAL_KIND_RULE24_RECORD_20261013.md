# Rule 24 record -- the `approval` kind in open-calls (NFRA_DEVPLN round 1, cell DP-b-1)

Cell `DP-b-1` of `org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round1.md`. The enum `KINDS` in `.tools/open-calls.py`
widens from `("fork", "act")` to `("fork", "act", "approval")`. Taxonomy law, four postulates (CLAUDE.md section 3, rule 24).
Measured at base `wk-NFRA_DEVPLN-1 @80247a96ad`; the census was run at `2026-10-13T19:03Z`.

## MECE

**Domain.** The kinds of a row on a box's open-calls list, `org/devices/state/<box>/open_calls.json` (the four box lists in the working
tree: dell1, dell2, laptop, sitez). A row is one call that asks one party for one act. The domain is the `kind` values those rows carry.
The S3 cluster copy holds the same rows and is not a separate population.

- `fork` = a decision with options (a ruling picks one option; the row carries a context and a REC).
- `act` = an act only Andrew can do (a delete, a signature, a vendor use).
- `approval` = a portal feature waiting for Andrew's yes or no (carries an `approval` object: branch, purpose, pages, class, how).

**Subtraction against a printed denominator.** One census of the `"kind"` token over the domain, `comp-find -i '"kind"' org/devices/state`:

    comp-find [content] '"kind"'
      DENOMINATOR: 93 hit(s) across 8 file(s) scanned in scope [corpus=all]

Split by value, the same corpus, each with its own printed denominator:

    comp-find -i '"kind": *"fork"' org/devices/state  ->  DENOMINATOR: 52 hit(s) across 8 file(s) scanned in scope [corpus=all]
    comp-find -i '"kind": *"act"' org/devices/state   ->  DENOMINATOR: 41 hit(s) across 8 file(s) scanned in scope [corpus=all]
    comp-find -i '"kind": *"approval"' org/devices/state -> DENOMINATOR: 0 hit(s) across 8 file(s) scanned in scope [corpus=all]
                                                          (NO HITS: a measured zero before this commit)

Subtraction: 93 - 52 (fork) - 41 (act) - 0 (approval) = 0. No `kind` value outside the three is held by any list. A row with no `kind`
key reads as `fork` (the reader's default, unchanged), so the three values cover every row that carries a kind. The approval count is
zero because the kind is new; the census was run before any approval row exists.

**Scope of the claim.** The census reads the working-tree lists of the four boxes at base `80247a96ad`. It does not read the S3 cluster
copies, which the tool writes beside them.

## SAME GRAIN

One row is one call to one decision, and the three kinds share one row shape: `id`, `project`, `subject`, `asked_by`, `source`,
`orders`, `roots`, `state` (OPEN|CLOSED), `opened_at`, `scope`, `closed`, `kind`. The grain of an `approval` row is one candidate
branch at its registration: the row names the branch (`cand/<box>/<slug>`), and the registration cell (DP-b-5) fills `head_sha` and
`commits` for that branch head. A later push needs a fresh row, so a row is not a standing permission for a branch.

The closure grain is also shared. `closed` keeps its old keys for a fork or act (`at, by, ruling, crossbox, ruled_by, xadj`). An approval
closure adds one key, `decision` (approved|declined), and nothing else. The per-kind extra objects are `context` and `rec` (fork) and
`approval` (approval); neither is stored on the other kind.

## INTENT COHERENCE

One axis: what the call asks the decider to do. Each kind has one intent, and its closure verb matches it.

- `fork` asks the decider to choose an option: closed by a ruling.
- `act` asks the decider to perform an act: closed by a ruling that the act was done or refused.
- `approval` asks the decider for a yes or no on a named feature: closed by `decision` (approved|declined), with `ruled_by` and the
  closing identity recorded.

`approval` does not reuse the fork's options or its REC. A feature's yes or no has no options to rank, so `--rec` and the 40-600 character
`context` rule do not apply; `purpose` and `how` carry its text. The class (client-facing, opal-internal, test-only) decides who may
close it validly, and that rule is read by `approval-status` (decomposition R3), not stored on the row, so the row carries one intent.

## STATE COHERENCE

A remedy's effect is stated by the values it does NOT move. Closing an `approval` row, with `--decision approved` or `declined`, writes
exactly one row of one box's list (`state`, `closed`), and the cluster copy of that list is put as every write is. It does NOT:

- merge, push, rebase or move any ref. A declined feature stays on its branch `cand/<box>/<slug>` with every commit intact.
- write a `Feature:` or `Approved-By:` trailer. Those are written by the merge-forward (DP-b-2) on the merge commit, not by the close.
- change `head_sha` or `commits` on the row. Those are the registration's values (DP-b-5) and a close never recomputes them.
- change the scope measurement of the row, or any other row of any list.
- store a validity value. `valid` is computed by `approval-status` from `state`, `decision`, `closed.by` and the class at read time. A
  stored validity would be a second carrier of one quantity, which drifts.

A reader on an older checkout is the one state change this record names. `validate_doc` refuses a key or a value it does not know, so
such a reader refuses the whole list of a box that holds an approval row until that box syncs this commit. The window is recorded as a
surprise row (`NFRA_DEVPLN-W1-S4`), not repaired here.
