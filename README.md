# NnC - Nextcloud AI Calendar Assistant

## Contents

[Project Overview](#project-overview) |
[Project Background](#project-background) |
[Getting Started](#getting-started) |
[Testing](#testing) |
[Project Brief & Timeframe](#project-brief) |
[Technologies Used](#technologies-used) |
[Result](#result) |
[Development Lifecycle](#development-lifecycle) |
[Wins](#wins) |
[Challenges](#challenges) |
[Bugs & Future Improvements](#bugs-and-future-improvements) |
[Key Learnings](#key-learnings) |
[Supporting Info](#supporting-info)

---

# Project Overview

NnC (Nancy) is an AI-powered assistant that enables User abstracted interaction with a Nextcloud calendar via a command-line "chat" interface. The assistant leverages OpenAI's function calling and the `caldav` package to execute calendar operations (CRUD - Create, Read, Update, Delete) on a NextcloudPi instance running on a local network. It processes natural language inputs and determines whether to create, update, retrieve, or delete events, and reports back to User.

---

# Project Background

The desire for an AI-integrated personal calendar assistant came from wanting ownership of own calendar on local server, as well as an open source(ish) AI assistant that could execute calendar actions rather than navigating Nextcloud’s UI. Many voice assistants and calendar automation tools exist but do not integrate well with **self-hosted solutions** like NextcloudPi. The challenge was to create a **mostly local AI-driven** interface that interacts with a personal Nextcloud calendar while maintaining modularity and future expandability.

---

# Getting Started

To set up and run NnC, follow these steps:

### **Prerequisites**
- A running **NextcloudPi** instance with CalDAV enabled
- A **Python 3.9+** environment
- An **OpenAI API Key**
- Required dependencies (see `requirements.txt`)

### **Installation Steps**
1. Clone this repository:
   ```sh
   git clone git@github.com:nedd-ludd/NnC.git
   cd nextcloud-ai-assistant
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
<!-- 3. Set up environment variables (create a `.env` file):
   ```ini
   OPENAI_API_KEY=your-api-key-here
   NEXTCLOUD_URL=http://192.168.1.100/remote.php/dav
   NEXTCLOUD_USER=your-username
   NEXTCLOUD_PASS=your-password
   ```
4. Run the assistant:
   ```sh
   python src/face.py
   ``` -->

---

<!-- # Testing

To test functionalities, use the CLI:

### **Example Commands**
```sh
python src/face.py "Add Noisily Festival to my calendar from July 11th to July 14th in the UK."
```
```sh
python src/face.py "What events do I have this Friday?"
```
```sh
python src/face.py "Cancel my meeting on Wednesday."
```
Check logs in `logs/` for debugging information.

--- -->

# Project Brief

## **Functional Requirements**
- Interpret natural language inputs and map them to CalDAV actions.
- Support **Create, Read, Update, and Delete** operations.
- Maintain a conversational flow that allows follow-up commands.

## **Non-Functional Requirements**
- Securely authenticate with Nextcloud.
- Modular architecture for easy expansion.

## **Deliverables**
- Command-line interface (`face.py`)
- AI interaction layer (`ai_interface.py`)
- Calendar integration (`calendar_caller.py`)
- Executive logic (`executive.py`)
- Modular CRUD operations (`crud_functions.py`)

---

# Technologies Used

| Category | Technologies |
|----------|-------------|
| **Languages** | Python |
| **AI & NLP** | OpenAI GPT-4 function calling |
| **Calendar API** | CalDAV (Nextcloud) |
| **Operating System** | Linux (Raspberry Pi OS) |
| **Development Tools** | VS Code, GitHub |
| **Networking** | Local network API calls |

---

# Result

✅ Seamless AI-driven event management.  
✅ Works entirely within the terminal.  
✅ Modular and scalable for future enhancements.  

---

# Development Lifecycle

## **Planning**
- Defined core modules: AI interaction, CRUD operations, Nextcloud integration.
- Considered potential pitfalls (e.g., ambiguous commands, handling multiple events).

## **Execution**
- Implemented OpenAI function calling.
- Created an executive control layer to handle follow-up actions.
- Developed a clean API for calendar interactions.

---

# Wins

- 🎯 Successfully interfaced **AI with Nextcloud** via CalDAV.
- 💡 **Scalable** design allows additional features like recurring events.
- 🚀 **Fully local** (no need for external services beyond OpenAI API calls).

---

# Challenges

- **Handling Ambiguous Queries** - Implemented AI follow-ups to clarify actions.
- **OpenAI API Call Optimization** - Reduced unnecessary calls by batching requests.
- **Event Conflict Handling** - Needed logic to prevent overlapping events.

---

# Bugs & Future Improvements

### **Known Issues**
- AI sometimes **misinterprets vague follow-ups**.
- Lacks a **GUI interface** (CLI only for now).

### **Planned Enhancements**
✅ Add a **GUI interface** for non-technical users.  
✅ Implement **recurring events** support.  
✅ Improve **event conflict resolution logic**.  
✅ Support for **multiple calendars** (e.g., work vs personal).  

---

# Key Learnings

- **Deepened knowledge of AI function calling**.
- **Gained hands-on experience with CalDAV**.
- **Refined understanding of modular software design**.

---

# Supporting Info

For additional setup and troubleshooting, refer to `docs/supporting_info.md`.

**Feedback & Contributions Welcome!** 🚀

[Back to Top](#project-overview)

