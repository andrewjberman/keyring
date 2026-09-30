# L4-R review -- NFRA_TRNSPT PRD v0.1, ratified-text half (`3.0.0_SA_CVO`)

**Delivery:** `1.0.0_SA_CTO` message 103217, 2026-09-30T07:16:01Z. **PRD:**
`org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` @`3a6e3dad13`, half_hash `bb1c147759e4`, FWD-1..FWD-11.
**Verdict: SIGN.** One wording note (W1), three items for L5 (Q1-Q3). None re-opens the half.

## The review limbs

| limb | result | evidence |
|---|---|---|
| ENDPOINT verbatim against the ratified pin | PASS | the PRD's FWD block (60 lines) against `ENDPOINT_FORWARD_NFRA_TRNSPT_20260930.md` revision 2 @3d825e1a26 (77 FWD lines), both by `git show`. The 27 differing lines are all outside the outcomes: the revision-1 retirement note under FWD-7, the two `(NEW)` markers on FWD-10 and FWD-11, and the endpoint's trailing DEPENDENCIES / OPEN / GROUNDED blocks. Every DONE WHEN, ACCEPT and SOURCE line is byte-equal after indentation |
| Andrew's confirmation of the DONE WHEN lines | PASS | `ANDREW_DIRECT_20260930_06xxZ_TRNSPT_DONE_WHEN_CONFIRMED_PAGEFILE_APPROVED_KIMI_STANDING_WORD.md` @6a861c4e18 quotes "Confirm, we have a lot more stuff that is going to be going through that bucket/channel but that one is a start" against revision 2 @3d825e1a26 |
| every operative constraint present | PASS | the alert moratorium is C-MORATORIUM; the per-use vendor word is C-KIMI; the two-reader rule is C-READERS; rule 30 is C-NAMES; the cross-firm rule is C-FIRM; no shadow pipeline is C-COPY; the tiering is C-TIERS under annex 17c |
| no annotation, history or seat name inside the section | PASS with W1 | the retirement history and the `(NEW)` markers were correctly left out; `(AMENDED IN PLACE)` remains on FWD-7's title, which is the endpoint's own bytes |
| CONTRACTS agrees with the counterpart PRDs | PASS | D7 `docs/architecture/D7_TICKET_VNEXT_PRD.md`: WS-1 (storage and the ticket bucket, first) and WS-2 (attachments on creation, the authorised-upload and refused-user exercise) as C-TICKET-ATTACH states; IRPT_BCKEND's PRD names no READY hook, as C-TRIGGER states ("no hook exists") |

## Checks this seat ran (07:2xZ)

- Every file the CONTRACTS cite exists at HEAD: `transcripts/main.tf`, `token_broker.py`, `config.py` (line 51 carries
  `Mail.Read`), `resolution_kimi.py` (line 20 is `MODEL = "kimi-k3"`), `ticket_center/lambda_function.py` (line 904 is
  `def _sod_block`), the transcript-tools spec, `systems.json`.
- C-SOURCES: `outlook` and `sharepoint` are not rows in `infra/logic/registry/systems.json` (4 top-level keys; the
  only `sharepoint` string is inside system 47's description; `teams` is present). The claim holds.
- The contract cells are consistent with each other: C-DEDUP's fallback key, C-WIPE's `[ID]` (not a hash) and
  C-WIPE-GATE's "planted classes removed, never no PII remains" read as one design.

## Wording note (not blocking; the endpoint's bytes)

- **W1.** FWD-7's title carries `(AMENDED IN PLACE)`. It is history, not outcome text. A later endpoint revision can
  drop it; ENDPOINT PROVENANCE already records the amendment.

## What you should have asked but did not

- **Q1. FWD-8's ACCEPT and C-READERS name different second readers.** The ACCEPT line says "Andrew and the terminal
  seat's account can read the original"; C-READERS names `opalbloomberg@opalinvest.com`. If these are the same
  account, the PRD should say so once; if not, the two-reader demonstration (S21) has three names in play before it
  starts. L5 should pin the two principals by identity, not by role.
- **Q2. C-IDENTITY's unmeasured token lifetime gates the thread's first two hops.** The PRD says so honestly. L5
  should cut the measurement as its own cell with a printed number (hours until `NeedsLogin`), because "hops 3-6
  built against a pull under a fresh sign-in" is a real run only if the fresh sign-in is itself a recorded act.
- **Q3. C-KIMI's input list is the PII boundary, and no cell owns proving it.** "Abstract fields only" is a claim the
  slicer's output must satisfy; C-WIPE-GATE tests the wipe, not the prompt. The first Kimi call should be preceded by a
  read of the exact payload with a planted-name control, or the wipe gate's pass is being borrowed for a different
  surface.

## Not verified by this seat

The `held` line numbers in the SURFACE MANIFEST, the bucket's live configuration (C-BUCKET), the Ticket Center's
deployed security state, and the CRO's mailbox measurements (v3 addendum 8). They are outside the ratified-text half.

-- 3.0.0_SA_CVO
