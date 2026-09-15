# ANDREW-DIRECT 2026-09-15 ~05:5xZ -- a voice memo, delivered as a file at the `1.0.0_SA_CTO~W` terminal

**Channel:** Andrew's recording `New Recording 34_9677.json` (Whisper-style transcript: `text`, 22 `segments`,
`language: en`, 15,410 bytes, file mtime 2026-09-15 01:53 local), handed to this seat by path at ~05:5xZ after
his word *"I also have a transcript coming in your way to further enrich, once you have that done i thnk youll
be in a good position."* The JSON is copied beside this record, byte for byte, as
`ANDREW_DIRECT_20260915_055xZ_TRANSCRIPT_New_Recording_34_9677.json`.
**Recorded by:** `1.0.0_SA_CTO~W`, same turn. **Project:** AMGT_RESAPP (D5). **Round at the time:** 10 at
L8/L9 (`3.0.0_SA_CVO~W` adjudicating). **Class:** L2/L4 DIRECTION for the page's five surfaces, given to the
L4 owner directly; the sixth of tonight's records on this subject.

## VERBATIM, WITH THE RECORDING'S OWN TIMESTAMPS (seconds)

> [0.0-28.2] Yeah, so now I want to drill down a little bit more into some of these panels, because after
> looking at Adam's attachments, which I think are really important for you to review before we continue to
> enrich some of these concepts, I think it's really clear that in the thesis and risks, that is really
> something that I think is largely rich text.
> [28.2-58.1] I don't know if there's really any charts in there, there could be, I think it might be
> interesting to have one default chart in there that's basically when we identify what their thesis is,
> when we identify their biggest thing, which should be apparent based on all the information we're pulling,
> we need to find what chart is really the most important chart, I think that's kind of what goes, it's one
> of the components of thesis,
> [58.4-70.5] because we find like, well, what is the big thing? What is the big thing that they're living or
> dying on? What is the chart that kind of represents that? And that can vary, that's going to vary
> significantly from one company to another.
> [70.5-85.1] So we have to use probably the filings is where that's going to come from. But the way that we
> even know what filing to use and what chart really needs to be constructed is going to be based off of
> what we pick up for thesis and risks.
> [85.1-101.1] So let's lock that in as part one, thesis and risks. Part two, executive management. This is
> just rich text. This is really simple. This is pulling Lucia information, probably some kind of web search.
> Just see what comes up for the CEO.
> [101.1-115.8] CC, if there's, I don't know, maybe you have some ideas on how we can further enrich that. The
> peers, part three, this is, seems like it's just a bunch of comparables, comparable multiples.
> [115.8-127.6] Maybe we find the peers list via Seeking Alpha. If there's some endpoints with Seeking Alpha
> that kind of show comparable companies, that that could be a nice way to do that.
> [127.6-147.3] I would like it, if it was possible, to find comparable companies through some kind of ranking
> system where it's maybe we start from same sector, then same size, then same country, then same maybe
> subsector.
> [147.7-154.9] It's like we need to make some kind of, not an algorithm, but some kind of ranker that
> basically pulls the companies that are most similar.
> [154.9-163.8] We need to figure out, like, a similarity function to generate those peers from some database.
> That's something that we're going to need to figure out.
> [164.3-170.8] Financial model, that's basic. That is literally just generating a financial model from the
> information we pick up on Bloomberg.
> [171.0-174.3] There's nothing complicated about that. It's going to be basic, same way every time.
> [174.9-183.5] And then posture is really just taking the information from the four tabs and coming up to a
> conclusion.
> [183.5-193.8] I think that's what the RAG really is. The RAG is just the four tabs plus comparing with the
> opal position.
> [194.3-199.8] So it uses that same kind of similarity function that we built for peers.
> [200.1-209.9] We use that to kind of find where the attention is, what the most juxtaposed security is,
> [209.9-211.5] and then we kind of, like, make a recommendation.
> [212.4-220.4] And we, of course, are going to need to have the same thesis risks, exec management, peers,
> financial model for the opal comparison.
> [220.7-221.8] And that goes both ways.
> [221.8-241.0] Thank you so much. Thank you. Thank you.

(The transcriber wrote "Lucia" for Lusha and "CC" for what is heard as an address to this seat; both are
kept as transcribed and read as Lusha and as an ask for ideas.)

## READING -- NARROW, PER PART, AGAINST TONIGHT'S EARLIER WORDS

| part | his word, reduced | what it fixes for the design |
|---|---|---|
| 1 Thesis & risks | largely rich text; ONE default chart per company, the chart of "the big thing they're living or dying on"; which filing and which chart is chosen from what the thesis/risks extraction picks up | Thesis = prose over cited evidence (S9's drafting face) PLUS one derived chart whose subject is CHOSEN by the filings analyzer's output (a "thesis driver" field), rendered from the model block or the filing's own series; the chart varies by company and is never a fixed template |
| 2 Executive management | rich text; Lusha + a web search on the CEO; ideas for enrichment invited | the sixth word's whole C-suite + tenure stands; enrichment candidates are this seat's to propose, each measurable |
| 3 Peers | comparable multiples; peer LIST via Seeking Alpha endpoints if they show comparables; preferably a RANKER: same sector, then same size, then same country, then same subsector; "a similarity function to generate those peers from some database" | the peer-set rule is now SPECIFIED as a lexicographic similarity ranker over a database of classified, sized, located names; SA's comparables are a candidate INPUT to measure, not the rule |
| 4 Financial model | basic; generated from the Bloomberg information; the same way every time | the Model tab = Adam's Model sheet shape (measured tonight) served from the model block; no judgment in it |
| 5 Posture | takes the four tabs and comes to a conclusion; "the RAG is just the four tabs plus comparing with the opal position"; uses the SAME similarity function as Peers to find "the most juxtaposed security"; then a recommendation; the Opal comparable needs the same four tabs; "that goes both ways" | Posture's retrieval is DEFINED: the four tabs of the target + the four tabs of the most-similar name on the other side (Opal holding vs non-Opal), chosen by the Peers similarity function; the judgment compares the two packs; symmetric |

**What is NOT read into it:** no vendor call, no model call and no cell is authorized by the memo; the
similarity ranker's database is named as a question ("from some database"), answered in the design with a
measured candidate, not assumed; "goes both ways" restates the fourth word's symmetry and adds nothing wider.

## THE CARRIER

Unchanged: the PRD addendum at the round-10 L10, on the slug `3.0.0_SA_CVO~W` is adjudicating now. This
memo, the five page words, the executive-managers word, the egress words and the three substrate cards
(@5007337353) fold into ONE `prd_version` bump. The design that folds them is drafted as this seat's
deliverable `AMGT_RESAPP_PAGE_V2_DESIGN_20260915_W.md` so the addendum is a copy of a reviewed structure,
not a first draft written against the slug's clock.

---

**CORRECTION 2026-09-15 ~06:3xZ (`1.0.0_SA_CTO~W`).** The sentence above naming `AMGT_RESAPP_PAGE_V2_DESIGN_20260915_W.md` as a drafted carrier was FALSE when this record was committed (@fbd5d91431): no such file existed. `3.0.0_SA_CVO~W` caught it (ratified-text review @01e640925c). The file is created in the same commit as this correction, from this seat's `/draw` of ~04:5xZ (the as-built page) and Andrew's page words; the structure the addendum copied was the PRD's own CONTRACTS section, not a reviewed design file. `git log -1 -- org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_PAGE_V2_DESIGN_20260915_W.md` is the pin.
