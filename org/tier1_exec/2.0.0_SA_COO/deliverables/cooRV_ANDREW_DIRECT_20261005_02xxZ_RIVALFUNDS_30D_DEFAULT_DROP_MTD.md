# ANDREW-DIRECT 2026-10-05 ~02:4xZ (22:4x ET 10-04) -- /rivalfunds period model: 30 trading days default, divider, QTD and YTD; no MTD

**Channel:** Andrew at the `2.0.0_SA_COO~RV` terminal (site Z), in session.

**Verbatim:**
> I want you to look at this statement on the /rivalfunds page "Year to date (2026), 2026-08-21 to 2026-10-01. 45 ranked" for
> IDVZ. You see of course why this is confusing. It seems like it is intended as a 30 day trading history, but it says YTD on
> it. Do we not have full history for IDVZ back to Jan 1 2026? Same for PFOE. I think there should be a clear bifurcation of
> 30d as the default selection, and then there is a divider where the user can select QTD or YTD for more clarity. If we are
> centering around 30 rolling days as the default, there is no need for MTD. We neeed to be practical and think about how this
> should be articulated in the frontend design of the Rivals page. Pitch me some ideas.

**What it changes (read by this seat, not adjudicated wider):** PRD v0.14 (@4cc8e40575) FWD-13/14/15/19 name the switch as
"the last 30 trading days first and selected by default, a dividing line, then month, quarter, year". This word removes
MONTH TO DATE from the switch: 30 trading days (default) | QTD | YTD. Round-8 workstream B (rn-1, built, not merged) renders
MTD and needs an amendment before the merge. The PRD text change is `1.0.0_SA_CTO`'s.

**Also asked:** whether IDVZ and PFOE have history back to 2026-01-01 (measured answer: no -- first reports 2026-08-21 and
2026-08-24, home-producer files only; WORKSTREAM_B_INPUTS.md @7cc969288b), and design ideas (pitched in session).

Recorded by `2.0.0_SA_COO~RV`.
