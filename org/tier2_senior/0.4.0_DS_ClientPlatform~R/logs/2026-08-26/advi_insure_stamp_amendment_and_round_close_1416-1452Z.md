# 0.4.0_DS_ClientPlatform~R -- ADVI_INSURE basis-axis amendment + round close (1416-1452Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** SCRIBE, DIAGNOSE

**seat:** `0.4.0_DS_ClientPlatform~R` · **window:** 2026-08-26T14:16Z -> 14:52Z
**prior log:** `advi_insure_gate_reread_and_ac2_join_1340-1416Z.md` @`6f26e2527a`
**project:** D2 / ADVI_INSURE · **TO:** `ADVI_INSURE.TO-R1-DS.landing-gold-platinum-planes`

---

## SUMMARY

AC2 was CLOSED by the issuer on the prior window's join. This window turned the one remaining
actionable item -- a wrong provenance stamp -- into a specified, approved, gate-clean producer change,
and **surfaced that the producer is not on the 49F runner chain at all**, which is the more valuable
half. **The ADVI_INSURE round is now closed for this lane with nothing owed and nothing in flight.**

---

## WHAT HAPPENED

1. **Issuer 72212** closed AC2 (*"satisfied on the available spine"*) and ruled the STAMP wrong:
   `NOT-DERIVABLE-UPSTREAM` says *a gap that may close*; what was measured is *can never close*.
   Ordered: specify the corrected stamp, do NOT edit the producer.
2. **Amendment spec delivered** @`211b4ae752` -- Rule 24 four-postulate record over the amended
   five-value domain plus a token-hygiene census. **APPROVED same-turn** (72236), both open questions
   answered my way: no `schema_version` bump; shared registry deferred to a **trigger** (Cottonwood
   reuse), not a date.
3. **Producer change landed** @`e9697d309d`, commit-gate `All checks passed` on 1 file.
4. **Deploy-state read surfaced the finding** -- producer absent from the runner chain and from the
   deployed code set. Reported; issuer **RULED option (a) source-only** (72267).
5. **Design-doc fifth row landed** @`06ff6bbb2f` under an audited author override, `~J` being dead.

---

## FINDINGS

### F4 -- The two negative stamps shared ONE constant while taking OPPOSITE remedies

`BASIS_NOT_DERIVABLE` fed **both** `account_id_basis` and `advisor_basis`. The discriminating test is
*could ANY upstream change populate this?* -- **YES** for advisor (BD template change, dim 436,
RESERVED to Andrew), **NO** for `account_id`, ever. **Under the four-value axis those are one value,
so the axis reported one remedy covering both when it covered one -- Rule 24(iv) unsatisfiable as
built.** That is a stronger reason than "the string is wrong," and it is the issuer's framing adopted.

Grounding: `account_id` IS the Schwab account number -- `dim_advisor_fee_role.account_id ==
dim_account_xref.schwab_account_id`, **5,337 of 5,337**, shuffle negative control **0 of 5,337**.

**The producer's own docstring at `:41-46` was already right** (*"insurance is held at carriers, not in
the AM book"*). Only the stamp disagreed with the design -- the cheapest possible confirmation of which
one was the defect.

### F5 -- The producer is not on the 49F runner chain, so the fix is DESIRED-layer only

| | |
|---|---|
| `data/assets/scripts/gold/runners_49f/` | 70 `.py` |
| `s3://opal-data-49financial/_code/` | 76 `.py` of 78 keys, **0 insurance-bearing** |
| `bd49f_insurance_nav_current.py` | **absent from both** |
| **positive control** | `bd49f_dim_portfolio_group.py` -- same prefix family -- present in **both** |

**Consequence:** no deployed copy exists to update, and the landed 2026-08-25 gold partition still
carries the old stamp in its bytes. Source fixed, artifact not. **By ruling, not by omission** -- it
restamps at AC4 emission via the scheduled producer.

### F6 -- A positive control caught my own false premise before it reached the issuer

I was about to report *"the producer is NOT DEPLOYED"* on an **assumed** mapping from
`data/assets/scripts/gold/` to that bucket's `_code/`. The control -- *do the other advi producers live
in that repo dir?* -- **FAILED**: they live in `runners_49f/`. **The sentence would have been
true-sounding and rested on a false premise, and the issuer had no way to see the premise.** The
finding survived in a sharper form; the original framing would not have.

---

## BRIEFS WRITTEN (DS role addition)

| brief | path | status |
|---|---|---|
| Basis-axis amendment spec | `.../0.4.0_DS_ClientPlatform~R/deliverables/ADVI_INSURE_BASIS_AXIS_AMENDMENT_SPEC_20260826.md` | **APPROVED** (72236) |

---

## COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `-i` on 5 candidate enum tokens + `account_id_basis` + `BASIS_NOT_DERIVABLE` | **PASS** | The census that made same-turn approval possible: `STRUCTURALLY-INAPPLICABLE` 0 of 26,746 (clean mint), `NOT-APPLICABLE` 103, `INAPPLICABLE` 149. Also proved **zero downstream consumers** (2 hits: 1 producer line, 1 doc of mine). |
| `comp-pipescript io` | `--pipeline advi` | **REFUSED, correctly** | `Unknown script in tree [advi]` -- the script is ~14h old and not in the graph. Tool named the tree and did not fall back to bd. |
| `comp-pipescript deployed` | flagless, then `--pipeline` | **REFUSED, correctly** | rc=2, *"NO GUESS IS MADE"* -- cannot resolve a tree for a script under `data/assets/scripts/gold/`. |
| `safe-commit.sh` | 3 commits (`-F` message files; one with `GIT_COMMIT_AUTHOR_OVERRIDE`) | **PASS** | commit-gate `All checks passed` on the `.py`; risk-reflex CLEAN each time; msg-verify MATCH each time. |

**What worked:** the token-hygiene census was decisive -- it caught that `INAPPLICABLE` is a
**substring** of the proposed token, so a census of one could not discriminate the other. That
rejected the tempting shorter name on evidence rather than taste.

**What failed:** nothing, in the sense that matters -- both `comp-pipescript` refusals were correct
and printed their reasoning.

**Gap found:** ⛔ **the estate cannot answer "is this producer deployed" through the standard
instrument for scripts under `data/assets/scripts/gold/`.** Both `io` and `deployed` refuse honestly
rather than guessing, which is right -- but the question then has no tool and must be answered by a
hand-rolled S3 walk, which is where the wrong-deploy-home assumption (F6) came from. Routed to
`1.0.0_SA_CTO` by the issuer as a second live instance of deploy-oracle blindness.

---

## MCP TRAFFIC

**8 messages** (4 in, 4 out). IN: 72212 (AC2 closed + stamp ruled wrong), 72236 (amendment approved,
both questions answered), 72267 (ruled option (a), design-doc override authorized). OUT: amendment
spec report, stamp-fix report carrying F5, round-close report. ACKs recorded for 72212, 72236, 72267.

---

## BLOCKERS

**None.** The producer's home is routed to `1.0.0_SA_CTO` as an architectural call -- that is a
routed decision, not a blocker on this lane.

---

## CURRENT STATE

- **ADVI_INSURE.TO-R1-DS:** AC1 CLOSED · AC2 CLOSED · AC5/AC6 PASS · **AC3 held open**, re-takes at
  emission as a null-change baseline extension, quote **10** independent digests · **AC4 still shut**,
  the only remaining build, untouched pending an explicit re-cut **plus** a freeze release.
- **Producer** `data/assets/scripts/gold/bd49f_insurance_nav_current.py` now carries two distinct basis
  constants with comments naming the discriminating test, and `advisor_basis` carries an explicit
  *"do not fix these to match"*.
- **Not deployed, deliberately.** No gold bytes rewritten, no bucket touched, no placement performed.
- **`~J`'s design doc** carries the fifth row + grain limit + a pointer block. ⚠ Its `(i)` and `(iv)`
  paragraphs **still predate the fifth value** -- I did not rewrite them because the authorization was
  scoped to the row, the limit and a pointer. The pointer block sits **above** them so a reader hits
  the warning first. One line from the issuer takes that reconciliation.
- **6 commits this session, all LOCAL** under the integrator-only push gate, riding `0.0.0_AB_MSTR`:
  `0628d6d259` · `4d6ffbb3db` · `6f26e2527a` · `211b4ae752` · `e9697d309d` · `06ff6bbb2f`.

---

## NEXT STEPS

1. **[`1.0.0_SA_CTO`]** Where does `bd49f_insurance_nav_current.py` live and deploy (Rule 17b)?
   **The cheap window closes at AC4 emission** -- before emission it is a file move; after, the producer
   has served a key and moving it is NEVER#3 with a never-widen sign-off attached.
2. **[`2.0.0_SA_COO`]** Optional: authorize reconciling ~J's (i)/(iv) paragraphs to the five-value set. Small edit, currently mitigated by the pointer.
3. **[`0.4.0_DS_ClientPlatform~R`]** AC3 re-take the moment AC4 emits. **Gated on another lane's build;
   this lane is not claiming it.**

---

## DO NOT

- **Do NOT re-run the producer to restamp the 08-25 partition** -- REFUSED by ruling 72267. Rewriting
  real gold bytes to fix a string nobody can read yet is a bad trade in the irreversible direction.
- **Do NOT place or deploy the producer** without the CTO architecture call.
- **Do NOT "fix" `advisor_basis` to match `account_id_basis`** -- they differ deliberately and the code
  says so at both sites.
