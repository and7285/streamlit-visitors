import streamlit as st
import time
import random

# --------------------
# Page config
# --------------------
st.set_page_config(
    page_title="Digital Trust",
    layout="wide"
)

# --------------------
# Global styles
# --------------------
st.markdown("""
<style>
.hero {
    background-color: #F6F7F9;
    padding: 96px 72px;
    border-radius: 28px;
}
.hero h1 {
    font-size: 52px;
    line-height: 1.15;
    font-weight: 700;
    margin-bottom: 24px;
}
.hero p {
    font-size: 18px;
    line-height: 1.6;
    color: #555;
    max-width: 520px;
}

.features {
    margin-top: 72px;
}
.feature-card {
    background-color: white;
    padding: 36px 32px;
    border-radius: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.04);
    height: 100%;
}
.feature-card h3 {
    font-size: 20px;
    margin-bottom: 12px;
}
.feature-card p {
    font-size: 15px;
    line-height: 1.6;
    color: #555;
}

.demo {
    margin-top: 96px;
    padding: 64px 72px;
    background-color: #0F172A;
    border-radius: 28px;
    color: white;
}
.demo h2 {
    font-size: 36px;
}
.demo p {
    color: #CBD5E1;
    max-width: 520px;
}

.report {
    margin-top: 48px;
    padding: 40px 48px;
    background-color: white;
    border-radius: 24px;
    box-shadow: 0 12px 32px rgba(0,0,0,0.06);
}
.signal {
    background-color: #F8FAFC;
    padding: 12px 16px;
    border-radius: 12px;
    margin-bottom: 8px;
    font-size: 14px;
}
.meta {
    font-size: 13px;
    color: #64748B;
    margin-top: 24px;
}
</style>
""", unsafe_allow_html=True)

# --------------------
# Hero Section
# --------------------
st.markdown('<div class="hero">', unsafe_allow_html=True)

left, right = st.columns([1.3, 1])

with left:
    st.markdown("""
    <h1>
        Your digital trust.<br/>
        Verified instantly.
    </h1>
    <p>
        AI that analyzes media artifacts inside and out to power high-impact
        security decisions.<br/>
        Detect deepfakes with <strong>99.9% accuracy</strong>.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)
    st.button("Get started")

with right:
    st.image(
        "https://placehold.co/600x420?text=AI+Security+Visual",
        use_container_width=True
    )

st.markdown('</div>', unsafe_allow_html=True)

# --------------------
# Feature Cards
# --------------------
st.markdown('<div class="features">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
        <h3>🛡️ Deepfake Detection</h3>
        <p>
            Detect manipulated media with industry-leading accuracy,
            identifying even subtle synthetic artifacts.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <h3>🔍 Media Integrity Analysis</h3>
        <p>
            Analyze images, videos, and audio inside and out
            to verify authenticity.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡ Instant Verification</h3>
        <p>
            Make high-impact security decisions in seconds
            with real-time analysis pipelines.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --------------------
# Demo Section
# --------------------
st.markdown('<div class="demo">', unsafe_allow_html=True)
l, r = st.columns([1.2, 1])

with l:
    st.markdown("""
    <h2>Try it yourself</h2>
    <p>
        Upload an image or video to instantly verify authenticity.
    </p>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload media",
        type=["png", "jpg", "jpeg", "mp4"],
        label_visibility="collapsed"
    )

    analyze = st.button("Analyze media")

with r:
    if uploaded_file:
        if uploaded_file.type.startswith("image"):
            st.image(uploaded_file, use_container_width=True)
        else:
            st.video(uploaded_file)

st.markdown('</div>', unsafe_allow_html=True)

# --------------------
# Result Report
# --------------------
def render_result(score: float):
    verdict = "Authentic" if score > 0.9 else "Potential Manipulation"
    color = "#16A34A" if score > 0.9 else "#DC2626"

    st.markdown('<div class="report">', unsafe_allow_html=True)

    st.markdown(
        f"<h2 style='color:{color};'>{verdict}</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p><strong>Confidence:</strong> {score*100:.2f}%</p>",
        unsafe_allow_html=True
    )

    st.progress(score)

    st.markdown("#### Key signals detected")

    signals = [
        "No GAN fingerprint patterns detected",
        "Consistent sensor noise",
        "Metadata structure intact"
    ] if score > 0.9 else [
        "Inconsistent facial landmarks",
        "Synthetic texture artifacts",
        "Anomalous compression patterns"
    ]

    for s in signals:
        st.markdown(f"<div class='signal'>• {s}</div>", unsafe_allow_html=True)

    st.markdown(
        "<div class='meta'>Analysis completed in 1.8s · Model v1.3</div>",
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

if analyze and uploaded_file:
    with st.spinner("Analyzing media artifacts..."):
        time.sleep(2)

    score = random.uniform(0.1, 0.99)
    render_result(score)
