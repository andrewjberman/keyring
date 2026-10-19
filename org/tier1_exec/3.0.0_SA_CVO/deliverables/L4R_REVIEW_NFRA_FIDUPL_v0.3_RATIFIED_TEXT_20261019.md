# L4-R re-review -- NFRA_FIDUPL PRD v0.3 @6d747e7737, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-19 ~18:4xZ. Delivered by 1.0.0_SA_CTO~DELL1 msg 8449, answering
`L4R_REVIEW_NFRA_FIDUPL_v0.1_RATIFIED_TEXT_20261019.md` @6c7c8bdf80. Half hash `5a43ba50b110`. (v0.2 carried the v0.1 hash `2f70753360a5`
unchanged, so the v0.1 refusal @5c277d3352 covered it.)
**Graded:** the PRD diff c09ae3894a -> 6d747e7737, and the amended L2 record at the same commit.

## Verdict: REFUSE (ground 1 only; ground 2 is closed)

- **Ground 2, closed.**
  - FWD-2 now drives the chain on demand with the schedule's own trigger, reads the live schedule inside the Schwab window, and runs once
    on demand for a day Fidelity has not produced. The organic morning is kept as the negative arm.
  - FWD-4 now pulls a Monday export on demand and pulls the same Friday files a second time to show they land once. The organic Monday is
    kept as the negative arm.
  - Neither line is a wait any longer.
- **Ground 1, stands.** Open call `dell1-20261019T180825Z-e141` still reads `[OPEN]` at this read (`python .tools/open-calls.py list`). The
  ENDPOINT therefore has no ratified pin.

## Checks that pass

- **Verbatim:** the PRD's ENDPOINT block is byte-identical to the amended L2 record's at 6d747e7737 (a script compared the fenced blocks
  via `git show`: IDENTICAL, 0 non-ASCII characters).
- **C-TENANCY agrees with the verdict @bc07810172:** a FIRM-tenancy `alongside` scope, never COMPOSITE, with the cross-firm gate edit in
  both directions in the same commit.

## Nit, not a ground

- FWD-4's parenthetical, "the 2026-10-19 files, holding 2026-10-16, are served now", is current state inside the ENDPOINT, and it will age.
  The DONE WHEN reads the same without it, and it could move to C-DATE or C-BACKFILL.

## Surfaced, not graded (Andrew's act `c3a6`)

- The Terms of Use finding @e999b31f1f says the terms prohibit robots and agentic AI unless Fidelity approves. FWD-1's ACCEPT requires that
  "no person signed in or typed a code". So FWD-1 as written is reachable only through Fidelity's written approval. This belongs with
  Andrew's word on C-TOU; this half does not grade it.

## Re-delivery

Re-deliver after Andrew confirms. If he confirms the eight lines as they stand, this half is signed on that delivery with no further
reading. If he changes a line, only that line is re-read.

-- 3.0.0_SA_CVO~DELL1
