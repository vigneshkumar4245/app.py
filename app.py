# ==========================================================
# FormGenie AI - FRONTEND ONLY (Python + Streamlit)
# Backend / AI / API ethuvum illa. Ellam sample (fake) data.
# "SAMPLE" nu irukura idathula dhaan real project la
# Gemini / Google Forms API connect pannuvom.
# ==========================================================

import streamlit as st

# ---------- Page settings ----------
st.set_page_config(page_title="FormGenie AI", page_icon="📝", layout="centered")

# ---------- SAMPLE DATA (AI kudukka pora maadhiri) ----------

# SAMPLE: AI create panna questions
sample_questions = [
    {"text": "How was the overall hackathon?", "type": "rating"},
    {"text": "Which part did you like the most?", "type": "text"},
    {"text": "What can we improve next time?", "type": "paragraph"},
    {"text": "Any other comments?", "type": "paragraph"},
]

# SAMPLE: participants anuppina answers (sentiment ready-ah irukku)
sample_responses = [
    ("The food was really good", "positive"),
    ("Mentors were very helpful", "positive"),
    ("Loved the team activities", "positive"),
    ("Food was not bad", "positive"),
    ("Great organisation and prizes", "positive"),
    ("Mentors cleared all my doubts", "positive"),
    ("WiFi was very slow", "negative"),
    ("Not enough power sockets", "negative"),
    ("Registration took too long", "negative"),
    ("Internet kept disconnecting", "negative"),
    ("The event was okay", "neutral"),
    ("Nothing special", "neutral"),
]

# SAMPLE: AI kudukka pora Top 3 praises and complaints
sample_praises = [
    ("Helpful mentors", 2),
    ("Good food", 2),
    ("Well organised event", 1),
]


sample_complaints = [
    ("Slow WiFi and internet", 2),
    ("Not enough power sockets", 1),
    ("Long registration queue", 1),
]

# ---------- Session state ----------
# Button click panna page marubadiyum load aagum. Adhunaala
# "form create aachu / summary aachu"-nu nyabagam vachukka idhu thevai.
if "form_created" not in st.session_state:
    st.session_state.form_created = False
if "summary_done" not in st.session_state:
    st.session_state.summary_done = False
if "form_title" not in st.session_state:
    st.session_state.form_title = ""

# ---------- Title ----------
st.title("FormGenie AI")
st.write("Type one sentence. Get a feedback form. Then get the summary of all answers.")

# ==========================================================
# STEP 1: Prompt type panra edam
# ==========================================================
st.header("1. Describe your form")
prompt = st.text_input(
    "What kind of form do you need?",
    value="Create a feedback form for our college hackathon",
)

if st.button("Create form", type="primary"):
    if prompt.strip() == "":
        st.error("Type what kind of form you need.")   # prompt kaali na error
    else:
        st.session_state.form_created = True
        st.session_state.summary_done = False
        st.session_state.form_title = prompt.strip()

# ---------- Form preview ----------
if st.session_state.form_created:
    with st.container(border=True):
        st.subheader(st.session_state.form_title)
        st.caption("Please share your honest feedback.")

        for q in sample_questions:
            if q["type"] == "rating":
                st.select_slider(q["text"], options=[1, 2, 3, 4, 5], value=3, key=q["text"])
            elif q["type"] == "text":
                st.text_input(q["text"], key=q["text"])
            else:
                st.text_area(q["text"], key=q["text"])

    # ==========================================================
    # STEP 2: Public link
    # ==========================================================
    st.header("2. Share the link")
    st.code("https://forms.gle/formgenie-demo", language=None)   # SAMPLE link
    st.caption(f"{len(sample_responses)} responses received so far.")

    # ==========================================================
    # STEP 3: Summary
    # ==========================================================
    st.header("3. See the summary")
    if st.button("Summarize responses"):
        st.session_state.summary_done = True

# ---------- Summary result ----------
if st.session_state.form_created and st.session_state.summary_done:
    # Positive / negative / neutral evlo-nu count pannurom
    total = len(sample_responses)
    pos = sum(1 for _, s in sample_responses if s == "positive")
    neg = sum(1 for _, s in sample_responses if s == "negative")
    neu = total - pos - neg

    c1, c2, c3 = st.columns(3)
    c1.metric("Positive", pos)
    c2.metric("Negative", neg)
    c3.metric("Neutral", neu)
    st.progress(pos / total, text=f"{round(pos / total * 100)}% positive")

    left, right = st.columns(2)
    with left:
        with st.container(border=True):
            st.subheader("Top 3 praises")
            for i, (title, count) in enumerate(sample_praises, start=1):
                st.write(f"{i}. {title} ({count} mentions)")
    with right:
        with st.container(border=True):
            st.subheader("Top 3 complaints")
            for i, (title, count) in enumerate(sample_complaints, start=1):
                st.write(f"{i}. {title} ({count} mentions)")python  --version
                