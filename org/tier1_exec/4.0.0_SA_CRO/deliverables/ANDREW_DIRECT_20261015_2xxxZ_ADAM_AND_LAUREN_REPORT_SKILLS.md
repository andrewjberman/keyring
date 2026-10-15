# ANDREW-DIRECT 2026-10-15 ~20:5xZ-21:1xZ -- /adam-report and /lauren-report skills; the IRPT YCharts brief (parked)

**Channel:** Andrew at the terminal of `4.0.0_SA_CRO~DELL1` (dell1). **Recorded by:** `4.0.0_SA_CRO~DELL1`, same turn.
Quoted verbatim, in order; the phrasing is the ruling.

1. ~20:5xZ:
   > What I want you to do now is read my teams conversation with Adam Muller, specifically about the document he
   > sent: C:\Users\Test\Downloads\T-Mobile_US_Investment_Memo_2026_10_13.docx. I want to be able to write a skill
   > that generates this information, and uses the relevant data sources from opal-data-harvest via the opalgateway
   > mcp. The tools necessary should be right there so it should be super fast. In the skill it should qualify that
   > if the opalgateway or the necessary information in the opal-data-harvest is not available, that it should
   > default to web search, with a focus on reputable sources like SEC EDGAR and so on.

2. ~21:0xZ (on this seat's finding that the gateway's YCharts tools returned 404/403 for a single stock):
   > YCharts absolutely does serve single stocks we may just not have the functionality for that wired in to the
   > opalgateway. That is worth an investigation separately via looking at the IRPT_BCKEND ops, because there are 4
   > endpoints YCharts surfaces, one specifically which does pricing, which we can use. The only thing is that
   > usually yahoofinance is more effective/faster for this kind of thing, but still worth an investigation for the
   > MCP, the brief covering all of this which should be taildropped over to the sitez MSTR with instruction that
   > the IRPT ycharts endpoints should be included into the opalgateway and properly tagged.

3. ~21:0xZ:
   > but dont get distracted with putting that brief together just yet, focus on the skill/opal-data-harvest layout
   > for Adam as it pertains to that document creationm

4. ~21:1xZ:
   > We also aregoing to want to do the exact same process with Lauren after you finish Adam, I recommemnd checking
   > our teams chat as well for her ASML report. we can make a /adam-report and /lauren-report skills with their
   > assocaited formats

## Disposition at this write

- (1) and (4): `/adam-report` built at `.claude/skills/adam-report/` (this commit); `/lauren-report` is next, from
  the Lauren Harmon Teams thread (ASML and UNH 3Q26 earnings updates).
- (2): PARKED by (3). Owner `4.0.0_SA_CRO~DELL1`. Un-parks when `/lauren-report` lands: a brief on wiring the
  IRPT_BCKEND YCharts endpoints (pricing among the four) into the opalgateway, properly tagged, with yfinance as the
  comparison, sent to the sitez MSTR by `/tdrop` (nothing that travels by /tdrop is committed).
- Context from the Adam Muller Teams thread (Adam, 2026-10-15 20:31Z, not Andrew): "having it write to work and link
  to the folder is most important" -- the skill writes a Word .docx into the user's linked folder.
