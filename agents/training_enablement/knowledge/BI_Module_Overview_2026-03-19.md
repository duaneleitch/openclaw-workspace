# Diversys BI Module - Support Knowledge Reference

**Added:** 2026-03-20
**Source:** Internal training session, March 19, 2026 (Mark, Alan, Dejan/Dan)
**Full note:** /mnt/obsidian/00_Alfred/10_Diversys/Product/Training/Business_Intelligence/BI_Module_Overview_and_Demo_2026-03-19.md

---

## What Is the BI Module?

Diversys is building a new Business Intelligence module powered by **Apache Superset** (open-source, originally from Airbnb, now Apache Foundation). It replaces MongoDB Charts with far greater flexibility, more chart types, and better end-user features.

**Current status as of March 2026:** Prototype in staging only. Not yet in production.

---

## Five Dashboards

### 1. Operational Efficiency
- Filters: time (flexible ranges), product, transaction type, transaction status
- Cross-filtering: click a data point to filter all charts on the dashboard simultaneously; fully reversible
- Charts: monthly transactions by type (line), by mode (bar), by status (bar), daily volume calendar heat map, weight by type/product (pie), KPI gauge (actual vs target)
- Time range slicer available on several charts

### 2. Product Volumes
- Charts: top 10 collectors by weight (pie), top 10 haulers by weight (pie), collection sites map (bubble), processor/hauler sites map (bubble), collected weight by region (sunburst), top 10 cities by weight (bar), monthly GHG savings (chart)
- Note: "Processor sites" in the demo = hauler sites for this account

### 3. Compliance
- Default filter: last quarter (compliance is monitored frequently on recent data)
- Charts: top 10 transporters by pickup distance deviation, top 10 by drop-off deviation, participants with most error transactions (interactive table with search)
- Distance deviation = actual GPS location vs expected site location vs defined threshold (not an average)
- Errors vs warnings: distinct categories. Errors = serious issues (wrong pickup, missing data). Definition still being refined.
- Error table: shows counts and percentages only. Cannot drill to individual transaction IDs yet.

### 4. Participants
- Geographic heat maps for haulers and collectors
- Darker red = higher concentration
- Blank areas = no participants in Diversys system (cannot detect participants not in the system)

### 5. Transportation Activities
- Flow/Sankey chart: carrier to collector weight flows; wider line = more weight; shows one-to-many relationships
- Defaults to top 10 relationships; users cannot paginate to 11-20 themselves (requires Diversys config change)

---

## Key Capabilities

- ~60 chart types available
- New types: calendar heat map, gauge, sunburst, flow/Sankey
- Export: aggregated output data to Excel (not raw records or formulas); CSV export planned
- View underlying data as a table (aggregated, not transaction records)
- Cross-filtering within a dashboard (not across dashboards)
- Chart descriptions available via three-dot menu on each chart
- Dashboard tabs and layout customization

---

## Common Support Questions

**Is it available to customers?** No. Staging prototype only as of March 2026.

**Can customers build their own charts?** No. Diversys pre-configures all charts. Self-serve dashboard builder (from Diversys chart library) is on the roadmap.

**What happened to MongoDB Charts?** Still in use but being replaced by Apache Superset.

**Can I export data?** Yes, to Excel (aggregated output only). CSV planned.

**What is cross-filtering?** Click a data point on one chart to filter all other charts on the same dashboard. Reversible.

**Errors vs warnings in compliance?** Distinct. Errors = serious issues (wrong location, missing data). Full definition still being finalized by engineering.

**Can I see which transactions have errors?** Not yet. Count and percentage only. Drill-down to individual transactions is planned.

**Can I paginate beyond top 10 in the flow chart?** Not as an end user. Requires Diversys staff to change the configuration.

---

## How Customers Get Charts (Current Process)

1. Customer tells Diversys what reports they need
2. Diversys (Alan or team) configures charts and dashboards
3. Customer receives pre-built dashboards
4. Changes or new charts require a Diversys engagement (support or training)
