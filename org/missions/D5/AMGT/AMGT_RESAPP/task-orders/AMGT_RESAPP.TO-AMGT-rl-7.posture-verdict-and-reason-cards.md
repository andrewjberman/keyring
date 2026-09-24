# AMGT_RESAPP task order -- `AMGT-rl-7` -- POSTURE: the verdict as a headline tile, the reasons as numbered cards with cites folded, an unresolved cite as an icon beside navy text

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rl-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~136</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the posture harness's python fetch READS two public-to-the-estate O-1 objects from s3://opal-data-harvest/posture/v1/ with the seat's ambient credentials; no role, policy or grant moves; no write.
comp-adversary: RUN by the issuer over the L1 brief at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: an S3 GET of two posture objects (the harness's own fetch, already its design). No vendor call, no Bloomberg call, no S3 write or delete.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~136`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`test -f portal/scripts/ui-class-census.mjs && echo INSTRUMENT-OK` (absent = BLOCKING row, stop). Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~136;`. **NEVER RUN AN INSTALL. No vite dev server on this cell.** Never
push, merge, rebase, `checkout --` or `clean`. **Portal is a NESTED repository at `<worktree>/portal`:** portal files are
committed inside it (`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~136 <0.9.0_WK_AMGT_RESAPP~136@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal` and your deliverables. Messages PURE ASCII via the Write tool. Scripts and logs under
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~136/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rl-7` (round 37, decomposition s.45)

**`FWD-26`:** *"the verdict renders as a Stat with the comparable beside it; each reason is a numbered card with cites
folded; an UNRESOLVED cite renders a status.warning ICON beside navy text and NOT amber text. ACCEPT: Status colour never
carries meaning as text on a light ground (C6)."* The walk counted **29 idioms** in `PostureTab.tsx`, the most of any file.

**The target (brief Part V, Posture):** ONE white panel (`Panel variant="nested"`). The verdict (HOLD / BETTER / WORSE /
STEER CLEAR, or MACHINEHOLD / MACHINEABSENT as the object says) as a LARGE local tile (label 13px/700, value at
section-title size, navy; `src/ui/components/Stat.tsx` is a dark idiom and is not used) beside the comparable's display
ticker as a navy link and the as-of; the "machine" chip ONCE in the header with the sentence "a machine's view for a
person to accept or reject" once in the subtitle. Reasons as NUMBERED CARDS in the pillar-card shape (navy numeral header
on a white body, 4px radius, hairline, no shadow), each with a "cites N" disclosure (`<details>`, collapsed by default): a
resolved cite quotes the passage at body size with its accession line at footnote size; an UNRESOLVED cite renders a
`status.warning` ICON beside NAVY text -- never amber text (C6/C9). The evidence-coverage sentence ("N of M cite(s)
resolved ...") becomes a footer line. The comparable's identity, when UNRESOLVED, still says so in words (AMGT-rj-1 is
KEPT). Every empty/loading/error state one of the four designed states (C12): no O-1 object is `PanelEmpty` with the
ABSENT reason, never a bare sentence.

⚠ **THE STARTING STATE YOU INHERIT:** at DEV HEAD `c1ac41ec` in this environment `__harness__/posture.harness.cjs` (yours)
exits 1 with `ENOENT .scratch/posture_BABA_US_Equity.json` -- its python step fetches the two O-1 objects into
`<workspace>/.scratch/` and that landed nothing here. Make the harness's fetch land its files (create the directory it
writes to; print the two S3 keys it read and their byte sizes) or point it at a directory under your deliverables; the
harness's ARMS and EXPECTATIONS do not change.

## 2. BOUNDS

1. **Files:** `tabs/PostureTab.tsx`, `postureCites.ts`, `__harness__/posture.harness.cjs` (yours; make it green), and the NEW
   `__harness__/posturePattern.harness.cjs`. Everything else in the page directory is another cell's this round;
   `src/ui/**`, `src/components/**`, `src/api/**` read-only. `IdentityLine`, `CheckFaceBadge` are being inverted by another
   cell in parallel -- render them unchanged. `PeersTab.tsx` is another cell's; `usePeerSet` for subject AND comparable
   (`PostureTab.tsx:339,347` today) is KEPT exactly -- the Peers/Posture symmetry is graded by the Peers cell's harness.
2. **`postureCites.ts`'s resolution is KEPT:** which cites resolve, against which bundles, and the counts; nothing computed
   on the page (`C-PRESENTATION-ONLY`). The presentation folds; it does not drop a claim, a cite or an absence.
3. **The contract is `portal/DESIGN.md` C1-C12** as in every cell this round.
4. **Standing:** no install, no vendor or Bloomberg call, no S3 write or delete (the harness's GET is its own design), no
   key hunting, no push, no promote. **REFUSE, do not rescue.**

## 3. THE HARNESS YOU ADD -- `__harness__/posturePattern.harness.cjs`

Same loader as `posture.harness.cjs` (actual `PostureTab`, installed typescript, `react-dom/server`; the O-1 objects and
the rj-9 bundles by key exactly as that harness stubs them, plus one render with a claim whose cite is UNRESOLVED and one
with no object). Prints `CHECK <name> <value> (expected <value>)` per line and `CHECKS-OK n of n`; expected counts READ OFF
THE OBJECTS: `panel_is_light` · `verdict_tile_text` == the object's verdict · `comparable_link_present` (a navy link to
`/security-analysis/<comparable>`) · `machine_chip_once` == 1 and `machine_sentence_once` == 1 · `reason_cards` == the
object's basis claims · `cards_numbered` (1..N in order) · `cite_disclosures` == the claims with cites · `resolved_cite_quotes`
== the resolved count postureCites reports · `unresolved_cite_icon_not_amber_text` (the UNRESOLVED cite's markup carries a
warning ICON and NO amber/warning text class) · `coverage_footer` == 1 ("N of M cite(s) resolved") · `absent_object_designed`
(the no-object render is `PanelEmpty`-shaped with the ABSENT reason) · `peers_called_subject_then_comparable`.

## 4. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/postureCites.ts
portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/posturePattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.BA_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.BABA_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.HD_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/components/IdentityLine.tsx
portal/src/pages/SecurityAnalysis/components/CheckFaceBadge.tsx
portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts
lib/research/api/scoped_amgt.py
portal/scripts/ui-class-census.mjs
portal/DESIGN.md
portal/src/ui/components/states/index.ts
portal/src/ui/components/panels/Panel.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~136/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

Of these you WRITE only the first four; `lib/research/api/scoped_amgt.py` is read-only (the harness calls its
`read_posture` through python; you do not edit it).

## 5. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rl-7"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/posturePattern.harness.cjs</invocation><expect>THE BUILT BEHAVIOUR: CHECKS-OK 12 of 12 with every CHECK line printed beside its object-derived expected value -- panel_is_light true, verdict_tile_text equal to the object's verdict, comparable_link_present true, machine_chip_once 1, machine_sentence_once 1, reason_cards equal to the basis claims, cards_numbered true, cite_disclosures equal to the claims with cites, resolved_cite_quotes equal to postureCites' resolved count, unresolved_cite_icon_not_amber_text true, coverage_footer 1, absent_object_designed true, peers_called_subject_then_comparable true</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rl-7"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis/tabs/PostureTab.tsx src/pages/SecurityAnalysis/postureCites.ts</invocation><expect>THE INVERSION IS COMPLETE ON YOUR FILES: FILES 2 TOTAL 0, both lines idiom=0 size=0 weight=0 radius=0 shadow=0 (the walk counted 29 in PostureTab, the largest of any file; a non-zero FAILS)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rl-7"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/posture.harness.cjs; echo "exit=$?"</invocation><expect>THE POSTURE HARNESS IS GREEN WITH ITS ARMS UNCHANGED: the two O-1 objects fetched (the two S3 keys and byte sizes printed), every arm reads its expectation OFF THE OBJECTS, CHECKS-OK n of n and exit 0 -- it exited 1 on ENOENT at DEV HEAD before this cell; an arm weakened or removed to reach green FAILS this criterion</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~136/AMGT_RESAPP.TO-AMGT-rl-7.posture-verdict-and-reason-cards.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** why the
posture harness's fetch landed nothing before and what you changed, the object-derived denominators, the two commit hashes,
and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

# pipeline-override: LIMB 6 only -- the BRIEF half reads STALE at 8da812bf80 (owed by 4.0.0_SA_CRO~Z, asked 05:59Z); R-10 (Andrew-direct 2026-09-23 ~21:2xZ, 'agreed with your rec': the L4-R signature is not a BAR for AMGT, the review is kept) + ADDENDUM B B.6 + 1.0.0_SA_CTO~Z msg 25282 (3) 'no round is held on it'; the review stays owed and is not skipped. The PRD_HEADER key refusal is CLEARED at 8da812bf80; coverage is NOTED at EXECUTING (enrichment recut).

**ISSUER NOTES:** wave 1, spawned after rl-1 merges. The posture harness's ENOENT is recorded in s.45f as the starting
state; the S3 GET it makes is the harness's own pre-existing design, declared in the preflight.

<status>pending</status>
<round>37</round>
<slot>~136</slot>
<fabric>site-z</fabric>
