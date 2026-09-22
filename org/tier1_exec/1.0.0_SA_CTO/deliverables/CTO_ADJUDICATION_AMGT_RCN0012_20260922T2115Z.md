# CTO ADJUDICATION -- RCN-0012's four open calls (Claude for Financial Services), 2026-09-22 ~21:1xZ

**Authority:** Andrew-direct ~21:0xZ, VERBATIM *"you have adjudication ability for any and all open calls you
encounter for the duration of this session as it pertains to AMGT projects"* (@`c5f33fe8a3`).

**State re-read at write time, not assumed:** `org/tier1_exec/4.0.0_SA_CRO/RECON_REGISTER.md` still carries
RCN-0012 as *"DELIVERED as CTO intake -- PROPOSAL ONLY, nothing dispatched ... **4 open calls at Andrew**."* They
are open, they pertain to AMGT_RESAPP's analysis layer, and they are ruled here.

Source of the calls and the RECs: `org/tier1_exec/4.0.0_SA_CRO/briefs/CLAUDE_FSI_PLUGIN_STRUCTURE_AND_DATA_SHAPES_BRIEF_20260922.md`
and `RESAPP_CLAUDE_FSI_THREADING_PROPOSAL_20260922.md` §5, `4.0.0_SA_CRO~F`.

---

```
+-- CALL 1 of 4 -- a vendor data subscription -------------------------+
  **Buy a market-data subscription (S&P kfinance or Daloopa) to close
    the consensus / estimate-revision / transcript surfaces?**
  ----------------------------------------------------------------------
  **REC (CRO) --** None until S1 shows Bloomberg `bestdata` cannot give
  revisions; then Daloopa first (API-key path, published record shape,
  per-figure filing citations) over S&P (OAuth-only).
  ----------------------------------------------------------------------
  **RULING --** NO SUBSCRIPTION AT THIS TIME. Adopted, on a ground that
  got STRONGER tonight: S1 is now MEASURABLE and has not been measured.
+----------------------------------------------------------------------+
```

**Why this is safely mine to rule:** a NO costs nothing and commits nothing. ⛔ **A YES would be SPEND, and spend
returns to Andrew** -- tonight's word gives adjudication over calls, and I do not read it as a purchasing
authority. If S1 comes back showing Bloomberg cannot give us the revision series, **the subscription question goes
back to him as a fresh card with the measurement attached**, which is a far better card than today's.

⭐ **The ground improved hours ago and nobody has noticed yet.** S1 asks whether `bestdata` bronze carries BEst
means and counts, and whether a SECOND pull differs -- i.e. whether a revision series is derivable from vintages we
already pay for. Until tonight Lenovo had **zero** `bestdata` bronze. `rk-116` landed at `20:12Z` and it now has
**its first ever forecast bronze** (15 `BEST_*` figures: EPS, SALES, EBITDA, DPS, PE_RATIO). **So the first half of
S1 is answerable today on a real object, and the second half becomes answerable on the next pull for the same
name.** Buying a vendor before running that read would be buying blind against data the firm already holds.

**Carried as a measurement item, owner `2.0.0_SA_COO~Z`'s harvest cells:** read the landed `bestdata` object for
the BEst means/counts, and diff the next vintage for the same name. Not a cell tonight; round 30 is frozen.

---

```
+-- CALL 2 of 4 -- installing the FSI plugin on this box --------------+
  **Install Anthropic's financial-services plugin on this machine?**
  ----------------------------------------------------------------------
  **REC (CRO) --** NO on the shared Windows user (every seat's sessions
  would get twelve vendor OAuth prompts); YES on an analyst's own
  machine or in Cowork, which is where it earns its keep.
  ----------------------------------------------------------------------
  **RULING --** NO on this box, ADOPTED. The "yes elsewhere" half is
  NOT RULED, because it is not this estate's to rule.
+----------------------------------------------------------------------+
```

**NO on this box.** The plugin is **files, not access** -- its twelve MCP servers are OAuth-gated vendor endpoints
we hold no entitlement to. Installing buys nothing we can use and imposes twelve auth prompts on **every seat
sharing this Windows user**, including headless spawns that cannot answer a prompt and would hang. ⚠ **A hanging
OAuth prompt in a headless agent session is indistinguishable from a dead seat**, which this estate has already
paid to learn on other surfaces.

**And it is unnecessary for what we actually want:** the brief's own finding is that we take the skills' METHODS --
section structure, the beat-or-miss method, the disclosure rules, the `[UNSOURCED]` marking -- and those are
readable from the repo at `@574ed36` (Apache-2.0) **without installing anything.** `AMGT_CORPUS` manifest row R12
already holds the lifted artifact as its home.

⚠ **The second half is deliberately NOT ruled.** An analyst's own laptop is not infrastructure this seat governs,
and Cowork is a product decision. **Available, not authorised by me** -- if someone wants it there, that is theirs
or Andrew's, and nothing here blocks it.

---

```
+-- CALL 3 of 4 -- the print target for a quarter ---------------------+
  **Is the LLY-style earnings update a SECOND print template, or a
    REPLACEMENT for Adam's one-pager?**
  ----------------------------------------------------------------------
  **REC (CRO) --** Second template, same renderer, same numbers.
  ----------------------------------------------------------------------
  **RULING --** SECOND TEMPLATE. Adopted, and a replacement is refused
  on never-widen grounds rather than taste.
+----------------------------------------------------------------------+
```

⛔ **A replacement is not a design choice; it is a move of served output with a real user at the end of it.** Adam's
one-pager is the ratified `FWD-5` artifact. Replacing it would need a never-widen pair, and **nothing about a
richer template justifies taking away the artifact a person currently receives.** A second template is purely
additive: nobody loses a thing, and the two can be compared in use rather than in argument.

**Two bindings that come with the ruling:**
1. **The numbers come from the served page object, never re-fetched** -- the export renders what the page already
   shows, so a printed figure and a screen figure cannot disagree.
2. **The brand law applies** (`deck_generation/DESIGN_BIBLE.md`), per Andrew's *"Opal Brand
   Colors/Guidelines/logos"* word.

**What I am NOT ruling:** which template a given reader should get for a given quarter. That is Adam's and Andrew's,
and it is a conversation, not a gate -- **the architecture above works whichever way that lands**, which is exactly
why the architecture can be decided now.

---

```
+-- CALL 4 of 4 -- the egress class of a web-searching skill run ------+
  **What egress class is a skill run that web-searches, and may it be
    a scheduled producer?**
  ----------------------------------------------------------------------
  **REC (CRO) --** Class W egress through Anthropic's tools, not Bright
  Data; keep it an interactive-analyst act, never a scheduled producer.
  ----------------------------------------------------------------------
  **RULING --** CLASS W, and NEVER A SCHEDULED PRODUCER -- adopted, on
  a CONTRACT ground that does not depend on tonight's egress word at
  all.
+----------------------------------------------------------------------+
```

⛔ **This is the one call tonight's egress grant could most easily be misread as answering, so it is ruled
explicitly.** Andrew's word permits egress this session; **it does not convert a web-searching model call into a
pipeline component.** The bar is a CONTRACT, not a permission:

**`C-BRONZE-AS-RECEIVED` cannot be satisfied by a model's web search.** There is no as-received object -- only
`mcp_tool_result` blocks inside a conversation. A producer that cannot land the bytes it read cannot be a producer
in this estate, whoever authorises its egress. **That is the same ground the brief used to refuse vendor MCP
connectors as a pipeline shape (option B), and it applies identically here.**

Beside it and independently: the standing **ad-hoc-runs-are-QA-only** rule and the **shadow-pipeline veto**.

**So: an analyst may run it interactively. Nothing scheduled, nothing in a producer chain, and nothing it returns
is bronze.**

---

## WHAT THIS ADJUDICATION DOES NOT DO

It commits no money, installs nothing, cuts no cell, mints no outcome, and moves no served artifact. **Two of the
four rulings are NOs that preserve the status quo, one is additive, and one is a contract restatement.** The single
branch that would have needed Andrew -- buying a subscription -- is the branch I declined to take, and it returns
to him with a measurement if S1 ever points that way.

**RCN-0012's queue at Andrew is now EMPTY.**

## ACTS

- This record, committed; broadcast the same turn to `4.0.0_SA_CRO~G`, `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z` and
  `0.0.0_AB_MSTR~Z`.
- The S1 measurement is carried with its owner named; it is not a cell tonight (round 30 is frozen).
- `4.0.0_SA_CRO`'s RECON_REGISTER row is the CRO's to update; I do not edit another seat's register.

-- `1.0.0_SA_CTO~Z`
