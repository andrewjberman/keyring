# DSGN_REBRND -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric). Append-only; rows below are minted by their own allocator (`.tools/surprise-row-gate.py` validates every NEW row).

```json
[
  {
    "id": "DSGN_REBRND-S1",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~D",
    "surfaced_at": "2026-09-11T14:52:00Z",
    "one_line": "On /attribution's STYLE VS BENCHMARK POSITIONING panel, the divergence bar's value label is overlapped and visually truncated by the centre target ornament: the ornament reserves no horizontal space and sits at z-20, while the label is positioned bar-relative with no awareness of it, so a small tilt produces a narrow bar whose label overflows toward the axis and is painted over.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D (folded into RB-s-9 by issuer amendment this turn)",
    "spec_asserts": "The PRD's endpoint carries FWD-2 ('an advisor reads a figure without the typeface telling them it came out of a terminal') and the brief's PART III bar 'an advisor reading a return figure cannot tell from its typeface whether it came from the product or a developer's console'. Both presume the figure is LEGIBLE. No cell of decomposition v1 owns collision between a data label and a chart ornament -- RB-s-9 owns spacing and a designed end state, RB-s-11 owned renderer consolidation, and neither reaches a label painted over by a sibling element.",
    "world_is": "Measured by reading portal/src/pages/Attribution/components/StylePolicyComparison.tsx at feature/d13-visual-elevation. (1) The centre ornament at :337-341 is `absolute left-1/2 -translate-x-1/2 z-20` wrapping a `px-3 py-1 rounded-full` pill -- approximately 15px of half-width either side of the zero axis. (2) The underweight container at :298 is `absolute left-0 right-1/2 flex justify-end pr-2` and the overweight container at :316 is `absolute left-1/2 right-0 flex justify-start pl-2` -- each stops 8px short of the axis. 15px of ornament against an 8px gap means the ornament's footprint overlaps each bar's inner edge, and z-20 paints it above the label. (3) The labels are bar-relative: `justify-start pl-4` (:301) and `justify-end pr-4` (:319) inside a bar of `width: barWidth%`, at `text-lg font-bold`. A small tilt yields a narrow bar the label cannot fit inside, and the overflow runs toward the axis and under the ornament. Andrew's screenshot at 14:43Z shows both halves of the failure on one panel: the underweight label reads '-8.7' with the percent sign cut, and the overweight label reads '8.7%' with its leading '+' hidden behind the ornament.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/Attribution/components/StylePolicyComparison.tsx:337-341 read at feature/d13-visual-elevation -- the ornament, z-20, px-3 rounded-full, translate-x-1/2 on the axis",
        "portal/src/pages/Attribution/components/StylePolicyComparison.tsx:298 and :316 -- the bar containers, pr-2 / pl-2, an 8px gap from the axis against the ornament's ~15px half-width",
        "portal/src/pages/Attribution/components/StylePolicyComparison.tsx:301 and :319 -- the labels, justify-start pl-4 / justify-end pr-4, bar-relative and unaware of the ornament",
        "Andrew's screenshot 2026-09-11 14:43Z: underweight label truncated mid-percent-sign; overweight label's leading '+' hidden behind the ornament",
        "This lane's own render of /attribution on the feature branch at 14:48Z returned SKELETON LOADERS with no data, so the collision could NOT be reproduced visually here -- the diagnosis is from source, and a populated fixture is required to prove the fix"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "FOUND BY ANDREW, NOT BY THIS LANE'S SUBTRACTION. Decomposition v1 declared its domain as the 11 write surfaces of the PRD's SURFACE MANIFEST and checked MECE over that -- a label colliding with an ornament inside one component is a member no cell claims, and the subtraction did not surface it because the domain was write-surfaces, not rendered outcomes. That is the Rule 24(i) uncovered-member failure the decomposition's own PART 7 warns about, realised. Folded into RB-s-9 by issuer amendment this turn rather than carried to L10, because RB-s-9 is still pending, already owns the panel layouts, and already requires POPULATED fixtures -- which is the only way this defect can be rendered at all. The fix must change BOTH halves: the ornament must reserve its footprint, and the label must be placed with awareness of it. Changing z-index alone moves the label under the ornament instead of over it and is not a fix."
  },
  {
    "id": "DSGN_REBRND-W1-S1",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T10:57:35Z",
    "one_line": "The project's surprise-channel tree did not exist at all (not just this file) -- this worker created it to have somewhere to append.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- a sibling worker slot (~2, ~3, ...) whose own worktree branched before this commit lands will hit the same missing directory and may independently create the same new file with a different header; the drain reconciles by UNION of rows under one header (IRPT_BCKEND precedent), never by picking one side.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls org/missions/D13/DSGN/DSGN_REBRND/ @b121dee318 (workspace) shows only decompositions/, prd/, project.json, task-orders/ -- no surprise-channel/",
        "ls org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/ @b121dee318 -> 'No such file or directory' (rc=2), and again for its investigations/ subdirectory",
        "org/missions/D13/DSGN/DSGN_REBRND/task-orders/DSGN_REBRND.TO-RB-s-1.token-spine.md <paths> block names this exact file, and RECORD FACE/BOUNDS both instruct appending to it as if it exists"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's <paths> grant and its surprise-row instructions name `org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md` as the append target, matching the pattern of every sibling tree project where the COO opens the channel with a seat row at L6 issuance before any worker TO fires.",
    "world_is": "Neither `surprise-channel/` nor `surprise-channel/investigations/` existed under this project's tree at this worker's start; no opening row from any seat precedes this one. This worker created both, and this file, matching the header shape used by sibling projects (e.g. IRPT_BCKEND) in place of an opener this project never had.",
    "notes": "Not blocking: the <paths> grant covers this file, so creating it is within grant, not an override. Filed so the COO's L8/drain does not read the empty history as 'no surprises found' when it is actually 'no channel existed yet'."
  },
  {
    "id": "DSGN_REBRND-W1-S2",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T10:57:35Z",
    "one_line": "RB1-AC2's own prose asserts the literal-colour-def count reads 60+ at issuance; measured at this worker's start it read 22.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-RB-s-1 ACCEPTANCE, RB1-AC2 prose: 'The count prints beside the verdict; at issuance this reads 60+, so the criterion detects the defect rather than confirming it.'",
        "python regex re.findall(r'--[a-z0-9-]+\\\\s*:\\\\s*(?:#[0-9a-fA-F]{3,8}|[0-9.]+\\\\s+[0-9.]+%\\\\s+[0-9.]+%)\\\\s*;') over portal/src/index.css @102362368f (before this TO's edits) returned LITERAL-COLOUR-DEFS: 22, itemised: --success/--danger/--warning/--info (4), --sentiment-extreme-fear/fear/neutral/greed/chartreuse (5), --model-default (1), --asset-equity/fixed-income/cash/hedge (4), --perf-strong-pos/-dark/weak-pos/-dark/neutral/-dark/weak-neg/-dark (8)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB1-AC2 prose: 'at issuance this reads 60+'.",
    "world_is": "Measured at portal 102362368f (this TO's starting point, unedited index.css): 22 literal colour-def matches, not 60+.",
    "notes": "Not acceptance-bearing: RB1-AC2's <expect> is the printed VERDICT string only ('VERDICT: ONE-WRITER'), and the task order's own BOUNDS state 'No number in this order is an acceptance value except where a criterion prints one' -- the criterion prints VERDICT, not the count. Carried for the CTO's L10 read as a spec-vs-measured mismatch, not a blocker."
  },
  {
    "id": "DSGN_REBRND-W1-S3",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T10:57:35Z",
    "one_line": "portal/design/themes/opal-capital.css was not reproducible by running its own generator against the JSON before this cell, and still is not for the pre-existing Semantic block -- relevant to R3 (canvas and surfaces), which owns collapsing that structure.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bun run --bun against design/tokens/brand-resolver.ts's own resolveBrandTheme+generateCSSVariables, executed against the unedited opal-capital.json, emits only --palette-* (flat, no canonical-navy tiers) and --semantic-* keyed on 'Background/Text/Border/Action/Accent' -- it does not, and structurally cannot, produce the checked-in file's --navy-dark/-medium/-light/-page/-deep/-tooltip/-input/-hover/-hover-light tiers",
        "portal design/brands/opal-capital.json (light) semantic.background.muted = 'darkMode.palette.darkNavyHeader' and semantic.background.contentPanel = 'darkMode.palette.darkNavyCard @ 85%' -- a LIGHT-mode semantic slot pointing into the darkMode palette, pre-existing and unchanged by this cell",
        "this cell repointed semantic.background.default -> palette.canvas and semantic.background.inverse -> palette.darkField in the JSON (verified by re-running the same resolver instrument: --semantic-background-default now resolves to 220 37% 97%, --semantic-background-inverse to 221 67% 12%), but portal/design/themes/opal-capital.css's checked-in Semantic: Background block is left unedited by this cell and still resolves --semantic-background-default through var(--navy-page) (a near-black), not through the corrected canvas value",
        "PRD org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md@8ad762f7bf CELL CANDIDATES row R3: 'the three-tier navy nesting collapses to canvas + ONE container level'; PATHS row: 'portal/src/index.css:52 (--bg-page), :132 (color-scheme: dark)' owned by R3, not R1/R8"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Cell text: 'portal/design/themes/opal-capital.css is GENERATED from it [the JSON]'; PRD CONTRACTS: 'the existing brand-token architecture (IV.4: correct shape, wrong values) ... ONE writer'.",
    "world_is": "The checked-in CSS is hand-tuned, not byte-generated (confirmed by running the generator against the JSON and diffing the shape), and several of its Semantic values still resolve through the pre-rebrand dark-navy tiers even after this cell's JSON-level fix, because propagating that into the hand-tuned CSS without re-deriving the whole Semantic block risked exactly the kind of component-visible recolour this cell's BOUNDS reserve for R3.",
    "notes": "Not a defect of this TO's acceptance: RB1-AC4 tests hex presence in the generated file (satisfied); AC2/AC5 test index.css only (satisfied). Recorded so R3 does not treat opal-capital.css as already reconciled with the corrected JSON."
  },
  {
    "id": "DSGN_REBRND-W1-S4",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T10:57:35Z",
    "one_line": "Two parallel model-portfolio colour systems disagree: the legacy --model-* CSS custom properties (now relocated to data.model / data.chart, values preserved) do not match portal/src/lib/modelPortfolioColors.ts's per-model hex for the same named models.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/index.css (pre-edit) --model-aggressive: var(--danger) = #f5365c (pink-red), while portal/src/lib/modelPortfolioColors.ts 'Ultra-Long Term' (the model the brief's own naming maps 'aggressive' to) = primary #ef4444 (Tailwind red-500) -- different hues",
        "portal/src/index.css (pre-edit) --model-short: var(--warning) = #fb6340 (orange), while modelPortfolioColors.ts 'Short Term' = primary #f59e0b (Tailwind amber-500) -- different hues",
        "grep across portal/src for var(--model-ultra-short|--model-short|...) found 0 files -- confirmed via a narrower grep that DID find the sibling --sentiment-*/--asset-*/--perf-* families consumed in 12 files, so the --model-* CSS mini-palette specifically appears unconsumed in portal/src today"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Cell text / PRD: 'portal/src/lib/modelPortfolioColors.ts is an existing DATA palette -- REUSE it, do not replace it', implying it is THE canonical model-colour source.",
    "world_is": "A second, older, disagreeing model-colour source (the --model-* CSS custom properties) also exists in index.css, and by this worker's grep of portal/src it has no live consumer today, so the disagreement is not currently user-visible -- but the two sources were not reconciled by this cell (out of scope: relocating a value is not redesigning it) and a future consumer of --model-* would render a different colour than getModelColor() for the same named model.",
    "notes": "This cell preserved --model-*'s exact pre-existing values while moving them off the now-changed --success/--warning/--info/--danger status tokens (data.model.defaultFallback, data.chart.*) -- it did not reconcile them against modelPortfolioColors.ts, which the cell text says to reuse, not replace or merge."
  },
  {
    "id": "DSGN_REBRND-W1-S5",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T11:45:59Z",
    "one_line": "RB2-AC4 requires self-hosted Lato .woff2 binaries under portal/public/fonts/; this worker cannot produce them without external vendor egress it is not authorized to perform.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D or 1.0.0_SA_CTO -- needs either Andrew's explicit per-use word for the specific external fetch, or the two files supplied by an already-authorized channel, before RB2-AC4 can be genuinely met (not merely mechanically green -- see DSGN_REBRND-W1-S6).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-RB-s-2 cell text: 'Ship Lato woff2 at 400 and 700 only under portal/public/fonts/, with the OFL text beside them.'",
        "CLAUDE.md Agent Autonomy: 'NEVER call an external vendor API without Andrew's explicit per-use word -- availability is not authorization.' No message in this session carries that word for a Lato-binary fetch.",
        "repo-wide search (python rglob) for *.woff2/*.woff/*.ttf/*.otf and any 'lato'-named file: 0 hits anywhere in the tree (28 raw 'lato' substring hits were all false positives -- 'interpolator'/'calculator')",
        "local search of C:\\Windows\\Fonts (533 installed fonts) and the user font cache: 0 files matching 'lato' -- not available to copy locally either",
        "docs/research/investor_reporting_export_20260910/FONT_LICENSE.txt IS genuinely Lato's SIL OFL 1.1 text (Reserved Font Name 'Lato' header verified) and was copied to portal/public/fonts/OFL.txt -- the licence half of RB2-AC4 is met, only the binaries are missing"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB2-AC4: 'the self-hosted Lato files and the OFL text are present under portal/public/fonts/.'",
    "world_is": "Only the OFL licence text is present. portal/src/index.css carries two @font-face rules pointing at /fonts/lato-400.woff2 and /fonts/lato-700.woff2 (correct once an authorized channel supplies them), and portal/public/fonts/README.md states the gap and its cause. Until the binaries exist, every page renders the font-family stack's fallback (a platform sans-serif), never literally Lato.",
    "notes": "This worker proceeded with everything else this cell covers (Inter/Google Fonts removal, the font-mono and inline-monospace census to zero, the @font-face wiring, the OFL text) rather than halting the whole TO over this one artifact. proof_of_spec marks RB2-AC4 FAIL, honestly, rather than trusting the mechanical invocation's rc=0 (see DSGN_REBRND-W1-S6) -- the TO's own status stays pending, not complete, per its proof_of_spec instruction that a FAIL row withdraws the flip."
  },
  {
    "id": "DSGN_REBRND-W1-S6",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T11:45:59Z",
    "one_line": "RB2-AC4's own invocation ('ls public/fonts/ | head -20; echo rc=$?') prints rc=0 even when public/fonts/ does not exist at all -- the pipeline's exit status is head's, not ls's, so the check cannot discriminate present from absent.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D or 1.0.0_SA_CTO -- a future re-cut of RB2-AC4 should test for the files directly (e.g. a python/test -e check on the two named filenames) rather than a piped ls, so a later accidental deletion of the fonts directory cannot re-pass this criterion silently.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "empirical test: sh -c 'ls public/fonts-does-not-exist/ | head -20; echo rc=$?' on this worktree printed 'ls: cannot access ... No such file or directory' to stderr, THEN 'rc=0' -- the pipeline's reported status is head's (head exits 0 reading an empty, error-free stdin), never ls's",
        "empirical test: the same shape against an EXISTING but EMPTY directory also printed rc=0 -- confirms the check cannot even distinguish 'empty directory' from 'has the two named files'",
        "RB2-AC4's invocation as issued: \"cd <WS>/portal && timeout 120 sh -c 'ls public/fonts/ | head -20; echo rc=$?'\" -- structurally the same shape tested above"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB2-AC4 <expect>rc=0</expect>, read by this worker's task order as: rc=0 means the files are present.",
    "world_is": "rc=0 is returned by this exact invocation regardless of whether portal/public/fonts/ exists, is empty, or holds the two named files -- it is a constant, not a measurement, for this specific check shape.",
    "notes": "Not treated as licence to report RB2-AC4 PASS: this worker's proof_of_spec grades RB2-AC4 by the TRUE presence of the named artifacts (FAIL -- see DSGN_REBRND-W1-S5), not by this invocation's un-discriminating rc. Filed so a future re-run of the literal criterion is not mistaken for evidence either way."
  },
  {
    "id": "DSGN_REBRND-W1-S7",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T11:45:59Z",
    "one_line": "portal/src/index.css was invalid CSS at the merged RB-s-1 vintage -- a comment this worker authored in RB-s-1 ('--chart-*/--data-*') contained an accidental */, prematurely closing the comment and breaking EVERY route; none of RB-s-1's own criteria parse or render CSS, so it was invisible until this cell's RB2-AC5 (ui-smoke) tried to render a page.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.9.0_WK_DSGN_REBRND~1 (this worker) -- DISARMED SAME TURN: fixed in this commit by rewording the comment to '--chart-* and --data-*' (no slash, no accidental closer); `node -e \"require('postcss').parse(...)\"` now reports CSS-PARSE: OK and RB2-AC5's ui-smoke render succeeds (rc=0, resolved canvas rgb(195, 202, 218), page content renders).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RB2-AC5's first run (before this fix), portal HEAD 964fc36150: rc=0 but CANVAS: rgba(0, 0, 0, 0), TEXT: '' (empty) -- the saved PNG showed a Vite error overlay: \"[plugin:vite:css] [postcss] C:/tmp/wk-dsgn-1b/portal/src/index.css:75:41: Unknown word\" citing the RB-s-1 comment text",
        "grep -n '\\*/' portal/src/index.css (pre-fix) showed exactly one occurrence not at an intended comment boundary: line 75, 'Disjoint from --chart-*/--data-* below (AC5): no chart series is ever' -- the substring 'art-*' immediately followed by '/--d' contains the literal sequence '*' then '/'",
        "node -e \"require('postcss').parse(fs.readFileSync('src/index.css','utf-8'))\" printed CSS-PARSE: OK after the fix; RB2-AC5 re-run printed CANVAS: rgb(195, 202, 218) and real page TEXT"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB-s-1's proof_of_spec (org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-1.token-spine.proof_of_spec.json) recorded RB1-AC1..AC5 PASS and proof-of-spec-check.py VALID (rc=0); none of those checks require the CSS to actually parse through PostCSS/Vite.",
    "world_is": "The CSS was syntactically invalid at that same vintage and broke every route's render, discovered only when a LATER cell (RB-s-2) exercised the dev server for the first time since RB-s-1 merged. Fixed in this cell's commit; RB-s-1's own already-merged proof_of_spec is not amended (frozen per spine v3), only this row is added.",
    "notes": "Systemic point for the CTO's L10 read, not just this one bug: no criterion in this project's battery so far actually renders/parses the CSS except RB2-AC5 and RB2-AC6, both introduced only at RB-s-2. A future CSS-only cell (e.g. one that never triggers a ui-smoke render) could reintroduce an equally invisible parse break."
  },
  {
    "id": "DSGN_REBRND-W1-S8",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T12:58:56Z",
    "one_line": "The product's BOLD weight is not a Bold: the cell orders Lato 400 and 700, a real Lato Bold is not on this box, and font-weight 700 is served by the SemiBold face (OS/2 usWeightClass 600) on the issuer's instruction.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- carried to Andrew by the issuer as a design call, not a defect; disarmed for this cell by making the substitution visible in three places (the shipped filename states 600, the @font-face rule states it is served as 700, portal/public/fonts/README.md states both). Fully disarmed only when a real Lato Bold is supplied, which is a one-file drop plus one rule repoint.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-RB-s-2 cell text: 'Ship Lato woff2 at 400 and 700 only under portal/public/fonts/'",
        "read from the faces' OWN tables, not their filenames (fontTools, .scratch/verify_fonts.py): Lato-Regular.ttf family=Lato subfamily=Regular OS/2.usWeightClass=400 sha256 d636e4683231f931eda222d588e944d082bfd3bdba02f928bee461c0f185b251; Lato-SemiBold.ttf subfamily=SemiBold usWeightClass=600 sha256 71b8b7decbe75a881ed267be539d402bd1e9420b799658aada4e0d1bd5af803c; Lato-Light.ttf subfamily=Light usWeightClass=300 sha256 cf2a774503baf418d584f49967bd160e1e03f087c13b25602f28024ec7788f08 -- three faces, no 700 among them",
        "the three .ttf files are the whole of .runtime/codex-seats/4.0.0_SA_CRO/performance-export-recon/fonts/ (3 of 3 entries scanned); no Lato face is installed on this box (C:\\Windows\\Fonts, 533 fonts, 0 matching 'lato') and none exists anywhere in the repo tree",
        "measured on the running page (playwright, /market at 1440): document.fonts holds 'Lato 700 normal status=loaded' and the h1 computes font-weight 700 with font-family beginning 'Lato' -- so the 700 slot IS live and IS being painted by the 600 face"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cell orders two weights, 400 and 700, on the measured finding that the brand book and opalinvest.com both ship exactly those two ('weights exclusively 400/700 on all 3 pages').",
    "world_is": "Only 300/400/600 exist on this box. 700 is served by the 600 SemiBold face, so every bold figure and heading in the product is ~100 weight units lighter than the measured site's bold. Nothing in the render is broken by this; it is a fidelity gap against the measured system, not a defect in the page.",
    "notes": "Supersedes the BLOCKING half of DSGN_REBRND-W1-S5: the binaries ARE now shipped (the issuer staged the .ttf faces into this worktree from a gitignored .runtime/ path that no fresh worktree carries, and conversion to woff2 was LOCAL -- fontTools + brotli, no network, and none was authorized). What remains open from S5 is only the 700 weight. The Light 300 face was deliberately NOT shipped: no @font-face rule references it and the cell restricts the product to two weights; its hash is recorded in portal/public/fonts/README.md so the decision is visible rather than silent."
  },
  {
    "id": "DSGN_REBRND-W1-S9",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T14:23:08Z",
    "one_line": "The canvas cannot reach its measured surface share from inside this cell's <paths>: 4,887 light-on-dark idioms in 171 page files outside the grant require the containers behind them to stay inverted, so the panels became ENUMERATED bands rather than white surfaces.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- turning the 449 enumerated band instances into white surfaces needs a cell whose <paths> includes portal/src/pages/**, because the text inside them must be repainted in the same act. Until then the product reads as a light page with large deliberate bands, not as the measured 56-67% canvas.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "census over portal/src/pages (171 .tsx files, all outside this cell's <paths>): text-white 2193, text-white/N 1625, bg-white/N 501, border-white/N 568 = 4887 light-on-dark idioms; the same census over the granted scopes returns 707 (components) and 226 (ui)",
        "portal/src/ui/components/panels/Panel.tsx's own pre-existing contract names this dependency: variant chart/mixed is documented DARK with 'White-text idiom is legal inside. (Case A)' -- the 4,887 occurrences are that contract being used",
        "band-producing surfaces enumerated at this vintage: Panel variant=chart|mixed 144 in 71 files, page-level bg --bg-header 202 in 68, --semantic-background-contentPanel 66 in 12, --bg-card 28 in 21, NestedCard 8 in 3, DarkCard 1 in 1 = 449 band instances",
        "measured target for comparison, design/brand/opalinvest.com.json: canvas surfaceSharePct [67.1, 64.0, 56.3], darkField [31.1, 20.9, 20.3]"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB-s-3: 'The canvas becomes #F4F6FA ... Collapse the nesting. Every rendered route is three rounded containers deep ... Two states only: on the canvas, or an inverted #0A1733 band', and RB3-AC6 grades that 'the canvas reads as one near-white field'.",
    "world_is": "The canvas IS #F4F6FA and the nesting IS collapsed (three navy tiers -> one band value; ui-smoke prints rgb(244, 246, 250) on both graded routes). What is NOT achieved is the measured SURFACE SHARE: the bands still occupy most of both routes, because turning them white would leave 4,887 page-level light-on-dark idioms unreadable and this cell cannot edit the files that carry them. Every band is therefore enumerated with its reason in the result file rather than silently left dark.",
    "notes": "Not a request to widen this cell -- the BOUNDS say a path this cell needs and does not have is a row, never an override, so this is the row. The token and primitive layer is now positioned so that repainting is a one-line change per call site rather than a re-architecture: a page that swaps its text-white for the ink token gets a white surface by changing its Panel variant from chart/mixed to nested."
  },
  {
    "id": "DSGN_REBRND-W1-S10",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T14:23:08Z",
    "one_line": "184 occurrences across 30 files colour TEXT with a BACKGROUND token (text-[hsl(var(--bg-header))]), which is why the page title rendered invisible at 1:1 the moment a real dark mode existed; 64 were repaired in grant, 120 in 20 page files were not.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- the 120 occurrences under portal/src/pages/ need a cell granted those paths. Until then the retained dark mode renders those strings at or near 1:1 wherever the page uses the idiom.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DOM probe of /market: h1 className 'text-3xl font-bold text-[hsl(var(--bg-header))] tracking-[0.025em] uppercase'; computed colour rgb(10, 23, 51) in light (16.4:1 on the canvas, passes) and rgb(11, 17, 29) in dark ON rgb(11, 17, 29) -- 1:1, invisible",
        "census of the idiom: 184 occurrences in 30 files; 64 in 10 files under portal/src/components and portal/src/ui were repointed onto the ink token text-[hsl(var(--foreground))] by this cell; 120 in 20 files under portal/src/pages are outside its <paths>",
        "after the in-grant repair the same DOM contrast sweep reports /market LIGHT 9 of 9 pairs passing and the title at 16.4:1; no title pair remains at 1:1 on either graded route"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB3-AC7 requires every text/background pair to meet WCAG 2.1 SC 1.4.3 in the selected dark mode as well as on the canvas and the bands.",
    "world_is": "A token used as BOTH a fill and an ink cannot be re-themed without breaking one of its two roles: --bg-header must equal the dark surface in dark mode, and ink equal to its own background is invisible by construction. The idiom passed for years only because the old product had no reachable dark mode -- this cell made one reachable, which is what surfaced it.",
    "notes": "Generalises beyond this project and is offered for the round analysis: the defect is not the value, it is the ROLE COLLISION. A background token read as ink is a latent 1:1 pair waiting for the first theme that moves it."
  },
  {
    "id": "DSGN_REBRND-W1-S11",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T14:23:08Z",
    "one_line": "In the selected dark mode NO accent colour of any hue can satisfy both of the roles the product gives it -- white-on-accent and accent-on-band both at 4.5:1 -- because the two luminance bounds do not overlap; this is arithmetic, not a tuning miss.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "white text on the accent fill requires the accent's relative luminance <= 1.05/4.5 - 0.05 = 0.1833; accent text on the dark-mode band (rgb(11,17,29), luminance 0.0055) requires >= 4.5*(0.0055+0.05) - 0.05 = 0.2002",
        "exhaustive search over hue 240-265, saturation 40-100%, lightness 30-85% (a 26 x 13 x 56 grid): 0 values satisfy both constraints",
        "measured on the running page in dark mode: white on accent 4.31:1 and accent on band 4.39:1 -- both just under the bar, from opposite directions, which is the signature of the conflict rather than of a bad value"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB3-AC7: every text/background pair, including in the selected dark mode, meets WCAG 2.1 SC 1.4.3.",
    "world_is": "Both accent pairs sit at 4.27-4.39:1 in dark mode and cannot both be lifted by changing the accent. The resolution is a DESIGN decision, not a value: either the accent fill carries dark text instead of white, or the accent splits into a fill token and an ink token with different luminances. Both are accent-vocabulary decisions, which the PRD gives to R5 (accent rationing and one set of controls), not to this cell.",
    "notes": "Light mode is unaffected and passes both pairs comfortably (6.52:1 white-on-accent, 6.03:1 accent-on-canvas), because the canvas gives the accent-as-ink role a bright background to work against. The conflict exists only where the accent must read against a near-black field."
  },
  {
    "id": "DSGN_REBRND-W1-S12",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T14:55:00Z",
    "one_line": "RB3-AC5's own pattern has a wildcard that crosses newlines, so any radius-token USAGE in index.css makes it read past the usage and grade the NEXT declaration's value as an off-band radius -- it printed MID-RANGE twice while all five radius tokens were in band.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D or 1.0.0_SA_CTO -- a future re-cut should anchor the criterion per LINE so a token USAGE cannot be read as a DECLARATION. Disarmed for this cell by writing the one usage as a literal that mirrors the token, so the criterion reads only the five declarations and prints SHARP.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "first firing: with border-radius set from the control token, the criterion printed RADII ending in 'inherit' with OFF-BAND ['inherit'] -> MID-RANGE. 'inherit' is the font-inheritance declaration two lines BELOW the usage, not a radius at all",
        "second firing: a code comment added to explain the first firing NAMED the pattern, and the criterion then matched its own quoted text, reporting a fragment of the regex as an off-band value rather than any CSS value",
        "after writing the single usage as a literal and describing the pattern in words instead of reproducing it: RADII ['2px', '3px', '4px', '720px', '50%'] OFF-BAND [] -> SHARP, with the five radius TOKENS unchanged across all three runs",
        "the same shape had already fired twice in this cell on other instruments: the theme rewriter's own assert matched the retired token names inside its own retirement note, and RB2-AC4's predecessor could not distinguish an absent directory from a present one (row W1-S6)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB3-AC5: 'every radius token sits in the 2/3/4px band (or a pill/circle)', graded by a pattern over portal/src/index.css.",
    "world_is": "The pattern grades radius DECLARATIONS and radius USAGES alike, and its wildcard spans newlines, so what it reports after a usage is whatever declaration comes next in the file. Verdict and property can therefore disagree in both directions: it printed MID-RANGE on a file whose every radius token was in band, and it would print SHARP on a file using an off-band literal radius anywhere outside a token declaration.",
    "notes": "PROCESS NOTE, the more useful half: this worker checked RB3-AC5 early, kept editing, flipped <status> to complete, and only then re-ran the whole battery -- which is when the regression appeared. The flip was made while the criterion printed MID-RANGE. It was caught by the post-flip re-run, repaired, and re-verified rather than left standing, and the proof instance and result file state the sequence. The rule that would have prevented it: re-run every mechanical criterion against the FINAL tree immediately before the flip, never against an intermediate one."
  },
  {
    "id": "DSGN_REBRND-W2-S1",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-11T11:06:54Z",
    "one_line": "TopicCloud.tsx's @visx/wordcloud spiral layout has no recharts equivalent -- migrating it would replace a spatial word-size/position cloud with a categorical chart type, changing WHAT the chart shows, so RB11-AC2/AC3 stay MULTI-RENDERER/STILL-DECLARED by the order's own rule.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D",
    "spec_asserts": "TO-RB-s-11: 'Migrate onto the incumbent: the 4 apexcharts files, the 1 nivo file and the 1 visx file move to recharts' and 'â›” A chart that cannot migrate without changing WHAT IT SHOWS is a SURPRISE ROW, never a quiet exception. File the row and stop on that criterion. Changing a chart's content to make a migration succeed is out of scope and is a failure.' RB11-AC2 expects VERDICT: ONE-RENDERER (apexcharts+@nivo+visx+phosphor-react all read zero importing files); RB11-AC3 expects all 8 named packages REMOVED from package.json.",
    "world_is": "portal/src/components/market-performance/TopicCloud.tsx renders a sentiment-coloured word cloud via @visx/wordcloud's Archimedean-spiral layout (variable per-word font size 10-20px and (x,y,rotate) placement solved by the library) plus @visx/text for per-word SVG text. recharts (^3.7.0) ships no word-cloud/tag-cloud chart type -- its component set is Cartesian/radial (Area/Bar/Line/Pie/Radar/RadialBar/Scatter/Treemap/Sankey/Funnel), none of which can render a spatial cloud of variably-sized, variably-positioned words without becoming a different visualization (e.g. a ranked bar list of the same keywords), which changes the CONTENT the chart presents, not just its chrome. The 4 apexcharts donuts (ModelPortfolios.tsx, AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx, AdvisorIntelligence/_shared/AdvisorPublicProfile.tsx, AdvisorIntelligence/_shared/tabs/DistributionTab.tsx) and the 1 @nivo/radar chart (FactorTilts/panels/FactorTiltOverviewPanel.tsx) WERE migrated onto recharts (same chart type, same data, same click-to-select and center-label behaviour, same custom benchmark-parity ring and per-factor label offsets on the radar) -- verified by a clean typecheck AND a live browser render of each (the radar chart's render was confirmed with a real data fixture, not just the empty state). This visx word cloud is the one holdout. Measured after every other migration: apexcharts and @nivo now read 0 importing .tsx files (were 4 and 1 at issuance); visx still reads 1 (TopicCloud.tsx, unchanged); phosphor-react already read 0 importing .tsx files at issuance (see DSGN_REBRND-W2-S3). portal/package.json still declares @visx/text and @visx/wordcloud (both genuinely imported by TopicCloud.tsx) after this cell removed apexcharts, react-apexcharts, @nivo/core, @nivo/radar, @visx/scale (confirmed zero importers anywhere in portal, safe to drop) and phosphor-react. RB11-AC2 therefore reads RETIRED-IMPORTS:1 / VERDICT:MULTI-RENDERER and RB11-AC3 reads RETIRED-STILL-PRESENT:2 ['@visx/text','@visx/wordcloud'] / VERDICT:STILL-DECLARED -- both correctly, by the order's own stop-on-that-criterion rule.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/market-performance/TopicCloud.tsx@102362368f -- imports { Text } from '@visx/text' and { Wordcloud } from '@visx/wordcloud'; spiral='archimedean', per-word fontSize/rotate/(x,y) solved by the library, colour from getSentimentColor",
        "measured (python census, AC2's own methodology) over portal/src rglob('*.tsx') after every other migration landed: LIB-FILE-COUNTS {'lucide-react':99,'recharts':36,'visx':1} RETIRED-IMPORTS:1 VERDICT:MULTI-RENDERER -- apexcharts and @nivo both read 0",
        "measured (python census, AC3's own methodology) over portal/package.json dependencies after this cell's edit: RETIRED-STILL-PRESENT:2 ['@visx/text','@visx/wordcloud'] VERDICT:STILL-DECLARED; both packages have a live importer (TopicCloud.tsx), so removing them would leave a genuine import unresolved on the next clean install even though the pre-populated node_modules junction would mask it today",
        "recharts 3.7.0's exported chart components (successful `bun run typecheck` importing RadarChart/PolarGrid/PolarAngleAxis/PolarRadiusAxis/Radar/PieChart/Pie/Cell/Customized from 'recharts', rc=0) contain no Wordcloud/TagCloud member; recharts ships no such chart type",
        "portal/src/components/market-performance/SentimentGauge.tsx renders TopicCloud on the /market route -- org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/rb-s-11_market_1440.png (RB11-AC5's own required capture) shows the unmigrated word cloud's honest-empty state ('No keywords available') under the smoke harness's unfixtured run"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "DSGN_REBRND-W2-S2",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-11T11:06:54Z",
    "one_line": "portal/vite.config.ts's build.rollupOptions.manualChunks still names 'vendor-apexcharts':['apexcharts'] and 'vendor-nivo':['@nivo/core','@nivo/radar'] after this cell retired both from package.json and from every .tsx importer; the file sits outside RB-s-11's <paths> grant so it was not edited.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-RB-s-11 <paths> grants only portal/package.json, portal/src/, portal/bun.lock and this investigation file; the order does not name portal/vite.config.ts, and BOUNDS states a path not named is a blocking row on the criterion it blocks -- but no acceptance criterion here requires editing it (AC1 is tsc, not a production build; AC5 is `bun run dev`).",
    "world_is": "portal/vite.config.ts lines 16-23 declare build.rollupOptions.output.manualChunks with 'vendor-apexcharts': ['apexcharts'] and 'vendor-nivo': ['@nivo/core', '@nivo/radar'] -- both packages this cell removed from package.json and whose last .tsx importers this cell migrated onto recharts. Neither AC1 (`bun run typecheck` = `tsc -b --noEmit`, which does not evaluate whether rollupOptions' string entries are actually imported) nor AC5 (`bun run dev`, and manualChunks is consulted only by `vite build`, never by the dev server) reads any different output because of this. Left unedited because the file is not in <paths>. Consequence for a future `vite build`: the two vendor chunk names would bundle whatever the still-present node_modules packages contain despite nothing importing them (dead weight), or Rollup may emit a near-empty chunk for each -- a production-bundle cleanliness question, not a functional break, since the packages remain physically resolvable via the pre-existing node_modules junction either way.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/vite.config.ts@102362368f lines 16-23 -- manualChunks object listing 'vendor-apexcharts': ['apexcharts'] and 'vendor-nivo': ['@nivo/core', '@nivo/radar'], alongside 'vendor-recharts': ['recharts'] which stays correct",
        "measured: `bun run typecheck` rc=0 with apexcharts, react-apexcharts, @nivo/core, @nivo/radar already absent from portal/package.json's dependencies in this cell's own working tree -- tsc's project build does not evaluate vite.config.ts's rollupOptions contents against actual import usage",
        "portal/package.json (this cell's edit, same commit as this row) -- apexcharts, react-apexcharts, @nivo/core, @nivo/radar, @visx/scale, phosphor-react, framer-motion removed from dependencies; motion, @visx/text, @visx/wordcloud, recharts, lucide-react retained"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "DSGN_REBRND-W2-S3",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-11T11:06:54Z",
    "one_line": "The order's measured-duplication line 'phosphor-react 1' file was a README, not code: zero .tsx/.ts files anywhere in portal import phosphor-react at issuance, so RB11-AC2's phosphor-react count already read zero before this cell touched anything, and RB11-AC3's phosphor-react removal needed only a package.json edit, no lucide migration.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-RB-s-11: 'Icons: lucide-react 102 files, phosphor-react 1.' and 'the 1 phosphor file moves to lucide.'",
    "world_is": "The only repo hits for the string 'phosphor-react' (any case) are portal/src/components/TrendingTopicImage.README.md (documentation for a Lambda-side social-share-image renderer, describing a component that is not present as a .tsx file in this repo), portal/package.json's dependency line, and portal/bun.lock. Zero .tsx or .ts files under portal/src import 'phosphor-react' or a Phosphor icon component. The '1 phosphor file' the order's census counted was therefore the README, not an importing code file; RB11-AC2's script (which globs *.tsx only) already read phosphor-react at 0 before this cell's edits. No lucide-react migration of a call site was possible or needed because there was no call site; the only available act -- removing the now-orphaned phosphor-react line from package.json -- was taken.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "grep 'phosphor-react' case-insensitive over portal/ (pre-edit) -- 3 hits: portal/src/components/TrendingTopicImage.README.md, portal/package.json, portal/bun.lock; 0 hits in any .tsx or .ts file",
        "measured (python census, AC2's own methodology) over portal/src/**/*.tsx before this cell's edits: 0 files containing the substring 'phosphor-react'",
        "portal/src/components/TrendingTopicImage.README.md@102362368f -- describes rendering trending-topic icons via the Phosphor React icon library for a Lambda-generated social image; no sibling TrendingTopicImage.tsx exists in the same directory"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "DSGN_REBRND-W2-S4",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-11T11:40:17Z",
    "one_line": "The RB-s-11 amendment was checked out into this worktree but the MERGED channel document was not: the issuer's instruction describes a 6-row union (W1-S1..S4, W3-S1..S2) while this worktree's copy holds only this worker's 3 rows, so the union is still owed at the drain -- on a file whose two sides are an add/add conflict by construction (CLAUDE.md 14b, measured 3 of 3 on an earlier round's drains).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D",
    "spec_asserts": "The issuer's RB-s-11 drain instruction: 'the channel now holds 6 rows from two workers (W1-S1..S4, W3-S1..S2) merged by union, so append to it as you find it.' The amended task order itself WAS placed in this worktree (staged, not merged) and is what this worker re-read and executed against.",
    "world_is": "MEASURED in this worktree immediately before appending this row: the project has exactly ONE channel document visible here (org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md) carrying exactly THREE row ids -- DSGN_REBRND-W2-S1, -W2-S2, -W2-S3 -- byte-identical at the worktree and at HEAD 0f88ccde18, with no W1 or W3 row present. So 'append to it as you find it' is executable exactly as written and this row is minted collision-free (the W2 allocator coordinate cannot collide with W1's or W3's sequence by construction, which is what the coordinate exists for), but the 6-row union the instruction describes does not exist on this branch and cannot be verified from here. The union therefore still has to be produced at the drain, where BOTH sides created the same path with disjoint content: a git merge of that is an add/add conflict, and the failure mode of a careless resolution is not a loud break but a SILENT ROW DROP of whichever side is discarded (three rows either way). The issuer's own word 'union' is already the correct resolution; what this row adds is a checkable bar for it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured (python over the worktree AND over `git show HEAD:<path>`): WORKTREE ids ['DSGN_REBRND-W2-S1','DSGN_REBRND-W2-S2','DSGN_REBRND-W2-S3']; HEAD ids identical -- denominator 1 document, 3 rows, for pathspecs org/surprise_channel/DSGN_REBRND/* and org/missions/D*/*/DSGN_REBRND/surprise-channel/*/*",
        "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@0f88ccde18 -- the committed 3-row state this worker created; nothing has modified it since (git status clean for that path before this append)",
        "the amended order org/missions/D13/DSGN/DSGN_REBRND/task-orders/DSGN_REBRND.TO-RB-s-11.one-renderer.md IS present here as a STAGED modification over 845cb2b6ac, which is how this worker read the new AC2/AC3 -- so the checkout mechanism reached the task order and not the channel",
        "CLAUDE.md 14b: 'an APPEND-ONLY SHARED file -> DO NOT ISOLATE ... two branches appending to one channel land at the SAME OFFSET and both restate the header, so a side branch converts a SECONDS-LONG STAGING RACE into a GUARANTEED CONFLICT -- measured 3 of 3 on round 4's drains (NFRA_CLDGRPH-S36)'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "ARMED against the DRAIN, not against this cell: nothing here is wrong today and no act of RB-s-11 is blocked. Disarm act, owned by the issuer that performs the merge: resolve the channel by UNION and then MEASURE the result -- the merged document must carry all four W2 ids (S1..S4) plus all six of W1's and W3's, i.e. 10 distinct ids and no id lost; a post-merge id-set read is the check, because the row gate grades only rows NEW in a commit and will not re-grade a row a bad resolution silently deleted. This worker cannot perform or verify that merge: it is forbidden to merge, and the other side is not visible from this branch."
  },
  {
    "id": "DSGN_REBRND-W3-S1",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~3",
    "surfaced_at": "2026-09-11T10:45:00Z",
    "one_line": "No route or panel in portal/src renders an observable NO-PERMISSION state today -- every access denial found (route-level requireAdmin/requireInternal/firm-allowlist, a panel-level element hide, and one transient toast) is non-rendering, so this inventory cannot cite a fixture or a render for that state anywhere.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D (RB-s-13 issuance) and 0.9.0_WK_DSGN_REBRND~1 (RB-s-10, the cell chartered to design the NO-PERMISSION state)",
    "spec_asserts": "This cell's own face and RB-s-10's face both list 'no-permission' as one of the designed states this project's inventory covers, on equal footing with empty/loading/error/default/toggled-panel -- RB-s-10's face: 'Four designed states, in the existing component set: EMPTY, LOADING, ERROR, NO-PERMISSION. Every panel with nothing to show uses exactly one of them.'",
    "world_is": "Measured across portal/src at this vintage: (1) ROUTE-LEVEL -- ProtectedRoute.tsx's requireAdmin (lines 39-40), requireInternal (lines 44-46) and the firm-allowlist check isPathAllowedForFirm (lines 57-59, reading portal/src/lib/firmAccess.ts) each resolve to a silent Navigate-replace to /login, /market or FIRM_DEFAULT_LANDING -- the denied route's component tree never mounts, so there is nothing to screenshot. (2) PANEL-LEVEL -- /advisor-intelligence's AdvisorPublicProfile.tsx (permissionScopeFor/canSeeBookToggle, reading portal/src/lib/permissionGroups.ts) and /trade-submission's useTradeSubmissionState.ts both OMIT an element outright rather than rendering a message. (3) TOAST -- /portfolio-management's UploadPortfolioModal.tsx line 300 fires a transient toast.error() on a blocked action, which is not a page/panel state. Zero of the three is a fixture-able or screenshot-able STATE; a case-insensitive census for 'permission' across portal/src/pages (comp-find, all-corpus, 468 files scanned) found no fourth mechanism.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/ProtectedRoute.tsx lines 39-40, 44-46, 57-59, read at portal HEAD 102362368fe9fc2a293f29c77b7b134e20f43d3f -- three separate denial branches, each a Navigate-replace, none a rendered message",
        "portal/src/lib/firmAccess.ts FIRM_ALLOWED_PATHS for 49financial and inflection, read at the same vintage -- neither allowlist includes /attribution, /factor-tilts, /correlations, /security-scanner, /portfolio-management, /data-refresh, /ticket-center, /investor-reporting, /investor-reporting/print or /dev/page-surface-control, and every one of those denials routes through the same isPathAllowedForFirm branch in ProtectedRoute.tsx",
        "comp-find 'permission' -i portal/src/pages (corpus=all, 468 files scanned): 22 hits, none a rendered no-permission component; the closest is portal/src/pages/PortfolioManagement/components/UploadPortfolioModal.tsx line 300, toast.error('You do not have permission to upload portfolio files.'), a transient toast",
        "portal/src/pages/AdvisorIntelligence/_shared/AdvisorPublicProfile.tsx line 1201, 'const hideBookToggle = !canSeeBookToggle(permissionScope)' -- omits an element, does not render one"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Recorded in design/brand/portal-surface-inventory.json as a top-level no_permission_state_gap field and on the two route-level-gated rows (/ticket-center, /data-refresh, state=no-permission), rather than worked around: this worker's grant is the inventory file and this channel only, and deciding whether NO-PERMISSION should stay a silent redirect or become a rendered state is an information-architecture call the PRD preamble reserves ('Information architecture is out of scope' -- RB-s-3 and RB-s-9 bounds), not a call this cell or this worker makes."
  },
  {
    "id": "DSGN_REBRND-W3-S2",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~3",
    "surfaced_at": "2026-09-11T10:46:00Z",
    "one_line": "This cell's own face and RB12-AC2's own prose assert 'at issuance the router reads 26'; RB12-AC2's own invocation, run at this vintage, prints APP-ROUTES: 24 -- the 26 counts raw Route elements including the two wildcard entries the same invocation's own set-comprehension excludes by name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-RB-s-12 RB12-AC2's prose: the inventory's printed denominator equals the router's own route count, and 'At issuance the router reads 26 and the inventory does not exist.'",
    "world_is": "Running RB12-AC2's own invocation verbatim against portal/src/App.tsx at portal HEAD 102362368fe9fc2a293f29c77b7b134e20f43d3f: the raw regex used by that invocation returns 26 matches, two of which are the literal strings that mark the DashboardLayout catch-all route and the top-level route that mounts DashboardLayout itself; the SAME invocation's own set-comprehension explicitly excludes those two literal values before taking the set, so its printed route count is 24, not 26. This inventory's route_count is 24, matching what RB12-AC2 actually verifies -- confirmed by running RB12-AC2's exact command against this inventory, which printed VERDICT: AGREES. The mismatch is confined to the order's narrative prose (or to a staler router state than the one now live), not to the mechanism the order names.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Standalone run of RB12-AC2's regex against portal/src/App.tsx at portal HEAD 102362368fe9fc2a293f29c77b7b134e20f43d3f printed: ALL MATCHES (raw, with dups): 26; DEDUP EXCLUDING wildcard entries: 24",
        "RB12-AC2's own invocation, run verbatim against design/brand/portal-surface-inventory.json, printed: APP-ROUTES: 24 INVENTORY-DENOMINATOR: 24 / VERDICT: AGREES"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No act taken beyond using the mechanism's own live output (24) as this inventory's route_count rather than the prose's 26. Marked INERT rather than ARMED: the checker recomputes the route set fresh from portal/src/App.tsx on every run rather than trusting a stored 26, so no persistent wrong value can propagate from this mismatch into a future grading pass."
  },
  {
    "id": "DSGN_REBRND-W1-S13",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T16:38:33Z",
    "one_line": "RB4-AC4 cannot see the defect it names and cannot be satisfied without breaking this cell's own BOUNDS: the duration ladder is hex constants, not Tailwind classes, so 0 of the 113 hue occurrences the criterion counts belong to the ladder.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D or 1.0.0_SA_CTO -- a re-cut should grade the LADDER's resolved colours (the DOM, or the four source constants) rather than Tailwind class tokens in any file that merely mentions UST and ULT. Until then the criterion reads MULTI-HUE on a tree where the ladder is a single ramp.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the ladder's colours are hex constants, not Tailwind classes: pages/Attribution/constants/holdings-shared.tsx PORTFOLIOS used PALETTE.orange500/amber500/green500/blue500/red500, lib/modelPortfolioColors.ts primaries #f97316/#f59e0b/#10b981/#3b82f6/#ef4444, lib/chartColors.ts MODEL_COLORS, and pages/Positioning/tabs/HoldingsTab.tsx BOOK_COLOR_CYCLE -- the criterion's regex matches none of these forms",
        "holdings-shared.tsx -- the /attribution ladder the cell names and Andrew screenshotted -- contains ZERO Tailwind hue tokens, so the criterion is blind to that route's ladder entirely",
        "attribution of every occurrence the criterion DOES count, across the 13 files it selects: categorical column groups 13, sign/diverging 38, status 1, other categorical 64 -- and THE LADDER 0 of 113",
        "measured after the ladder was fixed and DOM-verified as a single monotonic ramp (swatch luminance 0.713 > 0.525 > 0.367 > 0.244 > 0.152): the criterion still prints LADDER-FILES: 13 DISTINCT-HUES: 9 -> MULTI-HUE, unchanged from issuance",
        "this cell's BOUNDS: 'Do not touch a categorical palette. Only encodings of ORDER change.' and 'Chart series that are NOT ordered keep their colour' -- the 9 hues are exactly those categorical and sign encodings"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB4-AC4: 'the duration ladder resolves to AT MOST ONE named hue family', graded by collecting Tailwind hue tokens from every .tsx containing both UST and ULT.",
    "world_is": "The criterion selects files by a text co-occurrence and then grades EVERY hue token in them, so it measures the categorical column banding, the green/red sign colouring and one status red -- none of which is the ladder, and all of which this cell is forbidden to change. Driving it to ONE-HUE would require desaturating a categorical palette, which the same order prohibits in its BOUNDS.",
    "notes": "The cell's SUBSTANCE was done and is evidenced elsewhere: four independent sources of the ladder encoding were unified onto one hue, verified in the DOM in both modes, and the /market gauge arc is a ramp instead of a rainbow (RB4-AC2/AC3 renders, read). This row is about the instrument, not the work. The worker did not edit a categorical palette to make a criterion green."
  },
  {
    "id": "DSGN_REBRND-W1-S14",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-11T16:38:33Z",
    "one_line": "ONE ordered encoding -- the duration ladder -- had FOUR independent writers, and fixing the first three moved nothing on screen; only reading the DOM after each edit found the fourth.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- all four now carry the same ramp, so the product is consistent TODAY, but nothing prevents them drifting apart again. A later cell should collapse them onto one exported source; this cell unified the VALUES without re-architecting the ownership.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the four: lib/modelPortfolioColors.ts (canonical models + 8 aliases), lib/chartColors.ts MODEL_COLORS, pages/Attribution/constants/holdings-shared.tsx PORTFOLIOS, pages/Positioning/tabs/HoldingsTab.tsx BOOK_COLOR_CYCLE",
        "after editing the first source the DOM probe of the /positioning chips still returned the OLD five hues rgb(249,115,22) rgb(245,158,11) rgb(16,185,129) rgb(59,130,246) rgb(239,68,68); after the second, unchanged; after the third, unchanged; only after BOOK_COLOR_CYCLE did they become rgb(212,220,237) ... rgb(52,103,213)",
        "vite was serving the edited module correctly at each step (curl of the transformed module showed the new hexes), so the staleness hypothesis was excluded before continuing -- the render was right and the assumption about the source was wrong"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cell names one defect -- the duration ladder in five unrelated hues -- as though it had one source to correct.",
    "world_is": "It had four, in three different directories, two of them named as if they were the canonical palette ('modelPortfolioColors', 'MODEL_COLORS'). A per-source verification would have reported success three times while the screen was unchanged.",
    "notes": "Generalises: this is Rule 22's shared-dependency blindness inverted -- not one dependency beneath many members, but many writers beneath one rendered property. The only check that could distinguish them was reading the rendered value, which is the same lesson as row W1-S7."
  },
  {
    "id": "DSGN_REBRND-W1-S15",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T02:10:30Z",
    "one_line": "Amendment 1 KEEPS the two ReturnVolatilityScatter benchmark colours as non-canon ramp work, but before this cell they WERE the canon ULT red and LT blue, in constants named for the rungs -- and rb4-canon-check.py reads no grammar that sees them, so CANON-INTACT passes with both off canon.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- rule which clause governs these two constants: the KEEP list, or the CANON LOCK ('no act of this order may move' the five). If canon governs, the disarm is a two-line revert of ULT_COLOR/LT_COLOR to #EF4444/#3B82F6 plus a fifth grammar (`const <RUNG>_COLOR =`) in rb4-canon-check.py. Left as the order instructs (KEPT) by this worker.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/components/ReturnVolatilityScatter.tsx:121-122 @0e87cb9f99^ (pre-cell): `const ULT_COLOR = '#ef4444'  // Red` and `const LT_COLOR = '#3b82f6'  // Blue`, under the comment `// Colors for shared benchmark (ULT benchmark serves both ULT and LT)` -- byte-equal to canon ULT #EF4444 and LT #3B82F6",
        "portal src/components/ReturnVolatilityScatter.tsx:121-122 @0e87cb9f99: `'#183B86'  // ordered-scale ramp step 5 of 5 (was Red)` and `'#2650AB'  // ordered-scale ramp step 4 of 5 (was Blue)` -- unchanged by this worker's revert commit, per the KEEP instruction",
        "task order DSGN_REBRND.TO-RB-s-4 @1cceadbf81, 'What this cell KEEPS': '... and the two ordered benchmark colours in ReturnVolatilityScatter. None of those is canon'; same file, BOUNDS: 'UST #F97316 / ST #F59E0B / INT #10B981 / LT #3B82F6 / ULT #EF4444 are locked by Andrew'",
        "rb4-canon-check.py @1cceadbf81 reads ARM A `id: '<RUNG>'` / `name: '<long name>'`, ARM B the two arrays BOOK_COLOR_CYCLE and MODEL_COLORS, ARM C legacy-name keys in a file carrying 'Aggressive'/'Conservative' -- none matches `const ULT_COLOR =`; run on this worker's final tree it printed 23 sites across 4 files, none in ReturnVolatilityScatter.tsx, and VERDICT: CANON-INTACT"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Amendment 1: the two ordered benchmark colours in ReturnVolatilityScatter are among the ramp work that STANDS, 'None of those is canon'; RB4-AC4R certifies 'the canonical duration ladder is intact at every site'.",
    "world_is": "Those two colours are the ULT and LT benchmarks, and pre-cell they carried exactly the canon ULT and LT hexes by name and value. They are now navy ramp steps 5 and 4, so the scatter renders the ULT/LT benchmarks off canon while every other ULT/LT site is back on canon, and the canon checker is structurally blind to a fifth grammar (a rung-named const) and so certifies the ladder intact.",
    "notes": "Two clauses of the same amended order disagree about two lines of code. This worker followed the explicit KEEP instruction and neither reverted the two constants nor edited the checker. The row records the form of the conflict; its significance is the issuer's."
  },
  {
    "id": "DSGN_REBRND-W1-S16",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T02:10:30Z",
    "one_line": "Model-name holdouts, recorded for L10 as the order directs: getModelColor() in aum.ts still keys the five models by their EARLIER names, and this order fixed only their colours and the UST shadowing, not the names.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/api/endpoints/aum.ts:1074-1078 @0e87cb9f99: keys 'Aggressive', 'Conservative', 'Intermediate', 'Short-Term', 'Ultra Short-Term' -- the same five keys remain after this worker's edit, which changed only their values (now canon) and the match order (longest key first)",
        "portal src/lib/modelPortfolioColors.ts @0e87cb9f99^ (restored verbatim by this order): backward-compat aliases 'Long-Term Aggressive' and 'Long-Term Conservative' under the comment 'callers that use the API-returned name ... still resolve correctly' (MDPF_SCOPED.S4 2026-05-28) -- a second carrier of the earlier names, kept deliberately by its authors",
        "task order DSGN_REBRND.TO-RB-s-4 @1cceadbf81: 'DO NOT WIDEN THIS INTO A RENAME ... The name holdouts are an OBSERVATION row for L10.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Andrew-direct, quoted in the order: 'I thought we had already scanned through and changed any old names to the new ones but im not surprised there are little holdouts.'",
    "world_is": "At least two carriers still key on the earlier model names: getModelColor()'s colorMap in aum.ts, and the backward-compat aliases in modelPortfolioColors.ts. Both now resolve to canon colours, so nothing renders wrong today. Which names the API actually sends to getModelColor was NOT measured by this worker, so whether the legacy keys are live input or dead code is open.",
    "notes": "INERT because, with the colours on canon, a legacy-named model now renders its canonical colour. It would become harmful only if the keys were renamed without first measuring the API's names -- the blast radius the order names. Not a census of every holdout: two carriers seen in the course of this order, no hunt made."
  },
  {
    "id": "DSGN_REBRND-W1-S17",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T02:30:16Z",
    "one_line": "rb4-canon-check.py ARM A cannot see the five CANONICAL entries of MODEL_PORTFOLIO_COLORS -- their name and primary sit on different lines -- so on the pre-revert tree it flagged only the eight aliases while all five primaries were navy.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- the checker is an issuer artifact and read-only to this worker. A re-cut would let ARM A resolve a rung from the enclosing object key or name line and grade the primary a few lines below it. Until then, RB4-AC4R reads CANON-INTACT on a tree where the five canonical model entries are off canon, provided the aliases are on canon.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/lib/modelPortfolioColors.ts:18-20 @0e87cb9f99: `'Ultra-Long Term': {` / `name: 'Ultra-Long Term',` / `primary: '#183B86',      // ordered-scale ramp, step 5 of 5 -- darkest` -- rung label and colour on separate lines; the other four canonical entries have the same shape",
        "rb4-canon-check.py @1cceadbf81 resolves a rung and a colour from the SAME line only (colour_on(line) after an id:/name: match on that line); a name: line that carries no hex yields no site",
        "mutant run by this worker: the checker over `git archive 0e87cb9f99 src` (635 files, in .scratch/mut_prerevert) printed OFF-CANON for modelPortfolioColors.ts:111-115 and 122-124 only (the aliases), and nothing for lines 20/29/38/47/56 where the five canonical primaries were navy; overall verdict CANON-BROKEN, carried by the other writers",
        "on this worker's final tree (portal 46d2bc59) all five canonical primaries are back on canon by whole-file restore, so the gap costs nothing TODAY; it is a coverage gap in the instrument, not a live off-canon colour"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB4-AC4R: 'the canonical duration ladder is intact at every site' -- 'Every off-canon line prints with its file, line, rung, actual and expected value.'",
    "world_is": "The most-consumed ladder writer's five primary entries (the canonical model names, not the aliases) are not sites to the checker at all, so an off-canon colour there prints no line and cannot move the verdict. The checker's other arms happened to carry the pre-revert tree to CANON-BROKEN, which is why the issuer's navy-tree exercise did not reveal the gap.",
    "notes": "Found in the output of this worker's own mutant run, not by a hunt. Same family as W1-S15: a grammar the checker does not read. The worker did not edit the checker."
  },
  {
   "id": "DSGN_REBRND-S2",
   "project": "DSGN_REBRND",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~D",
   "surfaced_at": "2026-09-14T03:34:09Z",
   "one_line": "Andrew's OPTION A ruling (panels go light) puts the light-on-dark idioms of the page files in scope for inversion, and the committed inversion rule and per-role semantic re-derivation are applied to no token and no page: no cell of decomposition v1 covers applying them, so round 1 ends with Option A in the contract and light-on-dark idioms in the pages.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "spec_asserts": "Decomposition v1 (@e616ad99ec, frozen) covers 11 write surfaces; the canvas/surface work lands on surface 2 (portal/src/index.css) and surface 5 (the panel primitives), and no cell's write set is the page files that carry light-on-dark idioms. RB-s-13/14/15 are scoped to measure the product the 15 cells produce.",
   "world_is": "Andrew-direct 2026-09-11, VERBATIM (commit 11768022aa): 'Let's try A. ... I think A is the correct choice, but yes, we will have to do more work.' Option A: page light, panels white with a hairline, the dark band one deliberate element per page. The prior session of this lane reported roughly 123 of 171 page files carrying light-on-dark idioms that must invert (11768022aa; NOT re-measured this session). Andrew then asked for 'a defined logic from outset on how you want to invert the hex+opacity diffs' (1bedb59788); that logic is committed at design/brand/inversion-rule.json and both commits state it is NOT APPLIED -- no token changed, no file inverted. RB-s-7 Amendment 1 (@f6f7bfa706) carries the rule into the contract as normative text, but RB-s-7 moves no pixel. So round 1 closes with the law and the pages disagreeing, and RB-s-13/14/15 will measure a pre-inversion tree.",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "commit 11768022aa message: Option A verbatim; 'roughly 123 of 171 page files carry light-on-dark idioms that must invert'; 'NOT APPLIED: no token is changed by this commit'",
     "commit 1bedb59788 message: the inversion-logic mandate verbatim; 'NOT APPLIED. No token is changed by this commit and no file is inverted. The rule goes into the CONTRACT (RB-s-7) and the inversion becomes a cell cut against it'",
     "org/missions/D13/DSGN/DSGN_REBRND/decompositions/DSGN_REBRND_DECOMP.md @e616ad99ec s.2 rectangle and s.3 cell table: 15 cells over 11 write surfaces, none of them the page-file set",
     "org/missions/D13/DSGN/DSGN_REBRND/task-orders/DSGN_REBRND.TO-RB-s-7.the-contract.md @f6f7bfa706: Amendment 1 clauses B (Option A) and C (the inversion rule); 'This cell moves the CONTRACT and not a single pixel'"
    ]
   },
   "notes": "Surfaced by the issuer at the RB-s-4 drain; deferred from the start of the session only to avoid a guaranteed append conflict with two live worker branches. INERT, not ARMED: nothing is endangered in round 1 -- RB-s-13/14/15 still run against the tree round 1 produces, and their results are superseded once the inversion lands. Rides to L10 as a round-2 recommendation for 1.0.0_SA_CTO: an inversion cell (or a set split by route) applying the committed rule and re-deriving the semantic family per role, followed by a re-run of the coverage, parity and side-by-side cells. Andrew's side-by-side pack (RB-s-15, FWD-9) should say plainly that it shows the pre-inversion product.",
   "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "DSGN_REBRND-W2-S5",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T03:16:04Z",
    "one_line": "Option A makes every panel white (#FFFFFF, palette.surface) with #0A1733 as ONE deliberate band per page, but the token file's semantic.background.contentPanel still resolves to palette.darkField (#0A1733) -- the contract and the token file disagree on the panel role.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D",
    "spec_asserts": "TO-RB-s-7 Amendment 1 B: 'panels are white (#FFFFFF, palette.surface) with a hairline; panel titles are navy ink; the dark field #0A1733 (palette.darkField) is ONE deliberate band per page, never the default container' -- and 'Do not edit the token file and do not paper over it in the contract: state Option A as the law, and append ONE surprise row naming the divergence'.",
    "world_is": "The token file maps the panel role to the dark field: portal/design/brands/opal-capital.json@dc1d8020256e16dd55978c9541e490319d35ef7b line 165 reads \"contentPanel\": \"palette.darkField\", and palette.darkField.hex is #0A1733 (line 127). The live render agrees with the token file, not with Option A: /positioning at portal dc1d8020 draws all three of its panels (POSITIONING SUMMARY, PORTFOLIO COMPOSITION, HOLDINGS BREAKDOWN) as #0A1733 containers on the #F4F6FA canvas.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/design/brands/opal-capital.json@dc1d8020256e16dd55978c9541e490319d35ef7b line 165: \"contentPanel\": \"palette.darkField\"; line 127: darkField \"hex\": \"#0A1733\"",
        "org/missions/D13/DSGN/DSGN_REBRND/task-orders/DSGN_REBRND.TO-RB-s-7.the-contract.md@f6f7bfa706 Amendment 1 B (the Option A clause and the instruction to file this row)",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/rb-s-7_positioning_1440.png -- ui-smoke at 1440x900 on port 5182, CANVAS rgb(244, 246, 250); three dark panels visible, read by this worker"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "portal/DESIGN.md clause C3 states Option A as the law for the panel role and names this row as the known divergence. Token file NOT edited (the order edits no token file). The disarm is a token-file act (contentPanel -> palette.surface) plus the page cells that consume it; neither is this cell's."
  },
  {
    "id": "DSGN_REBRND-W2-S6",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T03:16:04Z",
    "one_line": "design/brand/inversion-rule.json, which the contract must cite for the worked examples, carries ground.dark_band #101828 -- the same non-ratified band the order names as a defect only in portal-opaque-ladder.json -- and its translucent worked examples are composited against it, not against #0A1733.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D",
    "spec_asserts": "TO-RB-s-7 Amendment 1 C: the contract 'cites design/brand/inversion-rule.json for the worked examples'; Amendment 1 D names #101828 as contradicting 'the PRD's ratified inverted band #0A1733, and the ratified value wins' -- but says so of design/brand/portal-opaque-ladder.json only.",
    "world_is": "design/brand/inversion-rule.json@f6f7bfa70649c232b1e55975cbb40ccd009b042e lines 26-30: ground.dark_band is \"#101828\". Its worked examples use that band as the backdrop: text-white/70's effective_hex #B7BABE is 0.7 x #FFFFFF + 0.3 x #101828 per channel (183.3, 185.7, 190.5 -> B7 BA BE); against the ratified #0A1733 the same idiom composites to #B6B9C2 (181.5, 185.4, 193.8). The opaque idiom is unaffected (white on #101828 and white on #0A1733 both measure 17.75:1), but every translucent example's effective hex, and therefore its ratio_before, is taken against a band the PRD did not ratify.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "design/brand/inversion-rule.json@f6f7bfa70649c232b1e55975cbb40ccd009b042e line 29: \"dark_band\": \"#101828\"; lines 41-48: text-white/70 effective_hex #B7BABE",
        "computed by this worker (WCAG 2.1 relative luminance, python): white on #101828 = 17.75, white on #0A1733 = 17.75; per-channel composite of white at 0.7 over #101828 = B7 BA BE, over #0A1733 = B6 B9 C2",
        "design/brand/portal-opaque-ladder.json@f6f7bfa706 line 21: rung 'band' hex #101828 (the file Amendment 1 D names)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "portal/DESIGN.md C5 carries the rule and the method, cites the file for the worked examples, restates none of their output hexes, and states that the file's ground.dark_band is not the ratified band and that the backdrop in C5.1/C5.3 is the real one (#F4F6FA, #FFFFFF or #0A1733). inversion-rule.json is read-only to this worker and was not edited."
  },
  {
    "id": "DSGN_REBRND-W2-S7",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T03:16:04Z",
    "one_line": "Byte-equal token values measure below the contrast floors the contract commits to in eight named role-and-ground pairs: status.warning is 3.15:1 as text on a white panel, and every status value misses its C5.7 per-role target on at least one ground.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D",
    "spec_asserts": "TO-RB-s-7: the contract commits to 'the minimum text contrast it commits to (WCAG 2.1 SC 1.4.3 / 1.4.11)', carries the per-role targets 'positive 4.8:1, negative 6.4:1, warning 4.6:1, info 5.4:1' and the 'boundary floor 1.35:1', AND 'Every value it names is BYTE-EQUAL to RB-s-1's JSON', with 'The status family is the token file's status block (#257E55 / #BE2D36 / #D37C17 / #2970A3), byte-equal'.",
    "world_is": "Measured WCAG 2.1 ratios of the token file's own values (portal/design/brands/opal-capital.json@dc1d8020256e16dd55978c9541e490319d35ef7b) on the panel #FFFFFF and the page #F4F6FA. status.success #257E55: 5.01 and 4.63, target 4.8, below on the page. status.danger #BE2D36: 5.80 and 5.36, target 6.4, below on both. status.warning #D37C17: 3.15 and 2.91, target 4.6 and the SC 1.4.3 floor 4.5, below on both. status.info #2970A3: 5.33 and 4.93, target 5.4, below on both. semantic.text.secondary #6B7280: 4.83 and 4.47, below 4.5 on the page. semantic.text.muted #A8B0C0: 2.18 and 2.01, below 4.5 on both. semantic.border.subtle #E8EBF0: 1.20 and 1.10, below the 1.35 boundary floor on both. palette.mutedTint #C4CBDB, whose note calls it a 'muted text tint': 1.63 and 1.50. So these values cannot meet the committed floors in those roles and grounds while staying byte-equal.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/design/brands/opal-capital.json@dc1d8020256e16dd55978c9541e490319d35ef7b lines 308-326 (status block), 176-184 (semantic.text), 186-190 (semantic.border), 137-146 (mutedTint note)",
        "computed by this worker, python, WCAG 2.1 relative luminance over the byte-equal hexes; the full table is in portal/DESIGN.md C3 and C6",
        "design/brand/inversion-rule.json@f6f7bfa706 lines 19-25 (role_targets) and line 25 (boundary_floor 1.35)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The contract moves no value. It restricts the roles instead: secondary text on a panel only (C3), #A8B0C0 is not text on a light ground (C3, C9), warning is never text on a light ground (C6), a status colour on a light ground always has a non-colour cue (C6), border.subtle is a fill and never a boundary (C3, C5.6). The values are the token file's (RB-s-1); whether the status block is re-derived to the C5.7 targets is not this cell's call."
  },
  {
    "id": "DSGN_REBRND-W2-S8",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T03:16:04Z",
    "one_line": "Three of the five locked canon hexes measure below the 3:1 SC 1.4.11 floor against the white panel, and the lock forbids moving them.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D",
    "spec_asserts": "TO-RB-s-7 Amendment 1 A: the five canon values are locked, value and order ('These are the only colors that truly must stay locked in'), AND the contract commits to WCAG 2.1 SC 1.4.11 (3:1 for a graphical object needed to understand content).",
    "world_is": "Measured against #FFFFFF: UST #F97316 2.80, ST #F59E0B 2.15, INT #10B981 2.54, LT #3B82F6 3.68, ULT #EF4444 3.76. Against #F4F6FA: 2.59, 1.98, 2.34, 3.40, 3.48. So 3 of 5 are below 3:1 on both light grounds. Under Option A the ladder moves off the dark panel onto white, which is the ground on which these three fall short. Because the hex cannot move, the model's identity can only meet SC 1.4.11 through a non-colour cue.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/2.0.0_SA_COO/ANDREW_DIRECT_20260911_THE_DURATION_LADDER_IS_CANON.md@f6f7bfa706 lines 40-49 (the locked table)",
        "portal/src/lib/modelPortfolioColors.ts@dc1d8020 lines 20, 29, 38, 47, 56 (primary #ef4444 #3b82f6 #10b981 #f59e0b #f97316)",
        "computed by this worker, python, WCAG 2.1 relative luminance"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "portal/DESIGN.md C4 carries the lock unchanged and requires every canon mark to carry its rung label or sit beside a legend entry, with model names in navy ink and never in the canon hex. This is a condition on pages, and page cells enforce it. The values stay Andrew's."
  },
  {
    "id": "DSGN_REBRND-W2-S9",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T03:16:04Z",
    "one_line": "The token file carries no typography, spacing, radius or grid block, so the non-colour values the cell itself requires the contract to resolve have no token-file counterpart to be byte-equal to.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-RB-s-7: 'Every value it names is BYTE-EQUAL to RB-s-1's JSON (portal/design/brands/opal-capital.json) -- with ONE named exception, the canonical duration ladder'; and the contract 'resolves: typeface (Lato 400/700, tabular numerals) ... spacing and density ... shape (radii 2/3/4px plus pill) ... layout split'.",
    "world_is": "The top-level keys of portal/design/brands/opal-capital.json@dc1d8020256e16dd55978c9541e490319d35ef7b are brand, slug, description, palette, semantic, darkMode, status and data. There is no typography, spacing, rounded/radius, grid or elevation key. So Lato 400/700, the radii 2/3/4px plus a pill, the type sizes, the spacing ladder and the 40/60 split cannot be byte-equal to anything there. The contract takes them from the cell text (Lato, 400/700, tabular-nums, 2/3/4px, the split) and from the RD draft @10236236 (type sizes, the 13.5-80px spacing ladder, pill 720px), and names that source. They were not re-measured.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/design/brands/opal-capital.json@dc1d8020256e16dd55978c9541e490319d35ef7b -- json.load keys: brand, slug, description, palette, semantic, darkMode, status, data (read by this worker)",
        "portal/DESIGN.md@10236236 (RD draft) lines 15-72: typography, rounded, spacing, grid front matter"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Read as: byte-equal binds every value the token file carries, and a value it does not carry takes the cell's own word or the draft's measurement with the source named in the front-matter comments. No colour outside the token file and the canon ladder is named."
  },
  {
    "id": "DSGN_REBRND-W2-S10",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T03:16:04Z",
    "one_line": "RB7-AC4 needs a worker that has never seen the portal to build one page from the contract alone. This worker can neither spawn nor message one, and as the contract's author it cannot stand in for that builder.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D",
    "spec_asserts": "TO-RB-s-7 RB7-AC4: 'a worker subagent that has never seen the portal builds ONE new page from the contract alone and it lands inside the system. The build record and the page are in the deliverables.' BOUNDS: 'Produce the on-demand half -- the built page, the clause-cited rejection -- and record it.'",
    "world_is": "This L7 worker's tool set is Bash, Read, Edit, Write, Glob and Grep. It has no agent-spawn tool and no send tool (spine v3 L7: workers carry no send tool). A page built by this worker would be built by the contract's author, who read the token file and the inputs, so it would not test whether the contract ALONE is enough. Starting a model session from Bash to stand in for a worker would be an unaudited spawn outside this order, and was not done. So the built page is not produced. The on-demand half that is produced is the build kit, the exact brief a fresh builder receives.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the build kit: org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/rb7-ac4-build-kit.md",
        "org/missions/D13/DSGN/DSGN_REBRND/task-orders/DSGN_REBRND.TO-RB-s-7.the-contract.md@f6f7bfa706 RB7-AC4 and BOUNDS (the second-actor clause)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "BLOCKING on RB7-AC4's on-demand half only. The order's mechanical criteria and RB7-AC5's rejection record are not blocked by it. Disarm: seat a fresh worker on the build kit, which names the contract as its only input and the output path, and have it write the page plus its build record into this deliverables folder before L9."
  },
  {
    "id": "DSGN_REBRND-W2-S11",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T03:25:29Z",
    "one_line": "The asset-class legend on /positioning paints Fixed Income #10B981 and Equities #3B82F6, the reverse of the token file's data.assetClass (equity #10B981, fixedIncome #3B82F6), so the two carriers disagree on which colour means which asset class.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D",
    "spec_asserts": "The token file is the one writer of the data family (TO-RB-s-7: 'Every value it names is BYTE-EQUAL to RB-s-1's JSON'; the token file's own data._note: 'Every value here is a RELOCATION of a pre-existing literal ... onto the one writer'), and it assigns data.assetClass.equity #10B981 and data.assetClass.fixedIncome #3B82F6.",
    "world_is": "Measured at the pixel on the live render of /positioning at portal dc1d8020 (the src tree is unchanged at 000478c9, which only edits DESIGN.md), POSITIONING SUMMARY panel, ASSET CLASSES legend: the swatch beside 'Fixed Income / Bonds & Cash' reads #10B981 at (128,282), and the swatch beside 'Equities / Stocks & Hedge' reads #3B82F6 at (128,334). That is the reverse of the token file's mapping. Not established: which carrier is intended, and whether any other page uses the token mapping. This worker reads no portal/src file outside its grant.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/design/brands/opal-capital.json@dc1d8020256e16dd55978c9541e490319d35ef7b lines 385-397: assetClass equity hex #10B981, fixedIncome hex #3B82F6",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/rb-s-7_positioning_1440.png sampled by .scratch/sample_png.py (PIL, 1440x1419): (128,282) #10B981 beside 'Fixed Income'; (128,334) #3B82F6 beside 'Equities'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Found off-task while producing RB7-AC5's clause-cited rejection of /positioning, which cites it under C6. No act taken. Whether the page or the token file carries the intended mapping is a data-family call (RB-s-1 / R8 owners), not this cell's."
  },
  {
    "id": "DSGN_REBRND-W2-S12",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T04:53:31Z",
    "one_line": "Amendment 2 limits the proof update to the RB7-AC4 row, but the reopened instance still carried four PENDING-THIS-COMMIT artifact rows whose files landed at 768bebce28, so the complete flip was refused until those four rows were re-pinned outside the RB7-AC4 row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-RB-s-7 Amendment 2: 'update the RB7-AC4 row of the existing proof instance so its evidence cites your three deliverables ... re-validate with the id list below, commit, and flip complete. Change NO other criterion row and NO other file.'",
    "world_is": "The hand run of proof-of-spec-check with RB7-AC1..AC7 read VALID (rc=0) with the RB7-AC4 row alone updated. Then the flip commit through safe-commit.sh was REFUSED by to-pipeline-gate: 'flips to complete but its instance is NOT VALID (rc=1)'. That gate runs the checker in the commit's staged context (python proof-of-spec-check.py <instance>, no ids, .tools/to-pipeline-gate.py:1625). There, the four artifacts_produced rows still pinned PENDING-THIS-COMMIT (rb-s-7_positioning_1440.png, rb7-ac5-rejection-positioning.md, rb7-ac4-build-kit.md, the-contract.result.md) point at files already committed at 768bebce28 and not staged again, which the checker names the CCX class. To flip, this worker re-pinned those four rows to 768bebce286a0fa2541a952ec9aa170c72267bef and changed their deploy_evidence text to match. No criterion row other than RB7-AC4 was changed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/to-pipeline-gate.py@c8ccbdb4f2 lines 1624-1633: subprocess.run(['python', chk, inst]) and the 'flips to ... but its instance is NOT VALID' refusal",
        "git show --stat 768bebce28 (author 0.9.0_WK_DSGN_REBRND~2, is-ancestor of c8ccbdb4f2 rc=0): the four artifacts at the pin with 72763 / 5753 / 3926 / 4522 bytes; negative control rb7-ac4-page.html absent at the pin (rc=128)",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-7.the-contract.proof_of_spec.json@c8ccbdb4f2: four artifacts_produced rows pinned PENDING-THIS-COMMIT"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Form only: a reopened order whose proof instance was committed with PENDING-THIS-COMMIT rows cannot flip complete again without re-pinning them, and the amendment's scope sentence did not provide for that. The re-pin is inside this worker's deliverables folder, which is the write grant. RB-s-8 runs under this same serial and W2 coordinate in another worktree, so a W2 id minted there could collide with this one at the drain."
  },
  {
    "id": "DSGN_REBRND-W1-S18",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T05:17:18Z",
    "one_line": "RB5-AC4 already printed VERDICT: RETIRED before this cell changed anything: RB-s-4 had removed the #ADFF2F literal from index.css, so this criterion cannot tell this cell's work from no work.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/index.css:170 @63345fac (this worker's base, before any edit): `--sentiment-chartreuse: var(--ramp-4);     /* an intermediate of the same step */` -- no hex literal; the cell text cites the literal at `:69`",
        "RB5-AC4's own count, run by this worker before its first edit on the same tree: `CHARTREUSE: 0`",
        "portal 547d12fd (RB-s-4 drain) repointed the six --sentiment-* tokens onto the ramp, so the literal was already gone when this cell started"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-5: 'portal/src/index.css:69 sets --sentiment-chartreuse: #ADFF2F'; RB5-AC4: 'At issuance this reads 1'.",
    "world_is": "At this worker's base (portal 63345fac) the count is 0 and the token resolves to ramp step 4. RB5-AC4 prints VERDICT: RETIRED on the untouched tree and again on the final tree, so its PASS here is vacuous for this cell. This cell did not edit the chartreuse line.",
    "notes": "The chartreuse-family lime survives on /market inside a chart series (the Global RSI bars, --perf-weak-pos / --perf-weak-pos-dark gradient in RSIBars.tsx:155), which the cell allows ('only under RB-s-1's data family'). Recorded for RB5-AC5's loudest-colour clause, not acted on."
  },
  {
    "id": "DSGN_REBRND-W1-S19",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T05:17:18Z",
    "one_line": "The app shell in portal/src/App.tsx, which is outside this order's <paths>, fills TWO persistent elements with the accent on every route (the active sidebar item and the avatar). So no route can reach the one-persistent-accent budget from inside this grant.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- widen a follow-on grant to portal/src/App.tsx (or rule the shell out of the per-view budget). The disarm is two class edits: the active nav item to weight and rule in band ink (App.tsx:189, which also carries `shadow-md`, a drop shadow under C11), and the avatar off the accent (App.tsx:382).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/App.tsx:189 @63345fac: `? 'bg-[hsl(var(--primary))] text-white shadow-md'` -- the active nav item; App.tsx:382: `<div className=\"w-8 h-8 rounded-full bg-[hsl(var(--primary))] ...` -- the avatar circle; App.tsx:261 carries a --primary border-image gradient on the sidebar edge",
        "this worker's counterexample walk (.scratch/accent-walk.mjs, copied to deliverables as rb-s-5_accent-walk.log) on the final tree: /positioning CHROME-ACCENT 2 (a 'Positioning' 36x36 at 6,276; div 'D' 32x32 at 6,862); /market CHROME-ACCENT 2 (a 'Market Overview'; div 'D'); /portfolio-management CHROME-ACCENT 3 (the same two plus button 'Upload Portfolio')",
        "TO-RB-s-5 <paths>: portal/src/index.css, portal/src/ui/, portal/src/components/, portal/src/pages/ -- App.tsx is not under any of them"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-5: 'A view carries the accent on exactly ONE PERSISTENT primary action'; RB5-AC5/AC6: the PERSISTENT accent count is one on each route.",
    "world_is": "After this cell, the page-level accent count is 0 on /positioning, 0 on /market and 1 on /portfolio-management (Upload Portfolio). The shell adds 2 on every route, so the measured persistent counts are 2, 2 and 3. The two shell elements are not actions under C8, and this worker cannot reach them. Not edited.",
    "notes": "BLOCKING for the budget clause of RB5-AC5 and RB5-AC6, both judgment rows graded at L9. It does not block the mechanical criteria."
  },
  {
    "id": "DSGN_REBRND-W1-S20",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T05:17:18Z",
    "one_line": "Two of the three routes have NO persistent primary action to put the accent on: every accent fill on /positioning and /market was a state control. The third route's one primary action (Upload Portfolio) sits inside a #0A1733 band, where DESIGN.md C8 says no primary action goes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "pre-cell /positioning @63345fac: the accent fills were the MODELS/ETFS/SATELLITES flip (Positioning.tsx:97), the Portfolio/Benchmark/Relative/Custom view (PositioningSummary.tsx:1088-1123) and Characteristics/Performance (HoldingsTab.tsx:1139). All three are view/state selectors (aria-pressed toggles or equivalent), not actions. The one real action, EXPAND DETAILS, was an outlined ghost",
        "pre-cell /market @63345fac: the accent fills were the period selectors (ExecutiveSummary.tsx:386, MarketRegimeIndicator.tsx:72, SentimentGauge.tsx:62), all state selectors; the only actions are the 'Expand' ghosts",
        "portal/DESIGN.md @63345fac C8: 'The band carries no primary action (#5F3BE3 on #0A1733 measures 2.72:1)'; OptimizationSummaryHeader.tsx renders Upload Portfolio in the OPTIMIZATION REPORT panel, which renders as a #0A1733 band (row W2-S5 -- panels have not gone light)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-5: each view carries the accent on 'exactly ONE PERSISTENT primary action'; RB5-AC5 asks for it 'enumerated in the result file'.",
    "world_is": "This worker invented no action to spend the accent on. /positioning and /market now carry 0 page-level accent fills, and /portfolio-management carries 1 (Upload Portfolio, kept as the primary in its band). Whether 0 satisfies 'exactly one' on a route with no action, and whether a band-resident primary is acceptable until W2-S5 is disarmed, are the grader's calls.",
    "notes": "The four state controls on /positioning and the three period selectors on /market now use the one segmented idiom (weight 700 + 2px rule). The duration ladder keeps its canonical hues and order."
  },
  {
    "id": "DSGN_REBRND-W1-S21",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T05:17:18Z",
    "one_line": "The worker face this worker was handed carries a BOUNDS bullet, 'THE CANON LOCK', that the task order file does not carry. So the face and its record disagree by one clause.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/task-orders/DSGN_REBRND.TO-RB-s-5.accent-controls.md @c8ccbdb4f2 (last changed at 845cb2b6ac, the L6 issuance): 0 matches for 'CANON LOCK' and 0 for 'F97316'",
        "the face in this worker's spawn prompt, BOUNDS, last bullet: 'THE CANON LOCK (Andrew-direct 2026-09-11, carried in the contract's clause C4): UST #F97316 / ST #F59E0B / INT #10B981 / LT #3B82F6 / ULT #EF4444 are the ONLY locked colours ... A five-hue segmented control that encodes the five duration models is the LADDER, not a defect -- its active state moves to weight and rule, its hues stay.'",
        "a CRLF-only diff of the file at feature/d13-visual-elevation against this worktree: every line differs by line ending only; neither carries the bullet"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's WORKER FACE is the worker's whole context, and the file is its record.",
    "world_is": "The face this worker executed carried one more clause than the file the complete flip lands on. This worker followed the face (the stricter reading, and portal/DESIGN.md C4 says the same): the ladder's hues and order are untouched, and only its active state moved.",
    "notes": "The same exposure the L4-R rule names for a mid-flight modification, in reverse: here the clause reached the worker but not the record. Its significance is the issuer's."
  },
  {
    "id": "DSGN_REBRND-W2-S16",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T05:02:14Z",
    "one_line": "design/process/UI_VERIFICATION.md did not carry the 2026-07-15 archetype in its body: 0 of the archetype's tokens, it pointed at COLOR_ARCHETYPES.md's three rules instead, so it carried the superseded law only by reference.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-RB-s-8, THE CELL: 'The four files, all carrying the superseded 2026-07-15 archetype (\"light SILVER canvas #C3CADA, dark navy containers floating on it\")' -- design/process/UI_VERIFICATION.md is the third of the four -- and 'if a file turns out not to carry the archetype at all, that is a surprise row.'",
    "world_is": "Census before any edit, worktree branch wk-dsgn_rebrnd-2c @1e7d8c0a13: design/process/UI_VERIFICATION.md (27 lines) carried 0 'C3CADA', 0 'SILVER', 0 'CANVAS', 0 'FLOATING' and 0 'NAVY' (case-folded counts). It stated the render-LOOK-commit rule and, at line 15, read screenshots 'against ../brand/COLOR_ARCHETYPES.md's three rules' -- so it carried the archetype BY REFERENCE, not in its body. As a result RB8-AC1's count reads 0 for this file both before and after the rewrite, and cannot tell a rewritten file from an untouched one here. The file was rewritten anyway: a supersession statement, the contract portal/DESIGN.md as what a screenshot is read against, and the clause-cite step, because by reference it was grading screenshots against the retired law.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "design/process/UI_VERIFICATION.md@1e7d8c0a13: pre-edit token census {'C3CADA': 0, 'SILVER': 0, '2026-07-15': 2, 'ARCHETYPE': 1, 'FLOATING': 0, 'CANVAS': 0, 'NAVY': 0} by python str.count over the upper-cased file",
        "design/process/UI_VERIFICATION.md@1e7d8c0a13 line 15: '3. READ the PNG against `../brand/COLOR_ARCHETYPES.md`'s three rules.'",
        "RB8-AC1 pre-edit run (.scratch/baseline_pre_edit.log): PER-FILE ... 'design/process/UI_VERIFICATION.md': 0 ... TOTAL: 5"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Form only; no act beyond the rewrite this order already names. The same by-reference shape means a file can carry a superseded law with no value in it, which no value census sees."
  },
  {
    "id": "DSGN_REBRND-W2-S13",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T05:02:14Z",
    "one_line": "portal/CLAUDE.md stated the silver canvas only as '222 24% 81%' and 'rgb(195,202,218)', never as the hex, so RB8-AC1's hex count read 0 on the UNEDITED file; the criterion cannot see the archetype in a non-hex form.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RB8-AC1: 'the superseded silver-canvas value is gone from ALL FOUR law files, judged on a single TOTAL', graded by counting the substring 'C3CADA' in each of the four files.",
    "world_is": "Before any edit, portal/CLAUDE.md@63345fac lines 11-14 read 'Color law -- THE CANVAS IS SILVER ... --palette-silver, 222 24% 81%, ~ rgb(195,202,218)' with 0 occurrences of 'C3CADA', and RB8-AC1's per-file count for it was 0 while the law stood in full. COLOR_ARCHETYPES.md and DESIGN_SYSTEM.md also carried the HSL form '222 24% 81%' beside the hex. So AC1's TOTAL can read 0 (SUPERSEDED) with the retired value still present in HSL or rgb form in any of the four files. This worker added a supplementary census that is not a criterion: the hex, '222 24% 81%', '195,202,218' and 'silver ... 81%' forms over all six edited files. After the edit it read 0 across 6 files.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/CLAUDE.md@63345facb72f6e98024855b28d87440a534f88f8 lines 11-14 (pre-edit): '## Color law -- THE CANVAS IS SILVER (Andrew-direct 2026-07-15)' ... '`222 24% 81%`, ~ `rgb(195,202,218)`'",
        "RB8-AC1 pre-edit run (.scratch/baseline_pre_edit.log): PER-FILE ... 'portal/CLAUDE.md': 0 ... TOTAL: 5",
        "supplementary census after the edit: OLD-VALUE-FORMS TOTAL: 0 over 6 files (hex, hsl, rgb, silver-81% regexes, case-insensitive)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "A criterion-instrument observation, filed for the L9 reader: RB8-AC1 PASSes on the edited files, and its blindness to the non-hex forms is covered here by a different instrument, not by the criterion itself."
  },
  {
    "id": "DSGN_REBRND-W2-S14",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T05:02:14Z",
    "one_line": "Two files outside the order's four-file list also stated the 2026-07-15 silver archetype: the /frontend-dev skill and the ui-smoke canvas label. Both are in <paths> and were rewritten under that grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-RB-s-8 names FOUR files as carrying the superseded archetype; .claude/skills/frontend-dev/SKILL.md is named only to 'gain one step' (the clause cite), and portal/scripts/ui-smoke.mjs only to keep 'printing the resolved canvas'.",
    "world_is": "Before any edit, .claude/skills/frontend-dev/SKILL.md@1e7d8c0a13 stated the archetype in its front-matter description ('check it against the silver-canvas color law') and body lines 8-10 ('The portal's page canvas is light silver (--bg-page, 222 24% 81%). Dark navy panels float on it'); portal/scripts/ui-smoke.mjs@63345fac line 342 labelled the canvas print '(the silver -- light fg on this is the footgun)' and line 357 said 'no light text/buttons outside dark panels'. The skill is loaded for every portal page build, so leaving it would have left the retired law standing beside the rewritten four. Both were rewritten onto the contract within this order's <paths>; ui-smoke's print of state.canvas itself is unchanged.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".claude/skills/frontend-dev/SKILL.md@1e7d8c0a13 lines 3 and 8-10 (pre-edit), quoted in world_is",
        "portal/scripts/ui-smoke.mjs@63345facb72f6e98024855b28d87440a534f88f8 lines 342 and 357 (pre-edit), quoted in world_is",
        "pre-edit census: SKILL.md SILVER 3, CANVAS 6; ui-smoke.mjs SILVER 1"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No widening: both paths are in the order's <paths>. Filed so the L9 reader sees that the edit set is six files, not four."
  },
  {
    "id": "DSGN_REBRND-W2-S15",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T05:02:14Z",
    "one_line": "Three auto-read portal/src carriers outside this order's grant still state the 2026-07-15 silver-canvas law as current: panels/README.md, TicketCenter.tsx and designTokens.ts. The running theme contradicts all three.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D",
    "spec_asserts": "TO-RB-s-8: 'never leave a second archetype standing beside the old one -- that is the shadow-system failure and it is banned'; the write grant is the seven <paths>, which name no portal/src file.",
    "world_is": "Native Grep over portal/src at portal@63345fac for --bg-page / --palette-silver (one pattern, portal/src only) found: src/ui/components/panels/README.md:5 '**The archetype (live-resolved 2026-07-15):** the page canvas is LIGHT SILVER (`--bg-page`,'; src/pages/TicketCenter/TicketCenter.tsx:11 '* COLOR LAW (Andrew-direct 2026-07-15): the page canvas is SILVER (--bg-page, 81% lightness).'; src/lib/designTokens.ts:10 '*   - The PAGE CANVAS is LIGHT SILVER (--bg-page = --palette-silver, 222 24% 81%).' and :40 '/** LIGHT SILVER page canvas (--palette-silver, 222 24% 81% at current brand).'. The applied theme is src/index.css:111 '--bg-page: var(--palette-canvas);' (#F4F6FA). A page builder reading any of the three is taught the retired law. None is in this order's <paths>, so none was edited. Not censused: the rest of the repo, and any carrier that does not name --bg-page or --palette-silver.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/ui/components/panels/README.md@63345facb72f6e98024855b28d87440a534f88f8:5",
        "portal/src/pages/TicketCenter/TicketCenter.tsx@63345facb72f6e98024855b28d87440a534f88f8:11",
        "portal/src/lib/designTokens.ts@63345facb72f6e98024855b28d87440a534f88f8:10 and :40",
        "portal/src/index.css@63345facb72f6e98024855b28d87440a534f88f8:111 '--bg-page: var(--palette-canvas);'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Found in passing while resolving the applied canvas for the rewrite; no hunt beyond the one search. The rewritten portal/CLAUDE.md and frontend-dev skill now name this row, so a reader of the law is told these comments are the superseded vintage."
  },
  {
    "id": "DSGN_REBRND-W2-S17",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T05:54:36Z",
    "one_line": "AMENDMENT 1's ordered re-mint (rename this branch's row id DSGN_REBRND-W2-S12 to DSGN_REBRND-W2-S16) is refused by the surprise-row gate as a DELETION of an existing row; the append-only channel admits a rename only by an audited override the order does not grant.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D",
    "spec_asserts": "TO-RB-s-8 AMENDMENT 1 (fa8d87fa08, 2.0.0_SA_COO~D): 'Re-mint THIS branch's W2-S12 as DSGN_REBRND-W2-S16 -- the row id itself, the proof instance's surprises entry, and every mention in your result file -- touching nothing else, re-validate, commit, and flip complete.'",
    "world_is": "The re-mint was applied in the worktree (channel row id, the instance's surprises entry, 3 result-file mentions), proof-of-spec-check read VALID (rc=0), and the commit through .tools/safe-commit.sh was then refused, rc=1: 'surprise-row-gate BLOCKED -- EXISTING row DSGN_REBRND-W2-S12 was DELETED. The channel is append-only: retire it with a new row that cites it, never by removal.' The gate names two paths: an audited '# surprise-row-override: <reason>' in a COMMIT message, and 'ON A MERGE (safe-merge.sh) THERE IS NO OVERRIDE PATH ... route it to the gate's owner (1.0.0_SA_CTO)'. The order grants no override, so none was used. The worktree edits were reversed to HEAD's bytes and the task order's status left pending, so nothing of the re-mint is committed. The collision stands: feature/d13-visual-elevation@a635ac70f0 carries the RB-s-7 builder's DSGN_REBRND-W2-S12 (a different finding), and this branch at fa8d87fa08 carries its own DSGN_REBRND-W2-S12 (the UI_VERIFICATION by-reference row). DSGN_REBRND-W2-S16 is left unused, reserved for the ordered re-mint, so this row takes S17.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/surprise-row-gate.py via .tools/safe-commit.sh, worktree C:/tmp/wk-dsgn-2c at HEAD fa8d87fa08, 2026-09-14: 'EXISTING row DSGN_REBRND-W2-S12 was DELETED. The channel is append-only: retire it with a new row that cites it, never by removal.' -- safe-commit rc=1, nothing committed (HEAD unchanged, read back)",
        "feature/d13-visual-elevation@a635ac70f0 org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md: DSGN_REBRND-W2-S12 surfaced_by 0.9.0_WK_DSGN_REBRND~2, one_line 'Amendment 2 limits the proof update to the RB7-AC4 row, ...'; DSGN_REBRND-W2-S16 in 0 of 33 rows",
        "wk-dsgn_rebrnd-2c@fa8d87fa08, same channel path: DSGN_REBRND-W2-S12 is this order's row ('design/process/UI_VERIFICATION.md did not carry the 2026-07-15 archetype in its body ...')"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Form only. Not tested: the gate's suggested path (a new row that cites W2-S12 and retires it) would still leave two rows carrying the id DSGN_REBRND-W2-S12 once the branches merge, so on its face it does not remove the collision the amendment exists to remove. The proof instance at 15dccb63e3 stays VALID with W2-S12 and is not edited here."
  },
  {
    "id": "DSGN_REBRND-W1-S22",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T07:45:49Z",
    "one_line": "The order says to build the ring from 'the ring token RB-s-1 defines', but RB-s-1 defined no ring token. The only ring definition is portal/DESIGN.md C11, a two-layer ring, not the site's single 2px ring the face quotes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal design/brands/opal-capital.json @845833fb: no key names a ring or focus; the one hit is the note string at :47 ('single action accent + focus ring')",
        "portal design/themes/opal-capital.css @845833fb: 0 matches for 'focus' and no '--ring' variable (Grep over portal/design/*.{css,json,ts}); the only '--ring' in the portal is portal/docs/archive/design-language-v0 ('--ring: var(--gold)')",
        "portal DESIGN.md @845833fb :175-178 components.focus-ring '0 0 0 2px #FFFFFF, 0 0 0 4px #5F3BE3' and focus-ring-on-band '0 0 0 2px #0A1733, 0 0 0 4px #E8ECF5'; clause C11 :388-392 states the same two values",
        "TO-RB-s-6 worker face, THE CELL: 'The live site's only box-shadow anywhere is its focus ring: rgb(95,59,227) 0 0 0 2px. Use the ring token RB-s-1 defines.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-6: 'Use the ring token RB-s-1 defines'; the site's ring is 'rgb(95,59,227) 0 0 0 2px'.",
    "world_is": "No ring token exists. This worker built the ring in portal/src/index.css from DESIGN.md C11's two values, composed from tokens that already exist (--bg-surface, --semantic-action-primary, --palette-darkField, --palette-white). The rendered ring is a 2px gap plus a 2px outer ring, 4px in all, not the site's single 2px ring. The contract was followed where it and the face differ."
  },
  {
    "id": "DSGN_REBRND-W1-S23",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T07:45:49Z",
    "one_line": "The order cites row DSGN_REBRND-W2-S15 as the source of the comment fold and its census, but no such row exists in the channel, so 'the same census the row used' cannot be re-run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md @7772585067: 1 json fence, 37 row ids; the W2 coordinate runs S1..S12 and stops",
        "the same file at feature/d13-visual-elevation (7772585067, git show): the same 37 ids, no W2-S13 or later"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-6, first ALSO paragraph: '(2026-09-14, row DSGN_REBRND-W2-S15) ... Evidence: the same census the row used, re-run after the edit, printing zero hits.'",
    "world_is": "This worker defined its own census and printed it on both vintages: case-insensitive 'silver|81%|222 24%' over the three named files reads 7 hit lines on portal 845833fb (README.md:5,6; TicketCenter.tsx:11,171; designTokens.ts:10,40,42) and 1 after the edit. Inside the four named comment blocks it reads 0. The one remaining hit is row W1-S24."
  },
  {
    "id": "DSGN_REBRND-W1-S24",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T07:45:49Z",
    "one_line": "A fifth comment, outside the four the order names, still states the superseded canvas: TicketCenter.tsx:174 (:171 at base) calls the page 'the silver canvas'. Not edited.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- a one-line comment rewrite under a grant that names portal/src/pages/TicketCenter/TicketCenter.tsx:174, the same act this order did for the four named comments.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/TicketCenter/TicketCenter.tsx:171 @845833fb: '{/* Canvas-level error banner: DARK text on the silver canvas (never light-on-light). */}' -- the same line sits at :174 after this order's three-line growth of the header comment",
        "the census of row W1-S23 after the edit: 1 hit line over the three named files, and it is this one"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-6: rewrite 'those four COMMENTS' (panels/README.md:5, TicketCenter.tsx:11, designTokens.ts:10 and :40); 'Comments only'; evidence 'the same census ... printing zero hits'.",
    "world_is": "Inside the four named blocks the census reads 0. Over the whole of the same three files it reads 1, on this JSX comment. It was left as it is: the order names four comments, and this worker does not widen it."
  },
  {
    "id": "DSGN_REBRND-W1-S25",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T07:45:49Z",
    "one_line": "The band ring renders rgb(230, 234, 244), #E6EAF4, not DESIGN.md's #E8ECF5, because the generated --palette-white is the rounded HSL '222 38% 93%'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "final keyboard walk (deliverables rb-s-6_walk_kbd.log): every band stop's computed box-shadow is 'rgb(10, 23, 51) 0px 0px 0px 2px, rgb(230, 234, 244) 0px 0px 0px 4px' -- the dark field is exact (#0A1733), the white is not",
        "portal design/themes/opal-capital.css @845833fb: '--palette-white: 222 38% 93%'",
        "portal DESIGN.md @845833fb :6-9 'Every colour below is byte-equal to portal/design/brands/opal-capital.json', :18 'white: \"#E8ECF5\"', :178 focus-ring-on-band '... 0 0 0 4px #E8ECF5'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DESIGN.md C11: inside the band the ring is '0 0 0 2px #0A1733, 0 0 0 4px #E8ECF5' (15.00:1).",
    "world_is": "The ring reads the token, and the token as generated resolves 2 units off the contract's hex in two channels. This worker's rule does not hard-code a hex, so it inherits whatever the generator emits. The rounding sits in the theme generator's output, outside this order's paths."
  },
  {
    "id": "DSGN_REBRND-W1-S26",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T07:45:49Z",
    "one_line": "To make the active nav item actually bold, this worker also moved font-medium out of the shared base class string (App.tsx:183) and gave the idle branch a transparent 2px rule: four changed lines, where the order names 'those two class edits only'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "a keyboard walk on the two-line edit (active branch 'font-bold ... border-l-2', base string still 'font-medium'): NAV-ACTIVE fontWeight '500' on /market, /positioning and /portfolio-management -- the base string's font-medium won over font-bold",
        "final walk (deliverables rb-s-6_walk_kbd.log): NAV-ACTIVE fontWeight '700', color rgb(230, 234, 244), background rgba(0, 0, 0, 0), borderLeft '2px solid rgb(230, 234, 244)', boxShadow 'none' on all three routes",
        "portal git diff --numstat src/App.tsx against 845833fb: 4 insertions, 4 deletions -- lines 183, 189, 190 (the one NavLink className expression) and 382 (the avatar)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-6, second ALSO paragraph: 'Those two class edits only -- no layout, no route, no behaviour' (App.tsx:189 the active item, :382 the avatar).",
    "world_is": "Three lines of the one NavLink className expression changed, plus the avatar. :183 drops font-medium from the base. :189 is weight 700 plus a 2px band-ink rule, with no fill and no shadow. :190 carries font-medium and 'border-l-2 border-transparent', so the rule does not shift the active item against the idle ones. :382 is the outlined avatar. No layout, route or behaviour changed; every nav item's content sits 2px further right, which is the rule's width."
  },
  {
    "id": "DSGN_REBRND-W1-S27",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T07:45:49Z",
    "one_line": "The shell sidebar is filled #0A1733 but is not marked .dark-band, so its items get the light-ground ring (a white gap plus #5F3BE3), not C11's band ring.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "final walk (deliverables rb-s-6_walk_kbd.log / the kbd walk JSON): 54 shell stops across the three routes (logo toggle, 16 nav links, user button), 1 distinct computed shadow: 'rgb(255, 255, 255) 0px 0px 0px 2px, rgb(95, 59, 227) 0px 0px 0px 4px'",
        "portal src/App.tsx @845833fb :256: the <aside> class is 'bg-[hsl(var(--bg-header))]', with no dark-band class; portal/src/index.css @845833fb :115 '--bg-header: var(--bg-band)'",
        "portal DESIGN.md @845833fb C8 :355: '#5F3BE3 on #0A1733 measures 2.72:1'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DESIGN.md C11: 'and 0 0 0 2px #0A1733, 0 0 0 4px #E8ECF5 inside the band (15.00:1)'.",
    "world_is": "On the sidebar the ring's 2px white inner layer carries the signal against #0A1733, and the 2px accent outer layer sits at 2.72:1 against it. Whether the shell is 'the band' for C11 is not this worker's call. Adding .dark-band to the aside would be a further App.tsx class edit with side effects (it resets ink, status colours and control colours for everything inside), so it was not made."
  },
  {
    "id": "DSGN_REBRND-W1-S28",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T07:45:49Z",
    "one_line": "A mouse click into a text field paints the ring (7 of 7 such clicks, on 5 of the 18 inventory routes). The browser matches :focus-visible on a field that takes typing, so 'no ring on a mouse click' holds for buttons, tabs and toggles but not for text inputs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "inventory walk (deliverables rb-s-6_walk_inventory.log) MOUSE-CLICK lines landing in a text field: /change-password 'Enter current password' (twice), /forgot-password 'you@example.com', /investor-reporting 'Client search' (twice), /login 'you@example.com', /security-scanner 'Search factors...' -- each ':focus-visible=true', ring ACCENT, or BAND on /security-scanner",
        "the same walks, clicks on non-text controls (buttons, tabs, segmented options): 15 clicks over the 21 walked routes, ':focus-visible=false ring=NONE' on all 15; on /market, /positioning and /portfolio-management 3 of 3",
        "instrument: headless Microsoft Edge (Chromium) through playwright-core, a real page.mouse.click at the element's centre"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-6: ':focus-visible (not :focus) so a mouse click does not paint a ring'; RB6-AC5: 'no ring appears on a mouse click'.",
    "world_is": "With :focus-visible as ordered, a click on a button, tab or segmented option paints nothing, and a click into a text field paints the ring, because Chromium's :focus-visible matches any element that accepts keyboard input, however it was focused. Suppressing the ring on text fields would also hide the location cue from keyboard users there. This worker did not do it."
  },
  {
    "id": "DSGN_REBRND-W1-S29",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T09:14:33Z",
    "one_line": "portal/DESIGN.md defines no page terminator, so 'the contract's designed terminator' that RB-s-9 asks every page to end on has no clause to point at.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal DESIGN.md @fb6f5023 (447 lines), case-insensitive search 'terminat|end state|end-state|footer': 0 hits for 'terminat', 'end state' or 'footer'. The only matches are the spacing ladder lines :134-140 and :398, :444",
        "portal DESIGN.md @fb6f5023 C12 :400-411: its 'designed states' are per PANEL (EMPTY, LOADING, ERROR, NO-PERMISSION), and C10 :379 says 'Dead canvas below the fold is a defect'. Neither names a page-end element",
        "rb-s-9 measure JSONs (deliverables 0.9.0_WK_DSGN_REBRND~1/rb-s-9_measure_*.json): no element carrying [data-page-end] on /market, /positioning (sparse) or /attribution, before or after"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-9: 'A page that has run out of content ends with the contract's designed terminator, not with canvas trailing off'; RB9-AC5: 'the page ends with the contract's designed terminator and reads as finished'.",
    "world_is": "The contract carries no terminator clause. This worker did not invent one: DESIGN.md is the single visual authority and lies outside this order's paths, and a page-end element the contract does not define would be a page disagreeing with the contract. Each route ends on its last panel's source-line footer, followed by <main>'s 32px bottom padding."
  },
  {
    "id": "DSGN_REBRND-W1-S30",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T09:14:33Z",
    "one_line": "With populated fixtures the 'lower third of empty canvas' does not occur on /market, /positioning (sparse) or /attribution at 1440x900. The canvas after the last content is 0.036 of a viewport on all three before any change: <main>'s 32px padding.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables 0.9.0_WK_DSGN_REBRND~1/rb-s-9_measure_before_market.json: docHeight 3572, lastContentBottom 3540, shareOfViewportBelowLastContent 0.036 (fixtures rb-s-9-market.json, 11 of 11 URL keys matched)",
        "rb-s-9_measure_before_positioning_sparse.json: docHeight 1565, lastContentBottom 1533, share 0.036. The SPARSE control (one holding per book, all three panels intact) still runs 665px past the fold",
        "rb-s-9_label_collision_before.json layout: /attribution docHeight 1601, lastContentBottom 1569, share 0.036",
        "the unfixtured baseline of the same three routes (netlog, this worker): every /api/general data URL returned 401. That empty-set plane is the one the brief's captures ran on"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-9 THE CELL: 'Every rendered route devotes roughly its lower third to empty canvas while the content above it is tightly packed.'",
    "world_is": "On populated data the three routes this order renders fill past the fold, and the only canvas below the last content is <main>'s p-8 bottom padding (32px, 0.036 of 900). This worker applied C10's spacing (panel inner 30px, 20px between sections) and added no content. The lower-third observation matches the 401/empty-set renders, where panels hold their empty states."
  },
  {
    "id": "DSGN_REBRND-W1-S31",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T09:14:33Z",
    "one_line": "The divergence-bar collision had a third cause the order did not name: each bar sat in Tooltip's inline-flex (shrink-to-fit) trigger, so its width:N% never resolved and every bar collapsed to about its label (16-66px where 100% is 424px).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/components/Tooltip.tsx @fb6f5023 :202 the trigger is className={preserveLayout ? 'contents' : 'inline-flex'}; :60 'If trigger has zero dimensions ... hide tooltip', so preserveLayout (a zero-rect contents box) cannot carry a tooltip",
        "rb-s-9_label_collision_before.json: bar_width_px 62.5 / 16 / 16 / 66.2 / 60.9 / 66.2 / 62.5 / 44.1 over the 8 bars, overlap_px > 0 on 8 of 8 pairs, the 'wide' bars included",
        "rb-s-9_label_collision_after.json: bar_width_px 424 at a 100% tilt, overlap_px 0 on 8 of 8 pairs (QTD, YTD, 1Y and SI, one narrow and one wide bar each)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-9, row-S1 amendment: the mechanism is the ornament's ~15px half-width against the bars' 8px gap, plus bar-relative labels in 'a bar of width: barWidth%'. 'Scope bound: ... You do not change what the panel shows, what it computes, or which figures appear.'",
    "world_is": "A bar of width: barWidth% never got that width, because the percent resolved against its own shrink-wrapped Tooltip trigger. This worker sized each bar with a column-flex wrapper the trigger stretches across, so the rendered bar lengths change to the barWidth the component already computed. The computation and the figures are unchanged. Other Tooltip-wrapped percent-width elements in portal/src were not censused."
  },
  {
    "id": "DSGN_REBRND-W1-S32",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T10:42:26Z",
    "one_line": "RB10-AC2 cannot read MIGRATED inside this order's grant: after the migration its census reads 1 across 265 files, and the one remaining hit is a console.error string in portal/src/context/TimeMachineProvider.tsx, a directory the order's <paths> do not name.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D (the issuer): widen <paths> to portal/src/context/TimeMachineProvider.tsx, or re-scope RB10-AC2's census to the granted directories",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RB10-AC2 invocation run verbatim on the worktree carrying portal a65b939a: 'RAW-STATE-STRINGS: 1 across 265 files' / 'VERDICT: RAW-REMAIN'. At issuance the TO records 143 across 263; rb-s-10_census.py reads 143 across 264 at portal e216de95",
        "portal src/context/TimeMachineProvider.tsx @e216de95 :42 console.error('[TimeMachine] Failed to load restore points:', err) -- a log line inside a .catch, not a rendered state; the file is unchanged at a65b939a",
        "TO-RB-s-10 <paths> names portal/src/ui/, portal/src/components/, portal/src/pages/ and the channel file only; its BOUNDS: 'A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-10 RB10-AC2: the census over every *.tsx under portal/src must print 'VERDICT: MIGRATED' (zero raw state strings); the order's <paths> grant portal/src/ui/, portal/src/components/ and portal/src/pages/.",
    "world_is": "Every hit inside the three granted directories is gone (142 of 143, across 56 files). The criterion's domain is all of portal/src, and the one remaining hit is in portal/src/context/, outside the grant, so no act this order permits can make the criterion read MIGRATED. The string is a developer console message, not a panel state. The order stays open on this row."
  },
  {
    "id": "DSGN_REBRND-W1-S33",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T10:42:26Z",
    "one_line": "The four state components paint their own white ground instead of inheriting the host panel's: C12 fixes a state as navy ink on #FFFFFF, but most host panels on /market and /positioning still resolve to the #0A1733 band, so inside them each state renders as a white content well.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal DESIGN.md @e216de95 C12 :400-401 'inside the panel, in the panel's own frame and size, navy ink on #FFFFFF'",
        "portal CLAUDE.md @e216de95 'Known divergence': Panel variant=\"chart\"/\"mixed\" resolve to the band (rows DSGN_REBRND-W1-S9, DSGN_REBRND-W2-S5)",
        "portal src/ui/components/states/PanelStates.tsx @a65b939a: GROUND = bg-[hsl(var(--bg-surface))], INK = text-[hsl(var(--palette-navy))]; surface='panel' adds the #C4CBDB hairline for a state standing on the canvas",
        "renders rb-s-10_positioning_empty_1440.png and rb-s-10_market_error_1440.png (CANVAS rgb(244, 246, 250) on both): every state reads as a white well with navy ink inside a band-valued panel; the /market tab-level error stands as its own hairline panel"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-10: 'Four designed states, in the existing component set' and 'No error is painted on the bare canvas'; DESIGN.md C12: 'inside the panel, in the panel's own frame and size, navy ink on #FFFFFF'.",
    "world_is": "Most host panels on the two rendered routes are band-valued (#0A1733). A state that inherited its host's ground would put navy ink on navy, so each state paints its own #FFFFFF ground, which the order did not say to do. Until the band-valued panel variants are retired, a state inside such a panel reads as a white well rather than as the whole panel, and that is what the L9 renders show."
  },
  {
   "id": "DSGN_REBRND-S3",
   "project": "DSGN_REBRND",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~D",
   "surfaced_at": "2026-09-14T13:14:18Z",
   "one_line": "The Global RSI bars on /market still render a lime/chartreuse gradient -- an ORDERED quantity on the token file's data.performance family, which no cell ramped -- and RB5-AC5's judgment evidence never renders /market, so the grader cannot see the route where 'no off-palette colour is the loudest thing on any page' is most at issue.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "spec_asserts": "RB5-AC5 (judgment, graded at L9 'from the PNGs'): '... no colour off the brand-derived palette is the loudest thing on any page.' RB-s-4's premise, surviving Amendment 1: non-canon ORDERED scales are single-hue ramps. RB-s-5's cell: chartreuse 'may survive INSIDE a chart series only under RB-s-1's data family.'",
   "world_is": "portal src/components/market-performance/RSIBars.tsx:141-155 @a65b939a: getGradientColors maps RSI value bands to hsl(var(--perf-weak-neg)), var(--perf-strong-pos), var(--perf-neutral) and var(--perf-weak-pos) -- an ordered quantity encoded in unrelated hues. src/index.css:194: `--perf-weak-pos: var(--data-performance-weakPos)` (#84cc16). The token file's data.sentiment still carries greed #84CC16 and chartreuse #ADFF2F. RB-s-4 ramped only --sentiment-* and --ramp-* (its RB4-AC6 checker reads those); the --perf-* family was never in any cell's claim. Hard-coded #84cc16 also survives in RSIModal.tsx:165/338/344 and FearGreedModal.tsx:160/861, outside every grant. Rendered 2026-09-14 from the feature worktree's dev server (port 5174): the bars are the most saturated colour on /market. RB-s-5's deliverables render /positioning and /portfolio-management only.",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "portal src/components/market-performance/RSIBars.tsx:141-155 @a65b939a (getGradientColors -> var(--perf-*))",
     "portal src/index.css:194 @a65b939a (--perf-weak-pos: var(--data-performance-weakPos), commented #84cc16)",
     "portal design/brands/opal-capital.json @a65b939a data.sentiment: greed #84CC16, chartreuse #ADFF2F",
     "portal src/components/market-performance/RSIModal.tsx:165,338,344 and FearGreedModal.tsx:160,861 @a65b939a: hard-coded #84cc16",
     "a 1440 render of /market from the feature worktree's dev server on port 5174, 2026-09-14, read by the issuer"
    ]
   },
   "notes": "Surfaced by the issuer while building Andrew's local demo of the feature branch (his request, 2026-09-14). Not armed: nothing in round 1 is endangered by it. For L9 -- the CVO grading RB5-AC5 should read a /market render, not only RB-s-5's two routes. For L10 -- the --perf-* and --sentiment data families are an ordered scale no cell owned; a round-2 cell could ramp them, or the CTO could rule chart-series colour out of the accent budget explicitly.",
   "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "DSGN_REBRND-W3-S3",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~3",
    "surfaced_at": "2026-09-14T13:32:23Z",
    "one_line": "23 of the inventory's 96 render obligations could not be rendered in their named state, yet rb13-coverage-check.py reads COVERED 96 of 96, because it checks that a mapped PNG exists and not what it shows: 12 data routes' DEFAULT rows render the route's ERROR (the live dev plane refuses the inert ui-smoke token with 401 and no ui-smoke fixture exists for them), 10 EMPTY rows render the app error boundary or an ERROR under the only empty shape constructible without a fixture, and /valuations|toggled-panel has no control to toggle while its data is refused.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D (issuer of rb13-coverage-check.py and of RB-s-12, whose inventory names the fixture sources); the per-row verdicts the L9 read needs are in org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/rb13-state-reached.json",
    "spec_asserts": "TO-RB-s-13: 'For every row marked with a render obligation: one read render' and RB13-AC2R 'every render obligation ... maps ... to a render of THIS cell'. The inventory (design/brand/portal-surface-inventory.json) defines state 'default' as 'the route's primary/landing rendering with realistic (non-empty, non-error) data' and gives every row a `fixture` source; the spawn note for this order says 'Each inventory row names its own fixture in its fixture field'.",
    "world_is": "Of the files the inventory's `fixture` field names for data routes, none is a ui-smoke.mjs {url-substring: body} fixture: model-portfolios.json and advisor-intelligence.json are page descriptions (keys pageName/pageUrl/features...), sscn_divdef_001_smoke.json is a frontend-dev constitution (keys name/login/scenarios), and cma.md, positioning.md and macro.md are prose scenario matrices. The only consumable fixtures are the rb-s-9 set, which cover /market, /positioning and /attribution; the other 13 data routes have fixture NONE or an unconsumable file. With no fixture the page runs against the live dev plane, which answers the inert token with 401 on every /api data request (ui-smoke --netlog on /valuations: 10 of 10 data requests 401), so the DEFAULT render shows the route's error handling. EMPTY was constructed as a shape-preserving emptied fixture where one exists and as a bare [] where none does; under [] nine routes fall to the app error boundary ('Something went wrong') and /factor-tilts renders its ERROR, so those ten renders cannot distinguish product fragility from the harness's shape. rb13-coverage-check.py still prints COVERED: 96 of 96, because it tests (OWN / png).is_file() and nothing about content.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb13-coverage-check.py -> COVERED: 96 of 96 | distinct PNGs used 96 / VERDICT: COVERED (rc=0), at workspace @4721f1f6ee",
        "ui-smoke.mjs valuations --netlog at portal @a65b939a (branch wk-dsgn_rebrnd-3b, == feature/d13-visual-elevation): GET 401 on all 10 /api/scoped and /api/general data requests; render shows \"Valuation metrics could not be loaded ... Cause: API request failed: 401 Unauthorized\"",
        "fixture shapes read at portal @a65b939a portal/.frontend-dev/testing/: rb-s-9-market.json keys are url substrings (summary/all-returns.json, ...); model-portfolios.json keys pageName,pageUrl,description,features,...; sscn_divdef_001_smoke.json keys name,description,login,scenarios",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/rb13-state-reached.json: per obligation row, reached YES / YES-NO-VISIBLE-DIFFERENCE / NO / NOT-RENDERABLE with what the render shows; the 23 NO rows are listed there by key",
        "sha256 of the renders: /factor-tilts default, empty and error are one image (1 distinct of 3); /valuations default and toggled-panel are one image (1 of 2)"
      ]
    },
    "notes": "No fixture was minted and no live token was minted: portal/.frontend-dev/testing/ is outside this order's <paths>, and a real bearer is not this order's to mint. The renders are on record and were read; what each one shows is stated per row rather than claimed as the named state.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "DSGN_REBRND-W3-S4",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~3",
    "surfaced_at": "2026-09-14T13:32:23Z",
    "one_line": "Under a forced failure (every data request answered 503), the live 401, or held requests, seven routes draw data, EMPTY or LOADING where C12 requires ERROR: /market's Global RSI bars and Fear & Greed dial show a reading (50, 'Neutral', stamped with the current time; the RSI tooltip reads 'Now 50.0, 90D ago 50.0, Neutral'); /positioning and /advisor-intelligence render EMPTY sentences; /attribution holds its skeleton and renders EMPTY; /portfolio-management renders 0.00 metrics and an EMPTY sentence identically in default, empty, loading and error; /ticket-center shows its error line above 'No open tickets.'; /data-refresh History says 'No History Yet' on a 401.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D, routing to RB-s-10 (the four-states cell), whose own result declares failure-swallowed-as-EMPTY censused only at the four sites it met",
    "spec_asserts": "portal/DESIGN.md C12 and TO-RB-s-10 RB10-AC5: every panel with nothing to show uses exactly one of the four states (EMPTY, LOADING, ERROR, NO-PERMISSION), the message says which in plain words, and a failed fetch renders ERROR. PRD binding ruling: 'the charts keep their colour' presumes the chart shows data it has.",
    "world_is": "Read renders at portal @a65b939a (branch wk-dsgn_rebrnd-3b, == feature/d13-visual-elevation), 1440x900, canvas rgb(244, 246, 250): rb-s-13_market_error_1440.png (41 data requests answered 503): RSI draws three bars near 50 and Fear & Greed shows 50 'Neutral' dated September 14th, 2026, 8:10a ET; walks/rb-s-13_market_error_1440_kbd-sheet.png stop #35 shows the RSI tooltip 'Now 50.0 / 90D ago 50.0 (0.0) / Status Neutral'; the same fabricated readings are in rb-s-13_market_loading_1440.png and in the RB13-AC3 render rb-s-13_market_coverage_1440.png (live 401). rb-s-13_positioning_error_1440.png: summary panel draws no bars and no message, composition and holdings read 'No holdings for INT.'. rb-s-13_advisor-intelligence_error_1440.png: 'No AUA or net-new-asset history for this partner yet.' and 'No advisors to rank for this period and metric.' on 503. rb-s-13_attribution_error_1440.png: the positioning panel stays in its skeleton and the breakdown reads 'No holdings for this portfolio.'; rb-s-13_attribution_empty_1440.png: all weights 0.00 with TOTAL 100.00 / 100.00. rb-s-13_portfolio-management_{default,empty,loading,error}_1440.png are one image (sha256 832b39892efc..., 1 distinct of 4) although the harness fetched live, emptied, held and failed (19 requests 503) respectively. rb-s-13_ticket-center_error_1440.png: error line above 'No open tickets.'. rb-s-13_data-refresh_toggled-panel_1440.png: 'No History Yet' under a 401.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/rb-s-13_capture-log_32_*.json: per render, the request counts (data / fixtured / held / failed / emptied / live) that establish which condition was constructed",
        "sha256: rb-s-13_portfolio-management_default/empty/loading/error_1440.png all 832b39892efc (1 distinct of 4)",
        "the listed PNGs, each read before this row; all in org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/"
      ]
    },
    "notes": "Rendered and read, not fixed: the order's BOUNDS say a defect seen is a row routed to the owning cell. The /market readings are the sharpest instance, because a neutral reading and a failed fetch are indistinguishable to an advisor.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "DSGN_REBRND-W3-S5",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~3",
    "surfaced_at": "2026-09-14T13:32:23Z",
    "one_line": "Beyond the four designed components, the read renders show a dozen further state treatments and developer text on client surfaces: bare spinners or a plain 'Loading...' line (/valuations, /correlations, /portfolios, /advisor-intelligence, /security-scanner, /data-refresh, /investor-reporting, /login); red text on the bare canvas plus a raw code IR-REQUEST-FAILED (/investor-reporting); an amber warning inside the band (/data-refresh); a red-on-pink banner (/positioning ETFs); the same ERROR sentence twice on one page (/factor-tilts); three error idioms across four auth pages, two of them light red-400 on pink; a tab that renders nothing (/philosophy Views); raw JSON response bodies in Cause lines; a CORS/S3 developer note (/portfolios); and 'silver page bg' contrast copy (/dev/page-surface-control).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "portal/DESIGN.md C12 fixes each state's form (navy ink on #FFFFFF, a status icon beside canvas-level errors, the cause once, no message repeated) and C3 fixes the light canvas law that superseded the 2026-07-15 silver archetype; UI_VERIFICATION.md step 3 asks every state the change touches to be screenshot and read against those clauses.",
    "world_is": "Read renders at portal @a65b939a (branch wk-dsgn_rebrnd-3b, == feature/d13-visual-elevation): rb-s-13_investor-reporting_default_1440.png (red 'Scope could not be resolved...' on the canvas, 'Failed / IR-REQUEST-FAILED' with an accent Retry); rb-s-13_portfolios_default_1440.png ('Distribution Data Unavailable ... requires CORS configuration on the S3 bucket ... may not be accessible in local development'; 'Category views could not be loaded right now.' with no icon); rb-s-13_valuations_loading_1440.png and rb-s-13_correlations_loading_1440.png (a bare spinner on the canvas); rb-s-13_security-scanner_loading_1440.png ('Loading factor data...' grey on navy); rb-s-13_data-refresh_default_1440.png (amber 'Could not load current data state' in the band); rb-s-13_positioning_toggled-panel_1440.png (red-on-pink ETF banner); rb-s-13_factor-tilts_default_1440.png (the same 'Factor tilts could not be loaded.' in two panels); rb-s-13_forgot-password_error_1440.png and rb-s-13_reset-password_error_1440.png (light red on pink), rb-s-13_login_error_1440.png (dark red on pink), rb-s-13_change-password_error_1440.png (white on solid red); rb-s-13_philosophy_toggled-panel_1440.png (Views selected, nothing beneath); Cause lines carrying {\"error\":\"Invalid or expired token\"} on /valuations, /macro, /market, /ticket-center; rb-s-13_dev_page-surface-control_default_1440.png ('Contrast gate: WCAG AA >= 4.5:1 against silver page bg').",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "each listed PNG, read before this row, in org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/",
        "TO-RB-s-10 result (deliverables/0.9.0_WK_DSGN_REBRND~1/four-states.result.md) declares the spinner and panel-level residue as not done, so part of this row is that declaration seen on screen"
      ]
    },
    "notes": "INERT: nothing here misstates data; it is the residue and the idiom spread the L9 grade of RB10-AC5 and RB13-AC4 reads. Routed to 2.0.0_SA_COO~D for RB-s-10 (states), RB-s-8 (the demo page's superseded copy) and whichever cell owns the auth pages.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "DSGN_REBRND-W3-S6",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~3",
    "surfaced_at": "2026-09-14T13:32:23Z",
    "one_line": "The 58 keyboard walks (1,379 stops, every one focus-visible with a painted ring) found what a ring cannot show: the file drop zones on /data-refresh and /trade-submission never take focus, so each page's upload is unreachable from the keyboard; /portfolios puts two stops on invisible chart internals (an empty svg and a bare g); and one of five loads of /attribution with its fixture fell to the app error boundary on mount. The read renders add two visual defects: the top '90D' marker on /market's Global RSI is clipped at the plot's upper edge, and /trade-submission's form fields paint a mid-grey fill inside the #0A1733 band.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-RB-s-6 and portal/DESIGN.md C11: every interactive surface is reachable by keyboard and shows the one focus ring; RB-s-13's cell: 'for every row marked interactive: a keyboard walk with a screenshot at each stop'. RB-s-9 (row S1 lineage): a chart label is never painted over or cut by its own ornament. C3/C5: controls inside the one band follow the band's control vocabulary.",
    "world_is": "Walks at portal @a65b939a (branch wk-dsgn_rebrnd-3b, == feature/d13-visual-elevation), Tab from a blurred document until focus returns to the first stop. org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/walks/rb-s-13_data-refresh_{default,error,toggled-panel}_1440_kbd-sheet.png: 21/21/22 stops, none on the 'Drag and drop files or click to browse' zone. walks/rb-s-13_trade-submission_{default,error}_1440_kbd-sheet.png: 34 stops each, the fields, checkboxes and Submit are reached, the 'Drop file here or click to browse' zone is not. walks/rb-s-13_portfolios_{default,error,toggled-panel}_1440_kbd-sheet.png stops #20 (svg[role=application], an empty navy rectangle) and #21 (a bare g element). /attribution|toggled-panel: the second harness run captured 'Something went wrong' with 7 data requests and 0 fixtured, so the page failed on mount before the YTD click; the first run and three sequential re-runs (rb-s-13_capture-log_rewalk-date-inputs-and-attribution-x3.json) rendered it populated, so 1 of 5 loads failed, and the failing load ran beside a second harness process. rb-s-13_market_{default,empty,loading,error}_1440.png and rb-s-13_market_coverage_1440.png: the Equities '90D' marker reads 'Y0D', clipped at the plot top. rb-s-13_trade-submission_default_1440.png: Fund, Weights as of, Trades as of, Destination and Comments render as mid-grey filled inputs inside the band.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/walks/*_kbd.json: 58 walks, 1,379 stops, fv true and ring true at every stop, every walk WRAPPED (returned to its first stop)",
        "the listed sheets and PNGs, each read before this row",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/rb-s-13_capture-log_rewalk-date-inputs-and-attribution-x3.json: three sequential /attribution|toggled-panel loads, each fixtured 8 and OK click YTD"
      ]
    },
    "notes": "INERT: seen and recorded, not fixed. Route: 2.0.0_SA_COO~D to RB-s-6 (focus reachability of the drop zones and of the chart internals), RB-s-9/RB-s-11 (the clipped RSI marker), RB-s-3/RB-s-5 (field fills in the band). The /attribution mount failure is an unreproduced one-in-five and is stated as exactly that.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "DSGN_REBRND-W1-S34",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T15:08:26Z",
    "one_line": "The side-by-side render pair has no site half. No render of opalinvest.com is on record: design/brand holds only the .md and .json of the 2026-09-11 capture. A new capture of the site is egress this order carries no word for. So the pair was produced as the three portal renders plus a sheet drawn from the two JSON files.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "design/brand/ @ff2bcda841: opalinvest.com.json and opalinvest.com.md and no image of the site; a glob for *opalinvest* under design/ returns those two files only, and *opalinvest*.png under the main workspace's .claude/skills/ returns nothing",
        "docs/briefs/portal-visual-elevation-brief-20260911.md:181-183 @ff2bcda841: 'Full output: design/brand/opalinvest.com.md and .json'",
        "TO-RB-s-14 @ff2bcda841, Amendment 1: re-pulling the extractor 'is EGRESS off Opal infrastructure and needs Andrew's per-use word, which this order does not carry'; CLAUDE.md Agent Autonomy: 'Excluded: all egress off Opal infrastructure.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-14 THE CELL: 'Produce the ON-DEMAND half -- the two JSON files and a side-by-side render pair -- and record it.'",
    "world_is": "The portal half is rb-s-14_market_extract_1440.png, rb-s-14_positioning_extract_1440.png and rb-s-14_portfolio-management_extract_1440.png, each full-page at 1440 wide. rb-s-14_side-by-side_1440.png draws the values of the two JSON files side by side, one row per IV.3 dimension, with the three portal renders as thumbnails. It is a render of measurements, not of the site. The site render is ABSENT. This worker did not capture opalinvest.com, because the capture would leave Opal infrastructure and the order carries no word for it.",
    "notes": "For L9: the RB14-AC5 walk visits the live site in any case. An on-demand site render needs either Andrew's word for one capture or the 2026-09-11 capture's screenshots, if they were kept outside the tree."
  },
  {
    "id": "DSGN_REBRND-W1-S35",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T15:08:26Z",
    "one_line": "RB14-AC1 counts the file's top-level keys, not its routes. A file in the website file's shape carries at least 12 keys, so it reads MEASURED however many routes it covers. A bare {a, b, c} object also reads 'ROUTES-MEASURED: 3 / VERDICT: MEASURED'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RB14-AC1 invocation @ TO-RB-s-14 ff2bcda841: n = len(d) if isinstance(d, list) else len(d.keys()); VERDICT MEASURED if n >= 3",
        "design/brand/opalinvest.com.json @ff2bcda841: 12 top-level keys (source, captured, viewport, pagesAnalyzed, stack, color, typography, space, shape, grid, tasteDNA, portalDelta); the pages it covers are the pagesAnalyzed list",
        "the verbatim invocation run from a scratch directory whose design/brand/portal-routes.json is {\"a\": 1, \"b\": 2, \"c\": 3}: 'ROUTES-MEASURED: 3' / 'VERDICT: MEASURED', rc=0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB14-AC1: 'the portal-side measurements exist in the website file's shape and cover AT LEAST the three fixed comparison routes. A missing file reads INCOMPLETE rather than throwing.'",
    "world_is": "The instrument's printed ROUTES-MEASURED is the number of top-level keys. On design/brand/portal-routes.json it prints 13, and the file covers 3 routes, listed in pagesAnalyzed. The PASS on this order rests on the key count, so the route coverage is stated in the proof from pagesAnalyzed and is not established by the instrument. The missing-file arm works as stated."
  },
  {
    "id": "DSGN_REBRND-W1-S36",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T15:08:26Z",
    "one_line": "The shadows dimension no longer agrees. The brief records shadows as the one agreement, but at portal a65b939a painting box-shadows sit on 5, 1 and 2 elements of /market, /positioning and /portfolio-management: a shadow-lg on the navigation rail on all three, one on the Optimization Report panel, and four red 12px glows on /market markers.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "extract.js effects.shadows in rb-s-14_extract_{market,positioning,portfolio-management}.json (deliverables/0.9.0_WK_DSGN_REBRND~1/): 'rgb(239, 68, 68) 0px 0px 12px 0px' x4 and a five-layer shadow ending 'rgba(0, 0, 0, 0.1) 0px 1...' on /market; the five-layer shadow x1 on /positioning and x2 on /portfolio-management",
        "attribution pass on the same routes and fixtures, keeping layers with non-zero alpha: aside.fixed.top-0.bottom-0.left-0 (48x900) 'rgba(0,0,0,0.1) 0 10px 15px -3px, rgba(0,0,0,0.1) 0 4px 6px -4px' on 3 of 3 routes; div.w-full.rounded-[4px].dark-band (1328x656, Optimization Report) the same on /portfolio-management; 4 x div.absolute.rounded-full (12x12) 'rgb(239,68,68) 0 0 12px 0' on /market",
        "design/brand/opalinvest.com.json @ff2bcda841 shape.shadowCount 0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD FWD-1 SOURCE: 'IV.3 (the portal contradicts it on every dimension but shadows)'; brief IV.3: 'Shadows | none | none | **the only agreement**'.",
    "world_is": "At portal a65b939a, rendered at 1440x900 with the rb-s-9 fixtures on /market and /positioning and no fixture on /portfolio-management, the portal paints a Tailwind shadow-lg on the navigation rail on every route and on the Optimization Report band panel. /market also has four red glows. The IV.3 shadows row therefore reads DIFFERS in design/brand/portal-routes.json, where the brief and the PRD record agreement. Which cell owns elevation is not judged here.",
    "notes": "Rendered and read, not fixed: this order's grant is the portal-routes file and the channel. For L9, the RB14-AC4 grade reads the shadows row from the file, not from the brief."
  },
  {
    "id": "DSGN_REBRND-W1-S37",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T15:08:26Z",
    "one_line": "The 270 +/- performance figures on /market paint #2DCE89 (147 text nodes) and #F5365C (123). Neither value matches any of the 4 --status-* or 23 --data-* tokens on the page's :root, so the busiest route's rendered gain/loss colour sits outside both token families.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "rb-s-14_extract_market.json (deliverables/0.9.0_WK_DSGN_REBRND~1/) extract.colors.textColors: rgb(45, 206, 137) x147, rgb(245, 54, 92) x123 -- the two most frequent text colours on the route",
        "attribution pass on /market with portal/.frontend-dev/testing/rb-s-9-market.json: both colours on span.text-sm.font-semibold.group-hover:font-bold.transition-all.cursor-help, 147 and 123 nodes",
        "computed :root tokens on the same page: --status-success 152 55% 32% (rgb 37,126,85), --status-danger 356 62% 46% (rgb 190,45,54), --status-info, --status-warning, and 23 --data-* tokens; none within 3 per channel of either rendered value (rb14-build.py comparison, printed 'matchesATokenWithin3': [] for both)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "brief IV.3: 'Status colours | brand-derived | Creative Tim \"Argon\" template | src/index.css:40-43' (the defect the project removes); PRD preamble: 'the charts keep their colour'.",
    "world_is": "At portal a65b939a the four --status-* tokens are no longer the values the brief cites, but the gain/loss figures in /market's Equity, Fixed Income and Commodities tables do not read them, nor any --data-* token. They paint #2DCE89 and #F5365C. That these are the Argon template's success and danger values is recalled, not read from a file here. Whether figure text is a status use or a chart series is not judged here; the values are recorded in design/brand/portal-routes.json color.status.renderedFigureColours.",
    "notes": "Seen and recorded, not fixed; not searched for in the source (the order navigates to its paths and does not hunt). Relates to row DSGN_REBRND-S3, the other /market colour outside a cell's claim."
  },
  {
    "id": "DSGN_REBRND-W2-S18",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T17:12:09Z",
    "one_line": "The retired one-accent rule is stated in more places than the order's seven-carrier list: 6 further in-grant sentences (DESIGN.md frontmatter tab-active and its 'Kept' line, Controls.tsx:14, SentimentGauge.tsx:49, MarketRegimeIndicator.tsx:61, OptimizationSummaryHeader.tsx:184-185) were updated; 1 out-of-grant carrier (the brief's O4) was not.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO for the PRD's FWD-4 text (the order's own preflight names it the CTO's to amend) and 4.0.0_SA_CRO for the brief's O4 -- both outside every worker grant, both still state the retired one-accent budget until amended.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "census instrument: native Grep (ripgrep), case-insensitive, pattern 'one (persistent )?(primary|purple|accent|#5F3BE3)|one-accent|ONE `?#5F3BE3|navy underline|not a tab indicator|DESIGN.md C8|one purple' over portal/ (node_modules excluded), design/, .claude/ and docs/, plus '\\bC8\\b' over portal/ and a read of portal/DESIGN.md for 'accent|indigo|underline|avatar|tab-active' -- run at portal a65b939a / workspace 3b45dfb5e3 before any edit",
        "NOT ON THE LIST, restating the retired rule, UPDATED in grant: portal/DESIGN.md:172-174@a65b939a frontmatter components.tab-active textColor and underline '{colors.navy}' (now '{colors.indigo}'); portal/DESIGN.md:429@a65b939a 'accent rationed to one per view' (now qualified with Andrew's 2026-09-14 widening); portal/src/ui/components/Controls.tsx:14@a65b939a 'spends the view's one accent on a state'; portal/src/components/market-performance/SentimentGauge.tsx:49@a65b939a and MarketRegimeIndicator.tsx:61@a65b939a 'spending the view's one accent on a state'; portal/src/pages/PortfolioManagement/components/OptimizationSummaryHeader.tsx:184-185@a65b939a 'THE ONE persistent primary action of this view, and the only accent fill on it' (false once the sidebar active item is filled)",
        "READ AND LEFT, still true under the amended C8 because each speaks of the one ACTION or the band: portal/src/index.css:304-307@a65b939a (::selection not counted against the one persistent primary action), portal/src/index.css:500-503@a65b939a (the focus ring never counts as the one persistent primary action), portal/src/ui/components/Controls.tsx:55-58@a65b939a (the band carries no primary action)",
        "OUT OF GRANT, NOT EDITED: docs/briefs/portal-visual-elevation-brief-20260911.md:62@3b45dfb5e3 'O4 is complete when a view spends its accent colour on the one primary action and nothing else'; the three other docs/ hits (docs/architecture/ADHC_PREFLT_PRD.md:98, ADVI_INFGRO_PRD.md:91, ADVI_PERFORMANCE_E2E_STANDARDIZATION_PLAN_20260806.md:380) use 'one primary' in unrelated senses and were read and excluded",
        "census bound: org/ was not swept beyond the order's own citations, so the PRD and decomposition texts are known only through the order's preflight line, not by this census"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-5 Amendment 1: 'THE RULE IS WRITTEN IN SEVEN CARRIERS: UPDATE EVERY ONE, OR THE OTHERS KEEP STATING THE RETIRED RULE', listing DESIGN.md C8 and :7/:415/:421, portal/CLAUDE.md:53, DESIGN_SYSTEM.md :64/:97, frontend-dev SKILL.md:58 and the comments at PageHeaderVariants.tsx:34-37/:49, TabNavigation.tsx:64-67, Controls.tsx:2,6 -- and 'A carrier you find that is NOT on this list is a surprise row, not a skip.'",
    "world_is": "Seven further carriers exist. Six are inside this order's <paths> and each stated the retired rule in words (a navy active-tab token, 'one accent per view', 'the only accent fill'); each was re-worded to the amended C8 in the same portal commit as the listed carriers. Three more in-grant sentences mention the one primary action but remain true and were left. One carrier, the brief's O4, is outside the grant and still reads 'the one primary action and nothing else'.",
    "notes": "Filed because the order's census was issued as complete ('seven carriers') and was not: the frontmatter token is the sharpest miss, because it is a machine-readable design token that a generator or linter would read as the active tab's colour, and it said navy after the prose clause said indigo."
  },
  {
    "id": "DSGN_REBRND-W2-S19",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~2",
    "surfaced_at": "2026-09-14T17:12:09Z",
    "one_line": "App.tsx paints the sidebar rail's right border with an accent border-image (hsl(var(--primary) / 0.3) gradient) on every route -- an accent paint outside the five identity sites, which the amended C8 says is 'nowhere else'; the order's table does not name it, so it was left unmoved.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- whether the rail's border-image is retired or added to the budget is a call this order did not make; until it is made, RB5-AC5R's 'AND NOWHERE ELSE' reads one extra accent paint on every route.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/App.tsx:261@a65b939a (:265 after this order's edits): the <aside> style sets borderImage 'linear-gradient(to bottom, hsl(var(--primary) / 0.3), transparent 50%, hsl(var(--primary) / 0.3)) 1' over a 1px right border",
        "rb-s-5r_accent-walk.log (deliverables/0.9.0_WK_DSGN_REBRND~2/): the border-image probe (computed borderImageSource matching rgba(95, 59, 227)) classifies 'aside ... border-image 0,0 48x900' as OTHER on 3 of 3 routes (/positioning, /portfolio-management, /market)",
        "round 1 declared it excluded as outside <paths>: deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-5.accent-controls.proof_of_spec.json declared_exclusions[0] 'the shell's active nav item and avatar accent fills, and the sidebar border-image'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-5 Amendment 1: 'PLUS identity accents at exactly five named places, and nowhere else'; RB5-AC5R: 'the identity accents at the five named sites AND NOWHERE ELSE, also enumerated'.",
    "world_is": "App.tsx is now inside <paths>, but the order's table names only its NavLink active branch (site 4) and its avatar (site 5). The rail's border-image is a sixth accent paint in the chrome on every route: not a site, not an action, not transient. Removing it would be an act the order did not name, so it is recorded here and enumerated as OTHER in the result file.",
    "notes": "Form only: whether a 1px, 30%-alpha gradient edge counts against the budget is L9's to judge."
  },
  {
    "id": "DSGN_REBRND-S4",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~D",
    "surfaced_at": "2026-09-14T16:56:46Z",
    "one_line": "prd-signoff.py hid every stamp refusal: it printed only the LAST 6 lines of safe-commit's output, and safe-commit's own DO-NOT-GREP reminder is exactly 6 lines, so a lane violation and a foreign MERGE_HEAD both read only as 'refused' with no reason -- and the TREE_PRD_SIGNOFF lane did not list the designated brief-half signer the tool itself supports.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/prd-signoff.py:229-231 (before ed78c9c6c6): tail = (sc.stdout + sc.stderr).strip().splitlines()[-6:]",
        "the DSGN_REBRND v0.3 brief-half stamp, 2026-09-14 16:56Z: two runs printed only the DO-NOT-GREP block; the same commit run by hand showed the reasons (a foreign MERGE_HEAD beaefc6cf5, then 'VIOLATION ... lane=TREE_PRD_SIGNOFF ... agent=2.0.0_SA_COO~D not in permitted_agents')",
        ".owned-paths.yaml:905 TREE_PRD_SIGNOFF permitted_agents [4.0.0_SA_CRO, 3.0.0_SA_CVO] against prd_signoff_lib.py:36-39 REVIEWERS['brief'] = (4.0.0_SA_CRO, 2.0.0_SA_COO)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md Rule 27 L4-R: the brief half is signed by 4.0.0_SA_CRO or a designated/live 2.0.0_SA_COO; the stamp is 'python .tools/prd-signoff.py sign', which commits the file through safe-commit.",
    "world_is": "The designated signer's stamp was refused by the lane the tool writes into, and the tool hid the reason. Both are fixed: 1.0.0_SA_CTO @ed78c9c6c6 prints safe-commit's whole output on a refusal, and 0.0.0_AB_MSTR @f7fe05777f (LD-0565) adds 2.0.0_SA_COO to TREE_PRD_SIGNOFF. The v0.3 stamp went through under the audited override (17:06:47Z), following the 09-11 precedent; the v0.5 stamp @b84d531a63 needed none.",
    "notes": "Filed for the record and the L8 compile, not as a live hazard: both remedies landed before this row. Resolution pins: ed78c9c6c6 (tool), f7fe05777f (lane)."
  },
  {
    "id": "DSGN_REBRND-W1-S38",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_REBRND~1",
    "surfaced_at": "2026-09-14T18:04:16Z",
    "one_line": "Same route, same width, same pre-round tree and no fixtures: two captures of /market on the BEFORE tree (portal 787015e8) caught the MULTI-ASSET tab body in two different states, a loading spinner and then a red error line, so 'same route, width and fixtures' does not fix which state a BEFORE capture shows.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/task-orders/DSGN_REBRND.TO-RB-s-15.andrew-pack.md:29-32 @3327c5a890 (Amendment 1: both sets the same three routes, 1440 wide, NO fixtures, so the pair is equal)",
        "run 1: node scripts/ui-smoke.mjs market <D>/rb-s-15_market_before_1440.png --port 5192 -> 'CANVAS: rgb(195, 202, 218)', rc=0; the PNG shows a spinner in the MULTI-ASSET tab body; kept as rb-s-15_market_before_1440_run1-loading.png, sha256 87bdf3c2aa9bc2b241944db8178d5ba1ed57afe3063cafeb5dfc09d8d2b0369c",
        "run 2, same server, minutes later, to .scratch/rerun_market_before.png -> 'CANVAS: rgb(195, 202, 218)', rc=0; the PNG shows 'Failed to load market data: ... Failed to fetch market returns from all available sources' in the tab body; copied to rb-s-15_market_before_1440.png, sha256 b42049a2e1e4dfc790a9ed86b94c317f96e3fce8812691a95977cb4630a5cc51",
        "control: the AFTER tree (portal 086371dd, port 5191) showed the same settled error with a retry button in both of its two /market captures"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-RB-s-15 Amendment 1: render both sets with the same three routes, at 1440 wide, with NO fixtures, so that the pair is equal; ui-smoke.mjs is the capture.",
    "world_is": "On the BEFORE tree the /market MULTI-ASSET tab body depends on capture timing: 1 of 2 captures showed a spinner and 1 of 2 showed the settled error line. Both printed the same canvas and rc=0. The pack pairs the settled BEFORE capture with the AFTER capture and keeps the spinner capture beside it, disclosed on the pack's own page. Neither tree was changed. The other two BEFORE routes were captured once each.",
    "notes": "Filed on form, not significance: the order's equal-inputs rule was followed and still gave two BEFORE states. Which capture is the fairer BEFORE for the /market tab body is L9's reading."
  },
  {
    "id": "DSGN_REBRND-S5",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T23:10:00Z",
    "one_line": "Round 3 E4 (fe461611) moves the Holdings Breakdown's grand-total row onto the selected rung; its dash ink (text-white/60) then computes to 4.23:1 against that rung, below the 4.5:1 text minimum, and the subtotal row's separation from the body drops from 1.35:1 to 1.22:1. No test asserts colour or contrast for either E4 pin.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal origin/DEV fe461611: HoldingsBreakdownTable.tsx:237-242 (tile and selected rungs), HoldingsTab.tsx:1038-1111; the rung values in index.css:367-370; this seat's contrast arithmetic (WCAG relative luminance) on those values, 2026-10-02 22:xZ",
        "no test file names a --layer-* rung; the four tests that render the table give the same result with fb5d6116 and fe461611 reversed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The design law: text on a dark panel meets 4.5:1; named layers separate visibly.",
    "world_is": "One ink falls just under the floor on the new rung and the subtotal band is harder to see than before. Measured by arithmetic on the CSS values, not on a rendered page.",
    "notes": "INERT: DEV only (PROD dcdc89b1 does not carry the pins). Owner 2.0.0_SA_COO~D: raise the dash ink (white/70 clears 4.5 by the same arithmetic, to be measured) and add one contrast assertion for the E4 rungs."
  },
  {
    "id": "DSGN_REBRND-S6",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~D",
    "surfaced_at": "2026-10-03T00:25:00Z",
    "one_line": "Ruling on DSGN_REBRND-W2-S8 (this seat's, per 1.0.0_SA_CTO batch 80 item 10, with the round 3 E4 contrast table in hand): the five canon hexes never move; on /positioning every canon mark sits on the band, where each clears 4.5:1 as text and 3:1 as a graphic, and a highlighted name keeps its canon colour on a band ground.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~D",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "walk 20261003T000242Z (local, signed in, GET-only, walker --contrast-table): 316 interactive text pairs on /positioning (Models Portfolio and Custom, ETFs, Satellites), 0 under their bar",
        "computed, WCAG 2.1 relative luminance, on the band rung (221 67% 12%): UST #f97316 6.33, ST #f59e0b 8.26, INT #10b981 7.0, LT #3b82f6 4.83, ULT #ef4444 4.72; on the body rung LT read 4.08 and ULT 3.99 (walk 20261002T233417Z)",
        "portal 44d6a215 panels/PositioningSummary.tsx HEADER_HOVER_GROUND: the hovered name takes --layer-strip as its ground; Andrew-direct 2026-09-15 (quoted in shared/bookColors.ts): a highlighted name uses its canonical colour"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarms DSGN_REBRND-W2-S8 for /positioning: the lock holds (no hex moved) and no canon pair on the page is under its bar; the condition on LIGHT grounds is DESIGN.md C4 (every canon mark carries its rung label or sits beside a legend entry, model names in navy ink), enforced by each page's own cells.",
    "spec_asserts": "TO-RB-s-7 Amendment 1 A locks the five canon values; the contract commits to SC 1.4.11 (3:1 for a graphical object) and SC 1.4.3 (4.5:1 for text).",
    "world_is": "On the band the five hexes clear both bars. On the body (18%) two fall under 4.5 as text, so a canon-coloured name is never drawn on the body: its highlighted state supplies the band as its ground. On white three fall under 3:1, which C4's label rule answers.",
    "notes": "Corrects this seat's first reading in portal 661e49b3 (the hover colour removed), which contradicted Andrew's 2026-09-15 word; 44d6a215 restored it on a band ground."
  },
  {
    "id": "DSGN_REBRND-S7",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~D",
    "surfaced_at": "2026-10-03T00:25:00Z",
    "one_line": "Ruling on DSGN_REBRND-W1-S11 (this seat's, batch 80 item 10): the dark-mode accent conflict is latent -- no code path selects dark mode -- and splitting the accent into a fill token and an ink token is the precondition of shipping a dark-mode toggle.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~D",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "census over portal/ (node_modules excluded): 'dark-mode' appears in 3 files only -- src/index.css, design/themes/opal-capital.css, design/OPAL_CAPITAL_LIGHT_DARK_SYSTEM.md; no source file adds the class, and no theme switch sets it (ThemeProvider/useTheme/prefers-color-scheme census: PageThemeProvider only, which sets a page accent, not a mode)",
        "design/OPAL_CAPITAL_LIGHT_DARK_SYSTEM.md lists 'Implement dark mode toggle component' as an unchecked item",
        "W1-S11's own arithmetic: white-on-accent needs accent luminance <= 0.1833 and accent-on-band needs >= 0.2002 -- no single value"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarms DSGN_REBRND-W1-S11 as latent: no user can select the dark mode today, so no pair is served. RULING for the day a toggle is built: the accent splits into an accent-fill token (white text on it, luminance <= 0.1833) and an accent-ink token (on the dark band, luminance >= 0.2002); the toggle does not ship without the split.",
    "spec_asserts": "RB3-AC7: every text/background pair, including in the selected dark mode, meets SC 1.4.3.",
    "world_is": "The dark-mode CSS exists but nothing selects it; the light world (the only one served) passes both accent pairs (6.52 and 6.03 per W1-S11's own notes).",
    "notes": "Route for the split when a toggle is ordered: the accent vocabulary (R5) owner; this row is the precondition's carrier."
  },
  {
    "id": "DSGN_REBRND-S8",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~D",
    "surfaced_at": "2026-10-03T00:25:00Z",
    "one_line": "DSGN_REBRND-S5 remedied on portal DEV b23917f7: the holdings table's band dash ink is white/70 (5.13:1 on the selected rung, 6.91 on the tile), pinned by iv-e-152, which reads the rungs from index.css and the inks from the table.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~D",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal b23917f7 (origin DEV, ls-remote read 00:2xZ): HoldingsBreakdownTable.tsx band dash 'text-white/70'",
        "iv-e-152: dash on tile 6.91, dash on selected 5.13, subtotal label on tile 10.29, ink on selected 8.50; CONTROL white/60 on selected fails; a planted mutant (white/60) fails arm (a)",
        "walk 20261003T001748Z (local, signed in, GET-only): /positioning's FIXED INCOME TOTAL row, the dash legible on the tile band"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarms DSGN_REBRND-S5: remedied (the dash clears 4.5:1 on every E4 rung) and pinned. The subtotal band's separation is the named-layer table's own tile step (1.22:1 lightness over the body) with its 2px rule; not changed.",
    "spec_asserts": "The design law: text on a dark panel meets 4.5:1; named layers separate visibly.",
    "world_is": "The dash reads 5.13:1 on the selected rung and 6.91 on the tile.",
    "notes": "S5 stays filed as it is (append-only); this row is its remedy record."
  },
  {
    "id": "DSGN_REBRND-S9",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-03T01:30:00Z",
    "one_line": "Row S7's census ('no code selects dark mode') covered html.dark-mode only: Tailwind 4's default `dark:` variant compiles to prefers-color-scheme (the portal declares no @custom-variant), and 132 `dark:` uses in 23 catalyst component files are reached by ExportModal, UserSettingsModal, SessionTimeoutWarning and RollbackConfirmDialog, so a viewer whose OS prefers dark gets those modals restyled on PROD with no toggle.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's grade 2026-10-03 00:xZ-01:xZ (portal origin/DEV b23917f7, on PROD 6169edd9): 'dark-mode' 8 hits in 3 files and 0 setters (S7's claim holds for that class); `dark:` 132 uses in 23 files under the catalyst components; no @custom-variant in the CSS entry, so the variant is media-query based"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row S7: no code selects dark mode, so the dark styling is latent.",
    "world_is": "A second dark path exists and is selected by the viewer's operating system, not by code. Not rendered by this seat: whether the dark-styled modals stay legible on the portal's grounds.",
    "notes": "INERT until rendered. Owner 2.0.0_SA_COO~D: either declare `@custom-variant dark (&:where(.dark-mode, .dark-mode *))` so the variant follows the app's own switch, or render the four modals under prefers-color-scheme: dark and grade them."
  },
  {
    "id": "DSGN_REBRND-S10",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-03T01:30:00Z",
    "one_line": "The Positioning Summary's percentage labels (PositioningSummary.tsx:1183 text-xl font-semibold, 20px/600, colour at :1211, Equity blue500 #3b82f6) compute to 4.07:1 on the body rung, below the 4.5:1 text floor (20px at 600 is not WCAG large text); the walk that disarmed W2-S8 measures interactive controls only and cannot see them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's arithmetic on index.css rung values and #3b82f6 (WCAG relative luminance), 2026-10-03 00:xZ-01:xZ; the label is visible in the walk's shot 004 ('98.07%')",
        "walk.mjs:620-661 (tmp/ui-walk/20261003T000242Z): getComputedStyle on interactive controls only, capped at 80 per view; 316 pairs, all >= 4.5, none of them these labels"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The design law: text on a dark panel meets 4.5:1.",
    "world_is": "A served label sits at 4.07:1; the instrument used to clear the page does not measure non-interactive text, so its 0-under result does not cover these.",
    "notes": "INERT (legibility, on PROD 6169edd9). Owner 2.0.0_SA_COO~D: a lighter Equity ink for text on the body rung, or 24px; and widen the walk's contrast limb to non-interactive text."
  },
  {
    "id": "DSGN_REBRND-S11",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~D",
    "surfaced_at": "2026-10-03T07:10:00Z",
    "one_line": "Round 3 E3 wires the NO-PERMISSION state at the route level: a signed-in viewer whose firm reaches a page but whose role does not (requireAdmin, requireInternal, requireDev) now sees PanelNoPermission and a way back instead of a silent bounce to /market.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~D",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal d7141e5a (origin DEV, ls-remote read) components/ProtectedRoute.tsx: RouteNoPermission rendered for the three role gates; the firm allowlist checked first and still a redirect",
        "portal src/components/__tests__/route-no-permission.test.tsx at d7141e5a: five arms from the working-tree ProtectedRoute under the real AuthContext provider (panel for each role denial; page for full roles; redirect for a firm outside its allowlist and for a signed-out viewer)",
        "real run 2026-10-03T07:0xZ on localhost:5174, a stubbed signed-in non-admin internal user on /investor-reporting: 'You do not have access to this page. An Opal Capital administrator can grant it. Go to Market Overview', inside the app shell; the link leads to /market"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarms DSGN_REBRND-W3-S1: an observable NO-PERMISSION state now renders on every route whose role gate denies a viewer, in the four-states component (DESIGN.md C12.4), with a fixture-free render and a pin. Not covered, by design: a partner firm outside its own allowlist is still redirected to its landing (parked in STATUS E3).",
    "spec_asserts": "Row W3-S1: RB-s-10's face lists NO-PERMISSION among the four designed states every panel with nothing to show uses.",
    "world_is": "The route-level denials render that state on DEV d7141e5a. Panel-level hides (an element not drawn for a role) remain non-rendering; none was found that leaves a panel empty.",
    "notes": "Panel-level census of hides not repeated here; W3-S4 (failure swallowed as EMPTY) stays with E3."
  },
  {
    "id": "DSGN_REBRND-S12",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~D",
    "surfaced_at": "2026-10-03T09:12:00Z",
    "one_line": "Round 3 row S10's remedy, both halves: the Positioning Summary's class percentage labels take a text ink that clears 4.5:1 on the body rung (Equity blue400, Structured pink400), and the walk's --contrast-table now also grades non-interactive text at rest.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~D",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal d8d236a0 (origin DEV, ls-remote read 09:11Z): lib/chartColors.ts getAssetClassInkOnDark (blue500 4.069 -> blue400 5.886; pink500 4.242 -> pink400 5.650; green500 5.899, yellow500 7.803, vermilion500 4.553 unchanged) and the four label sites in Positioning/panels/PositioningSummary.tsx",
        "portal src/pages/Positioning/panels/class-label-ink.test.ts at d8d236a0: three arms, with a CONTROL that the raw Equity colour reads 4.069:1 on --layer-body read from index.css",
        "walk tmp/ui-walk/20261003T090209Z (signed in, localhost:5174, the widened .claude/skills/ui-walk/walk.mjs): span[data-class-label] rgb(96,165,250) 5.90:1 x4, rgb(244,114,182) 5.67:1 x3, rgb(16,185,129) 5.91:1 x5, all on rgb(25,38,67); the screenshot was looked at"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarms DSGN_REBRND-S10: every class percentage label on the Positioning Summary clears 4.5:1 on its ground in the served code, and the instrument that missed them now measures non-interactive text.",
    "spec_asserts": "Row S10: text on a dark panel meets 4.5:1; the walk's contrast limb sees non-interactive text.",
    "world_is": "Both hold on DEV d8d236a0. The widened limb reads 35 non-interactive text groups on /positioning at load, 4 of them under their bar; they are listed in STATUS.md as round 3's next contrast item, not ruled here.",
    "notes": "The bars, swatches and legend keep the class colour; only text drawn in a class colour on the dark rung changes ink."
  },
  {
    "id": "DSGN_REBRND-S13",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-03T10:34:00Z",
    "one_line": "d7141e5a (E3 / row W3-S1, the designed NO-PERMISSION state) breaks F49-AC4: 32 of 32 pass at its parent and 31 of 32 from this commit on. The test reads COMMITTED blobs and classes the new panel as rendering NOTHING, though the viewer is still refused. The commit's '32 of 32' was measured before commit, against the old file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's portal grade 2026-10-03 ~08:5xZ-10:3xZ (scratch worktree of origin/DEV, removed after): F49-AC4 at d7141e5a^ 32/32, at d7141e5a and at 46aeea17 31/32; ProtectedRoute.tsx:121",
        "fe-s-49 and fe-s-47 (AC6, AC7) read committed blobs: a full-suite revert of the working tree cannot see them, and a pre-commit 'N of N' for them is not a measurement of the change"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A FAST pin adds no failing test; its 'N of N' is measured on the bytes it lands.",
    "world_is": "One test now fails on DEV because of this pin, and its own record says the opposite. CI runs no unit tests, so nothing else caught it.",
    "notes": "INERT (DEV only; a test's class of the panel, not a served defect: the viewer is still refused). Owner 2.0.0_SA_COO~D: teach F49-AC4 the NO-PERMISSION panel as a refusal, and re-measure committed-blob tests after the commit."
  },
  {
    "id": "DSGN_REBRND-S14",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~D",
    "surfaced_at": "2026-10-03T14:52:00Z",
    "one_line": "Every route row W3-S4 named now renders ERROR on a failed fetch (and LOADING while pending) instead of data, EMPTY or a stand-in reading: /market, /positioning, /advisor-intelligence, /attribution, /portfolio-management, /ticket-center and /data-refresh, each re-measured on DEV before its fix.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~D",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal origin DEV (each ls-remote read at its push): /market 55560835 (Global RSI and Fear & Greed; the Fear & Greed endpoint stopped returning a made-up 50 'neutral'), a7b16628 (Daily Cloud, Trending Topics, Top/Bottom Performers; the keyword endpoint stopped returning an empty list), 564a8f95 and 1754d9c1 (RSI hook: an incomplete summary and a missing period change), 4a40a0ff (RSI modal); /positioning b0b3c524; /attribution 94c055e8; /portfolio-management c3e1d7b9; /ticket-center 3d8cce99; /data-refresh 30f7fca1 (History and Emergency Rollback); /advisor-intelligence 075d33fa (Advisors), 10fca02d (Data Source 'Connected' claim), 1b8fccfd (Assets Overview)",
        "pins at those commits: components/market-performance/__tests__/market-failed-fetch.test.tsx (arms a-f), Positioning/panels/summary-states.test.tsx, Attribution/components/style-policy-states.test.tsx, PortfolioManagement/components/summary-states.test.tsx; each with a negative control on the commit before",
        "real runs on localhost:5174: scripts/ui-smoke.mjs with the session stubbed (data answered 401) or --fail 503 per route, before and after, looked at; signed-in walks as positive controls with live data (20261003T120014Z, 124023Z, 130059Z, 131333Z, 133002Z, 134302Z, 144759Z)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarms DSGN_REBRND-W3-S4: on every route the row named, a failed fetch now renders the designed ERROR state (DESIGN.md C12), with no fabricated reading and no EMPTY sentence standing for a failure. Effect-driven branches with no static pin (HoldingsTab, SelectionTab, TicketCenter, DataRefresh, AdvisorsTab, PartnerAnalytics) were checked by the 401 render alone.",
    "spec_asserts": "Row W3-S4 / RB10-AC5: a failed fetch renders ERROR; a neutral reading and a failed fetch must be distinguishable.",
    "world_is": "Holds on DEV 1b8fccfd for the named routes. Not swept: routes the row did not name. Not yet re-measured after commit: the repo's committed-blob suites (row S13's lesson); this seat runs them next.",
    "notes": "PartnerAnalytics.tsx was released from 2.0.0_SA_COO~M's MDPF_SECCLASS lease for 1b8fccfd (msgs 104617, 104623)."
  },
  {
    "id": "DSGN_REBRND-S15",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~D",
    "surfaced_at": "2026-10-03T15:10:00Z",
    "one_line": "Row S13's two asks done: FE-s-49 F49-AC4 reads the designed NO-PERMISSION panel as a refusal (portal e2563c17), and the committed-blob suites were re-measured after commit across this seat's pins, which found a second break of the same class this seat made: FE-s-47 F47-AC6, two unclassified PrintEntry.tsx sites from b618efc9, now classified and measured (2da1eaaf).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~D",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal e2563c17 (origin DEV, ls-remote 15:00Z): admin-gate.test.ts gains outcome NO_PERMISSION (`data-slot=\"route-no-permission\"`), counted with REDIRECT in F49-AC3 and F49-AC4; fe-s-49 10 pass 0 fail at HEAD and again after the commit; F49-AC4 refuses 10 of 10",
        "portal 2da1eaaf (origin DEV, ls-remote 15:09Z): no-status-reason.test.ts classifies PrintEntry.tsx:83 (import) and :162 (analysisChromeFromStatus's seed, OVERWRITTEN) and measures the overwrite as OVERWRITE (3); census breaks 0; 9 of 9 reaches carry their reason",
        "the seven committed-blob suites (fe-s-33, fe-s-41, fe-s-47, fe-s-49, fe-s-54, iv-e-8, iv-e-10) at 2da1eaaf after commit: 45 pass, 0 fail (before e2563c17: F49-AC4 and F47-AC6 failing)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarms DSGN_REBRND-S13: F49-AC4 passes on DEV with the NO-PERMISSION panel counted as a refusal, and this seat's committed-blob suites are measured on the bytes that landed. The F47-AC6 break (b618efc9) had been filed as pre-existing by this seat's earlier baseline comparison; it was its own, and is fixed in the same pass.",
    "spec_asserts": "Row S13: a FAST pin adds no failing test, and its N of N is measured on the bytes it lands.",
    "world_is": "Holds at portal DEV 2da1eaaf for the seven suites that read committed blobs. The full repository suite was not run.",
    "notes": "Committed-blob suites found by searching test files for portalBlob( / git show / execFileSync('git'); fe-s-47 was added on the CVO's naming."
  },
  {
    "id": "DSGN_REBRND-S16",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-04T20:35:00Z",
    "one_line": "7b053135 (R4-1) claims to replace 'the last two bare spinners'; at portal DEV 7b053135, LoadingInline remains at AdvisorBookView.tsx:897, ClientsTab.tsx:636,645,668,765, ModelPortfolios.tsx:1340,1361,1671,2368, PeersTab.tsx:347, SentimentGauge.tsx:131,195, KeywordSentimentModal.tsx:183, AssetAllocationSummary.tsx:66,69 and MacroTimeSeriesModal.tsx:438, and a panel-sized animate-spin at IndexPerformanceModal.tsx:301, LoadingOverlay.tsx:11, VersionHistoryModal.tsx:94, PrintExportAction.tsx:154, PipelineProgress.tsx:327 and the DataRefresh HistoryTab/EmergencyRollbackTab; the pin's census bans only the named components, so an animate-spin div beside PanelLoading passes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's portal grade 2026-10-04 ~19:4xZ-20:4xZ (scratch worktree of origin/DEV 7b053135, removed after): source census of the files above, all imported by live code; pin r4-1-remaining-spinners 3/3, NEG fails, MUT (an animate-spin div beside PanelLoading) passes"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FWD-11 (one designed state per kind) and the R4-1 claim: no bare spinner remains where a panel loads.",
    "world_is": "The two named sites are fixed; about 20 panel-sized bare spinners remain, so FWD-11's loading clause is not met by this pin.",
    "notes": "INERT (presentation). Owner 2.0.0_SA_COO~D: widen the census to animate-spin and LoadingInline at panel size, with the list above as its baseline, and retire the sites or name the exceptions."
  }
]
```

## DSGN_REBRND-S17 -- /correlations page end reads an as-of field the served JSON lacks

```json
{
  "id": "DSGN_REBRND-S17",
  "project": "DSGN_REBRND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-04T22:21:00Z",
  "one_line": "97b7a6f2 (R4-2 batch 1) ends /correlations on PageEnd with dataAsOf={data.metadata?.as_of_date} (Correlation.tsx); the served s3://opal-data-portal-v2/json/correlations/correlation_data.json (version obQwHWjT.., written 2026-10-03 11:05Z) has metadata keys generated_at, periods_available, ticker_count and its as-of at top-level data_as_of (2026-10-02), so the page end prints no date on served data; the matrix's own asOfDate reads the same missing field (pre-existing). The batch-1 pin's fixture supplies a field production does not serve.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "this seat's boto3 get_object of the served correlation_data.json 2026-10-04 ~22:2xZ: top keys correlations, data_as_of, metadata, tickers; metadata has no as_of_date",
      "git -C portal show 97b7a6f2:src/pages/Correlation/Correlation.tsx (PageEnd dataAsOf and matrix asOfDate read data.metadata.as_of_date); correlation-states.test.tsx fixture uses data_as_of"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-10: every page ends on the shared page end naming its own as-of.",
  "world_is": "/correlations ends on the page end with no as-of on served data; the pin passes on a fixture shape production does not serve.",
  "notes": "INERT (DEV only; not on PROD c69b4747). Owner 2.0.0_SA_COO~D: read data_as_of (and fix the matrix asOfDate), and give the pin a fixture copied from the served object's shape."
}
```

## DSGN_REBRND-S18 -- /market fallback tier reads a field its six-month-old artifact lacks

```json
{
  "id": "DSGN_REBRND-S18",
  "project": "DSGN_REBRND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-04T22:49:00Z",
  "one_line": "/market's SECONDARY tier is dead: market.ts:246 calls portalProxy.getAllMarketData(), which returns response.data (portal-proxy.ts:159-161), but the served s3://opal-data-portal-v2/json/market/all_returns.json has keys as_of_date, cache_until, count, data_as_of, generated_at, tickers and no data, so marketData is undefined and the fallback throws; the file was last written 2026-04-15T20:19:39Z although the doc comment says it updates twice daily.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "this seat's boto3 get_object of json/market/all_returns.json 2026-10-04 ~22:5xZ: LastModified 2026-04-15T20:19:39Z; top keys as listed, no data key",
      "git -C portal show 1b9f553d:src/api/portal-proxy.ts:147-161 and src/api/endpoints/market.ts:241-265"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "portal-proxy.ts's own comment: the secondary artifact is updated 6am and 2pm UTC daily by opal-precompute-market-metrics, and the fallback serves it when the tiered summary fails.",
  "world_is": "The fallback reads a field the artifact does not carry and the artifact is about six months old; if the primary tier fails, /market gets no fallback data (the throw is inferred from the code, not run).",
  "notes": "INERT (the primary tier serves 2026-10-02; pre-existing, not from 57ac37d6). Owner 2.0.0_SA_COO~D: read tickers (or retire the tier), and say whether opal-precompute-market-metrics still runs; the DEGRADED warn was added under OPAL_ANALYST.EXP1 change D."
}
```
