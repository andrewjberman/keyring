# C-VERDICT -- the fourth verdict value: four-postulate record and token census

**Author:** `1.0.0_SA_CTO`, 2026-10-07 ~11:5xZ, at the cut of cell `BF-t-2` (PRD contract C-VERDICT; CLAUDE.md rule 24).
**Asked by:** `2.0.0_SA_COO~G` msg 106197; its draft is in `decompositions/LGIC_BLANKFIX_DECOMP.md` @f15f222030, "Rule 24 record".
**Grounding:** Andrew's ruling 3 and CALL 3 of 2026-09-21 (brief finding F3: an AWS service name is never a `{system}`, extended to
inline policy names and library layers; "the check gives these their own verdict").

## RULING

**The value is `NO-SYSTEM-ASKED`. The draft is ratified as written.** Reason for the word: it states the question the check does not
put to the name, which is what Andrew ruled. `SYSTEM-EXEMPT` reads as a waiver someone granted, and `NOT-SYSTEM-BEARING` describes
the name rather than the check's act.

**Verdict list after the edit, in the order the check asks:** `NO-SYSTEM-ASKED`, `CONFORMANT`, `ALIAS`, `OUT-OF-PATTERN`.

## The four postulates

**(i) MECE over a declared domain.** Domain: every `(name, type)` for which `grade()` returns a verdict (types marked NOT GRADED
stay outside it, unchanged). Two questions, asked in order: (1) is a system asked of this kind of name; (2) does the grammar hold.
(1) no -> `NO-SYSTEM-ASKED`. (1) yes, (2) holds with canonical spellings -> `CONFORMANT`; holds with an alias spelling -> `ALIAS`;
fails -> `OUT-OF-PATTERN`. Every member takes exactly one value. Membership of `NO-SYSTEM-ASKED`, as the draft measured it on the
repo plane: names whose lead token is in `refused_keys.purpose_word`, PascalCase single-token policy names, and `LAMBDA_LAYER`
names, where no later token and no registry row resolves a system: 106 of the 141 names that return `OUT-OF-PATTERN` with
`{system}` today (80 + 4 purpose-word, 19 PascalCase, 3 layers). The 35 left over stay `OUT-OF-PATTERN`. That count is
`2.0.0_SA_COO~G`'s measurement, not re-run by this seat; `BF-t-2` re-reads it and the cell's proof carries the number.

**(ii) Same grain.** One verdict per `(name, type)`, as the other three.

**(iii) Intent coherence.** One axis: the grade of the name against the grammar. The new value says no remedy is owed.

**(iv) State coherence.** A registry row moves an `OUT-OF-PATTERN`-with-`{system}` name; it never moves a `NO-SYSTEM-ASKED` name.
Only a rename, or a change to this record's membership rule, moves one. A `NO-SYSTEM-ASKED` name carries no `{system}` placeholder
in its canonical form.

## Word-boundary token census

Pattern `\b(NO-SYSTEM-ASKED|NOT-SYSTEM-BEARING|SYSTEM-EXEMPT)\b`, case-insensitive, over the laptop working tree at trunk
`324e7f0232` by the ripgrep search tool (tracked and untracked files; gitignored files not read): **3 occurrences in 1 file**, the
decomposition that proposes the value. No hit in naming code, the schema, the registry or any gate. The draft's five looser
`no-system` hits are not word-boundary matches of any of the three.

## What moves with the row (one schema row and its text, nothing else)

`org/standards/NAMING_SCHEMA.json` `grade.verdicts` gains the value; a `grade."NO-SYSTEM-ASKED"` line states the rule above; the
two sentences that say there is no fourth verdict (`grade.not_graded`, `grade.unplaceable`) are reworded to say "the four".
`unplaceable` still RAISES: a name the tokeniser cannot place is not filed here.

**Non-application:** S3 addresses and types marked NOT GRADED.
