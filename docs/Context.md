# Development Context - Phishing Simulation Tool

**Last Updated:** 07/Dec/2025 19:20 SGT (UTC+8)

## Project Overview
Building an open-source phishing simulation tool for SMEs as a portfolio project that provides real value to the community.

## Developer Profile
- **Team Size**: Solo developer
- **Technical Background**:
  - Moderate in Python
  - Minimal web development experience (frontend/backend)
  - No experience with email systems (SMTP, deliverability)
  - No OAuth/authentication experience
  - Minimal database design experience
  - Zero DevOps experience
  - Want to learn React during this project
- **Time Commitment**: Almost full-time (alongside manageable intern workload)
- **Timeline**: 2-3 months maximum
- **Budget**: $0 - completely free tools and resources

## Core Constraints
1. Zero budget for hosting, APIs, third-party services
2. Solo developer with limited web dev experience
3. 2-3 month delivery timeline
4. Must use completely free tools and resources
5. Learning React on the job

## Technical Stack Decisions
- **Backend**: Python with Flask ✅ (implemented in app.py)
- **Frontend**: Plain HTML/CSS with Jinja2 templates ✅ (React planned for later versions)
- **Database**: SQLite ✅ (file-based, zero configuration)
- **Email**: smtplib with Gmail SMTP (Phase 4 - in progress)
- **Deployment**: Local development only (MVP)
- **Charts**: Not needed for MVP (basic tables sufficient)
- **Auth**: None for MVP (planned for later versions)
- **UI Complexity**: Simple HTML/CSS with inline styles ✅

## MVP Feature Set (Functional Focus)
**Must Have (Core Functionality):**
1. Email delivery (SMTP with wizard and validation) - Phase 4 in progress
2. Click tracking (unique URLs per recipient) ✅ Implemented
3. Campaign creation and management - Phase 4-5 in progress
4. Basic analytics dashboard (who clicked, when, aggregate stats) ✅ Implemented

**Current Implementation Status:**
- ✅ Database with users and clicks tables
- ✅ Click tracking via `/track/<token>` route
- ✅ Educational landing page after click
- ✅ Admin results dashboard with styled table
- ✅ Phishing email HTML template
- 🔄 Email sending functionality (next up)
- ⏳ Command-line campaign trigger

## Target User
- **Primary**: Solo sysadmin (50-150 person company)
- **Capabilities**: Can run Docker, configure SMTP with help, edit config files, 
troubleshoot with docs

## Key Metrics to Track
**Currently Implemented (MVP):**
- ✅ Link clicked count (boolean flag in database)
- ✅ Click timestamps (stored in clicks table)
- ✅ User identity (name and email linked to clicks)

**Planned for Future Versions:**
- Email sent count
- Device/browser information
- Geolocation
- Open rates (if tracking pixels are added)