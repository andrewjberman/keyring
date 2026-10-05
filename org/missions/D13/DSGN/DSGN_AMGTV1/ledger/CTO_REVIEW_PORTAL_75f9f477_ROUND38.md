# DSGN_AMGTV1 round 38 -- CTO review of portal candidate 788d54a8 + 75f9f477 (AV-zp-1), `1.0.0_SA_CTO~Z`, 2026-10-05 ~12:5xZ

**Input:** COO~D drain @48d8c081d7 (worker proof @65627bac8e: repairs38 5 of 5, battery29 ALL PASS). The round-38 list is
@0a865d7e8f.

## Placement

- **The stack:** 75f9f477 -> 788d54a8 -> 85e24287, the unpushed round-37 candidate, which is still awaiting Andrew's DEV word.
- **DEV:** `origin/DEV` is now `31510397`. It moved by four DSGN_REBRND FAST-lease commits (99c6ae08..31510397).
- **Trial merge** of 75f9f477 onto it (`git merge-tree --write-tree`): **clean, 0 conflicts**.
- **The DEV push now carries rounds 37 and 38 together:** 24 files, +554/-103 against the merge base 3e1aa46f.

## Read

| item | read | verdict |
|---|---|---|
| Shared `PanelFooter.tsx` | Two optional props: `ground` (default `'band'`, unchanged) and `timeText` (absent means the old formatter path). Every other page's footer renders as before. | PASS |
| `CardFooter.tsx` (new, 201 lines) | Prints a footer only when the card SERVES both a time and a source; otherwise no line (FWD-27). The time is the newest served value; a bare served day prints as a day with no invented clock. | PASS, with the one fix below |
| What changed panel | On PanelLoading and PanelError (FWD-19); the issuer's battery and repairs pass | PASS |

## REQUIRED before the push (FWD-11: "no raw code, id or storage path shows on the visible face")

`sourceWords()` at `CardFooter.tsx:95` falls back, for any long source value it does not recognise, to the raw value with its
punctuation turned into spaces. A storage-style source such as `issuer-site/harvest/silver/filing_source` would print as "issuer site
harvest silver filing source". That is a raw code in words, and FWD-11 forbids it on the face.

**The fix:** that last fallback returns `UNNAMED_SOURCE_WORDS` ("a source this page has no name for yet"), the same as line 94 does
for short codes. One line, plus one arm in repairs38 that plants an unknown long source and expects the unnamed phrase.

## Verdict

**APPROVED for the DEV push once that fix lands**, as the merge onto `origin/DEV` `31510397` carrying rounds 37 and 38. The push
needs Andrew's word (CLAUDE.md Portal, per-push word for product files) and is held at `0.0.0_AB_MSTR~Z`.

**CONFIRMATION (2026-10-05 ~14:0xZ):** the required fix landed as portal 72c60f2b (`CardFooter.tsx:95` returns `UNNAMED_SOURCE_WORDS`;
1 line; repairs38 6/6 with the unknown-source arm). The push candidate is **portal `481b3bcc`**:
- it CONTAINS `origin/DEV` `cab2b039`, so it is a fast-forward;
- 24 files, +554/-103, the reviewed footprint.

Relayed to `0.0.0_AB_MSTR~Z` for the DEV push under Andrew's record 121b7b016e.
