# IC 01 · Investment Case — TrAIvel Friend
> ⚠️ Fictional company — all names and figures are created for training purposes.
> Status: working draft, developed step by step. Submitted to **AIktivInvest** for evaluation by the KI-Manager.

---

## 1 · Proposal

The following proposal has been submitted to AktivInvest for consideration and funding:

**TrAIvel Friend** is an AI-based travel companion. It organises the entire journey — "the experience" — for the user: from the first vague idea of a destination, through the booking of flights, hotels, theatre or museum tickets and restaurant tables, to the handling of claims and the post-trip feedback and recommendations for other travellers. It is built around a **personal AI agent**.

---

## 2 · Product / Features

- **Destination brainstorming** with a recommendation function based on purchases in other apps (e.g. Amazon or Opodo) and selected personal preferences (sport, culture, etc.).
- **Pre-booking of flights and hotels** for a selected period, subject to final approval by the traveller.
- **Reservation of restaurant tables, taxis or alternative transport**, plus payment via the traveller's stored card details (each confirmed by the traveller).
- **Individual day-by-day (and night) itineraries** for the destination.
- **Personal agent** that translates requests into the local language and answers back into the traveller's language.

---

## 3 · Business Model

Commission-based: TrAIvel Friend earns an affiliate / booking commission on the flights, hotels, activities and restaurant/transport bookings it intermediates. Possible later layers: premium subscription, sponsored placements, data-driven recommendations.

---

## 4 · Business Parameters & Growth Potential

### Why now — demand-side evidence

The behaviour this product depends on is already shifting, and the incumbent discovery layer is visibly losing ground.

| Signal | Figure | Source |
|---|---|---|
| Americans using an AI app to plan a holiday | **55 %** last summer, up from **38 %** the year before | McKinsey, cited in *The Economist* (Aug 2026) |
| Tripadvisor web traffic | estimated **–20 %** in one year; the company attributes this to AI | *The Economist* (Aug 2026) |
| Guidebook sales | sharply down over the past two decades | *The Economist* (Aug 2026) |
| Average chatbot prompt length | ~25 words — users are posing relatively complex queries | *The Economist* (Aug 2026) |

**That the recommendation layer moves real money is supported by academic work.** Dante Donati (Columbia Business School) found that when the EU abolished mobile roaming charges in 2017, the resulting increase in tourists consulting Tripadvisor on the go produced a **5 % revenue uplift** for Rome's tourist-oriented restaurants — concentrated among the highest-rated. Whoever controls the recommendation captures measurable spend. That is the prize TrAIvel Friend is competing for.

**Caveat for the committee:** these are journalistic figures. The McKinsey number is a consultancy survey; the Tripadvisor traffic decline is an estimate attributed to the company itself, which has an interest in explaining a decline it did not cause. Donati's finding is the only one with an identifiable academic author and method. Treat the first three as direction, not magnitude.

### Market sizing (TAM → SAM → SOM)

Sizing logic (as instructed): *total city-trip spending × 1 % captured booking share × commission rate*.

| Level | Basis | Figure |
|---|---|---|
| **TAM** — city breaks / short getaways | Global weekend-getaway market 2024 (≈ USD 246 bn, ~7 % CAGR); broader urban-tourism spend ≈ USD 7.4 tn (2025) as upper bound. Short trips (≤ 7 days) = ~54 % of all tourism activity. | **≈ USD 250 bn** (conservative) |
| **SOM** — captured booking volume (GMV) | 1 % of TAM intermediated through TrAIvel Friend | **≈ USD 2.5 bn GMV** |
| **Revenue** | GMV × commission rate | see sensitivity below |

**Commission sensitivity** (annual revenue at ~USD 2.5 bn GMV):

| Commission on GMV | Annual revenue |
|---|---|
| 0.001 % *(as noted in the brief)* | ≈ **USD 25 k** — implausibly low; almost certainly a slip |
| 3 % | ≈ USD 74 m |
| 5 % | ≈ USD 123 m |
| 8 % | ≈ USD 197 m |

> ⚠️ **Assumption to correct:** real online-travel commissions run ~5–10 % on hotels and ~0–15 % on flights; affiliate programmes pass through a share of the ~15 % supplier commission. A blended take rate of **~5–8 %** is realistic — the 0.001 % input should be replaced before this case goes to committee.

### Competitive landscape

The AI trip-planning space is crowded and moving fast:

| Player | Positioning |
|---|---|
| **Mindtrip** | "Most Innovative Company" 2025; strong map integration and collaborative planning |
| **Layla** | 4.9★, 1.1 m+ trips planned; live pricing across flights, hotels, trains, activities |
| **MonkeyTravel** | ~350 k monthly US visitors; group planning with built-in voting |
| **Wonderplan / Wanderlog / iMean AI / Travo** | itinerary builders adding real-time, agentic features |
| **Incumbent OTAs** (Booking.com, Expedia, etc.) | embedding AI agents on top of their own inventory and distribution |

**Two competitor categories were missing from the original draft. Both are material.**

| Category | Why it competes | Evidence |
|---|---|---|
| **General-purpose chatbots** — ChatGPT, Gemini, Google AI Mode | They already plan trips, at no marginal cost to the user, inside an interface the user opens anyway. Each draws on a different corpus — ChatGPT largely on online guides and Reddit threads, Google's AI Mode on Google Maps reviews — so they produce genuinely different itineraries. | 55 % of Americans used an AI app to plan a holiday last summer |
| **Human advisers — and the platforms arming them** | Demand for human advisers is growing, not shrinking, especially at the top end. **Fora**, a luxury host agency, built a billion-dollar business by selling advisers an AI platform that speeds up administrative work — AI *for* the adviser, not instead of. | ~⅓ of British travellers booked through a human specialist last year (ABTA); ASTA membership >310 k, up from 190 k in 2024 |

**Frontier trend (2026):** *agentic* AI that proactively re-plans — e.g. noticing a booked restaurant is closed and rebooking before the traveller lands.

**Differentiation TrAIvel Friend must prove:** end-to-end execution including payment and claims; cross-app personalisation from purchase history; a built-in translation agent.

**The strategic fork the committee should force.** Two viable models exist in this market and TrAIvel Friend has only costed one:

- **B2C disintermediation** (the current proposal): win the traveller directly, earn booking commission. Competes head-on with free chatbots on one side and OTA inventory on the other.
- **B2B2C augmentation** (the Fora pattern): sell the agent layer to advisers and agencies, monetise seats or transactions. Smaller consumer brand, but a paying customer who already owns the relationship — and the only model in this space with a demonstrated billion-dollar outcome.

The second is not obviously worse. It should be priced before the first is funded.

---

## 5 · Open items — to develop step by step

- ~~Problem statement & "why now"~~ — first evidence now in §4; still needs the customer problem stated in the founders' own words
- Traction / pilots (currently none)
- Go-to-market & distribution (critical in a crowded market)
- Unit economics: customer acquisition cost, lifetime value, take rate, and "Return on Token" (LLM cost per completed booking)
- Financial projections (3–5 years)
- Fit with the AIktivInvest thesis and target ticket size

### Key risks — with the evidence now attached

**Regulatory and contractual** (unchanged, still to be worked): payment regulation (PSD2), data protection (GDPR — cross-app purchase data plus stored card details), dependency on OTA inventory and APIs.

**Product risk 1 · The model invents places that do not exist.** Daniel Paül i Agustí (University of Lleida) collected 10,000 ChatGPT recommendations for Barcelona. They covered **215 distinct locations** — against roughly **1,300** locations represented in a comparable set of tourist photographs from Instagram. Among the recommendations were **38 attractions that appeared to be fabricated**.

For a planner this is an annoyance. For TrAIvel Friend — which books tables, buys tickets and charges a stored card — it is a direct liability exposure. This turns the existing "liability for faulty bookings" line from a legal abstraction into a measured failure rate that diligence can size. **Required:** a verification layer between recommendation and booking, and an explicit answer to who pays when a booking is made against a place that does not exist.

**Product risk 2 · The same question does not produce the same answer.** An analysis by Evertune found that Gemini's jointly most-recommended pizzerias in Rome appeared in **91 %** of its responses — meaning close to one user in ten never sees the top pick at all. Across all responses it named **24 different** establishments.

Consequences for this business model, in order of severity: itineraries are not reproducible, so complaints cannot be reconstructed; quality assurance has no stable baseline to test against; and the "sponsored placements" revenue layer sketched in §3 is hard to sell and harder to disclose honestly if placement cannot be guaranteed.

**Product risk 3 · Recommendation quality is inherited, not owned.** ChatGPT's answers rest largely on online guides and Reddit threads; Google's AI Mode on Google Maps reviews. The core asset — knowing where to send someone — belongs to whichever model TrAIvel Friend sits on. A model change, a licensing change or an outage moves the product's quality without the company touching its own code. **Required:** name the model dependency, the substitution plan, and what is owned independently of it.

**Market risk 1 · Service recovery is where humans currently win.** Evan Frank, co-founder of Fora: *"You can't call your AI if your room is wrong or you missed your transfer."* §2 lists claims handling as a feature. The market evidence says this is precisely the moment travellers reach for a human. **Required:** state what happens at 23:00 when the hotel has no reservation — and cost it.

**Market risk 2 · Demand for humans is counter-cyclical.** Travellers are *more* likely to book through an adviser during geopolitical disruption or extreme weather, when booking feels risky. A pure-AI product may therefore lose demand exactly when travel is most disrupted — a correlation that undercuts the usual "travel always recovers" argument.

**Market risk 3 · The high-value segment is moving the other way.** At the top end, clients pay a **$100,000 annual subscription** on top of seven-figure travel budgets for a human fixer. Advisers are chosen for taste, judgment, country knowledge and access to closed hotel networks. If the willingness to pay concentrates where TrAIvel Friend is weakest, the realistic segment is the mid-market — which lowers both the take rate and the defensibility assumed in §4.

---

## 5b · Questions for the investment committee

Eight questions the case must answer before it is worth a term sheet. Each is answerable — none is rhetorical.

1. **Why would a traveller route through us at all?** ChatGPT and Gemini plan trips for free, inside an app the user already has open. What does our booking-and-payment layer add that is worth switching for — and can we state it in one sentence a consumer would repeat?
2. **What does the verification layer cost?** Given a measured tendency to invent attractions, no booking may execute against an unverified entity. Is that a supplier-API check, a human review queue, or both — and what does it do to gross margin per booking?
3. **Who pays for a booking made against a place that does not exist?** Us, the supplier, or the traveller. This needs a contractual answer, not a support policy.
4. **How do we reconstruct a complaint** when the itinerary that produced it cannot be reproduced? Do we log and version every recommendation, and what does that mean for GDPR retention?
5. **Can sponsored placement be sold honestly** if placement is probabilistic? If not, that revenue layer should come out of the model.
6. **Which model are we built on, what happens if it changes or disappears, and what do we own that survives it?**
7. **What is the answer at 23:00** when the hotel has no reservation? Human on call, insurance, supplier guarantee — each has a cost line.
8. **Have we priced the B2B2C alternative?** Selling the agent layer to advisers is the only model in this market with a demonstrated billion-dollar outcome. Rejecting it is defensible; not having costed it is not.

### A note on the evidence — for the analyst preparing this case

The travel-adviser figures in §4 come with a live contradiction worth carrying into the committee. **LinkedIn** ranked travel adviser among the fastest-growing jobs in America. The **US Bureau of Labour Statistics** expects the occupation to grow **more slowly than average** through 2034.

Same occupation, opposite signals. One source is a commercial platform reporting from its own user base, with an interest in showing labour-market momentum; the other is the federal statistical agency. Where they conflict, the statistical agency carries more weight — and a case that quotes the more flattering figure without naming the conflict has told the committee something untrue by omission.

The same discipline applies to the adoption figures in §4: name the source type beside the number, and let the reader discount it themselves.

---

## 6 · Organizational Structure

xxxx *(to be developed)*

---

## 7 · Funding Requirements

xxxx *(to be developed)*

---

## Sources (market & competition)

- Weekend Getaway Market — [Growth Market Reports](https://growthmarketreports.com/report/weekend-getaway-market)
- Urban Tourism Market — [Coherent Market Insights](https://www.coherentmarketinsights.com/industry-reports/urban-tourism-market)
- AI trip-planner comparison (Mindtrip, Layla & others) — [MonkeyTravel](https://monkeytravel.app/blog/best-ai-trip-planners-2026-compared)
- Layla — [layla.ai](https://layla.ai/) · Mindtrip — [mindtrip.ai](https://mindtrip.ai/)
- Online-travel commission rates 2025–2026 — [Travelovin](https://travelovin.com/blog/online-travel-agency-commission-rates-2025-2026)

### Demand, AI recommendation quality & the human-adviser counter-trend

- *"Can AI save tourists from the TikTok herd?"* — **The Economist**, August 2026. Source of the McKinsey adoption figures, the Tripadvisor traffic estimate, and the Evertune consistency analysis.
- *"Travel agents are in demand—especially for luxury trips"* — **The Economist**, 13 August 2026. Source of the ABTA and ASTA membership figures, the Fora model, and the LinkedIn / Bureau of Labour Statistics conflict.

**Primary sources named in those articles — cite these directly where possible, they are stronger than the reporting:**

- **Daniel Paül i Agustí** (University of Lleida) — comparison of ChatGPT recommendations against geocoded tourist photography for Barcelona: 215 recommended locations vs ~1,300 photographed, including 38 apparently fabricated attractions. *Academic author, named institution — the strongest single finding for our product-risk section.*
- **Dante Donati** (Columbia Business School) — 2017 EU roaming-charge abolition, mobile Tripadvisor consultation and a 5 % revenue uplift for Rome's tourist restaurants.
- **University of Westminster** — finding that ChatGPT shows "a marked preference for well-established tourist hubs".
- **ABTA** (British travel trade association) and **ASTA** (American Society of Travel Advisers) — membership and booking-channel figures; trade bodies, so directionally useful but not disinterested.
- **US Bureau of Labour Statistics** — occupational growth projection to 2034.
- **Evertune** — AI analytics firm, commissioned by the publication for the chatbot comparison. Vendor-adjacent; use the consistency finding as an illustration, not as a measurement.

*Note: market-research and product/commission figures above are practitioner sources (not government/academic Tier-1). The city-break TAM and the ~5–10 % commission range are each supported by more than one of the sources listed. The Economist articles are quality journalism, not peer-reviewed research — the academic findings they report should be traced to the original work before this case goes to committee.*
