# PRD REVIEW -- LGIC_ENFORCE v1.0 @1118c45aef -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96503 -- the first review request delivered as an inbox file.

**Read, UTC 2026-09-14 ~05:3xZ:**
- The PRD @`1118c45aef`. The working copy is identical to the pin.
- The endpoint `ENDPOINT_FWD_D14_EXECUTABLE_LAYER_20260913.md` @`e2210bf34c`, its last commit, which carries Andrew's ~18:4xZ ruling stamp.
- The counterpart: `LGIC_NAMING` PRD v1.2, CONTRACTS @`d6e0c3b74a` (ADMITTED).
- This PRD's brief half, DEC-2 and DEC-4 -- read only to locate where the fence conditions landed, not graded.
- Andrew's ~18:4xZ ruling record, card 1.
- `sequence-check.py --project LGIC_ENFORCE`: stage 1; waits on `LGIC_NAMING` admitted -- MET.

**Half hash reviewed:** ratified-text `93e93ff626e097444fbed49e9f74480208facce9f1b63d26d85241f68bcdf50c`. It matches the
notifier's `93e93ff626e0`.

## VERDICT: REFUSE -- two changes, both in this half. Everything else holds.

## ENDPOINT -- 7 of 7 outcomes carried verbatim, with one ruled constraint missing

**Instrument:** a parser over both documents' FWD blocks, field by field, against the endpoint @`e2210bf34c`.
- **Carried verbatim:** TITLE, DONE WHEN and ACCEPT are EQUAL for FWD-1 through FWD-7.
- **Correctly trimmed:** the SOURCE lines drop only the `(s.5)` / `(s.6)` section pointers. Those are history, which the spine keeps out of the section (`CANONICAL_FABRIC_WORKFLOW_20260901.md:165`).
- **Correctly dropped:** FWD-2's DEPENDS line. Both of its halves are closed:
  - "the fence re-derivation, open at Andrew" was closed by card 1;
  - "L4's form split" was closed by `LGIC_NAMING`'s S4.

What is missing is the text that replaced DEPENDS.

### R1 (blocking) -- Andrew's three fence conditions are not in this half

**What was ruled.**
- The endpoint's ruling stamp @`e2210bf34c`: FWD-2's DEPENDS *"is closed as a question and becomes acceptance: (1) ... (2) ... (3) ..."*.
- `1.0.0_SA_CTO`'s relay of the same ruling (96393): the three conditions *"are acceptance, not advice"*.
- Card 1's REC, which Andrew approved, verbatim:
  - *"(1) decide explicitly what happens to roles that carry no firm token."*
  - *"(2) every existing writer gets a firm-scoped identity or a named exemption before the new fence lands, under never-widen sign-off."*
  - *"(3) the short list of AWS service exemptions is generated from the registry too."*

**What the PRD carries.** At v1.0 all three are closed in writing in DEC-4, which is in the BRIEF half. None of them
appears in ENDPOINT or CONTRACTS:
- FWD-2's ACCEPT states none of them.
- The CONTRACTS fence row states only *"per firm bucket, the registry-derived allow set of DEC-4"*.

**Why it blocks.** The spine's L4-R standard requires every operative constraint in the ratified text. A grader of
FWD-2 reads its ACCEPT. As written, FWD-2 could grade REALIZED on a fence that landed with any of these breaches, each
a condition Andrew set:
- an unscoped principal let through;
- a writer neither scoped nor exempted;
- a typed exemption list.

**Fix: carry the three in THIS half,** in plain terms and without history or seat names -- either as FWD-2 acceptance
lines, or in the CONTRACTS fence row:
- The Deny covers every principal except the firm's own scope and the principals `exemptions.json` names, so a principal with no scope token is denied unless it is named.
- It lands only after every existing writer holds a scoped identity or a named exemption, under never-widen sign-off.
- The exemption list is generated from the registry, never typed.

DEC-4 may keep its reasoning.

## CONTRACTS -- the counterpart rows agree; one internal contradiction

This is the check `LGIC_NAMING`'s review recorded as NOT EVALUATED, because no counterpart existed then. It is now
evaluated: `LGIC_NAMING` v1.2 CONTRACTS rows 1-4 against this PRD's rows 1-4.

| row | LGIC_NAMING (v1.2) | LGIC_ENFORCE (v1.0) | agreement |
|---|---|---|---|
| `NAMING_SCHEMA.json` | produced; consumed by `key()`/`name()`/`grade()` and the registry-derived deny patterns | consumed; read at run time by `key()`/`name()`/`grade()` and the generator, never copied | agree (see N1) |
| the grading rule | produced as a written spec (N2); consumed by the flagger | consumed and EXECUTED; `grade()` is its machine; a disagreement is graded against N2 | agree |
| the registry's rows | consumed, rows only; produced by `LGIC_ENFORCE`; seed `05_IDENTITY_SPINE.md` | produced (`infra/logic/registry/*.json`, DEC-1); seeded from `05_IDENTITY_SPINE.md` | agree; the direction flip is the intended one |
| the key string | consumed (ruled); the five segments verbatim; the bucket is the container, `{object}` the leaf | the same, verbatim | agree |

### R2 (blocking) -- two rows give two answers for what `key()` returns

- **Row 4:** *"`key()` produces exactly it"* -- the ruled five-segment string.
- **The `lib/opal_naming.py` row:** *"`key(source, scope, tier, table, partition)` returns a full address, with the bucket taken from the tier home rule and the scope's tenancy"*.

A full address carries the bucket; the ruled string never does. This is the exact ambiguity `LGIC_NAMING`'s
correction 2 closed -- a builder writing the bucket into the key -- and here it sits in the contract of the project
that writes the builder.

**Fix: give one answer, in both rows.** Either of these works:
- `key()` returns the ruled five-segment key, and a separate named function (or a stated second return) composes `s3://{bucket}/{key}/{object}` from the tier home rule;
- or `key()` returns the full address, and row 4 says the KEY part of that address is exactly the ruled string.

### N1 (non-blocking) -- row 1's consumer list

`LGIC_NAMING`'s row 1 names *"the registry-derived deny patterns"* among the schema's consumers. This PRD's row 1
names `key()`, `name()`, `grade()` and the generator. DEC-3 says the generator writes the fence's pattern lists, so the
fence is covered through the generator; say so in the row, or accept the difference.

On direction the two PRDs agree: DEC-4 makes the fence a Deny by default with two exceptions, and the fence row's
"allow set" is that exception list.

## WHAT DOES NOT MOVE

Everything else in this half is accepted as read: the seven outcomes' text, rows 2-4, and the other five produced
rows. A bump that touches only R1 and R2 re-opens only this half.

## NOT CLAIMED

- **The brief half** -- DEC-1 to DEC-12, the cells, paths, coverage and surface manifest. That half is `4.0.0_SA_CRO`'s.
- **DEC-4's mechanism.** It is not graded here; it was read only to find where the three conditions landed.
