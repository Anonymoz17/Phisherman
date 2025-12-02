# Phishing Email Trainer - MVP Scope

## Project Goal
Build a functional phishing simulation trainer that sends test emails, tracks clicks, and educates users. Focus: **working end-to-end in one weekend**.

---

## MVP SCOPE (Version 0.1) - MUST HAVE

### Core Functionality
- Send simulated phishing email to a list of email addresses
- Track when recipients click the link in the email
- Show educational "gotcha" page after click
- Display basic results dashboard showing who clicked

### Technical Stack
- **Backend:** Flask (single `app.py` file to start)
- **Database:** SQLite (file-based, zero configuration)
- **Email:** `smtplib` with Gmail SMTP (free)
- **Frontend:** Plain HTML/CSS (no JavaScript frameworks)
- **Hosting:** Local development only

### Features Included
1. **One phishing template** - Password expiration email
2. **Manual email list** - Hardcoded list of 3-5 emails in code
3. **Unique tracking links** - Generate UUID for each recipient
4. **Click tracking** - Log email, timestamp, and IP when link is clicked
5. **Educational landing page** - Static HTML showing "This was a test" + 3 red flags they missed
6. **Basic results view** - Simple HTML table showing who clicked and when

### Database Schema (Minimal)
```
users table:
- id (primary key)
- email (text)
- name (text)

clicks table:
- id (primary key)
- user_id (foreign key)
- tracking_token (text, unique)
- clicked (boolean, default false)
- click_timestamp (datetime)
```

### File Structure
```
phishing-trainer/
├── app.py                    # All Flask code here
├── database.db               # SQLite (auto-generated)
├── templates/
│   ├── phishing_email.html   # Email template
│   ├── landing.html          # "You got phished" page
│   └── results.html          # Admin results view
└── requirements.txt          # Flask only
```

### MVP User Flow
1. Admin runs script: `python app.py send-campaign`
2. System sends email to hardcoded list
3. User receives email with tracking link: `http://localhost:5000/track/<uuid>`
4. User clicks link
5. System logs click in database
6. User sees educational landing page
7. Admin visits `http://localhost:5000/results` to see who clicked

### Success Criteria
- Can send phishing email to yourself
- Clicking the link logs it in the database
- Can view results in a web page

### Technical Constraints (Keep it Simple)
- No user authentication (anyone can view results page for MVP)
- No email validation or error handling beyond basics
- No scheduled campaigns - manual trigger only
- No configuration files - hardcode everything
- No tests (yet)
- No deployment - runs on localhost only

---

## OUT OF SCOPE (Future Versions)

### Version 0.2 - Basic Improvements
- **Multiple templates** - Add 2-3 more phishing scenarios
- **CSV upload** - Load email list from file instead of hardcoded
- **Better styling** - Add Bootstrap for cleaner UI
- **Error handling** - Validate emails, handle send failures
- **Environment variables** - Move SMTP credentials out of code

### Version 0.3 - Admin Features
- **Admin authentication** - Password protect results page
- **Campaign management** - Create/edit/delete campaigns via UI
- **Template builder** - Simple form to customize email content
- **Export results** - Download CSV of campaign results

### Version 0.4 - User Experience
- **Difficulty levels** - Easy/medium/hard phishing templates
- **Credential harvesting** - Fake login form to test password entry
- **Detailed education** - Personalized feedback on what user missed
- **Progress tracking** - Show user's improvement over multiple tests

### Version 0.5 - Advanced Features
- **Scheduled campaigns** - Set date/time for automatic sending
- **Email analytics** - Open rates, click rates, time-to-click
- **Reporting dashboard** - Charts and graphs for organization metrics
- **Multi-organization support** - Separate campaigns for different groups

### Version 1.0 - Production Ready
- **Docker deployment** - Containerize for easy hosting
- **Proper authentication** - User roles (admin, org manager, user)
- **Email service integration** - SendGrid/Mailgun for better deliverability
- **HTTPS/SSL** - Deploy to cloud with proper security
- **Database migrations** - Alembic for schema changes
- **Comprehensive testing** - Unit and integration tests
- **API endpoints** - Programmatic access to campaigns and results

### Nice to Have (Someday)
- AI-generated phishing emails based on company context
- Browser extension for real-time phishing detection
- Integration with corporate training platforms
- Mobile app for on-the-go training
- Gamification with leaderboards and achievements
- Slack/Teams integration for notifications
- Machine learning to personalize difficulty
- Simulated voice phishing (vishing) scenarios
- Multi-language support

---

## First Coding Session Checklist

- [ ] Create project folder
- [ ] Install Flask: `pip install flask`
- [ ] Create `app.py` with basic Flask routes
- [ ] Create SQLite database with users and clicks tables
- [ ] Generate UUID tracking tokens
- [ ] Create basic email HTML template
- [ ] Set up Gmail app password for SMTP
- [ ] Send test email to yourself
- [ ] Verify tracking link logs click
- [ ] Create results page showing clicks

**Time budget:** 6-8 hours for a working MVP

---

## Red Lines (Do NOT Add to MVP)
- ❌ Docker/containers
- ❌ React/Vue/any JS framework
- ❌ Redis/message queues
- ❌ Real company branding/logos
- ❌ Collecting actual passwords
- ❌ Complex user management
- ❌ Payment/subscription features
- ❌ Mobile apps
- ❌ Real-time notifications
- ❌ Advanced analytics/ML

**Remember:** If it's not in MVP scope, don't build it until MVP is 100% complete and working.