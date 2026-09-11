# STATE LOG -- 2.0.0_SA_COO~ZZZ -- AMGT_RESAPP -- device reboot 2026-09-11 ~13:3xZ

Written for a SUCCESSOR with NO context (Andrew-direct @21382: /log then reboot; every site-Z session is
gone after the reboot and nothing respawns). This seat = the COO lane owning the AMGT_RESAPP canonical
workflow (L5 decomp, L6 issuance, L7 spawn/drain). Pick this project up with `/canonical-flow AMGT_RESAPP`.

## ONE-LINE STATE
Rounds 1-4 all TERMINAL. Round 4 (v4) DRAINED and handed to the CVO for L8/L9/L10. No live workers, no open
orders, nothing owed FROM me. The SURFACE round (v5) is PARKED for the relaunch, gated on the CVO's v0.4 sign.

## WHERE THINGS ARE (hashes)
- HEAD at close: `79ec889666` (round-4 rc-20 drain). Push state LOCAL; 0.0.0_AB_MSTR~Z holds/pushes origin/SITEZ.
- PRD: v0.4 `@bbbf35c38e` (Andrew approved all four /open-calls, ruling @21365: DESIGN_SPEC lifted, FWD-15
  minted, infra GO, time-scoped vendor word, starred-per-firm).
- Decomp: v0.5 `@06d72ff757` (round 4, section 12) + round-4 ruling amendment `@af0a64a7ec` (S11 framing) +
  carrier relabel `@8fa4ac817e` (round 2b -> canonical v3). Sections 1-11 are rounds 1-3, frozen.

## OPEN TASK ORDERS + STATUS
NONE open. All 26 (round 1) + 5 (round 2, r-*) + 5 (round 3, rb-*) + 2 (round 4, rc-*) task orders are
`<status>complete</status>`, VALID at HEAD. Round-4 cells: `AMGT-rc-19` (class-level S11 unresolved-overlay
figure rule) drain `eb87c923ed`; `AMGT-rc-20` (S3 provenance: distinct observation/vintage/derivation fields,
render_figure_line emits fig.source) drain `79ec889666`.

## WORKER SUBAGENTS + WORKTREES
NONE live. All round-4 workers drained; all worktrees retired; `git worktree list` shows no wk-amgt/wk-AMGT.
(Subagents do not survive the reboot regardless.)

## OWED, AND TO WHOM
- FROM me: nothing. Round-4 drain-end sent to 3.0.0_SA_CVO~Z (msg @130743Z) -- it owns round-4 L8/L9/L10
  (stamp r4, cut REMEDIATION_v4, grade rc-19 AC4 + rc-20 AC4, disposition row W1-S6 [OBSERVATION/INERT],
  confirm C-S16 CLOSES). That is the CVO's, recorded OWED per the directive, NOT rushed at 0.2 GB.
- TO me (blocks my next act): the CVO's v0.4 RATIFIED-TEXT L4-R sign-off (the ENDPOINT now carries FWD-15, a
  real re-sign, not byte-identical). 4.0.0_SA_CRO~Z's coverage half is SIGNED `@1b7a996c86`. When BOTH v0.4
  halves sign, the L4 notifier delivers the PRD to the COO -- that is the trigger to cut the surface round.

## HELD / PARKED, AND WHY
THE SURFACE ROUND (v5) -- the .tsx shell (S16 Lead Panel + Thesis/Peers/Coverage tabs, Print header export,
Model tab cut with figures rehomed) PLUS the infra cells (opal-amgt-articles + opal-amgt-security-metrics
tables FIRST, then the harvester EC2 box with its own IAM role -- explicitly NOT the ASTN_WSJFT box), under
the six PRD s.3b constraints (article store, server-side ranking, box-side price puller, harvester compute,
starred-per-firm, the time-scoped SA/FT/Bloomberg/WSJ vendor word effective only when the box is up). FWD-15
bar EXERCISED. PARKED per Andrew @21382 ("the SURFACE round waits for the relaunch"). NEXT COO ACT on
relaunch: once round 4 is drained (done) AND both v0.4 halves sign, cut it via `/atom-decomp AMGT_RESAPP` on
the v0.4 surface manifest, then the L6 issuance.

## DEVICE NOTE
The full ~33k-file worktree checkout OOM-killed twice pre-reboot (Rio.exe leak, 0.2 GB free). Round-4 workers
ran on a cone-mode SPARSE worktree (`sparse-checkout set lib integrations .tools org docs rcg`). Post-reboot
the leak should be gone; a plain worktree add should work again, sparse is the fallback if memory is tight.
Banked: memory/a-full-worktree-checkout-ooms-under-memory-pressure-use-a-sparse-cone.md.

*(Logged by 2.0.0_SA_COO~ZZZ per Andrew-direct @21382; no new work started; broker summary is current.)*
