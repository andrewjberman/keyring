# ANDREW-DIRECT 2026-08-19 (voice memo, CRO terminal) -- the infrastructure-graph program: goals, the foundational hierarchy, the endpoint

**Recorded by:** 4.0.0_SA_CRO . **Channel:** voice memo handed at the CRO terminal for analysis + planning interview
**Source file:** C:/Users/AndrewBerman/Desktop/new recordings/Infrastructure graph_9297.txt (transcribed audio; "4.0.0 essay underscore CRO" is the transcriber's rendering of 4.0.0_SA_CRO)
**Status:** RECORDED VERBATIM + BROADCAST same turn (org/XXX.md law). Planning interview IN PROGRESS at the CRO terminal; the settled plan will be recorded separately and cite this.

## THE MEMO -- VERBATIM, COMPLETE

And the last thing that we need to address is the continued development of our infrastructure
efforts.
And I've had 4.0.0 essay underscore CRO pursuing this.
They're the ones who are really looking into the semantic pipeline and the Kimi vertical
pipeline work.
And the current state is really that we want to work down from the top.
What that means is we want to make sure that all of our terminology, our system underscore
definitions actually are resolving.
We want to make sure that when we use these definitions, they resolve to a specific concept
because the only way that our ontology works is if everything can be run essentially deterministically.
We want to be able to run without a completely resolving defined foundation, we are going
to be doomed to hands drawn bullshit and coverage issues and all kinds of problems with the
denominator and recall.
So it's very important that we lock in our definitions, that we thoroughly check every
single step from definitions to the C0, C1, C2, C3 nodes, interactions, motifs, systems,
the D1, D2, D3.
We need to make sure these are all locked in the data flow.
We need to make sure that everything resolves at every level solely in our ontology because
all of the ontological stuff, it cannot be hand drawn, it cannot be stale.
We have to establish these definitions and make them exceedingly robust because all of
the tooling, all of the Trino, the Kimi semantic pipeline, the comp tools, all of that relies
on having concrete denominators and we do not have concrete denominators unless these
terms resolve and they are very, very cut and dried and clear.
So we want to start from that basis.
And I think we want to proceed through our tooling.
We want to make sure all of the tooling is very tight.
And from there, we really want to start understanding how to build out our world model.
The whole purpose of this infrastructure work is to build what I like to call and what I
hope to achieve is a generalizable ontology.
We should be able to build systems that adapt to any system so that we are able to apply
our foundational rules, foundational logic to be able to govern these systems.
What this looks like and what is something that I would like to print to the record is
I believe that all systems need to begin with a deterministic foundation.
The deterministic foundation is almost everything.
That is our lexical strategies, how we use our BM25 and corp localize as functions.
This is the base for everything and that is why the ontology is so important.
This goes when we start to need to get into semantic details about how these things work.
We want to lead with NLP.
We want to lead with a potion or model to VEC or however we need to do it because that
is going to be faster and cheaper than having to pour actual inference on it.
If we can't handle it with NLP or it is ready to graduate to inference then we have very
targeted AI that goes over and kind of assesses the patterns and semantics and ties it together
there.
At the very, very top of this logic is the user input.
This is extremely expensive and extremely high leverage which is why we want to make
a pattern of we always go deterministic slash lexical to NLP, to AI inference, to user input.
This is how all functions, all autonomous functions, all pipelines, this is the pattern
that we need to look at as our foundational hierarchy, how we put together these systems.
I want to kind of audit what we have.
The goal behind doing this is that we want to create a system where as we create goals,
as the user says we need to do this, this and this, we have everything on a grid.
We know what is happening.
We have every square inch of our execution space, ultimately of our code base, of our
knowledge space, our document space and Microsoft SharePoints.
We need our various ingestion points throughout looking, et cetera.
We want all of this on the graph so we really need to be able to create a system where if
I am a user and I say I go into a meeting and they say, hey, we need a product that
does this and then I realize that we need some products that is, let's call it advisor
intelligence, which is something we already have.
Let's say that we're like, oh, we need to create a new advisor intelligence platform
for some new partner.
I need to be able to say that and say the specs of it, which may need, requires some
differentiation and our system needs to know where everything is so well that if I want
to instantiate an entirely new infrastructure, that should take, I should not have to say
anything.
I should be able to be like, hey, spin up this exact, spin up our entire Opal infrastructure
for this new partner.
It should take no further direction because we should have everything understood.
We should have every pipeline on the map.
We should have all of our logs and semantic data, how we got to these points.
We should be able to create infrastructure at light speed and with minimal user input.
But the only way that this is possible is if we build out these systems.
This is something that's very important to me and we need to be very, very thoughtful
about it.

