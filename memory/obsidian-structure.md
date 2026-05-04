# Obsidian Vault Structure — Current (as of 2026-04-14)

This file documents the canonical Obsidian vault structure. **05_Diversys no longer exists.** All Diversys content is under `00_Alfred/10_Diversys`.

## Vault Root: `/mnt/obsidian`

### Top-level directories

| Path | Purpose |
|---|---|
| `/mnt/obsidian/00_Alfred` | Alfred's workspace (work + personal) |
| `/mnt/obsidian/01_Elliot` | Elliot's workspace |
| `/mnt/obsidian/02_General_Info` | Shared reference, How-Tos, Excalidraw |
| `/mnt/obsidian/03_Indexes` | Index files |
| `/mnt/obsidian/04_Notes` | General notes |
| `/mnt/obsidian/05_Action_Items` | Action Register, My_Actions, Others_Actions |
| `/mnt/obsidian/06_Notifications` | Notification logs |
| `/mnt/obsidian/06_Personal_Email` | Personal email triage |
| `/mnt/obsidian/07_Diversys_Email` | Diversys email triage |
| `/mnt/obsidian/07_OpenClaw` | OpenClaw notes |
| `/mnt/obsidian/08_Environments` | Environment configs |
| `/mnt/obsidian/09_Reference` | Reference materials |
| `/mnt/obsidian/Obsidian` | Obsidian app data |
| `/mnt/obsidian/guide-media` | Media/guide assets |

**Note:** `/mnt/obsidian/05_Diversys` does NOT exist. It was moved to `/mnt/obsidian/00_Alfred/10_Diversys`.

---

## 00_Alfred structure

| Path | Purpose |
|---|---|
| `/mnt/obsidian/00_Alfred/00_Attachments` | File attachments |
| `/mnt/obsidian/00_Alfred/10_Diversys` | **All Diversys content** (see below) |
| `/mnt/obsidian/00_Alfred/20_Diversys_Email` | Diversys email triage output |
| `/mnt/obsidian/00_Alfred/30_Alfred_Sub_Agents` | Sub-agent output folders |
| `/mnt/obsidian/00_Alfred/40_PowerPoint` | Presentations and templates |

---

## 10_Diversys structure (canonical Diversys root)

**Path:** `/mnt/obsidian/00_Alfred/10_Diversys`

| Path | Purpose |
|---|---|
| `Clients/` | Client-specific folders and emails |
| `Clients/ABCRC/` | ABCRC (includes Email, API Integrations, Transcripts) |
| `Clients/Aramco/` | Aramco (includes Email) |
| `Clients/CalRecycle_EWaste/` | CalRecycle E-Waste (includes ROI) |
| `Clients/CalRecycle_Tires/` | CalRecycle Tires (includes Email) |
| `Clients/ENCORP/` | ENCORP (includes Email) |
| `Clients/EkoCircles/` | EkoCircles (includes Email, SM_Gunn) |
| `Clients/Tarkett/` | Tarkett (includes Email) |
| `Customer_Success/` | Customer Success materials |
| `Delivery/` | Delivery and implementation |
| `Enablement_Programs/` | Enablement programs |
| `Executive_Comms/` | Executive communications |
| `KPI_Analytics/` | KPI and analytics |
| `Management_Meetings/` | Meeting transcripts by person (Dejan, Kim_Sally, Mark, Mike, Roger) |
| `Marketing/` | Marketing (includes Product_Marketing) |
| `Meetings/` | General meetings |
| `Operations/` | Operations |
| `People_Ops/` | People operations |
| `Product/` | Product documentation (see below) |
| `Programs/` | Programs |
| `Projects/` | Projects (includes Support Page Makeover) |
| `QA/` | Quality assurance |
| `RFP_Collateral/` | RFP materials |
| `Risk_Compliance/` | Risk and compliance |
| `Sales/` | Sales materials |
| `Solution_Engineering/` | Solution engineering |
| `Strategy/` | Strategy |
| `Support/` | Support (FAQs, Mobile App, Tenant Creation, Ticket Requests) |
| `Tech_expert/` | Technical expert materials |
| `Training/` | Training materials |
| `Training_Enablement/` | Training enablement |

### Product substructure

| Path | Purpose |
|---|---|
| `Product/API_Knowledge/` | API docs, extracts, FAQ |
| `Product/Confluence/` | Confluence exports (Compliance, CoC, On-Boarding, Product Description, Marketing, Requirements, Release Info, R&D, UX-UI) |
| `Product/Data_Model/` | Data model documentation |
| `Product/Release_Notes/` | Release notes |
| `Product/Roles/` | Product roles |
| `Product/Software_Development/` | Software development docs |
| `Product/Training/` | Product training (API, Advanced, Basic, BI, Clients, Product, Release) |

---

## Client email domain mapping

| Client | Possible domains |
|---|---|
| ENCORP | @returnit.ca |
| Tarkett | oneturfpro |
| EkoCircles | ekocircles.com |
| CalRecycle | calrecycle.ca.gov |
| Aramco | aramco.com |

---

## Key reference files

- **Product KB:** `/mnt/obsidian/00_Alfred/10_Diversys/Product/Product_KB.md`
- **Product Index:** `/mnt/obsidian/00_Alfred/10_Diversys/Product/Product_Index.md`
- **API Basics Manual Extract:** `/mnt/obsidian/00_Alfred/10_Diversys/Product/API_Knowledge/API_Basics_Manual_Extract.md`
- **Swagger Guidebook Extract:** `/mnt/obsidian/00_Alfred/10_Diversys/Product/API_Knowledge/2025_API_Basics_Guidebook_Swagger_Extract.md`
- **Action Register:** `/mnt/obsidian/05_Action_Items/Action Register.md`
- **Action Register Readable:** `/mnt/obsidian/05_Action_Items/Action_Register_Readable.md`
- **Agent Folder Map:** `/mnt/obsidian/02_General_Info/Agent_Folder_Map.md`
- **Mac Mini Install Journal:** `/mnt/obsidian/02_General_Info/How_To/Mac_Mini_NemoClaw_Install_Journal.md`

---

Last verified: 2026-04-14