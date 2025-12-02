# Development Context - Phishing Simulation Tool

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
- **Backend**: Python with Flask
- **Frontend**: React with UI  library (React-Bootstrap or Shadcn/UI - TBD)
- **Database**: -
- **Email**: -
- **Deployment**: -
- **Charts**: -
- **Auth**: Flask-Login (simple session management)
- **UI Complexity**: -

## MVP Feature Set (Functional Focus)
**Must Have (Core Functionality):**
1. Email delivery (SMTP with wizard and validation)
2. Click tracking (unique URLs per recipient)
3. Campaign creation and management
4. Basic analytics dashboard (who clicked, when, aggregate stats)

## Target User
- **Primary**: Solo sysadmin (50-150 person company)
- **Capabilities**: Can run Docker, configure SMTP with help, edit config files, 
troubleshoot with docs

## Key Metrics to Track
- Email sent count
- Link clicked count
- Timestamps for all events
- User identity (privacy concerns to address)
- Device/browser information
- Geolocation