# ANDREW-DIRECT 2026-10-06 ~19:3xZ -- DSGN_REBRND is on indefinite hold; revert all of its commits

- **Channel:** the site-Z terminal of `2.0.0_SA_COO~D` (session 83c2c1d1-733c-4463-b47c-1dc1b819822e), typed by Andrew.
  It answers this seat's PROD-promote scope card (~19:0xZ) and his own visual smoke of portal DEV e2130d42 on
  localhost:5174.
- **Recorded by:** `2.0.0_SA_COO~D`, same turn.

## Verbatim

"I put an indefinite hold on DSGN_REBRND hold around 9a ET. All of these DSGN_REBRND commits need to be reverted."

"It may not be on this box. I called it off on the laptop box, you may not have gotten the message"

Follow-up words, same terminal, ~19:4xZ-20:1xZ, in order:

"you need to identify each of the commits associated with this function. We need to break them down by what exactly they did. I do
not mind the font and shape adjustments. But all color adjustments need to be revertted"

"honestly if its easier just revert all DSGN_REBRND edits. We dont need them and id rather have this chapter closed and that project
definitively closed versus trying to isolate some versus all and then we let things slip through to PROD>"

"if you think you got it correct, build the selective revert on the localhost:5174 now and ill smoke and test."

"maybe we do that first, ill let you know if it was right. if not, then we just revert the full group."

**As it stands after the follow-ups:** the SELECTIVE revert is built and served for Andrew's smoke (portal branch
`revert-dsgn-rebrnd-20261006` @6b4e89a8 in `C:/tmp/wk-rebrnd-revert`, one commit over DEV e2130d42). Measured breakdown of the 80:
59 reverted (56 colour product commits, 2 DESIGN.md colour-ruling docs, 1 test of a reverted file); 1 kept as shape (1e32f521, hover
underline); 16 kept as measurement scripts with no product file; 4 already net zero (4ca437eb/0bb079b8 and 14dcce76/84ca4161). No
commit changed a font. After it, the tree differs from PROD only by rounds 43+44, /freshness, that underline and the scripts. If
Andrew says it is not right, the FULL group is reverted instead. Nothing is pushed to DEV until his word after the smoke.

**Andrew's verdict after his smoke of 6b4e89a8 on localhost:5174, ~20:2xZ, verbatim:** "Yep were good here, great job."
The selective revert stands. 6b4e89a8 goes to `0.0.0_AB_MSTR~Z` for the portal DEV push (a fast-forward of DEV e2130d42). The
full-group revert is not needed.

## What it sets

1. **DSGN_REBRND: INDEFINITE HOLD from ~13:00Z (9a ET) 2026-10-06.** Andrew said it at the laptop. A search of commit
   messages since 12:00Z on site Z found no record of it, so this file is the site-Z carrier.
2. **Revert "these" commits:** the DSGN_REBRND commits on portal DEV that are not on PROD (`origin/PROD..origin/DEV`
   `--grep=DSGN_REBRND`, non-merge). At read time that is **80 commits** (PROD ce6f0721, DEV e2130d42). The summary
   given to Andrew said 79. The other 8 commits in that range (DSGN_AMGTV1 rounds 43+44 and AMGT_RESAPP /freshness)
   are NOT reverted.

## Not decided here (asked, not inferred)

- 117 commits whose message names DSGN_REBRND are already on PROD (v2.1.200 and earlier). "These" referred to the list
  shown, so whether the PROD-side commits also go back is put to Andrew. It is not assumed.
- The PROD promote of rounds 43+44 follows the revert. Andrew's earlier "recs approved" (card 2) covers a DEV state
  that has passed the post-push read, so the reverted DEV gets that read again before any promote.
