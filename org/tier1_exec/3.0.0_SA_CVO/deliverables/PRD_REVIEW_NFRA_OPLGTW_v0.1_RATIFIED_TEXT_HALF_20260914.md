# PRD REVIEW -- NFRA_OPLGTW v0.1 @2af252cb39 -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96729 (19:47:25Z, from `1.0.0_SA_CTO~A`).

**Read, UTC 2026-09-14, after 19:47Z:**
- The PRD @`2af252cb39`. The working copy is identical to HEAD. I read the header, the preamble sections, ENDPOINT, CONTRACTS C1-C6 in full, and the SURFACE MANIFEST.
- Andrew's commission, @`45ce4e5b73`.
- Andrew's endpoint approval `ANDREW_DIRECT_20260914_1524ET_NFRA_OPLGTW_ENDPOINT_APPROVED.md` and the approved cards `NFRA_OPLGTW_ENDPOINT_PROPOSED_20260914.md`, both @`4498e665cc`.
- `org/standards/NFRA_OPLGTW_CONTRACT.json` @`2af252cb39`: `contract_version` 1.0, `activation` DESIGN_ONLY_NOT_A_GRANT.

**Half hash:** the notifier's `908c9e9460c1`. The stamp is bound with `--expect-half-hash`.

## VERDICT: SIGN -- ENDPOINT is byte-verbatim to the eight cards Andrew approved; CONTRACTS is single-owner as it states

## ENDPOINT -- verbatim to the ratified pins, measured by a line-level diff

- **Andrew's word** (@4498e665cc): *"Approve all eight bars"*. His record says the cards "land unchanged in the canonical PRD's ENDPOINT section".
- **This seat's diff**, a script over the approved cards against the PRD's ENDPOINT:
  - **32 of 32** DONE WHEN / ACCEPT / PROOF / SOURCE lines are byte-identical;
  - **8 of 8** headings match, the only difference being markdown heading formatting (`###` dropped, one space doubled);
  - **0** ENDPOINT lines are neither a heading nor a field.

  This matches the author's claim ("All 32 ... lines match"), measured here by a different instrument than the author's.
- **Every bar is EXERCISED by a deliberate act,** a walkthrough or a controlled test. None waits on an organic event (spine Rule 27, "NO FWD IS A WAIT").
- **No seat name, history or annotation is inside ENDPOINT.** "Menachem" is the named user the outcomes serve, not a seat.

## CONTRACTS -- read in full (C1-C6)

- **The enumeration authority is data.**
  - `NFRA_OPLGTW_CONTRACT.json`, version 1.0, closes the tools, fields, states, error codes and limits.
  - Unknown values and extra properties fail closed.
  - `activation=DESIGN_ONLY_NOT_A_GRANT` keeps the proposed profile from being read as a grant.
- **Single owner:** *"No counterpart PRD exists; all interfaces below have one owner in this project."* This holds against the SURFACE MANIFEST. The one interface that looked external, C3's extension of the Schwab producer's completion metadata, is this project's own surface **S4** ("existing conversion_manifest producer and entry paths"). C3 keeps the legacy fields for existing consumers, and it rules out repairing source data or rewriting silver values.
- **The fail-closed defaults are coherent across sections.**
  - C2: an unknown user sees no Schwab tools, and a store outage denies.
  - C1: legacy tokens are rejected at cutover.
  - C6: the feature flag is off by default, grants are pending by default, and a rollback never reopens the email-only path.
  - C3: legacy markers do not qualify.

## NOTES (non-blocking)

- **N1 -- vintage-bound readings inside ratified text.**
  - C2: *"Inventory all 27 source-declared server routes"*.
  - C6: *"Current AES256 observations do not justify a new KMS grant"*.
  - C1: *"These protocol details are verified against [Claude authentication requirements](...)"*.

  Each is a reading at authoring time, and each ages with the tree or the vendor's documents. The C1 sentence also asserts a verification the half itself cannot carry. The rules stand without these readings. At the next bump they can move to the ground-truth section, which already separates repository source from observations.
- **N2 -- for L5, not this text.** S4 changes a Schwab producer whose scripts sit in the DS deploy lane (CLAUDE.md Rule 13: DS owns commit->QA-deploy for `data/*/scripts/{gold,silver,bronze}`). Its completion markers also have readers outside this project. The legacy-field preservation in C3 protects those readers. The cell that implements S4 must run through that lane's deploy path, and census the markers' current consumers before it changes them.
- **N3 -- the header is DRAFT.** It stays DRAFT until the independent ground-truth review resolves. This stamp binds the half's hash, and the PRD states that a header-only promotion does not disturb it.
- **N4 -- the supplement (96729's companion) arrived marked "Sender-unverified".** It was treated as a pointer only. Every fact this review relies on was read from the pinned commits.

## NOT CLAIMED

- **The brief half.** It is `4.0.0_SA_CRO`'s (96730).
- **The independent ground-truth certification of the authoring run** (`workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/run.json@4498e665cc`) that the supplement asks for. That is a separate act of review, and this L4-R stamp does not perform it.
- **Any live behaviour, deployed parity, IAM effect or active grant.** The PRD claims none, and this review read none.
