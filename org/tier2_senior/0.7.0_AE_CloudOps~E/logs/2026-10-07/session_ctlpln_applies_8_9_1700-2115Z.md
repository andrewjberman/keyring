# `0.7.0_AE_CloudOps~E` -- session log, 2026-10-07 ~17:00-21:15Z: NFRA_CTLPLN TO-APPLY-8 and TO-APPLY-9

**Seat:** `0.7.0_AE_CloudOps~E` (laptop). **Issuer:** `2.0.0_SA_COO~C`. **Preceding log:**
`session_ctlpln_applies_5_6_7_1150-1545Z.md`. Both orders are WORLD-risk, genre DEPLOY, each with two signed
never-widen halves read in full before acting.

| order | act | result | entry | proof |
|---|---|---|---|---|
| TO-APPLY-8 @`c6037a3f5e` | dell1's read-only prefix-scoped join to three firm fences | `0 added, 3 changed, 0 destroyed` | CLOSED 6/6 | VALID rc=0, 8/8 controls |
| TO-APPLY-9 @`70eeb0005b` | the transcripts KMS key admits both Dell users to decrypt | `0 added, 1 changed, 0 destroyed` | CLOSED 6/6 | VALID rc=0, 8/8 controls |

Commits: `968a65390b` (entry 8 open), `97156fb12c` (8 closed + evidence), `a8ba6cdd9a` (entry 9 open),
`d84d5b2c4a` (9 closed + evidence + the NFRA_TRNSPT file). Push state at close of session: `968a65390b` and
`a8ba6cdd9a` ON ORIGIN; `97156fb12c` and `d84d5b2c4a` LOCAL (`origin/CLOUD` read `f797fc2df1` by `ls-remote`,
with a positive control). `0.0.0_AB_MSTR` pushes on Andrew's word.

---

## TO-APPLY-8 -- what made it different from the two dell2 joins before it

Under TO-APPLY-4 and TO-APPLY-5 this seat applied **the same three resources** to admit dell2, and admission WAS the
whole change. **Here admission alone would have been a write grant.** `cloudops-dell1-agent-user`'s own identity
policy allows get, PUT and list on the estate bucket pattern, and a principal admitted through a fence sits outside
that fence's Deny. The narrowing is done by three `DenyScopedExemption1*` statements added **in the same apply**.

**The decisive measurement was made by removing the thing being tested.** With all three statements stripped from
the document passed to the simulator, **12 of 12 confining arms read `allowed` -- PUT included**. With them present,
12 of 12 `explicitDeny`. So the claim "this is a read-only, prefix-scoped grant" rests on a differential, not on the
absence of a complaint.

### An instrument was discarded mid-verification, and its transcript was kept

The condition required each refusal attributed to a named statement, and `MatchedStatements` reports the source as
`Resource Policy`, never the Sid. Three instruments were tried:

1. **An all-three differential** -- 12/12 `full=explicitDeny`, `minus=allowed`. Sound, but names the three only
   collectively.
2. **A column-offset Sid mapping** -- returned `DenyForeignFirmPrincipals` for all 12, which **contradicted (1)**: a
   statement that no longer refuses an admitted principal cannot be the cause. Root cause measured: the API reports
   `StartPosition {Line: 1, Column: N}` against the single-line `json.dumps` string actually passed, while the helper
   windowed into a re-indented rendering whose Sids sit on lines 5/28/47/59 -- two coordinate spaces, so it always
   caught the first Sid. Corrected once, it still named a scoped statement on only **6 of 12** and still disagreed.
   **Offset arithmetic was then abandoned entirely.**
3. **Leave-one-out** -- remove each statement individually and see which removal lifts the refusal. No arithmetic.
   **12/12 attributed by name**, every result semantically exact and identical across all three buckets.

`READBACK8_sid_naming_20261007.txt` is committed **deliberately** as the record of the rejected instrument, so a
later reader sees what was discarded and not only what worked.

### The census verdict went `ok=False` and was filed, not smoothed

Before: `dell1_admitted=21/24 disagree=0 ok=True`. After: `dell1_admitted=24/24 disagree=3 ok=False`. Three rows read
`dell1 reading=ADMITTED evaluator=explicitDeny` on exactly the three scoped buckets, and the census computes `ok`
with `disagree==0`. **The control sat in the same run:** dell2, which has no scoped statements, shows
`ADMITTED/allowed` and no disagreement on those same buckets. So the census has no concept of
*admitted-but-scoped*. **Reported to the issuer and the CTO, not adjudicated here** -- the CTO half already owned a
cell for this, but it anticipated a misleading COUNT, not a FAILING VERDICT, so the gap is theirs to close. The
census is not one of that order's acceptance criteria; AC1, AC2 and AC3 all passed.

### Other points worth keeping

- The order's four-file gate used a `git diff` form that is **uncontrolled here**: `17b61b4124` is a trunk pin that
  never touched those files, so its diff is trivially empty. Proven positively by blob hash instead, with a **working
  control** (`d5516cb074^..HEAD` on the same pathspec prints 36 insertions).
- `0` changed-value lines is a different claim from `0` removed lines: Terraform renders a changed value as
  `~ old -> new`, which is neither. Checked separately; every `~` in that plan is a container marker.
- Two projects now compose in the cottonwood policy: dell1, newly admitted to that fence, is **still** `explicitDeny`
  on `commonwealth/cottonwood/bronze/crm/`, so ADVI_COTBKF's statements bind a principal admitted *after* them.

---

## TO-APPLY-9 -- the most constrained apply of the day

Root `infra/aws/terraform/transcripts/`, one statement on one KMS key. **The widening is the widest this seat has
applied:** after it, both Dell box users can read **every object in the meeting-transcripts store, the raw tier
included** -- their own policies already allowed the bucket read and only the key stopped them. Wider than the
recommendation Andrew was shown, and what he answered ("Yes Dell boxes can read all of that"). Both halves state it
at that width and neither narrows it; the entry states it at that width too.

### Two root conditions that shaped every step

- **The root cannot be applied untargeted.** It carries another project's unapplied work: `9 to add, 4 to change`.
  Everything was targeted at one address, and the only untargeted plans were read-only with `-lock=false`.
- **`terraform init` refuses in the shared tree** ("Backend configuration changed"). Everything ran from a
  `TF_DATA_DIR` scratch directory **proven outside every git tree**, with no `-reconfigure` and no `-migrate-state`
  and no prompt offered. The root's own `.terraform/terraform.tfstate` is **1818 B, sha256 `13b0ae84...215383`
  before the init, after the init and after the apply**.

**A precision neither half carries:** that stale record's `bucket`, `key` and `region` all **match** `main.tf`, so the
refusal is NOT the obvious mismatch -- it is some other field. Filed for the root's owner, not diagnosed further and
not repaired.

### The wrapper's fitness was read because the order made it a stop

"If the wrapper cannot be made to use the scratch data directory or the target, STOP" is not satisfiable by assuming
environment inheritance works. `safe-apply.sh:428` is `exec "$TERRAFORM" "$@"` -- argv forwarded transparently, the
environment inherited through `exec`, no `env -i`, no `unset`, no mention of `TF_DATA_DIR` anywhere -- and lines
119-120 parse `-target` explicitly. One read; it is the whole difference between a verified pass and a lucky one.

### A stop condition handled without idling

COO condition 6 (both Dells told before the apply) **could not be shown** from the fabric manager's record at
~19:30Z. Rather than apply and report the gap, or wait with nothing moving, the **one permitted ask** went out and
**every step that did not depend on the answer was completed meanwhile** -- the commit gate, the check, the scratch
init, the saved key policy, the targeted plan and the untargeted BEFORE read. Only the apply waited.

Shown from the **primary record** (read directly, not from the relay alone): dell2 ACK `98cdd415` at 18:26:33Z (12
DELIVERED / 0 QUEUED), dell1 ACK `c0781efc` at 18:38:55Z (6 / 0 / 0), both **sends** at 18:19Z and 18:33Z and so
before any apply. **The record's own limit is carried:** those onward counts are each Dell's broker delivery as its
manager reports it, **not each seat's read**. The record is untracked on disk, so it is anchored by content rather
than a commit pin. **Provenance:** its mtime is 19:39:39Z, nine minutes *after* the census, so the absence read was
correct when made and the record was written in answer to the ask.

### `ok=False` again -- and this time it is not a finding

The cell's check read `ok=True` before the apply and `ok=False` after. **All eight conjuncts were printed; exactly
one is False** -- `live_same` (line 290), which asserts the LIVE policy equals the **PRE-EDIT render**. It is a
pre-apply freshness guard, so after a successful apply it is necessarily False, and `ok=True` afterwards would have
meant **the apply had not landed**.

**The contrast with TO-APPLY-8's census is the lesson of the day.** Same symptom -- a check flipping to `ok=False`
after a correct act -- opposite disposition. There, the governing half had anticipated a misleading count but not a
failing verdict, so it was filed. Here, the order's AC1 `<expect>` **deliberately omits `ok=`**, so the issuer had
already accounted for it and no row is owed. **The difference was decided by reading the governing text, not by
habit**, and in both cases the conjuncts were decomposed before the thing was characterised at all.

### Nothing of the other project moved

Untargeted: `9 to add, 4 to change, 0 to destroy` before; `9 to add, 3 to change, 0 to destroy` after. The one
departed change is the key; the other 12 blocks are identical in count and identity; **0 destroys in either read**;
none of it applied. The order's predicted after-count is **derived, not guessed** -- exactly one of the four
pre-existing changes was this act's.

### One instrument error of this seat's, recorded in the evidence

The unlisted-principal arm first threw `NoSuchEntity`: it was sent through `simulate_principal_policy`, which
requires the IAM entity to **exist**. The cell's check uses `simulate_custom_policy` with a neutral identity and
`CallerArn`, which needs no such user and is the right instrument for "a principal the key policy does not name".
The corrected arm sits beside the error in `READBACK9_step7_20261007.txt`, with the reason, because the two calls are
easy to confuse.

### CTO condition 8 discharged as a file, with no id minted

`org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/ROWS_FROM_LAPTOP_TRANSCRIPTS_ROOT_20261007.md` --
two candidate rows, each with `spec_asserts` and `world_is`, **no `NFRA_TRNSPT-S<n>` id minted by this seat** (a Dell
mints that project's ids; the channel's highest is S14), and **"not already filed" explicitly NOT asserted**, since
this seat did not read that project's adjudications. The sharper row: the root cannot be applied untargeted. The
quieter hazard named inside it: the three **in-place** Lambda updates, which do not announce themselves as new
infrastructure, and `aws_kms_grant.pull`, an access change on the same key this seat had just edited.

---

## WHAT IS OWED, AND BY WHOM -- nothing here is this seat's

| item | owner |
|---|---|
| `<status>` flips on TO-APPLY-8 and TO-APPLY-9 | `2.0.0_SA_COO~C` |
| AC2 of TO-APPLY-9 (judgment; **no verdict** asserted by this seat, by the order's instruction) | `2.0.0_SA_COO~C` + `3.0.0_SA_CVO` at L9 |
| whether the fence census needs more than the cell already on the list, given it now reads `ok=False` | `2.0.0_SA_COO~C` / `1.0.0_SA_CTO` |
| NFRA_TRNSPT FWD-8 amended to match Andrew's word (CTO condition 7; expressly did not hold the apply) | `1.0.0_SA_CTO~DELL2` |
| the two candidate rows numbered and folded into NFRA_TRNSPT's channel | NFRA_TRNSPT's owner, via `1.0.0_SA_CTO~DELL2` |
| **the exercised reads** -- dell1's three arms on the scoped prefixes; a Dell's decrypt and refused put on the transcripts store | a Dell, by another route |
| the push of `97156fb12c` and `d84d5b2c4a` | `0.0.0_AB_MSTR` on Andrew's word |

**Both grants are APPLIED, NOT EXERCISED, in those words.** This seat read no object, listed no firm bucket and no
key of the transcripts bucket, and made no decrypt call. **CTO condition 9 of TO-APPLY-9 and condition 7 of
TO-APPLY-8 are same-window restore triggers, not notes:** if a Dell PUT succeeds, or a get outside the scoped prefix
succeeds, the saved policy for that resource goes back **that window** and `1.0.0_SA_CTO` is told. This seat's own
arms show every such shape refused and attributed by name, so a success would mean the live policy is not what was
applied.
