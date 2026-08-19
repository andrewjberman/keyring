# CVO VERDICT — D8 package (Philosophy + Benchmark Modal Live-Edit)

**Reviewer:** `3.0.0_SA_CVO` · **Date:** 2026-08-19 · **archetype:** VALIDATE
**Package scored, vintage-pinned:**
- `docs/architecture/D8_LIVE_EDIT_MODALS_PRD.md` @8d662d5f1f (163 lines, v0.1)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/D8_ATOMDECOMP/run_20260819.md` @8d662d5f1f (58 lines)

**Verdict: ACCEPT — 0 P0, 1 P1, 1 P2.** Careful package. Four practices worth naming:

- **B4 records a TOOL FAILING and substitutes a sound method, openly.** `comp-transform schema-check
  ModelPortfolioModal` returned *"Component not found"* (components/ dir not indexed); the contract was
  grounded by direct source read and **the limitation is written into both run and §5.2.** That is the
  instrument-blind-spot discipline applied to our own tooling.
- **§5.2 carries a NOT-RUN row.** `comp-routes trace` is recorded as *"NOT RUN this pass"* with the
  reason (route placement depends on the §6 Lambda selection) and the requirement moved into the AE
  TO's Phase 1. **A tool not run, said so, and converted into an obligation — rather than a silent gap.**
- **The supersession is handled at the source, not just in the PRD.** §1 names the 08-12 in-file ceiling
  and the DE leg **updates the comment block** *"so the next reader does not obey the stale ceiling."*
  That is the law-edit delivery problem solved locally.
- **The two-call-site propagation is stated pre-emptively** (§2, run B1/B3) — *"by design, stated here
  so nobody reads it as a leak."* An edit on the Benchmark heatmap also changes Positioning bars.

**Explicitly not a finding:** run D2's absence claim (*no existing table is a natural home*) is scoped
to its census, marked INFERRED, and TO-A Phase 1 binds the re-verify. CTO banked this at 185240Z; it is
conforming and I did not re-derive it.

---

## P1-1 — For CTO + Andrew. §7 Q3 presents only ONE of the two silent-failure directions, and the unstated one lands on named people.

§3 proposes precedence: `store override (DDB) > existing JSON block (pillars only) > repo baseline`.
§7 Q3 asks Andrew to confirm and states the downside of the *alternative*: *"workbook-wins … would make
portal edits silently revertable on the next workbook upload — not recommended, but **Yang/Manav
currently use the workbook path**."*

**The recommended option has the mirror-image failure and it is not stated.** If store-override wins,
then for any pillar field carrying an override, a Yang/Manav edit to the CMA workbook's Philosophy
sheet — re-uploaded through Data Refresh, regenerating `assumptions.json` exactly as run A2 describes —
**produces no visible change.** The workbook edit lands, the JSON regenerates, the portal keeps showing
the override. No error, no notice, and the person most likely to hit it is the person the PRD names as
the current user of that path.

**So Andrew is being asked to choose between two silent-failure modes while shown only one.** That is
the substantive defect: not the recommendation (store-wins is probably right — it is the surface the
edit was made on), but that the question as posed cannot be answered with both costs visible.

**Recommend:** state both directions in §7 Q3, and — whichever is ruled — **the losing path must not
fail silently.** Cheapest sufficient form, no new machinery and moratorium-clean: the store already
records `updated_by`/`updated_at`, so an overridden field can be marked as overridden where the
workbook path is operated (or the override list is simply readable), letting a workbook editor see that
their field is shadowed. **A record with a reader** — the same convention I asked you to rule on family-wide.

---

## P2-1 — For CTO. §2's cited write-API precedent is an API that authenticates but does not authorize — and D6 now points at D8 as the auth-doctrine reference.

§2 lists the **"Write-API precedent: opal-ticket-api + opal-data-refresh-api are live authenticated
portal write paths (run D1)."**

**D7's run R6 records that opal-ticket-api *"STAMPS caller identity, never CHECKS it: no
per-caller/per-firm authorization on six /api/scoped/ routes"*** — a finding standing at Andrew since
08-12. So the exemplar cited for *"authenticated write path"* is precisely the one where
authentication is not authorization.

**D8's own design does NOT inherit the defect, and I want that on the record:** §3 requires *"PUT
verifies the Opal-employee claim SERVER-SIDE from the JWT (client predicate is advisory)"*, run C3
marks the requirement INFERRED-as-requirement rather than as an existing mechanism, and TO-A Phase 3
requires an exercised **403 negative with a non-employee token**. The controls are right.

**The risk is a reader, not the design** — and it is now amplified: **D6's addendum states *"Same auth
doctrine as D8's server-side claim check"***, making D8 the family's auth reference. A reference
standard whose own §2 cites a non-conforming exemplar is a trap for a fast-moving implementer who reads
*"precedent: opal-ticket-api"* and copies the pattern rather than the requirement.

**Recommend:** one clause on the §2 precedent line — cite the two APIs as precedent for the *shape*
(authenticated portal write path) and note that opal-ticket-api's authorization gap is a standing
finding, **so the pattern to copy is D8 §3's server-side check, not the ticket-API's**. One sentence;
it protects the reference D6 now leans on.

---

## Explicit deferrals

- **Run D2 absence claim** — banked by CTO, scoped to its census, re-verify bound into TO-A. Conforming.
- **Last-write-wins on conflict** (§4.1) — a stated, reasoned acceptance for v1 with `prev_bodies`
  (last 5) as the audit trail. Proportionate to prose edits by a small editor set. **No finding.**
- **Figures stay ruled/untouchable** (run B2, Andrew-direct 08-11) — correctly scoped out; only prose is
  editable. Verified the six-field set is not in the edit surface.
- **Split verdict on run D1** (*"MEASURED (existence/shape); INFERRED at live plane this run"*) — the
  family vocabulary issue; covered by @36a7fbd70e. No expected-value derives from the INFERRED half.
- **DDB as application state, not pipeline data** (§3) — correctly reasoned: the medallion/platinum law
  governs pipeline data, and the precedent class (opal-tickets, opal-users-v2) is right. **Rule 17b is
  not violated by this store**, and the PRD says why rather than assuming it.

---

## What you should have asked but did not

**The store's primary key is a DISPLAY NAME — in the same week D1 is re-legislating display names, and
on a page that has already survived exactly this kind of rename.**

§3 specifies `opal-portal-content` with PK `surface_id`, and gives the shapes:
`philosophy_pillar#long-term-perspective` and **`model_key_notes#Ultra-Short Term`**. Run B2 confirms
the source: `modelPortfolioNotes.ts` is *"keyed by canonical model name."*

**So a persistent, human-authored content store is keyed on a name that other work in flight can
change.** Three things converge:

1. **D1 is building the category registry** whose entries carry `display_name` and `view_path`, with
   the Models tree split Primary/Custom — display naming is actively in motion this week.
2. **D4 adds four ETFs to that same registry**, and D1 §7 Q1 is still open on how they are named.
3. **This exact page already lived through a rename**: run A1 records route `/philosophy` against page
   dir `CapitalMarketAssumptions/` — the `/cma` → `/philosophy` rename (OPAL_INVPHL, 2026-08-11), where
   the artifact kept its identity while the name moved. **Eight days ago, on this surface.**

**The failure is silent, and it is D1's fallback class again:** rename "Ultra-Short Term" and the
override key orphans, `usePortalContent()` finds nothing for the new name, the modal renders the repo
baseline, and **the page looks perfectly fine while a human's saved edit is gone.** No 404, no error —
the fallback is doing its job. The estate already carries this lesson in the guarded-set spelling law
(`account_units` vs `account-units`), where one leaf name spelled two ways made a census read the live
half as orphaned.

**Recommend, and it is far cheaper now than after content exists:** key the store on a **stable
identifier** that survives renames — the registry's member id once D1 lands it, or a minted slug — and
carry the display name as an attribute, not the key. If that is not possible in v1, then **declare the
rename procedure** (a rename migrates its override keys) as an explicit obligation on D1's registry
work, so the coupling is owned rather than discovered. **Worth settling before TO-A writes the table,
because the PK is the one thing a DDB table cannot change later.**

— 3.0.0_SA_CVO
